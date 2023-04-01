"""Contains objects for querying and managing DearPyGui's runtime and
application-level states.
"""
import os
import collections
import enum
import time
from dearpygui import dearpygui as dpg, _dearpygui as _dpg
from . import px_appstate as _appstate
from .px_items import Config, AppItemLike
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

    @staticmethod
    def create_context() -> None:
        _dpg.create_context()  # XXX: DPG doesn't care when calling multiple times.

    @staticmethod
    def destroy_context() -> None:
        _dpg.destroy_context()

    @classmethod
    def setup(cls) -> None:
        """Create the required graphical context for the application and, if necessary,
        initializes DearPyGui via `setup_dearpygui`.
        """
        if not cls.is_set_up:
            cls.create_context()
            _dpg.setup_dearpygui()

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
        return cls.state()["set_up"]

    @staticmethod
    def state() -> DPGApplicationState:
        return {"set_up": _appstate._APPLICATION_SET_UP}

    # ~~ Properties, Methods ~~

    @staticproperty
    def process_id() -> int:
        """Return the id of the running process."""
        return os.getpid()

    @property
    def platform(self) -> int:
        """Return the DearPyGui constant value representing the running operating
        system."""
        return _dpg.get_platform()

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
    def __init__(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., disable_close: bool = ..., primary_window: ItemId | None = ..., callback: DPGCallback | None = ..., user_data: Any = ..., **kwargs) -> None: ...
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
    def configure(self, *, title: str = ..., small_icon: str = ..., large_icon: str = ..., width: int = ..., height: int = ..., x_pos: int = ..., y_pos: int = ..., min_width: int = ..., max_width: int = ..., min_height: int = ..., max_height: int = ..., resizable: bool = ..., vsync: bool = ..., always_on_top: bool = ..., decorated: bool = ..., clear_color: tuple[int, ...] = ..., disable_close: bool = ..., primary_window: ItemId | None = ..., callback: DPGCallback | None = ..., user_data: Any = ..., **kwargs) -> None: ...
    def configure(self, callback: DPGCallback | None | Null = Null, user_data: Any = Null, primary_window: ItemId | None | Null = Null, **kwargs: DPGViewportConfig) -> None:
        """Update the viewport's configuration. If the viewport is showing, 'icon'-related
        options are ignored.
        """
        _dpg.configure_viewport(self.__UUID, **kwargs)
        if callback is not Null:
            _dpg.set_viewport_resize_callback(callback, user_data=_appstate._VIEWPORT_USER_DATA)
        if user_data is not Null:
            _dpg.set_viewport_resize_callback(_appstate._VIEWPORT_RESIZE_CALLBACK, user_data=user_data)
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
        config.update(
            primary_window=_appstate._VIEWPORT_PRIMARY_WINDOW,
            callback=_appstate._VIEWPORT_RESIZE_CALLBACK,
            user_data=_appstate._VIEWPORT_USER_DATA,
        )
        return config

    @classproperty  # inquire w/o forcefully creating vp
    def is_created(cls) -> bool:
        return cls.state()["created"]

    @classproperty
    def is_visible(cls) -> bool:
        return cls.state()["visible"]

    @classproperty
    def is_fullscreen(cls) -> bool:
        return cls.state()["fullscreen"]

    @staticmethod
    def state() -> DPGViewportState:
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
                else:
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







class _TaskSchedule(enum.IntEnum):
    """Special frame values for the next, last, and all frames."""
    ALL  = -1
    NEXT = -2
    LAST = -3


_RT_STATE: '_RuntimeState | None' = None

class _RuntimeState:
    __slots__ = (
        "tasks",
        "_frame_rate_limit",
        "_frame_rate_lock",
        "_render_interval",
        "tick_interval",
    )

    def __init__(self):
        self._frame_rate_limit: int
        self._frame_rate_lock : bool
        self._render_interval : float

        self._render_interval  = 0.0  # |
        self.tick_interval     = 1.0  # |- milliseconds
        self.tasks             = {}

        self.frame_rate_limit = None
        self.frame_rate_lock  = False

    @property
    def frame_rate_limit(self) -> int | None:
        return self._frame_rate_limit or None
    @frame_rate_limit.setter
    def frame_rate_limit(self, value: int | None):
        self._frame_rate_limit = value = int(value) if value is not None else 0
        self._upd_render_interval()

    @property
    def frame_rate_lock(self) -> bool:
        return self._frame_rate_lock
    @frame_rate_lock.setter
    def frame_rate_lock(self, value: bool) -> None:
        self._frame_rate_lock = bool(value)
        self._upd_render_interval()

    @property
    def render_interval(self) -> float:
        return self._render_interval

    def _upd_render_interval(self):
        if self.frame_rate_limit and self.frame_rate_lock:
            self._render_interval = round(1000.0 / self.frame_rate_limit, 6)
        else:
            self._render_interval = 0.0

    def _fill_priority_queue(self) -> float:
        priority_queue = self.tasks[_TaskSchedule.NEXT]
        standby_queue  = self.tasks[_TaskSchedule.ALL]
        if not priority_queue:
            priority_queue._queue.extend(standby_queue)

    def _fill_priority_queue2(self) -> float:
        self._fill_priority_queue()  # user tasks normally run first regardless
        if _dpg.get_app_configuration()["manual_callback_management"]:
            self.tasks[_TaskSchedule.NEXT]._queue.extend(
                Callback(cb, sender=s, app_data=a, user_data=u)
                for cb, s, a, u in _dpg.get_callback_queue()
                if cb is not None
            )


def _perf_counter_ms() -> float:
    return 1000.0 * time.perf_counter()


class Runtime(AppItemLike):
    """Interface for the main event loop and runtime-level queries.

    All instances operate on the global state. Automatically prepares the runtime
    environment when the first instance is created.
    """

    # XXX: `Runtime` is more of a module w/descriptors than a class. There
    # are no instance methods and very few class methods -- updates are
    # performed explicitly on the `Runtime` object, not `cls` or `self`.
    # This makes it difficult to change existing behavior

    __slots__ = ()

    @overload
    def __init__(self, *, stack_factory: type[CallStack] = CallStack, frame_rate_limit: int | None = ..., frame_rate_lock: bool = ..., **kwargs) -> None: ...
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

        Other methods may call this one to ensure the runtime enviroment is set up.
        """
        global _RT_STATE
        if _RT_STATE is None:
            Application.setup()
            _RT_STATE = _RuntimeState()
            _RT_STATE.tasks[_TaskSchedule.ALL ] = stack_factory()
            _RT_STATE.tasks[_TaskSchedule.NEXT] = stack_factory(tasker_mode=TaskerMode.POPLEFT)
            _RT_STATE.tasks[_TaskSchedule.LAST] = stack_factory(tasker_mode=TaskerMode.POPLEFT)

    # ~~ Item API ~~

    frame_rate_limit: Config[int | None, int | None] = Config()
    frame_rate_lock : Config[bool, bool]             = Config()
    tick_interval   : Config[float, float]           = Config()

    @overload
    def configure(self, *, frame_rate_limit: int | None = ..., frame_rate_lock: bool = ..., tick_interval: float = ..., **kwargs) -> None: ...
    def configure(self, **kwargs) -> None:
        for k, v in kwargs.items():
            try:
                setattr(_RT_STATE, k, v)
            except AttributeError:
                raise TypeError(f"invalid configuration option {k!r}.")

    def configuration(self) -> dict[str]:
        return dict(
            frame_rate_limit=_RT_STATE.frame_rate_limit,
            frame_rate_lock=_RT_STATE.frame_rate_lock,
            tick_interval=_RT_STATE.tick_interval,
        )

    @staticproperty  # for better performance, don't use `.state` hook (used in rt loop)
    def is_running() -> bool:
        return _dpg.is_dearpygui_running()

    @staticproperty  # for better performance, don't use `.state` hook (used in rt loop)
    def is_frame_rate_clamped():
        return bool(_RT_STATE and _RT_STATE.frame_rate_limit)

    @classproperty
    def is_set_up(cls) -> bool:
        return cls.state()["set_up"]

    @staticmethod
    def state() -> dict[str, bool]:
        return dict(
            set_up=_RT_STATE is not None,
            running=_dpg.is_dearpygui_running,
            frame_rate_clamped=bool(_RT_STATE and _RT_STATE.frame_rate_limit),
        )

    # ~~ Main Event Loop API ~~

    @overload
    @staticmethod
    def render_frame(): ...  # pyright inferrence
    render_frame = staticmethod(_dpg.render_dearpygui_frame)   # can be overloaded (non-instance-bound)

    @classmethod
    def start(cls, *, prerender_frames: int = 0):
        """Start the runtime loop. This blocks the calling thread until the viewport is
        closed or the `.stop` method is called.

        Args:
            * prerender_frames: The number of frames to render before starting the loop.
            Defaults to 0.


        This method will also do the following (in order, as needed);
            * create the required graphical context for the application
            * initialize DearPyGui
            * create and/or show the viewport


        At the start of each iteration, a snapshot of the runtime's settings are stored locally.
        Updates to the runtime settings will not take effect until the next iteration.

        Scheduled tasks are processed oldest-to-newest using a fixed time step (`.tick_interval`
        setting). Tasks remain in queue until they are processed.

        When the runtime settings are "snapped" each iteration, the `frame_rate_limit` setting
        is ignored unless the `frame_rate_lock` setting is `True`. Similarly, `frame_rate_lock`
        is ignored if `frame_rate_limit` is not meaningful.

        Passing a *prerender_frames* argument will render that many frames before and outside
        the runtime loop. Any task scheduled for a frame rendered this way will not run until
        all pre-rendered frames have been rendered. This can be useful when you want to ensure
        DearPyGui has enough time to update its internal state (this usually occurs within the
        first few frames).
        """
        cls.setup()
        rt_state = _RT_STATE

        # set the scheduler for the runtime ("manual_callback_management" will not change anymore)
        if Application().configuration()["manual_callback_management"]:
            fill_prio_queue = rt_state._fill_priority_queue2
        else:
            fill_prio_queue = rt_state._fill_priority_queue
        # create and/or show the viewport
        Viewport().show()

        for _ in range(prerender_frames):
            cls.render_frame()

        task_queue    = rt_state.tasks[cls.PRIORITY]
        tick_interval = rt_state.tick_interval
        ts_last_upd   = _perf_counter_ms()
        ts_last_fr    = ts_last_upd
        time_buffer   = 0.0
        updates       = task_queue.tasker()
        while cls.is_running:
            this_upd_ts  = _perf_counter_ms()
            time_buffer += round(this_upd_ts - ts_last_upd, 12)
            ts_last_upd  = this_upd_ts
            fill_prio_queue()
            try:
                while time_buffer >= tick_interval:
                    next(updates)
                    time_buffer -= tick_interval
            except StopIteration:
                updates = task_queue.tasker()

            fr_interval = rt_state.render_interval
            ts_this_fr  = _perf_counter_ms()
            if ts_this_fr - ts_last_fr >= fr_interval:
                ts_last_fr = ts_this_fr
                cls.render_frame()
        rt_state.tasks[cls.AT_EXIT]()

    @classmethod
    def stop(cls):
        if cls.is_running:
            _dpg.stop_dearpygui()
            _RT_STATE.tasks[cls.AT_EXIT]()


    # ~~ Updates/Ticks/Callback API ~~

    PRIORITY = _TaskSchedule.NEXT
    STANDBY  = _TaskSchedule.ALL
    AT_EXIT  = _TaskSchedule.LAST

    @classproperty
    def tasks(cls) -> dict[int, CallStack] | None:
        try:
            return _RT_STATE.tasks
        except AttributeError:
            cls.setup()
            return _RT_STATE.tasks

    @classmethod
    def schedule(cls, callback: Callable = None, /, *, when: int = PRIORITY, **kwargs):
        """Schedules a runtime task. Optionally usable as a decorator.

        Args:
            * callback: Callable object to schedule.

            * when: Dictates when and/or how frequently *callback* will run. Defaults to
            `Runtime.PRIORITY`.


        When and how frequently a callback is executed depends on the value passed
        to *when*. `Runtime.STANDBY` will store the callback into a secondary queue. At the
        start of each cycle of the runtime loop, all tasks in this queue are moved (copied)
        to the priority queue IF the priority queue is empty. `Runtime.PRIORITY` will schedule
        it at the end of the primary queue and will run one time only. If `Runtime.AT_EXIT`,
        the callback will run when exiting the runtime loop after the last frame has rendered
        (they will NOT run if the runtime loop is never started, unless the `.stop` method is
        called).
        """
        def _on_frame(_callback):
            task = _callback
            if kwargs:
                task = Callback(_callback, **kwargs)
            try:
                tasks = _RT_STATE.tasks
            except AttributeError:
                cls.setup()
                tasks = _RT_STATE.tasks
            try:
                stack = tasks[when]
            except KeyError:
                raise ValueError(
                    "`frame` expected one of the following `Runtime` members; `STANDBY`, `PRIORITY`, `AT_EXIT`."
                ) from None
            stack.append(task)
            return _callback
        return _on_frame if callback is None else _on_frame(callback)

    @classmethod
    def get_task_queue(cls):
        try:
            _RT_STATE._fill_priority_queue2()
        except AttributeError:
            cls.setup()
            _RT_STATE._fill_priority_queue2()
        return _RT_STATE.tasks[cls.PRIORITY]

    # ~~ DPG Function Hooks (staticmethods) ~~

    @classproperty
    def frame_count(cls):
        return cls.get_frame_count()

    @staticmethod
    def get_frame_count() -> int:
        """Return the number of frames rendered."""
        return _dpg.get_frame_count()


    @classproperty
    def frame_rate(cls):
        return cls.get_frame_rate()

    @staticmethod
    def get_frame_rate() -> int:
        """Return the average frames rate over the last 120 frames."""
        return _dpg.get_frame_rate()


    @classproperty
    def elapsed_time(cls):
        return cls.get_elapsed_time()

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
