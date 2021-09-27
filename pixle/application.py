from typing import Callable, Any, Union
from abc import ABCMeta as _ABCMeta
import sys
import ctypes
from dearpygui import dearpygui, _dearpygui
# Many of these tend to be called between frames as render
# callbacks -- trying to avoid lookup overhead.
from dearpygui._dearpygui import (
    # mainloop
    render_dearpygui_frame,
    is_dearpygui_running,
    cleanup_dearpygui,
    stop_dearpygui,
    # getters
    get_mouse_drag_delta,
    get_drawing_mouse_pos,
    get_plot_mouse_pos,
    get_mouse_pos,
    get_total_time,
    get_frame_count,
)
from pixle.itemtypes import Item as _Item
from pixle.itemtypes.support import EventSupport
from pixle.theming import Theme
from pixle.events import (
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
]


class UniqueMeta(_ABCMeta):
    __application__ = None
    def __call__(cls, *args, **kwargs):
        if cls.__application__ is None:
            cls.__application__ = super().__call__(*args, **kwargs)
        return cls.__application__

class UniqueItem(_Item):
    def __init__(
        self,
        enable_docking: bool = False,
        dock_space: bool = False,
        virtual_scaling: bool = False,
    ):
        # This needs to be set before the viewport is created,
        # and cannot be changed afterwards.
        type(self)._command()  # viewport creation
        if enable_docking:
            dearpygui.enable_docking(dockspace=dock_space)
        # This can be changed.
        if sys.platform == "win32" and not virtual_scaling:
            self.disable_virtual_scaling()
        dearpygui.setup_dearpygui(viewport=self.id)

    # These inherited methods do not work for this class, and have
    # been overloaded and listed here for clarity.
    def unstage(self) -> NotImplemented:
        return NotImplemented

    def delete(self) -> NotImplemented:
        return NotImplemented

    def duplicate(self) -> NotImplemented:
        return NotImplemented


class Application(EventSupport, UniqueItem, metaclass=UniqueMeta):
    """Creates and performs setup on the viewport. Directly manages application
    settings. 

    Application is a singleton - only one instance can exist at a time.
    Multiple attempts at instantiation will return the existing instance.

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
        clear_color: list[float] = (0, 0, 0, 255),
        decorated: bool = True,
        
        enable_docking: bool = False,
        dock_space: bool = False,

        theme: Theme = None,
        virtual_scaling: bool = False,
    ):  
        super().__init__(
            enable_docking=enable_docking,
            dock_space=dock_space,
            virtual_scaling=virtual_scaling
        )
        self.__virtual_scaling = virtual_scaling
        self.__dock_space = dock_space
        self.__docking_mode = enable_docking
        self.__staging_mode = False
        self.__primary_window = None
        self.__use_primary_window = False

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

        self.theme = theme or Theme()

        self.called_on_start: list[Callable] = []
        self.called_on_exit: list[Callable] = []
        self.called_on_render: list[Callable] = []
        self.called_on_resize: list[Callable] = []

    def __str__(self):  # Overloaded from Item
        return self.title

    def __getattr__(self, attr):  # Overloaded from Item
        try:
            return dearpygui.get_viewport_configuration(self._id)[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __setattr__(self, attr, value):  # Overloaded from Item
        # Allowing special methods, descriptors, etc. first.
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        elif attr in self._configurations:
            return dearpygui.configure_viewport(self._id, **{attr: value})
        object.__setattr__(self, attr, value)


    ################################
    ###### App Setup/Mainloop ######
    ################################
    def register_callbacks(self) -> None:
        """Register start, exit, and resize callbacks.
        """
        _dearpygui.set_start_callback(lambda: [f() for f in self.called_on_start])
        _dearpygui.set_exit_callback(lambda: [f() for f in self.called_on_exit])
        _dearpygui.set_viewport_resize_callback(lambda: [f() for f in self.called_on_resize])

    def call_on_render_callbacks(self) -> None:
        """Calls all on-render callbacks.
        """
        [f() for f in self.called_on_render]

    def show_viewport(self) -> None:
        """Show the viewport. Icon configuration options can't be changed once
        showing the viewport.
        """
        type(self)._is_viewport_showing = True
        return _dearpygui.show_viewport(self._id)

    @classmethod
    def start(cls) -> None:
        # Verify a configured viewport
        if cls.__application__ is None:
            cls.__application__ = cls()
        # Verify viewport is showing
        if not cls._is_viewport_showing:
            _dearpygui.show_viewport(cls._id)

        application = cls.__application__
        application.register_callbacks()
        call_on_render_callbacks = application.call_on_render_callbacks
        while is_dearpygui_running():
            call_on_render_callbacks()
            render_dearpygui_frame()
        cleanup_dearpygui()

    @staticmethod
    def stop() -> None:
        """Stops the main render loop.
        """
        stop_dearpygui()

    @staticmethod
    def cleanup() -> None:
        cleanup_dearpygui()

    @staticmethod
    def render_frame() -> None:
        """Renders a frame.
        """
        return render_dearpygui_frame()

    @property
    def is_running(self) -> bool:
        return is_dearpygui_running()
    
    @property
    def is_viewport_showing(self) -> bool:
        return self._is_viewport_showing

    ################################
    ######## Event Handlers ########
    ################################

    # NOTE: These handle events but are not event handler items.
    def on_resize(self, func) -> Callable:
        """Adds *func* to a list of functions that will be called when
        the viewport is resized (in the order that they are added).
        """
        self.called_on_resize.append(func)
        return func

    def on_render(self, func) -> Callable:
        """Adds *func* to a list of functions that will be called while
        the main loop is running (in the order that they are added).
        """
        self.called_on_render.append(func)
        return func

    def on_start(self, func) -> Callable:
        """Adds *func* to a list of functions that will be called before
        the main loop (in the order that they are added).
        """
        self.called_on_start.append(func)
        return func

    def on_exit(self, func) -> Callable:
        """Adds *func* to a list of functions that will be called as the
        main loop ends (in the order that they are added).
        """
        self.called_on_exit.append(func)
        return func

    # NOTE: These are event handler items (managed by the EventSupport mixin).
    def while_key_down(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, key=key, **kwargs)

    def on_key_press(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, key=key, **kwargs)

    def on_key_up(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, key=key, **kwargs)

    def while_mouse_down(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, **kwargs)

    def on_mouse_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, **kwargs)

    def on_mouse_double_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, **kwargs)

    def on_mouse_up(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, **kwargs)

    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_drag(self, callback: Callable = None, *, button: int = -1, threshold: float = 10.0, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, threshold=threshold, **kwargs)

    ################################
    ########## Properties ##########
    ################################
    @property
    def theme(self) -> Theme:  # Overloaded from ThemeHandler
        return self.__theme
    @theme.setter
    def theme(self, value: Theme):  # Overloaded from ThemeHandler
        self.__theme = value
        try:
            value._set_as_default()
        except TypeError:
            raise TypeError(f"value of 'theme' cannot be `None`.")

    @property
    def staging_mode(self) -> bool:
        return self.__staging_mode
    @staging_mode.setter
    def staging_mode(self, value: bool):
        self.__staging_mode = value
        _dearpygui.set_staging_mode(mode=value)

    @property
    def font_scaling(self) -> float:
        return _dearpygui.get_global_font_scale()
    @font_scaling.setter
    def font_scaling(self, value: float):
        _dearpygui.set_global_font_scale(value)

    @property
    def primary_window(self) -> UniqueItem:
        return self.__primary_window
    @primary_window.setter
    def primary_window(self, value):
        if not self.__primary_window:
            self.__use_primary_window = True
        self.__primary_window = value
        if self.__use_primary_window:
            _dearpygui.set_primary_window(value._id, True)

    @property
    def use_primary_window(self) -> bool:
        return self.__use_primary_window
    @use_primary_window.setter
    def use_primary_window(self, value: bool):
        _dearpygui.set_primary_window(value._id, value)

    @property
    def docking_mode(self) -> bool:
        return self.__docking_mode

    @property
    def dock_space(self) -> bool:
        return self.__dock_space

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

    if sys.platform == "win32":
        @property
        def virtual_scaling(self) -> bool:
            return self.__virtual_scaling
        @virtual_scaling.setter
        def virtual_scaling(self, value: bool):
            if not value:
                return self.disable_virtual_scaling()
            return self.enable_virtual_scaling()

    ################################
    ######## Misc. methods #########
    ################################
    def maximize(self) -> None:
        """Maximizes the viewport.
        """
        _dearpygui.maximize_viewport()

    def minimize(self) -> None:
        """Minimizes the viewport.
        """
        _dearpygui.minimize_viewport()

    def configuration(self, option: str = None) -> Union[dict[str, Any], Any]:  # Overloaded from Item
        """Returns the item's configuration options and values
        that are internally used to manage the item. If <option>
        is included, only the value of that option will be returned.
        
        NOTE: Typically, attributes included in configuration are the
        parameters used to create an instance of an item. This will
        not include other instance attributes, and does not replace
        `getattr`.
        """
        config = dearpygui.get_viewport_configuration(self)
        configurations = self._configurations
        config = {attr: val for attr, val in
                  dearpygui.get_viewport_configuration(self).items()
                  if attr in configurations or attr == "id"}
        return config.get(option, config)

    def children(self) -> list[UniqueItem]:  # Overloaded from Item
        """Returns a list of all tracked items.
        """
        child_ids = dearpygui.get_all_items()
        appitems = self.APPITEMS
        return [child for child_id in child_ids if
                (child:= appitems.get(child_id, None))]

    def handlers(self) -> list[UniqueItem]:  # Overloaded from Item
        """Returns a list of all application-level event handlers.
        """
        # Items in Slot 3 are event handlers.
        appitems = self.APPITEMS
        handler_ids = _dearpygui.get_item_info(self._handler_registry_id)["children"][3]
        return [handler for handler_id in handler_ids if
                (handler:=appitems.get(handler_id, None))]

    def frames(self) -> int:
        """Returns the number of frames rendered.
        """
        return get_frame_count()

    def framerate(self) -> int:
        """Returns the average frames rendered per second (rounded).
        """
        return round((get_frame_count() or 1) / (get_total_time() or 1))

    def runtime(self) -> float:
        """Returns the time that has elapsed since the main render loop
        was started.
        """
        return get_total_time()

    if sys.platform == "win32":
        @staticmethod
        def enable_virtual_scaling() -> None:
            """Use the current 'Scale and layout' display setting in Windows
            for this process. Renders may suffer from quality loss (from being
            stretched), and may also affect how well items scale within the
            application window.
            """
            ctypes.windll.shcore.SetProcessDpiAwareness(0)

        @staticmethod
        def disable_virtual_scaling() -> None:
            """Ignore the 'Scale and layout' display setting in Windows
            for this process.
            """
            ctypes.windll.shcore.SetProcessDpiAwareness(2)


    ################################
    ######### Internal-Use #########
    ################################

    # Default registry id's
    _font_registry_id = _dearpygui.mvReservedUUID_0
    _handler_registry_id = _dearpygui.mvReservedUUID_1
    _texture_registry_id = _dearpygui.mvReservedUUID_2
    _value_registry_id = _dearpygui.mvReservedUUID_3
    _colormap_registry_id = _dearpygui.mvReservedUUID_4

    _command = dearpygui.create_viewport
    _id = "DPG_NOT_USED_YET"
    _is_viewport_showing = False
    _configurations: set = {
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
    }
    _handler_map = {  # EventSupport abstractmethod
        "while_key_down": KeyDownHandler,
        "on_key_press": KeyPressHandler,
        "on_key_up": KeyReleaseHandler,
        "while_mouse_down":  MouseDownHandler,
        "on_mouse_click": MouseClickHandler,
        "on_mouse_double_click": MouseDoubleClickHandler,
        "on_mouse_up": MouseReleaseHandler,
        "on_mouse_wheel_scroll": MouseWheelHandler,
        "on_mouse_move": MouseMoveHandler,
        "on_mouse_drag": MouseDragHandler,
    }

