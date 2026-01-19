import sys
import enum
import types
import functools
import typing
import annotationlib
import inspect

if typing.TYPE_CHECKING:
    from .protocols import Property




type _SourceStrings = typing.Sequence[str]



_MISSING = object()


_DEFAULT_MODULE = types.ModuleType(f"<module>")
_DEFAULT_MODULE.__dict__.update(globals())

_DEFAULT_LOCALS = {}

def create_function(
    name: str,
    args: _SourceStrings,
    body: _SourceStrings,
    module: str = '',
    *,
    return_type: typing.Any = _MISSING,
    globals: dict[str, typing.Any] | None = None,
    locals: dict[str, typing.Any] | None = None,
) -> typing.Callable:
    if isinstance(args, str):
        args = args.split(",")
    if isinstance(body, str):
        body = (body,)

    body = '\n'.join(f'        {line}' for line in body)

    if return_type is not _MISSING:
        if locals is None:
            locals = _DEFAULT_LOCALS

        locals = dict(locals)
        locals["_return_type"] = return_type

        ret_src = " -> _return_type"
    else:
        if locals is None:
            locals = _DEFAULT_LOCALS

        ret_src = ''

    if globals is None:
        if module in sys.modules:
            globals = sys.modules[module].__dict__
        else:
            globals = _DEFAULT_MODULE.__dict__

    closure = (
        f"def __create_function__({', '.join(locals)}):\n"
        f"    def {name}({','.join(args)}){ret_src}:\n{body}\n"
        f"    return {name}"
    )

    scope = {}
    exec(closure, globals, scope)

    fn = scope["__create_function__"](**locals)
    fn.__module__   = module or _DEFAULT_MODULE.__name__
    fn.__qualname__ = fn.__name__ = name

    return fn


FGET_SOURCE_ARGS = FDEL_SOURCE_ARGS = ("self",)
FSET_SOURCE_ARGS = ("self", "value",)


def create_property(
    fget_body: _SourceStrings,
    fset_body: _SourceStrings | None = None,
    fdel_body: _SourceStrings | None = None,
    doc: str | None = None,
    *,
    module: str = '',
    globals: dict[str, typing.Any] | None = None,
    locals: dict[str, typing.Any] | None = None,
) -> "Property[typing.Any, typing.Any, typing.Any]":
    fget = create_function(
        "getter", FGET_SOURCE_ARGS, fget_body, module, globals=globals, locals=locals
    )

    if fset_body is not None:
        fset = create_function(
            "setter", FSET_SOURCE_ARGS, fset_body, module, globals=globals, locals=locals
        )
    else:
        fset = None

    if fdel_body is not None:
        fdel = create_function(
            "deleter", FDEL_SOURCE_ARGS, fdel_body, module, globals=globals, locals=locals
        )
    else:
        fdel = None

    return property(fget, fset, fdel, doc)  # type: ignore


class DescriptorDelegate:
    __slots__ = ("factory",)

    def __init__(self, factory: typing.Callable[[str], typing.Any], /):
        self.factory = factory

    def __get__(self, instance=None, cls=None):
        return self

    def __set_name__(self, cls, name):
        prop = self.factory(name)
        setattr(cls, name, prop)


def source_signature_from_parameters(parameters: typing.Sequence[inspect.Parameter], /) -> list[str]:
    source = str(inspect.Signature(parameters, __validate_parameters__=False)) \
        .partition(" ->")[0] \
        .removeprefix('(') \
        .removesuffix(')') \
        .split(", ")

    return source


def wrapped[T: typing.Callable](wrapped: T, /) -> typing.Callable[[typing.Any], T]:
    def get_wrapper(wrapper, /):
        return wrapper
    return get_wrapper




# The library will create a LOT of parameter objects — many of
# which contain the same information. Since they aren't the
# cheapest objects to make anyway, caching them reduces memory
# usage and has performance benefits.
_Parameter = inspect.Parameter


class _ParameterCache(dict[tuple[str, int, typing.Any, typing.Any], _Parameter]):
    __slots__ = ("_state",)

    def __enter__(self, /):
        assert inspect.Parameter is _Parameter
        inspect.Parameter = Parameter

    def __exit__(self, exc_type = None, exc_value = None, traceback = None, /):
        inspect.Parameter = _Parameter


cached_parameters = _ParameterCache()


class Parameter(_Parameter):
    __slots__ = ()

    def __new__(cls, name: str, kind: typing.Any, default: typing.Any = _Parameter.empty, annotation: typing.Any = _Parameter.empty) -> inspect.Parameter:
        return parameter(name, kind, default, annotation)

    def __init__(self, name: str, kind: typing.Any, default: typing.Any = _Parameter.empty, annotation: typing.Any = _Parameter.empty) -> None:
        pass


_get_parameter = cached_parameters.get

def parameter(name: str, kind: int, default: typing.Any = _Parameter.empty, annotation: typing.Any = _Parameter.empty) -> inspect.Parameter:
    # HACK: Dear PyGui functions sometimes have default list
    # values. Mutable defaults in public functions are VERY
    # uncommon, which is why we only check for lists here.
    if isinstance(default, list):
        default = tuple(default)

    key = (name, kind, default, annotation)

    param = _get_parameter(key)
    if param is not None:
        return param

    param = cached_parameters[key] = _Parameter(name, kind, default=default, annotation=annotation)  # pyright: ignore[reportArgumentType]
    return param


CLASS_PARAMETER = parameter("cls", _Parameter.POSITIONAL_OR_KEYWORD)
SELF_PARAMETER = parameter("self", _Parameter.POSITIONAL_OR_KEYWORD)
ARGS_PARAMETER = parameter("args", _Parameter.VAR_POSITIONAL)
KWDS_PARAMETER = parameter("kwargs", _Parameter.VAR_KEYWORD)


def signature(obj: typing.Callable, **kwargs) -> inspect.Signature:
    with cached_parameters:
        sig = inspect.signature(obj, **kwargs)
    return sig
