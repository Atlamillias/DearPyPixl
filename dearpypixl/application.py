from __future__ import annotations
from typing import Callable, Any, TYPE_CHECKING
from typing_extensions import Self
from enum import IntEnum, Enum
import logging
import os
import ctypes
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
    # container stack
    pop_container_stack,
    top_container_stack,
    empty_container_stack,
    # misc
    split_frame,
    get_text_size,
)
from ._internal import registry
from ._internal.errors import err_viewport_showing
from ._internal.constants import APP_UUID, NULL_THEME_UUID, NULL_FONT_UUID
from ._internal.utilities import classproperty
from ._internal.item import (
    ItemData,
    ItemType,
    AppItem,
)

if TYPE_CHECKING:
    from .theme import Theme
    from .events import FrameEvents, Key
    from .font import Font, FontFamily

logging.info("")

__all__ = [
    "Platform",
    "DPIAwareness",
    "DeviceManager",
    "Application",
]



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


class AppStateKey(str, Enum):
    THEME_UUID    = "theme_uuid"
    FONT_UUID     = "font_uuid"
    DEFAULT_THEME = "default_theme"
    DEFAULT_FONT  = "default_font"
    FRAME_EVENTS  = "frame_events"


def _get_app_config(obj, name):
    return get_app_configuration()[name]


def _set_app_config(obj, name, value):
    if _dearpygui.is_viewport_ok():
        raise err_viewport_showing(name)
    configure_app(**{name: value})


class Application(AppItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(identity=(APP_UUID, "Application"))
    __itemdict__   = {
        AppStateKey.THEME_UUID   : NULL_THEME_UUID,
        AppStateKey.FONT_UUID    : NULL_THEME_UUID ,
        AppStateKey.DEFAULT_THEME: ...,
        AppStateKey.DEFAULT_FONT : ...,
        AppStateKey.FRAME_EVENTS : ...,
    }
    __NULL = object()

    registry = registry

    auto_device        : bool = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    docking            : bool = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    docking_space      : bool = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    device             : int  = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    wait_for_input     : bool = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    load_init_file     : str  = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    init_file          : str  = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)
    auto_save_init_file: bool = __dearpypixl__.set_configuration(_get_app_config, _set_app_config)

    @property
    @__dearpypixl__.as_configuration
    def font_scale(self) -> float:
        return get_global_font_scale()
    @font_scale.setter
    def font_scale(self, value: float) -> None:
        set_global_font_scale()

    @property
    @__dearpypixl__.as_configuration
    def theme(self) -> Theme:
        theme_uuid = self.__itemdict__[AppStateKey.THEME_UUID]
        if not theme_uuid:
            default_theme = self.__itemdict__[AppStateKey.DEFAULT_THEME]
            self.theme = default_theme
            return default_theme
        return registry.get_item(theme_uuid)
    @theme.setter
    def theme(self, value: Theme) -> None:
        if not value:
            value = self.__itemdict__[AppStateKey.DEFAULT_THEME]
        value.bind()

    @property
    @__dearpypixl__.as_configuration
    def font(self) -> Font:
        font_uuid = self.__itemdict__[AppStateKey.FONT_UUID]
        if not font_uuid:
            default_theme = self.__itemdict__[AppStateKey.DEFAULT_FONT]
            self.theme = default_theme
            return default_theme
        return registry.get_item(font_uuid)
    @font.setter
    def font(self, value: Font | None) -> None:
        if not value:
            value = self.__itemdict__[AppStateKey.DEFAULT_FONT]
        value.bind()


    #### Information Properties ####
    @classproperty
    @__dearpypixl__.as_information
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

    @classproperty
    @__dearpypixl__.as_information
    def process_id(cls) -> str:
        """Return the current process identifier.
        """
        return os.getpid()

    @classproperty
    @__dearpypixl__.as_information
    def version(cls) -> str:
        """Return the version of Dearpygui that is being used.
        """
        return _dearpygui.get_app_configuration()["version"]

    @classproperty
    @__dearpypixl__.as_information
    def platform(cls) -> Platform:
        """Return the platform.
        """
        return Platform.get()

    @classproperty
    @__dearpypixl__.as_information
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
    def start(cls, cleanup_on_exit: bool = True) -> None:
        """Start the application by executing the main render loop.

        Args:
            * cleanup_on_exit (bool): If True, the `end` method will be invoked
            once the application is terminated. Defaults to True.
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
        if cleanup_on_exit:
            cls.end()

    @classmethod
    def stop(cls) -> None:
        """Break the main render loop and stop the application if it is running.
        This is equivelent to closing the application using the title bar button.
        """
        if cls.is_running():
            stop_dearpygui()

    @staticmethod
    def end() -> None:
        """Post-process clean-up. Releases resources used by DearPyGui.
        """
        _dearpygui.destroy_context()


    ################################
    ######## Event Handling ########
    ################################

    @classproperty
    def frame_events(cls) -> FrameEvents:
        return cls.__itemdict__[AppStateKey.FRAME_EVENTS]

    @classmethod
    def on_frame(cls, callback: Callable = None, /, *, frame: int = 0, user_data: Any = None, **kwargs):
        """(Decorator) Schedules a callback to run on a specific frame.

        Args:
            * callback (Callable): Callable object to run.
            * frame (int, optional): The callback will run before this frame
            is rendered. If this value is 0, it will run every frame. If -1,
            it will run on the last frame (application exit). Defaults to 0.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            argument to <callback>. Defaults to None.
        """
        return cls.frame_events.on_frame(
            callback,
            frame=frame,
            user_data=user_data,
            **kwargs
        )

    ################################
    ####### Container Stack ########
    ################################

    @classmethod
    def pop_container_stack(cls):
        top_item = cls.top_container_stack()
        if top_item:
            pop_container_stack()
        return top_item

    @classmethod
    def top_container_stack(cls) -> ItemType | None:
        return cls.registry.get_item(top_container_stack(), None)

    @classmethod
    def empty_container_stack(cls):
        return empty_container_stack()


    ################################
    ######## Other Methods #########
    ################################
    @classmethod
    def state(cls) -> dict[str, Any]:
        return super().state() | {"is_running": cls.is_running()}

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
        def output_frame_buffer(file: str = '', callback: Any = None, **kwargs): ...

    else:
        @staticmethod
        def output_frame_buffer(file: str = '', callback: Any = None, **kwargs):
            return dearpygui.output_frame_buffer(file=file, callback=callback, **kwargs)


    __dpi_aware = False

    if Platform.get() != Platform.Windows:
        @classmethod
        def _toggle_dpi_awareness(cls): ...

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


    ################################
    ####### Work-In-Progress #######
    ################################

    # manual_callback_management: bool
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
