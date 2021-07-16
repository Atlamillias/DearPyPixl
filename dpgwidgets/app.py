from typing import Any, Callable
from contextlib import contextmanager

from dpgwidgets import dpg, Item, _Registry
from dpgwidgets.theme import ThemeSupport
from dpgwidgets.handler import AppHandlerSupport
from dpgwidgets.constants import THEME_IMGUI_DARK


class Viewport(ThemeSupport, AppHandlerSupport):
    # This class doesn't subclass <class "Item"> because
    # everything needs to be re-defined regardless.
    # Whatever isn't re-defined would just raise an error.
    # The overall structure is identical.
    __command = dpg.create_viewport
    __id = "DPG_NOT_USED_YET"
    __config = set()
    # callbacks to register during setup
    called_on_start = []  # set on system/application
    called_on_exit = []  # set on system/application
    called_on_resize = []  # set on viewport

    def __init__(
        self,
        title: str = "Application",
        *,
        # config passed to dpg
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
        # addl. settings
        staging_mode: bool = False,
        enable_docking: bool = False,
        dock_space: bool = False,
    ):
        super().__init__()
        # viewport config
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
        
        # misc. stuff set on viewport
        self.__docking_enabled = enable_docking  # must be called before vp setup
        self.__primary_window = None

        # app-level config
        self.__staging_mode = staging_mode
        self.theme.configure(**THEME_IMGUI_DARK)

        # setup viewport
        self.__config = dict(
            title=title,
            small_icon=small_icon,
            large_icon=large_icon,
            width=width,
            height=height,
            x_pos=x_pos,
            y_pos=y_pos,
            min_width=min_width,
            max_width=max_width,
            min_height=min_height,
            max_height=max_height,
            resizable=resizable,
            vsync=vsync,
            always_on_top=always_on_top,
            maximized_box=maximized_box,
            minimized_box=minimized_box,
            border=border,
            caption=caption,
            overlapped=overlapped,
            clear_color=clear_color,
        )
        self.__class__.__command(**self.__config)
        self.__config = {*self.__config.keys()}
        if enable_docking:
            self.__docking_enabled = True
            dpg.enable_docking(dock_space=dock_space)
        dpg.setup_dearpygui(viewport=self.__id)
        dpg.show_viewport(self.__id)

    def __repr__(self):
        return f"{self.__class__.__qualname__} ({type(self)}) =>"

    def __int__(self):
        # viewport id is currently a string literal in dpg
        return str(self.__id)

    def __str__(self):
        return self.title

    def __getattribute__(self, attr: str):
        _getattribute = super().__getattribute__
        if attr.startswith("_"):
            return _getattribute(attr)
        elif attr in _getattribute("_Viewport__config"):
            id = _getattribute("_Viewport__id")
            return dpg.get_viewport_configuration(id)[attr]

        return _getattribute(attr)

    def __setattr__(self, attr, value):
        if attr in object.__getattribute__(self, "_Viewport__config"):
            dpg.configure_viewport(self.__id, **{attr: value})
        else:
            object.__setattr__(self, attr, value)

    @property
    def id(self):
        return self.__id

    def configure(self, **config):
        """Updates the viewport configuration.
        """
        dpg.configure_viewport(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current viewport configuration, or only
        <option> if specified.
        """
        if option:
            return dpg.get_viewport_configuration(self.__id)[option]

        return dpg.get_viewport_configuration(self.__id)

    def maximize(self):
        """Maximizes the viewport.
        """
        dpg.maximize_viewport(self.__id)

    def minimize(self):
        """Minimizes the viewport.
        """
        dpg.minimize_viewport(self.__id)

    def show_dev_window(self):
        from dpgwrap.containers import Window
        from dpgwrap.widgets import Button

        with Window("Dev Tools", width=300, no_move=True, no_close=True, no_resize=True) as dev:
            dev.tstyle.window_padding = 0, 0
            dev.tcolor.title_bg = (
                0.14 * 255, 0.14 * 255, 0.14 * 255, 1.00 * 255)
            dev.tcolor.window_bg = (0.06 * 255, 0.06 * 255, 0.06 * 255, 125)
            dev.tcolor.title_bg_active = (
                0.14 * 255, 0.14 * 255, 0.14 * 255, 1.00 * 255)
            dev.pos = (self.width - dev.width, 20)
            dev.height = self.height
            btn_width = dev.width
            Button("Documentation", callback=show_documentation, width=btn_width)
            Button("Debug", callback=show_debug, width=btn_width)
            Button("Style Editor", callback=show_style_editor, width=btn_width)
            Button("Metrics", callback=show_metrics, width=btn_width)
            Button("About", callback=show_about, width=btn_width)
            Button("Font Manager", callback=show_font_manager, width=btn_width)
            Button("Item Registry", callback=show_item_registry, width=btn_width)
            Button("Logger", callback=show_logger, width=btn_width)

        @self.on_resize
        def devwin_pos():
            dev.pos = (self.width - dev.width, 20)
            dev.height = self.height


    # Addl. handlers/callback stuff
    def on_resize(self, func):
        """Adds <func> to a list of functions that will be
        called when the viewport is resized (in the order that
        they are added).
        """
        self.called_on_resize.append(func)

        return func

    def on_start(self, func):
        """Adds <func> to a list of functions that will be
        called before the main loop (in the order that they are added).
        """
        self.called_on_start.append(func)

        return func

    def on_exit(self, func):
        """Adds <func> to a list of functions that will be
        called as the main loop ends (in the order that they are added).
        """
        self.called_on_exit.append(func)

        return func


    # High-level setup, start/stop
    def register_callbacks(self):
        """Register all callbacks.
        """
        dpg.set_start_callback(lambda: [f() for f in self.called_on_start])
        dpg.set_exit_callback(lambda: [f() for f in self.called_on_exit])
        dpg.set_viewport_resize_callback(lambda: [
            f() for f in self.called_on_resize])

    def start(self):
        """Registers callbacks and starts the main render loop.
        """
        self.register_callbacks()
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.cleanup_dearpygui()

    @staticmethod
    def stop():
        """Stops the main render loop.
        """
        dpg.stop_dearpygui()


    # Misc.
    @property
    def time_elapsed(self):
        """Returns the time that has elapsed since the main render loop
        was started.
        """
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

    @property
    def primary_window(self):
        return self.__primary_window

    def set_primary_window(self, state: bool, window: int = None):
        if window is not None:
            self.__primary_window = window

        dpg.set_primary_window(int(self.__primary_window), state)




## Useful commands (most are copy/paste from dearpygui) ##
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
