# TODO: rewrite

from __future__ import annotations
from collections import deque
from inspect import Parameter, signature
from typing import (
    Any,
    MutableSequence,
    Literal,
    Sequence,
)
from dearpygui import _dearpygui
from .px_utils import forward_method
from .px_typing import DPGCallback, NULL, T, FrozenNamespace


_VARIADIC_POS    = Parameter.VAR_POSITIONAL
_POSITIONAL_KIND = (Parameter.POSITIONAL_OR_KEYWORD, Parameter.POSITIONAL_ONLY)


def _is_event_callback(_object: Any) -> bool:
    return isinstance(_object, CallbackEvent)


def _get_parg_count(_callable) -> int:
    try:
        params = signature(_callable).parameters.values()
    except TypeError:
        raise TypeError(f"{_callable!r} is not callable.") from None
    except ValueError:
        # built-ins don't have a signature
        if getattr(_callable, "__module__", None) == "builtins":
            raise ValueError(f"Unable to manage builtin object {_callable.__name__!r} (no signature).") from None
        raise
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

def _event_property_getter(target: str):
    def getter(self: CallbackEvent):
        return getattr(self, target)
    return getter

def _event_property_setter(target):
    def setter(self: CallbackEvent, value):
        self.__setattr__(target, value)
        self._set_call_fn()
    return setter




class CallbackEvent(DPGCallback):
    """A wrapper object for callables intended for use as DearPyGui callbacks. Supports
    positional argument overrides and additional keyword-only arguments. Can be used as
    a decorator.
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
        callback : DPGCallback,
        /, *,
        sender   : int   = NULL,
        app_data : Any  = NULL,
        user_data: Any | None = NULL,
        **kwargs,
    ) -> None:
        """Args:
            * callback (Callable[[Any, ...], None]): A callable that accepts zero to three positional
            arguments, any number of keyword-only arguments.

            The following are optional keyword-only arguments. When this object's `__call__` method is
            invoked, these override the corresponding local argument sent.

            * sender (int | None): If included, this will be used as the `sender` (first positional)
            argument instead of the argument sent by DearPyGui.

            * app_data (Any | None): If included, this will be used as the `app_data` (second positional)
            argument instead of the argument sent by DearPyGui.

            * user_data (Any | None):  If included, this will be used as the `sender` (third positional)
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
        # NOTE: This is a pretty error-prone method -- always review after any class
        # code changes.
        n_args = n_args if n_args is not None else _get_parg_count(self._callback)

        local_vars = ("_sender", "_app_data", "_user_data")[0:n_args]
        bound_vals = (self._sender, self._app_data, self._user_data)
        arg_vars   = (var if self_val is not NULL else var.lstrip("_")
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
        """Creates and binds a new `__call__` method that invokes `self.callback`.
        """
        # NOTE: This is a pretty error-prone method -- always review after any class
        # code changes.
        call_fn_txt = (
            "def __call__(sender: int | None | str = None, app_data: Any | None = None, user_data: Any | None = None, /, **kwargs):"
            " _callback({args}**{kwargs})\n"
        )
        self.__call__ = self._create_call_fn(call_fn_txt, n_args)
        self.__code__ = self.__call__.__code__ # incognito DPG callback

    @property
    def callback(self):
        return self._callback
    @callback.setter
    def callback(self, value: T) -> T:  # decorator usage
        pos_arg_cnt = _get_parg_count(value)
        self._callback = value
        self._set_call_fn(n_args=pos_arg_cnt)
        return value

    sender   : int | None     = property(_event_property_getter("_sender")   , _event_property_setter("_sender"))
    app_data : Any | None     = property(_event_property_getter("_app_data") , _event_property_setter("_app_data"))
    user_data: Any | None     = property(_event_property_getter("_user_data"), _event_property_setter("_user_data"))
    kwargs   : dict[str, Any] = property(_event_property_getter("_kwargs")   , _event_property_setter("_kwargs"))


class EventStack(CallbackEvent, MutableSequence[CallbackEvent]):
    """A double-ended queue containing Event instances. When called, all events in the
    stack are called as a result.

    The stack should only contain instances of `Event`. When a non-Event would be added,
    it is wrapped in an Event instance object which is then added to the stack. If the
    object is already an Event instance, it will be added as-is.

    Fun fact: EventStack is a subclass of Event.
    """
    __slots__ = ("_eventstack", "_exec_order", "_exec_once")

    FIRST = "first"
    LAST  = "last"

    def __init__(
        self,
        iterable: Sequence[DPGCallback] = (),
        maxlen  : int = 24,
        *,
        sender    : int | None               = NULL,
        app_data  : Any | None               = NULL,
        user_data : Any | None               = NULL,
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
            (CallbackEvent(cb) if not _is_event_callback(cb) else cb for cb in iterable),
            maxlen=maxlen
        )
        self._callback   = NULL
        self._sender     = sender
        self._app_data   = app_data
        self._user_data  = user_data
        self._kwargs     = kwargs
        self._set_call_fn()

    def _set_call_fn(self, n_args: int = 3):
        """Creates and binds a new `__call__` method that executes the call stack.
        """
        # XXX This is a pretty error-prone method -- always review after any class
        # code changes.
        call_fn_txt = "def __call__(sender: int | None | str = None, app_data: Any | None = None, user_data: Any | None = None, /, **kwargs):\n{}"

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

    def __copy__(self: T) -> T:
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

    def __iadd__(self: T, other) -> T:
        other = (CallbackEvent(cb) if not _is_event_callback(cb) else cb for cb in other)
        self._eventstack.__iadd__(other)
        return self

    def __setitem__(self, index: int, value: DPGCallback) -> None:
        if not _is_event_callback(value):
            value = CallbackEvent(value)
        self._eventstack.__setitem__(index, value)

    @forward_method("_eventstack")
    def __getitem__(self, index: int) -> CallbackEvent: ...
    @forward_method("_eventstack")
    def __delitem__(self, index: int) -> None: ...
    @forward_method("_eventstack")
    def __len__(self) -> int: ...
    @forward_method("_eventstack")
    def __contains__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __lt__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __le__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __gt__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def __ge__(self, *args, **kwargs) -> bool: ...
    @forward_method("_eventstack")
    def count(self, _object: Any) -> int: ...
    @forward_method("_eventstack")
    def index(self, value: CallbackEvent, start: int = 0, stop: int = None): ...
    @forward_method("_eventstack")
    def pop(self) -> CallbackEvent: ...
    @forward_method("_eventstack")
    def popleft(self) -> CallbackEvent: ...
    @forward_method("_eventstack")
    def remove(self) -> None: ...
    @forward_method("_eventstack")
    def rotate(self) -> None: ...
    @forward_method("_eventstack")
    def reverse(self) -> None: ...
    @forward_method("_eventstack")
    def clear(self) -> None: ...

    def insert(self, index: int, _object: DPGCallback) -> None:
        if not _is_event_callback(_object):
            _object = CallbackEvent(_object)
        self._eventstack.insert(index, _object)

    def extend(self, other: Sequence[DPGCallback]) -> None:
        other = (CallbackEvent(cb) if not _is_event_callback(cb) else cb for cb in other)
        self._eventstack.extend(other)

    def extendleft(self, other: Sequence[DPGCallback]) -> None:
        other = (CallbackEvent(cb) if not _is_event_callback(cb) else cb for cb in other)
        self._eventstack.extendleft(other)

    def append(self, _object: DPGCallback) -> None:
        if not _is_event_callback(_object):
            _object = CallbackEvent(_object)
        self._eventstack.append(_object)

    def appendleft(self, _object: DPGCallback) -> None:
        if not _is_event_callback(_object):
            _object = CallbackEvent(_object)
        self._eventstack.appendleft(_object)

    def copy(self: T) -> T:
        return self.__copy__()

    def push(self, _object: T) -> T:
        """Decorator equivelent of `self.append()`."""
        self.append(_object)
        return _object

    def pushleft(self, _object: T) -> T:
        """Decorator equivelent of `self.appendleft()`."""
        self.appendleft(_object)
        return _object

    @property
    def maxlen(self) -> int:
        return self._eventstack.maxlen

    @property
    def callback(self):
        return self.__call__

    exec_order: Literal["first", "last"] = property(
        _event_property_getter("_exec_order"),
        _event_property_setter("_exec_order"),
    )
    exec_once: bool = property(
        _event_property_getter("_exec_once"),
        _event_property_setter("_exec_once"),
    )





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


class Mouse(FrozenNamespace):
    ANY    = -1
    LEFT   = 0
    RIGHT  = 1
    MIDDLE = 2
    X1     = _dearpygui.mvMouseButton_X1
    X2     = _dearpygui.mvMouseButton_X2
