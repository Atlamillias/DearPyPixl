"""Internal module containing various utilities for creating
or extending interface types."""
import sys
import types
import threading
import collections.abc

import typing
if typing.TYPE_CHECKING:
    from dearpypixl.core.protocols import ItemCallback


__all__ = ()




_MISSING = object()


type _SourceStrings = typing.Sequence[str]

_DEFAULT_MODULE = types.ModuleType("<module>")
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
            return __FUNC(f"{self.tag}/{__PATH}")  # type: ignore
    else:
        getter = None

    if source_prop.fset is not None:
        def setter(self, value, /, *, __PATH=child_path, __FUNC=source_prop.fset):
            __FUNC(f"{self.tag}/{__PATH}", value)  # type: ignore
    else:
        setter = None

    if source_prop.fdel:
        def deleter(self, /, *, __PATH=child_path, __FUNC=source_prop.fdel):
            return __FUNC(f"{self.tag}/{__PATH}")  # type: ignore
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


class EventContainer[**P](collections.abc.MutableSequence):
    """Creates a sequence-like callable that stores other like-signature
    callables. Calling the container calls every object within it in
    FIFO order; they receive any arguments passed to the container.

    Instead of iterating over each object in the container, the delegation
    procedure uses a vectorized function where calls to objects are in-lined.
    This function is (re)compiled lazily when calling the container following
    any mutations, so it is recommended to perform mutations enmasse to limit
    how often the function gets re-compiled.

    Container operations are thread-safe, iteration withstanding. The
    :py:attr:`lock` is reentrant, so a user can acquire it themselves when
    commiting several changes to ensure the lock is not released between
    operations. Note that under certain conditions, holding the lock may
    block other threads attempting to call the container until it is released.

    Unlike a normal mutable sequence, `EventContainer` objects will ignore
    any additions that are already present in the container (via `__eq__()`).
    For example, `self.append(print)` will add the `print()` function as
    expected, but `self.append(print)` again becomes a no-op because `print()`
    is already registered.

    A container can be serialized and copied. Copying a container creates
    a shallow copy with a new internal lock.

    The :py:meth:`remove()` method works similarly to `set().discard()`
    where it will not throw an error if the input callable is not in the
    container.

    The :py:meth:`append()` returns the input callable instead of `None`,
    allowing it to be used as a decorator.

    :type iterable: `Iterable[Callable]` (optional)
    :param iterable: Callables to initialize the container with.

    :type positional_only: `bool` (optional)
    :param positional_only: If `True`, callables in the container will
        not receive keyword arguments during delegation. This optimizes
        the procedure by omitting keyword argument unpacking during the
        process. Recommended if the container will delegate to callables
        only expecting positional arguments. Defaults to `False`.

    :type parg_count: `int` (optional)
    :param parg_count: Sets the container's call signature so that it requires
        *n* positional arguments instead of accepting any number of positional
        arguments. This optimizes the delegation procedure by telling the
        compiler to inline positional argument references directly instead of
        unpacking the argument tuple for each object called at runtime e.g.
        `object(arg1, arg2)` vs `object(*args)`. Defaults to -1.
    """
    __slots__ = ("_lock", "_delegate", "_events", "_pargs_only", "_parg_count")

    type T = typing.Callable[P, typing.Any]

    @property
    def events(self, /) -> tuple[T, ...]:
        """[***get**, **set***] callables within the container.

        Returns a snapshot of the container's contents as a tuple
        on-access. On set, the container is emptied first, then
        updated with the new contents.
        """
        return (*self._events,)
    @events.setter
    def events(self, value: typing.Iterable[T], /) -> None:
        with self._lock:
            self._events.clear()
            self._events.extend(value)
            self._delegate = None

    _lock: threading.RLock

    @property
    def lock(self, /) -> threading.RLock:
        """[***get**] the reentrant lock used internally to maintain
        thread safety.

        Managing code can hold the lock to ensure it is not released
        in between operations.
        """
        return self._lock

    _delegate: typing.Any

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        self._lock     = threading.RLock()
        self._delegate = None
        return self

    def __init__(self, iterable: typing.Iterable[T] | None = None, *, positional_only: bool = True, parg_count: int = -1) -> None:
        self._events = []
        self._pargs_only = positional_only
        self._parg_count = None if parg_count < 0 else parg_count

        if iterable is not None:
            self.extend(iterable)

    def __getstate__(self, /) -> tuple[dict | None, dict]:
        state = object.__getstate__(self)

        slot_state = state[1]  # type: ignore
        try:
            del slot_state["_lock"]  # type: ignore
        except KeyError:
            pass
        try:
            del slot_state["_delegate"]  # type: ignore
        except KeyError:
            pass
        return state  # type: ignore

    def __setstate__(self, state: tuple[dict | None, dict], /):
        dict_state, slot_state = state

        if dict_state is not None:
            assert hasattr(self, "__dict__")
            self.__dict__.update(dict_state)

        setattr = self.__setattr__
        for attr, obj in slot_state.items():
            setattr(attr, obj)

    def __copy__(self, memo=None, /):
        state = self.__getstate__()
        state[1]["_events"] = self._events.copy()

        copy = self.__new__(type(self))
        copy.__setstate__(state)
        return copy

    def copy(self, /):
        """Return a shallow copy of the container with a new internal lock."""
        return self.__copy__()

    def _compile_delegate(self, /, *, __no_op=lambda *args, **kwargs: None) -> typing.Callable[..., typing.Any]:
        if len(self._events) == 0:
            return __no_op

        if self._parg_count is not None:
            s_args = [f"arg{i}" for i in range(self._parg_count)]
        else:
            s_args = ("*args",)

        if self._pargs_only:
            s_kwds = ()
        else:
            s_kwds = ("**kwargs",)

        fn_lcls = {f"func{i}":func for i,func in enumerate(self._events)}
        fn_args = (*s_args, *s_kwds)
        fn_body = f"({', '.join(fn_args)})\n".join(fn_lcls).split("\n")
        fn_body[-1] = fn_body[-1] + f"({', '.join(fn_args)})"

        return create_function("callback", fn_args, fn_body, module=__name__, locals=fn_lcls)

    def compile(self, /) -> None:
        """Compile or re-compile the internal, vectorized delegator function.

        This is normally a lazy, implicit procedure. However, compiling the
        function pre-emptively is more performant as it avoids exception
        handling overhead.
        """
        with self._lock:
            self._delegate = self._compile_delegate()

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        callback = self._delegate
        try:
            callback(*args, **kwargs)
            return
        except TypeError:
            if callback is not None:
                raise

        with self._lock:
            if self._delegate is not None:
                callback = self._delegate
            else:
                callback = self._delegate = self._compile_delegate()

        callback(*args, **kwargs)

    def __repr__(self, /):
        return f"{type(self).__name__}({self._events})"

    # mutable sequence protocol

    def __len__(self, /):
        return len(self._events)

    def __contains__(self, other, /):
        try:
            return other in self._events
        except TypeError:
            return False

    def __iter__(self, /):
        return iter(self._events)

    def __reversed__(self, /):
        return reversed(self._events)

    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex, /) -> T: ...
    @typing.overload
    def __getitem__(self, slice: slice, /) -> typing.Self: ...
    def __getitem__(self, index, /):
        res = self._events[index]
        if type(res) is list:
            state = self.__getstate__()
            state[1]["_events"] = res

            copy = self.__new__(type(self))
            copy.__setstate__(state)
            return self

        return res

    @typing.overload
    def __setitem__(self, index: typing.SupportsIndex, value: T, /) -> None: ...
    @typing.overload
    def __setitem__(self, slice: slice, value: typing.Iterable[T], /) -> None: ...
    def __setitem__(self, index, value, /) -> None:
        with self._lock:
            if isinstance(index, slice):
                buffer = self._events.copy()
                buffer[index] = value

                events = []
                for obj in buffer:
                    if obj not in events: events.append(obj)

                self._events.clear()
                self._events.extend(events)
            else:
                self._events[index] = value
            self._delegate = None

    @typing.overload
    def __delitem__(self, index: typing.SupportsIndex, /) -> None: ...
    @typing.overload
    def __delitem__(self, slice: slice, /) -> None: ...
    def __delitem__(self, index, /):
        with self._lock:
            del self._events[index]
            self._delegate = None

    def reverse(self, /) -> typing.Self:  # pyrefly: ignore [bad-override]
        with self._lock:
            self._events.reverse()
            self._delegate = None
        return self

    def sort(self, /, *, key: typing.Callable[[T], typing.Any], reverse: bool = False) -> typing.Self:
        with self._lock:
            self._events.sort(key=key, reverse=reverse)
            self._delegate = None
        return self

    def index(self, value: str, /, start: typing.SupportsIndex = 0, stop: typing.SupportsIndex | None = None) -> int:
        if stop is not None:
            return self._events.index(value, start, stop)
        return self._events.index(value, start)

    def insert(self, index: typing.SupportsIndex, value: str, /) -> None:
        with self._lock:
            if value in self._events:
                return
            self._events.insert(index, value)
            self._delegate = None

    def append(self, callback: T, /) -> T:  # pyrefly: ignore [bad-override]
        with self._lock:
            if callback not in self._events:
                self._events.append(callback)
                self._delegate = None
        return callback

    def extend(self, iterable: typing.Iterable[T], /) -> None:
        with self._lock:
            events = self._events
            length = len(events)
            events.extend((obj for obj in iterable if obj not in events))
            if len(events) != length:
                self._delegate = None

    def __add__(self, other: typing.Iterable[T], /) -> typing.Self:
        copy = self.__copy__()
        copy.extend(other)
        return copy

    def __iadd__(self, other: typing.Iterable[T], /) -> typing.Self:
        self.extend(other)
        return self

    def remove(self, callback: typing.Any, /) -> None:
        with self._lock:
            try:
                self._events.remove(callback)
            except ValueError:
                pass
            self._delegate = None

    def pop(self, index: typing.SupportsIndex = -1, /) -> T:
        with self._lock:
            res = self._events.pop(index)
            self._delegate = None
        return res

    def clear(self, /) -> None:
        with self._lock:
            self._events.clear()
            self._delegate = None
