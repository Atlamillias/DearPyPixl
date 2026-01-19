import typing
import enum
import time
import collections
import threading

from dearpypixl.core.protocols import Item
from dearpypixl.core import parsing
from dearpypixl.constants import Key, MouseButton
from dearpypixl import items


if parsing.DEARPYGUI_VERSION < (2, 0):
    import ctypes
    _Py_DECREF = ctypes.pythonapi.Py_DecRef
    _Py_DECREF.argtypes = (ctypes.py_object,)
    _Py_DECREF.restype = None
else:
    def _Py_DECREF(object: object, /) -> None:
        pass




# enum conversions are a little slow, so the associations
# are cached for quicker access
_KEYCODE_MAP = {m.value: m for m in Key}
_PTRCODE_MAP = {m.value: m for m in MouseButton}

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

    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex): ...
    @typing.overload
    def __getitem__(self, index: slice): ...
    def __getitem__(self, index: typing.Any):
        return self._inputs[index]

    def __contains__(self, other: typing.Any):
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
            _Py_DECREF(key_info)


    MOUSE_DOWN = InputEvent.MOUSE_DOWN

    def _cb_mouse_down(self, handler: Item, key_info: tuple[int, float]):
        with self.lock:
            self._inputs.append(
                (time.time(), self.MOUSE_DOWN, (_PTRCODE_MAP[key_info[0]], key_info[1]))
            )
            _Py_DECREF(key_info)


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
            _Py_DECREF(cursor_pos)


    MOUSE_DRAG = InputEvent.MOUSE_DRAG

    def _cb_mouse_drag(self, handler: Item, drag_data: tuple[int, float, float]):
        key, x_pos_dt, y_pos_dt = drag_data
        with self.lock:
            self._inputs.append((time.time(), self.MOUSE_DRAG, (_PTRCODE_MAP[key], x_pos_dt, y_pos_dt)))
            _Py_DECREF(drag_data)


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

    _inputs: collections.deque[tuple[float, InputEvent, typing.Any]]

    @typing.overload
    def __init__(   # type: ignore
        self,
        maxlen   : int                    = 10000,
        events   : typing.Collection[InputEvent] = InputEvent,
        inclusive: bool                   = True,
        *,
        label             : str  = ...,
        user_data         : typing.Any  = ...,
        use_internal_label: bool = ...,
        tag               : Item = ...,
        show              : bool = ...,
        **kwargs
    ) -> None: ...
    def __init__(self, maxlen: int = 10000, events: typing.Collection[InputEvent] = InputEvent, inclusive: bool = True, **kwargs):
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
            _Py_DECREF(key_info)


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
            _Py_DECREF(key_info)


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
        _Py_DECREF(mscroll)


    last_drag_delta = (0, 0.0, 0.0)

    def _cb_mouse_drag(self, handler: Item, mdrag_info: tuple[int, float, float]):
        mkey, dt_xpos, dt_ypos =  mdrag_info
        self.last_drag_delta = _PTRCODE_MAP[mkey], dt_xpos, dt_ypos
        _Py_DECREF(mdrag_info)


    cursor_pos = (0.0, 0.0)

    def _cb_mouse_move(self, handler: Item, pos: tuple[float, float]):
        self.cursor_pos = pos
        _Py_DECREF(pos)


