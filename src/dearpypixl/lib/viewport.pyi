from typing import *
from os import PathLike

from dearpypixl.core import interface
from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.lib.items import mvWindowAppItem


__all__ = ("Viewport", "viewport",)




class _FrameCallbackMap(Mapping[int, tuple[ItemCallback, Any]]):
    """An dictionary-like interface for managing a viewport's on-frame
    callbacks. Keys represent a specific frame, while values are 2-tuples
    consisting of the callback that is scheduled to run when rendering that
    frame and the `user_data` it will receive (if any).

    Callbacks are managed by mutating the mapping:
    ```python
    import dearpypixl as dpx

    dpx.Application.create()
    viewport = dpx.Viewport.create()


    # scheduling a callback to run on frame 10
    viewport.frame_callbacks[10] = lambda frame: print(f"called on frame {frame}")

    # scheduling a callback to run on frame 100 with optional `user_data`
    viewport.frame_callbacks[100] = (lambda frame, _, user_data: print(f"called on {user_data} frame {frame}"), "foobar")

    # scheduling a callback to run after rendering the last frame
    viewport.frame_callbacks[-1] = lambda: print("called on exit")

    # delete a scheduled callback — it will not run
    del viewport.frame_callbacks[10]


    viewport.show()
    dpx.start_dearpygui()
    ```

    **NOTE**: Only one instance of this class exists globally. It is created
    when Dear PyPixl is initialized and is accessible via a viewport object's
    :py:property:`Viewport.frame_callbacks` property. Callbacks set using
    Dear PyGui's `set_frame_callback()` and `set_exit_callback()` functions
    are automatically populated in the mapping.
    """
    def __init__(self, /) -> None: ...
    def __len__(self, /) -> int: ...
    def __iter__(self, /) -> Iterator[int]: ...
    def __contains__(self, key: Any, /) -> bool: ...
    def __getitem__(self, frame: int, /) -> tuple[ItemCallback, Any]: ...
    def __setitem__(self, frame: int, value: ItemCallback | tuple[ItemCallback, Any], /) -> None: ...
    def __delitem__(self, frame: int, /) -> None: ...
    @overload
    def get(self, key: int, /) -> tuple[ItemCallback, Any] | None: ...
    @overload
    def get(self, key: int, /, default: tuple[ItemCallback, Any]) -> tuple[ItemCallback, Any]: ...
    @overload
    def get[T](self, key: int, /, default: T) -> tuple[ItemCallback, Any] | T: ...
    @overload
    def set[T: ItemCallback](self, frame: int, /, *, user_data: Any = None) -> Callable[[T], T]: ...
    @overload
    def set[T: ItemCallback | None](self, frame: int, callback: T, /, *, user_data: Any = None) -> T: ...
    @overload
    def pop(self, key: int, /) -> tuple[ItemCallback, Any]: ...
    @overload
    def pop[T](self, key: int, default: T, /) -> tuple[ItemCallback, Any] | T: ...
    @overload
    def pop[T](self, key: Any, default: T, /) -> T: ...
    def popitem(self, /) -> tuple[int, tuple[ItemCallback, Any]]: ...
    def clear(self, /) -> None: ...




type _ViewportCallback = ItemCallback[int | str, tuple[int, int, int, int], Any]
type _FrameBufferCallback = ItemCallback[int | str, mvBuffer, Any]

class _ViewportBaseConfigDict(TypedDict, total=False):
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
    clear_color  : Array[float, Literal[3, 4]]
    disable_close: bool

class _ViewportConfigDict(_ViewportBaseConfigDict, total=False):
    primary_window: Item | None
    callback      : _ViewportCallback | None
    user_data     : Any

class _ViewportStateDict(TypedDict, total=True):
    ok: bool
    pos: list[int]
    rect_size: list[int]
    fullscreen: bool


class Viewport(interface.Interface):
    """An interface for the DearPyGui viewport.

    Like items created using a DearPyPixl interface class, a viewport
    is created and destroyed via the :py:meth:`Viewport.create()` and
    :py:meth:`Viewport.destroy()` methods. The state of the viewport
    is not bound to a specific interface, so multiple interfaces can
    exist for the same viewport once it has been created\*. DearPyGui
    must be initialized before creating the viewport.

    ```python
    import dearpypixl as dpx

    dpx.Application.create()  # OR `create_context(); setup_dearpygui()`

    viewport = dpx.Viewport.create(title="A-Very-Fitting-Title")

    # configure it post-creation via `configure()` or member assignment
    viewport.width = 800
    viewport.height = 600
    viewport.primary_window = dpx.add_window()
    viewport.callback = lambda sender, rect: print(f"viewport resized: {rect}")

    # register on-frame callbacks
    viewport.frame_callbacks[10] = lambda: print("called on frame 10")
    viewport.frame_callbacks[-1] = lambda: print("called on exit/last frame")
    # as a tuple w/user_data
    viewport.frame_callbacks[14] = (
        lambda: sender, user_data: print(f"called on frame 14 with {user_data}"),
        "some-very-fitting-user-data"
    )
    # access returns the callback & user data as a 2-tuple, or `None`
    assert viewport.frame_callbacks[3] is None

    # show the viewport before entering the main loop
    viewport.show()
    dpx.start_dearpygui()
    ```
    *\*As of DearPyGui v2.3.1, only one viewport can be created per
    thread and device context. Even after the viewport has been
    destroyed, the success of creating a new one is not guaranteed.*
    """
    @property
    def tag(self, /) -> int | str: ...
    @classmethod
    def create(cls, **configuration: Unpack[_ViewportConfigDict]) -> Self:
        """Create the DearPyGui viewport and return an interface for
        it. Only one viewport can exist globally, but any number of
        interfaces can exist per viewport.

        **NOTE**: Even once the original viewport has been destroyed,
        it still may not be possible to create a new one within the
        same thread and device context.*
        """
    def destroy(self) -> None:
        """Destroy the viewport if it exists.
        """
    def exists(self, /) -> bool:
        """Return `True` if the viewport has been created and
        still exists.

        ***NOTE**: When this method returns `True`, it is implied that
        :py:meth:`Application.exists()` will also return `True` as
        setting up DearPyGui is required before creating the viewport.*
        """
    @property
    def client_width(self) -> int:
        """[get] the horizontal size of the viewport in pixels."""
    @property
    def client_height(self) -> int:
        """[get] the vertical size of the viewport in pixels."""
    @property
    def title(self, /) -> str:
        """[get, set] the text displayed in the viewport's decoration."""
    @title.setter
    def title(self, value: str, /) -> None: ...
    @property
    def small_icon(self, /) -> str:
        """[get, set] the filepath of the icon displayed in the viewport's
        decoration.

        The ICO (`.ico`) image format is supported across all systems.
        PNG images can be used as icons on non-Windows systems.

        Note that this must be set prior to showing the viewport -- "runtime"
        updates are ignored.
        """
    @small_icon.setter
    def small_icon(self, value: str, /) -> None: ...
    @property
    def large_icon(self, /) -> str:
        """[get, set] the filepath of the icon displayed in the system
        taskbar or application dock.

        The ICO (`.ico`) image format is supported across all systems.
        PNG images can be used as icons on non-Windows systems.

        Note that this must be set prior to showing the viewport -- "runtime"
        updates are ignored.
        """
    @large_icon.setter
    def large_icon(self, value: str, /) -> None: ...
    @property
    def width(self, /) -> int:
        """[get, set] the horizontal size of the viewport's "drawable" space
        in pixels.
        """
    @width.setter
    def width(self, value: int, /) -> None: ...
    @property
    def height(self, /) -> int:
        """[get, set] the vertical size of the viewport's "drawable" space
        in pixels.
        """
    @height.setter
    def height(self, value: int, /) -> None: ...
    @property
    def x_pos(self, /) -> int:
        """[get, set] the viewport's horizontal position relative to the
        screen or desktop.
        """
    @x_pos.setter
    def x_pos(self, value: int, /) -> None: ...
    @property
    def y_pos(self, /) -> int:
        """[get, set] the viewport's vertical position relative to the
        screen or desktop.
        """
    @y_pos.setter
    def y_pos(self, value: int, /) -> None: ...
    @property
    def min_width(self, /) -> int:
        """[get, set] the lower-bound limit of the viewport's width."""
    @min_width.setter
    def min_width(self, value: int, /) -> None: ...
    @property
    def max_width(self, /) -> int:
        """[get, set] the upper-bound limit of the viewport's width."""
    @max_width.setter
    def max_width(self, value: int, /) -> None: ...
    @property
    def min_height(self, /) -> int:
        """[get, set] the lower-bound limit of the viewport's height."""
    @min_height.setter
    def min_height(self, value: int, /) -> None: ...
    @property
    def max_height(self, /) -> int:
        """[get, set] the upper-bound limit of the viewport's height."""
    @max_height.setter
    def max_height(self, value: int, /) -> None: ...
    @property
    def resizable(self, /) -> bool: ...
    @resizable.setter
    def resizable(self, value: bool, /) -> None: ...
    @property
    def vsync(self, /) -> bool: ...
    @vsync.setter
    def vsync(self, value: bool, /) -> None: ...
    @property
    def always_on_top(self, /) -> bool: ...
    @always_on_top.setter
    def always_on_top(self, value: bool, /) -> None: ...
    @property
    def decorated(self, /) -> bool: ...
    @decorated.setter
    def decorated(self, value: bool, /) -> None: ...
    @property
    def clear_color(self, /) -> Array[int | float, Literal[3, 4]]:
        """[get, set] the viewport's background color.

        Note that some systems may ignore the alpha channel.
        """
    @clear_color.setter
    def clear_color(self, value: Array[int | float, Literal[3, 4]], /) -> None: ...
    @property
    def disable_close(self, /) -> bool: ...
    @disable_close.setter
    def disable_close(self, value: bool, /) -> None: ...
    @property
    def primary_window(self, /) -> mvWindowAppItem | None:
        """[***get***, ***set***, ***del***] the `mvWindowAppItem` used as
        the viewport's primary window. A window set as the primary window
        fills the space within the viewport."""
    @primary_window.setter
    def primary_window(self, value: int | str | None, /): ...
    @primary_window.deleter
    def primary_window(self, /) -> None: ...
    @property
    def callback(self, /) -> _ViewportCallback | None:
        """[***get***, ***set***, ***del***] the callback invoked when the
        viewport is resized via user input.

        If supported by the callback, it will recieve the viewport's position
        and size (as a 4-tuple) as the second positional argument.
        """
    @callback.setter
    def callback(self, value: _ViewportCallback | None, /) -> None: ...
    @callback.deleter
    def callback(self, /) -> None: ...
    @property
    def user_data(self, /) -> Any:
        """[***get***, ***set***, ***del***] the payload sent as the third
        positional argument tot he viewport's on-resize callback.
        """
    @user_data.setter
    def user_data(self, value: Any, /) -> None: ...
    @user_data.deleter
    def user_data(self, /) -> None: ...
    def configure(self, /, **kwargs: Unpack[_ViewportConfigDict]) -> None: ...
    def configuration(self) -> _ViewportConfigDict: ...
    @property
    def pos(self, /) -> list[int]:
        """[get, set] the viewport's position relative to the screen or
        desktop."""
    @pos.setter
    def pos(self, value: Sequence[int], /) -> None: ...
    @property
    def is_visible(self, /) -> bool:
        """[***get***] the visibility status of the viewport -- returning
        `True` if the viewport exists and the :py:meth:`show()` method has
        been called at least once.
        """
    @overload
    def show(self, /,) -> None: ...
    @overload
    def show(self, /, *, minimized: bool) -> None: ...
    @overload
    def show(self, /, *, maximized: bool) -> None: ...
    @property
    def is_fullscreen(self, /) -> bool:
        """Return `True` if the viewport's display mode is set to
        borderless/windowed fullscreen."""
    def fullscreen(self, value: bool | None = None, /) -> None:
        """Toggles the borderless fullscreen display mode when *value*
        is omitted, or explicitly enables or disables it otherwise.

        :type value: `bool | None` (*optional*)
        :param value: A boolean indicating the state of the feature.
            `True` enables fullscreen (if not already), while and `False`
            to disable it (if enabled). Defaults to `None`.
        """
    @property
    def rect_size(self, /) -> list[int]: ...
    def state(self) -> _ViewportStateDict: ...
    def minimize(self, /) -> None:
        """Minimize the viewport, hiding it into the taskbar, application
        dock, etc. Does nothing if the viewport is already minimized.

        Implicitly reverts the viewport's display mode if in
        borderless fullscreen.
        """
    def maximize(self, /) -> None:
        """Maximize the viewport, enlarging it to fill the screen's
        available space. Does nothing if the viewport is already maximized.

        Implicitly reverts the viewport's display mode if in
        borderless fullscreen.
        """
    @property
    def frame_callbacks(self, /) -> _FrameCallbackMap:
        """[***get***] the registry of on-frame callbacks as a mapping-like
        object.

        Refer to :py:class:`_FrameCallbackMap` for more information.
        """
    def get_active_window(self) -> Item | None:
        """Returns the identifier of the foreground root window item."""
    def get_mouse_pos(self, /, *, local: bool = True) -> Array[float, Literal[2]]: ...
    def get_mouse_drag_delta(self, /) -> float:
        """Return the distance the mouse cursor has traveled since
        the last update.
        """
    def get_mouse_plot_pos(self, /) -> Array[float, Literal[2]]:
        """Return the position of the mouse cursor relative to the
        active `mvPlot` item.
        """
    def get_mouse_drawing_pos(self, /) -> Array[float, Literal[2]]:
        """Return the position of the mouse cursor relative to the
        active `mvDrawlist` or  `mvViewportDrawlist` item."""

    @overload
    def output_frame_buffer(self, file: str | PathLike[str]) -> None: ...
    @overload
    def output_frame_buffer(self, *, callback: _FrameBufferCallback) -> None: ...
    def output_frame_buffer(self, file: str | PathLike[str] = "", *, callback: _FrameBufferCallback | None = None) -> None:
        """Dump the frame buffer as a PNG image. Can only be called if
        at least one frame has been rendered. Unavailable on MacOS.

        :type file: `str | PathLike[str]` (*optional*)
        :param file: A filename for the image. Defaults to `''`.

        :type callback: `Callable[[Any, mvBuffer], Any] | None` (*optional*)
        :param callback: If specified, DearPyGui will call it next frame
            to process the image data instead of saving it to a file. The
            image data is passed as the second positional argument. Defaults
            to `None`.
        """


def viewport(**configuration: Unpack[_ViewportConfigDict]) -> Viewport:
    """Return a viewport interface, implicitly initializing DearPyGui
    if necessary and creating the viewport if it does not exist.

    :param **kwargs: Initial settings to use when creating the viewport.
        Only used when it is necessary to create the viewport.
    """