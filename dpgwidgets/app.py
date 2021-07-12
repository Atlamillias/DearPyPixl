from typing import Any, Callable
from contextlib import contextmanager

from . import dpg
from .handler import AppHandler
from .theme import Theme as AppTheme
from .dpgwrap.registries import (
    FontRegistry, 
    TextureRegistry,  
    ValueRegistry
)


# Application and Viewport classes kinda share
# responsibilities. This is mostly because at the moment
# DPG only supports 1 viewport. However in the future
# it may support several, so they will need to be 
# more de-coupled.
class Application:
    called_on_start = []
    called_on_exit = []

    def __init__(
        self, 
        enable_staging: bool = False, 
        enable_docking: bool = False,
        dock_space: bool = False,
        show_dev_tools:bool = False
    ):
        self.viewport = Viewport()

        # Registries (WIP)
        self.__fonts = FontRegistry(id=dpg.mvReservedUUID_0)
        self.__handler = AppHandler(id=dpg.mvReservedUUID_1)
        self.__textures = TextureRegistry(id=dpg.mvReservedUUID_2)
        self.__values = ValueRegistry(id=dpg.mvReservedUUID_3)

        self.__theme = AppTheme()
        self.__docking_enabled = False
        self.__dev_tools = True if show_dev_tools else False
        self.__staging_mode = enable_staging
        
        if enable_docking:
            dpg.enable_docking(dock_space=dock_space)
            self.__docking_enabled = True

        self.viewport.setup()
        self.viewport.show()


    def register_callbacks(self):
        dpg.set_start_callback(lambda: [f() for f in self.called_on_start])
        dpg.set_exit_callback(lambda: [f() for f in self.called_on_exit])

    def start(self):
        self.register_callbacks()
        if self.__dev_tools:
            self.viewport._show_dev_toolbar()

        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()

        dpg.cleanup_dearpygui()

    @staticmethod
    def stop():
        dpg.stop_dearpygui()


    ## Decorators ##
    def on_start(self, func):
        """Adds <func> to a list of functions that will be
        called before the main loop (in the order that they are added)."""
        self.called_on_start.append(func)

        return func

    def on_exit(self, func):
        """Adds <func> to a list of functions that will be
        called as the main loop ends (in the order that they are added)."""
        self.called_on_exit.append(func)

        return func

    ## Registries ##
    @property
    def fonts(self):
        return self.__fonts


    @property
    def values(self):
        return self.__values

    @property
    def textures(self):
        return self.__textures

    ## Handler ##
    @property
    def handle(self):
        return self.__handler

    def unhandle(self, handler_type: str, callback: Callable):
        return self.__handler.unhandle(handler_type, callback)
    
    ## Theme ##
    @property
    def theme(self):
        return self.__theme

    @property
    def color(self):
        return self.__theme.color

    @property
    def style(self):
        return self.__theme.style


    ## Misc. ##
    @property
    def time_elapsed(self):
        return dpg.get_total_time()
    
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

    @property
    def docking_enabled(self):
        return self.__docking_enabled


class Viewport:
    # Note: DPG currently only allows 1 viewport
    # so only call once
    __config = {}
    __primary_window = None
    called_on_resize = []

    def __init__(
        self,
        title: str = "Application",
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
        resizable: bool = True,  # not working?
        vsync: bool = True,
        always_on_top: bool = False,
        maximized_box: bool = True,
        minimized_box: bool = True,
        border: bool = True,
        caption: bool = True,
        overlapped: bool = True,
        clear_color: list[float] = [0, 0, 0, 255],
    ):
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
        self.maximized_box = maximized_box
        self.minimized_box = minimized_box
        self.border = border
        self.caption = caption
        self.overlapped = overlapped
        self.clear_color = clear_color

        self.__config = {
            "title": title,
            "small_icon": small_icon,
            "large_icon": large_icon,
            "width": width,
            "height": height,
            "x_pos": x_pos,
            "y_pos": y_pos,
            "min_width": min_width,
            "max_width": max_width,
            "min_height": min_height,
            "max_height": max_height,
            "resizable": resizable,
            "vsync": vsync,
            "always_on_top": always_on_top,
            "maximized_box": maximized_box,
            "minimized_box": minimized_box,
            "border": border,
            "caption": caption,
            "overlapped": overlapped,
            "clear_color": clear_color,
        }

        # __getitem__ will ask dpg for all of the above
        # if this is called before setting instance attrs
        self.__id = dpg.create_viewport(**self.__config)

    def __str__(self):
        return f"{self.__id}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}"

    def __getattr__(self, attr):
        if attr in self.__config:
            try:
                return dpg.get_viewport_configuration(self.__id)
            except KeyError:
                return super().__getattr__(attr)

        return super().__getattr__(attr)

    def __setattr__(self, attr, value):
        if attr in self.__config:
            dpg.configure_viewport(self.__id, **{attr: value})
        else:
            super().__setattr__(attr, value)

    def _show_dev_toolbar(self):
        from .dpgwrap.containers import Menu, ViewportMenuBar
        from .dpgwrap.widgets import MenuItem

        with ViewportMenuBar():
            with Menu("Development") as dev:
                MenuItem("Documentation", callback=show_documentation)
                MenuItem("Debug", callback=show_debug)
                MenuItem("Style Editor", callback=show_style_editor)
                MenuItem("Metrics", callback=show_metrics)
                MenuItem("About", callback=show_about)
                MenuItem("Font Manager", callback=show_font_manager)
                MenuItem("Item Registry", callback=show_item_registry)
                MenuItem("Logger", callback=show_logger)

    @property
    def id(self):
        return self.__id

    def configure(self, **config):
        """Updates the viewport configuration."""
        dpg.configure_viewport(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current viewport configuration, or
        <option> if specified."""
        if option:
            return dpg.get_viewport_configuration(self.__id)[option]

        return dpg.get_viewport_configuration(self.__id)

    def maximize(self):
        """Maximize the viewport"""
        dpg.maximize_viewport(self.__id)

    def minimize(self):
        """Minimize the viewport."""
        dpg.minimize_viewport(self.__id)

    def setup(self):
        dpg.setup_dearpygui(viewport=self.__id)

    def show(self):
        """Display the viewport."""
        dpg.show_viewport(self.__id)

    # Decorator
    def on_resize(self, func):
        """Updates the viewport callback collection."""
        self.called_on_resize.add(func)
        dpg.set_viewport_resize_callback(lambda: [
            f() for f in self.called_on_resize])

        return func

    @property
    def primary_window(self):
        return self.__primary_window

    def set_primary_window(self, state: bool, window: int = None):
        if window is not None:
            self.__primary_window = window

        dpg.set_primary_window(int(self.__primary_window), state)


## Misc. (most are copy/paste from dearpygui) ##
@contextmanager
def mutex():
   try:
       yield dpg.lock_mutex()
   finally:
       dpg.unlock_mutex()


def show_style_editor(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Style)


def show_metrics(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Metrics)


def show_about(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_About)


def show_debug(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Debug)


def show_documentation(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Doc)


def show_font_manager(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Font)


def show_item_registry(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_ItemRegistry)


def show_logger(sender: str = "", data: Any = None):
    from dearpygui import logger
    logger.mvLogger()
