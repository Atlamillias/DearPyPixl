from typing import Callable, Union, Any
import warnings
import sys
import os

# Many of these tend to be called between frames as render
# callbacks -- trying to avoid lookup overhead with these
# imports.
from dearpygui import _dearpygui
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
    # misc
    split_frame,
    set_frame_callback,
    # setters
    set_global_font_scale,
    configure_app,
)
from dearpypixl.application import AppItemType, AppAttribute
from dearpypixl.constants import AppUUID, ViewportUUID, Key
from dearpypixl.components import ItemT, item_attribute, Theme, UpdaterList, ProtoItem
from dearpypixl.item.configuration import CONFIGURATION, INFORMATION, STATE
if sys.platform == "win32":
    from dearpypixl.platforms import windows



def _get_app_config(obj, name):
    return get_app_configuration()[name]

def _set_app_config(obj, name, value):
    configure_app(**{name: value})
    if _dearpygui.is_viewport_ok():
        warnings.warn("`Application` configuration settings cannot be changed once the viewport is showing.")

# Slightly too complex for a lambda.
def _set_theme(obj, name, value):
    default_theme = ProtoItem._AppItemsRegistry.get(Theme._default_theme_uuid, None)
    if value is None and not default_theme:
        return None
    elif not value:
        return default_theme.unbind()
    value.bind()


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




class Application(ProtoItem, metaclass=AppItemType):
    # NOTE: This class is basically an inheritable module -- Methods defined are either classmethods or staticmethods.
    # While "configuration" attributes aren't technically defined as such, all `Application` instances will get and set from
    # the same pool of information. Trying to redefine a configuration attribute on `Application` or its decendants is not
    # possible, and will instead set the attribute on a fallback instance (to invoke `__set__` if it is a property).

    # Again, the metaclass prevents `CONFIGURATION`-related attributes from being redefined.
    # Any value that would be set is instead set on a fallback instance.

    # NOTE: DearPyPixl currently doesn't support the commented-out internal app configuration. 
    # load_init_file         : str  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # init_file              : str  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # auto_save_init_file    : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # allow_alias_overwrites : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # manual_alias_management: bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_required_args     : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_positional_args   : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    # skip_keyword_args      : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    auto_device   : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    docking       : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    docking_space : bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    device        : int  = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config
    wait_for_input: bool = AppAttribute(CONFIGURATION, _get_app_config, _set_app_config)  # internal app config

    font_scale    : float        = AppAttribute(CONFIGURATION,
                                                lambda obj, name: get_global_font_scale(),
                                                lambda obj, name, value: set_global_font_scale(value))
    theme         : Theme | None = AppAttribute(CONFIGURATION,
                                                lambda obj, name: obj._AppItemsRegistry.get(Theme._default_theme_uuid, None),
                                                _set_theme)


    ## Information properties ##
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def tag(cls) -> int:
        return AppUUID

    _calls_on_startup = _StartupUpdaterList()
    _calls_on_exit    = _ExitUpdaterList()
    _calls_on_render = []

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def calls_on_startup(cls) -> list[Callable]:
        return cls._calls_on_startup

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def calls_on_exit(cls) -> list[Callable]:
        return cls._calls_on_exit

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def calls_on_render(cls) -> list[Callable]:
        return cls._calls_on_render

    @classmethod
    @property
    @item_attribute(category="information")
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
    @item_attribute(category="information")
    def process_id(cls) -> str:
        """Return the current process identifier.
        """
        return os.getpid()

    @classmethod
    @property
    @item_attribute(category="information")
    def version(cls) -> str:
        """Return the version of Dearpygui that is being used.
        """
        return _dearpygui.get_app_configuration()["version"]

    @classmethod
    @property
    @item_attribute(category="information")
    def platform(cls) -> str:
        """Return the platform.
        """
        return _dearpygui.get_app_configuration()["platform"]

    @classmethod
    @property
    @item_attribute(category="information")
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
        # Show viewport if it is not shown already.
        if not _dearpygui.is_viewport_ok():
            _dearpygui.show_viewport()
        # Avoiding lookup overhead in the loop as it is the most "sensitive"
        # spot in the entire framework.
        is_running = cls.is_running
        render_frame = cls.render_frame  

        # NOTE: This is the render loop.
        while is_running():
            render_frame()
        cls.end()

    @classmethod
    def stop(cls) -> None:
        """Break the main render loop and stop the application
        if it is running. This is the equivelent to pressing the
        "close"/"exit" button on the application title bar.
        """
        if cls.is_running():
            stop_dearpygui()

    @classmethod
    def end(cls) -> None:
        """Post-process clean-up. Must be called following the render
        loop to ensure proper 'cleanup'.
        """
        _dearpygui.destroy_context()

    @classmethod
    def render_frame(cls) -> None:
        """Renders a frame. Only for use in the main render loop (see the
        `start` method).
        """
        for render_callable in cls._calls_on_render:
            render_callable()
        render_dearpygui_frame()

    ################################
    ######## Event Handling ########
    ################################
    @classmethod
    def on_startup(cls, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will run within the first
        few frames.
        """
        cls._calls_on_startup.append(callback)
        return callback

    @classmethod
    def on_render(cls, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will after a frame is rendered.
        """
        cls._calls_on_render.append(callback)
        return callback

    @classmethod
    def on_exit(cls, callback: Callable) -> Callable:
        """Adds *callback* to a list of callables that will run on the last frame.
        """
        cls._calls_on_exit.append(callback)
        return callback

    @classmethod
    def on_frame(cls, frame: int, callback: Callable = None) -> Callable:
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
    @classmethod
    def configuration(cls) -> dict[str, Any]:
        config = get_app_configuration()  # The only change from `Item.configuration`
        item_config_attrs = cls._item_config_attrs
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def information(cls) -> dict[str, Any]:
        return {attr: getattr(cls, attr) for attr in cls._item_inform_attrs}

    @classmethod
    def state(cls) -> dict[str, Any]:
        return {attr: getattr(cls, attr) for attr in cls._item_states_attrs}

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

    @property
    def _dpi_aware(cls):
        return cls.__is_dpi_aware

    if sys.platform == "win32":
        __is_dpi_aware = False
        windows.toggle_process_dpi_scaling()

        @_dpi_aware.setter
        def _dpi_aware(cls, value: bool):
            # Process DPI awareness can only be set prior to showing the app/viewport window.
            if _dearpygui.is_viewport_ok():
                warnings.warn("`Application` configuration settings cannot be changed once the viewport is showing.")
            elif cls.__is_dpi_aware is not value:
                windows.toggle_process_dpi_scaling()
                cls.__is_dpi_aware = not cls.__is_dpi_aware

    _dpi_aware = classmethod(_dpi_aware)



