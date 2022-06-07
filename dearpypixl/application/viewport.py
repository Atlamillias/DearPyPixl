from typing import Callable, Union, Any, TYPE_CHECKING
import sys
import warnings

from dearpygui import _dearpygui, dearpygui
from dearpygui._dearpygui import (
    # getters
    get_mouse_drag_delta,
    get_drawing_mouse_pos,
    get_plot_mouse_pos,
    get_mouse_pos,
    get_active_window,
    get_viewport_configuration,
    # setters
    configure_viewport
)

from dearpypixl.application import AppItem, AppAttribute
from dearpypixl.constants import ViewportUUID
from dearpypixl.components import CONFIG, INFORM, STATES, ItemT, ItemAttribute
from dearpypixl.containers import Window

if sys.platform == "win32":
    from dearpypixl.platforms import windows




def _get_viewport_config(__o, __name):
    return get_viewport_configuration(__o.tag)[__name]

def _set_viewport_config(__obj, __name, value):
    configure_viewport(__obj.tag, **{__name: value})

def _set_viewport_fickle_config(obj, name, value):
    if obj.is_showing:
        warnings.warn(f"`Viewport` configuration {name!r} cannot be changed once the viewport is showing.")
    else:
        configure_viewport(obj.tag, **{name: value})

def _get_primary_window(obj, name):
        p_window = obj.__registry__[0].get(Viewport._primary_window, None)
        if p_window is None:
            Viewport._primary_window = None  # possibly deleted
        return p_window

def _set_primary_window(obj, name, value):
    if not value and Viewport._primary_window:
        _dearpygui.set_primary_window(Viewport._primary_window, False)
        Viewport._primary_window = None
    elif not value:
        Viewport._primary_window = None
    else:
        Viewport._primary_window = int(value)
        _dearpygui.set_primary_window(Viewport._primary_window, True)



class Viewport(AppItem):
    # NOTE: This class is basically an inheritable module -- Methods defined are either classmethods or staticmethods.
    # While "configuration" attributes aren't technically defined as such, all `Viewport` instances will get and set from
    # the same pool of information. Trying to redefine a configuration attribute on `Viewport` or its decendants is not
    # possible, and will instead set the attribute on a fallback instance (to invoke `__set__` if it is a property).

    # Again, the metaclass prevents `CONFIGURATION`-related attributes from being redefined.
    # Any value that would be set is instead set on a fallback instance.
    title        : str  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    width        : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    height       : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    min_width    : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    min_height   : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    max_width    : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    max_height   : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    x_pos        : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    y_pos        : int  = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    resizable    : bool = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    vsync        : bool = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    always_on_top: bool = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    decorated    : bool = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)
    clear_color  : bool = AppAttribute(CONFIG, _get_viewport_config, _set_viewport_config)

    small_icon       : str           = AppAttribute(CONFIG,
                                                    lambda obj, name: get_viewport_configuration(ViewportUUID)["small_icon"],
                                                    _set_viewport_fickle_config)
    large_icon       : str           = AppAttribute(CONFIG,
                                                    lambda obj, name: get_viewport_configuration(ViewportUUID)["large_icon"],
                                                    _set_viewport_fickle_config)
    primary_window   : Window | None = AppAttribute(CONFIG,
                                                    _get_primary_window,
                                                    _set_primary_window)
    _primary_window  : int | None    = None


    ## Information properties ##
    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def tag(cls) -> str:
        return ViewportUUID

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def client_width(cls) -> int:
        return _get_viewport_config(cls, "client_width")

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def client_height(cls) -> int:
        return _get_viewport_config(cls, "client_height")


    _calls_on_resize = []

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def calls_on_resize(cls) -> list[tuple[Callable, dict[str, Any]]]:
        return cls._calls_on_resize

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def active_window(cls):
        return cls.__registry__[0].get(get_active_window(), None)

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def mouse_drag_delta(cls):
        return get_mouse_drag_delta()

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def local_mouse_pos(cls) -> list[float]:
        return get_mouse_pos()

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def global_mouse_pos(cls) -> list[float]:
        return get_mouse_pos(local=False)

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def drawing_mouse_pos(cls) -> list[float]:
        return get_drawing_mouse_pos()

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def plot_mouse_pos(cls) -> list[float]:
        return get_plot_mouse_pos()

    ## State properties ##
    @classmethod
    @property
    @ItemAttribute.register_member(category=STATES)
    def is_showing(cls) -> bool:
        return _dearpygui.is_viewport_ok()


    _is_maximized  = False
    _is_minimized  = False
    _is_fullscreen = False

    @classmethod
    @property
    @ItemAttribute.register_member(category=STATES)
    def is_maximized(cls) -> bool:
        return cls._is_maximized

    @classmethod
    @property
    @ItemAttribute.register_member(category=STATES)
    def is_minimized(cls) -> bool:
        return cls._is_minimized

    @classmethod
    @property
    @ItemAttribute.register_member(category=STATES)
    def is_fullscreen(cls) -> bool:
        return cls._is_fullscreen

    ################################
    ######## Event Handling ########
    ################################
    @classmethod
    def on_resize(cls, _callback: Callable = None, **kwargs):
        def _on_resize(callback):
            if not callable(callback):
                raise TypeError(f"{callback!r} is not callable.")
            cls._calls_on_resize.append((callback, kwargs))
            return callback

        if not _callback:
            return _on_resize
        return _on_resize(_callback)

    def _on_event_callback(sender, app_data, user_data):  # user_data = list of callables
        for call_able, kwargs in user_data:
            call_able(sender, app_data, **kwargs)

    dearpygui.set_viewport_resize_callback(_on_event_callback, user_data=_calls_on_resize)

    ################################
    ######## Misc. methods #########
    ################################
    @classmethod
    def configuration(cls) -> dict[str, Any]:
        config = get_viewport_configuration()  # The only change from `Item.configuration`
        item_config_attrs = cls.__internal__[0]
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def children(cls) -> tuple[ItemT, ...]:
        """Return a tuple of all items.
        """
        return tuple(cls.__registry__[0].values())

    _restore_width  = None
    _restore_height = None
    _restore_pos    = None

    @classmethod
    def _save_restore_states(cls, *args, **kwargs) -> None:
        cls._restore_width  = cls.width
        cls._restore_height = cls.height
        cls._restore_pos    = cls.x_pos, cls.y_pos

    @classmethod
    def maximize(cls, *args, **kwargs) -> None:
        """Maximizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        if not cls._is_maximized and not cls._is_maximized:
            cls._save_restore_states()

        cls._is_maximized = True
        cls._is_minimized = False
        _dearpygui.maximize_viewport()

    @classmethod
    def minimize(cls, *args, **kwargs) -> None:
        """Minimizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        if not cls.is_maximized and not cls.is_maximized:
            cls._save_restore_states

        cls._is_maximized = False
        cls._is_minimized = True
        _dearpygui.minimize_viewport()
    
    @classmethod
    def restore_down(cls, *args, **kwargs) -> None:
        """Restores the viewport to its previous non-maximized, non-
        minimized size and position.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        width    = cls._restore_width
        height   = cls._restore_height
        position = cls._restore_pos

        if width and height and position:
            cls.configure(width=width, height=height, x_pos=position[0], y_pos=position[1])
            cls._restore_width  = None
            cls._restore_height = None
            cls._restore_pos    = None


    @classmethod
    def toggle_fullscreen(cls, *args, **kwargs) -> None:
        cls._is_maximized  = False
        cls._is_minimized  = False
        cls._is_fullscreen = not cls._is_fullscreen
        _dearpygui.toggle_viewport_fullscreen()

    @classmethod
    def show(cls) -> None:
        """Begin rendering the viewport. Application and some viewport configurations
        will no longer be editable.
        """
        if not cls.is_showing:
            _dearpygui.show_viewport()


    @staticmethod
    def get_mouse_global_pos():
        get_mouse_pos(local=False)

    @staticmethod
    def get_mouse_local_pos():
        get_mouse_pos(local=True)

    @staticmethod
    def get_mouse_plot_pos():
        return get_plot_mouse_pos()

    @staticmethod
    def get_mouse_drawing_pos():
        return get_drawing_mouse_pos()


    if sys.platform == "win32":
        @classmethod
        def _toggle_overlay(cls) -> None:
            if cls.is_showing:
                windows.toggle_dpg_viewport_transparency()
                cls._is_minimized  = False
                cls._is_maximized  = True
                cls._is_fullscreen = False
            else:
                warnings.warn(f"`Viewport` configuration `_toggle_overlay_mode` cannot be changed unless the viewport is showing.")

