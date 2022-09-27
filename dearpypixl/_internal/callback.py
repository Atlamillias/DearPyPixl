from __future__ import annotations
from collections import deque
from inspect import Parameter, signature
from typing import  Any, MutableSequence, Literal, Protocol, Sequence, TypeVar, overload
from typing_extensions import Self
from .utilities import forward_method
from .comtypes import Null
from dearpygui.dearpygui import get_item_configuration, configure_item


_T = TypeVar("_T")

class Sender(int):
    """Invoker and first positional argument of a DearPyGui callback. This will
    always be an ItemType instance, or the unique identifier of an item if a
    bound ItemType reference for the identifier does not exist.
    """
    __slots__ = ()

class AppData(object):
    """Second positional argument of a DearPyGui callback. This can be of any
    type (including None). If `sender` (preceding argument) is a handler item,
    this can be the the hotkey (`int`) that triggered the invocation (if any). If
    `sender` is an item that can store a value, this will be that value.
    """
    __slots__ = ()

class UserData(object):
    """The third and final positional argument of a DearPyGui callback. This can
    be of any type (including None). It will always be the `user_data` value of
    `sender` (first positional argument).
    """
    __slots__ = ()



_VARIADIC_POS    = Parameter.VAR_POSITIONAL
_POSITIONAL_KIND = (Parameter.POSITIONAL_OR_KEYWORD, Parameter.POSITIONAL_ONLY)


def is_dearpypixl_callback(_object: Any) -> bool:
    return isinstance(_object, Event) or getattr(_object, "__dearpypixl__", None)

def _get_parg_count(_callable) -> int:
    try:
        params = signature(_callable).parameters.values()
    except TypeError:
        raise TypeError(f"{_callable!r} is not callable.") from None
    except ValueError:
        if getattr(_callable, "__module__", None) == "builtins":
            raise ValueError(f"Unable to manage builtin object {_callable.__name__!r} (no signature).") from None
        raise
    # It is not ideal to go through `__code__.co_argcount` due to `__code__` technically
    # being a Python "implementation detail". `co_argcount` also won't include variadic
    # positional arguments (which kinda makes sense).
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

def _event_property_getter(target: str):
    def getter(self: Event):
        return getattr(self, target)
    return getter

def _event_property_setter(target):
    def setter(self: Event, value):
        self.__setattr__(target, value)
        self._set_call_fn()
    return setter


class Callback(Protocol):
    """Any callable object that accepts up to three positional arguments."""
    __slots__ = ("__code__",) # * -> `self.__call__.__code__`
    # *By default, DearPyGui does not support class/instance objects as callbacks. It pulls
    # `__code__` from the object to read its `co_argcount` attribute -- the former only
    # exists on function/method types.

    NULL = Null

    @overload
    def __call__(self, sender: Sender) -> Any: ...
    @overload
    def __call__(self, sender: Sender, app_data: Any) -> Any: ...
    @overload
    def __call__(self, sender: Sender, app_data: Any, user_data: Any) -> Any: ...
    def __call__(self, sender: Sender, app_data: Any, user_data: Any) -> Any: ...


class _Event(Callback):
    __slots__ = ()

    def __call__(self, sender: Sender = None, app_data: AppData = None, user_data: UserData = None, /, **kwargs) -> None: ...


class Event(_Event):
    """A wrapper for callables intended for use as DearPyGui callbacks. Supports positional
    argument overrides and additional keyword-only arguments. Can be used as a decorator.
    """
    __slots__ = (
        "_callback",
        "_sender",
        "_app_data",
        "_user_data",
        "_kwargs",
        "__call__",
    )

    def __init__(
        self,
        callback : Callback,
        /, *,
        sender   : Sender   = Null,
        app_data : AppData  = Null,
        user_data: UserData = Null,
        **kwargs,
    ) -> None:
        """Args:
            * callback (Callable[[Any, ...], None]): A callable that accepts zero to three positional
            arguments, any number of keyword-only arguments. For information regarding the positional
            arguments, see types `Sender`, `AppData`, and `UserData`. To see the full, expected
            signature of this argument, refer to the `Callback` type.

            The following are optional keyword-only arguments. When this object's `__call__` method is
            invoked, these override the corresponding local argument sent.

            * sender (Sender): If included, this will be used as the `sender` (first positional)
            argument instead of the argument sent by DearPyGui.

            * app_data (AppData): If included, this will be used as the `app_data` (second positional)
            argument instead of the argument sent by DearPyGui.

            * user_data (UserData):  If included, this will be used as the `sender` (third positional)
            argument instead of the argument sent by DearPyGui.

            Any additional keyword arguments will be sent to <callback> when called. If you include these,
            ensure that the callback can accept them.
        """
        self._callback  = callback
        self._sender    = sender
        self._app_data  = app_data
        self._user_data = user_data
        self._kwargs    = kwargs
        self.__call__   = None  # rebuilt on property set

        self.callback   = self._callback

    def __repr__(self):
        return f"{type(self).__qualname__}(callback={self._callback!r}, sender={self._sender!r})"

    def _create_call_fn(self, func_str: str, n_args: int = 0):
        n_args = n_args if n_args is not None else _get_parg_count(self._callback)

        local_vars = ("_sender", "_app_data", "_user_data")[0:n_args]
        bound_vals = (self._sender, self._app_data, self._user_data)
        arg_vars   = (var if self_val is not Null else var.lstrip("_")
                        for var, self_val in zip(local_vars, bound_vals))
        kwargs_var = "_kwargs" if self._kwargs else "kwargs"

        # The "argument string" passed to the callback is pre-built to reduce the on-call overhead
        # introduced by the wrapper.
        call_fn_txt = func_str.format(args=''.join(f'{a},' for a in arg_vars), kwargs=kwargs_var)
        localizer   = (
            "def __call_fn__(self, _callback, _sender, _app_data, _user_data, /, **_kwargs):\n"
            "    {fn}"
            "    return __call__"
        ).format(fn=call_fn_txt)

        ns = {}
        exec(localizer, None, ns)
        return ns["__call_fn__"](self, self._callback, *bound_vals, **self._kwargs)

    def _set_call_fn(self, n_args: int = 0):
        """Creates a new function that invokes `self.callback` (bound to `self.__call__`).
        """
        call_fn_txt = (
            "def __call__(sender: int | str = None, app_data: Any = None, user_data: Any = None, /, **kwargs):"
            " _callback({args}**{kwargs})\n"
        )
        self.__call__ = self._create_call_fn(call_fn_txt, n_args)
        self.__code__ = self.__call__.__code__ # used by DPG

    @property
    def callback(self):
        return self._callback
    @callback.setter
    def callback(self, value: _T) -> _T:  # decorator usage
        pos_arg_cnt = _get_parg_count(value)
        self._callback = value
        self._set_call_fn(n_args=pos_arg_cnt)
        return value

    sender   : Sender         = property(_event_property_getter("_sender")   , _event_property_setter("_sender"))
    app_data : AppData        = property(_event_property_getter("_app_data") , _event_property_setter("_app_data"))
    user_data: UserData       = property(_event_property_getter("_user_data"), _event_property_setter("_user_data"))
    kwargs   : dict[str, Any] = property(_event_property_getter("_kwargs")   , _event_property_setter("_kwargs"))


class EventStack(Event, MutableSequence[Event]):
    """A double-ended queue containing Event instances. When called, all events in the
    stack are called as a result.

    The stack should only contain instances of `Event` or `Item`. When a non-Event or Item
    object would be added, an `Event` object is created for it and is added to the stack
    instead. If the object is already an Event instance, it will be added to the stack
    as-is (fun fact: this is an `Event` subclass).

    """
    __slots__ = ("_eventstack", "_exec_order", "_exec_once")

    FIRST = "first"
    LAST  = "last"

    def __init__(
        self,
        iterable: Sequence[Callback] = (),
        maxlen  : int = 24,
        *,
        sender    : Sender                   = Null,
        app_data  : AppData                  = Null,
        user_data : UserData                 = Null,
        exec_order: Literal["first", "last"] = FIRST,
        exec_once : bool                     = False,
        **kwargs,
    ) -> None:
        """Args:
            * iterable (Sequence[Callback]): A sequence containing suitable DearPyGui callback arguments.

            * maxlen (int): Maximum size of the stack. When adding a value to the stack would cause it
            to be filled over capacity, the left-most value in the stack is removed first before adding
            the value.

            The following are optional keyword-only arguments.

            * sender (Sender): If included, this will be used as the `sender` (first positional)
            argument for each event called, instead of the argument sent by DearPyGui. If `Event().sender`
            is set on the event, it will be used over this one.

            * app_data (AppData): If included, this will be used as the `app_data` (second positional)
            argument for each event called, instead of the argument sent by DearPyGui. If `Event().app_data`
            is set on the event, it will be used over this one.

            * user_data (UserData): If included, this will be used as the `sender` (third positional)
            argument for each event called, instead of the argument sent by DearPyGui. If `Event().user_data`
            is set on the event, it will be used over this one.

            * exec_order (Literal[str]): Indicates which end of the stack will be used as the "starting
            point" when called. If set to "first", events in the stack will be called from left to right.
            Vice-versa if set to "last". Defaults to "first".

            * exec_once (bool): If True, the event will be removed from the stack when called as a
            result of calling the stack itself. Defaults to False.

            Any additional keyword arguments will be sent to each event called. If you include these,
            ensure that **all callbacks in the stack** can accept them. If `Event().kwargs` is set on the
            event, those keyword arguments will be used instead of these.
        """
        self._exec_order = exec_order
        self._exec_once  = exec_once
        self._eventstack  = deque(
            (Event(cb) if not is_dearpypixl_callback(cb) else cb for cb in iterable),
            maxlen=maxlen
        )
        self._callback   = Null
        self._sender     = sender
        self._app_data   = app_data
        self._user_data  = user_data
        self._kwargs     = kwargs
        self._set_call_fn()

    def _set_call_fn(self, n_args: int = 3):
        """Creates a new function that runs the call stack (bound to `self.__call__`).
        """
        call_fn_txt = "def __call__(sender: int | str = None, app_data: Any = None, user_data: Any = None, /, **kwargs):\n{}"

        if self._exec_once:
            pop_fn_txt   = ("        callstack=self._eventstack\n"
                            "        pop_fn=callstack.{}\n")
            loop_stmt_txt = "        while callstack: pop_fn().__call__({args}**{kwargs})\n"
            if self._exec_order == self.FIRST:
                loop_stmt_txt = pop_fn_txt.format("popleft") + loop_stmt_txt
            else:
                loop_stmt_txt = pop_fn_txt.format("pop") + loop_stmt_txt
        else:
            loop_stmt_txt = ("        callstack=self._eventstack\n"
                             "        for event in {}:")
            if self._exec_order == self.FIRST:
                loop_stmt_txt = loop_stmt_txt.format("callstack")
            else:
                loop_stmt_txt = loop_stmt_txt.format("reversed(callstack)")
            loop_stmt_txt += " event.__call__({args}**{kwargs})\n"

        call_fn_txt = call_fn_txt.format(loop_stmt_txt)
        self.__call__ = self._create_call_fn(call_fn_txt, 3)
        self.__code__ = self.__call__.__code__  # used by DPG

    def __repr__(self):
        return f"{type(self).__qualname__}(callbacks={self.__len__()!r}, maxlen={self.maxlen!r}, sender={self._sender!r})"

    def __iter__(self):
        yield from self._eventstack

    def __bool__(self) -> bool:
        return bool(self._eventstack)

    def __copy__(self) -> Self:
        self_copy = type(self)(
            (),
            self.maxlen,
            sender=self._sender,
            app_data=self._app_data,
            user_data=self._user_data,
            exec_order=self._exec_order,
            exec_once=self._exec_once,
            **self._kwargs,
        )
        self_copy._eventstack.extend(self._eventstack)
        return self_copy

    def __iadd__(self, other) -> Self:
        other = (Event(cb) if not is_dearpypixl_callback(cb) else cb for cb in other)
        self._eventstack.__iadd__(other)
        return self

    # rich comparisons
    @forward_method("_eventstack")
    def __lt__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __le__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __gt__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __ge__(self, *args, **kwargs) -> bool: ...
    # ABC
    @forward_method("_eventstack")
    def __len__(self) -> int: ...
    @forward_method("_eventstack")
    def __getitem__(self, index: int) -> Event: ...

    def __setitem__(self, index: int, value: Callback) -> None:
        if not is_dearpypixl_callback(value):
            value = Event(value)
        self._eventstack.__setitem__(index, value)

    @forward_method("_eventstack")
    def __delitem__(self, index: int) -> None: ...
    @forward_method("_eventstack")
    def __contains__(self, *args, **kwargs) -> bool: ...

    @forward_method("_eventstack")
    def insert(self, index: int, _object: Callback) -> None:
        if not is_dearpypixl_callback(_object):
            _object = Event(_object)
        self._eventstack.insert(index, _object)

    # deque methods
    @forward_method("_eventstack")
    def count(self, _object: Any) -> int: ...

    def extend(self, other: Sequence[Callback]) -> None:
        other = (Event(cb) if not is_dearpypixl_callback(cb) else cb for cb in other)
        self._eventstack.extend(other)

    def extendleft(self, other: Sequence[Callback]) -> None:
        other = (Event(cb) if not is_dearpypixl_callback(cb) else cb for cb in other)
        self._eventstack.extendleft(other)

    @forward_method("_eventstack")
    def index(self, value: Event, start: int = 0, stop: int = None): ...
    @forward_method("_eventstack")
    def pop(self) -> Event: ...
    @forward_method("_eventstack")
    def popleft(self) -> Event: ...
    @forward_method("_eventstack")
    def remove(self) -> None: ...
    @forward_method("_eventstack")
    def rotate(self) -> None: ...
    @forward_method("_eventstack")
    def reverse(self) -> None: ...
    @forward_method("_eventstack")
    def clear(self) -> None: ...

    def append(self, _object: Callback) -> None:
        if not is_dearpypixl_callback(_object):
            _object = Event(_object)
        self._eventstack.append(_object)

    def appendleft(self, _object: Callback) -> None:
        if not is_dearpypixl_callback(_object):
            _object = Event(_object)
        self._eventstack.appendleft(_object)

    def copy(self) -> Self:
        return self.__copy__()

    def push(self, _object: _T) -> _T:
        """Decorator equivelent of `self.append()`."""
        self.append(_object)
        return _T

    def pushleft(self, _object: _T) -> _T:
        """Decorator equivelent of `self.appendleft()`."""
        self.appendleft(_object)
        return _T

    @property
    def maxlen(self) -> int:
        return self._eventstack.maxlen

    @property
    def callback(self):
        return self.__call__
