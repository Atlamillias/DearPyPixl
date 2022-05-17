from typing import Callable, Union, Any, Sequence, SupportsIndex
from typing_extensions import Self
import functools
import warnings
import sys
import os

# Many of these tend to be called between frames as render
# callbacks -- trying to avoid lookup overhead with these
# imports.
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
from dearpypixl.application import AppItem, AppAttribute
from dearpypixl.application.frameevents import FrameEvents
from dearpypixl.constants import AppUUID, Platform, Key
from dearpypixl.components import Item, item_attribute, Theme, ProtoItem
from dearpypixl.components.configuration import CONFIGURATION, INFORMATION, STATE
from dearpypixl.themes import _theme_presets, dearpygui_internal

if sys.platform == "win32":
    from dearpypixl.platforms import windows


_appitem_registry = Item._AppItemsRegistry




def _get_app_config(obj, name):
    return get_app_configuration()[name]

def _set_app_config(obj, name, value):
    configure_app(**{name: value})
    if _dearpygui.is_viewport_ok():
        warnings.warn(f"`Application` configuration {name!r} cannot be changed once the viewport is showing.")

def _set_theme(obj, name, value):  # too complex as a lambda.
    default_theme = ProtoItem._AppItemsRegistry.get(Theme._default_theme_uuid, None)
    if value is None and not default_theme:
        return None
    elif not value:
        return default_theme.unbind()
    value.bind()




class Application(AppItem):
    # NOTE: This class is basically an inheritable module -- Methods defined are either classmethods or staticmethods.
    # While "configuration" attributes aren't technically defined as such, all `Application` instances will get and set from
    # the same pool of information. Trying to redefine a configuration attribute on `Application` or its decendants is not
    # possible, and will instead set the attribute on a fallback instance (to invoke `__set__` if it is a property).

    #### DearPyPixl currently doesn't support the commented-out internal app configuration. 
    # load_init_file         : str  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # init_file              : str  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # auto_save_init_file    : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # allow_alias_overwrites : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # manual_alias_management: bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_required_args     : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_positional_args   : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_keyword_args      : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    auto_device               : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    docking                   : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    docking_space             : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    device                    : int  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    wait_for_input            : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    manual_callback_management: bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config

    font_scale    : float        = AppAttribute(CONFIGURATION,
                                                lambda obj, name: get_global_font_scale(),
                                                lambda obj, name, value: set_global_font_scale(value))
    theme         : Theme | None = AppAttribute(CONFIGURATION,
                                                lambda obj, name: _appitem_registry.get(Theme._default_theme_uuid, None),
                                                _set_theme)


    ## Information properties ##
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def tag(cls) -> int:
        return AppUUID

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def device_manager(cls) -> str:
        """Return the current controller of the display adapter used for the
        application.
        
        Possible returns:
            * system: The display adapter has been set by your operating
            system.
            * internal: The display adapter has been set by DearPyGui.
            * manual: The display adapter has been manually selected.
        """
        device = cls.device
        auto_device = cls.auto_device
        if device != -1:
            return "manual"
        elif not auto_device:
            return "system"
        return "internal"

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def process_id(cls) -> str:
        """Return the current process identifier.
        """
        return os.getpid()

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def version(cls) -> str:
        """Return the version of Dearpygui that is being used.
        """
        return _dearpygui.get_app_configuration()["version"]

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def platform(cls) -> str:
        """Return the platform.
        """
        return _dearpygui.get_app_configuration()["platform"]

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def device_name(cls) -> str:
        """Return the name of the display adapter in use.
        """
        return _dearpygui.get_app_configuration()["device_name"]

    ################################
    ######### Render loop ##########
    ################################
    @classmethod
    def start(cls) -> None:
        """Start the application by executing the main render loop.
        """
        # Viewport.show()
        if not _dearpygui.is_viewport_ok():
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

    @classmethod
    def end(cls, *args, **kwargs) -> None:
        """Post-process clean-up. Must be called following the render
        loop to ensure proper 'cleanup'.
        """
        _dearpygui.destroy_context()

    @classmethod
    def render_frame(cls) -> None:
        """Renders a frame. Only for use in the main render loop (see the `start` method).
        """
        render_dearpygui_frame()

    ################################
    ######## Event Handling ########
    ################################
    _frame_events = FrameEvents()

    @classmethod
    @property
    def frame_events(cls) -> FrameEvents:
        return cls._frame_events

    on_frame = classmethod(_frame_events.on_frame)


    # Callback debugging
    @classmethod
    def get_callback_queue(cls) -> Any:
        """Clear and return the callbacks that were to be ran this frame.
        `manual_callback_management` must be set to True. Call only within
        the main render loop.
        """
        if not cls.manual_callback_management:
            raise RuntimeError("`manual_callback_management` must be True.")
        return dearpygui.get_callback_queue()

    @classmethod
    def run_callbacks(cls, callback_queue, *args, **kwargs) -> None:
        """Run all callbacks within the callback queue. `manual_callback_management`
        must be set to True. Call only within the main render loop.
        """
        if not cls.manual_callback_management:
            raise RuntimeError("`manual_callback_management` must be True.")
        return dearpygui.run_callbacks(callback_queue)

    @classmethod
    def run_callback_queue(cls, *args, **kwargs) -> None:
        """Retrieve all callbacks scheduled to be ran this frame, clear the
        queue, and run them. Does nothing if the callback queue is empty.
        `manual_callback_management` must be set to True. Call only within
        the main render loop.
        """
        callback_queue = cls.get_callback_queue()
        return cls.run_callbacks(callback_queue)


    ################################
    ######## Misc. methods #########
    ################################
    @classmethod
    def _export_configuration(cls) -> dict:
        ...
        
    @classmethod
    def configuration(cls) -> dict[str, Any]:
        config = get_app_configuration()  # The only change from `Item.configuration`
        item_config_attrs = cls._item_config_attrs
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def state(cls) -> dict[str, Any]:
        states = {attr: getattr(cls, attr) for attr in cls._item_states_attrs}
        return states | {"is_running": cls.is_running()}

    @classmethod
    def theme_presets(cls) -> tuple[Theme, ...]:
        """Return the available pre-made themes.
        """
        return _theme_presets

    @staticmethod
    def output_frame_buffer(file: str = '', callback: Any = None, **kwargs):
        return dearpygui.output_frame_buffer(file=file, callback=callback, **kwargs)

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
    def is_key_pressed(key: Union[Key, int]) -> bool:
        """Return True if `key` is pressed, otherwise return False.

        Args:
            * key (Union[Key, Mouse, int]): Union[Key, int] event code to inquire
            about.
        """
        return is_key_pressed(int(key))

    @staticmethod
    def is_key_released(key: Union[Key, int]) -> bool:
        """Return True if `key` is released, otherwise return False.

        Args:
            * key (Union[Key, Mouse, int]): Union[Key, int] event code to inquire
            about.
        """
        return is_key_released(int(key))

    @staticmethod
    def is_key_down(key: Union[Key, int]) -> bool:
        """Return True if `key` is down, otherwise return False.

        Args:
            * key (Union[Key, Mouse, int]): Union[Key, int] event code to inquire
            about.
        """
        return is_key_down(int(key))


    __is_dpi_aware = True

    # NOTE: This does not actually set properly on the class as it is not included
    # as "configuration".
    @property
    def _dpi_aware(cls):
        return cls.__is_dpi_aware

    if sys.platform == "win32":
        __is_dpi_aware = False
        windows.toggle_process_dpi_awareness()

        @_dpi_aware.setter
        def _dpi_aware(cls, value: bool):
            # Process DPI awareness can only be set prior to showing the app/viewport window.
            if _dearpygui.is_viewport_ok():
                warnings.warn(f"`Application` configuration `_dpi_aware` cannot be changed once the viewport is showing.")
            elif cls.__is_dpi_aware is not value:
                windows.toggle_process_dpi_awareness()
                cls.__is_dpi_aware = not cls.__is_dpi_aware

    _dpi_aware = classmethod(_dpi_aware)

    if dearpygui.get_platform() == Platform.MacOS:
        @staticmethod
        def output_frame_buffer(callback: Callable = None, file: str = '', **kwargs):
            raise NotImplementedError(f"MacOS")

    # Gimmicky WIP crap
    _fps60  = 0.0167
    _fps90  = 0.0111
    _fps120 = 0.0083
    _fps240 = 0.0041

    @classmethod
    def _start(cls, ms_per_update) -> None:
        """(Expiremental) Main render loop that updates in real-time.
        """
        if not _dearpygui.is_viewport_ok():
            _dearpygui.show_viewport()

        previous_time = get_total_time()
        lag           = 0.0
        events        = cls.frame_events()
        while cls.is_running():
            current_time  = get_total_time()
            elapsed_time  = current_time - previous_time
            previous_time = current_time
            lag += elapsed_time
            while lag >= ms_per_update:
                next(events)
                lag -= ms_per_update
            print("break")
            render_dearpygui_frame()
        cls.end()


Application.theme = dearpygui_internal
