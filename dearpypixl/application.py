from typing import Callable, Any, Union, Iterable
from abc import ABCMeta, abstractmethod
import sys
import os
import ctypes
import functools
from itertools import filterfalse
from dearpygui import dearpygui, _dearpygui
# Many of these tend to be called between frames as render
# callbacks -- trying to avoid lookup overhead with these
# imports.
from dearpygui._dearpygui import (
    # mainloop
    render_dearpygui_frame,
    is_dearpygui_running,
    stop_dearpygui,
    # getters
    get_mouse_drag_delta,
    get_drawing_mouse_pos,
    get_plot_mouse_pos,
    get_mouse_pos,
    get_total_time,
    get_frame_count,
    get_active_window,
    is_key_pressed,
    is_key_down,
    is_key_released,
    # misc
    split_frame,
    set_frame_callback,
)

from dearpypixl.item import Item
from dearpypixl.item.other import UniqueItemMeta, ItemLike, UpdaterList
from dearpypixl.constants import AppUUID, ViewportUUID, Key, Mouse, DefaultRegistries
from dearpypixl.theming import Theme
from dearpypixl.containers import Window
from dearpypixl.events import (
    KeyDownHandler,
    KeyPressHandler,
    KeyReleaseHandler,
    MouseDownHandler,
    MouseClickHandler,
    MouseDoubleClickHandler,
    MouseReleaseHandler,
    MouseMoveHandler,
    MouseWheelHandler,
    MouseDragHandler
)

__all__ = [
    "Application",
    "Viewport",
]

Keycode = Union[Key, Mouse, int]


class Application(ItemLike, metaclass=UniqueItemMeta):
    def __init__(self):
        """Configuration Attributes:
            * auto_device (bool): The display adapter with the most dedicated video
            memory will be used. If this is False and the value of `device` is -1,
            your operating system will automatically select an adapter. Default is False.
            * docking (bool): Allows `Window` items to dock into each other when dragged
             and dropped. Default is False.
            * docking_space (bool): Allows `Window` items to also dock directly to the
            viewport/primary window space if `docking` is True. Default is False.
            * device (int): Manually set the display adapter to use.

            NOTE: Configuration attributes listed above will NOT BE CONFIGURABLE once
            the Viewport is shown. Typically, the Viewport will be shown when the 
            `start` method is called.
        """
        DefaultRegistries.setup_registries()
        self.__calls_on_render = None
        self.__calls_on_startup = None
        self.__calls_on_exit = None
        self.__virtual_scaling = None
        self.__events = ...

        self.auto_device: bool = False
        self.docking: bool = False
        self.docking_space: bool = False
        self.device: int = -1

        self.calls_on_startup = []  # _StartupUpdaterList
        self.calls_on_render = []
        self.calls_on_exit = []  # _ExitUpdaterList

        if sys.platform == "win32":
            self.virtual_scaling = False

    def __manage_callable_list(method=None):
        # Enforcing pretty strict type checks for properties holding callables
        # so useful information is provided if something breaks.
        @functools.wraps(method)
        def wrapper(self, value: list, *args, **kwargs):
            if not isinstance(value, list):
                raise TypeError(f"{type(list)!r} expected, got {type(value)!r} ({value!r}).")
            for non_callable in filterfalse(callable, value):
                raise TypeError(f"{type(list)!r} of callables expected, found {type(non_callable)!r} ({non_callable!r}).")
            return method(self, value, *args, **kwargs)
        return wrapper

    ################################
    ######### Render loop ##########
    ################################
    def start(self) -> None:
        """Start the application by executing the main render loop. This
        is the recommended way to start the application.

        NOTE: It is not recommended to manually build the render loop.
        If it is necessary for code to be ran in the loop itself, use
        a function instead and, either decorate the function with the
        `on_render` decorator (or pass it normally as an argument) or
        directly append it to `calls_on_render`.
        """
        Viewport().show()  # singleton
        # Avoiding lookup overhead in the loop as it is the most
        # "sensitive" spot in the entire framework.
        is_running = self.is_running
        render_frame = self.render_frame  

        # NOTE: This is the render loop.
        while is_running():
            render_frame()
        self.end()

    def stop(self) -> None:
        """Break the main render loop and stop the application
        if it is running. This is the equivelent to pressing the
        "close" or "exit" button application title bars.

        """
        if self.is_running():
            stop_dearpygui()

    def end(self) -> None:
        """Post-process wind-down. Must be called following the render
        loop to ensure proper 'cleanup'. Once called, future calls
        to the internal library will likely cause a segmentation fault
        (i.e. this should be the last call you make).

        NOTE: The `start` method automatically calls this. You should only
        need to make this call yourself if you're not calling `start` and
        have made the render loop manually.
        """
        _dearpygui.destroy_context()

    def render_frame(self) -> None:
        """Renders a frame. Only for use in the main render loop (see the
        `start` method).
        """
        [c() for c in self.__calls_on_render]
        render_dearpygui_frame()

    ################################
    ######### Properties ###########
    ################################
    @property
    def calls_on_startup(self) -> list[Callable]:
        """List of callables set to run within the first few frames on
        application startup.
        """
        return self.__calls_on_startup
    @calls_on_startup.setter
    @__manage_callable_list
    def calls_on_startup(self, value: list[Callable]) -> None:
        self.__calls_on_startup = self._StartupUpdaterList(value)


    @property
    def calls_on_render(self) -> list[Callable]:
        """List of callables set to run after rendering a frame.
        """
        return self.__calls_on_render
    @calls_on_render.setter
    @__manage_callable_list
    def calls_on_render(self, value: list[Callable]) -> None:
        self.__calls_on_render = value


    @property
    def calls_on_exit(self) -> list[Callable]:
        """List of callables set to run on application exit.
        """
        return self.__calls_on_exit
    @calls_on_exit.setter
    @__manage_callable_list
    def calls_on_exit(self, value: list[Callable]) -> None:
        self.__calls_on_exit = self._ExitUpdaterList(value)


    @property
    def theme(self) -> Theme:
        """The application's default Theme item.
        """
        if not (default_theme_uuid := getattr(Theme, "_Theme__default_theme")):
            theme_item = Theme("APPICATION_AUTO_DEFAULT", include_presets=True)
            theme_item.bind()
            return theme_item
        return self._appitems[default_theme_uuid]
    @theme.setter
    def theme(self, value: Union[Theme, None]) -> None:
        if value is None:
            value.unbind()
        value.bind()
    

    @property
    def events(self) -> ...:
        """The polling event manager that is currently in use.
        """
        return self.__events
    @events.setter
    def events(self, value: ...):
        ...


    @property
    def font_scale(self) -> float:
        """The value in which all font renders are scaled to. A value larger
        than 1.0 can result in a loss of visual quality.
        """
        return _dearpygui.get_global_font_scale()
    @font_scale.setter
    def font_scale(self, value: float):
        _dearpygui.set_global_font_scale(value)


    @property
    def version(self) -> str:
        """Return the version of Dearpygui that is being used.
        """
        return _dearpygui.get_app_configuration()["version"]

    @property
    def platform(self) -> str:
        """Return the platform.
        """
        return _dearpygui.get_app_configuration()["platform"]

    @property
    def device_name(self) -> str:
        """Return the name of the display adapter in use.
        """
        return _dearpygui.get_app_configuration()["device_name"]

    @property
    def device_manager(self) -> str:
        """Return the current controller of the display adapter used for the
        application.
        
        Possible returns:
            * system: The display adapter has been set by your operating
            system.
            * internal: The display adapter has been set by DearPyGui.
            * manual: The display adapter has been manually selected.
        """
        configuration = self._configuration()
        device = configuration["device"]
        auto_device = configuration["auto_device"]
        if device != -1:
            return "manual"
        elif not auto_device:
            return "system"
        return "internal"


    @property
    def process_id(self) -> str:
        """Return the current process identifier.
        """
        return os.getpid()

    if sys.platform == "win32":
        @property
        def virtual_scaling(self) -> bool:
            """If True, the interface will be scaled to the current value of
            the "Scale" setting in Windows. This can improve the readability
            of the interface if this value is set over 100% when viewed on
            high-resolution displays, but the quality of the renders will
            be reduced. If False, the process will ignore this setting and
            the interface will not be scaled.
            """
            return self.__virtual_scaling
        @virtual_scaling.setter
        def virtual_scaling(self, value: bool) -> None:
            self.__virtual_scaling = value
            if value is True:
                # enable virtual scaling
                return ctypes.windll.shcore.SetProcessDpiAwareness(0)
            # disable virtual scaling
            return ctypes.windll.shcore.SetProcessDpiAwareness(2)

    ################################
    ######## Event Handling ########
    ################################
    def on_startup(self, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will run within the first
        few frames.
        """
        self.__calls_on_startup.append(callback)
        return callback

    def on_render(self, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will after a frame is rendered.
        """
        self.__calls_on_render.append(callback)
        return callback

    def on_exit(self, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will run on the last frame.
        """
        self.__calls_on_exit.append(callback)
        return callback

    def on_frame(self, frame: int, callback: Callable = None) -> Callable:
        """Schedule a callback to run on frame *frame*.
        """
        # No list attribute/property for this one. No reasonable reason for it
        # to exist, and not worth the work implementing and keeping track of it.
        def wrapper(callback):
            set_frame_callback(frame, callback)
            return callback

        if callback:
            return wrapper(callback)
        return wrapper

    ################################
    ######## Misc. methods #########
    ################################
    def children(self) -> list[Item]:
        """Return a list of all tracked items.
        """
        child_tags = dearpygui.get_all_items()
        appitems = self._appitems
        return [child for child_tag in child_tags if
                (child := appitems.get(child_tag, None))]

    @staticmethod
    def runtime() -> float:
        """Return the time that has elapsed since the main render loop
        was started.
        """
        return get_total_time()

    @staticmethod
    def frames() -> int:
        """Return the number of frames rendered.
        """
        return get_frame_count()

    @staticmethod
    def framerate() -> int:
        """Return the average frames rendered per second (rounded).
        """
        return round((get_frame_count() or 1) / (get_total_time() or 1))

    @staticmethod
    def split_frame(delay: int = 32) -> None:
        """Add a delay (milliseconds) before rendering the next frame.
        """
        return split_frame(delay=delay)

    @staticmethod
    def is_running() -> bool:
        """Return the status of the main render loop.
        """
        # Not a property to avoid lookup overhead in the 
        # render loop...
        return is_dearpygui_running()

    @staticmethod
    def is_key_pressed(keycode: Keycode) -> bool:
        """Return True if `keycode` is pressed, otherwise return False.

        Args:
            * keycode (Union[Key, Mouse, int]): key event code to inquire
            about.
        """
        return is_key_pressed(int(keycode))

    @staticmethod
    def is_key_released(keycode: Keycode) -> bool:
        """Return True if `keycode` is released, otherwise return False.

        Args:
            * keycode (Union[Key, Mouse, int]): key event code to inquire
            about.
        """
        return is_key_released(int(keycode))

    @staticmethod
    def is_key_down(keycode: Keycode) -> bool:
        """Return True if `keycode` is down, otherwise return False.

        Args:
            * keycode (Union[Key, Mouse, int]): key event code to inquire
            about.
        """
        return is_key_down(keycode)

    ################################
    ###### Private/Internal ########
    ################################
    _tag = AppUUID
    _configurations = (
        # Supported by pixl
        'auto_device',
        'docking',
        'docking_space',
        'device',
    )

    def _configure(self, **kwargs):
        dearpygui.configure_app(**kwargs)
    
    def _configuration(self):
        return _dearpygui.get_app_configuration()

    class _StartupUpdaterList(UpdaterList):
        """Automatically re-sets the startup callback with the contents
        of `self` on creation, or update through list method calls.
        """
        @staticmethod
        def _on_update(callables):
            set_frame_callback(1, lambda: [c() for c in callables])

    class _ExitUpdaterList(UpdaterList):
        """Automatically re-sets the exit callback with the contents
        of `self` on creation, or update through list method calls.
        """
        @staticmethod
        def _on_update(callables):
            _dearpygui.set_exit_callback(lambda: [c() for c in callables])


class Viewport(ItemLike, metaclass=UniqueItemMeta):
    def __init__(self):
        self.__primary_window = None
        self.__use_primary_window = False
        dearpygui.create_viewport()
        dearpygui.setup_dearpygui()

        self.title: str = 'Application'
        self.small_icon: str = ''
        self.large_icon: str = ''
        self.width: int = 1280
        self.height: int = 800
        self.x_pos: int = 100
        self.y_pos: int = 100
        self.min_width: int = 250
        self.max_width: int = 10000
        self.min_height: int = 250
        self.max_height: int = 10000
        self.resizable: bool = True
        self.vsync: bool = True
        self.always_on_top: bool = False
        self.decorated: bool = True
        self.clear_color: Union[list[float], tuple[float, ...]] = (0, 0, 0, 255)

    ################################
    ######## Event Handling ########
    ################################
    # TODO: Add I/O handlers
    def on_resize(self, callback: Callable): ...

    ################################
    ########## Properties ##########
    ################################
    @property
    def active_window(self):
        return get_active_window()

    @property
    def mouse_drag_delta(self):
        return get_mouse_drag_delta()

    @property
    def local_mouse_pos(self) -> list[float]:
        return get_mouse_pos()

    @property
    def global_mouse_pos(self) -> list[float]:
        return get_mouse_pos(local=False)

    @property
    def drawing_mouse_pos(self) -> list[float]:
        return get_drawing_mouse_pos()

    @property
    def plot_mouse_pos(self) -> list[float]:
        return get_plot_mouse_pos()

    @property
    def primary_window(self) -> Union[Window, None]:
        return self.__primary_window
    @primary_window.setter
    def primary_window(self, value: Union[Window, None]):
        if value is None:
            dearpygui.set_primary_window(self.__primary_window._tag, False)
        else:
            dearpygui.set_primary_window(value._tag, self.__use_primary_window)
        self.__primary_window = value

    @property
    def use_primary_window(self) -> bool:
        return self.__use_primary_window
    @use_primary_window.setter
    def use_primary_window(self, value: bool) -> None:
        if self.__primary_window:
            dearpygui.set_primary_window(self.__primary_window._tag, value)
        self.__use_primary_window = value

    ################################
    ######## Misc. methods #########
    ################################
    def children(self) -> list[Item]:
        """Returns a list of all tracked items.
        """
        child_tags = dearpygui.get_all_items()
        appitems = self._appitems
        return [child for child_tag in child_tags if
                (child := appitems.get(child_tag, None))]

    def maximize(self) -> None:
        """Maximizes the viewport.
        """
        _dearpygui.maximize_viewport()

    def minimize(self) -> None:
        """Minimizes the viewport.
        """
        _dearpygui.minimize_viewport()

    def show(self) -> None:
        """Shows the viewport. Some configuration options will no longer
        be configurable.
        """
        _dearpygui.show_viewport()

    ################################
    ###### Private/Internal ########
    ################################
    def _configure(self, **kwargs):
        dearpygui.configure_viewport(self._tag, **kwargs)

    def _configuration(self) -> dict:
        return _dearpygui.get_viewport_configuration(self._tag)

    _tag = ViewportUUID
    _configurations = (
        'title',
        'small_icon',
        'large_icon',
        'width',
        'height',
        'x_pos',
        'y_pos',
        'min_width',
        'max_width',
        'min_height',
        'max_height',
        'resizable',
        'vsync',
        'always_on_top',
        'decorated',
        'clear_color',
    )



