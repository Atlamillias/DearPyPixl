import inspect
import sys
from typing import Callable
from contextlib import contextmanager

from dearpygui import _dearpygui as idpg, dearpygui as dpg
from dearpygui._dearpygui import (
    configure_viewport, 
    get_viewport_configuration,
)

import dpgwidgets
from dpgwidgets import _c_types
from dpgwidgets.item import Item
from dpgwidgets.containers import Window
from dpgwidgets.error import ViewportError
from dpgwidgets.handler import AppHandlerSupport
from dpgwidgets.theme import ThemeSupport, Theme
from dpgwidgets.themes import DEFAULT


__all__ = [
    "Viewport",
    "mutex",
]


class Viewport(Item, ThemeSupport, AppHandlerSupport):
    """Creates and performs setup on a DearPyGui viewport. A Viewport
    instance represents the application itself, and only one instance 
    should exist per-process.

        Args:
            title (str, optional): Text displayed in the viewport title bar.
        Defaults to "Application".
            small_icon (str, optional): Path to an image to be displayed on the left
        in the viewport title bar. Defaults to ''.
            large_icon (str, optional): Path to an image to be displayed on, for example,
        the Windows taskbar while the application is running. Defaults to ''.
            width (int, optional): Starting horizontal size in pixels. Defaults to 1280.
            height (int, optional): Starting vertical size in pixels. Defaults to 800.
            x_pos (int, optional): Starting position on the x-axis. Defaults to 100.
            y_pos (int, optional): Starting position on the y_axis. Defaults to 100.
            min_width (int, optional): The minimum width that the viewport can
        be sized to. Defaults to 250.
            max_width (int, optional): The maximum width that the viewport can be sized
        to. Defaults to 10000.
            min_height (int, optional): The minimum height that the viewport can
        be sized to. Defaults to 250.
            max_height (int, optional): The maximum height that the viewport can be sized
        to. Defaults to 10000.
            resizable (bool, optional): If False, the viewport cannot be resized through
        the interface. Defaults to True.
            vsync (bool, optional): Enables vertical sync - synchronizes the application
        framerate with your monitor's refresh rate. Defaults to True.
            always_on_top (bool, optional): If True, the application will always be "in front"
        of any other application. Useful for games, etc. Defaults to False.
            decorated (bool, optional): If False, the viewport borders and titlebar will
        not be shown. Default is True.
            clear_color (list[float], optional): [UNDOCUMENTED - Sets viewport background color?].
        Defaults to [0, 0, 0, 255].
            staging_mode (bool, optional): Enables staging mode. Defaults to False.
            enable_docking (bool, optional): Enables docking - drag and dropping windows in other
        windows will "nest" them into each other where you can tab back and forth between them.
        Defaults to False.
            dock_space (bool, optional): If True and <enable_docking> is also True, windows can also
        be docked on the viewport. Defaults to False.
    
    """
    called_on_start: list[Callable] = []  # registered before main loop
    called_on_exit: list[Callable] = []
    called_on_render: list[Callable] = []
    called_on_resize: list[Callable] = []

    def __init__(
        self,
        title: str = "Application",
        *,
        small_icon: str = '',
        large_icon: str = '',
        width: int = 1280,
        height: int = 800,
        x_pos: int = 100,
        y_pos: int = 100,
        min_width: int = 250,
        max_width: int = 10000,
        min_height: int = 250,
        max_height: int = 10000,
        resizable: bool = True,
        vsync: bool = True,
        always_on_top: bool = False,
        clear_color: list[float] = (0, 0, 0, 255),
        decorated: bool = True,

        staging_mode: bool = False,
        enable_docking: bool = False,
        dock_space: bool = False,
        theme: Theme = None
    ):
        # setting `self._item_config` as empty prevents __getattribute__ from
        # making calls that would raise internal errors (since the viewport
        # hasn't been created yet). `self._item_config` is deleted later in 
        # _setup_viewport.
        self._item_config = ()
        self.__staging_mode = staging_mode
        self.__docking_enabled = enable_docking
        self.__dock_space = dock_space
        self.__primary_window = None
        self.__primary_window_enabled = False

        self.title = title
        self.small_icon = small_icon
        self.large_icon = large_icon
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height
        self.resizable = resizable
        self.vsync = vsync
        self.always_on_top = always_on_top
        self.clear_color = clear_color
        self.decorated = decorated

        # Initializing mixins only.
        ThemeSupport.__init__(self)
        AppHandlerSupport.__init__(self)

        self.theme = theme or DEFAULT

        if sys.platform == "win32":
            # This lets the application use the real resolution of your
            # display(s) instead of a virtual one that Windows might be set
            # to use.
            self.disable_virtual_scaling()

        self._setup_viewport()


    def __repr__(self):
        return f"{self.__class__.__qualname__} ({type(self)}) =>"

    def __int__(self):
        return str(self.id)

    def __str__(self):
        return self.title

    def __getattribute__(self, attr: str):
        if attr in object.__getattribute__(self, "_item_config"):
            return get_viewport_configuration()[attr]

        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr in object.__getattribute__(self, "_item_config"):
            configure_viewport(self.id, **{attr: value})
        else:
            object.__setattr__(self, attr, value)

    @property
    def exists(self):
        return self.__exists

    def configure(self, **config):
        """Updates the viewport configuration.
        
        """
        dpg.configure_viewport(self.id, **config)

    def configuration(self, option=None):
        """Returns the entire current viewport configuration, or only
        <option> if specified.
        """
        if option:
            return dpg.get_viewport_configuration(self.id)[option]

        return dpg.get_viewport_configuration(self.id)

    def maximize(self):
        """Maximizes the viewport.
        """
        dpg.maximize_viewport()

    def minimize(self):
        """Minimizes the viewport.
        """
        dpg.minimize_viewport()


    ##########################################
    ########## Callback Decorators ###########
    ##########################################
    @classmethod
    def on_resize(cls, func):
        """Adds <func> to a list of functions that will be
        called when the viewport is resized (in the order that
        they are added).
        """
        cls.called_on_resize.append(func)
        return func

    @classmethod
    def on_render(cls, func):
        """Adds <func> to a list of functions that will be
        called while the main loop is running (in the order that they are added).
        """
        cls.called_on_render.append(func)
        return func

    @classmethod
    def on_start(cls, func):
        """Adds <func> to a list of functions that will be
        called before the main loop (in the order that they are added).
        """
        cls.called_on_start.append(func)
        return func

    @classmethod
    def on_exit(cls, func):
        """Adds <func> to a list of functions that will be
        called as the main loop ends (in the order that they are added).
        """
        cls.called_on_exit.append(func)
        return func

    ##########################################
    ############### Main Loop ################
    ##########################################
    @classmethod
    def register_callbacks(cls):
        """Register all callbacks.
        """
        dpg.set_start_callback(lambda: [f() for f in cls.called_on_start])
        dpg.set_exit_callback(lambda: [f() for f in cls.called_on_exit])
        dpg.set_viewport_resize_callback(lambda: [
            f() for f in cls.called_on_resize])

    @classmethod
    def call_render_callbacks(cls):
        """Calls all on-render callbacks.

        """
        [f() for f in cls.called_on_render]
        #return lambda: [f() for f in cls.called_on_render]

    @property
    def is_running(self):
        return idpg.is_dearpygui_running()

    def render_frame(self):
        """Renders a frame.

        """
        return idpg.render_dearpygui_frame()

    def cleanup(self):
        idpg.cleanup_dearpygui()

    def start(self):
        """Registers callbacks and starts the main render loop. For
        complex/detailed UI, you may wish to create this loop manually:

            ...
            app = Viewport()
            app.register_callbacks() 
            while app.is_running:
                # do stuff
                app.call_render_callbacks()
                # do more stuff
                app.render_frame()
            app.cleanup()

        """
        self.register_callbacks()
        render_callbacks = self.call_render_callbacks
        while idpg.is_dearpygui_running():
            render_callbacks()
            idpg.render_dearpygui_frame()
        idpg.cleanup_dearpygui()

    @staticmethod
    def stop():
        """Stops the main render loop.
        """
        dpg.stop_dearpygui()


    @property
    def primary_window(self) -> Window:
        return self.__primary_window
    @primary_window.setter
    def primary_window(self, value):
        self.__primary_window = value
        if self.__primary_window_enabled:
            dpg.set_primary_window(int(value), True)

    @property
    def primary_window_enabled(self) -> bool:
        return self.__primary_window_enabled
    @primary_window_enabled.setter
    def primary_window_enabled(self, value: bool):
        dpg.set_primary_window(int(self.__primary_window), value)

    def set_primary_window(self, window: Window, value: bool = False):
        self.__primary_window = window
        self.__primary_window_enabled = value
        dpg.set_primary_window(int(self.__primary_window), value)


    # mouse
    @property
    def mouse_drag_delta(self):
        return idpg.get_mouse_drag_delta()
    
    @property
    def local_mouse_pos(self):
        return idpg.get_mouse_pos()

    @property
    def global_mouse_pos(self):
        return idpg.get_mouse_pos(local=False)

    @property
    def drawing_mouse_pos(self):
        return idpg.get_drawing_mouse_pos()

    def get_mouse_pos(self, local: bool = True):
        return idpg.get_mouse_pos(local=local)


    def frame_count(self):
        return dpg.get_frame_count()

    def runtime(self):
        """Returns the time that has elapsed since the main render loop
        was started.
        """
        return dpg.get_total_time()

    def framerate(self):
        """Returns the average frames per second (independant of
        the display's refresh rate).
        """
        frames = idpg.get_frame_count() or 1
        t = idpg.get_total_time() or 1
        return round(frames / t)

    def event_handlers(self):
        """Returns a list of event handlers that are currently registered
        to the application.

        NOTE: Calling the `delete` method on the references in the returned
        list will unregister the handler from the application and destroy the
        handler.
        """
        cls = type(self)
        registry_id = idpg.mvReservedUUID_1
        return [cls.APPITEMS[item] for item in cls.APPITEMS if
                idpg.get_item_info(item)["parent"] == registry_id]


    @property
    def docking_enabled(self) -> bool:
        return self.__docking_enabled

    @property
    def global_font_scale(self):
        return dpg.get_global_font_scale()
    @global_font_scale.setter
    def global_font_scale(self, value: float):
        dpg.set_global_font_scale(value)

    @property
    def staging_mode(self):
        return self.__staging_mode
    @staging_mode.setter
    def staging_mode(self, value: bool):
        self.__staging_mode = value
        dpg.set_staging_mode(mode=value)

    ##########################################
    ############# Windows-only  ##############
    ##########################################
    if sys.platform == "win32":
        @staticmethod
        def set_transparent_color(rgb: tuple[int, int, int]):
            """Sets a color to be transparent. Anything painted that color
            will be transparent instead. Transparent parts of items can
            be clicked through. Only one color can be set as transparent
            at a time - the old one will be unset for subsequent calls.

            NOTE: If this is called, you will lose ALL functionality of the
            viewport title bar, including dragging the window, and the 'close'
            button. It is strongly advised to set the instance attribute
            `decorated` to False, and implement a way of correctly stopping
            the main loop using the `stop` method within the application.

            Args:
                rgb (tuple[int, int, int]): The color that will be transparent.

            """
            return _c_types.set_transparent_color(rgb)

        @staticmethod
        def restore_color():
            """Removes the transparency from the set transparent color
            i.e. color is no longer transparent. Functionality to the
            application title bar might not be restored.

            """
            return _c_types.restore_color()

        @staticmethod
        def enable_virtual_scaling():
            """Use the current 'Scale and layout' display setting in Windows
            for this process. Renders may suffer from quality loss (from being
            stretched), and may also affect how well items scale within the
            application window.

            """
            return _c_types.enable_virtual_scaling()

        @staticmethod
        def disable_virtual_scaling():
            """Ignore the 'Scale and layout' display setting in Windows
            for this process.

            """
            return _c_types.disable_virtual_scaling()

    ##########################################
    ########### Internal-use Only ############
    ##########################################
    __exists = False
    _command = dpg.create_viewport
    _id = "DPG_NOT_USED_YET"
    _item_config = (
        "title",
        "small_icon",
        "large_icon",
        "width",
        "height",
        "x_pos",
        "y_pos",
        "min_width",
        "max_width",
        "min_height",
        "max_height",
        "resizable",
        "vsync",
        "always_on_top",
        "clear_color",
        "decorated",
    )

    def _setup_viewport(self):
        cls = type(self)

        if cls.__exists:
            raise ViewportError("Instance already exists, and only 1 instance can exist.")

        cls.__exists = True

        config = {option:getattr(self, option) for option in cls._item_config}
        cls._command(**config)
        # Now __getattribute__ can properly set configuration
        # options with the viewport made.
        del self._item_config

        # must be called before dpg.setup_dearpygui
        if self.__docking_enabled:  
            dpg.enable_docking(dock_space=self.__dock_space)

        dpg.setup_dearpygui(viewport=self.id)
        dpg.show_viewport(self.id)

        # Re-binding the global reference to the real viewport
        dpgwidgets.Application = self
    



class _Viewport(Viewport):
    """Creates a dummy viewport instance. Intended to be bound to
    'dpgwidgets.__init__.Application'.
    """
    def __init__(self):
        # Initializing mixins
        [c.__init__(self) for c in Viewport.__bases__
         if c.__name__.endswith("Support")]

        # Fetching parameters
        vp_attrs = inspect.signature(Viewport).parameters.values()
        vp_attrs = {p.name: p.default for p in
                      vp_attrs if p.name != "kwargs"}

        self._item_config = ()
        # Hard-coded for intellisense/language servers...
        self.title = vp_attrs["title"]
        self.small_icon = vp_attrs["small_icon"]
        self.large_icon = vp_attrs["large_icon"]
        self.width = vp_attrs["width"]
        self.height = vp_attrs["height"]
        self.x_pos = vp_attrs["x_pos"]
        self.y_pos = vp_attrs["y_pos"]
        self.min_width = vp_attrs["min_width"]
        self.max_width = vp_attrs["max_width"]
        self.min_height = vp_attrs["min_height"]
        self.max_height = vp_attrs["max_height"]
        self.resizable = vp_attrs["resizable"]
        self.vsync = vp_attrs["vsync"]
        self.always_on_top = vp_attrs["always_on_top"]
        self.clear_color = vp_attrs["clear_color"]
        self.decorated = vp_attrs["decorated"]


## Misc stuff ##
@contextmanager
def mutex():
   try:
       yield dpg.lock_mutex()
   finally:
       dpg.unlock_mutex()
