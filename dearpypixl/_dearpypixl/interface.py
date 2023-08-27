import abc
import sys
import uuid
import inspect
import functools
from inspect import Parameter
from dearpygui import dearpygui, _dearpygui
from . import api, common, constants, tools, errors, parsing, mkstub
from .api import Item as ItemAPI, Registry as RegistryAPI, _create_uuid
from .tools import classproperty
from .common import (
    Item,
    ItemInterface,
    ItemCommand,
    ItemConfig,
    ItemInfo,
    ItemState,
    null_itemtype,
    null_command,

    Color,
    Any,
    Self,
    Array,
    Callable,
    Iterator,
    Literal,
    Iterable,
    Generic,
    Mapping,
    Property,
    Sequence,
    SupportsIndex,
    final,
    overload,

    TypedDict,
    TypeVar,
    ParamSpec,

    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from ..items import mvTheme, mvFont, mvItemHandlerRegistry




_T = TypeVar("_T")
_P = ParamSpec("_P")

_ITP = TypeVar("_ITP", bound='AppItemType')


_exported = mkstub.Exported(__name__)




# [ METACLASS HELPERS ]

def _is_default_command(value: Any) -> bool:
    if isinstance(value, (staticmethod, classmethod)):
        value = value.__wrapped__
    return bool(value is null_command)


def _incompatible_bases(command: ItemCommand, identity: tuple[int, str], *bases: type['AppItemType | Any']) -> bool:
    """Return True if a new item type from *bases* would
    create an incompatible union between two or more Dear
    PyGui item types.
    """
    try:
        bases = tuple(b for b in bases if issubclass(b, AppItemType))
    except NameError:
        return False
    commands = {
        b.command if not isinstance(b.command, (classmethod, staticmethod))
        else b.command.__wrapped__
        for b in bases
    }
    commands.add(command)
    commands.discard(null_command)
    identities = {b.identity for b in bases}
    identities.add(identity)
    identities.discard(null_itemtype)
    return any(len(s) > 1 for s in (commands, identities))


def _register_itemtype(cls: Any, *, register: bool | None):
    if (
        register is True
        or register is not False and not cls.__qualname__.startswith("_")
    ):
        AppItemMeta.__itemtype_registry__[cls.identity[1]] = cls


def _get_itp_subclasses(*parent_cls: type[_T]) -> tuple[type[_T]]:
    return tuple(
        cls for cls in AppItemMeta.__itemtype_registry__.values()
        if issubclass(cls, parent_cls)
    )


def _create_init_method(cls: Any, parameters: Mapping[str, Parameter]) -> Any:
    method = tools.create_function(
        '__init__',
        ('self', '*args', 'tag: int | str = 0', '**kwargs'),
        (
            "super(__class__, self).__init__()",
            "try:",
            "    self.command(*args, tag=self, **kwargs)",
            "except (SystemError, TypeError) as e:",
            # BUG: The patch applied in __init__.py revealed that DPG will still
            # sometimes register foreign `tag`s even when throwing an argument-related
            # `SystemError`s (the patch ensures a `tag` is always sent so they're never
            # internally generated i.e. are always 'foreign'). In fact, the item is
            # still created in cases where no arguments are actually required. In any
            # case, it scuffs "does item exist" checks. Explicit `tag`s are *usually*
            # sent without arguments, and can be used as a decent `does_item_exist`
            # substitute.
            f"    if not errors.{errors.does_item_exist.__name__}(self) or (not tag and (args or kwargs)):",
            f"        err_chks = (",
            f"            errors.{errors.err_arg_unexpected.__name__},",
            f"            errors.{errors.err_parent_invalid.__name__},",
            f"        )",
            f"        for err_chk in err_chks:",
            f"            err = err_chk(self, self.command, *args, **kwargs)",
            f"            if err:",
            f"                self.destroy()",
            f"                raise err from None",
            f"        self.destroy()",
            f"        raise",
        ),
        None,
        locals={
            '__class__': cls,
            'errors'   : errors,
        }
    )
    method.__name__      = '__init__'
    method.__qualname__  = f'{cls.__qualname__}.__init__'
    method.__signature__ = inspect.Signature(
        [Parameter('self', Parameter.POSITIONAL_OR_KEYWORD), *parameters.values()],
        return_annotation=None,
    )
    command = cls.command
    if command.__defaults__:
        method.__defaults__ = tuple(command.__defaults__)
    if command.__kwdefaults__:
        method.__kwdefaults__ = dict(command.__kwdefaults__)
    method.__annotations__.clear()
    for p in method.__signature__.parameters.values():
        if p.annotation is not p.empty:
            method.__annotations__[p.name] = p.annotation
    return method


def _create_configure_method(cls: Any, parameters: Mapping[str, Parameter]) -> Any:
    """Generate and return a new `.configure` method using item
    command parameters."""
    method = tools.create_function(
        'configure',
        ('self', '**kwargs'),
        (
            "try:",
            "    configure_item(self, **kwargs)",
            "except SystemError:",
           f"    err = errors.{errors.err_item_nonexistant.__name__}(self, self.command, **kwargs)",
            "    if err: raise err from None",
            "    bad_kwds = ', '.join(repr(k) for k in kwargs if k not in _ITEM_CFG_KEYS)",
            "    if bad_kwds:",
            "        raise TypeError(",
            "            f'`{type(self).__qualname__}.configure()` received '",
            "            f'unexpected keyword argument(s) {bad_kwds}.'",
            "        ) from None",
            "    for k,v in kwargs.items():",
            "        try:",
            "            configure_item(self, **{k:v})",
            "        except SystemError:",
            "            raise TypeError(",
            "                f'configuration key {k!r} of {type(self).__qualname__!r} interface '",
            "                'is read-only.'",
            "            ) from None",
        ),
        None,
        locals={
            '__class__'       : cls,
            'errors'          : errors,
            'configure_item'  : _dearpygui.configure_item,
            '_ITEM_CFG_KEYS'  : frozenset(parameters),
        }
    )
    method.__name__      = "configure"
    method.__qualname__  = f'{cls.__qualname__}.configure'
    method.__signature__ = inspect.Signature(
        parameters=[
            Parameter('self', Parameter.POSITIONAL_OR_KEYWORD),
            *(p.replace(default=...) for p in parameters.values()),
            Parameter('kwargs', Parameter.VAR_KEYWORD),
        ],
        return_annotation=None,
    )
    method.__annotations__.clear()
    for p in method.__signature__.parameters.values():
        if p.annotation is not p.empty:
            method.__annotations__[p.name] = p.annotation
    return method


def _create_configuration_method(cls: Any, parameters: Mapping[str, Parameter]) -> Any:
    """Generate and return a new `.configuration` method using item
    command parameters."""
    return_annotation = eval(
        f'dict[Literal[{", ".join(repr(p) for p in parameters)}], Any]',
        globals(),
        locals(),
    )
    method = tools.create_function(
        'configuration',
        ('self',),
        (
            f"try:",
            f"    return {{",
            f"        k:v for k,v in get_item_configuration(self).items()",
            f"        if k in _ITEM_CFG_KEYS",
            f"    }}",
            f"except SystemError:",
            f"    err = errors.{errors.err_item_nonexistant.__name__}(self, self.command)",
            f"    if err: raise err from None",
            f"    raise",
        ),
        return_annotation,
        locals={
            '__class__'             : cls,
            'errors'                : errors,
            'get_item_configuration': _dearpygui.get_item_configuration,
            '_ITEM_CFG_KEYS'        : frozenset(parameters),
        },
    )
    method.__name__      = 'configuration'
    method.__qualname__  = f'{cls.__qualname__}.configuration'
    method.__signature__ = inspect.Signature(
        parameters=[
            Parameter('self', Parameter.POSITIONAL_OR_KEYWORD),
        ],
        return_annotation=return_annotation,
    )
    method.__annotations__.clear()
    for p in method.__signature__.parameters.values():
        if p.annotation is not p.empty:
            method.__annotations__[p.name] = p.annotation
    return method


# [ ITEM META & BASE ]

_AppT = TypeVar("_AppT", bound=api.Application)
_VpT  = TypeVar("_VpT", bound=api.Viewport)
_RtT  = TypeVar("_RtT", bound=api.Runtime)

class _GlobalStateObject(Generic[_T]):
    __slots__ = ("_key",)

    def __init__(self, key: str = '', /):
        self._key = key

    def __set_name__(self, cls: Any, name: str):
        self._key = self._key or f"_{name}"

    def __get__(self, instance: Any, cls: Any = None) -> _T | None:
        if instance is None:
            return self  # type: ignore
        getattr(AppItemMeta, self._key, None)

    def __set__(self, instance: Any, value: _T) -> None:
        setattr(AppItemMeta, self._key, value)



class AppItemMeta(type):
    __slots__ = ()

    __itemtype_registry__ = api.Registry.__itemtype_registry__

    identity: tuple[int, str] = null_itemtype
    command : ItemCommand     = null_command

    def __new__(
        mcls,
        name     : str,
        bases    : tuple[type[object], ...],
        namespace: dict[str, Any],
        *,
        identity: tuple[int, str] | None  = None,  # type: ignore
        command : ItemCommand | None = None,  # type: ignore
        register: bool | None        = None,  # None == 'auto', True == 'force register', False == 'do not register'
        **kwargs
    ):
        command : Any = namespace.get("command", command)
        identity: Any = namespace.get("identity", identity)

        if command and not _is_default_command(command):
            if parsing.is_contextmanager(command):
                command = command.__wrapped__
            if not parsing.is_item_command(command):
                if callable(command):
                    raise ValueError(f'{command!r} is not a valid item command.')
                raise TypeError(f'{command!r} is not callable.')
        if identity and identity == null_itemtype:
            try:
                int_id, str_id = identity
                if not (isinstance(int_id, int) and isinstance(str_id, str)):
                    raise TypeError
            except TypeError:
                raise TypeError(
                    f'`identity` must be a 2-tuple containing an '
                    f'integer and string value respectively (got {identity!r}).'
                ) from None

        cls = super().__new__(mcls, name, bases, namespace, **kwargs)

        # XXX: `__bool__` is purposefully undefined for all interfaces. It
        # must ALWAYS point to `int.__bool__` or eval to `bool(self.tag)`
        # because the Python C-API hooks used by DPG rely on it. If it's
        # falsy, the `tag` value of the interface is treated as 0.
        if issubclass(cls, int) and getattr(cls, '__bool__') is not int.__bool__:
            raise TypeError(
                f'derived item interface types cannot override `__bool__`.'
            )

        if all((command, identity)):  # try to process as a new base item type
            cls.identity = identity
            cls.command  = (
                staticmethod(command)
                if not isinstance(command, staticmethod)
                else command
            )
            if _is_default_command(command) or identity == null_itemtype:
                # early exit for primitive bases
                return cls

            if _incompatible_bases(command, identity, *bases):
                raise TypeError(
                    f"cannot create class {name!r} -- incompatible union of bases."
                )

            tp_def = parsing.item_definitions()[
                cls.identity[1].removeprefix("mvAppItemType::")
            ]

            # these methods are built only once per base type
            if getattr(cls, '__init__', object.__init__) is object.__init__:
                setattr(cls, '__init__', _create_init_method(cls, tp_def.init_parameters))
            if getattr(cls, "configure", api.Item.configure) is api.Item.configure:
                setattr(cls, 'configure', _create_configure_method(cls, tp_def.config_parameters))
            if getattr(cls, "configuration", api.Item.configuration) is api.Item.configuration:
                setattr(cls, 'configuration', _create_configuration_method(cls, tp_def.config_parameters))

            # set missing configuration descriptors
            for kwd in tp_def.config_parameters:
                if hasattr(cls, kwd):
                    continue
                config_desc = ItemConfig()
                setattr(cls, kwd, config_desc)
                config_desc.__set_name__(cls, kwd)  # type: ignore

            _register_itemtype(cls, register=register)

        elif register is True:
            _register_itemtype(cls, register=register)

        return cls

    def __repr__(self) -> str:
        return f"<class {self.__qualname__!r}>"

    def __hash__(self):
        return hash((self.__name__, self.__module__, *self.identity))

    def __eq__(self, other: Any):
        # Being very explicit w/*other* typing here to prevent
        # unexpected results in niche cases.
        if isinstance(other, str) and other.startswith("mvAppItemType::"):
            return self.identity[1] == other
        if type(other) is int:
            return self.identity[0] == other
        return other is self

    def __str__(self) -> str:
        return self.identity[1]

    def __int__(self) -> int:
        return self.identity[0]

    application: Property[_AppT | None] = _GlobalStateObject()  # type: ignore
    viewport   : Property[_VpT  | None] = _GlobalStateObject()  # type: ignore
    runtime    : Property[_RtT  | None] = _GlobalStateObject()  # type: ignore

    def start(self, *args, **kwargs) -> Any:
        """Start the user interface event loop, blocking the thread until
        the viewport is closed.

        This method forwards the call to `self.runtime.start`. If a
        `Runtime` object has not yet been set, an internal default
        `.start` method is called instead. The default implementation
        performs all required setup, if not done so already.
        """
        rt = self.runtime
        if rt is None:
            rt = api.Runtime
        return rt.start(*args, **kwargs)

    def stop(self, *args, **kwargs) -> Any:
        """Close the viewport and kill the runtime.

        This method forwards the call to `self.runtime.stop`. If a
        `Runtime` object has not yet been set, an internal default
        `.stop` method is called instead.
        """
        rt = self.runtime
        if rt is None:
            rt = api.Runtime
        return rt.stop(*args, **kwargs)


class ABCAppItemMeta(AppItemMeta, abc.ABCMeta):
    """Metaclass for creating abstract app item interface types."""





# [ `AppItemType` HELPERS ]

def _onetime_setup(fn: _T) -> _T:
    """`AppItemType.__new__ wrapper`. Performs application-level setup
    once.
    """
    @functools.wraps(fn)  # type: ignore
    def application_setup(*args, **kwargs):
        if not api.Application.state()['ok']:
            api.Application.create_context()
            api.Application.prepare()
        obj = fn(*args, **kwargs)  # type: ignore
        AppItemType.__new__ = fn  # type: ignore
        return obj
    return application_setup  # type: ignore


def _get_base_itp(item: Item, information: common.ItemInfoDict | None = None):
    return AppItemMeta.__itemtype_registry__[
        (information or ItemAPI.information(item))['type']
    ]


_Reduced = tuple[
    Callable[..., _ITP],
    tuple[type[_ITP], tuple[Any, ...], dict[str, Any]],
    '_SaveState',
    Iterator[Any] | None,
    Iterator[tuple[str, Any]] | None,
    Callable[[_ITP, '_SaveState'], _ITP],
]

class _SaveState(TypedDict):
    alias         : str
    type          : str
    parent        : int | str | None
    theme         : Any
    font          : Any
    handlers      : Any
    children      : tuple[list[Any], list[Any], list[Any], list[Any]]
    configuration : dict[str, Any]
    value         : Any
    itf_state     : dict[str, Any] | None
    itf_state_keys: tuple[str, ...]

def _to_save_state(item: 'AppItemType', info: common.ItemInfoDict | None = None, **kwargs) -> _SaveState:
    info   = info or item.information()
    config = item.configuration()
    pos    = item.state()['pos']
    if pos and any(v > 0 for v in pos):
        config['pos'] = pos
    config.update(kwargs)

    return {
        "alias"         : item.get_alias(),
        "type"          : info["type"],
        "parent"        : info["parent"],
        "theme"         : info["theme"],
        "font"          : info["font"],
        "handlers"      : info["handlers"],
        "children"      : tuple(info['children'].values()),
        "configuration" : config,                             # type: ignore
        "value"         : item.get_value(),
        # these are set by things that use them
        "itf_state"     : None,
        "itf_state_keys": (),
    }

def _load_reduced(item: 'AppItemType', save_state: _SaveState):
    """Loader for reduced/pickled item interfaces."""
    # The interface state is restored first because the
    # relationship of the item and `source` are unknown.
    # This gives every opportunity to ensure it exists.
    itf_state = save_state['itf_state']
    if itf_state:
        for k in save_state['itf_state_keys']:
            newfn, newargs, ss, *_, loader = itf_state[k]
            newcls, newargs, newkwds = newargs
            itf = newfn(newcls, *newargs, **newkwds)
            loader(itf, ss)
        setstate = getattr(item, '__setstate__', None)
        if setstate:
            setstate(itf_state)
        else:
            for k, v in itf_state.items():
                setattr(item, k, v)

    # Re-create the item state. The check sort of acts
    # as a memo map; reducing the chances of creating
    # interfaces of items already re-created.
    alias = save_state['alias']
    if not RegistryAPI.item_exists(alias):
        parent = save_state['parent']
        if parent:
            item.command(tag=item, parent=parent)
        else:
            item.command(tag=item)
        item.set_alias(alias)

        for k in ('theme', 'font', 'handlers'):
            reduced = save_state[k]
            if reduced:
                newfn, newargs, ss, *_, loader = reduced
                newcls, newargs, newkwds = newargs
                itf = newfn(newcls, *newargs, **newkwds)
                loader(itf, ss)
                getattr(item, f'set_{k}')(itf)

        for slot in save_state['children']:
            for reduced in slot:
                newfn, newargs, ss, *_, loader = reduced
                newcls, newargs, newkwds = newargs
                itf = newfn(newcls, *newargs, **newkwds)
                ss['parent'] = alias
                loader(itf, ss)

        config = save_state['configuration']
        # If `source` has any ('physical'?) ties to this
        # interface/item, it should exist by now.
        source = config.get('source', 0)
        if source and not RegistryAPI.item_exists(source):
            raise RuntimeError(
                f'{type(item).__name__!r} state loading error -- '
                f'`source` item {source!r} does not exist.'
            )
        else:
            item.set_value(save_state['value'])
        ItemAPI.configure(item, **config)

    return item


# Interfaces need to be instances of the built-in `int` or `str` type
# to allow them to be used for `tag`, `item`, etc. arguments. This is
# because Dear PyGui uses `PyLong_Check` and `PyUnicode_Check` which
# takes a shortcut; checking the class' `tp_flags` instead of the
# normal `isinstance/issubclass` procedure.
@ItemInterface.register
class AppItemType(api.Item, int, register=False, metaclass=AppItemMeta):
    __slots__ = ()

    # [ CONSTRUCTORS ]


    @_onetime_setup
    def __new__(cls, *args, tag: Item = 0, **kwargs) -> Self:
        """Args:
            * tag: Item identifier, in-use or otherwise. If 0 or None, an
            integer identifier is automatically generated.

        NOTE: If an item would be created as a result of creating an
        interface, *tag* should not be a string alias.
        """
        if not tag:
            tag = _create_uuid()
        elif isinstance(tag, str):
            tag = RegistryAPI.get_item_uuid(tag)
            if not tag:
                # DPG's item registry API was never finished, so it's impossible
                # to register an alias and tell DPG to actually use the uuid
                # bound to the alias for the item. Basically; manually registering
                # aliases does absolutely nothing. A work-around is complicated,
                # so just use the alternate constructor.
                raise ValueError(
                    "using use the `.aliased` method "
                )
        return super().__new__(cls, tag)

    @classmethod
    def aliased(cls, *args, tag: Item, **kwargs) -> Self:
        """Alternate interface constructor that supports string aliases
        when creating both an interface and item.

        Args:
            * tag: Item identifier, in-use or otherwise. If 0 or None, an
            integer identifier is automatically generated.
        """
        if not isinstance(tag, str):
            return cls(*args, tag=tag, **kwargs)
        self = cls(*args, **kwargs)
        self.set_alias(tag)
        return self

    @classmethod
    def new(cls, tag: Item = 0) -> Self:
        """Return a new interface. The instance is not initialized.

        Args:
            * tag: Item identifier, in-use or otherwise. If 0 or None, an
            integer identifier is automatically generated.


        If the instance's tag value is unused, expect errors when using
        most of the instance-bound API. The instance can be initialized
        at any time by calling the `.__init__` or `.init` methods.

        The new instance returned by this method is created by directly
        calling the class' `__new__` method (using *args* and *kwargs*)
        without ever calling `__init__` and NOT through typical
        invocation.

        It is not necessary to hook through this method to create an
        interface for an existing item, since the default `__init__`
        implementation will handle the resulting exception. This method
        is more performant over the former when creating interfaces for
        several existing items.
        """
        return cls.__new__(cls, tag=tag)

    def init(self, *args, **kwargs):
        """Initialize or re-initialize the interface. If the instance's
        tag value is unused, a proper item will be created to validate
        the interface's existance.

        Args:
            * args: Positional arguments used to create the item.

            * kwargs: Keyword arguments used to create the item.


        Required arguments can be omitted if the interface's tag value
        is already in-use.
        """
        return self.__init__(*args, **kwargs)


    # [ BEHAVIORS ]

    def __repr__(self):
        return (
            f"{type(self).__qualname__}("
            f"tag={int(self)!r}, "
            f"alias={ItemAPI.get_alias(self)!r}, "
            f"label={ItemAPI.configuration(self)['label']!r}, "
            f"parent={ItemAPI.information(self)['parent']!r}"
            f")"
        )

    def __getitem__(self, index: Literal[0, 1, 2, 3] | slice) -> list[Item] | list[list[Item]]:
        slots = self.information()["children"]
        try:
            return slots[index]  # type: ignore
        except KeyError:
            raise IndexError(f"expected slot index, got {index!r}.") from None
        except TypeError:  # unhashable
            if isinstance(index, slice):
                return [*slots.values()][index.start: index.stop: index.step]  # type: ignore
            raise

    def __getnewargs_ex__(self):
        return (), {}

    def __reduce_ex__(self, protocol: int = -1) -> _Reduced:
        save_state = _to_save_state(self)

        alias = save_state['alias']
        if not alias:
            alias = save_state['alias'] = f'{self.tag}-{uuid.uuid4()}'
            self.set_alias(alias)

        for k in ('theme', 'font', 'handlers'):
            item = save_state[k]
            if item:
                save_state[k] = _get_base_itp(item).new(item).__reduce_ex__()

        for slot in save_state['children']:
            for i, child in enumerate(slot):
                slot[i] = _get_base_itp(child).new(child).__reduce_ex__()

        # When unpickled, the loader will inject the parent's
        # alias into a child's save state before loading it.
        # Clearing the existing parent here simply allows for
        # the top-level item take advantage of the container
        # stack when it is not a root item i.e.
        # `with Window(): pickle.load(...)`.
        save_state['parent'] = 0

        # `source` is extremely tricky to handle since it may
        # exist in a separate item branch. Ensure it has an alias
        # and hope for the best. Ideally, the user will pickle it
        # as well, and load beforehand. No worries if `source` is
        # a child of this item since the loader
        source = save_state['configuration'].get('source', 0)
        if source:
            _source = ItemAPI.get_alias(source)
            if not _source:
                _source = f'{source}-{uuid.uuid4()}'
                ItemAPI.set_alias(source, _source)
            save_state['configuration']['source'] = _source

        itf_state = save_state['itf_state'] = self.__getstate__()
        if itf_state:
            itf_state_keys = []
            for k, v in itf_state.items():
                # it falls upon the user to serialize anything else
                if isinstance(v, AppItemType):
                    itf_state[k] = v.__reduce_ex__()
                    itf_state_keys.append(k)
            save_state['itf_state_keys'] = tuple(itf_state_keys)

        cls = self.__class__
        return (
            cls.__new__,
            (cls, *self.__getnewargs_ex__()),
            save_state,
            None,
            None,
            _load_reduced,
        )

    __getstate__: Callable[..., dict[str, Any]]

    @overload
    def __copy__(self, **kwargs) -> Self: ...
    @overload
    def __copy__(self) -> Self: ...
    def __copy__(self, __save_state__: _SaveState | None = None, **kwargs) -> Self:
        copy_state = __save_state__ or _to_save_state(self, **kwargs)

        nargs, nkwds = self.__getnewargs_ex__()
        copy_item = self.__class__.__new__(self.__class__, *nargs, **nkwds)
        copy_item.command(tag=copy_item, **copy_state['configuration'])

        for k in ('font', 'theme', 'handlers'):
            item = copy_state[k]
            if item:
                getattr(copy_item, f"set_{k}")(item)

        if self.is_container:
            c_parent = copy_item
        else:
            c_parent = self
        for slot in copy_state['children']:
            for child in slot:
                child_info = ItemAPI.information(child)
                child_itf  = _get_base_itp(child).new(child)
                child_ss   = _to_save_state(child_itf, child_info)
                child_ss['configuration']['parent'] = c_parent
                child_itf.__copy__(parent=c_parent)

        itf_state = copy_state['itf_state']
        if itf_state:
            setstate = getattr(copy_item, '__setstate__', None)
            if setstate:
                setstate(copy_item, itf_state)
            else:
                for k,v in copy_state.items():
                    setattr(copy_item, k, v)

        return copy_item

    def __deepcopy__(self, memo: Any = None):
        return NotImplemented


    # [ GLOBAL STATE API ]

    # These are dependant on hooks being defined in two places; on
    # the metaclass, and below. They are read/write at the (non-meta)
    # class level, but read-only at the instance level. It falls upon
    # the user to set these at runtime, if they want. Otherwise they'll
    # simply return None.

    @property
    def application(self):
        """[get] Return the global `Application` object."""
        return AppItemMeta.application

    @property
    def viewport(self):
        """[get] Return the global `Viewport` object."""
        return AppItemMeta.viewport

    @property
    def runtime(self):
        """[get] Return the global `Runtime` object."""
        return AppItemMeta.runtime


    # [ CLASS-BOUND API ]

    identity: tuple[int, str] = null_itemtype
    command : ItemCommand     = null_command    # metaclass -> command = staticmethod(command)

    @classproperty
    def is_container(cls) -> bool:
        """[get] Return True if items of this type can contain other
        non-root items."""
        # A more accurate check would be to call `is_item_container`,
        # but that would require an existing item.
        return issubclass(cls, ContainerType)  # type: ignore

    @classproperty
    def is_root_item(cls) -> bool:
        """[get] Return True if items of this type cannot be parented.
        """
        return issubclass(cls, RootType)  # type: ignore

    @classproperty
    def is_plot_item(cls) -> bool:
        """[get] Return True if items of this type are included in Dear
        PyGui's plotting API."""
        return issubclass(cls, PlottingType)  # type: ignore

    @classproperty
    def is_node_item(cls) -> bool:
        """[get] Return True if items of this type are included in Dear
        PyGui's node API."""
        return issubclass(cls, NodeType)  # type: ignore

    @classproperty
    def is_theme_item(cls) -> bool:
        """[get] Return True if items of this type are included in Dear
        PyGui's theming API.
        """
        return issubclass(cls, ThemeType)  # type: ignore

    @classproperty
    def is_table_item(cls) -> bool:
        """[get] Return True if items of this type are included in Dear
        PyGui's table API."""
        return issubclass(cls, TableType)  # type: ignore

    @classproperty
    def is_draw_item(cls) -> bool:
        """[get] Return True if items of this type are included in Dear
        PyGui' drawing API."""
        return issubclass(cls, DrawingType)  # type: ignore

    @classproperty
    def target_slot(cls) -> Literal[0, 1, 2, 3]:
        """[get] Return the index of the child slot that would store
        items of this type.
        """
        # This is included as the 'target' key in the return value of
        # `get_item_information()`. But that requires an item to actually
        # exist.
        tp_name = cls.identity[1]
        if tp_name in (
            'mvAppItemType::mvFileExtension',
            'mvAppItemType::mvFontRangeHint',
            'mvAppItemType::mvNodeLink',
            'mvAppItemType::mvAnnotation',
            'mvAppItemType::mvDragLine',
            'mvAppItemType::mvDragPoint',
            'mvAppItemType::mvLegend',
            'mvAppItemType::mvTableColumn',
        ):
            slot = 0
        elif tp_name == 'mvAppItemType::mvDragPayload':
            slot = 3
        elif tp_name.startswith("mvAppItemType::mvDraw"):
            slot = 2
        else:
            slot = 1  # for root items, too
        return slot


    # [ INSTANCE-BOUND API ]

    @property
    def tag(self) -> int:
        """[get] Return the item's unique integer identifier."""
        return self.real

    @property
    def alias(self) -> str:
        """[get] Return the item's unique string identifier."""
        return self.get_alias()
    @alias.setter
    def alias(self, value: str | None) -> None:
        """[set] Set a unique string identifier for the item."""
        if value is None:
            alias = self.alias
            if alias is None:
                return
            return RegistryAPI.remove_alias(alias)
        return self.set_alias(value)

    # configuration members
    label             : Property[str | None] = ItemConfig()
    user_data         : Property[Any]        = ItemConfig()
    use_internal_label: Property[bool]       = ItemConfig()

    # information members
    @property
    def parent(self) -> 'mvAll | None':
        """[get] Return an interface for the item's parent, or None if
        the item is not parented.
        """
        parent = self.information()['parent']
        return mvAll(parent) if parent else parent  # type: ignore

    @property
    def theme(self) -> 'mvTheme | Item | None':
        """[get] Return the theme set onto the item."""
        theme = self.get_theme()
        try:
            return AppItemMeta.__itemtype_registry__['mvAppItemType::mvTheme'].new(
                theme
            ) if theme else theme
        except KeyError:
            return theme
    @theme.setter
    def theme(self, value: Item | None) -> None:
        """[set] Set the reflected theme item."""
        self.set_theme(value)

    @property
    def font(self) -> 'mvFont | Item | None':
        """[get] Return the font item in use."""
        font = self.get_font()
        try:
            return AppItemMeta.__itemtype_registry__['mvAppItemType::mvFont'].new(
                font
            ) if font else font
        except KeyError:
            return font
    @font.setter
    def font(self, value: Item) -> None:
        """[set] Set the reflected font item."""
        self.set_font(value)

    @property
    def handlers(self) -> 'mvItemHandlerRegistry | Item | None':
        """[get] Return the handler registry used by the item."""
        handlers = self.get_handlers()
        try:
            return AppItemMeta.__itemtype_registry__['mvAppItemType::mvItemHandlerRegistry'].new(
                handlers
            ) if handlers else handlers
        except KeyError:
            return handlers
    @handlers.setter
    def handlers(self, value: Item | None) -> None:
        """[set] Set an item handler registry for the item to use."""
        self.set_handlers(value)

    # state members
    is_ok                    : Property[bool | None]            = ItemState("ok")
    is_hovered               : Property[bool | None]            = ItemState("hovered")
    is_active                : Property[bool | None]            = ItemState("active")
    is_focused               : Property[bool | None]            = ItemState("focused")
    is_clicked               : Property[bool | None]            = ItemState("clicked")
    is_left_clicked          : Property[bool | None]            = ItemState("left_clicked")
    is_right_clicked         : Property[bool | None]            = ItemState("right_clicked")
    is_middle_clicked        : Property[bool | None]            = ItemState("middle_clicked")
    is_visible               : Property[bool | None]            = ItemState("visible")
    is_edited                : Property[bool | None]            = ItemState("edited")
    is_activated             : Property[bool | None]            = ItemState("activated")
    is_deactivated           : Property[bool | None]            = ItemState("deactivated")
    is_deactivated_after_edit: Property[bool | None]            = ItemState("deactivated_after_edit")
    is_resized               : Property[bool | None]            = ItemState("resized")
    rect_min                 : Property[Array[int, int] | None] = ItemState()
    rect_max                 : Property[Array[int, int] | None] = ItemState()
    rect_size                : Property[Array[int, int] | None] = ItemState()
    content_region_avail     : Property[Array[int, int] | None] = ItemState()

    # misc
    @property
    def value(self) -> Any:
        """[get] Return the item's stored value."""
        return self.get_value()
    @value.setter
    def value(self, value: Any) -> None:
        """[set] Set the item's value. Not all items can hold value."""
        self.set_value(value)

    @property
    def root_parent(self) -> 'mvAll | None':
        """[get] Return an interface for the item's top-level parent, or
        None if the item is a root item."""
        root_parent = super().root_parent()
        return mvAll(root_parent) if root_parent else root_parent  # type: ignore


class ABCAppItemType(AppItemType, metaclass=ABCAppItemMeta):
    """Abstract interface base class."""



@_exported
class mvAll(
    api.Window,  # needs to be before Table
    api.Table,
    api.Drawing,
    api.Plot,
    api.NodeEditor,
    api.Container,
    api.BasicItem,
    AppItemType,
):
    """Generic item interface with a constructor optimized for existing
    items. It features an expansive API, but lacks type identity and
    behavior unique to specific interface types.

    Unlike the typical item type constructor, `mvAll` will not generate
    any new identifiers. It accepts a sole (required) *tag* argument,
    with a strong preference of `int` identifiers.

    If *tag* is a `str` alias, it will try to fetch the related uuid.

    `mvAll` is the fallback interface for the `interface` function.

    The `mvAll` type has an integer value of 0.
    """
    __slots__ = ()

    def __new__(cls, tag: Item) -> Self:
        # I've tried every implementation under the sun trying to get
        # this to be as fast as possible. Only one exists, and the
        # extremely marginal gain isn't warrant given the straight-
        # forward approach. Even then, it was only a gain when `tag`
        # was actually an integer.
        if isinstance(tag, int):
            return int.__new__(cls, tag)
        return int.__new__(cls, RegistryAPI.get_item_uuid(tag))

    def __init__(self, tag: Item): ...

    def __enter__(self) -> Self:
        try:
            self.push_stack()
        except:
            raise TypeError(f"{type(self).__qualname__!r} is not a container item.")
        return self

    def __exit__(self, *args) -> None:
        self.pop_stack()

    # Identity-related class properties would always return False,
    # so they need to be re-implemented. Fortunately, class-level
    # insight isn't needed for this interface since the type itself
    # lacks identity.

    @property
    def is_container(self) -> bool:
        """[get] Return True if this item can contain other
        non-root items."""
        return self.information()['container']

    @property
    def is_root_item(self) -> bool:
        """[get] Return True if this item cannot be parented.
        """
        return self.information()['parent'] is not None

    @property
    def is_plot_item(self) -> bool:
        """[get] Return True if this item is included in Dear
        PyGui's plotting API."""
        tp_name = self.information()['type'].split("::", maxsplit=1)[-1]
        return tp_name.startswith('mvPlot') or tp_name == 'mvAnnotation'

    @property
    def is_node_item(self) -> bool:
        """[get] Return True if this item is included in Dear
        PyGui's node API."""
        tp_name = self.information()['type'].split("::", maxsplit=1)[-1]
        return tp_name.startswith('mvNode')

    @property
    def is_theme_item(self) -> bool:
        """[get] Return True if this item is included in Dear
        PyGui's theming API.
        """
        tp_name = self.information()['type'].split("::", maxsplit=1)[-1]
        return tp_name.startswith('mvTheme')

    @property
    def is_table_item(self) -> bool:
        """[get] Return True if this item is included in Dear
        PyGui's table API."""
        tp_name = self.information()['type'].split("::", maxsplit=1)[-1]
        return tp_name.startswith('mvTable')

    @property
    def is_draw_item(self) -> bool:
        """[get] Return True if this item is included in Dear
        PyGui' drawing API."""
        tp_name = self.information()['type'].split("::", maxsplit=1)[-1]
        return tp_name.startswith('mvDraw') or "Drawlist" in tp_name




# [ CORE COMPONENTS ]


# LOW-LEVEL CLASSIFICATION TYPES

@_exported
class BasicType(api.BasicItem, AppItemType):
    """Interface for basic non-container items."""
    __slots__ = ()


@_exported
class ContainerType(api.Container, AppItemType):
    """Interface for items that can contain others."""
    __slots__ = ()

    def __enter__(self) -> Self:
        self.push_stack()
        return self

    def __exit__(self, *args) -> None:
        self.pop_stack()

    @property
    def is_top_stack(self):
        return super().is_top_stack()


@_exported
class RootType(ContainerType):
    """Interface for top-level container items. Root items cannot be parented.
    """
    __slots__ = ()


@_exported
class RegistryType(RootType):
    __slots__ = ()



# HIGH-LEVEL CLASSIFICATION TYPES

@_exported
class HandlerType(api.BasicItem, AppItemType):
    """Interface for items that fire a callback given a certain event.
    """
    __slots__ = ()

    MouseInput = constants.MouseInput
    KeyInput   = constants.KeyInput


@_exported
class NodeType(AppItemType):
    __slots__ = ()

@_exported
class NodeEditorType(api.NodeEditor, NodeType):
    __slots__ = ()



@_exported
class ThemeType(AppItemType):
    __slots__ = ()


@_exported
class FontType(AppItemType):
    __slots__ = ()

    def text_size(self, text: str, *, wrap_width: int = -1):
        return ItemAPI.text_size(text, wrap_width=wrap_width, font=self)


@_exported
class DrawingType(api.Drawing, AppItemType):
    __slots__ = ()

@_exported
class DrawNodeType(api.DrawNode, DrawingType):
    __slots__ = ()


@_exported
class PlottingType(AppItemType):
    __slots__ = ()

@_exported
class PlotType(api.Plot, PlottingType):
    __slots__ = ()

@_exported
class PlotAxisType(api.PlotAxis, PlottingType):
    __slots__ = ()


@_exported
class TableType(AppItemType):
    __slots__ = ()

@_exported
class TableItemType(api.Table, TableType):
    __slots__ = ()


@_exported
class WindowType(api.Window, AppItemType):
    __slots__ = ()

    @property
    def x_scroll_max(self):
        return super().x_scroll_max()

    @property
    def x_scroll_pos(self):
        return self.get_x_scroll_pos()
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):
        self.set_x_scroll_pos(value)

    @property
    def y_scroll_max(self):
        return super().y_scroll_max()

    @property
    def y_scroll_pos(self):
        return self.get_y_scroll_pos()
    @y_scroll_pos.setter
    def y_scroll_pos(self, value: float):
        self.set_y_scroll_pos(value)

    @property
    def is_active_window(self) -> bool:
        """[get] Return True if this window or any of its' children are focused."""
        return self.tag == api.Viewport.active_window()



# FUNCTIONAL CLASSIFICATION TYPES
# (these do not inherit from a base API)

@_exported
class SupportsSized(AppItemType):
    """Interface for rendered items with a bounding box. They can be resized
    and explicitly positioned."""
    __slots__ = ()

    # Every item with `pos` has sizing support. However, they are not
    # always configured through the `width` and `height` keywords. This
    # covers the common case.

    width : Property[int] = ItemConfig()
    height: Property[int] = ItemConfig()

    # Some items like `mvWindowAppItem` only support `rect_size`. The min/max
    # for these can be easily calculated.
    @property
    def rect_min(self) -> Array[int, int]:
        state = self.state()
        try:
            return state["rect_min"]  # type: ignore
        except KeyError:
            return state["pos"]  # type: ignore

    @property
    def rect_max(self) -> Array[int, int]:
        state = self.state()
        try:
            return state["rect_max"]  # type: ignore
        except KeyError:
            config = self.configuration()
            x, y = state["pos"]  # type: ignore
            return x + config["width"], y + config["height"]  # type: ignore


@_exported
class SupportsValueArray(AppItemType, Generic[_T]):
    """Interface for items that can store an array of arbitrary size."""
    __slots__ = ()

    def get_value(self) -> list[_T]:
        return ItemAPI.get_value(self) or []

    def __add__(self, other: Iterable[_T]) -> Self:
        value = self.get_value()
        value.extend(other)
        self.set_value(value)
        return self

    __iadd__ = __add__

    def __mul__(self, other: int) -> Self:
        value = self.get_value()
        self.set_value(value * other)
        return self

    __imul__ = __mul__

    @overload
    def __getitem__(self, index: SupportsIndex, /) -> _T: ...
    @overload
    def __getitem__(self, slice: slice, /) -> list[_T]: ...
    def __getitem__(self, index: Any, /):
        return self.get_value()[index]

    def __setitem__(self, index: int, value: _T) -> None:
        item_value = self.get_value()
        item_value.__setitem__(index, value)
        self.set_value(item_value)

    def __delitem__(self, index: int):
        value = self.get_value()
        del value[index]
        self.set_value(value)

    def __contains__(self, value: _T):
        return value in self.get_value()

    def __reversed__(self):
        yield from reversed(self.get_value())

    def __str__(self):
        return self.get_value().__str__()

    def __len__(self):
        return self.get_value().__len__()

    def __iter__(self):
        return iter(self.get_value())

    def __lt__(self, other: Any):
        return self.get_value() < other

    def __le__(self, other: Any):
        return self.get_value() <= other

    def __eq__(self, other: Any):
        self.get_value()

    def __ge__(self, other: Any):
        self.get_value()

    def __gt__(self, other: Any):
        self.get_value()

    def count(self, value: Any) -> int:
        return self.get_value().count(value)

    def index(self, value: _T, start: int = 0, stop: int = sys.maxsize) -> int:
        return self.get_value().index(value, start, stop)

    def append(self, value: _T) -> None:
        """Add *value* to the end of this item's values."""
        item_value = self.get_value()
        item_value.append(value)
        self.set_value(item_value)

    def extend(self, iterable: Sequence[_T]) -> None:
        """Append values in *iterable* to this item's values."""
        item_value = self.get_value()
        item_value.extend(iterable)
        self.set_value(item_value)

    def pop(self, index: int = -1) -> _T:
        """Remove and return the last value at *index*."""
        item_value = self.get_value()
        value = item_value.pop(index)
        self.set_value(item_value)
        return value

    def insert(self, index: int, value: _T):
        """Insert *value* before *index*."""
        item_value = self.get_value()
        item_value.insert(index, value)
        self.set_value(item_value)

    def remove(self, value: _T):
        """Remove the first occurance of *value*."""
        item_value = self.get_value()
        item_value.remove(value)
        self.set_value(item_value)

    @overload
    def sort(self, /, *, key: Callable[[_T], Any] = ..., reverse: bool = ...) -> None: ...
    @overload
    def sort(self, /) -> None: ...
    def sort(self, /, **kwargs) -> None:
        """Sort values in-place."""
        item_value = self.get_value()
        item_value.sort(**kwargs)
        self.set_value(item_value)

    def reverse(self) -> None:
        """Reverse item values in-place."""
        self.set_value(self.get_value()[::-1])


@_exported
class SupportsCallback(AppItemType, Generic[_P, _T]):
    """Interface for items that support an optional callback.

    The callback can be invoked by calling the interface.which
    can be invoked by calling the item. They can also be passed
    as a callback-related argument for other items.
    """
    __slots__ = ()

    def __init_subclass__(cls):
        super().__init_subclass__()
        if '__call__' in cls.__dict__ and not '__code__' in cls.__dict__:
            setattr(cls, '__code__', getattr(cls, '__call__').__code__)

    @property
    def callback(self) -> Callable[_P, _T] | None:
        """[get] Return the item's assigned callback."""
        return self.configuration()["callback"]  # type: ignore
    @callback.setter
    def callback(self, value: Callable[_P, _T] | None) -> Callable | None:
        """[set] Set the item's callback."""
        self.configure(callback=value)
        return value

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> None:
        callback = self.callback
        if callback:
            callback(*args, **kwargs)

    __code__ = __call__.__code__




def itp_base_from_def(tp_def: parsing.ItemDefinition) -> type[AppItemType]:
    tp_name: str = tp_def.name # type: ignore
    reg_key = f'mvAppItemType::{tp_name}'

    # cached?
    if reg_key in AppItemMeta.__itemtype_registry__:
        cls = AppItemMeta.__itemtype_registry__[reg_key]

    else:
        params = inspect.signature(tp_def.command1).parameters

        ll_bases = []
        if "parent" not in params:
            if any(
                tp_def.command1.__name__.endswith(n) for n in ('_registry', 'theme')
            ):
                ll_bases.append(RegistryType)
            else:
                ll_bases.append(RootType)
        elif tp_def.is_container:
            ll_bases.append(ContainerType)
            ll_bases.append(BasicType)
        else:
            ll_bases.append(BasicType)

        hl_bases = []
        if tp_name == 'mvTable':
            hl_bases.append(TableItemType)
        elif tp_name.startswith("mvTable"):
            hl_bases.append(TableType)
        elif "Handler" in tp_name and not RegistryType in ll_bases:
            hl_bases.append(HandlerType)
        elif "Window" in tp_name:
            assert any(b in ll_bases for b in (ContainerType, RootType))
            hl_bases.append(WindowType)
        elif tp_name == 'mvDrawNode':
            hl_bases.append(DrawNodeType)
        elif tp_name.startswith('mvDraw') or "Drawlist" in tp_name:
            hl_bases.append(DrawingType)
        elif tp_name == 'mvFont':
            hl_bases.append(FontType)
        elif tp_name == "mvPlot":
            assert tp_def.is_container
            hl_bases.append(PlotType)
        elif tp_name == 'mvPlotAxis':
            hl_bases.append(PlotAxisType)
        elif any(n in tp_name for n in ("Plot", "Series", "mvAnnotation", "mvLegend")):
            hl_bases.append(PlottingType)
        elif tp_name == 'mvNodeEditor':
            hl_bases.append(NodeEditorType)
        elif tp_name.startswith("mvNode"):
            hl_bases.append(NodeType)
        if tp_name.startswith("mvTheme"):
            hl_bases.append(ThemeType)

        fn_bases = []
        if any(
            s in tp_def.command1.__name__
            for s in ("_series", "theme_color", "theme_style")
        ):
            fn_bases.append(SupportsValueArray)
        if all(p in params for p in ("pos", "width", "height")):
            fn_bases.append(SupportsSized)
        if "callback" in params:
            fn_bases.append(SupportsCallback)

        bases = [*fn_bases, *hl_bases, *ll_bases]
        class_body = {
            '__doc__'  : parsing.upd_command_doc(tp_def.command1),
            '__slots__': (),
        }

        cls = type(
            tp_name,
            tuple(bases),
            class_body,
            command=tp_def.command1,
            identity=(tp_def.enum, f"mvAppItemType::{tp_name}")
        )

        assert bases
        for b in cls.mro():
            if b in (object, int):
                continue
            assert hasattr(b, '__slots__')

    return cls  # type: ignore



# [ THEME ELEMENT COMPONENTS ]

class ThemeElementType(SupportsValueArray, BasicType, ThemeType):
    __slots__ = ()

    category: classproperty[constants.ThemeCategory]
    target  : classproperty[int]

    def __init__(self, tag: Item = 0, **kwargs):
        kwargs.update(
            category=self.category,
            target=self.target,
        )
        try:
            self.command(tag=self, **kwargs)
        except (SystemError, TypeError) as e:
            if not errors.does_item_exist(self) or (not tag and kwargs):
                err_chks = (
                    errors.err_arg_unexpected,
                    errors.err_parent_invalid,
                )
                for err_chk in err_chks:
                    err = err_chk(self, self.command, **kwargs)
                    if err:
                        self.destroy()
                self.destroy()
                raise


class ThemeColor(ThemeElementType, register=False):
    __slots__ = ()

    command  = dearpygui.add_theme_color
    identity = dearpygui.mvThemeColor, 'mvAppItemType::mvThemeColor'

    @overload
    def __init__(self, value: Color, /, **kwargs) -> None: ...
    @overload
    def __init__(self, r: int, g: int, b: int, a: int = 255, /, **kwargs) -> None: ...
    def __init__(self, value: Any, /, *args: int, tag: Item = 0, **kwargs) -> None:
        super().__init__(value=value if not args else (value, *args), **kwargs)


class ThemeStyle(ThemeElementType, register=False):
    __slots__ = ()

    command  = dearpygui.add_theme_style
    identity = dearpygui.mvThemeStyle, 'mvAppItemType::mvThemeStyle'

    def __init__(self, x: float = 1, y: float = -1, **kwargs) -> None:
        super().__init__(x=x, y=y, **kwargs)


def itp_theme_element_from_def(tp_def: parsing.TElemDefinition) -> type[ThemeElementType]:
    category = constants.ThemeCategory(tp_def.category)

    if tp_def.type == tp_def.COLOR:
        tp_base = ThemeColor
    else:
        assert tp_def.type == tp_def.STYLE
        tp_base = ThemeStyle

    name = tp_def.name \
        .replace("_", "") \
        .replace("Background", "Bg") \
        .replace("bg", "Bg")

    return type(  # type: ignore
        name,
        (tp_base,),
        {
            "__slots__": (),
            "category" : classproperty(lambda cls, *, _category=category: _category),
            "target"   : classproperty(lambda cls, *, _target=tp_def.enum: _target),
        },
        register=False
    )





# [ PUBLIC FUNCTIONS ]

@_exported
def interface(item: Item, *, initialize: bool = False, default_itp: type[_ITP] = mvAll) -> AppItemType | _ITP:
    """Return a proper `AppItemType` interface for an existing item
    based on its' internal type.

    Args:
        * item: Reference to an existing item.

        * initialize: If True, the interface's `__init__` method will
        be called during its creation. Default is False.

        * default_itp: Used as a fallback if a more specific interface
        type for the item cannot be found.
    """
    itp = AppItemMeta.__itemtype_registry__.get(
        ItemAPI.information(item)["type"],
        default_itp,
    )
    if initialize:
        return itp.new(item)
    return itp(tag=item)


@_exported
def registry_types() -> tuple[type[RegistryType]]:
    """Return all registry-type item classes."""
    return _get_itp_subclasses(RegistryType)


@_exported
def root_types() -> tuple[type[RootType]]:
    """Return all root-type item classes."""
    return _get_itp_subclasses(RootType)


@_exported
def container_types() -> tuple[type[ContainerType]]:
    """Return all container-type item classes."""
    return _get_itp_subclasses(ContainerType)


@_exported
def basic_types() -> tuple[type[BasicType]]:
    """Return all non-container type item classes."""
    return _get_itp_subclasses(BasicType)


@_exported
def table_types() -> tuple[type[TableType]]:
    """Return all table-type item classes."""
    return _get_itp_subclasses(TableType)


@_exported
def drawing_items() -> tuple[type[DrawingType]]:
    """Return all drawing-type item classes."""
    return _get_itp_subclasses(DrawingType)


@_exported
def plotting_items() -> tuple[type[PlottingType]]:
    """Return all plotting-type item classes."""
    return _get_itp_subclasses(PlottingType)


@_exported
def node_types() -> tuple[type[NodeType]]:
    """Return all node-type item classes."""
    return _get_itp_subclasses(NodeType)


@_exported
def theme_types() -> tuple[type[ThemeType]]:
    """Return all theming-type item classes."""
    return _get_itp_subclasses(ThemeType)


@overload
def auto_parent(parent_factory: ItemCommand, /) -> Callable[[type[_ITP]], type[_ITP]]: ...
@overload
def auto_parent(parent_factory: ItemCommand, /) -> Callable[[_T], _T]: ...
@overload
def auto_parent(parent_factory: ItemCommand, /, wrapped: type[_ITP]) -> type[_ITP]: ...
@overload
def auto_parent(parent_factory: ItemCommand, /, wrapped: _T) -> _T: ...
@_exported
def auto_parent(parent_factory: Any, /, wrapped: Any = None):  # type: ignore
    """Wrapper for `AppItemType` classes and functions that create
    Dear PyGui items. Before creating the item, a parent will
    automatically be created for the item if none is available.
        >>> # Usage w/interfaces
        >>> @auto_parent(dearpypixl.mvWindowAppItem)
        >>> class Frame(dearpypixl.mvChildWindow):
        ...     ...
        >>>
        >>> # Usage w/functions
        >>> @auto_parent(dearpygui.add_window)
        >>> def create_frame(*args, **kwargs):
        ...     ...
        ...     with dearpygui.child_window(*args, **kwargs) as frame:
        ...         ...
        ...     return frame

    Args:
        * parent_factory: A callable that, when called, creates a
        container item and returns a reference to it. Should be
        callable without arguments.

        * wrapped: A callable following the `ItemCommand` protocol.


    When wrapping `AppItemType` classes, this procedure specifically
    targets their `__init__` method.
    """
    def capture_wrapped(wrapped: Any):

        if isinstance(wrapped, type) and issubclass(wrapped, AppItemType):

            @functools.wraps(wrapped.__init__)
            def __init__(self, *args, **kwargs):
                if not kwargs.get('parent', 0) and not RegistryAPI.top_stack_item():
                    kwargs["parent"] = parent_factory()
                cls_init(self, *args, **kwargs)

            if wrapped.is_root_item:
                raise TypeError(
                    f"cannot set up auto parenting on a root interface "
                    f"type {wrapped.__qualname__!r}."
                )
            cls_init = wrapped.__init__
            wrapped.__init__ = __init__
            return wrapped

        elif callable(wrapped):

            @functools.wraps(wrapped)
            def item_command(*args, **kwargs):
                if not kwargs.get('parent', 0) and not RegistryAPI.top_stack_item():
                    kwargs["parent"] = parent_factory()
                return wrapped(*args, **kwargs)

            return item_command

        raise TypeError(
            f"expected a callable that creates items "
            f"for `wrapped`, got {type(wrapped).__qualname__!r}."
        )

    if wrapped is None:
        return capture_wrapped
    return capture_wrapped(wrapped)