from typing import Any
from contextlib import contextmanager

from . import idpg
from .dpgwrap.containers import Window
from .dpgwrap.registries import (
    FontRegistry, 
    TextureRegistry, 
    HandlerRegistry, 
    ValueRegistry
)



class Application:
    called_on_start = []
    called_on_exit = []

    def __init__(self) -> None:
        self.viewport = Viewport()

        # Registries
        self.fonts = FontRegistry(id=idpg.mvReservedUUID_0)
        self.handlers = HandlerRegistry(id=idpg.mvReservedUUID_1)
        self.textures = TextureRegistry(id=idpg.mvReservedUUID_2)
        self.values = ValueRegistry(id=idpg.mvReservedUUID_3)

        self.__theme = None
        self.__primary_window = None
        self.__staging_mode = False
        self.__docking_mode = False

        self.viewport.setup()
        self.viewport.show()

    def register_callbacks(self):
        idpg.set_start_callback(lambda: [f() for f in self.called_on_start])
        idpg.set_exit_callback(lambda: [f() for f in self.called_on_exit])

    def start(self):
        self.register_callbacks()

        while idpg.is_dearpygui_running():
            idpg.render_dearpygui_frame()

        idpg.cleanup_dearpygui()

    @staticmethod
    def stop():
        idpg.stop_dearpygui()


    ## Decorators ##
    def on_start(self, func):
        """Adds <func> to a list of functions that will be
        called before the main loop."""
        self.called_on_start.append(func)

        return func

    def on_exit(self, func):
        """Adds <func> to a list of functions that will be
        called as the main loop ends."""
        self.called_on_exit.append(func)

        return func

    
    ## Misc. ##
    @property
    def time_elapsed(self):
        return idpg.get_total_time()

    @property
    def global_font_scale(self):
        return idpg.get_global_font_scale()

    @global_font_scale.setter
    def global_font_scale(self, value: float):
        idpg.set_global_font_scale(value)

    @property
    def primary_window(self):
        return self.__primary_window

    @primary_window.setter
    def primary_window(self, window):
        if isinstance(window, (Window, int)):
            self.__primary_window = window
            idpg.set_primary_window(int(window),True)
        elif window is None and self.__primary_window:
            idpg.set_primary_window(int(self.__primary_window), False)
            self.__primary_window = window
        else:
            raise TypeError("Value must be of type <int>, <Window>.")

    @property
    def staging_mode(self):
        return self.__staging_mode

    @staging_mode.setter
    def staging_mode(self, value: bool):
        self.__staging_mode = value
        idpg.set_staging_mode(mode=value)

    @property
    def docking_mode(self):
        return self.__docking_mode

    @docking_mode.setter
    def docking_mode(self, value: bool):
        self.__docking_mode = value
        idpg.enable_docking(dock_space=value)


class Viewport:
    # Note: DPG currently only allows 1 viewport per loop
    __config = {}
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
        resizable: bool = True,
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
        self.__id = idpg.create_viewport(**self.__config)

    def __str__(self):
        return f"{self.__id}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}"

    def __getattr__(self, attr):
        if attr in self.__config:
            try:
                return idpg.get_viewport_configuration(self.__id)
            except KeyError:
                return super().__getattr__(attr)

        return super().__getattr__(attr)

    def __setattr__(self, attr, value):
        if attr in self.__config:
            idpg.configure_viewport(self.__id, **{attr: value})
        else:
            super().__setattr__(attr, value)

    @property
    def id(self):
        return self.__id

    def configure(self, **config):
        """Updates the viewport configuration."""
        idpg.configure_viewport(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current viewport configuration, or
        <option> if specified."""
        if option:
            return idpg.get_viewport_configuration(self.__id)[option]

        return idpg.get_viewport_configuration(self.__id)

    def maximize(self):
        """Maximize the viewport"""
        idpg.maximize_viewport(self.__id)

    def minimize(self):
        """Minimize the viewport."""
        idpg.minimize_viewport(self.__id)

    def setup(self):
        idpg.setup_dearpygui(viewport=self.__id)

    def show(self):
        """Display the viewport."""
        idpg.show_viewport(self.__id)

    # Decorator
    def on_resize(self, func):
        """Updates the viewport callback collection."""
        self.called_on_resize.add(func)
        idpg.set_viewport_resize_callback(lambda: [
            f() for f in self.called_on_resize])

        return func



## Misc. (most are copy/paste from dearpygui) ##
@contextmanager
def mutex():
   try:
       yield idpg.lock_mutex()
   finally:
       idpg.unlock_mutex()


def show_style_editor(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_Style)


def show_metrics(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_Metrics)


def show_about(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_About)


def show_debug(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_Debug)


def show_documentation(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_Doc)


def show_font_manager(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_Font)


def show_item_registry(sender: str = "", data: Any = None):
    idpg.show_tool(idpg.mvTool_ItemRegistry)
