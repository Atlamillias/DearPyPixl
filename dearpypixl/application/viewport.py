from typing import Callable, Union, Any, TYPE_CHECKING
import sys
import warnings

from dearpygui import _dearpygui
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

from dearpypixl.application import AppItemType, AppAttribute
from dearpypixl.constants import ViewportUUID
from dearpypixl.components import ItemT, item_attribute, UpdaterList, ProtoItem
from dearpypixl.containers import Window
from dearpypixl.item.configuration import CONFIGURATION, INFORMATION, STATE

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
        p_window = obj._AppItemsRegistry.get(obj._primary_window, None)
        if p_window is None:
            obj._primary_window = None  # possibly deleted
        return p_window

def _set_primary_window(obj, name, value):
    if not value and obj._primary_window:
        _dearpygui.set_primary_window(obj._primary_window, False)
        obj._primary_window = None
    elif not value:
        obj._primary_window = None
    else:
        obj._primary_window = int(value)
        _dearpygui.set_primary_window(obj._primary_window, True)

class _ResizeUpdaterList(UpdaterList):
    """Automatically re-sets the exit callback with the contents
    of `self` on creation, or update through list method calls.
    """
    @staticmethod
    def _on_update(callables):
        _dearpygui.set_viewport_resize_callback(lambda: [c() for c in callables])



class Viewport(ProtoItem, metaclass=AppItemType):
    # NOTE: This class is basically an inheritable module -- Methods defined are either classmethods or staticmethods.
    # While "configuration" attributes aren't technically defined as such, all `Viewport` instances will get and set from
    # the same pool of information. Trying to redefine a configuration attribute on `Viewport` or its decendants is not
    # possible, and will instead set the attribute on a fallback instance (to invoke `__set__` if it is a property).

    # Again, the metaclass prevents `CONFIGURATION`-related attributes from being redefined.
    # Any value that would be set is instead set on a fallback instance.
    title        : str  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    width        : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    height       : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    min_width    : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    min_height   : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    max_width    : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    max_height   : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    x_pos        : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    y_pos        : int  = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    resizable    : bool = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    vsync        : bool = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    always_on_top: bool = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    decorated    : bool = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)
    clear_color  : bool = AppAttribute(CONFIGURATION, _get_viewport_config, _set_viewport_config)

    small_icon       : str           = AppAttribute(CONFIGURATION,
                                                    lambda obj, name: get_viewport_configuration(ViewportUUID)["small_icon"],
                                                    _set_viewport_fickle_config)
    large_icon       : str           = AppAttribute(CONFIGURATION,
                                                    lambda obj, name: get_viewport_configuration(ViewportUUID)["large_icon"],
                                                    _set_viewport_fickle_config)
    primary_window   : Window | None = AppAttribute(CONFIGURATION,
                                                    _get_primary_window,
                                                    _set_primary_window)
    _primary_window  : int | None    = None


    ## Information properties ##
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def tag(cls) -> str:
        return ViewportUUID

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def client_width(cls) -> int:
        return _get_viewport_config(cls, "client_width")

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def client_height(cls) -> int:
        return _get_viewport_config(cls, "client_height")

    
    _calls_on_resize = _ResizeUpdaterList()

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def calls_on_resize(cls) -> list:
        return cls._calls_on_resize

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def active_window(cls):
        return cls._AppItemsRegistry.get(get_active_window(), None)

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def mouse_drag_delta(cls):
        return get_mouse_drag_delta()

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def local_mouse_pos(cls) -> list[float]:
        return get_mouse_pos()

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def global_mouse_pos(cls) -> list[float]:
        return get_mouse_pos(local=False)

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def drawing_mouse_pos(cls) -> list[float]:
        return get_drawing_mouse_pos()

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def plot_mouse_pos(cls) -> list[float]:
        return get_plot_mouse_pos()

    ## State properties ##
    @classmethod
    @property
    @item_attribute(category=STATE)
    def is_showing(cls) -> bool:
        return _dearpygui.is_viewport_ok()


    _is_maximized  = False
    _is_minimized  = False
    _is_fullscreen = False

    @classmethod
    @property
    @item_attribute(category=STATE)
    def is_maximized(cls) -> bool:
        return cls._is_maximized

    @classmethod
    @property
    @item_attribute(category=STATE)
    def is_minimized(cls) -> bool:
        return cls._is_minimized

    @classmethod
    @property
    @item_attribute(category=STATE)
    def is_fullscreen(cls) -> bool:
        return cls._is_fullscreen


    _is_using_primary_window = False

    @classmethod
    @property
    @item_attribute(category=STATE)
    def is_using_primary_window(cls) -> bool:
        return cls._is_using_primary_window

    ################################
    ######## Event Handling ########
    ################################
    def on_resize(cls, callback: Callable):
        cls._calls_on_resize.append(callback)
        return callback

    ################################
    ######## Misc. methods #########
    ################################
    @classmethod
    def configuration(cls) -> dict[str, Any]:
        config = get_viewport_configuration()  # The only change from `Item.configuration`
        item_config_attrs = cls._item_config_attrs
        return {attr:(config[attr] if attr in config else
                getattr(cls, attr)) for attr in item_config_attrs}

    @classmethod
    def information(cls) -> dict[str, Any]:
        return {attr: getattr(cls, attr) for attr in cls._item_inform_attrs}

    @classmethod
    def state(cls) -> dict[str, Any]:
        return {attr: getattr(cls, attr) for attr in cls._item_states_attrs}

    @classmethod
    def children(cls) -> tuple[ItemT, ...]:
        """Return a tuple of all items.
        """
        return tuple(cls._AppItemsRegistry.values())

    @classmethod
    def maximize(cls) -> None:
        """Maximizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()
        cls._is_maximized = True
        cls._is_minimized = False
        _dearpygui.maximize_viewport()

    @classmethod
    def minimize(cls) -> None:
        """Minimizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()
        cls._is_maximized = False
        cls._is_minimized = True
        _dearpygui.minimize_viewport()

    @classmethod
    def toggle_fullscreen(cls) -> None:
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


    @classmethod
    def get_mouse_global_pos(cls):
        get_mouse_pos(local=False)

    @classmethod
    def get_mouse_local_pos(cls):
        get_mouse_pos(local=True)

    @classmethod
    def get_mouse_plot_pos(cls):
        return get_plot_mouse_pos()

    @classmethod
    def get_mouse_drawing_pos(cls):
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

