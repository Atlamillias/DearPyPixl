import enum
import collections
import gc
import functools
import inspect
from inspect import Parameter
from time import perf_counter, perf_counter_ns
from dearpygui import dearpygui, _dearpygui
from .px_typing import (
    NULL, T, P, KT, VT,
    ItemId, DPGCallback, DPGCommand,
    FrozenNamespace,
    typing_overload,
    # typing
    overload,
    cast,
    Any,
    Sequence,
    TypedDict,
    Generic,
    ParamSpec,
    Self,
    Iterator,
    Iterable,
    Callable,
    Generator,
    Mapping,
    Protocol,
    Concatenate,
)
from .px_items import AppItemType, RegistryItem, HandlerItem, Config
from . import px_items


__all__ = [
    # typing
    "ItemId",
    "DPGCallback",

    # misc
    "perf_counter",
    "perf_counter_ns",

    # constants, enums
    "Mouse",
    "KeyCode",
    "TaskerMode",
    "Frame",

    # "poster" objects
    "Callback",
    "CallStack",
    "FrameEvents",
]



_CALLBACK  = "callback"
_SENDER    = "sender"
_APP_DATA  = "app_data"
_USER_DATA = "user_data"


def _callback_parg_count(_callable: Callable) -> int:
    try:
        sig = inspect.signature(_callable)
    except TypeError:
        raise TypeError(f"{_callable!r} is not callable.") from None
    except ValueError:
        # built-ins don't have a signature
        if getattr(_callable, "__module__", None) == "builtins":
            raise ValueError(f"Unable to manage builtin object {_callable.__name__!r} (no signature).") from None
        raise

    params = sig.parameters.values()

    _VARIADIC_POS    = Parameter.VAR_POSITIONAL
    _POSITIONAL_KIND = (Parameter.POSITIONAL_OR_KEYWORD, Parameter.POSITIONAL_ONLY)
    # It is not ideal to go through `__code__.co_argcount` as it won't include
    # variadic positional arguments.
    pos_arg_cnt = 0
    for p in params:
        kind = p.kind
        if kind in _POSITIONAL_KIND:
            pos_arg_cnt += 1
        elif kind == _VARIADIC_POS:
            pos_arg_cnt = 3
            break
        # DearPyGui will only send a max of three positional args.
        if pos_arg_cnt >= 3:
            pos_arg_cnt = 3
            break
    return pos_arg_cnt


def _callback_defaults_src(_callable: Callable) -> tuple[str, str, str]:
    # The workflow calls this following `_callback_parg_count`, so the same
    # checks are not needed here.
    params = inspect.signature(_callable).parameters.values()
    # Get defaults from at least 3 parameters.
    parg_defaults = []
    for p in params:
        if p.kind in (Parameter.KEYWORD_ONLY, Parameter.VAR_POSITIONAL):
            break

        if p.default != Parameter.empty:
            parg_defaults.append(str(p).split("=")[-1].strip())
        else:
            parg_defaults.append('None')

        if len(parg_defaults) >= 3:
            break

    parg_defaults.extend(['None'] * 3)  # always return three values
    return tuple(parg_defaults[:3])


def _callback_wrapper(callback: T, *args) -> T:
    # new fn definition string
    cb_parg_defaults = _callback_defaults_src(callback)
    call_fn_params   = (
        f"{_SENDER}: ItemId | None = {cb_parg_defaults[0]}",
        f"{_APP_DATA}: Any = {cb_parg_defaults[1]}",
        f"{_USER_DATA}: Any = {cb_parg_defaults[2]}",
    )
    # new fn body string
    local_vars = (_SENDER, _APP_DATA, _USER_DATA)                          # bound to DPG args (local to callback)
    bound_vars = (f"_{_SENDER}", f"_{_APP_DATA}", f"_{_USER_DATA}")        # bound to CallbackEvent args (nonlocal to callback)
    cb_args    = [bound_vars[i] if args[i] is not NULL else local_vars[i]
                  for i in range(len(args))]

    # closure returning the new function
    wrapper_fn_src = (
        f"def wrapper({_CALLBACK}, {bound_vars[0]} = None, {bound_vars[1]} = None, {bound_vars[2]} = None):\n"
        f"    def __call__({', '.join(call_fn_params)}) -> None: {_CALLBACK}({', '.join(cb_args)})\n"
        f"    return __call__"
    )
    namespace = {}
    exec(wrapper_fn_src, None, namespace)
    return namespace["wrapper"](callback, *args)


def _null_callback(*args) -> None:
    """Fallback callable to use when `callback` is None or NULL."""


class CallbackConfig(TypedDict):
    callback : DPGCallback[P]
    sender   : ItemId | None | NULL
    app_data : Any
    user_data: Any


class Callback(DPGCallback[P]):
    __slots__ = (
        "__wrapped__",
        "__signature__",
        # For performance reasons, `__call__` is dynamically created to cater to the wrapped
        # callable, and is set at the instance-level. This typically does nothing -- dunder
        # method lookups are done at class-level through its type slots. Using descriptors is
        # the only way around this.
        "__call__",
        # Callable non-functions don't normally work as DPG callbacks because of the
        # missing `__code__` attribute. It works with both `__code__` and `__call__`.
        "__code__",
        # Overrides for DPG's sent `sender`, `app_data`, and `user_data` positional arguments.
        "_cb_pos_args",
    )

    NULL = NULL

    def __init__(
        self,
        callback : DPGCallback[P] | None | NULL = None,
        /,
        sender   : ItemId | None | NULL = NULL,
        app_data : Any                  = NULL,
        user_data: Any                  = NULL,
    ) -> None:
        # unwrap other instances of `Callback`
        if isinstance(callback, Callback):
            callback, sender, app_data, user_data = callback.configuration().values()
        self._cb_pos_args = (sender, app_data, user_data)
        self.__wrapped__  = callback
        self.configure(callback=callback, sender=sender, app_data=app_data, user_data=user_data)

    def __repr__(self):
        return (
            f"{type(self).__qualname__}("
            f"{', '.join(f'{k}: {str(v)!r}' for k, v in self.configuration().items())}"
            f")"
        )

    def __getattr__(self, name: str):
        try:
            return self.configuration()[name]
        except KeyError:
            pass
        try:
            return getattr(self.__wrapped__, name)
        except AttributeError:
            pass
        raise AttributeError(name) from None

    __call__: DPGCallback[P]

    callback : Config[DPGCallback[P] | None, DPGCallback[P] | None | NULL] = Config()
    sender   : Config[ItemId | None | NULL, ItemId | None | NULL]          = Config()
    app_data : Config[Any | NULL, Any | NULL]                              = Config()
    user_data: Config[Any | NULL, Any | NULL]                              = Config()

    @overload
    def configure(self, *, callback: DPGCallback[P] = ..., sender: ItemId = ..., app_data: Any = ..., user_data: Any = ..., **kwargs) -> None: ...
    def configure(self, **kwargs: CallbackConfig) -> None:
        cb = self.__wrapped__
        if _CALLBACK in kwargs:
            cb = kwargs[_CALLBACK]
        cb_args = [*self._cb_pos_args]
        if _SENDER in kwargs:
            cb_args[0] = kwargs[_SENDER]
        if _APP_DATA in kwargs:
            cb_args[1] = kwargs[_APP_DATA]
        if _USER_DATA in kwargs:
            cb_args[2] = kwargs[_USER_DATA]

        # rebuild `__call__` after any updates to the instance
        if kwargs:
            self._cb_pos_args = tuple(cb_args)
            if cb not in (None, NULL):
                self.__wrapped__ = cb
                self.__call__    = _callback_wrapper(cb, *self._cb_pos_args[:_callback_parg_count(cb)])
                self.__code__    = cb.__code__
            else:
                self.__wrapped__ = _null_callback
                self.__call__    = _null_callback
                self.__code__    = _null_callback.__code__

    def configuration(self) -> CallbackConfig:
        return dict(zip((_CALLBACK, _SENDER, _APP_DATA, _USER_DATA), (self.__wrapped__, *self._cb_pos_args)))




##########################################
########### CALLSTACK OBJECTS ############
##########################################

_MODE_TO_TASKER: dict[int, str] = {}

def new_tasker(mode: 'TaskerMode'):
    def register_tasker(mthd: T) -> T:
        _MODE_TO_TASKER[mode] = mthd.__name__
        setattr(mthd, "_tasker_mode_", mode)
        return mthd
    return register_tasker


class TaskerMode(enum.IntEnum):
    ITER    = 0
    CYCLE   = 1
    POP     = 2
    POPLEFT = 3
    RUNTIME = 4


class Tasker(DPGCallback):
    # Contains the bulk that processes scheduled events for `CallStack`. The `_cb_pos_args`
    # attribute still needs to be defined in `CallStack`.

    __slots__ = ()

    timer : Callable[[], float]
    tasker: Callable[[Self, ItemId | None, Any, Any], Generator[float, None, None]]

    @property
    def tasker_mode(self) -> TaskerMode | int:
        """[get] Return the mode used by the `.tasker` method."""
        return getattr(self.tasker, "_tasker_mode_", self.DEFAULT)
    @tasker_mode.setter
    def tasker_mode(self, value: TaskerMode | int | None) -> None:
        """[set] Change the behavior of the `.tasker` method."""
        if not value:
            value = self.DEFAULT
        self.tasker = getattr(self, _MODE_TO_TASKER[value])

    # TODO: flag system for mixed behaviors
    ITER     = TaskerMode.ITER
    CYCLE    = TaskerMode.CYCLE
    POP      = TaskerMode.POP
    POPLEFT  = TaskerMode.POPLEFT

    DEFAULT = ITER

    @new_tasker(ITER)
    def _tasker_iter(self: 'CallStack', sender: ItemId = None, app_data : Any = None, user_data: Any = None) -> Generator[Any, None, None]:
        sender, app_data, user_data = self._get_task_arguments(sender, app_data, user_data)
        for callback in self:
            yield callback(sender, app_data, user_data)

    @new_tasker(CYCLE)
    def _tasker_cycle(self: 'CallStack', sender: ItemId = None, app_data : Any = None, user_data: Any = None) -> Generator[Any, None, None]:
        while True:
            yield from self._tasker_iter(sender, app_data, user_data)

    @new_tasker(POP)
    def _tasker_pop(self: 'CallStack', sender: ItemId = None, app_data : Any = None, user_data: Any = None) -> Generator[Any, None, None]:
        sender, app_data, user_data = self._get_task_arguments(sender, app_data, user_data)
        next_callback = self.pop
        while True:
            try:
                yield next_callback()(sender, app_data, user_data)
            except IndexError:
                break

    @new_tasker(POPLEFT)
    def _tasker_popleft(self: 'CallStack', sender: ItemId = None, app_data : Any = None, user_data: Any = None) -> Generator[Any, None, None]:
        sender, app_data, user_data = self._get_task_arguments(sender, app_data, user_data)
        next_callback = self.popleft
        while True:
            try:
                yield next_callback()(sender, app_data, user_data)
            except IndexError:
                break

    @new_tasker(TaskerMode.RUNTIME)
    def _tasker_runtime(self: 'CallStack', *args) -> Generator[Any, None, None]:
        # Is `POPLEFT` but does not pass or build arguments. Better for manual
        # callback management w/`functools.partial`.
        next_callback = self.popleft
        while True:
            try:
                yield next_callback()()
            except IndexError:
                break

    def _get_task_arguments(self: 'CallStack', sender: Any = None, app_data: Any = None, user_data: Any = None) -> Iterator[Any]:
        """Return an iterator containing callback positional arguments (in order) for *sender*,
        *app_data* and *user_data*.

        Callstack attributes `.sender`, `.app_data` and `.user_data` are prioritized and will
        replace *sender*, *app_data* and/or *user_data* in the returned tuple if they have been
        set.
        """
        return (v2 if v2 != NULL else v1 for v1, v2 in zip((sender, app_data, user_data), self._cb_pos_args))

    # XXX [`*args`]: `__code__` (below) references the unbound `__call__` function. DPG will
    # count `self` in `__code__.co_argcount` and will pass an additional `None` argument.
    def __call__(self, sender: ItemId = None, app_data: Any = None, user_data: Any = None, *args) -> None:
        for _ in self.tasker(sender, app_data, user_data): ...

    __code__ = __call__.__code__  # helps DPG call this object


# 'CallStack().force_wrapping'
def _CallStack_force_wrapping_F(callback: T, **kwargs) -> T:
    if not callable(callback):
        raise TypeError(f"{callback!r} is not callable.")
    if _callback_parg_count(callback) < 3 or not inspect.isfunction(callback):
        return Callback(callback, **kwargs)
    return callback

def _CallStack_force_wrapping_T(callback: DPGCallback[P], **kwargs) -> Callback[P]:
    return Callback(callback, **kwargs)

# 'Callstack().wrapped_returns'
def _CallStack_wrapped_returns_F(original: T, callback_inst: Any) -> T:
    return original

def _CallStack_wrapped_returns_T(original: DPGCallback[P], callback_inst: Callback[P] | DPGCallback[P]) -> DPGCallback[P] | Callback[P]:
    return callback_inst


class _CallStack(Generic[T]):  # slotted method signatures & generic typing
    __slots__ = ()

    def count(self, _object: Any) -> int: ...
    def index(self, value: Callback, start: int = 0, stop: int = None): ...
    def pop(self) -> Callback: ...
    def popleft(self) -> Callback: ...
    def remove(self) -> None: ...
    def rotate(self) -> None: ...
    def reverse(self) -> None: ...
    def clear(self) -> None: ...

    def _fn_return_callable(original: DPGCallback[P], callback_inst: Callback[P] | DPGCallback[P]) -> DPGCallback[P] | Callback[P]: ...
    def _fn_process_callable(callback: DPGCallback[P]) -> DPGCallback[P] | Callback[P]: ...

    def tasker(self, sender: ItemId = None, app_data : Any = None, user_data: Any = None) -> Generator[float, None, None]:
        """Returns a generator that, when advanced, times and executes a queued callback.

        Args:
            * sender: Sent as the first positional argument for callbacks. This value is ignored
            if `self.sender` is set. Defaults to None.

            * app_data: Sent as the second positional argument for callbacks. This value is ignored
            if `self.app_data` is set. Defaults to None.

            * user_data: Sent as the final positional argument for callbacks. This value is ignored
            if `self.user_data` is set. Defaults to None.


        The behavior of this method depends on the stack's mode setting:

            `TaskerMode.ITER`: The generator iterates through the queue and calls each callback
            iterated. Reaching the end of the queue exhausts the generator.

            `TaskerMode.CYCLE`: Same behavior as `TaskerMode.ITER` looped indefinitely.

            `TaskerMode.POP`: Advancing the generator pops the right-most (newest) callback from
            the queue and runs it. The generator is exhausted once the queue is cleared.

            `TaskerMode.POPLEFT`: Similar behavior to `TaskerMode.POP`, but pops the left-most
            (oldest) callback from the queue instead.
        """


class CallStack(_CallStack[DPGCallback], Tasker):
    """Multipurpose event queue for DearPyGui. Behaves near-identical to `collections.deque`.
    All queue-related methods are either hooked or directly forwarded an underlying `deque`
    -- pops and appends from either end are thread-safe. Like `Callback` objects, stacks support
    positional argument overrides for `sender`, `app_data`, and `user_data`.

    `Callstack` instances are DearPyGui-callable. This allows users to run or schedule several
    callbacks from a single item interaction. The
        >>> events = CallStack()
        ...
        >>> # The `.append` and `.appendleft` methods are tweaked for decorator usage.
        >>> @events.append
        ... def callback1(sender):
        ...     print(sender)
        ...
        ...
        >>> @events.append
        ... def callback2(sender, app_data):
        ...     print(app_data)
        ...
        ...
        >>> with dpg.window():
        ...     dpg.add_button(callback=events, user_data="a very interesting string")
        ...
        ...
        >>> @events.appendleft
        ... def callback3(sender, app_data, user_data):
        ...     print(user_data)
        ...
        >>> # Run and click the button!

    The stack requires that DearPyGui can sucessfully call any callable it contains. They also
    must accept all three of DearPyGui's sent positional arguments; `sender`, `app_data`, and
    `user_data`. Functions that cannot accept these arguments, in addition to all non-function
    callables, will be wrapped in a `Callback` object before adding it to the queue. Setting the
    '.force_wrapping' attribute to True will wrap all added callables regardless.

    NOTE: By default, the `.append` and `.appendleft` methods return the original callable.
    This behavior can be changed to return the `Callback` object instead (if created) by setting
    the `.wrapped_returns` attribute to True.

    Users have some control over how callbacks are executed. Calls to the stack invoke the
    `.tasker` method; behavior of this method varies depending on the stack's `tasker_mode` attribute
    (a member of the `TaskerMode` enumeration). For convenience, `TaskerMode` members are also
    available as constants on the `CallStack` class. See `Callstack.tasker` for more information
    regarding these behaviors.
    """
    __slots__ = (
        "tasker",                  # 'tasker_mode'
        "_fn_return_callable",     # 'wrapped_returns'
        "_fn_process_callable",    # 'force_wrapping'
        # internal attributes
        "_queue",
        "_cb_pos_args",
        # deque methods
        "count",
        "index",
        "pop",
        "popleft",
        "remove",
        "rotate",
        "reverse",
        "clear",
    )

    NULL = NULL

    def __init__(
        self,
        iterable: Sequence[DPGCallback] = (),
        maxlen  : int | None            = None,
        *,
        sender         : ItemId | None | NULL = NULL,
        app_data       : Any                  = NULL,
        user_data      : Any                  = NULL,
        tasker_mode    : TaskerMode | int     = TaskerMode.ITER,
        force_wrapping : bool = False,
        wrapped_returns: bool = False,
        **kwargs,
    ) -> None:
        super().__init__()
        self._cb_pos_args = (NULL, NULL, NULL)
        self._queue  = collections.deque(maxlen=maxlen)
        self.tasker  = self._tasker_iter
        self.count   = self._queue.count
        self.index   = self._queue.index
        self.pop     = self._queue.pop
        self.popleft = self._queue.popleft
        self.remove  = self._queue.remove
        self.rotate  = self._queue.rotate
        self.reverse = self._queue.reverse
        self.clear   = self._queue.clear
        self.configure(
            sender=sender,
            app_data=app_data,
            user_data=user_data,
            tasker_mode=tasker_mode,
            force_wrapping=force_wrapping,
            wrapped_returns=wrapped_returns,
            **kwargs,
        )
        self.extend(iterable)

    def __str__(self):
        return f'{type(self).__qualname__}({str(self._queue).split("(", maxsplit=1)[-1]}'

    def __repr__(self):
        return (
            f"{type(self).__qualname__}(maxlen={self.maxlen}"
            f"{', '.join(f'{k}={str(v)!r}' for k, v in self.configuration().items())}"
            f")"
        )

    def __iter__(self):
        return iter(self._queue)

    def __bool__(self) -> bool:
        return bool(self._queue)

    def __copy__(self) -> Self:
        copy = type(self)((), self.maxlen, **self.configuration())
        copy._queue = self._queue.copy()  # avoids re-processing values
        return copy

    def __add__(self, other: Iterable[DPGCallback]):
        self._queue.extend(other)
        return self

    def __getitem__(self, index: int) -> Callback:
        return self._queue.__getitem__(index)

    def __setitem__(self, index: int, value: DPGCallback) -> None:
        self._queue.__setitem__(index, self._fn_process_callable(value))

    def __delitem__(self, index: int) -> None:
        self._queue.__delitem__(index)

    def __getattr__(self, name: str):
        try:
            return self.configuration()[name]
        except KeyError:
            raise AttributeError(name)

    def __len__(self) -> int:
        return len(self._queue)

    def __contains__(self, x: Any) -> bool:
        return x in self._queue

    @property
    def maxlen(self):
        return self._queue.maxlen

    sender         : Config[ItemId | None | NULL, ItemId | None | NULL] = Config()
    app_data       : Config[Any | NULL, Any | NULL]                     = Config()
    user_data      : Config[Any | NULL, Any | NULL]                     = Config()
    force_wrapping : Config[bool, bool]                                 = Config()
    wrapped_returns: Config[bool, bool]                                 = Config()

    @overload
    def configure(self, *, sender: ItemId | None | NULL = ..., app_data: Any = ..., user_data: Any = ..., tasker_mode: TaskerMode | int = ..., wrapped_returns: bool = ..., force_wrapping: bool = ..., **kwargs) -> None: ...
    def configure(self, tasker_mode: Any = None, wrapped_returns: bool | None = None, force_wrapping: bool | None = None, **kwargs) -> None:
        cb_args = [*self._cb_pos_args]
        if _SENDER in kwargs:
            cb_args[0] = kwargs[_SENDER]
        if _APP_DATA in kwargs:
            cb_args[1] = kwargs[_APP_DATA]
        if _USER_DATA in kwargs:
            cb_args[2] = kwargs[_USER_DATA]
        self._cb_pos_args = tuple(cb_args)

        if tasker_mode is not None:
            self.tasker_mode = tasker_mode  # `Tasker.tasker_mode`
        if force_wrapping is not None:
            self._fn_process_callable = _CallStack_force_wrapping_T if force_wrapping else _CallStack_force_wrapping_F
        if wrapped_returns is not None:
            self._fn_return_callable = _CallStack_wrapped_returns_T if wrapped_returns else _CallStack_wrapped_returns_F

    def configuration(self) -> dict[str]:
        config = dict(zip((_SENDER, _APP_DATA, _USER_DATA), self._cb_pos_args))
        config.update(
            tasker_mode=self.tasker_mode,
            force_wrapping=True if self._fn_process_callable == _CallStack_force_wrapping_T else False,
            wrapped_returns=True if self._fn_return_callable == _CallStack_wrapped_returns_T else False,
        )
        return config

    def copy(self) -> Self:
        return self.__copy__()

    def insert(self, index: int, _object: DPGCallback) -> None:
        self._queue.insert(index, self._fn_process_callable(_object))

    def extend(self, other: Sequence[DPGCallback]) -> None:
        if isinstance(other, CallStack):
            self._queue.extend(other._queue)
        else:
            self._queue.extend((self._fn_process_callable(cb) for cb in other))

    def extendleft(self, other: Sequence[DPGCallback]) -> None:
        if isinstance(other, CallStack):
            self._queue.extendleft(other._queue)
        else:
            self._queue.extendleft((self._fn_process_callable(cb) for cb in other))

    def append(self, _object: DPGCallback[P]) -> DPGCallback[P] | Callback[P]:
        wrapped = self._fn_process_callable(_object)
        self._queue.append(wrapped)
        return self._fn_return_callable(_object, wrapped)

    def appendleft(self, _object: DPGCallback[P]) -> DPGCallback[P] | Callback[P]:
        wrapped = self._fn_process_callable(_object)
        self._queue.appendleft(wrapped)
        return self._fn_return_callable(_object, wrapped)




###########################################
##### Handlers, Registries Extensions #####
###########################################

# handler method signatures
def _handler_fn(self, callback: DPGCallback | None = None, *, label: str = None, user_data: Any = None, use_internal_label: bool = True, tag: ItemId = 0, parent: ItemId = 0, show: bool = True, **kwargs) -> DPGCallback | None: ...

def _mouse_handler_fn(self, callback: DPGCallback | None = None, *, button: int = -1, label: str = None, user_data: Any = None, use_internal_label: bool = True, tag: ItemId = 0, parent: ItemId = 0, show: bool = True, **kwargs) -> DPGCallback | None: ...

def _key_hander_fn(self, callback: DPGCallback | None = None, *, key: int = -1, label: str = None, user_data: Any = None, use_internal_label: bool = True, tag: ItemId = 0, parent: ItemId = 0, show: bool = True, **kwargs) -> DPGCallback | None: ...


def handler_hook(handler_fn: Any, protocol: Callable[P, T] = _handler_fn) -> Callable[...,  Callable[P, T]]:

    def wrap_method(mthd: Any) -> Callable[P, T]:
        @functools.wraps(mthd)
        def mthd_add_handler(self: 'mvHandlerRegistry | mvItemHandlerRegistry', callback = None, *args, parent: ItemId = 0, **kwargs):
            def add_handler(callback):
                handler_fn(callback=callback, parent=parent or self, **kwargs)
                return callback

            if callback is None:
                return add_handler
            return add_handler(callback)

        return mthd_add_handler

    return wrap_method




# This module should be available to use w/o the generated appitems module. Create
# the necessary base(s) if they're missing.
if "mvHandlerRegistry" not in px_items.ITEMTYPE_REGISTRY:

    @px_items.null_registration
    class mvHandlerRegistry(px_items.RegistryItem, px_items.AppItemType):
        command  = dearpygui.add_handler_registry
        identity = dearpygui.mvHandlerRegistry, 'mvAppItemType::mvHandlerRegistry'

        label             : str
        user_data         : Any
        use_internal_label: bool
        show              : bool

else:
    from .appitems import mvHandlerRegistry


class pxHandlerRegistry(mvHandlerRegistry):
    """`mvHandlerRegistry` extension exposing global input handler methods. These methods
    can optionally be used as function decorators.

    The signature of each method slightly differs from the DearPyGui command hook it uses.
    For all methods, the *callback* parameter is the only positional argument (optional).
    All other arguments are optional and keyword-only, including *key* and *button* arguments
    (formerly positional OR keyword) for those that use them. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without parenthesis (you do not
    need to call them). Using parenthesis will allow for passing arguments; in this case, you
    should not include a *callback* argument.
    """

    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...

    @handler_hook(dearpygui.add_mouse_click_handler, _mouse_handler_fn)
    def on_mouse_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button down and up event
        occur on the same object.

        Uses `add_mouse_click_handler`.
        """

    @handler_hook(dearpygui.add_mouse_down_handler, _mouse_handler_fn)
    def on_mouse_click_down(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is clicked/pressed.

        Uses 'add_mouse_down_handler'.
        """

    @handler_hook(dearpygui.add_mouse_release_handler, _mouse_handler_fn)
    def on_mouse_click_up(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is released.

        Uses 'add_mouse_release_handler'.
        """

    @handler_hook(dearpygui.add_mouse_double_click_handler, _mouse_handler_fn)
    def on_mouse_double_click(self, *args, **kwargs):
        """Schedule a callback to run when a mouse click event occurs twice consecutively
        on the same object.

        Uses 'add_mouse_double_click_handler'.
        """

    @handler_hook(dearpygui.add_mouse_wheel_handler, _mouse_handler_fn)
    def on_mouse_wheel(self, *args, **kwargs):
        """Schedule a callback to run on mouse wheel input (excluding middle click).

        Uses 'add_mouse_wheel_handler'.
        """

    @handler_hook(dearpygui.add_mouse_move_handler, _mouse_handler_fn)
    def on_mouse_move(self, *args, **kwargs):
        """Schedule a callback to run when a mouse is moved.

        Uses 'add_mouse_move_handler'.
        """

    @handler_hook(dearpygui.add_mouse_drag_handler, _mouse_handler_fn)
    def on_mouse_drag(self, *args, **kwargs):
        """Schedule a callback to run when a mouse move event occurs during a mouse click
        down event.

        Uses 'add_mouse_drag_handler'.
        """

    @handler_hook(dearpygui.add_key_down_handler, _key_hander_fn)
    def on_key_down(self, *args, **kwargs):
        """Schedule a callback to run on key down input. On many OS, this will fire
        continuously while the key is down.

        Uses 'add_key_down_handler'.

        NOTE: 'Key down' and 'key press' events are similar but not identical -- A 'key down'
        event occurs before a 'key press' event.
        """

    @handler_hook(dearpygui.add_key_press_handler, _key_hander_fn)
    def on_key_press(self, *args, **kwargs):
        """Schedule a callback to run when a key is pressed. On many OS, this will fire
        continuously while the key is pressed.

        Uses 'add_key_press_handler'.

        NOTE: 'Key down' and 'key press' events are similar but not identical -- A 'key press'
        event occurs after a 'key down' event.
        """

    @handler_hook(dearpygui.add_key_release_handler, _key_hander_fn)
    def on_key_up(self, *args, **kwargs):
        """Schedule a callback to run when a key is released.

        Uses `add_key_release_handler`.
        """




# This module should be available to use w/o the generated appitems module. Create
# the necessary base(s) if they're missing.
if "mvItemHandlerRegistry" not in px_items.ITEMTYPE_REGISTRY:

    @px_items.null_registration
    class mvItemHandlerRegistry(px_items.RegistryItem, px_items.AppItemType):
        command  = dearpygui.add_item_handler_registry
        identity = dearpygui.mvItemHandlerRegistry, 'mvAppItemType::mvItemHandlerRegistry'

        label             : str
        user_data         : Any
        use_internal_label: bool
        show              : bool

else:
    from .appitems import mvItemHandlerRegistry


class pxItemHandlerRegistry(mvItemHandlerRegistry):
    """`mvItemHandlerRegistry` extension exposing item handler methods. These methods can
    optionally be used as function decorators.

    The signature of each method slightly differs from the DearPyGui command hook it uses.
    For all methods, the *callback* parameter is the only positional argument (optional).
    All other arguments are optional and keyword-only, including *key* and *button* arguments
    (formerly positional OR keyword) for those that use them. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without parenthesis (you do not
    need to call them). Using parenthesis will allow for passing arguments; in this case, you
    should not include a *callback* argument.
    """

    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...

    @handler_hook(dearpygui.add_item_resize_handler)
    def on_resize(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is resized.

        Uses `add_item_resize_handler`.
        """

    @handler_hook(dearpygui.add_item_clicked_handler, _mouse_handler_fn)
    def on_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button down and button up events
        occur consecutively on a single item bound to this registry.

        Uses `add_item_clicked_handler`.
        """

    @handler_hook(dearpygui.add_item_toggled_open_handler)
    def on_toggle_open(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is toggled open.

        Uses `add_item_toggled_open_handler`.
        """

    @handler_hook(dearpygui.add_item_edited_handler)
    def on_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is edited.

        Uses `add_item_edited_handler`.
        """

    @handler_hook(dearpygui.add_item_deactivated_after_edit_handler)
    def on_deactivation_after_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is deactivated and
        recently edited.

        Uses `add_item_deactivated_after_edit_handler`.
        """

    @handler_hook(dearpygui.add_item_activated_handler)
    def on_activation(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is interacted with.

        Uses `add_item_activated_handler`.
        """

    @handler_hook(dearpygui.add_item_deactivated_handler)
    def on_deactivation(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is deactivated.

        Uses `add_item_deactivated_handler`.
        """

    @handler_hook(dearpygui.add_item_active_handler)
    def while_enabled(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is not disabled.

        Uses `add_item_active_handler`.
        """

    @handler_hook(dearpygui.add_item_visible_handler)
    def while_visible(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is visible.

        Uses `add_item_visible_handler`.
        """

    @handler_hook(dearpygui.add_item_focus_handler)
    def while_focused(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is focused.

        Uses `add_item_focus_handler`.
        """

    @handler_hook(dearpygui.add_item_hover_handler)
    def while_hovered(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is hovered.

        Uses `add_item_hover_handler`.
        """


##########################################
######### CONSTANTS, ENUMS, ETC. #########
##########################################

class Mouse(FrozenNamespace):
    ANY    = -1
    LEFT   =  0
    RIGHT  =  1
    MIDDLE =  2
    X1     =  3
    X2     =  4


class KeyCode(FrozenNamespace):
    # These are not DPG unique, so there's no risk of the values changing
    # between versions.
    ANY              = -1
    BREAK            = 3
    BACKSPACE        = 8
    TAB              = 9
    CLEAR            = 12
    RETURN           = 13
    ENTER            = RETURN
    SHIFT            = 16
    CTRL             = 17
    ALT              = 18
    PAUSE            = 19
    CAPS_LOCK        = 20
    ESC              = 27
    SPACEBAR         = 32
    PAGE_UP          = 33
    PAGE_DN          = 34
    END              = 35
    HOME             = 36
    ARROW_LEFT       = 37
    ARROW_RIGHT      = 38
    ARROW_UP         = 39
    ARROW_DN         = 40
    SELECT           = 41
    PRINT            = 42
    EXEC             = 43
    PRINTSCREEN      = 44
    PRTSCR           = PRINTSCREEN
    INSERT           = 45
    INS              = INSERT
    DELETE           = 46
    DEL              = DELETE
    HELP             = 47
    DIGIT_0          = 48
    DIGIT_1          = 49
    DIGIT_2          = 50
    DIGIT_3          = 51
    DIGIT_4          = 52
    DIGIT_5          = 53
    DIGIT_6          = 54
    DIGIT_7          = 55
    DIGIT_8          = 56
    DIGIT_9          = 57
    A                = 65
    B                = 66
    C                = 67
    D                = 68
    E                = 69
    F                = 70
    G                = 71
    H                = 72
    I                = 73
    J                = 74
    K                = 75
    L                = 76
    M                = 77
    N                = 78
    O                = 79
    P                = 80
    Q                = 81
    R                = 82
    S                = 83
    T                = 84
    U                = 85
    V                = 86
    W                = 87
    X                = 88
    Y                = 89
    Z                = 90
    L_META           = 91
    R_META           = 92
    L_WIN            = L_META
    R_WIN            = R_META
    APPS             = 93
    SLEEP            = 95
    NUMPAD_0         = 96
    NUMPAD_1         = 97
    NUMPAD_2         = 98
    NUMPAD_3         = 99
    NUMPAD_4         = 100
    NUMPAD_5         = 101
    NUMPAD_6         = 102
    NUMPAD_7         = 103
    NUMPAD_8         = 104
    NUMPAD_9         = 105
    NUMPAD_MUL       = 106
    NUMPAD_ADD       = 107
    NUMPAD_SEP       = 108
    NUMPAD_SUB       = 109
    NUMPAD_DEC       = 110
    NUMPAD_DIV       = 111
    F1               = 112
    F2               = 113
    F3               = 114
    F4               = 115
    F5               = 116
    F6               = 117
    F7               = 118
    F8               = 119
    F9               = 120
    F10              = 121
    F11              = 122
    F12              = 123
    F13              = 124
    F14              = 125
    F15              = 126
    F16              = 127
    F17              = 128
    F18              = 129
    F19              = 130
    F20              = 131
    F21              = 132
    F22              = 133
    F23              = 134
    F24              = 135
    NUM_LOCK         = 144
    SCR_LOCK         = 145
    L_SHIFT          = 160
    R_SHIFT          = 161
    L_CTRL           = 162
    R_CTRL           = 163
    L_MENU           = 164
    R_MENU           = 165
    BROWSER_BACK     = 166
    BROWSER_FORWARD  = 167
    BROWSER_REFRESH  = 168
    BROWSER_STOP     = 169
    BROWSER_SEARCH   = 170
    BROWSER_FAVS     = 171
    BROWSER_HOME     = 172
    VOL_MUTE         = 173
    VOL_DN           = 174
    VOL_UP           = 175
    MEDIA_TRACK_NEXT = 176
    MEDIA_TRACK_PREV = 177
    MEDIA_STOP       = 178
    MEDIA_PLAY       = 179
    MEDIA_PAUSE      = MEDIA_PLAY
    LAUNCH_MAIL      = 180
    MEDIA_SELECT     = 181
    LAUNCH_APP1      = 182
    LAUNCH_APP2      = 183
    SEMICOLON        = 186
    PLUS             = 187
    COMMA            = 188
    MINUS            = 189
    PERIOD           = 190
    FORWARD_SLASH    = 191
    TILDE            = 192  # ~
    BRACKET_OPEN     = 219  # [
    BACKSLASH        = 220  #
    BRACKET_CLOSE    = 221
    QUOTE            = 222
    INTL_BACKSLASH   = 226  # \
    UNIDENTIFIED     = 255



