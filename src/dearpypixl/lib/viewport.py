import typing
import inspect
import threading

from dearpygui import dearpygui, _dearpygui

from dearpypixl.core import management
from dearpypixl.core import interface
from dearpypixl.core import codegen
from dearpypixl.core import management
from dearpypixl.core import protocols
from dearpypixl.core.protocols import Property as property, ItemCallback, Array

if typing.TYPE_CHECKING:
    from dearpypixl.lib.items import mvWindowAppItem


__all__ = ("Viewport",)




type _ViewportCallback = (
    protocols.ItemCallback[int | str, tuple[int, int, int, int], typing.Any]
)
type _FrameBufferCallback = (
    protocols.ItemCallback[int | str, protocols.mvBuffer, typing.Any]
)


_MISSING = object()


# [ managed global state ]

class _FrameCallbackMap(typing.Mapping[int, tuple[ItemCallback, typing.Any]]):
    __slots__ = ("_lock", "_mapping",)

    def _set_callback(
        self, /, frame: int, callback: ItemCallback | None, user_data: typing.Any = None,
        *,
        _set_exit_callback=_dearpygui.set_exit_callback,
        _set_frame_callback=_dearpygui.set_frame_callback,
    ) -> None:
        if frame < 0:
            frame = -1
            _set_exit_callback(callback, user_data=user_data)  # ty:ignore[invalid-argument-type]
        else:
            _set_frame_callback(frame, callback, user_data=user_data)  # ty:ignore[invalid-argument-type]
        self._mapping[frame] = (callback, user_data)

    def _del_callback(
        self, /, frame: int,
        *,
        _set_exit_callback=_dearpygui.set_exit_callback,
        _set_frame_callback=_dearpygui.set_frame_callback,
    ) -> None:
        if frame < 0:
            del self._mapping[-1]
            _set_exit_callback(None, user_data=None)  # ty:ignore[invalid-argument-type]
        else:
            del self._mapping[frame]
            _set_frame_callback(frame, None, user_data=None)  # ty:ignore[invalid-argument-type]

    def __init__(self, /) -> None:
        self._lock = threading.Lock()
        self._mapping = {}

    def __len__(self, /) -> int:
        return len(self._mapping)

    def __iter__(self, /):
        with self._lock:
            keys = tuple(self._mapping)
        return iter(keys)

    def __contains__(self, key: typing.Any, /) -> bool:
        if key in self._mapping:
            return True
        try:
            if key < -1:
                return -1 in self._mapping
        except TypeError:
            pass
        return False

    def __getitem__(self, frame: int, /) -> tuple[ItemCallback, typing.Any]:
        try:
            return self._mapping[frame]
        except KeyError:
            if frame < 0 and frame != -1:
                try:
                    return self._mapping[frame]
                except KeyError:
                    pass
            raise

    def __setitem__(self, frame: int, value: ItemCallback | tuple[ItemCallback, typing.Any], /) -> None:
        if isinstance(value, tuple):
            callback, user_data = value
        else:
            callback, user_data = value, None
        with self._lock:
            self._set_callback(frame, callback, user_data)  # type: ignore

    def __delitem__(self, frame: int, /) -> None:
        with self._lock:
            self._del_callback(frame)

    @typing.overload
    def get(self, key: int, /) -> tuple[ItemCallback, typing.Any] | None: ...
    @typing.overload
    def get(self, key: int, /, default: tuple[ItemCallback, typing.Any]) -> tuple[ItemCallback, typing.Any]: ...
    @typing.overload
    def get[T](self, key: int, /, default: T) -> tuple[ItemCallback, typing.Any] | T: ...
    def get(self, key, /, default = None, ):
        return self._mapping.get(key, default)

    @typing.overload
    def set[T: ItemCallback](self, frame: int, /, *, user_data: typing.Any = None) -> typing.Callable[[T], T]: ...
    @typing.overload
    def set[T: ItemCallback | None](self, frame: int, callback: T, /, *, user_data: typing.Any = None) -> T: ...
    def set(self, frame, callback: typing.Any = _MISSING, /, *, user_data=None):
        if callback is not _MISSING:
            with self._lock:
                self._set_callback(frame, callback, user_data)
            return callback

        def wrapper(callback, /):
            with self._lock:
                self._set_callback(frame, callback, user_data)
            return callback

        return wrapper

    @typing.overload
    def pop(self, key: int, /) -> tuple[ItemCallback, typing.Any]: ...
    @typing.overload
    def pop[T](self, key: int, default: T, /) -> tuple[ItemCallback, typing.Any] | T: ...
    @typing.overload
    def pop[T](self, key: typing.Any, default: T, /) -> T: ...
    def pop(self, key, default: typing.Any = _MISSING, /):
        try:
            if key < 0:
                frame = -1
            else:
                frame = key

            with self._lock:
                callback = self._mapping[frame]
                self._del_callback(frame)
                return callback
        except (KeyError, TypeError):
            if default is not _MISSING:
                return default

        raise KeyError(key)

    def popitem(self, /) -> tuple[int, tuple[ItemCallback, typing.Any]]:
        with self._lock:
            value = self._mapping.popitem()
            frame = value[0]
            if frame < 0:
                _dearpygui.set_exit_callback(None, user_data=None)  # type: ignore
            else:
                _dearpygui.set_frame_callback(frame, None, user_data=None)  # type: ignore
        return value

    def clear(self, /) -> None:
        mapping = self._mapping
        with self._lock:
            if -1 in mapping:
                _dearpygui.set_exit_callback(None, user_data=None)  # type: ignore
                del mapping[-1]

            set_frame_callback = _dearpygui.set_frame_callback
            for frame in mapping:
                set_frame_callback(frame, None, user_data=None)  # type: ignore

            mapping.clear()


_FRAME_CALLBACKS = _FrameCallbackMap()




if management.DEARPYGUI_VERSION >= (2, 0):
    _VIEWPORT_UUID = 0
else:
    _VIEWPORT_UUID = "DPG NOT USED YET"

_VIEWPORT_DEFAULTS = typing.cast(dict[str, typing.Any], dearpygui.create_viewport.__kwdefaults__)
assert _VIEWPORT_DEFAULTS is not None


_GLOBAL_LOCK = threading.Lock()


_GLOBAL_CONFIG = dict.fromkeys(("primary_window", "callback", "user_data"), None)


def _get_vp_primary_window() -> mvWindowAppItem | None:  # pyright: ignore[reportRedeclaration]
    global _get_vp_primary_window

    def _get_vp_primary_window(
        *,
        _item_type=interface.Interface.__item_registry__["mvAppItemType::mvWindowAppItem"]
    ) -> mvWindowAppItem | None:
        ...
        config = _GLOBAL_CONFIG

        primary_window = config["primary_window"]
        # check if our "primary_window" state is dirty
        if primary_window and not _dearpygui.does_item_exist(primary_window):
            primary_window = config["primary_window"] = None
        else:
            primary_window = _item_type(tag=primary_window)

        return primary_window

    return _get_vp_primary_window()

def _set_vp_primary_window(primary_window: int | str | None, /) -> None:
    config = _GLOBAL_CONFIG

    main_window = config['primary_window']

    # BUG: The process of setting or unsetting a window as primary
    # makes it lose its "no_scroll_with_mouse" (<=1.10) and
    # "no_scrollbar" flags. They need to be re-applied after the
    # change.

    # replace current primary window with a new one
    if primary_window:
        pwndw_config = _dearpygui.get_item_configuration(primary_window)

        _dearpygui.set_primary_window(primary_window, True)
        config['primary_window'] = primary_window

        _dearpygui.configure_item(
            primary_window,
            no_scrollbar=pwndw_config["no_scrollbar"],
            no_scroll_with_mouse=pwndw_config["no_scroll_with_mouse"],
        )

    # unset the primary window
    elif main_window:
        mwndw_config = _dearpygui.get_item_configuration(main_window)

        _dearpygui.set_primary_window(main_window, False)
        config['primary_window'] = None

        _dearpygui.configure_item(
            main_window,
            no_scrollbar=mwndw_config['no_scrollbar'],
            no_scroll_with_mouse=mwndw_config['no_scroll_with_mouse'],
        )


def _get_vp_callback() -> tuple[typing.Any, typing.Any]:
    return _GLOBAL_CONFIG["callback"], _GLOBAL_CONFIG["user_data"]

def _set_vp_callback(callback: typing.Any = _MISSING, user_data: typing.Any = _MISSING):
    config = _GLOBAL_CONFIG

    if callback is not _MISSING:
        if user_data is _MISSING:
            user_data = config["user_data"]
        _dearpygui.set_viewport_resize_callback(callback, user_data=user_data)
        config["callback"] = callback
        config["user_data"] = user_data

    elif user_data is not _MISSING:
        callback = config["callback"]
        _dearpygui.set_viewport_resize_callback(callback, user_data=user_data)  # ty:ignore[invalid-argument-type]
        config["callback"] = callback
        config["user_data"] = user_data



_GLOBAL_STATE = dict.fromkeys(("ok", "visible", "fullscreen"), False)


def _get_vp_ok():
    return _GLOBAL_STATE["ok"]

def _set_vp_ok(value: bool, /):
    if value:
        _dearpygui.create_viewport(**_VIEWPORT_DEFAULTS)
        _GLOBAL_STATE["ok"] = False
    else:
        _dearpygui.stop_dearpygui()
        _GLOBAL_STATE["ok"] = _GLOBAL_STATE["visible"] = False


def _get_vp_visible():
    return _GLOBAL_STATE["visible"]

def _set_vp_visible():
    _dearpygui.show_viewport(minimized=False, maximized=False)
    _GLOBAL_STATE["visible"] = True


def _get_vp_fullscreen():
    return _GLOBAL_STATE["fullscreen"]

def _set_vp_fullscreen(value=None, /):
    fullscreen = _GLOBAL_STATE["fullscreen"]

    if value is None:
        _dearpygui.toggle_viewport_fullscreen()
        value = not fullscreen
    elif value and not fullscreen:
        _dearpygui.toggle_viewport_fullscreen()
        value = True
    elif fullscreen:
        _dearpygui.toggle_viewport_fullscreen()
        value = False

    _GLOBAL_STATE['fullscreen'] = value

def _set_vp_maximize():
    if _GLOBAL_STATE["fullscreen"]:
        _dearpygui.toggle_viewport_fullscreen()
        _GLOBAL_STATE["fullscreen"] = False
    _dearpygui.maximize_viewport()

def _set_vp_minimize():
    if _GLOBAL_STATE["fullscreen"]:
        _dearpygui.toggle_viewport_fullscreen()
        _GLOBAL_STATE["fullscreen"] = False
    _dearpygui.minimize_viewport()




# [ API patches ]

@management.patch(dearpygui.create_viewport)
def create_viewport(**kwargs: typing.Unpack[_ViewportBaseConfigDict]) -> None:
    with _GLOBAL_LOCK:
        _set_vp_ok(True)
        _dearpygui.configure_viewport(_VIEWPORT_UUID, **kwargs)

create_viewport.__kwdefaults__ = _VIEWPORT_DEFAULTS


@management.patch(dearpygui.show_viewport)
def show_viewport(*, minimized: bool = False, maximized: bool = False, **kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_visible()
        if minimized:
            _set_vp_maximize()
        elif maximized:
            _set_vp_maximize()


@management.patch(dearpygui.set_primary_window)
def set_primary_window(window: int | str, value: bool, **kwargs) -> None:
    with _GLOBAL_LOCK:
        _dearpygui.set_primary_window(window, value)
        if value:
            _GLOBAL_CONFIG["primary_window"] = window
        else:
            _GLOBAL_CONFIG["primary_window"] = None


@management.patch(dearpygui.stop_dearpygui)
def stop_dearpygui(**kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_ok(False)


@management.patch(dearpygui.set_viewport_resize_callback)
def set_viewport_resize_callback(callback: _ViewportCallback | None = None, *, user_data: typing.Any = None, **kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_callback(callback=callback, user_data=user_data)


@management.patch(dearpygui.toggle_viewport_fullscreen)
def toggle_viewport_fullscreen(**kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_fullscreen()


@management.patch(dearpygui.maximize_viewport)
def maximize_viewport(**kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_maximize()


@management.patch(dearpygui.minimize_viewport)
def minimize_viewport(**kwargs) -> None:
    with _GLOBAL_LOCK:
        _set_vp_minimize()


@management.patch(dearpygui.set_frame_callback)
def set_frame_callback(frame: int, callback: ItemCallback | None, *, user_data: typing.Any = None, **kwargs) -> None:
    if frame < 1:
        return

    if callback is None:
        try:
            del _FRAME_CALLBACKS[frame]
        except KeyError:
            pass
    else:
        _FRAME_CALLBACKS.set(frame, callback, user_data=user_data)


@management.patch(dearpygui.set_exit_callback)
def set_exit_callback(callback: ItemCallback | None, *, user_data: typing.Any = None, **kwargs) -> None:
    if callback is None:
        try:
            del _FRAME_CALLBACKS[-1]
        except KeyError:
            pass
    else:
        _FRAME_CALLBACKS.set(-1, callback, user_data=user_data)


_JOB_ARGCOUNTS = {}

@management.patch(dearpygui.run_callbacks)
def run_callbacks(jobs: typing.Sequence[tuple[typing.Callable | None, typing.Any, typing.Any, typing.Any]]) -> None:
    global _JOB_ARGCOUNTS

    for callback, *args in jobs:
        if callback is None:
            continue

        key = id(callback)

        arg_count = _JOB_ARGCOUNTS.get(key, None)
        if arg_count is None:
            parameters = inspect.signature(callback).parameters.values()

            arg_count = 0
            for param in parameters:
                if (
                    arg_count > 3 or
                    param.kind != param.POSITIONAL_ONLY or
                    param.kind != param.POSITIONAL_OR_KEYWORD
                ):
                    break
                arg_count += 1

            _JOB_ARGCOUNTS[key] = arg_count

        if arg_count == 3:
            callback(*args)
        else:
            callback(*args[:arg_count])

    cache_size = len(_JOB_ARGCOUNTS)
    if cache_size > 10_000:
        d = dict(_JOB_ARGCOUNTS.popitem() for _ in range(cache_size // 2))
        # even though we created a new dict, we're going to keep
        # using the old one since the interpreter has already
        # allocated enough memory for it at its largest size
        _JOB_ARGCOUNTS.clear()
        _JOB_ARGCOUNTS.update(d)
        d.clear()




# [ Viewport ]

_PROPERTY_LOCALS = {
    "uuid": _VIEWPORT_UUID,
    "getter": _dearpygui.get_viewport_configuration,
    "setter": _dearpygui.configure_viewport,
}

def _create_config_property( name, /):
    fget = codegen.create_function(
        name, ("self",), (f"return getter(uuid)['{name}']",),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    fset = codegen.create_function(
        name, ("self", "value"), (f"setter(uuid, {name}=value)",),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    return property(fget, fset)

def _config_property() -> typing.Any:
    return codegen.DescriptorDelegate(_create_config_property)


class _ViewportBaseConfigDict(typing.TypedDict, total=False):
    title        : str
    small_icon   : str
    large_icon   : str
    width        : int
    height       : int
    x_pos        : int
    y_pos        : int
    min_width    : int
    max_width    : int
    min_height   : int
    max_height   : int
    resizable    : bool
    vsync        : bool
    always_on_top: bool
    decorated    : bool
    clear_color  : protocols.Array[float, typing.Literal[3, 4]]
    disable_close: bool

class _ViewportConfigDict(_ViewportBaseConfigDict, total=False):
    primary_window: protocols.Item | None
    callback      : _ViewportCallback | None
    user_data     : typing.Any

class _ViewportStateDict(typing.TypedDict, total=True):
    ok: bool
    pos: list[int]
    rect_size: list[int]
    fullscreen: bool


class Viewport(interface.Interface):
    __slots__ = ()

    __itemtype_identity__ = (0, "Viewport")

    @property
    def tag(self, /) -> int | str:
        return _VIEWPORT_UUID

    @classmethod
    def create(cls, **configuration: typing.Unpack[_ViewportConfigDict]) -> typing.Self:
        with _GLOBAL_LOCK:
            _set_vp_ok(True)

        self = cls()
        self.configure(**configuration)
        return self

    def destroy(self) -> None:
        with _GLOBAL_LOCK:
            if _get_vp_ok():
                _set_vp_ok(False)

    @property
    def client_width(self) -> int:
        return _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)['client_width']

    @property
    def client_height(self) -> int:
        return _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)['client_height']

    title: property[str, str] = _config_property()
    small_icon: property[str, str] = _config_property()
    large_icon: property[str, str] = _config_property()
    width: property[int, int] = _config_property()
    height: property[int, int] = _config_property()
    x_pos: property[int, int] = _config_property()
    y_pos: property[int, int] = _config_property()
    min_width: property[int, int] = _config_property()
    max_width: property[int, int] = _config_property()
    min_height: property[int, int] = _config_property()
    max_height: property[int, int] = _config_property()
    resizable: property[bool, bool] = _config_property()
    vsync: property[bool, bool] = _config_property()
    always_on_top: property[bool, bool] = _config_property()
    decorated: property[bool, bool] = _config_property()
    clear_color: property[Array[int | float, typing.Literal[3, 4]], Array[int | float, typing.Literal[3, 4]]] = _config_property()
    disable_close: property[bool, bool] = _config_property()

    @property
    def primary_window(self, /) -> mvWindowAppItem | None:
        with _GLOBAL_LOCK:
            primary_window = _get_vp_primary_window()
        return primary_window
    @primary_window.setter
    def primary_window(self, value: int | str | None, /):
        with _GLOBAL_LOCK:
            _set_vp_primary_window(value)
    @primary_window.deleter
    def primary_window(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_primary_window(None)

    @property
    def callback(self, /) -> _ViewportCallback | None:
        with _GLOBAL_LOCK:
            value = _get_vp_callback()
        return value[0]
    @callback.setter
    def callback(self, value: _ViewportCallback | None, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_callback(value)
    @callback.deleter
    def callback(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_callback(None)

    @property
    def user_data(self, /) -> _ViewportCallback | None:
        with _GLOBAL_LOCK:
            value = _get_vp_callback()
        return value[1]
    @user_data.setter
    def user_data(self, value: _ViewportCallback | None, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_callback(user_data=value)
    @user_data.deleter
    def user_data(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_callback(user_data=None)

    @typing.overload
    def configure(self, /, **kwargs: typing.Unpack[_ViewportConfigDict]) -> None: ...  # pyright: ignore[reportInconsistentOverload]  # ty:ignore[invalid-overload]
    def configure(
        self,
        /, *,
        client_height = None, client_width = None,  # `Viewport(**viewport.configuration())`
        primary_window: typing.Any = _MISSING,
        callback: typing.Any = _MISSING,
        user_data: typing.Any = _MISSING,
        **kwargs
    ) -> None:
        with _GLOBAL_LOCK:
            if primary_window is not _MISSING:
                _set_vp_primary_window(primary_window)
            _set_vp_callback(callback, user_data)
            _dearpygui.configure_viewport(_VIEWPORT_UUID, **kwargs)

    def configuration(self) -> _ViewportConfigDict:
        config = _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)
        with _GLOBAL_LOCK:
            config.update(_GLOBAL_CONFIG)
        return config  # type: ignore

    @property
    def pos(self, /) -> list[int]:
        config = _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)
        return [config["x_pos"], config["y_pos"]]
    @pos.setter
    def pos(self, value: typing.Sequence[int], /) -> None:
        x, y, *_ = value
        _dearpygui.configure_viewport(_VIEWPORT_UUID, x_pos=x, y_pos=y)

    @property
    def is_visible(self, /) -> bool:
        with _GLOBAL_LOCK:
            return _get_vp_visible()

    @typing.overload
    def show(self, *, minimized: bool = ...) -> None: ...
    @typing.overload
    def show(self, *, maximized: bool = ...) -> None: ...
    def show(self, *, minimized: bool = False, maximized: bool = False) -> None:
        with _GLOBAL_LOCK:
            _set_vp_visible()
            if minimized:
                _set_vp_maximize()
            elif maximized:
                _set_vp_maximize()

    @property
    def is_fullscreen(self, /) -> bool:
        with _GLOBAL_LOCK:
            return _get_vp_fullscreen()

    def fullscreen(self, value: bool | None = None, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_fullscreen(value)

    @property
    def rect_size(self, /) -> list[int]:
        config = _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)
        return [config["client_width"], config["client_height"]]

    def state(self) -> _ViewportStateDict:
        state = {}

        config = _dearpygui.get_viewport_configuration(_VIEWPORT_UUID)
        state["rect_size"] = [config["client_width"], config["client_height"]]
        state["pos"] = [config["x_pos"], config["y_pos"]]

        with _GLOBAL_LOCK:
            state.update(_GLOBAL_STATE)

        return state  # type: ignore

    def minimize(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_minimize()

    def maximize(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_vp_maximize()

    @property
    def frame_callbacks(self, /) -> _FrameCallbackMap:
        return _FRAME_CALLBACKS

    def get_active_window(self) -> protocols.Item | None:
        """Returns the identifier of the foreground root window item."""
        return _dearpygui.get_active_window()

    def get_mouse_pos(self, /, *, local: bool = True) -> Array[float, typing.Literal[2]]:
        return _dearpygui.get_mouse_pos(local=local)  # type: ignore

    def get_mouse_drag_delta(self, /) -> float:
        """Return the distance the mouse cursor has traveled since
        the last update.
        """
        return _dearpygui.get_mouse_drag_delta()

    def get_mouse_plot_pos(self, /) -> Array[float, typing.Literal[2]]:
        """Return the position of the mouse cursor relative to the
        active `mvPlot` item.
        """
        return _dearpygui.get_plot_mouse_pos()  # type: ignore

    def get_mouse_drawing_pos(self, /) -> Array[float, typing.Literal[2]]:
        """Return the position of the mouse cursor relative to the
        active `mvDrawlist` or  `mvViewportDrawlist` item."""
        return _dearpygui.get_drawing_mouse_pos()  # type: ignore

    def output_frame_buffer(
        self,
        file: str = "",
        *,
        callback: _FrameBufferCallback | None = None
    ) -> None:
        """Take a screenshot of the viewport's content. Can only be called
        if at least one frame has been rendered. Unavailable on MacOS.

        Args:
            * file: A filename for the screenshot, saved in `.png` format.

            * callback: A DearPyGui-callable callback. If specified, Dear
            PyGui will call it next frame; passing it a `mvBuffer` object
            as the callback's second positional argument. The buffer will
            contain the raw image data.
        """
        dearpygui.output_frame_buffer(file, callback=callback)  # type: ignore

Viewport.create = management.initializer(Viewport.create)  # ty:ignore[invalid-assignment]
