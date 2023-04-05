"""Contains objects for querying and managing DearPyGui's runtime and
application-level states.
"""
import os
import enum
import functools
import time
from dearpygui import dearpygui as dpg, _dearpygui as _dpg
from . import px_appstate as _appstate
from .px_items import Config, AppItemLike
from .px_utils import staticproperty, classproperty
from .events import Callback, CallStack, TaskerMode
from .px_typing import (
    T,
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
    """Item-like interface for DearPyGui's application state. Instances operate on the
    global state.


    When the first `Application` instance is created, various setup commands such as
    `create_context` and `setup_dearpygui` are called if not already done so.

    Any keyword argument supported by DearPyGui's `configure_app` function can also be
    passed to `Application`s constructor and `.configure` method. Included arguments will
    be used to update the application-level configuration. In addition, the following
    unqiue keyword arguments are also supported;
        * **theme**: A reference to the `mvTheme` item used as the application-level
        theme.

        * **font**: A reference to the `mvFont` item used as the application-level
        font.

    NOTE: The DearPyGui API does not include a way of accessing any of the above once
    they have been set. Because of this, several DearPyGui functions have been patched
    to update various states unique to this library -- Returned values of these settings
    are always up-to-date even if you, for example, update the application-level font
    using the "raw" `bind_theme` function.
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
        """Creates the graphical context for the application. Does nothing if
        the graphical context has already been created.

        Many calls to DearPyGui (and consequently DearPyPixl) will fail if
        the `create_context` hook has not been called prior.
        """
        _dpg.create_context()  # DPG doesn't care when calling multiple times

    @staticmethod
    def destroy_context() -> None:
        """Destroys the graphical context created via `create_context` hook.

        Several calls to DearPyGui (and consequently DearPyPixl) will fail once
        the `destroy_context` hook has been called.
        """
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
        """[get] Return True if the `setup_dearpygui` function has been called."""
        return cls.state()["set_up"]

    @staticmethod
    def state() -> DPGApplicationState:
        """Return various application-level states."""
        return {"set_up": _appstate._APPLICATION_SET_UP}

    # ~~ Properties, Methods ~~

    @staticproperty
    def process_id() -> int:
        """[get] Return the id of the running process."""
        return os.getpid()

    # ~~ DPG Function Hooks ~~

    @classproperty
    def platform(cls):
        """[get] Return the DearPyGui constant value representing the running
        operating system."""
        return _dpg.get_platform()

    @staticmethod
    def get_platform() -> int:
        """Return the DearPyGui constant value representing the running
        operating system."""
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
    """Item-like interface for DearPyGui's viewport. Instances operate on
    the global state.


    When the first `Viewport` instance is created, various setup commands such as
    `create_context` and `setup_dearpygui` are called if not already done so.
    Additionally, the *actual* viewport is created if it does not exist.

    Any keyword argument supported by DearPyGui's `create_viewport` function can also
    be passed to `Viewport`s constructor and `.configure` method. Included arguments
    will be used to update the viewport's global configuration. In addition, the
    following unqiue keyword arguments are also supported;
        * **callback**: The callable invoked when the viewport is resized.

        * **user_data**: The object to pass to *callback* when conditionally called.

        * **primary_window**: A reference to a `mvWindowAppItem` item to use as
        the "primary" window, filling the viewport's space.

    NOTE: The relationship between *callback* and *user_data* is functionally identical
    to that of items. Additionally, both are updated independently of one another even
    though both are internally updated using the same function (i.e.
    `set_viewport_resize_callback`).

    NOTE: The DearPyGui API does not include a way of accessing any of the above once
    they have been set. Because of this, several DearPyGui functions have been patched
    to update various states unique to this library -- Returned values of these settings
    are always up-to-date even if you, for example, update the primary window using the
    "raw" `set_primary_window` function.


    `Viewport` also exposes several unique states as read-only properties. They are
    class-bound so they can be accessed without needing to actually create the viewport
    (which would otherwise be problematic, especially for a `Viewport().is_created`
    inquiry).
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
        """Update the viewport's global configuration.

        NOTE: DearPyGui ignores 'icon'-related options once the viewport is visible.
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
        """Return the viewport's global configuration."""
        config = _dpg.get_viewport_configuration(self.__UUID)
        config.update(
            primary_window=_appstate._VIEWPORT_PRIMARY_WINDOW,
            callback=_appstate._VIEWPORT_RESIZE_CALLBACK,
            user_data=_appstate._VIEWPORT_USER_DATA,
        )
        return config

    @classproperty  # inquire w/o forcefully creating vp
    def is_created(cls) -> bool:
        """[get] Return True if the viewport exists."""
        return cls.state()["created"]

    @classproperty
    def is_visible(cls) -> bool:
        """[get] Return True if the showing the viewport."""
        return cls.state()["visible"]

    @classproperty
    def is_fullscreen(cls) -> bool:
        """[get] Return True if the viewport is displayed in borderless windowed
        fullscreen"""
        return cls.state()["fullscreen"]

    @staticmethod
    def state() -> DPGViewportState:
        """Return the global viewport state."""
        return {
            "created": _appstate._VIEWPORT_CREATED,
            "visible": _dpg.is_viewport_ok(),
            "fullscreen": _appstate._VIEWPORT_FULLSCREEN,
        }

    # ~~ Properties, Methods ~~

    @property
    def pos(self) -> tuple[int, int]:
        """[get] Return the *x_pos* and *y_pos* configurations of the viewport."""
        config = self.configuration()
        return config["x_pos"], config["y_pos"]
    @pos.setter
    def pos(self, value: tuple[int, int]) -> None:
        """[set] Update the *x_pos* and *y_pos* configurations of the viewport."""
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
        """Return the position of the mouse cursor relative to the focused item.

        If no item(s) is focused when called, return the cursor's last position
        relative to the item that was most recently focused (when it was focused).
        """
        return _dpg.get_mouse_pos(local=True)

    @staticmethod
    def get_mouse_plot_pos():
        """Return the position of the mouse cursor relative to the focused plot
        item."""
        return _dpg.get_plot_mouse_pos()

    @staticmethod
    def get_mouse_drawing_pos():
        """Return the position of the mouse cursor relative to the focused
        drawlist item."""
        return _dpg.get_drawing_mouse_pos()

    @staticmethod
    def output_frame_buffer(file: str = "", *, callback: Any = None, **kwargs) -> None:
        """Captures a screenshot of the viewport (excludes the title bar).

        Args:
            * file: A filepath for the resulting .png file. Name must include
            ".png". Defaults to "".

            * callback: A DearPyGui-callable object accepting zero to three
            positional arguments that will handle the raw image buffer. Defaults
            to None.

        NOTE: Not supported on MacOS.


        The result of this function varies depending on the arguments passed;
            * If *file* is not an empty string, the screenshot is saved as
            *file* in .png format.

            * If *file* is an empty string and *callback* is not None, DearPyGui
            queues *callback* to run next frame, passing it a `mvBuffer` object
            as the second positional argument if able (i.e. `app_data`).

        NOTE: `mvBuffer` objects are exposed in DearPyGui's namespace but are undocumented.
        They use Python's buffer protoco, but are NOT Python arrays, and do not behave
        as such. Casting them to another built-in sequence type will also fail -- To cast
        to a Python list, use the built-in `memoryview` function to create a view of the
        buffer, then call the view's `.tolist` method. Read the official docs at
        <https://docs.python.org/3/library/stdtypes.html#typememoryview> for more information
        on `memoryview` objects.
        """
        # XXX: have not tested what happens w/both arguments
        _dpg.output_frame_buffer(file, callback=callback)

    @staticmethod
    def save_frame_buffer(file: str, **kwargs) -> None:
        """Captures a screenshot of the viewport (excluding the title bar) and
        saves it as a .png file.

        Args:
            * file: A filepath for the resulting .png file. Will append ".png" if
            it does not end with it.

        NOTE: Not supported on MacOS.
        """
        if not file.endswith(".png"):
            file = f"{file}.png"
        _dpg.output_frame_buffer(file, callback=None)




class _RuntimeQueue(enum.IntEnum):
    """Special frame values for the next, last, and all frames."""
    ONETIME = enum.auto()
    ROUTINE = enum.auto()
    AT_EXIT = enum.auto()


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
        active_queue : CallStack = self.tasks[_RuntimeQueue.ONETIME]
        standby_queue: CallStack = self.tasks[_RuntimeQueue.ROUTINE]
        if not active_queue:
            active_queue._queue.extend(standby_queue)

    def _fill_priority_queue2(self) -> float:
        # DPG runs its own updates in the first half of `render_dearpygui_frame`
        # (called after runtime ticks). This order is maintained here when using
        # manual_callback_management to avoid different behaviors between modes.
        self._fill_priority_queue()
        if _dpg.get_app_configuration()["manual_callback_management"]:
            queue: CallStack = self.tasks[_RuntimeQueue.ONETIME]
            queue._queue.extend(  # avoid `CallStack` wrap behavior
                # The front-loaded cost of `Callback` is a bit much here considering
                # the instance is thrown out afterward. `functools.partial` works fine
                # since compat. w/non-functions is only needed when DPG is the caller.
                functools.partial(callback, *args)
                for callback, *args in (_dpg.get_callback_queue() or ())
                if callback is not None
            )




def _perf_counter_ms() -> float:
    return 1000.0 * time.perf_counter()


class Runtime(AppItemLike):
    """Item-like interface for the main event loop and runtime-level queries. All
    instances operate on the global state.


    Creating the first instance of `Runtime` will invoke setup commands such as
    `create_context` and `setup_dearpygui` if a user has not done so already.
    Additonally, the `.start` method will create and/or show the viewport. Note
    that it does not *configure* the application or viewport in any way.
        >>> # import code goes here
        >>>
        >>> rt = Runtime()
        >>>
        >>> # UI code goes here
        >>>
        >>> rt.start()


    `Runtime` supports task ("callback") scheduling. Tasks are cached in one of three
    queues;
        * "onetime": The runtime's running queue. It is processed every iteration
        of the runtime loop before (possibly) rendering a frame. It is not guaranteed
        that the queue will process all tasks within every cycle or frame.

        * "routine": Contains common tasks that are repeatedly pushed onto priority
        queue. This will occur at the beginning of every runtime loop iteration
        **if the priority queue is empty**. This queue is never directly processed.

        * "at exit": Contains any tasks scheduled to run when the UI is closed or when
        the `.stop` method is called, will not be processed until either occurs.

    Queue contents are processed from oldest to newest. Any "processed" task is removed
    from the queue. Tasks can be pushed onto any queue and at any time, via the `.schedule`
    method. The queues themselves are exposed through the `.tasks` read-only property.


    There are several unique `Runtime` settings which affect various behavior of the
    `.start` method;
        * **frame_rate_limit**: The maximum number of frames to render every second.

        * **frame_rate_lock**: `True` clamps the frame rate to *frame_rate_limit*.
        Otherwise, the limit is not enforced.

        * **tick_interval**: The fixed time step (in milliseconds) in which
        tasks/updates occur.

    Passing any of the above as keyword arguments to the constructor or to the
    `.configure` method will update the respective option globally. These settings
    can updated while the runtime is running, but the changes won't take affect until
    the next iteration of the loop.
    """

    __slots__ = ()

    @overload
    def __init__(self, *, frame_rate_limit: int | None = ..., frame_rate_lock: bool = ..., tick_interval: float = ..., **kwargs) -> None: ...
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
            _RT_STATE.tasks[_RuntimeQueue.ONETIME] = stack_factory(tasker_mode=TaskerMode.RUNTIME, force_wrapping=None)
            _RT_STATE.tasks[_RuntimeQueue.ROUTINE] = stack_factory(force_wrapping=None)
            _RT_STATE.tasks[_RuntimeQueue.AT_EXIT] = stack_factory(tasker_mode=TaskerMode.RUNTIME, force_wrapping=None)

    # ~~ Item API ~~

    frame_rate_limit: Config[int | None, int | None] = Config()
    frame_rate_lock : Config[bool, bool]             = Config()
    tick_interval   : Config[float, float]           = Config()

    @overload
    def configure(self, *, frame_rate_limit: int | None = ..., frame_rate_lock: bool = ..., tick_interval: float = ..., **kwargs) -> None: ...
    def configure(self, **kwargs) -> None:
        """Updates global runtime settings. They will take effect at the start of the
        next runtime loop cycle.
        """
        for k, v in kwargs.items():
            try:
                setattr(_RT_STATE, k, v)
            except AttributeError:
                raise TypeError(f"invalid configuration option {k!r}.")

    def configuration(self) -> dict[str]:
        """Return the global runtime configuration."""
        return dict(
            frame_rate_limit=_RT_STATE.frame_rate_limit,
            frame_rate_lock=_RT_STATE.frame_rate_lock,
            tick_interval=_RT_STATE.tick_interval,
        )

    @staticproperty  # for better performance, don't use `.state` hook (used in rt loop)
    def is_running() -> bool:
        """Return True if DearPyGui is running."""
        return _dpg.is_dearpygui_running()

    @staticproperty  # for better performance, don't use `.state` hook (used in rt loop)
    def is_frame_rate_clamped():
        """[get] Return True if the frame rate is or will be clamped using the
        current runtime settings."""
        return bool(_RT_STATE and _RT_STATE.render_interval)

    @classproperty
    def is_set_up(cls) -> bool:
        """[get] Return True if the runtime environment has been prepared."""
        return cls.state()["set_up"]

    @staticmethod
    def state() -> dict[str, bool]:
        """Return the global runtime state."""
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


        Passing a *prerender_frames* argument will render that many frames before and outside
        the runtime loop. Any task scheduled for a frame rendered this way will not run until
        all pre-rendered frames have been rendered. This can be useful when you want to ensure
        DearPyGui has enough time to update its internal state (this usually occurs within the
        first few frames).

        A snapshot is taken of the runtime's settings at the start of each iteration of the loop.
        Updates to the runtime settings will not take effect until the next iteration. When the
        runtime settings are "snapped", the `frame_rate_limit` setting is ignored unless the
        `frame_rate_lock` setting is `True`. Similarly, `frame_rate_lock` is ignored if
        `frame_rate_limit` is not meaningful.

        Tasks are executed from a priority queue from oldest to newest using a fixed time step
        (`tick_interval` setting), and remain queued until they are processed. When the queue
        is empty, it is "reloaded" with tasks from the secondary/standby queue.

        When clamping the frame rate, code execution does not wait until it's time to render
        (i.e. thread does not sleep). Instead, it checks to see if enough time has passed
        and, if not, continues execution without rendering.
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

        running_queue = rt_state.tasks[cls.ONETIME]
        ts_last_upd   = _perf_counter_ms()
        ts_last_fr    = ts_last_upd
        time_buffer   = 0.0
        updates       = running_queue.tasker()
        while cls.is_running:
            this_upd_ts   = _perf_counter_ms()
            tick_interval = rt_state.tick_interval
            time_buffer  += round(this_upd_ts - ts_last_upd, 12)
            ts_last_upd   = this_upd_ts
            fill_prio_queue()
            try:
                while time_buffer >= tick_interval:
                    next(updates)
                    time_buffer -= tick_interval
            except StopIteration:
                updates = running_queue.tasker()

            fr_interval = rt_state.render_interval
            ts_this_fr  = _perf_counter_ms()
            if ts_this_fr - ts_last_fr >= fr_interval:
                ts_last_fr = ts_this_fr
                cls.render_frame()
        cls.tasks[cls.AT_EXIT]()

    @classmethod
    def stop(cls):
        if cls.is_running:
            _dpg.stop_dearpygui()
            cls.tasks[cls.AT_EXIT]()

    # ~~ Updates/Ticks/Callback API ~~

    ONETIME = _RuntimeQueue.ONETIME
    ROUTINE = _RuntimeQueue.ROUTINE
    AT_EXIT = _RuntimeQueue.AT_EXIT

    @classproperty
    def tasks(cls) -> dict[int, CallStack] | None:
        """[get] Return the mapping containing the runtime's task queues.

        Valid keys are `Runtime` members 'ONETIME', 'ROUTINE', and 'AT_EXIT'.
        """
        try:
            return _RT_STATE.tasks
        except AttributeError:
            cls.setup()
            return _RT_STATE.tasks

    @classmethod
    def schedule(cls, callback: T = None, /, *, queue: int = ONETIME, **kwargs) -> T:
        """Schedules a runtime task with *callback*. Optionally usable as a decorator.

        Args:
            * callback: Callable object to queue.

            * when: Dictates when and/or how frequently *callback* will run. Defaults to
            `Runtime.ONETIME`.


        This method always returns *callback*, allowing it to be used as a decorator.

        The object used as the callback can be any callable, and does not need to adhere
        to DearPyGui's callback convention. No arguments will be passed to the callable
        when called. If additional keyword arguments are included via *kwargs*, the result of
        `functools.partial(callback, **kwargs)` is queued instead of the original object.

        When and how frequently a callback is executed depends on the value passed
        to *queue*;
        - `Runtime.ONETIME` will schedule the callback at the end of the running queue and
        will run one time only. They will run in the same thread that calls the `.start`
        method.
        - `Runtime.ROUTINE` will store the callback into a standby queue. At the
        start of each cycle of the runtime loop, all tasks in this queue are moved (copied)
        to the priority queue IF the running queue is empty.
        - `Runtime.AT_EXIT`, the callback will run when exiting the runtime loop after the
        last frame has rendered. They will NOT run if the runtime loop is never started,
        unless the `.stop` method is called.

        All queues are `CallStack` objects, exposed via the `.tasks` property. Tasks can be
        pushed directly onto these queues without calling this method through their API.
        """
        def _on_frame(_callback):
            task = _callback if not kwargs else functools.partial(_callback, **kwargs)
            try:
                callstack = cls.tasks[queue]
            except KeyError:
                raise ValueError(
                    f"`frame` must be one of the following `Runtime` members; {', '.join(repr(s) for s in _RuntimeQueue._member_names_)}."
                ) from None
            callstack.append(task)
            return _callback
        return _on_frame if callback is None else _on_frame(callback)

    @classmethod
    def get_task_queue(cls) -> CallStack:
        """Populate and return the runtime's priority task queue.

        If the priority queue is empty, then a copy of the secondary queue is pushed
        onto the priority queue.

        If the application-level setting "manual_callback_management=True", this method
        will push DearPyGui's callback queue (via `get_callback_queue`) onto the priority
        queue.
        """
        try:
            _RT_STATE._fill_priority_queue2()
        except AttributeError:
            cls.setup()
            _RT_STATE._fill_priority_queue2()
        return _RT_STATE.tasks[cls.ROUTINE]

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
