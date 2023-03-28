"""Contains objects for querying and managing DearPyGui's runtime and
application-level states.
"""
import os
import collections
import enum
import time
from dearpygui import dearpygui as dpg, _dearpygui as _dpg
from . import px_utils, px_appstate as _appstate
from .px_items import Config, State, AppItemLike
from .px_utils import staticproperty, classproperty
from .events import Callback, CallStack, TaskerMode
from .px_typing import (
    Any,
    ItemId,
    Callable,
    Null,
    overload,
    DPGCallback,
    DPGApplicationConfig,
    DPGApplicationState,
    DPGViewportConfig,
    DPGViewportState,
)


__all__ = [
    "Application",
    "Viewport",
    "Frame",
    "Runtime"
]




class Application(AppItemLike):
    """Object-oriented interface for DearPyGui's application state.

    All instances operate on the global state. DearPyGui setup is performed when
    the first instance is created.
    """

    __slots__ = ()

    @overload
    def __init__(self, *, docking: bool = ..., docking_space: bool = ..., load_init_file: str = ..., init_file: str = ..., auto_save_init_file: bool = ..., device: int = ..., auto_device: bool = ..., allow_alias_overwrites: bool = ..., skip_required_args: bool = ..., skip_positional_args: bool = ..., skip_keyword_args: bool = ..., wait_for_input: bool = ..., manual_callback_management: bool = ..., **kwargs) -> None: ...
    def __init__(self, **kwargs: DPGApplicationConfig):
        super().__init__()
        self.setup()
        if kwargs:
            self.configure(**kwargs)

    def __getattr__(self, name: str) -> Any:
        try:
            return self.configuration()[name]
        except KeyError:
            raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {name!r}.")

    # ~~ Item API ~~

    theme: Config[ItemId | None, ItemId | None] = Config()
    font : Config[ItemId | None, ItemId | None] = Config()

    @overload
    def configure(self, *, docking: bool = ..., docking_space: bool = ..., load_init_file: str = ..., init_file: str = ..., auto_save_init_file: bool = ..., device: int = ..., auto_device: bool = ..., allow_alias_overwrites: bool = ..., skip_required_args: bool = ..., skip_positional_args: bool = ..., skip_keyword_args: bool = ..., wait_for_input: bool = ..., manual_callback_management: bool = ..., theme: ItemId | None = ..., font: ItemId | None = ..., **kwargs) -> None: ...
    def configure(self, theme: ItemId | None | Null = Null, font: ItemId | None | Null = Null, **kwargs: DPGApplicationConfig) -> None:
        """Update the application's configuration. If the viewport is showing, many all
        options and values are ignored.
        """
        _dpg.configure_app(**kwargs)
        if theme is not Null:
            _dpg.bind_theme(theme)
        if font is not Null:
            _dpg.bind_font(font)

    def configuration(self) -> DPGApplicationConfig:
        """Return the application's configuration."""
        return _dpg.get_app_configuration() | {
            "theme": _appstate._APPLICATION_THEME,
            "font": _appstate._APPLICATION_FONT,
        }

    @classproperty  # inquire w/o prepping app
    def is_set_up(cls) -> bool:
        return Application.state(None)["prepped"]

    def state(self) -> DPGApplicationState:
        return {"prepped": _appstate._APPLICATION_SET_UP}


    # ~~ Properties, Methods ~~

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

    @classmethod
    def create_context(cls) -> None:
        _dpg.create_context()  # XXX: DPG doesn't care when calling multiple times.

    @classmethod
    def destroy_context(cls) -> None:
        _dpg.destroy_context()

    @classmethod
    def setup(cls) -> None:
        """Create the required graphical context for the application and, if necessary,
        initializes DearPyGui via `setup_dearpygui`.
        """
        if not cls.is_set_up:
            cls.create_context()
            _dpg.setup_dearpygui()

    @staticmethod
    def save_ini_file(file: str) -> None:
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




class Viewport(AppItemLike):
    """Object-oriented interface for DearPyGui's viewport.

    All instances operate on the global state. The actual viewport is created
    when the first instance is created.
    """

    __slots__ = ()

    __UUID = "DPG NOT USED YET"

    @overload
    def __init__(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., primary_window: ItemId | None = ..., callback: DPGCallback | None = ..., user_data: Any = ..., **kwargs) -> None: ...
    def __init__(self, **kwargs: DPGViewportConfig):
        super().__init__()
        self.create(title="Application")
        if kwargs:
            self.configure(**kwargs)

    # ~~ Item API ~~

    callback      : Config[DPGCallback | None, DPGCallback | None] = Config()
    user_data     : Config[Any, Any]                               = Config()
    primary_window: Config[ItemId | None, ItemId | None]           = Config()

    @overload
    def configure(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., primary_window: ItemId | None = ..., callback: DPGCallback | None = ..., user_data: Any = ..., **kwargs) -> None: ...
    def configure(self, callback: DPGCallback | None | Null = Null, user_data: Any = Null, primary_window: ItemId | None | Null = Null, **kwargs: DPGViewportConfig) -> None:
        """Update the viewport's configuration. If the viewport is showing,
        'icon'-related options are ignored."""
        _dpg.configure_viewport(self.__UUID, **kwargs)
        if callback is not Null:
            _dpg.set_viewport_resize_callback(callback, _appstate._VIEWPORT_USER_DATA)
        if user_data is not Null:
            _dpg.set_viewport_resize_callback(_appstate._VIEWPORT_RESIZE_CALLBACK, user_data)
        if primary_window is not Null:
            glbl_pri_wndw = _appstate._VIEWPORT_PRIMARY_WINDOW
            # set a new primary window and use it
            if primary_window:
                _dpg.set_primary_window(primary_window, True)
            # attempting to clear the primary window -- pass the previous one but disable it
            elif glbl_pri_wndw:
                _dpg.set_primary_window(glbl_pri_wndw, False)
                _appstate._VIEWPORT_PRIMARY_WINDOW = None
            # both are None -- do nothing
            ...

    def configuration(self) -> DPGViewportConfig:
        """Return the viewport's configuration."""
        config = _dpg.get_viewport_configuration(self.__UUID)
        primary_window = _appstate._VIEWPORT_PRIMARY_WINDOW
        # update a dirty primary window state
        if primary_window and not px_utils.does_itemid_exist(primary_window):
            primary_window = None
            self.configure(primary_window=primary_window)
        config.update(primary_window=primary_window, callback=_appstate._VIEWPORT_RESIZE_CALLBACK)
        return config

    is_visible   : State[bool] = State()
    is_fullscreen: State[bool] = State()

    @classproperty  # inquire w/o forcefully creating vp
    def is_created(cls) -> bool:
        return Viewport.state(None)["created"]

    def state(self) -> DPGViewportState:
        return {
            "created": _appstate._VIEWPORT_CREATED,
            "visible": _dpg.is_viewport_ok(),
            "fullscreen": _appstate._VIEWPORT_FULLSCREEN,
        }


    # ~~ Properties, Methods ~~

    @property
    def pos(self) -> tuple[int, int]:
        config = self.configuration()
        return config["x_pos"], config["y_pos"]
    @pos.setter
    def pos(self, value: tuple[int, int]) -> None:
        x, y = value
        self.configure(x_pos=x, y_pos=y)

    @classmethod
    def create(cls, **kwargs) -> None:
        """Create the DearPyGui viewport. Does nothing if the viewport has already
        been created.

        This method will also do the following (in order, as needed);
            * create the required graphical context for the application
            * initialize DearPyGui

        NOTE: Most application settings will no longer be writable after calling this
        method.
        """
        if not cls.is_created:
            Application.create_context()
            try:
                dpg.create_viewport(**kwargs)
            except SystemError:
                if not Application.is_set_up:
                    Application.setup()
                    dpg.create_viewport(**kwargs)
                raise

    def show(self) -> None:
        """Show the viewport if it's not already visible. The viewport cannot be hidden
        once made visible.

        NOTE: Icon-related viewport settings will not be writable after calling this
        method.
        """
        if not self.is_visible:
            dpg.show_viewport()

    def minimize(self) -> None:
        """Minimizes the viewport. Disables fullscreen mode."""
        _dpg.minimize_viewport()

    def maximize(self) -> None:
        """Maximizes the viewport. Disables fullscreen mode.
        """
        _dpg.maximize_viewport()

    def fullscreen(self) -> None:
        """Enables borderless fullscreen.

        This does not switch between fullscreen modes like `toggle_viewport_fullscreen` --
        use the `.minimize` and `.maximize` methods to disable fullscreen.
        """
        if not self.is_fullscreen:
            _dpg.toggle_viewport_fullscreen()

    def close(self) -> None:
        """Kill the DearPyGui runtime. This is equivelent to closing the application
        window using the title bar's close button.
        """
        if dpg.is_dearpygui_running():
            dpg.stop_dearpygui()

    # ~~ DPG Function Hooks (staticmethods) ~~

    @staticmethod
    def get_global_mouse_pos():
        """Return the position of the mouse cursor relative to the viewport."""
        return _dpg.get_mouse_pos(local=False)

    @staticmethod
    def get_local_mouse_pos():
        """Return the position of the mouse cursor relative focused item.

        If no item(s) is focused when called, return the cursor's last position
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
        if dpg.get_platform == dpg.mvPlatform_Apple:
            return NotImplemented  # unsupported on MacOS
        return _dpg.output_frame_buffer(file, callback=callback)




class Frame(enum.IntEnum):
    """Special frame values for the next, last, and all frames."""
    ALL  = -1
    NEXT = -2
    LAST = -3


class Runtime(AppItemLike):
    """Interface for the main event loop and runtime-level queries.

    All instances operate on the global state. Automatically prepares the runtime
    environment when the first instance is created.
    """

    # XXX: `Runtime` is more of a module w/descriptors than a class. There
    # are no instance methods and very few class methods. Updates are
    # performed on `Runtime` explicitly, not `cls` or `self`.

    def __init__(self, *, stack_factory: type[CallStack] = CallStack, **kwargs):
        super().__init__()
        self.setup(stack_factory=stack_factory)
        if kwargs:
            self.configure(**kwargs)

    @staticmethod
    def setup(*, stack_factory: type[CallStack] = CallStack):
        """Prepares the global runtime environment. Does nothing if the runtime is
        already set up.

        Args:
            * stack_factory: `CallStack` class to use for frame callback setup. Defaults
            to `CallStack`.

        This method will also do the following (in order, as needed);
            * create the required graphical context for the application
            * initialize DearPyGui
            * create the viewport
            * create call stacks for on-frame/runtime updates

        NOTE: Most application settings will no longer be writable after calling this method.
        """
        Application.setup()
        Viewport.create()
        if Runtime._frame_tasks is None:
            Runtime._frame_tasks = collections.defaultdict(stack_factory)
        if Runtime.ALL not in Runtime._frame_tasks:
            Runtime._frame_tasks[Runtime.ALL]  = stack_factory(tasker_mode=TaskerMode.CYCLE)
        if Runtime.NEXT not in Runtime._frame_tasks:
            Runtime._frame_tasks[Runtime.NEXT] = stack_factory(tasker_mode=TaskerMode.POPLEFT)
        if Runtime.LAST not in Runtime._frame_tasks:
            Runtime._frame_tasks[Runtime.LAST] = stack_factory(tasker_mode=TaskerMode.POPLEFT)


    # ~~ Item API ~~

    frame_rate_limit: int | None = classproperty(lambda cls: cls.configuration()["set_up"])
    lock_frame_rate : bool       = classproperty(lambda cls: cls.configuration()["limiting_frames"])

    _frame_rate_limit: int  = 0
    _frame_rate_lock : bool = False

    @overload
    @staticmethod
    def configure(frame_rate_limit: int | None = ..., frame_rate_lock: bool = ..., **kwargs) -> None: ...
    @staticmethod
    def configure(frame_rate_limit: Any = Null, frame_rate_lock: Any = Null, **kwargs) -> None:
        if frame_rate_limit is not Null:
            Runtime._frame_rate_limit = frame_rate_limit or 0
        if frame_rate_lock is not Null:
            Runtime._frame_rate_lock = bool(frame_rate_lock)

    @staticmethod
    def configuration() -> dict[str]:
        return {"frame_rate_limit": Runtime._frame_rate_limit or None, "frame_rate_lock": Runtime._frame_rate_lock}

    is_set_up         : bool = staticproperty(lambda cls: cls.state()["set_up"])
    is_limiting_frames: bool = staticproperty(lambda cls: cls.state()["limiting_frames"])

    @staticproperty
    def is_running() -> bool:
        # this needs to be fast, so it doesn't fetch through `.state()`
        return _dpg.is_dearpygui_running()

    @staticmethod
    def state() -> dict[str, bool]:
        return {
            "set_up"         : Runtime._frame_tasks is not None,
            "running"        : _dpg.is_dearpygui_running(),
            "limiting_frames": bool(Runtime._frame_rate_limit),
        }


    # ~~ Main Event Loop API ~~

    _previous_frame: int = 0

    @staticmethod
    def _schedule_tasks() -> float:
        """Queue callbacks to invoke this (upcoming) frame. Additionally, return the time
        (in milliseconds) this execution took.
        """
        all_frame_tasks = Runtime._frame_tasks
        pending_tasks   = all_frame_tasks[Frame.NEXT]

        start_time = pending_tasks.timer()

        previous_frame = Runtime._previous_frame
        current_frame  = _dpg.get_frame_count() + 1
        # Add tasks from this frame only. If the runtime is behind, tasks from
        # previous frames should still be in-queue.
        if previous_frame + 1 == current_frame:
            pending_tasks._queue.extend(all_frame_tasks.pop(current_frame, ()))
            pending_tasks._queue.extend(all_frame_tasks[Frame.ALL])  # routine tasks

        # The runtime's state is dirty because a frame(s) was rendered outside of
        # the `.start` method. Queue all pending tasks from prior frames.
        elif previous_frame < current_frame:
            for f in range(previous_frame + 1, current_frame):
                pending_tasks._queue.extend(all_frame_tasks.pop(f, ()))
            # XXX maybe nest this into the above loop for accuracy/"fairness"
            pending_tasks._queue.extend(all_frame_tasks[Frame.ALL])  # routine tasks

        # The "current frame" has not been rendered and the task queue has yet to be
        # processed (maybe a duplicate call) -- do nothing.
        else:
            ...

        Runtime._previous_frame = current_frame
        return pending_tasks.timer() - start_time

    @staticmethod
    def _schedule_tasks_manual() -> float:
        if _dpg.get_app_configuration()["manual_callback_management"]:
            Runtime.frame_tasks[Frame.NEXT]._queue.extend(
                Callback(cb, sender=s, app_data=a, user_data=u)
                for cb, s, a, u in _dpg.get_callback_queue()
                if cb is not None
            )
        return Runtime._schedule_tasks()

    @overload
    @staticmethod
    def render_frame(): ...  # pyright inferrence
    render_frame = staticmethod(_dpg.render_dearpygui_frame)

    @classmethod
    def start(cls, *, prerender_frames: int = 0):
        cls.setup()

        if Application().configuration()["manual_callback_management"]:
            schedule_tasks = cls._schedule_tasks_manual
        else:
            schedule_tasks = cls._schedule_tasks
        Viewport().show()
        for _ in range(prerender_frames):
            cls.render_frame()

        infinity = float('inf')
        tasker   = Runtime.frame_tasks[Frame.NEXT].tasker()
        while cls.is_running:
            frlimit = Runtime._frame_rate_limit
            time_avail = 1000 / frlimit if frlimit and Runtime._frame_rate_lock else infinity
            time_used  = schedule_tasks()

            try:
                while time_used < time_avail:
                    time_used += next(tasker)
            except StopIteration:
                pass

            if time_avail != infinity:
                # runtime is ahead -- take a nap
                time.sleep(max(time_avail - time_used, 0) / 1000)

            # XXX: Rendering the frame could take awhile depending on DPG's load. Maybe
            # render first, then update? Seems weird imo.
            cls.render_frame()
        Runtime.frame_tasks[cls.LAST]()

    @classmethod
    def stop(cls):
        if cls.is_running:
            _dpg.stop_dearpygui()
            Runtime.frame_tasks[Frame.LAST]()


    # ~~ On-Frame Callback API ~~

    ALL  = Frame.ALL
    NEXT = Frame.NEXT
    LAST = Frame.LAST

    _frame_tasks: dict[int, CallStack] | None = None

    @staticproperty
    def frame_tasks() -> dict[int, CallStack] | None:
        return Runtime._frame_tasks

    @staticmethod
    def on_frame(callback: Callable = None, /, *, frame: int = Frame.ALL, **kwargs):
        """Schedules a callback to run on a specific frame. Can be used
        as a decorator.

        Args:
            * callback: Callable object to schedule.

            * frame: *callback* will run immediately before rendering this frame.
            Defaults to `Frame.ALL`.
        """
        def _on_frame(_callback):
            task = _callback
            if kwargs:
                task = Callback(_callback, **kwargs)
            Runtime.frame_tasks[frame].append(task)
            return _callback
        return _on_frame if callback is None else _on_frame(callback)

    @classmethod
    def get_task_queue(cls):
        cls._schedule_tasks_manual()
        return Runtime.frame_tasks[cls.NEXT]

    # ~~ DPG Function Hooks (staticmethods) ~~

    @staticproperty
    def frame_count():
        return Runtime.get_frame_count()

    @staticmethod
    def get_frame_count() -> int:
        """Return the number of frames rendered."""
        return _dpg.get_frame_count()

    @staticproperty
    def frame_rate():
        return Runtime.get_frame_rate()

    @staticmethod
    def get_frame_rate() -> int:
        """Return the average frames rate over the last 120 frames."""
        return _dpg.get_frame_rate()

    @staticproperty
    def elapsed_time():
        return Runtime.get_elapsed_time()

    @staticmethod
    def get_elapsed_time() -> float:
        """Return the amount of time passed since rendering the first frame.
        """
        return _dpg.get_total_time()

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
    def split_frame(delay: int = 16) -> None:
        """Ensures that any updates made to DearPyGui following this call are
        postponed until the next frame (at minimum).

        Args:
            * delay: The time in milliseconds to delay updates by.

        All code execution can be delayed (and not just DearPyGui updates) by
        calling `time.sleep` after `.split_frame(delay=0)`.
        """
        return _dpg.split_frame(delay=delay)
