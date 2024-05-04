"""Callback and event-related utilities for Dear PyPixl
and Dear PyGui."""
import time
import enum
import types
import inspect
import functools
import threading
import collections
from inspect import Parameter as _Parameter
from dearpygui import dearpygui
from .constants import KeyInput, MouseInput
from . import (
    api,
    _interface,
    _tools,
)
# BUG: DPG leaks callback arguments. `user_data` is leaked
# in some cases, but `app_data` leaks are plentiful and can
# be a BIG problem. Non-container values are sometimes fine;
# even if these do leak, they're not the primary concern.
# Containters though...we decref those. We decref those to
# *heck*.
from ._tools import Py_DECREF
from ._typing import (
    Any,
    Item,
    ItemCallback,
    ItemConfig,
    Property,
    Iterable,
    Collection,
    Sequence,
    Generic,
    Callable,
    MethodType,
    SupportsIndex,
    ItemInterface,
    TypeVar,
    ParamSpec,
    Self,
    overload,
    override,
    cast,
)
from . import items


_T   = TypeVar("_T")
_N   = TypeVar("_N", float, int)
_P   = ParamSpec("_P")




class _empty: ... # this declaration keeps the typechecker quiet
_empty = _tools.create_marker_type("Empty", __name__)  # type: ignore

Empty = type[_empty]


# NOTE: Several classes (or their instances) with a `__call__` member may
# also have a `__code__` member. This is necessary to make non-function
# instances "DPG-callable", as DearPyGui needs `.__code__.co_argcount` to
# help determine the number of arguments it needs to send to the callback.
# This creates a few issues; variadic arguments cannot be considered by
# only inspecting `__code__.co_argcount` -- which can be empty or may not
# even exist when the callable is a bound method compiled via nuitka or
# another JIT compiler. DPG can't even call a typical bound method
# correctly either since since it can't distinguish `self` from `sender`!
# These issues are relevant here, because they are easily fixed with a better
# `mvRunCallback` implementation -- and that the initial attempt to do so
# broke the "hack" used here to make instances callable. Future attempts
# could as well. A "proper" implementation would better analyze the callback:
#
#   * If an object's `.tp_call` member is not NULL, it's a callable non-
#   function PyObject. `self` is the registered "callback", while the
#   actual callback is `PyObject_GetAttrString(callback, "__call__")`.
#
#   * An object with `__self__` and `__func__` is a bound method. `self` is
#   `PyObject_GetAttrString(callback, "__self__")`, while the actual
#   callback is `PyObject_GetAttrString(callback, "__func__")`.
#
#   * Any other callable is likely a PyCFunction object.
#
#   * The underlying function is always called, not the top-level object
#   (ex. not `obj.method()`, but `method(obj)`). In case 1 or 2, `self`
#   should be considered when reading `.co_argcount`.
#
#   * Parsing variadic params is probably annoying w/o the `inspect`
#   module. Worst-case they can be ignored completely as they aren't
#   included in `.co_argcount`.


_CODE_NO_ARGS = (lambda: ...).__code__



# [ HANDLER REGISTRY EXTENSIONS ]

# handler signatures -- protocols are just more work here

def _handler(
    self,
    callback: ItemCallback | None = None,
    *,
    label             : str | None = None,
    user_data         : Any        = None,
    use_internal_label: bool       = True,
    tag               : Item       = 0,
    parent            : Item       = 0,
    show              : bool       = True,
    **kwargs
) -> ItemCallback | None: ...
def _mouse_handler(
    self,
    callback: ItemCallback | None = None,
    *,
    button            : int        = -1,
    label             : str | None = None,
    user_data         : Any        = None,
    use_internal_label: bool       = True,
    tag               : Item       = 0,
    parent            : Item       = 0,
    show              : bool       = True,
    **kwargs
) -> ItemCallback | None: ...
def _key_hander(
    self,
    callback: ItemCallback | None = None,
    *,
    key               : int        = -1,
    label             : str | None = None,
    user_data         : Any        = None,
    use_internal_label: bool       = True,
    tag               : Item       = 0,
    parent            : Item       = 0,
    show              : bool       = True,
    **kwargs
) -> ItemCallback | None: ...


def handler_hook(handler_fn: Any, protocol: Callable[_P, _T] = _handler) -> Callable[[Callable], Callable[_P, _T]]:
    def wrap_method(mthd: Any) -> Callable[_P, _T]:
        @functools.wraps(mthd)
        def mthd_add_handler(self, callback = None, *args, parent: Item = 0, **kwargs):
            def add_handler(callback):
                handler_fn(
                    callback=callback,
                    parent=parent or self,
                    **kwargs
                )
                return callback

            if callback is None:
                return add_handler
            return add_handler(callback)

        return mthd_add_handler  # type: ignore

    return wrap_method




class HandlerRegistry(items.mvHandlerRegistry):
    """`mvHandlerRegistry` extension exposing global input
    handler methods, which can optionally be used as decorators.

    The signature of each method slightly differs from the
    DearPyGui command hook used. For all methods, the *callback*
    parameter is the only positional argument. All other arguments
    are optional and keyword-only. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without
    parenthesis (you do not need to call them). Using parenthesis
    will allow for passing arguments; in this case, you should not
    include a *callback* argument.

    Command: `dearpygui.add_handler_registry`
    """

    @handler_hook(dearpygui.add_mouse_click_handler, _mouse_handler)
    def on_mouse_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button
        down and up event occur on the same object.

        Command: `dearpygui.add_mouse_click_handler`
        """

    @handler_hook(dearpygui.add_mouse_down_handler, _mouse_handler)
    def on_mouse_click_down(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is
        clicked/pressed.

        Command: `dearpygui.add_mouse_down_handler`
        """

    @handler_hook(dearpygui.add_mouse_release_handler, _mouse_handler)
    def on_mouse_click_up(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is
        released.

        Command: `dearpygui.add_mouse_release_handler`
        """

    @handler_hook(dearpygui.add_mouse_double_click_handler, _mouse_handler)
    def on_mouse_double_click(self, *args, **kwargs):
        """Schedule a callback to run when a mouse click event
        occurs twice consecutively on the same object.

        Command: `dearpygui.add_mouse_double_click_handler`
        """

    @handler_hook(dearpygui.add_mouse_wheel_handler, _mouse_handler)
    def on_mouse_wheel(self, *args, **kwargs):
        """Schedule a callback to run on mouse wheel input
        (excluding middle click).

        Command: `dearpygui.add_mouse_wheel_handler`
        """

    @handler_hook(dearpygui.add_mouse_move_handler, _mouse_handler)
    def on_mouse_move(self, *args, **kwargs):
        """Schedule a callback to run when a mouse is moved.

        Command: `dearpygui.add_mouse_move_handler`
        """

    @handler_hook(dearpygui.add_mouse_drag_handler, _mouse_handler)
    def on_mouse_drag(self, *args, **kwargs):
        """Schedule a callback to run when a mouse move event
        occurs during a mouse click down event.

        Command: `dearpygui.add_mouse_drag_handler`
        """

    @handler_hook(dearpygui.add_key_down_handler, _key_hander)
    def on_key_down(self, *args, **kwargs):
        """Schedule a callback to run on key down input. On
        many OS, this will fire continuously while the key is
        down.

        Command: `dearpygui.add_key_down_handler`

        NOTE: 'Key down' and 'key press' events are similar
        but not identical -- A 'key down' event occurs before
        a 'key press' event.
        """

    @handler_hook(dearpygui.add_key_press_handler, _key_hander)
    def on_key_press(self, *args, **kwargs):
        """Schedule a callback to run when a key is pressed.
        On many OS, this will fire continuously while the key
        is pressed.

        Command: `dearpygui.add_key_press_handler`

        NOTE: 'Key down' and 'key press' events are similar
        but not identical -- A 'key press' event occurs after
        a 'key down' event.
        """

    @handler_hook(dearpygui.add_key_release_handler, _key_hander)
    def on_key_up(self, *args, **kwargs):
        """Schedule a callback to run when a key is released.

        Command: `dearpygui.add_key_release_handler`
        """


class ItemHandlerRegistry(items.mvItemHandlerRegistry):
    """`mvItemHandlerRegistry` extension exposing item handler
    as methods, which can optionally be used as decorators.

    The signature of each method slightly differs from the
    DearPyGui command hook used. For all methods, the *callback*
    parameter is the only positional argument. All other arguments
    are optional and keyword-only. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without
    parenthesis (you do not need to call them). Using parenthesis
    will allow for passing arguments; in this case, you should not
    include a *callback* argument.

    Command: `dearpygui.add_item_handler_registry`
    """

    @handler_hook(dearpygui.add_item_resize_handler)
    def on_resize(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to
        this registry is resized.

        Command: `dearpygui.add_item_resize_handler`
        """

    @handler_hook(dearpygui.add_item_clicked_handler, _mouse_handler)
    def on_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button
        down and button up events occur consecutively on a single
        item bound to this registry.

        Command: `dearpygui.add_item_clicked_handler`
        """

    @handler_hook(dearpygui.add_item_toggled_open_handler)
    def on_toggle_open(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this
        registry is toggled open.

        Command: `dearpygui.add_item_toggled_open_handler`
        """

    @handler_hook(dearpygui.add_item_edited_handler)
    def on_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this
        registry is edited.

        Command: `dearpygui.add_item_edited_handler`
        """

    @handler_hook(dearpygui.add_item_deactivated_after_edit_handler)
    def on_deactivation_after_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this
        registry is deactivated and
        recently edited.

        Command: `dearpygui.add_item_deactivated_after_edit_handler`
        """

    @handler_hook(dearpygui.add_item_activated_handler)
    def on_activation(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this
        registry is interacted with.

        Command: `dearpygui.add_item_activated_handler`
        """

    @handler_hook(dearpygui.add_item_deactivated_handler)
    def on_deactivation(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this
        registry is deactivated.

        Command: `dearpygui.add_item_deactivated_handler`
        """

    @handler_hook(dearpygui.add_item_active_handler)
    def while_enabled(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this
        registry is not disabled.

        Command: `dearpygui.add_item_active_handler`
        """

    @handler_hook(dearpygui.add_item_visible_handler)
    def while_visible(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to
        this registry is visible.

        Command: `dearpygui.add_item_visible_handler`
        """

    @handler_hook(dearpygui.add_item_focus_handler)
    def while_focused(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to
        this registry is focused.

        Command: `dearpygui.add_item_focus_handler`
        """

    @handler_hook(dearpygui.add_item_hover_handler)
    def while_hovered(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to
        this registry is hovered.

        Command: `dearpygui.add_item_hover_handler`
        """




# enum conversions are a little slow, so the associations
# are cached for quicker access
_KEYCODE_MAP = {m.value: m for m in KeyInput}
_PTRCODE_MAP = {m.value: m for m in MouseInput}

class _InputPoller(items.mvHandlerRegistry):
    def __init__(self, *args, **kwargs) -> None:
        if not 'label' in kwargs:
            kwargs['label'] = f'[{type(self).__name__}]'
        super().__init__(*args, **kwargs)
        # Most of the traffic will be from the DPG callback
        # thread, so the necessity of this lock is questionable.
        self.lock = threading.RLock()
        self._inputs = []

    def __iter__(self):
        with self.lock:
            return iter(self._inputs)

    def __len__(self):
        with self.lock:
            return len(self._inputs)

    def __str__(self):
        return str(self._inputs)

    @overload
    def __getitem__(self, index: SupportsIndex): ...
    @overload
    def __getitem__(self, index: slice): ...
    def __getitem__(self, index: Any):
        return self._inputs[index]

    def __contains__(self, other: Any):
        return other in self._inputs


class InputEvent(enum.StrEnum):
    NONE           = "NONE"
    KEY_DOWN       = "KEY_DOWN"
    KEY_UP         = "KEY_UP"
    KEY_PRESS      = "KEY_PRESS"
    MOUSE_DOWN     = "MOUSE_DOWN"
    MOUSE_UP       = "MOUSE_UP"
    MOUSE_MOVE     = "MOUSE_MOVE"
    MOUSE_DRAG     = "MOUSE_DRAG"
    MOUSE_V_SCROLL = "MOUSE_V_SCROLL"


class InputRecorder(_InputPoller):
    """A global handler registry that records input events.
    Useful for logging and debugging.

    The registry behaves like a primitive sequence; supporting
    iteration, indexing, and slicing. Iterating the registry
    yields 3-item tuples containing polled input data. The first
    item is the approx. time of the event as returned by
    `time.time()`. The second indicates the type of input that
    was captured, and is always a member of the `InputEvent`
    string enumeration. The last item is the value Dear PyGui
    sent as `app_data` to the related handler's callback when
    the input event triggered. The value type of the third item
    varies depending on the type of input captured;
        * `InputEvent.KEY_DOWN`: A 2-item list containing the key
        event code and the duration it has been held down in
        fractional seconds.

        * `InputEvent.KEY_UP`: Event code of the key released.

        * `InputEvent.MOUSE_DOWN`: A 2-item tuple containing the
        button event code and the duration it has been held down
        in fractional seconds.

        * `InputEvent.MOUSE_UP`: Event code of the button released.

        * `InputEvent.MOUSE_MOVE`: A 2-item tuple containing the
        x and y position of the cursor relative to the top-left
        corner of the Dear PyGui viewport.

        * `InputEvent.MOUSE_DRAG`: A 3-item tuple containing the
        event code of the button held down and the x/y position
        delta of the cursor. Coordinates are relative to the
        location of the cursor when the button was first pressed.

        * `InputEvent.MOUSE_V_SCROLL`: A single integer indicating
        the direction and intensity of the scroll input. The value
        is positive when a "scroll up" input is captured, and vice-
        versa. The speed or intensity of the input is indicated by
        the integer's absolute value; the higher the value, the
        greater the intensity.

        * `InputEvent.NONE`: Indicates the instantiation of the
        object, and is always the first event "recorded". The
        value is always 0.

    "Push"/"click" events are captured as individual "down"
    and "up" events.
    """

    KEY_DOWN = InputEvent.KEY_DOWN

    def _cb_key_down(self, handler: Item, key_info: tuple[int, float]):
        with self.lock:
            self._inputs.append(
                (time.time(), self.KEY_DOWN, (_KEYCODE_MAP[key_info[0]], key_info[1]))
            )
            Py_DECREF(key_info)


    MOUSE_DOWN = InputEvent.MOUSE_DOWN

    def _cb_mouse_down(self, handler: Item, key_info: tuple[int, float]):
        with self.lock:
            self._inputs.append(
                (time.time(), self.MOUSE_DOWN, (_PTRCODE_MAP[key_info[0]], key_info[1]))
            )
            Py_DECREF(key_info)


    KEY_UP = InputEvent.KEY_UP

    def _cb_key_up(self, handler: Item, key: int):
        with self.lock:
            self._inputs.append((time.time(), self.KEY_UP, _KEYCODE_MAP[key]))


    MOUSE_UP = InputEvent.MOUSE_UP

    def _cb_mouse_up(self, handler: Item, key: int):
        with self.lock:
            self._inputs.append((time.time(), self.MOUSE_UP, _PTRCODE_MAP[key]))


    MOUSE_MOVE = InputEvent.MOUSE_MOVE

    def _cb_mouse_move(self, handler:  Item, cursor_pos: tuple[float, float]):
        with self.lock:
            self._inputs.append((time.time(), self.MOUSE_MOVE, tuple(cursor_pos)))
            Py_DECREF(cursor_pos)


    MOUSE_DRAG = InputEvent.MOUSE_DRAG

    def _cb_mouse_drag(self, handler: Item, drag_data: tuple[int, float, float]):
        key, x_pos_dt, y_pos_dt = drag_data
        with self.lock:
            self._inputs.append((time.time(), self.MOUSE_DRAG, (_PTRCODE_MAP[key], x_pos_dt, y_pos_dt)))
            Py_DECREF(drag_data)


    MOUSE_V_SCROLL = InputEvent.MOUSE_V_SCROLL

    def _cb_mouse_v_scroll(self, handler: Item, value: int):
        with self.lock:
            self._inputs.append((time.time(), self.MOUSE_V_SCROLL, value))


    __INPUT_HOOK_MAP = {
        KEY_DOWN      : items.mvKeyDownHandler,
        KEY_UP        : items.mvKeyReleaseHandler,
        MOUSE_DOWN    : items.mvMouseDownHandler,
        MOUSE_UP      : items.mvMouseReleaseHandler,
        MOUSE_MOVE    : items.mvMouseMoveHandler,
        MOUSE_DRAG    : items.mvMouseDragHandler,
        MOUSE_V_SCROLL: items.mvMouseWheelHandler,
    }

    _inputs: collections.deque[tuple[float, InputEvent, Any]]

    @overload
    def __init__(   # type: ignore
        self,
        maxlen   : int                    = 10000,
        events   : Collection[InputEvent] = InputEvent,
        inclusive: bool                   = True,
        *,
        label             : str  = ...,
        user_data         : Any  = ...,
        use_internal_label: bool = ...,
        tag               : Item = ...,
        show              : bool = ...,
        **kwargs
    ) -> None: ...
    def __init__(self, maxlen: int = 10000, events: Collection[InputEvent] = InputEvent, inclusive: bool = True, **kwargs):
        """Args:
            * maxlen: The length of the cache. Will grow to an
            arbitrary length when set to 0 (note: not a good idea).

            * events: A collection of `InputEvent` members of events
            to capture or ignore, depending on the value of *inclusive*.

            * inclusive: If True, only capture inputs specified in
            *events*. If False, capture all inputs except those
            specified in *events*.
        """
        super().__init__(**kwargs)
        self._inputs = collections.deque(
            [(time.time(), InputEvent.NONE, 0)],
            maxlen=maxlen
        )
        with self:
            for input_tp, h_factory in self.__INPUT_HOOK_MAP.items():
                if inclusive:
                    if input_tp in events:
                        h_factory(callback=getattr(self, f'_cb_{input_tp.lower()}'))
                elif input_tp not in events:
                    h_factory(callback=getattr(self, f'_cb_{input_tp.lower()}'))

    @property
    def oldest(self):
        with self.lock:
            return self._inputs[0]

    @property
    def newest(self):
        with self.lock:
            return self._inputs[-1]


class KeyPoller(_InputPoller):
    """A global handler registry that polls and caches keycode
    inputs.

    The registry is a living cache and behaves like a primitive
    sequence. Iterating through it yields the keys held down at
    the time of the interaction from oldest to newest. It also
    supports indexing and slicing.

    Values of the most recent mouse inputs are cached and
    are exposed via instance attributes;
        * last_pressed: The event code of the most recently-pressed
        key.

        * last_released: The event code of the most recently-
        released key.

    "Push"/"click" events are captured as individual "down"
    and "up" events.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        with self:
            items.mvKeyDownHandler(callback=self._cb_key_down)
            items.mvKeyReleaseHandler(callback=self._cb_key_up)

    def to_chars(self) -> str:
        with self.lock:
            return ''.join(chr(i) for i in self._inputs)

    def keys_pressed(self, *keys: int) -> bool:
        """Return True if a series of keys are currently pressed
        and were pressed in order.
        """
        # BUG: This can return a false positive in niche situations.
        # For example; 'l_ctrl', 'l_shift', and 'f' are pressed in order
        # and are held down. Then, 'l_shift' is released -- passing a
        # key set of `(l_ctrl, f)` at this time would return True.
        with self.lock:
            return ' '.join(str(k) for k in keys) in ' '.join(str(i) for i in self._inputs)


    last_pressed = 0

    def _cb_key_down(self, handler: Item, key_info: tuple[int, float]):
        key = _KEYCODE_MAP[key_info[0]]
        with self.lock:
            self.last_pressed = key
            if key not in self._inputs:
                self._inputs.append(key)
            Py_DECREF(key_info)


    last_released = 0

    def _cb_key_up(self, handler: Item, key: int):
        key = _KEYCODE_MAP[key]
        with self.lock:
            self.last_released = key
            if key in self._inputs:
                self._inputs.remove(key)


class MousePoller(_InputPoller):
    """A global handler registry that polls and caches mouse
    inputs.

    The registry is a living cache and behaves like a primitive
    sequence. Iterating through it yields the mouse buttons held
    down at the time of the interaction from oldest to newest.
    It also supports indexing and slicing.

    Values of the most recent mouse inputs are cached and
    are exposed via instance attributes;
        * cursor_pos: A 2-item sequence of the last known coordinates
        of the mouse cursor, relative to the top-left corner of
        the Dear PyGui viewport.

        * last_pressed: The event code of the most recently-pressed
        mouse button.

        * last_released: The event code of the most recently-
        released mouse button.

        * last_scroll: A single integer indicating the direction
        and intensity of the most recent scroll input. The value
        is positive when a "scroll up" input is captured, and vice-
        versa. The speed or intensity of the input is indicated by
        the integer's absolute value; the higher the value, the
        greater the intensity.

        * last_drag_delta: A 3-item tuple containing the event
        code of the button held down and the x/y position delta
        of the cursor. Coordinates are relative to the location
        of the cursor when the button was initially pressed.

    "Push"/"click" events are captured as individual "down"
    and "up" events.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        with self:
            items.mvMouseDownHandler(callback=self._cb_mouse_down)
            items.mvMouseReleaseHandler(callback=self._cb_mouse_up)
            items.mvMouseWheelHandler(callback=self._cb_mouse_scroll)
            items.mvMouseMoveHandler(callback=self._cb_mouse_move)
            items.mvMouseDragHandler(callback=self._cb_mouse_drag)


    last_pressed = 0

    def _cb_mouse_down(self, handler: Item, key_info: tuple[int, float]):
        mkey = _PTRCODE_MAP[key_info[0]]
        with self.lock:
            self.last_pressed = mkey
            if mkey not in self._inputs:
                self._inputs.append(mkey)
            Py_DECREF(key_info)


    last_released = 0

    def _cb_mouse_up(self, handler: Item, mkey: int):
        mkey = _PTRCODE_MAP[mkey]
        with self.lock:
            self.last_released = 0
            if mkey in self._inputs:
                self._inputs.remove(mkey)


    last_scroll = 0

    def _cb_mouse_scroll(self, handler: Item, mscroll: int):
        self.last_scroll = mscroll
        Py_DECREF(mscroll)


    last_drag_delta = (0, 0.0, 0.0)

    def _cb_mouse_drag(self, handler: Item, mdrag_info: tuple[int, float, float]):
        mkey, dt_xpos, dt_ypos =  mdrag_info
        self.last_drag_delta = _PTRCODE_MAP[mkey], dt_xpos, dt_ypos
        Py_DECREF(mdrag_info)


    cursor_pos = (0.0, 0.0)

    def _cb_mouse_move(self, handler: Item, pos: tuple[float, float]):
        self.cursor_pos = pos
        Py_DECREF(pos)









# [ CALLBACK WRAPPERS ]

_CALLBACK_MARKER = '__item_callback__'


@_tools.frozen_namespace
class _CallArgs:
    SENDER    = 'sender'
    APP_DATA  = 'app_data'
    USER_DATA = 'user_data'


def _count_pargs(_callable: Callable):
    try:
        sig = inspect.signature(_callable)
    except TypeError:
        raise TypeError(f"{_callable!r} is not callable.") from None
    except ValueError: # "built-in"/ c-extension function?
        if _tools.is_builtin(_callable):
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

    priority: Property[int] = _tools.simpleproperty()

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
    def args(self) -> tuple[Item | Empty, Item | Empty, Item | Empty]:
        """A 3-tuple containing "sender", "app_data", and "user_data".
        Any non-`Empty` value will replace the corresponding argument
        sent by Dear PyGui when calling this object.

        [get] Return the overriding positional arguments for
        `self.callback`.

        [set] Set overriding positional arguments for `self.callback`
        """
        return self._call_args  # type: ignore
    @args.setter
    def args(self, value: tuple[Item | Empty, Item | Empty, Item | Empty] | Sequence[Item | Empty] | Empty | None):
        """[set] """
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
            __call__ = _tools.create_function(
                '__call__',
                self.__CALL_ARGS,
                (f'_callback({", ".join(callback_args)})',),
                None,
                globals=globals(),
                locals=call_locals,
            )
            self.__call__ = MethodType(__call__, self)
            self.__code__ = self.__call__.__code__  # type:ignore


class CallStack(Callback):
    """A list-like Dear PyGui-callable object containing other
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

    # BUG: `__call__` must be able to accept a total of 5
    # args, including `self`. This is because DPG sees `self`
    # in `__code__.co_argcount` and tries to pass an additional
    # argument. This wouldn't be an issue of it called `__call__`
    # unbound, but the logic expects functions, so...
    @overload
    def __call__(self, sender: Item = 0, app_data: Any = None, user_data: Any = None, /) -> None: ...  # type:ignore
    def __call__(self, sender: Item = 0, app_data: Any = None, user_data: Any = None, *args) -> None:
        # The lock is not held during execution so callbacks can
        # edit the stack without issue.
        with self._lock:
            # Creating a shallow-copy of the queue is the easiest
            # way to make this op thread-safe while solving key
            # problems. Not the most performant, though...
            callbacks = self.callbacks.copy()
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

    callbacks: Property[list[Callable]] = _tools.simpleproperty()

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


Callstack = CallStack




class Cooldown(Generic[_N]):
    """A wrapper that limits the frequency of a target callable's
    execution over a period of time.


    `Cooldown` objects require a zero-argument callable, a measurement of
    time, and a timer function to initialize. The unit represented by the
    time interval should be consistent with the timer function's return
    value:
        >>> import time
        >>>
        >>>
        >>> # `time.perf_counter()` returns a number of fractional seconds, so
        >>> # *interval* must be a number of seconds.
        >>> cd = Cooldown(lambda: print('foobar'), 1.0, time.perf_counter)

    Once created, calls to the `Cooldown` object are forwarded to the
    underlying callable. Once the callable is executed, it goes on cooldown.
    Any call made to the `Cooldown` object while the callable is on cooldown
    becomes a no-op. The cooldown is lifted once an amount of real time has
    elapsed equal to or greater than the interval value it's assigned --
    Unless the below example is running on a literal potato, "foobar"
    should only appear once as output:
        >>> for _ in range(100_000):
        ...     cd()

    It becomes easier to notice by pacing out our calls. Here, `cd` is called
    twice a second. However, "foobar" will only appear 5 times as output:
        >>> for _ in range(10):
        ...     cd()
        ...     time.sleep(0.5)

    The cooldown interval can be updated at any time by assigning a new value
    to the `.interval` attribute. However, the target callable and the timer
    function cannot be re-assigned.


    `Cooldown` objects support the accumulation of a set number of "uses" for
    the target callable, allowing it to be executed multiple times in short
    succession. This is controlled by the values found on the instance's `stock`
    and `stock_max` attributes. Whenever an amount of real time equal to
    `self.interval` has elapsed, the value of `self.stock` is incremented by 1.
    When calling a `Cooldown` object, its' underlying callable is only executed
    when `self.stock` is at least 1 - the value is decremented by 1 upon
    executing the callable. The default maximum stock value is 1.
        >>> import time
        >>>
        >>>
        >>> # +1 stock every second, up to a max of 5. Additionally, the
        >>> # instance will have an initial stock value of 5.
        >>> cd = Cooldown(lambda: print('foobar'), 1.0, stock_max=5)
        >>>
        >>> # `cd` loses 1 stock every second, given the initial stock and
        >>> # the rate at which they're accumulated. This means that the
        >>> # callback will be ran almost every time `cd` is called over the
        >>> # next 5 seconds; except the very last one, where `cd.stock` will
        >>> # be 0.
        >>> for _ in range(10):
        ...     cd()
        ...     time.sleep(0.5)

    Although uses accumulate over time, the current stock value of a `Cooldown`
    object can be set at any time via the `.stock` attribute, but any new value
    will be automatically clamped to `.stock_max` before assignment. Additionally,
    updating `.stock_max` will clamp `.stock` using the new value. Calling the
    `.refresh` or `.reset` methods will set the stock value to maximum or 0
    respectively.

    """
    __slots__ = (
        'interval',
        '_callback',
        '_stock_max',
        '_stock',
        '_target',
        '_timer',
        '_ts_last_advance',
    )

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        # Event loop performance micro-optimization (`cls.__code__`
        # could just be made a property).
        if cls.__code__ is not cls.__call__.__code__:
            cls.__code__ = cls.__call__.__code__

    def __init__(
        self,
        target   : Callable[[], Any],
        interval : _N = 0.0,
        timer    : Callable[[], _N] = time.perf_counter,
        *,
        stock_max: int = 1,
        callback : Callable[[Self, bool], Any] | None = None,
    ) -> None:
        super().__init__()
        self._ts_last_advance = timer()
        self._target          = target
        self._timer           = timer
        self._stock           = 1.0
        self._stock_max       = 1
        self._callback        = None

        self.callback  = callback
        self.interval  = interval
        self.stock_max = stock_max
        self.stock     = self.stock_max

    def __hash__(self):
        return hash((self._target, self._timer))

    _trunc = staticmethod(float.__trunc__)  # ~2x faster than `int(...)` & floor division

    def __call__(self, *args, clock: Any = None) -> None:
        """Advances the object via `self.advance(clock)`. If `self.stock` is
        at least 1, it is decremented by 1, then `self.target` is called. If
        `self.callback` is then called (if able), receiving `self` and a
        boolean indicating if `self.target` was ran as a result of this call.

        Args:
            - clock: Used as the "time now" value for the advancement.
            Defaults to `self.timer()`.
        """
        self.advance(clock)
        if self._trunc(self._stock):
            # XXX: race-condition risk
            self._stock -= 1.0
            self._target()
            if self._callback is not None:
                self._callback(self, True)
        elif self._callback is not None:
            self._callback(self, False)

    __code__ = __call__.__code__

    @property
    def __wrapped__(self):
        """[Get] the underlying callable."""
        return self._target

    @property
    def timer(self):
        """[Get] the timer function used by the object."""
        return self._timer

    @property
    def clock(self):
        """[Get] the object's internal clock."""
        return self._ts_last_advance

    @property
    def stock_max(self):
        """[Get, Set] the upper limit for the target callable's stock count (min.
        0).

        Additionally, clamp the value of `self.stock` when set.
        """
        return self._stock_max
    @stock_max.setter
    def stock_max(self, count: int, *, __int=int, __min=min, __max=max):  # cached globals for faster access
        # XXX: race-condition risk
        self._stock_max = __int(__max(count, 0))
        self._stock     = __min(self._stock, self._stock_max)

    @property
    def stock(self) -> float:
        """[Get, Set] the number of times the target callable can be invoked in
        short succession (min. 0, max. `self.stock_max`).
        """
        return self._stock
    @stock.setter
    def stock(self, count: float | None):
        self._stock = min(self._stock_max, max(count or 0.0, 0.0))

    @property
    def callback(self) -> Callable[[Self, bool], Any] | None:
        """[Get, Set] a callback that is invoked after calling the instance,
        regardless if the underlying target callable is invoked.

        If callable, it should accept the instance of `Cooldown` (the caller)
        as the sole positional argument.
        """
        if self._callback is None:
            return None
        return self._callback.__func__
    @callback.setter
    def callback(self, value: Callable[[Self, bool], Any] | None):
        if value is not None:
            value = types.MethodType(value, self)  # event loop performance micro-optimization
        self._callback = value

    def forward(self, interval: _N):
        """Update `self.stock` based on `self.interval` and *interval*.

        Does not update the object's internal clock.

        Args:
            - interval: Elapsed time value.
        """
        self.stock += interval / self.interval

    def advance(self, clock: _N | None = None):
        """Advance the object's state based on the amount of time that has
        elapsed since the its' last update.

        Args:
            - clock: Used as the "time now" value for the advancement.
            Defaults to `self.timer()`.
        """
        if clock is None:
            clock = self._timer()
        self.stock += (clock - self._ts_last_advance) / self.interval  # inlined `self.forward`
        self._ts_last_advance = clock

    def refresh(self):
        """Sets `self.stock` to `self.stock_max`.

        Updates the object's internal clock.
        """
        self._ts_last_advance = self.timer()
        self._stock = self._stock_max

    def exhaust(self):
        """Sets `self.stock` to zero and resets the cooldown timer.

        Updates the object's internal clock.
        """
        self._ts_last_advance = self.timer()
        self._stock = 0












# [ UTILITIES ]

@overload
def callback(*, sender: Item = ..., app_data: Any = ..., user_data: Any = ..., priority: int = ...) -> Callback: ...
@overload
def callback(callback: ItemCallback, /, sender: Item = ..., app_data: Any = ..., user_data: Any = ..., priority: int = ...) -> Callback: ...
def callback(callback: Any = None, sender: Any = _empty, app_data: Any = _empty, user_data: Any = _empty, priority: int = 1) -> Any:
    """Convenience decorator for creating `Callback` objects.

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
def cooldown(interval: _N = ..., timer: Callable[[], _N] = ..., **kwargs) -> Callable[[Callable[[], Any]], Cooldown]: ...
@overload
def cooldown(interval: _N = ..., timer: Callable[[], _N] = ..., target: Callable[[], Any] = ..., **kwargs) -> Cooldown: ...

def cooldown(interval: Any = None, timer: Any = None, target: Any = None, *, no_args=None, **kwargs) -> Any:
    """Convenience decorator for creating `Cooldown` objects.

    See the `Cooldown` class for more information
    """
    def capture_callback(target):
        return Cooldown(**kwargs)

    if interval is not None:
        kwargs['interval'] = interval
    if timer is not None:
        kwargs['timer'] = timer
    if target is None:
        return capture_callback
    return capture_callback(target)


cooldown_s = cooldown  # deprecated


def root_ihandler_registry(item: Item) -> items.mvItemHandlerRegistry:
    """Return the item handler registry bound to an item's
    root parent. If unbound, create a new registry,
    bind it to the root parent, and return the new registry.
    """
    root_parent = api.Item.root_parent(item)
    root_ihr = api.Item.information(root_parent)['handlers']
    if not root_ihr:
        root_ihr = items.mvItemHandlerRegistry()
        api.Item.set_handlers(root_parent, root_ihr)
        return root_ihr
    return items.mvItemHandlerRegistry.new(root_ihr)


def resized_fill_content_region(
    item: Item,
    *,
    autosize_x : bool = True,
    autosize_y : bool = True,
) -> items.ResizeHandler:
    """Emulate the behavior of assigning a "stretch" policy
    onto the target item; when its' root parent is resized,
    the target will be sized to consume the available space
    within its' direct parent.

    Args:
        * item: Target item to resize.

        * autosize_x: If True, the target item's width will be
        adjusted to fill its' parent's available space.

        * autosize_y: If True, the target item's height will be
        adjusted to fill its' parent's available space.


    A `TypeError` or `ValueError` is raised when one or more of
    the following conditions are not met prior to calling this
    function;
        - the target item must be non-root item

        - the target item must be sizable via 'width' and/or
        'height' configuration

        - the target item's direct parent must support the
        'content_region_avail' state

        - the target item's root parent must support the
        'resized' state

    This function attaches a `mvResizeHandler` onto the
    target item's root parent. If the root parent does not
    have a bound item handler registry, one is created and
    assigned prior to creating and attaching the handler.
    The created `mvResizeHandler` item is destroyed when the
    callback is triggered and either the target item or its'
    direct parent are destroyed.

    The target's root parent will almost always be a
    `mvWindowAppItem` item, which supports 'resized'. Parent
    items that support 'content_region_avail' include
    `mvChildWindow` and `mvGroup` items. The target can be
    any sizable item, such as a `mvButton`, `mvChildWindow`,
    or `mvPlot` item.
    """
    item        = _interface.mvAll(item)
    item_config = item.configuration()
    item_info   = item.information()
    if (
        (autosize_x and "width" not in item_config) or
        (autosize_y and "height" not in item_config)
    ):
        raise TypeError(
            f"{item_info['type'].split('::')[1]!r} item {item!r} cannot be sized."
        )

    parent = item_info['parent']
    if not parent:
        raise TypeError(
            f"target cannot be a top-level root item."
        )
    parent = _interface.mvAll(parent)

    if not parent.state()['content_region_avail']:
        _parent_tp = parent.information()['type'].split('::')[1]
        raise TypeError(
            f"parent {_parent_tp!r} item does not have a content region."
        )

    get_x_scr_max = dearpygui.get_x_scroll_max
    get_y_scr_max = dearpygui.get_y_scroll_max
    try:
        parent.get_x_scroll_pos()
    except:
        get_x_scr_max = get_y_scr_max = lambda x: 0

    root_parent = cast(_interface.mvAll, item.root_parent)
    root_info   = root_parent.information()
    if not root_info['resized_handler_applicable']:
        raise TypeError(
            f"top-level parent {root_info['type'].split('::')[1]!r} item "
            f"does not support resize handlers."
        )

    root_ihr = root_info['handlers']
    if not root_ihr:
        root_ihr = ItemHandlerRegistry()
        api.Item.set_handlers(root_parent, root_ihr)

    if autosize_x and autosize_y:
        cb_body = (
            "avail_wt, avail_ht = parent.state()['content_region_avail']",
            "item.configure(",
            "    width=avail_wt,",
            "    height=avail_ht,",
            ")",
            "split_frame()",
            "avail_wt, avail_ht = parent.state()['content_region_avail']",
            "item.configure(",
            "    width=max(1, avail_wt - get_x_scr_max(parent)),",
            "    height=max(1, avail_ht - get_y_scr_max(parent)),",
            ")",
        )
    elif autosize_x:
        cb_body = (
            "item.configure(width=parent.state()['content_region_avail'][0])",
            "split_frame()",
            "item.configure(",
            "    width=max(1, parent.state()['content_region_avail'][0] - get_x_scr_max(parent))",
            ")",
        )
    elif autosize_y:
        cb_body = (
            "item.configure(height=parent.state()['content_region_avail'][1])",
            "split_frame()",
            "item.configure(",
            "    height=max(1, parent.state()['content_region_avail'][1] - get_y_scr_max(parent))",
            ")",
        )
    else:
        cb_body = ("...",)

    cb_body = (
        "try:",
        *(f'    {ln}' for ln in cb_body),
        "except SystemError:",
        "    if not item.exists() or not parent.exists():",
        "        handler.callback = None",
        "        handler.destroy()",
        "        del callback",
        "    else:",
        "        raise",
    )

    handler  = items.ResizeHandler.new()
    callback = _tools.create_function(
        'callback',
        (),
        cb_body,
        globals=globals(),
        locals={
            'item'            : _interface.mvAll(item),
            'parent'          : _interface.mvAll(parent),
            'handler'         : handler,
            'get_x_scr_max'   : get_x_scr_max,
            'get_y_scr_max'   : get_y_scr_max,
            'split_frame'     : api.Runtime.split_frame,
        }
    )
    handler.init(callback=callback, parent=root_ihr)
    return handler
