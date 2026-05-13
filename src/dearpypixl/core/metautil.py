""":meta private:"""
import sys
import types
import typing
if typing.TYPE_CHECKING:
    from dearpypixl.core.protocols import ItemCallback


__all__ = ()




_MISSING = object()


type _SourceStrings = typing.Sequence[str]

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

    fn = scope["__create_function__"](**locals)  # pyrefly: ignore[not-callable]
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
) -> property:
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
    __slots__ = ("factory", "name")

    def __init__(self, factory: typing.Callable[[str], typing.Any], name: str = '', /):
        self.factory = factory
        self.name    = name

    def __get__(self, instance=None, cls=None):
        return self

    def __set_name__(self, cls, name):
        name = self.name or name
        prop = self.factory(name)
        setattr(cls, name, prop)

def create_named_desc_factory(factory: typing.Callable[[str], typing.Any], /) -> typing.Any:
    """Creates a wrapper that automatically provides the member
    name to a descriptor factory that needs it. The *name* argument
    of the returned wrapper is optional -- it will override the
    member name when provided.
    """
    def descfactory_delegate_factory(name: str = '', /):
        return DescriptorDelegate(factory, name)
    return descfactory_delegate_factory




def create_compitem_prop_delegate[T: property](child_path: str, source_prop: T, /) -> T:
    """Create a new property that makes a component item property
    available on interfaces of the enclosing item type class.

    The component item *must* be assigned an alias in a specific
    format -- a path-like string with a dynamic root segment and
    a static tail e.g. `f"<{self.tag}>/{child_path}"` where `self`
    is the composite interface that owns or created the item and
    `child_path` is the *child_path* argument passed to this function.
    *source_prop* should point to an existing "simple item type
    property" -- one where its getter/setter/deleter's *self* arguments
    are **only** used as *item* parameter arguments for DearPyGui
    functions (or similar). Nearly all built-in item type properties
    are compatible.

    :type child_path: `str`
    :param child_path: The alias of the component item without
        the root path (e.g. `"input"`, `"settings/width/input"`,
        etc).

        The actual alias assigned to the component item **must**
        resolve to `f"<{self.tag}>/{child_path}"`.

    :type source_prop: `property`
    :param source_prop: The `property` object to unwrap.
    """
    if source_prop.fget:
        def getter(self, /, *, __PATH=child_path, __FUNC=source_prop.fget):
            return __FUNC(f"<{self.tag}>/{__PATH}")  # type: ignore
    else:
        getter = None

    if source_prop.fset is not None:
        def setter(self, value, /, *, __PATH=child_path, __FUNC=source_prop.fget):
            __FUNC(f"<{self.tag}>/{__PATH}", value)  # type: ignore
    else:
        setter = None

    if source_prop.fdel:
        def deleter(self, /, *, __PATH=child_path, __FUNC=source_prop.fget):
            return __FUNC(f"<{self.tag}>/{__PATH}")  # type: ignore
    else:
        deleter = None

    return type(source_prop)(getter, setter, deleter, source_prop.__doc__)


def get_positional_arity(func: typing.Callable, /) -> int:
    """Return the number of positional arguments accepted by a callable.
    `-1` is returned for callables that accept an arbitrary number of
    arguments.

    Accepted callables include any object where a code object can be
    found on the `__code__` attribute, either directly on the object or
    indirectly on its `__call__` member. Does not work for native C
    functions, however, a special exception is made for `print()` which
    returns `-1`.
    """
    code = getattr(func, "__code__", None)
    if code is None:
        try:
            call = func.__call__  # type: ignore
        except AttributeError:
            assert not callable(func), "object is callable but has no `__call__` member"
            raise TypeError(f"{func!r} is not callable") from None
        try:
            code = call.__code__  # type: ignore
        except AttributeError:
            # special-case for `print()` since it can be a quick debug check
            if func is print:
                return -1
            raise ValueError(
                f"cannot determine positional arity of {func!r} object"
            ) from None

        func = call

    if code.co_flags & 0x04:  # `inspect.CO_VARARGS`
        return -1

    return code.co_argcount - int(hasattr(func, "__self__"))


def get_positional_defaults(func: typing.Callable, /) -> tuple:
    defaults = getattr(func, "__defaults__", _MISSING)
    if defaults is _MISSING:
        try:
            call = func.__call__  # type: ignore
        except AttributeError:
            assert not callable(func), "object is callable but has no `__call__` member"
            raise TypeError(f"{func!r} is not callable") from None
        try:
            defaults = call.__defaults__
        except AttributeError:
            if func is print:
                return ()
            raise ValueError(
                f"cannot determine positional defaults of {func!r} object"
            ) from None

    return defaults or ()  # type: ignore


class _CallbackDelegate[T: ItemCallback](typing.Protocol):
    __name__: str
    __code__: types.CodeType
    __defaults__: tuple
    __kwdefaults__: dict[str, typing.Any]
    @property
    def __wrapped__(self, /) -> T: ...
    def __call__(self, sender: int | str, app_data: typing.Any, user_data: typing.Any, /) -> None: ...

def create_callback_delegate[T: ItemCallback](func: T, /) -> _CallbackDelegate[T]:
    """Create a DearPyGui callback wrapper with a consistent
    signature. The wrapper accepts the three positional
    arguments sent to DearPyGui callbacks: *sender*, *app_data*,
    and *user_data*. When called, the wrapped callable will receive
    a number of these arguments, but not more than what it can
    accept.

    :type func: `ItemCallback`
    :param func: A callable with a positional arity of 0 to 3.

    The original, unwrapped callable can be accessed via the
    wrapper's `__wrapped__` attribute of the wrapper.
    """
    lcls: dict = {"_callback": func}

    match arity := get_positional_arity(func):
        case 0: body = "_callback()"
        case 1: body = "_callback(sender)"
        case 2: body = "_callback(sender, app_data)"
        case _:
            body = "_callback(sender, app_data, user_data)"
            arity = 3

    if arity and (defaults := get_positional_defaults(func)):
        # Use the callable defaults as our defaults. When the callable's
        # arity (0-3) differs from the delegate's (always 3), ensure the
        # delegate's trailing arguments also have defaults.
        count  = len(defaults)
        istart = arity - count
        istop  = istart + count

        tmp = [0, None, None]
        tmp[istart:istop] = defaults[:]
        defaults = tmp
        defaults[istop:] = (0, None, None)[istop:]

        args = ["sender", "app_data", "user_data"]
        for i in range(istart, 3):
            var = f"_default{i}"

            lcls[var] = defaults[i]
            args[i]   = f"{args[i]}={var}"

        args.append('/')
    else:
        args = ("sender", "app_data", "user_data", "/")

    wrapper = create_function("callback_delegate", args, body, __name__, locals=lcls)
    wrapper.__wrapped__ = func  # type: ignore

    return wrapper  # type: ignore

ITEM_CALLBACK_CODE_0 = (lambda: None).__code__
ITEM_CALLBACK_CODE_1 = (lambda sender=0: None).__code__
ITEM_CALLBACK_CODE_2 = (lambda sender=0, app_data=None: None).__code__
ITEM_CALLBACK_CODE_3 = (lambda sender=0, app_data=None, user_data=None: None).__code__
