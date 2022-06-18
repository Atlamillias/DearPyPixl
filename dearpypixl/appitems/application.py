from typing import Callable, Any
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
from dearpypixl.appitems import AppItem, AppAttribute
from dearpypixl.itemtypes.events import FrameEvents
from dearpypixl.constants import AppUUID, Platform, Key
from dearpypixl.itemtypes import CONFIG, INFORM, STATES, Item, ItemProperty, Theme, ItemType
from dearpypixl.itemtypes.themes.presets import _theme_presets, dearpygui_internal

if dearpygui.get_platform() == Platform.Windows:
    import ctypes

    _dpi_aware: bool = False

    def toggle_process_dpi_awareness():
        global _dpi_aware

        if _dpi_aware:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        else:
            ctypes.windll.shcore.SetProcessDpiAwareness(0)
        _dpi_aware = not _dpi_aware


_appitem_registry = Item.__registry__[0]



def _get_app_config(obj, name):
    return get_app_configuration()[name]

def _set_app_config(obj, name, value):
    configure_app(**{name: value})
    if _dearpygui.is_viewport_ok():
        warnings.warn(f"`Application` configuration {name!r} cannot be changed once the viewport is showing.")

def _set_theme(obj, name, value):  # too complex as a lambda.
    default_theme = ItemType.__registry__[0].get(Theme._default_theme_uuid, None)
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
    auto_device               : bool = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config
    docking                   : bool = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config
    docking_space             : bool = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config
    device                    : int  = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config
    wait_for_input            : bool = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config
    manual_callback_management: bool = AppAttribute(CONFIG, _get_app_config, _set_app_config)  # internal app config

    font_scale    : float        = AppAttribute(CONFIG,
                                                lambda obj, name: get_global_font_scale(),
                                                lambda obj, name, value: set_global_font_scale(value))
    theme         : Theme | None = AppAttribute(CONFIG,
                                                lambda obj, name: _appitem_registry.get(Theme._default_theme_uuid, None),
                                                _set_theme)


    ## Information properties ##
    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def tag(cls) -> int:
        return AppUUID

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
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
    def platform(cls) -> str:
        """Return the platform.
        """
        return _dearpygui.get_app_configuration()["platform"]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
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
    def configuration(cls) -> dict[str, Any]:
        config = get_app_configuration()  # The only change from `Item.configuration`
        item_config_attrs = cls.__internal__[0]
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def state(cls) -> dict[str, Any]:
        states = {attr: getattr(cls, attr) for attr in cls.__internal__[2]}
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


    if dearpygui.get_platform() == Platform.MacOS:
        @staticmethod
        def output_frame_buffer(callback: Callable = None, file: str = '', **kwargs):
            raise NotImplementedError(f"MacOS")




Application.theme = dearpygui_internal
