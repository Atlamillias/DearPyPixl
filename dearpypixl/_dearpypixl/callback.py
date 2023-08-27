"""Callback wrappers and other callable-related utilities."""
import time
import types
import inspect
import functools
import threading
from inspect import Parameter as _Parameter
from .common import (
    Any,
    Item,
    Array,
    ItemConfig,
    Protocol,
    Property,
    Iterable,
    Callable,
    MethodType,
    Callable,
    SupportsIndex,
    ItemInterface,
    TypeVar,
    ParamSpec,
    Self,
    overload,
    override
)
from . import tools

__all__ = [
    # typing
    'ItemCallback',
    # classes
    'Callback',
    'Callstack',
    'CallStack',
    # functions
    'callback',
    'cooldown',
    'cooldown_s',
]



_N = TypeVar("_N", float, int)
_P = ParamSpec("_P")
_T = TypeVar("_T")


class _empty: ... # this declaration keeps the typechecker quiet
_empty = tools.create_marker_type("Empty")  # type: ignore

Empty = type[_empty]



class _ItemCallback0(Protocol):
    __code__: types.CodeType
    def __call__(self, /) -> Any: ...

class _ItemCallback1(Protocol):
    __code__: types.CodeType
    def __call__(self, __sender: Item, /) -> Any: ...

class _ItemCallback2(Protocol):
    __code__: types.CodeType
    def __call__(self, __sender: Item, __app_data: Any, /) -> Any: ...

class _ItemCallback3(Protocol):
    __code__: types.CodeType
    def __call__(self, __sender: Item, __app_data: Any, __user_data: Any, /) -> Any: ...

class _ItemCallback4(Protocol):
    __code__: types.CodeType
    def __call__(self, /, *args: Any) -> Any: ...

ItemCallback = TypeVar(
    "ItemCallback",
    _ItemCallback0,
    _ItemCallback1,
    _ItemCallback2,
    _ItemCallback3,
    _ItemCallback4,
)




def _count_pargs(_callable: Callable):
    try:
        sig = inspect.signature(_callable)
    except TypeError:
        raise TypeError(f"{_callable!r} is not callable.") from None
    except ValueError: # "built-in"/ c-extension function?
        if tools.is_builtin(_callable):
            raise ValueError(
                f"built-in object {_callable.__name__!r} has no signature."
            ) from None
        raise

    variadic_pos     = _Parameter.VAR_POSITIONAL
    positional_types = _Parameter.POSITIONAL_OR_KEYWORD, _Parameter.POSITIONAL_ONLY
    # It is not ideal to go through `__code__.co_argcount` as it won't include
    # variadic positional arguments.
    pos_arg_cnt = 0
    for p in sig.parameters.values():
        kind = p.kind
        if kind in positional_types:
            pos_arg_cnt += 1
        elif kind == variadic_pos:
            pos_arg_cnt = 3
            break
        # DearPyGui will only send a max of three positional args.
        if pos_arg_cnt >= 3:
            pos_arg_cnt = 3
            break
    return pos_arg_cnt


@tools.frozen_namespace
class _CallArgs:
    SENDER    = 'sender'
    APP_DATA  = 'app_data'
    USER_DATA = 'user_data'


_CALLBACK_MARKER = '__item_callback__'


class Callback(ItemInterface):
    """Dynamic "Dear PyGui-callable" object wrapper. Enables non-
    function callables to be callable by Dear PyGui, allowing them
    to be registered as callbacks. In addition, optionally set
    default values for the callback's positional arguments which
    will override Dear PyGui-sent positional arguments.

    `Callback` instances can be compared to a less-generalized
    `functools.partial`. While they are specifically used for
    making a callable "Dear PyGui-callable", they are fairly multi-
    purpose and can be used in place of many lambdas, partials, closures,
    or decorators. A rather niche use-case for them is in priority
    queues, as wrappers support "priority" rich comparisons. Unlike
    `functools.partial` objects, argument overrides do not affect the
    the wrapper call procedure or signature -- "sender", "app_data",
    and "user_data" positional arguments are always accepted (but will
    be ignored when using an override). Overridden arguments can also
    be updated throughout the wrapper's lifetime.

    The implementation of this structure is aimed at keeping the on-call
    overhead onset by the wrapper to an minimum. The `__call__` method
    only forwards calls the target callback and does nothing else; no
    logic, no comparisons - no other code is executed. Instead, the
    overhead is "front-loaded" onto the first call to the wrapper
    proceeding an update to the assigned callback or overridding
    arguments; compiling a new `__call__` method using the current
    state of the wrapper. Updating the wrapper's state will force the
    creation of a new `__call__` method on the next call to the wrapper.
    This can be done beforehand by calling the `.prepare` method.

    The wrapper holds a non-reentrant lock for all reads and writes
    to help maintain thread safety. The lock is not held when the
    wrapper is called.

    The wrapper does not modify the target callback object. They remain
    as they were when set on the wrapper, and can be accessed or updated
    at any time via the `.callback` attribute.
    """
    __slots__ = (
        '__call__',
        '__code__',
        '__wrapped__',
        '_call_args',
        '_lock',
        '_priority',
    )

    __item_callback__ = True

    empty = _empty

    priority: Property[int] = tools.simpleproperty()

    def __init__(
        self,
        callback : Callable | None = None,
        /,
        sender   : Item | Empty = empty,
        app_data : Any  | Empty = empty,
        user_data: Any  | Empty = empty,
        *,
        priority : int         = 1,
    ) -> None:
        """Args:
            * callback: The target callable to wrap.

            * sender: Override for the callback's first positional argument
            "sender".

            * app_data: Override for the callback's second positional
            argument "app_data".

            * user_data: Override for the callback's third positional argument
            "user_data".

            * priority: Numeric value used for rich comparisons.

        The *priority* value is used when comparing the wrapper to other
        objects; useful when used with priority queues.

        """
        self.priority    = priority
        self.__call__    = self.__call
        self.__code__    = self.__call.__code__
        self.__wrapped__ = None
        self._call_args  = (sender, app_data, user_data)
        self._lock       = threading.RLock()
        self.configure(
            callback=callback,
            sender=sender,
            app_data=app_data,
            user_data=user_data
        )

    def __lt__(self, other: Any):
        return self.priority < other

    def __le__(self, other: Any):
        return self.priority <= other

    def __eq__(self, other: Any):
        return self.priority == other

    def __ge__(self, other: Any):
        return self.priority >= other

    def __gt__(self, other: Any):
        return self.priority > other

    def __call__(self, sender: Item = 0, app_data: Any = None, user_data: Any = None, /) -> None: ...
    exec('del __call__')  # signature for auto-complete -- hide removal from pyright

    callback : Property[Callable | None] = ItemConfig()
    sender   : Property[Item | Empty]    = ItemConfig()
    app_data : Property[Any | Empty]     = ItemConfig()
    user_data: Property[Any | Empty]     = ItemConfig()

    @property
    def args(self):
        return self._call_args
    @args.setter
    def args(self, value: Array[Item | Empty, Any | Empty, Any | Empty] | Empty | None):
        try:
            sender, app_data, user_data = value  # type:ignore
        except TypeError:
            if value in (None, _empty):
                sender = app_data = user_data = _empty
            raise
        self.configure(
            sender=sender,
            app_data=app_data,
            user_data=user_data
        )

    @overload
    @override
    def configure(  # type:ignore
        self,
        *,
        callback : Callable | None = ...,
        sender   : Item | Empty    = ...,
        app_data : Any | Empty     = ...,
        user_data: Any | Empty     = ...,
    ) -> None: ...
    @override
    def configure(self, **kwargs):
        with self._lock:
            callback, *call_args = (
                kwargs.pop(k, v)
                for k, v in zip(
                    ('callback', _CallArgs.SENDER, _CallArgs.APP_DATA, _CallArgs.USER_DATA),
                    (self.__wrapped__, *self._call_args)
                )
            )
            if kwargs:
                raise TypeError(
                    f'{self.configure.__name__}() got unexpected keyword '
                    f'argument(s) {", ".join(repr(k) for k in kwargs)}.'
                )
            self.__call__    = self.__call
            self.__code__    = self.__call.__code__
            self.__wrapped__ = callback
            self._call_args  = tuple(call_args)

    @override
    def configuration(self):
        with self._lock:
            return dict(zip(
                ('callback', _CallArgs.SENDER, _CallArgs.APP_DATA, _CallArgs.USER_DATA),
                (self.__wrapped__, *self._call_args)),
            )

    @override
    def information(self):
        return {'priority': self.priority}

    __CALL_ARGS = (
        'self',
        f'{_CallArgs.SENDER}: Item = 0',
        f'{_CallArgs.APP_DATA}: Any = None',
        f'{_CallArgs.USER_DATA}: Any = None',
        # BUG: `__call__` must be able to accept a total of 5 args, including
        # `self`. This is because DPG sees `self` in `__code__.co_argcount` and
        # tries to pass an additional argument. This wouldn't be an issue of it
        # called `__call__` unbound, but the logic expects functions, so...
        '*args'
    )
    __CALL_LCLS  = (
        f'_{_CallArgs.SENDER}_OVERRIDE',
        f'_{_CallArgs.APP_DATA}_OVERRIDE',
        f'_{_CallArgs.USER_DATA}_OVERRIDE',
    )
    __CALLBACK_ARGS = tuple(zip(
        (_CallArgs.SENDER, _CallArgs.APP_DATA, _CallArgs.USER_DATA),
        (__CALL_LCLS)
    ))

    def __call(self, *args) -> None:
        if self.callback is not None:
            self.prepare()
            self.__call__(*args)

    def prepare(self):
        """Write, compile, and set this object's `__call__` method, binding
        any positional argument overrides.

        This is done automatically when the object is first called after
        updating the "callback" or positional argument override attributes.
        It can, however, be called manually in advance.
        """
        with self._lock:
            callback = self.__wrapped__
            try:
                arg_count = _count_pargs(callback)  # type:ignore
            except TypeError:
                raise TypeError(f"`callback` value must be callable.")
            except ValueError:
                raise ValueError(f"unable to get `callback` value signature")

            # mimic what DPG does and only send args if the callback
            # can accept them
            call_locals = dict(zip(self.__CALL_LCLS, self._call_args))
            call_locals['_callback'] = callback
            callback_args = (
                passed_arg if call_locals[ovrrd_arg] is _empty else ovrrd_arg
                for passed_arg, ovrrd_arg in self.__CALLBACK_ARGS[:arg_count]
            )
            __call__ = tools.create_function(
                '__call__',
                self.__CALL_ARGS,
                (f'_callback({", ".join(callback_args)})',),
                None,
                globals=globals(),
                locals=call_locals,
            )
            self.__call__ = MethodType(__call__, self)
            self.__code__ = self.__call__.__code__  # type:ignore


class Callstack(Callback):
    """A sequence-like Dear PyGui-callable object containing other
    callables. When called, callbacks are executed in FIFO order
    without clearing them from the queue. Like `Callback` wrapper
    objects, stack-level positional argument overrides are supported.

    Every stack operation is thread-safe. Callbacks executed by
    the stack can even edit the call stack's contents. However,
    note that the stack takes a "snapshot" of its' current state
    and workload before processing, so changes made to the stack
    at that time won't be reflected on the current workload.

    Callbacks are stored in a `list` object and are exposed via the
    read-only `.callbacks` attribute. Operations performed directly
    on this object are NOT thread-safe. For this reason, it is
    recommended to operate on the stack instance instead. If you choose
    to operate on the underlying sequence instead, it is best to
    use the stack as a context manager as it will automatically manage
    the internal lock and return the underlying callback container.
        >>> stack = Callstack()
        >>> with stack as callbacks:
        ...     ...

    When called, the stack will try to pass three positional
    arguments to each callback; `sender`, `app_data` `user_data`.
    Each callable added to the stack is first checked for
    compatibility; it will be wrapped in a `Callback` object
    beforehand if it cannot accept all three arguments. Both the
    compatibility check and the wrapping are costly procedures.
    If you are certain that your callables adhere to the protocol,
    you can operate on the internal callback container directly with
    the procedure mentioned above.

    The `.append` and `.appendleft` methods return the (wrapped)
    object, allowing them to be used as decorators.

    Since the stack will wrap any callable that doesn't fit its'
    "schema", they can technically contain any callable object. This
    includes other other stacks. However, adding a stack to itself
    via `.append` or `.appendleft` will likely result in a
    `RecursionError`.

    `Callstack` inherits `Callback`s rich comparison behavior. This
    can be misleading since the behavior differs from that of other
    sequence types.

    The underlying lock IS reentrant, unlike the lock used by
    `Callback` objects.
    """
    __slots__ = ("_callbacks",)

    def __init_subclass__(cls):
        super().__init_subclass__()
        # ensure the 'DPG-callable hack' persists when overriding `__call__`
        if '__call__' in cls.__dict__:
            cls.__code__ = cls.__call__.__code__

    def __init__(
        self,
        iterable : Iterable[Callable] = (),
        /,
        sender   : Item | Empty = _empty,
        app_data : Any  | Empty = _empty,
        user_data: Any  | Empty = _empty,
        *,
        priority : int         = 1,
    ) -> None:
        """Args:
            * iterable: Inital contents for the stack.

            * sender: Override for the callback's first positional argument
            "sender".

            * app_data: Override for the callback's second positional
            argument "app_data".

            * user_data: Override for the callback's third positional argument
            "user_data".

            * priority: Numeric value used for rich comparisons.

        The *priority* value is used when comparing the wrapper to other
        objects; useful when used with priority queues.
        """
        # a reentrant lock is used here due to the heightened chance
        # of deadlocking -- mainly due to the object being iterable
        self._lock       = threading.RLock()
        self._call_args  = (sender, app_data, user_data)
        self.priority    = priority
        self.extend(iterable)

    # BUG: `__call__` must be able to accept a total of 5 args, including
    # `self`. This is because DPG sees `self` in `__code__.co_argcount` and
    # tries to pass an additional argument. This wouldn't be an issue of it
    # called `__call__` unbound, but the logic expects functions, so...
    @overload
    def __call__(self, sender: Item = 0, app_data: Any = None, user_data: Any = None, /) -> None: ...  # type:ignore
    def __call__(self, sender: Item = 0, app_data: Any = None, user_data: Any = None, *args) -> None:
        # The lock is not held during execution so callbacks can
        # edit the stack without issue.
        with self._lock:
            # Creating a shallow-copy of the queue is the easiest way to make
            # this op thread-safe while solving key problems. Not the most
            # performant, though...
            callbacks = [cb for cb in self.callbacks]
            sender, app_data, user_data = [  # type: ignore
                passed_arg if ovrrd_arg is _empty else ovrrd_arg
                for passed_arg, ovrrd_arg in zip((sender, app_data, user_data), self._call_args)
            ]
        for callback in callbacks:
            callback(sender, app_data, user_data)

    __code__ = __call__.__code__

    def __enter__(self):
        self._lock.acquire()
        return self.callbacks

    def __exit__(self, *args):
        self._lock.release()

    callbacks: Property[list[Callable]] = tools.simpleproperty()

    @property
    def callback(self):
        return self.__call__

    @overload
    @override
    def configure(  # type:ignore
        self,
        *,
        sender   : Item | _empty = ...,
        app_data : Any | _empty  = ...,
        user_data: Any | _empty  = ...,
    ) -> None: ...
    @override
    def configure(self, **kwargs):
        with self._lock:
            call_args = (
                kwargs.pop(k, v)
                for k, v in zip(
                    (_CallArgs.SENDER, _CallArgs.APP_DATA, _CallArgs.USER_DATA),
                    self._call_args
                )
            )
            if kwargs:
                raise TypeError(
                    f'{self.configure.__name__}() got unexpected keyword '
                    f'argument(s) {", ".join(repr(k) for k in kwargs)}.'
                )
            self._call_args  = tuple(call_args)

    @override
    def configuration(self):
        with self._lock:
            return dict(zip(
                (_CallArgs.SENDER, _CallArgs.APP_DATA, _CallArgs.USER_DATA),
                self._call_args),
            )

    @override
    def prepare(self):
        """Not implemented."""

    # [ INTERNAL HELPERS ]

    def _prepped_callback(self, value: Callable):
        if (
            not hasattr(value, _CALLBACK_MARKER)
            or _count_pargs(value) < 3
        ):
            return Callback(value)
        return value

    def _prepped_callbacks(self, values: Iterable[Callable]):
        if hasattr(values, _CALLBACK_MARKER):
            return values
        yield from (Callback(v) for v in values)

    # [ QUEUE METHODS ]

    def __bool__(self) -> bool:
        with self._lock:
            return len(self.callbacks) == 0

    def __len__(self) -> int:
        with self._lock:
            return len(self.callbacks)

    def __iter__(self):
        with self._lock:
            yield from self.callbacks

    def __reversed__(self):
        with self._lock:
            yield from self.callbacks.__reversed__()

    def __contains__(self, value: Any):
        with self._lock:
            return value in self.callbacks

    def __getitem__(self, index: SupportsIndex):
        with self._lock:
            return self.callbacks[index]

    def __setitem__(self, index: SupportsIndex, value: Callable):
        with self._lock:
            self.callbacks[index] = self._prepped_callback(value)

    def __delitem__(self, index: SupportsIndex):
        with self._lock:
            del self.callbacks[index]

    def count(self, value: Any):
        with self._lock:
            return self.callbacks.count(value)

    def insert(self, index: SupportsIndex, value: Callable):
        value = self._prepped_callback(value)
        with self._lock:
            self.callbacks.insert(index, value)
        return value  # decorator usage

    def append(self, value: Callable):
        """Add a callback to the end of the stack. Can be used as a decorator."""
        value = self._prepped_callback(value)
        with self._lock:
            self.callbacks.append(value)
        return value  # decorator usage

    def appendleft(self, value: Callable):
        """Add a callback to the start of the stack. Can be used as a decorator."""
        return self.insert(0, value)  # decorator usage

    def extend(self, value: Iterable[Callable]):
        with self._lock:
            value = list(self.callbacks) if value is self else self._prepped_callbacks(value)
            self.callbacks.extend(value)

    def __add__(self, value: Iterable[Callable]):
        self.extend(value)
        return self

    __iadd__ = __add__

    def extendleft(self, value: Iterable[Callable]):
        with self._lock:
            value = list(self.callbacks) if value is self else self._prepped_callbacks(value)
            callbacks = (*value, *self.callbacks)
            self.callbacks.clear()
            self.callbacks.extend(callbacks)

    def pop(self, index: SupportsIndex = -1):
        with self._lock:
            return self.callbacks.pop(index)

    def popleft(self):
        return self.pop(0)

    def clear(self):
        with self._lock:
            self.callbacks.clear()

    def copy(self) -> Self:
        copy = type(self)(
            (),
            priority=self.priority,
            **self.configuration()  # holds lock
        )
        with self._lock:
            copy.callbacks.extend(self.callbacks)   # avoid re-processing values
        return copy

    __copy__ = copy

    def reverse(self):
        with self._lock:
            self.callbacks.reverse()


CallStack = Callstack  # alias for compat.




# [ UTILITY FUNCTIONS ]

@overload
def callback(*, sender: Item = ..., app_data: Any = ..., user_data: Any = ..., priority: int = ...) -> Callback: ...
@overload
def callback(callback: ItemCallback, /, sender: Item = ..., app_data: Any = ..., user_data: Any = ..., priority: int = ...) -> Callback: ...
def callback(callback: Any = None, sender: Any = _empty, app_data: Any = _empty, user_data: Any = _empty, priority: int = 1) -> Any:
    """Convenience decorator for wrapping a callable in a `Callback` object.

    See the `Callback` class for more information.
    """
    def capture_callback(callback: Callable | None):
        return Callback(
            callback,
            priority=priority,
            sender=sender,
            app_data=app_data,
            user_data=user_data
        )

    if callback is None:
        return capture_callback
    return capture_callback(callback)


@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, /, *, no_args: bool = False) -> Callable[[Callable[_P, Any]], Callable[_P, None]]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, /, *, no_args: bool = True) -> Callable[[Callable[[], Any]], Callable[[], None]]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = False) -> Callable[_P, None]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = True) -> Callable[[], None]: ...
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Any = None, /, *, no_args: bool = False):
    """Return a wrapper that, when called, executes the target callable only
    if enough time has elapsed since the last time it was ran. Can be used
    as a function decorator.

    This function adds a "cooldown" to a callable, limiting how often it can
    be executed over a period of time. In the event that not enough time has
    elapsed between calls (where *callback* was actually executed), the call
    simply does nothing.

    *timer_fn* should be a zero-argument callable that returns a number
    representing a unit of time, while *interval* is the amount of time needed
    between consecutive calls. *interval* and the return of *timer_fn* must
    be of the same time unit. For example, if *timer_fn* returns fractional
    seconds (i.e. `time.perf_counter`), then the value of *interval* is expected
    to also be a fractional number of seconds.

    By default, the returned wrapper forwards all arguments to the target
    callable. The process adds some overhead which may be notable for more time-
    sensitive programs. Setting the *no_args* flag reduces this overhead
    considerably by simplifying the returned wrapper. It cannot accept
    arguments, however, and will call *callback* without trying to pass any.

    This function does not create or utilize threads, nor does it queue
    the callable for execution in any way.
    """
    def capture_callback(callback: Callable) -> Callable:
        if no_args:
            def recurring_tasker():  # type: ignore
                ts_last_update = timer_fn() - interval
                while True:
                    ts_this_update = timer_fn()
                    if ts_this_update - ts_last_update >= interval:
                        ts_last_update = ts_this_update
                        callback()
                    yield

            dispatcher = recurring_tasker().__next__  # type: ignore

        else:
            def recurring_tasker():
                ts_last_update = timer_fn() - interval
                args, kwds = yield
                while True:
                    ts_this_update = timer_fn()
                    if ts_this_update - ts_last_update >= interval:
                        ts_last_update = ts_this_update
                        callback(*args, **kwds)
                    args, kwds = yield

            @functools.wraps(callback)
            def dispatcher(*args, **kwargs) -> None:
                _dispatcher.send((args, kwargs))

            _dispatcher = recurring_tasker()
            next(_dispatcher)  # prime generator

        return dispatcher

    if callback is None:
        return capture_callback
    return capture_callback(callback)


@overload
def cooldown_s(interval: _N, /, *, no_args: bool = False) -> Callable[[Callable[_P, Any]], Callable[_P, None]]: ...
@overload
def cooldown_s(interval: _N, /, *, no_args: bool = True) -> Callable[[Callable[[], Any]], Callable[[], None]]: ...
@overload
def cooldown_s(interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = False) -> Callable[_P, None]: ...
@overload
def cooldown_s(interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = True) -> Callable[[], None]: ...
def cooldown_s(interval: _N, callback: Any = None, /, no_args: bool = False):  # type: ignore
    """Adds a cooldown to a callable with an interval in fractional seconds.

    Refer to the `cooldown` function for more information.
    """
    return cooldown(time.perf_counter, interval, callback, no_args=no_args)
