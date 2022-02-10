from typing import Callable, Union, Any
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
    # misc
    split_frame,
    set_frame_callback,
    # setters
    set_global_font_scale,
    configure_app,
)
from dearpypixl.application import AppItem, AppAttribute
from dearpypixl.constants import AppUUID, ViewportUUID, Key
from dearpypixl.components import Item, item_attribute, Theme, ProtoItem
from dearpypixl.components.configuration import CONFIGURATION, INFORMATION, STATE
if sys.platform == "win32":
    from dearpypixl.platforms import windows



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
                                                lambda obj, name: obj._AppItemsRegistry.get(Theme._default_theme_uuid, None),
                                                _set_theme)


    ## Information properties ##
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def tag(cls) -> int:
        return AppUUID

    _calls_on_startup = []
    _calls_on_exit    = []
    _calls_on_render  = []

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
        is_running   = cls.is_running
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
        for call_able, kwargs in cls._calls_on_render:
            call_able(cls, None, **kwargs)
        render_dearpygui_frame()

    ################################
    ######## Event Handling ########
    ################################
    @classmethod
    def on_startup(cls, _callback: Callable = None, **kwargs) -> Callable:
        """Adds *callback* to a list of callables that will run after the first
        frame is rendered.

        Args:
            * kwargs (optional, keyword-only): Keyword arguments to pass to the callback.
        """
        def _on_startup(callback):
            if not callable(callback):
                raise TypeError(f"{callback!r} is not callable.")
            cls._calls_on_startup.append((callback, kwargs))
            return callback

        if not _callback:
            return _on_startup
        return _on_startup(_callback)

    @classmethod
    def on_exit(cls, _callback: Callable = None, **kwargs) -> Callable:
        """Adds *callback* to a list of callables that will run on the last frame.

        Args:
            * kwargs (optional, keyword-only): Keyword arguments to pass to the callback.
        """
        def _on_exit(callback):
            if not callable(callback):
                raise TypeError(f"{callback!r} is not callable.")
            cls._calls_on_exit.append((callback, kwargs))
            return callback

        if not _callback:
            return _on_exit
        return _on_exit(_callback)

    def _on_event_callback(sender, app_data, user_data):  # user_data = list of callables
        # TODO: Pass `cls` instead of explicitly passing `Application`
        for call_able, kwargs in user_data:
            call_able(Application, app_data, **kwargs)

    dearpygui.set_frame_callback(1, _on_event_callback, user_data=_calls_on_startup)
    dearpygui.set_exit_callback(_on_event_callback, user_data=_calls_on_exit)


    @classmethod
    def on_render(cls, _callback: Callable = None, **kwargs) -> Callable:
        """Adds *callback* to a list of callables that will run after a frame is rendered.

        Args:
            * kwargs (optional, keyword-only): Keyword arguments to pass to the callback.    
        """
        def _on_render(callback):
            if not callable(callback):
                raise TypeError(f"{callback!r} is not callable.")
            # NOTE: `render_frame` method calls these before rendering a frame.
            cls._calls_on_render.append((callback, kwargs))
            return callback

        if not _callback:
            return _on_render
        return _on_render(_callback)

    @classmethod
    def on_frame(cls, _frame: int, _callback: Callable = None, **kwargs) -> Callable:
        """Schedule a callback to run on frame *frame*.
        """
        # Keeping track of all callables to run per frame would be slow -- this is
        # already done by dearpygui.
        def _on_frame(callback):
            # callback is wrapped to pass unpacked user_data (kwargs)
            set_frame_callback(_frame, 
                               lambda sender, app_data, user_data: \
                                   callback(sender, app_data, **user_data),
                               user_data=kwargs)
            return callback

        if _callback:
            return _on_frame(_callback)
        return _on_frame
        

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
    def run_callbacks(cls, callback_queue) -> None:
        """Run all callbacks within the callback queue. `manual_callback_management`
        must be set to True. Call only within the main render loop.
        """
        if not cls.manual_callback_management:
            raise RuntimeError("`manual_callback_management` must be True.")
        return dearpygui.run_callbacks(callback_queue)

    @classmethod
    def run_callback_queue(cls) -> None:
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
        item_config_attrs = cls._item_config_attrs
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def state(cls) -> dict[str, Any]:
        states = {attr: getattr(cls, attr) for attr in cls._item_states_attrs}
        return states | {"is_running": cls.is_running()}

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

