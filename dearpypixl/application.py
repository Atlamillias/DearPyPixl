import ctypes
from typing import Callable, Any, Literal
from typing_extensions import Self
from enum import IntEnum, Enum
import os
from dearpygui import _dearpygui, dearpygui
from dearpygui._dearpygui import (
    # mainloop
    render_dearpygui_frame,
    is_dearpygui_running,
    stop_dearpygui,
    # getters
    get_total_time,
    get_frame_count,
    is_key_pressed,
    is_key_down,
    is_key_released,
    get_global_font_scale,
    get_app_configuration,
    # setters
    set_global_font_scale,
    configure_app,
    # misc
    split_frame,
)
from dearpypixl.itemtypes.themes.presets import dearpygui_internal
from dearpypixl.itemtypes.events import FrameEvents, Key
from dearpypixl.itemtypes import (
    ItemProperty,
    CONFIG,
    INFORM,
    STATES,
    ItemIdType,
    Item,
    AppItem,
    Theme,
)
from dearpypixl.errors import err_viewport_showing


__all__ = [
    "Platform",
    "DPIAwareness",
    "DeviceManager",
    "Application",
]


_DEFAULT_THEME = dearpygui_internal
_FRAME_EVENTS  = FrameEvents()


class Platform(IntEnum):
    Windows = _dearpygui.mvPlatform_Windows
    Linux   = _dearpygui.mvPlatform_Linux
    MacOS   = _dearpygui.mvPlatform_Apple

    @classmethod
    def get(cls) -> Self:
        return cls(dearpygui.get_platform())


class DPIAwareness(IntEnum):
    Unaware    = 0
    System     = 1
    PerMonitor = 2


class DeviceManager(str, Enum):
    Manual   = "manual"
    System   = "system"
    Internal = "internal"




def _get_app_config(obj, name):
    return get_app_configuration()[name]


def _set_app_config(obj, name, value):
    if _dearpygui.is_viewport_ok():
        raise err_viewport_showing(name)
    configure_app(**{name: value})


class Application(AppItem):
    auto_device   : bool = ItemProperty(CONFIG, _get_app_config, _set_app_config)
    docking       : bool = ItemProperty(CONFIG, _get_app_config, _set_app_config)
    docking_space : bool = ItemProperty(CONFIG, _get_app_config, _set_app_config)
    device        : int  = ItemProperty(CONFIG, _get_app_config, _set_app_config)
    wait_for_input: bool = ItemProperty(CONFIG, _get_app_config, _set_app_config)

    @property
    @ItemProperty.register(category=CONFIG)
    def font_scale(self) -> float:
        return get_global_font_scale()
    @font_scale.setter
    def font_scale(self, value: float) -> None:
        set_global_font_scale()

    @property
    @ItemProperty.register(category=CONFIG)
    def theme(self) -> Theme:
        theme_uuid = self.__cached__["theme_uuid"]
        if not theme_uuid:
            return _DEFAULT_THEME
        return self.__registry__.get_item(theme_uuid)
    @theme.setter
    def theme(self, value: Theme) -> None:
        if not value:
            value = _DEFAULT_THEME
        value.bind()


    #### Information Properties ####
    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def tag(cls) -> int:
        return cls.__cached__["app_uuid"]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def device_manager(cls) -> DeviceManager:
        """Return the current controller of the display adapter used for the
        application.

        Possible returns:
            * DeviceManager.System: The display adapter has been set by your operating
            system.
            * DeviceManager.Internal: The display adapter has been set by DearPyGui.
            * DeviceManager.Manual: The display adapter has been manually selected.
        """
        device = cls.device
        auto_device = cls.auto_device
        if device != -1:
            return DeviceManager.Manual
        elif not auto_device:
            return DeviceManager.System
        return DeviceManager.Internal

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def process_id(cls) -> str:
        """Return the current process identifier.
        """
        return os.getpid()

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def version(cls) -> str:
        """Return the version of Dearpygui that is being used.
        """
        return _dearpygui.get_app_configuration()["version"]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def platform(cls) -> Platform:
        """Return the platform.
        """
        return Platform.get()

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def device_name(cls) -> str:
        """Return the name of the display adapter in use.
        """
        return _dearpygui.get_app_configuration()["device_name"]


    ###############################
    ########## Rendering ##########
    ###############################
    @staticmethod
    def render_frame() -> None:
        """Renders a frame. Only for use in the main render loop (see the `start` method).
        """
        render_dearpygui_frame()

    @classmethod
    def start(cls) -> None:
        """Start the application by executing the main render loop.
        """
        if not _dearpygui.is_viewport_ok():  # Viewport.show()
            _dearpygui.show_viewport()

        is_running   = cls.is_running
        render_frame = cls.render_frame
        frame_events = cls.frame_events[0]

        while is_running():
            for event in frame_events:
                event()
            render_frame()
        cls.end()

    @classmethod
    def stop(cls, *args, **kwargs) -> None:
        """Break the main render loop and stop the application
        if it is running. This is the equivelent to pressing the
        "close"/"exit" button on the application title bar.
        """
        if cls.is_running():
            stop_dearpygui()

    @staticmethod
    def end(*args, **kwargs) -> None:
        """Post-process clean-up. Must be called following the render
        loop to ensure proper 'cleanup' of system resources.
        """
        _dearpygui.destroy_context()


    ################################
    ######## Event Handling ########
    ################################
    ALL_FRAMES = FrameEvents.ALL_FRAMES
    LAST_FRAME = FrameEvents.LAST_FRAME

    @classmethod
    @property
    def frame_events(cls) -> FrameEvents:
        return _FRAME_EVENTS

    @classmethod
    def on_frame(cls, callback: Callable = None, /, *, frame: int = ALL_FRAMES, user_data: Any = None, **kwargs):
        """(Decorator) Schedules a callback to run on a specific frame.

        Args:
            * callback (Callable): Callable object to run.
            * frame (int, optional): The callback will run before this frame
            is rendered. If this value is 0, it will run every frame. If -1,
            it will run on the last frame (application exit). Defaults to 0.
            * user_data (Any, optional): This will be sent as the third positional
            argument to <callback>. Defaults to None.
        """
        return cls.frame_events.on_frame


    ################################
    ######## Other Methods #########
    ################################
    @classmethod
    def configure(cls, **config) -> None:
        # Set on internal instance.
        return Item.configure(_Application)

    @classmethod
    def configuration(cls) -> dict[str, Any]:
        # Set on internal instance.
        cfg_attrs  = cls.__internal__[0]
        dpg_config = get_app_configuration()
        config     = {attr:(dpg_config[attr] if attr in dpg_config else getattr(_Application, attr))
                      for attr in cfg_attrs}
        return config

    @classmethod
    def information(cls) -> dict[str, Any]:
        # These should all be classmethod properties, so this is straightforward.
        return Item.information(cls)

    @classmethod
    def state(cls) -> dict[str, Any]:
        return {"is_running": cls.is_running()}


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
        # render loop.
        return is_dearpygui_running()

    @staticmethod
    def is_key_pressed(key: Key | int) -> bool:
        """Return True if `key` is pressed, otherwise return False.

        Args:
            * key (Key | Mouse | int): Key | int event code to inquire
            about.
        """
        return is_key_pressed(int(key))

    @staticmethod
    def is_key_released(key: Key | int) -> bool:
        """Return True if `key` is released, otherwise return False.

        Args:
            * key (Key | Mouse | int): Key | int event code to inquire
            about.
        """
        return is_key_released(int(key))

    @staticmethod
    def is_key_down(key: Key | int) -> bool:
        """Return True if `key` is down, otherwise return False.

        Args:
            * key (Key | Mouse | int): Key | int event code to inquire
            about.
        """
        return is_key_down(int(key))


    ## Platform-specific ##
    if Platform.get() == Platform.MacOS:
        @staticmethod
        def output_frame_buffer(file: str = '', callback: Any = None, **kwargs):
            raise NotImplementedError

    else:
        @staticmethod
        def output_frame_buffer(file: str = '', callback: Any = None, **kwargs):
            return dearpygui.output_frame_buffer(file=file, callback=callback, **kwargs)


    __dpi_aware = False

    if Platform.get() != Platform.Windows:
        @classmethod
        def _toggle_dpi_awareness(cls):
            raise NotImplementedError

    else:
        @classmethod
        def _toggle_process_dpi_awareness(cls):
            if not cls.__dpi_aware:
                ctypes.windll.shcore.SetProcessDpiAwareness(2)
            else:
                ctypes.windll.shcore.SetProcessDpiAwareness(0)
            cls.__dpi_aware = not cls.__dpi_aware

        __dpi_aware = True

        ctypes.windll.shcore.SetProcessDpiAwareness(2)


    ###############################
    ########### END API ###########
    ###############################
    __slots__ = ()
    __itemtype_id__ = ItemIdType(AppItem.__cached__["app_uuid"], "Application")


    ################################
    ####### Work-In-Progress #######
    ################################

    # manual_callback_management: bool
    # load_init_file            : str
    # init_file                 : str
    # auto_save_init_file       : bool
    # allow_alias_overwrites    : bool
    # manual_alias_management   : bool
    # skip_required_args        : bool
    # skip_positional_args      : bool
    # skip_keyword_args         : bool

    # @classmethod
    # def get_callback_queue(cls) -> Any:
    #     """Clear and return the callbacks that were to be ran this frame.
    #     `manual_callback_management` must be set to True. Call only within
    #     the main render loop.
    #     """
    #     if not cls.manual_callback_management:
    #         raise RuntimeError("`manual_callback_management` must be True.")
    #     return dearpygui.get_callback_queue()

    # @classmethod
    # def run_callbacks(cls, callback_queue, *args, **kwargs) -> None:
    #     """Run all callbacks within the callback queue. `manual_callback_management`
    #     must be set to True. Call only within the main render loop.
    #     """
    #     if not cls.manual_callback_management:
    #         raise RuntimeError("`manual_callback_management` must be True.")
    #     return dearpygui.run_callbacks(callback_queue)

    # @classmethod
    # def run_callback_queue(cls, *args, **kwargs) -> None:
    #     """Retrieve all callbacks scheduled to be ran this frame, clear the
    #     queue, and run them. Does nothing if the callback queue is empty.
    #     `manual_callback_management` must be set to True. Call only within
    #     the main render loop.
    #     """
    #     callback_queue = cls.get_callback_queue()
    #     return cls.run_callbacks(callback_queue)

# Some Application classmethods use this as it's easier to get descriptor
# values from an instance.
_Application = Application()
_Application.theme = _DEFAULT_THEME
