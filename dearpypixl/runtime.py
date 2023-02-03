"""This module contains objects for querying and managing DearPyGui's
runtime and application-level state.

Due to DearPyGui having a global state, all instances of the same
object share their data and state with other instances.
"""
import os
import collections
from typing import Callable, Any, overload
from dearpygui import dearpygui as dpg, _dearpygui as _dpg
from .events import EventStack, CallbackEvent
from .px_utils import forward_method
from .px_typing import DPGCallback, DPGApplicationConfig, DPGViewportConfig



# Users don't need to worry about working around this by *not* calling
# `create_context` just because they imported this module -- there's no
# harm in calling it multiple times.
dpg.create_context()


class Application:
    """Object-oriented and extended API for DearPyGui's application state.

    All instances share the same state.
    """

    __slots__ = ()

    @overload
    def __init__(self, *, docking: bool = ..., docking_space: bool = ..., load_init_file: str = ..., init_file: str = ..., auto_save_init_file: bool = ..., device: int = ..., auto_device: bool = ..., allow_alias_overwrites: bool = ..., manual_alias_management: bool = ..., skip_required_args: bool = ..., skip_positional_args: bool = ..., skip_keyword_args: bool = ..., wait_for_input: bool = ..., manual_callback_management: bool = ..., **kwargs) -> None: ...
    def __init__(self, **kwargs: DPGApplicationConfig):
        self.configure(**kwargs)

    def __getattr__(self, name: str) -> Any:
        try:
            return self.configuration()[name]
        except KeyError:
            raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {name!r}.")

    @property
    def process_id(self) -> int:
        """Return the id of the running process."""
        return os.getpid()

    @property
    def platform(self) -> int:
        """Return the DearPyGui constant value representing the running
        operating system."""
        return _dpg.get_platform()

    @property
    def version(self) -> str:
        """Return the running DearPyGui version as 'major.minor.patch'."""
        return self.configuration()["version"]

    @overload
    def configure(self, *, docking: bool = ..., docking_space: bool = ..., load_init_file: str = ..., init_file: str = ..., auto_save_init_file: bool = ..., device: int = ..., auto_device: bool = ..., allow_alias_overwrites: bool = ..., manual_alias_management: bool = ..., skip_required_args: bool = ..., skip_positional_args: bool = ..., skip_keyword_args: bool = ..., wait_for_input: bool = ..., manual_callback_management: bool = ..., **kwargs) -> None: ...
    def configure(self, **kwargs: DPGApplicationConfig) -> None:
        """Update the application's configuration. If the viewport is showing,
        all options and values are ignored.
        """
        _dpg.configure_app(**kwargs)

    def configuration(self) -> DPGApplicationConfig:
        """Return the application's configuration."""
        return _dpg.get_app_configuration()


class Viewport:
    """Object-oriented (and extended) API for DearPyGui's viewport state.

    All instances all share the same state and data. DearPyGui initialization
    is performed when the first instance is created. If setup is performed
    externally, set `is_initialized` to True on the class before instantiating.
    """

    __slots__ = ()

    __UUID = "DPG NOT USED YET"

    # Because only one DPG viewport can exist, setting these on the class-level
    # means that all instances stay up-to-date. If DPG ever supports multiple
    # viewports, it's trivial to have instances write to themselves instead.
    _is_fullscreen = False
    _pri_wndw_uuid = None

    is_initialized = False

    @overload
    def __init__(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., **kwargs) -> None: ...
    def __init__(self, title: str = "Application", **kwargs: DPGViewportConfig):
        super().__init__(**kwargs)
        if not self.is_initialized:
            type(self).is_initialized = True
            dpg.create_viewport(title=title, **kwargs)
            dpg.setup_dearpygui()

    @property
    def pos(self) -> tuple[int, int]:
        return self.get_rect()[:2]

    @pos.setter
    def pos(self, value: tuple[int, int]) -> None:
        x, y = value
        self.configure(x_pos=x, y_pos=y)

    @property
    def size(self) -> tuple[int, int]:
        return self.get_rect()[2:]

    @size.setter
    def size(self, value: tuple[int, int]) -> None:
        wt, ht = value
        self.configure(width=wt, height=ht)

    @property
    def primary_window(self) -> int | str | None:
        wndw = self._pri_wndw_uuid
        # Has the cached wndw uuid been invalidated via deletion?
        if not wndw:
            exists = False
        elif isinstance(wndw, int):
            exists = _dpg.does_item_exist(wndw)
        elif isinstance(wndw, str):
            exists = _dpg.does_alias_exist(wndw)

        if not exists:
            self._pri_wndw_uuid = wndw = None
        return wndw

    @primary_window.setter
    def primary_window(self, value: int | str | None):
        cls = type(self)
        # "value is None(ish)" -> unset the current primary window
        if not value and cls._pri_wndw_uuid:
            _dpg.set_primary_window(cls._pri_wndw_uuid, False)
            cls._pri_wndw_uuid = None
        # Both are None; do nothing.
        elif not value:
            cls._pri_wndw_uuid = None
        # Set new primary window.
        else:
            cls._pri_wndw_uuid = value
            _dpg.set_primary_window(cls._pri_wndw_uuid, True)

    @property
    def is_showing(self) -> bool:
        return _dpg.is_viewport_ok()

    @property
    def is_fullscreen(self) -> bool:
        return self._is_fullscreen

    # no `is_maximized/minimized` states since use of the title bar buttons
    # would invalidate them immediately

    def fullscreen(self) -> None:
        """Toggles the viewport to borderless fullscreen mode."""
        type(self)._is_fullscreen = not self._is_fullscreen
        _dpg.toggle_viewport_fullscreen()

    def maximize(self) -> None:
        """Maximizes the viewport."""
        # XXX There is no "restore down" command in DPG's API to inverse
        # this. Toggling fullscreen twice will do it but it's not a clean
        # transition.
        if self._is_fullscreen:
            self.fullscreen()
        dpg.maximize_viewport()

    def minimize(self) -> None:
        """Minimizes the viewport."""
        # XXX There is no "restore down" command in DPG's API to inverse
        # this. Toggling fullscreen twice will do it but it's not a clean
        # transition.
        if self._is_fullscreen:
            dpg.toggle_viewport_fullscreen()
        dpg.minimize_viewport()

    def close(self) -> None:
        """Kill the DearPyGui runtime. This is equivelent to closing the application
        window using the title bar's close button.
        """
        if dpg.is_dearpygui_running():
            dpg.stop_dearpygui()

    def show(self) -> None:
        """Begin showing the viewport if it is not already showing."""
        # Calling `show_viewport` multiple times will actually result in additional
        # viewports -- The last viewport made will "consume" the initialization of
        # the real viewport (the one with the *stuff*) at runtime. Worthy of a
        # safety check.
        if not self.is_showing:
            _dpg.show_viewport()

    @overload
    def configure(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., **kwargs) -> None: ...
    def configure(self, **kwargs: DPGViewportConfig) -> None:
        """Update the viewport's configuration. If the viewport is showing,
        'icon'-related options are ignored."""
        dpg.configure_viewport(self.__UUID, **kwargs)

    def configuration(self) -> DPGViewportConfig:
        """Return the viewport's configuration."""
        return _dpg.get_viewport_configuration(self.__UUID)

    def get_rect(self) -> tuple[int, int, int, int]:
        """(Convenience method) Return the position and size of the viewport."""
        cfg = self.configuration()
        return cfg["x_pos"], cfg["y_pos"], cfg["width"], cfg["height"]

    def set_rect(
        self,
        x_pos  : int = None,
        y_pos  : int = None,
        width  : int = None,
        height : int = None,
    ) -> None:
        """(Convenience method) Update the viewport's position and/or size."""
        old_rect = self.get_rect()
        new_rect = x_pos, y_pos, width, height
        # Use current rect values in place of missing ones.
        x, y, wt, ht = (nv or ov for nv, ov in zip(new_rect, old_rect))
        self.configure(x_pos=x, y_pos=y, width=wt, height=ht)



class FrameEvents:
    """A dictionary-like object that manages frame callbacks.

    You can access the callbacks assigned to a specific frame via `<FrameEvents>[<frame>]`.
    Callbacks assigned to frame 0 are those scheduled to run every frame -- Be sure to
    **call** the instance within the render loop to ensure these run.

    A new event stack will be created for the frame the first time it is accessed. Key
    assignment `<FrameEvents>[<frame>] = x` does not assign, but instead appends `x` to
    the frame's stack.

    NOTE: DearPyGui only supports one callback (via `set_frame_callback`) to exist prt
    frame, which are managed by FrameEvents instances. It is hightly suggested to limit
    the number of instances (to 1, ideally) to avoid conflicts between them.
    """
    ALL_FRAMES =  0
    LAST_FRAME = -1

    def __init__(self) -> None:
        super().__init__()
        self._frames: set[int]  = set()
        self._events: dict[int] = collections.defaultdict(EventStack)

        self._events[ 0]  # "all frames"/render callbacks
        self._events[-1]  # "last frame"/exit callbacks
        dpg.set_exit_callback(self._events[-1])

    def __call__(self, *args, **kwargs):
        self._events[0](*args, **kwargs)

    def __getitem__(self, frame: int) -> EventStack:
        fevents = self._events[frame]
        if frame not in self._frames:
            self._frames.add(frame)
            dpg.set_frame_callback(frame, fevents)
        return fevents

    def __setitem__(self, frame: int, callback: DPGCallback) -> None:
        self._events[frame].append(callback)

    @forward_method("_events")
    def get(self, frame: int) -> EventStack: ...

    def on_frame(
        self,
        callback: Callable = None,
        /,
        *,
        frame: int = ALL_FRAMES,
        **kwargs,
    ):
        """(Decorator) Schedules a callback to run on a specific frame.

        Args:
            * callback (Callable): Callable object to run. If *callback* is not an instance of
            `Event`, the callback and all additional keyword arguments other than *frame* are
            passed to Event's constructor.

            * frame (int, optional): The callback will run before this frame is rendered. If this
            value is 0, it will run every frame. If -1, it will run on the last frame (application
            exit). Defaults to 0.

        """
        def _on_frame(_callback):
            self[frame] = (
                _callback
                if isinstance(_callback, CallbackEvent)
                else CallbackEvent(_callback, **kwargs)
            )
            return _callback

        return _on_frame if callback is None else _on_frame(callback)


class RuntimeEvents:
    """Registry system for viewport resize and frame events.

    All instances share the same state and data. Global setup is performed
    when the first instance is created. It's recommended to avoid calling
    `set_viewport_resize_callback` and `set_frame_callback` -- doing so may
    cause instances to behave incorrectly.
    """

    __slots__ = ()

    # Instances need to share state due to the limitations of
    # `set_viewport_resize_callback` and `set_frame_callback`.
    # Individual states would conflict with each other as they
    # would overwrite the others' callbacks.
    _frame_events : FrameEvents = None
    _resize_events: FrameEvents = None

    is_initialized = False

    def __init__(
        self,
        *,
        frame_events: FrameEvents = None,
        resize_events: FrameEvents = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if not self.is_initialized:
            cls = type(self)
            cls.is_initialized = True
            cls._frame_events = frame_events or FrameEvents()
            cls._resize_events = resize_events or FrameEvents()
            # This could be set last-minute before rendering instead,
            # but that would create an extra step for a user if they
            # do not use `Runtime`.
            dpg.set_viewport_resize_callback(self._resize_events[0])

    @property
    def resize_events(self):
        return self._resize_events

    @property
    def frame_events(self):
        return self._frame_events

    @forward_method("_frame_events")
    def on_frame(self, callback: Callable = None, /, *, frame: int = 0, **kwargs):
        """(Decorator) Schedules a callback to run on a specific frame.

        Args:
            * callback (Callable): Callable object to invoke.
            * frame (int): The callback will run before this frame is rendered. If this
            value is 0, it will run every frame. If -1, it will run on the last frame.
            Defaults to 0.

            Any additional keyword arguments are sent to the `Event` callback wrapper.
        """

    @forward_method("_resize_events", "on_frame")
    def on_resize(self, callback: Callable = None, /, **kwargs):
        """(Decorator) Schedules a callback to run when the viewport is resized.
        Args:
            * callback (Callable): Callable object to invoke.

            Any additional keyword arguments are sent to the `Event` callback wrapper.
        """


class Runtime:
    """"""

    __slots__ = (
        "application",
        "viewport",
        "events",
    )

    def __init__(
        self,
        *,
        application: Application = None,
        viewport: Viewport = None,
        events: RuntimeEvents = None,
        **kwargs: DPGApplicationConfig,
    ):
        super().__init__()
        self.application = application or Application(**kwargs)
        self.viewport = viewport or Viewport()
        self.events = events or RuntimeEvents()

    @property
    def is_running(self):
        return _dpg.is_dearpygui_running()

    @overload
    @staticmethod
    def render_frame() -> None: ...  # pyright typing
    render_frame = staticmethod(_dpg.render_dearpygui_frame)

    def start(self, *, post_cleanup_ok: bool = True):
        """Begin rendering the application.

        NOTE: Due to limitations and/or implementation details of DearPyGui, this
        can only be called once per thread.
        """
        if not self.viewport.is_showing:
            self.viewport.show()

        render_frame = self.render_frame
        frame_events = self.events.frame_events
        while self.is_running:
            frame_events()
            render_frame()
        if post_cleanup_ok:
            self.end()

    def stop(self) -> None:
        """Kill the DearPyGui runtime. This is equivelent to closing the application
        window using the title bar's close button.
        """
        return self.viewport.close()

    def end(self) -> None:
        """Post-process clean-up. Releases resources used by DearPyGui."""
        dpg.destroy_context()

    @staticmethod
    def save_init_file(file: str) -> None:
        """Dump an ini file containing the following information:
            - window positions
            - window sizes
            - window collapse state
            - window docking
            - table column widths
            - table column ordering
            - table column visible state
            - table column sorting state

        Window and table items with `no_saved_settings` set to `True` are excluded.
        """
        _dpg.save_init_file(file)

    @staticmethod
    def elapsed_time() -> float:
        """Return the time that has elapsed since the main render loop
        was started.
        """
        return _dpg.get_total_time()

    @staticmethod
    def frames() -> int:
        """Return the number of frames rendered."""
        return _dpg.get_frame_count()

    @staticmethod
    def framerate() -> int:
        """Return the average frames rendered per second (rounded)."""
        return round((_dpg.get_frame_count() or 1) / (_dpg.get_total_time() or 1))

    @staticmethod
    def split_frame(delay: int = 32) -> None:
        """Add a delay (milliseconds) before rendering the next frame."""
        return _dpg.split_frame(delay=delay)

    @staticmethod
    def is_key_pressed(key: int) -> bool:
        """Return True if `key` is pressed, otherwise return False.

        Args:
            * key (int): Key event code to query.
        """
        return _dpg.is_key_down(key)

    @staticmethod
    def is_key_released(key: int) -> bool:
        """Return True if `key` is released, otherwise return False.

        Args:
            * key (int): Key event code to query.
        """
        return _dpg.is_key_down(key)

    @staticmethod
    def is_key_down(key: int) -> bool:
        """Return True if `key` is down, otherwise return False.

        Args:
            * key (int): Key event code to query.
        """
        return _dpg.is_key_down(key)

    @staticmethod
    def get_mouse_global_pos():
        """Return the position of the mouse cursor relative to the viewport."""
        return _dpg.get_mouse_pos(local=False)

    @staticmethod
    def get_mouse_local_pos():
        """Return the position of the mouse cursor relative focused item. If
        no item(s) is focused when called, return the cursor's last position
        relative to the item that was most recently focused (when it was focused).
        """
        return _dpg.get_mouse_pos(local=True)

    @staticmethod
    def get_mouse_plot_pos():
        return _dpg.get_plot_mouse_pos()

    @staticmethod
    def get_mouse_drawing_pos():
        return _dpg.get_drawing_mouse_pos()

    @staticmethod
    def output_frame_buffer(file: str = "", *, callback: Any = None, **kwargs):
        return NotImplemented  # unsupported on MacOS

    if dpg.get_platform() != dpg.mvPlatform_Apple:
        output_frame_buffer = staticmethod(dpg.output_frame_buffer)
