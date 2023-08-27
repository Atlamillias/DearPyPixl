import re
import ast
import sys
import types
import inspect
import itertools  # type: ignore
import dataclasses
from inspect import Parameter
from types import ModuleType
from typing import (
    MutableMapping,
    TypeVar,
    Iterable,
    Sequence,
    Mapping,
    Any,
    Callable,
    Self,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from .interface import AppItemType



_T = TypeVar('_T')


# [ STRING FORMATTING ]

class _IndentedStrType(type):
    __slots__ = ()

    def indent(self) -> None:
        self.level += 1

    def dedent(self) -> None:
        self.level -= 1
        if self.level < 0:
            self.level = 0

    def __enter__(self):
        self.indent()

    def __exit__(self, *args):
        self.dedent()

class indent(str, metaclass=_IndentedStrType):
    __slots__ = ()

    __indent: str = ' ' * 4

    level: int = 0

    def __new__(cls, s: str, level: int | None = None) -> str:
        return cls.__indent * (level or cls.level) + s or ''

    @classmethod
    def lines(cls, s: str, level: int, *, sep: str = '\n') -> str:
        indent = cls.__indent * (level or cls.level)
        return indent + indent.join(s.split(sep))


# >>> re.findall('vector: collections.abc.Sequence[int | typing.Any]')
# ['collections.abc.S', 'typing.A']
_RE_PTRN_TPLOOKUP = re.compile(r'(?:(?::\s?)|(?:\[)|(?:\s*\|\s*)\s?)((?:(?:\w*\.)(?:\w))+)')

def _rm_source_anno_namespaces(s: str) -> str:
    """Removes dotted namespace lookup prefixes from signatures and
    annotations of Python source code.

        >>> clean_source_annotations('vector: collections.abc.Sequence[int | typing.Any]')
        'vector: Sequence[int | Any]'

    """
    # This should not remove namespace lookup strings elseware, but
    # needs more testing. Unused for now.
    for hit in set(re.findall(_RE_PTRN_TPLOOKUP, s)):
        try:
            # the pattern isn't perfect -- matches also include
            # the char after the last dot
            s = s.replace(hit[:-1], "")
        except IndexError:
            pass
    return s


_RE_PTRN_NSPFX = r'((?:(?:\w*\.))+)'

def trim_lookup_trail(s: str) -> str:
    """Removes dotted namespace lookup prefixes in a
    Python source code string."""
    # Unlike the *other* one, this one is rather...indescriminate
    # when it comes to matches.
    for hit in set(re.findall(_RE_PTRN_NSPFX, s)):
        s = s.replace(hit, "")
    return s


def uneval(tp: type | str | None) -> str:
    """Return a string that would evaluate to the passed type or
    annotation of that type when compiled as source code."""
    return inspect.formatannotation(tp)


def object_annotation(o: Any) -> str:
    """Return a string that would evaluate to the passed type or
    annotation of that type when compiled as source code if
    available in the would-be namespace."""
    return trim_lookup_trail(uneval(o))




# [ PARSERS / WRITERS ]

def _get_module(module: str | types.ModuleType) -> types.ModuleType:
    if isinstance(module, str):
        try:
            return sys.modules[module]
        except KeyError:
            raise ValueError(
                f"{module!r} is not the name of an imported module."
            ) from None
    assert isinstance(module, types.ModuleType)
    return module


@dataclasses.dataclass(init=False)
class Exported(MutableMapping):
    """A mapping containing names and objects to export to stub files.

    Flagging objects for export:
        >>> exported = Exported(__name__)  # `ModuleType` object also works
        ...
        >>> @exported  # uses `PublicClass.__qualname__` as the key
        >>> class PublicClass: ...
        ...
        >>> @exported  # uses `public_func.__name__` as the key
        >>> def public_func(): ...
        ...
        >>> # passing an explicit name
        >>> exported(public_func, "alias_of_public_func")

    Getting exports from a module:
        >>> # the module must have been imported prior
        >>> exports = Exported.fetch(__name__)  # `ModuleType` object also works

    """

    module: str | types.ModuleType

    __slots__ = ("_module", "_cache")

    EXPORTED = '__exported__'

    def __init__(self, module: str | types.ModuleType):
        self._cache  = {}
        self._module = _get_module(module)
        setattr(self._module, self.EXPORTED, self)

    def __getitem__(self, key: str):
        return self._cache[key]

    def __setitem__(self, key: str, value: Any):
        self._cache[key] = value

    def __delitem__(self, key: str):
        del self._cache[key]

    def __iter__(self):
        return iter(self._cache)

    def __len__(self):
        return len(self._cache)

    def export(self, o: _T | None = None, /, name: str = '') -> _T:
        def capture_object(o: _T) -> _T:
            nonlocal name
            if not name:  # type: ignore
                try:
                    name = o.__qualname__  # type: ignore
                except AttributeError:
                    name = o.__name__   # type: ignore
            self._cache[name] = o
            return o
        if o is None:
            return capture_object  # type: ignore
        return capture_object(o)

    __call__ = export

    @classmethod
    def fetch(cls, module: types.ModuleType) -> Mapping[str, Any]:
        """Return a mapping of a module's exports."""
        module = _get_module(module)
        return types.MappingProxyType(getattr(module, cls.EXPORTED, {}))



@dataclasses.dataclass(slots=True)
class Imported(Sequence):
    module  : str | ModuleType
    sorted  : bool       = True
    absolute: bool       = False
    relative: bool       = True

    _name_map: dict[Any, str] = dataclasses.field(init=False, repr=False)
    _imports : list[Any]      = dataclasses.field(init=False, repr=False)
    _exports : list[Any]      = dataclasses.field(init=False, repr=False)

    def __post_init__(self):
        self.module    = _get_module(self.module)
        self._imports  = []
        self._exports  = []   # "exported" imports need to be followed up with an alias "obj as obj"
        self._name_map = {}
        self._build_name_map()

    def _build_name_map(self):
        self._name_map.clear()
        for k, v in self.module.__dict__.items():
            try:
                self._name_map[v] = k
            except TypeError:
                continue

    def __getitem__(self, key: int) -> Any:
        return NotImplemented

    def __len__(self):
        return len(self._imports) + len(self._exports)

    def __iter__(self):
        yield from itertools.chain(self._imports, self._exports)

    def __str__(self) -> str:
        stmt = []
        src  = self.module.__name__  # type: ignore
        if self.absolute and self.relative:
            if not self._imports:
                return ''
            stmt.append(f"from {src} import (")
        elif self.relative:
            if not self._imports:
                return ''
            stmt.append(f'from .{src.split(".", maxsplit=1)[-1]} import (')
        else:
            return f'import {src}'

        imports = []
        for o in self._imports:
            imports.append(f"    {self._name_map[o]},")
        for o in self._exports:
            o_name = self._name_map[o]
            imports.append(f"    {o_name} as {o_name},")

        if self.sorted:
            imports.sort()

        stmt.extend(imports)
        stmt.append(")")
        return '\n'.join(stmt)

    @property
    def imports(self) -> tuple[Any]:
        return tuple(self._imports)

    @property
    def exports(self) -> tuple[Any]:
        return tuple(self._exports)

    def copy(self) -> Self:
        copy = type(self)(self.module, self.sorted, self.absolute, self.relative)
        copy._imports = self._imports.copy()
        return copy

    def append(self, value: Any, *, export: bool = False):
        if export:
            self._exports.append(value)
            if value in self._imports:
                self._imports.remove(value)
        else:
            self._imports.append(value)
            if value in self._exports:
                self._exports.remove(value)

    def extend(self, iterable: Iterable[Any], *, export: bool = False):
        for v in iterable:
            self.append(v, export=export)




def validate_source(s: str) -> str:
    """Validate a Python source code string.

    Returns the string unchanged if the source is valid. Throws
    various errors otherwise.
    """
    ast.parse(s)
    return s


def to_source_classdef(tp: type) -> str:
    """Return a source code string containing the preliminary
    class definition of a type.
    """
    src = [
        f"class {tp.__qualname__}({', '.join(b.__qualname__ for b in tp.__bases__)}):"
    ]
    with indent:
        if tp.__doc__:
            src.append(indent('"""') + tp.__doc__  + '\n    """')

        if '__slots__' in tp.__dict__:
            slots = tp.__slots__  # type: ignore
            if slots:
                src.append(indent('__slots__: tuple[str, ...] = ('))
                with indent:
                    mbrs = ''.join(
                        ",\n".join(indent(repr(m)) for m in slots)
                    )
                    src.append(mbrs)
                src.append(indent(")"))
            else:
                src.append(indent('__slots__: tuple[str, ...] = ()'))
    return '\n'.join(src)


def to_source_parameters(parameters: Mapping[str, Parameter]) -> str:
    """Return a source code string containing the argument
    signature of a callable.
    """
    src = []

    mk_pos_only = False
    mk_kwd_only = False
    for p in parameters.values():
        if p.annotation is p.empty:
            src_string = p.name
        else:
            src_string = f"{p.name}: {trim_lookup_trail(uneval(p.annotation))}"
        if p.default is not p.empty:
            src_string = f"{src_string} = ..."

        kind = p.kind

        if kind == p.POSITIONAL_ONLY:
            mk_pos_only = True
            src.append(src_string)
            continue
        elif mk_pos_only:
            mk_pos_only = False
            src_string = f"/, {src_string}"

        if kind == p.VAR_POSITIONAL:
            # Arguments following VAR_POSITIONAL are made KEYWORD_ONLY
            # by way of Python syntax. In this case, however, the lone
            # "*" marker is not needed.
            mk_kwd_only = True
        elif kind == p.KEYWORD_ONLY and not mk_kwd_only:
            src_string  = f"*, {src_string}"
            mk_kwd_only = True
        elif kind == p.VAR_KEYWORD:
            src_string  = f"**{src_string}"

        src.append(src_string)

    return ', '.join(src)


def to_source_function(fn: Callable, signature: inspect.Signature | None = None) -> str:
    """Return a source code string containing the definition and
    signature of a function.
    """
    signature = signature or inspect.signature(fn)
    if signature.return_annotation is signature.empty:
        return_tp = 'None'
    else:
        return_tp = trim_lookup_trail(uneval(signature.return_annotation))
    return f"def {fn.__name__}({to_source_parameters(signature.parameters)}) -> {return_tp}: ..."
