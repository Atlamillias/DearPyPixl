from __future__ import annotations
from typing import Callable, Any, TYPE_CHECKING
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
from .events import FrameEvents, Callback
from .itemtypes import (
    ItemData,
    AppItem,
)
from ._internal import registry
from ._internal.errors import err_viewport_showing
from ._internal.constants import VP_UUID
from ._internal.utilities import classproperty


if TYPE_CHECKING:
    from dearpypixl.containers import Window


__all__ = ["Viewport"]




_RESIZE_EVENTS = FrameEvents()


def _run_resize_events():
    for event in _RESIZE_EVENTS[0]:
        event()

dearpygui.set_viewport_resize_callback(_run_resize_events)




def _get_viewport_config(__o, __name):
    return get_viewport_configuration(__o.tag)[__name]

def _set_viewport_config(__obj, __name, value):
    configure_viewport(__obj.tag, **{__name: value})

def _set_viewport_fickle_config(obj, name, value):
    if _dearpygui.is_viewport_ok():
        raise err_viewport_showing(name)
    configure_viewport(obj.tag, **{name: value})


class Viewport(AppItem):
    __dearpypixl__ = ItemData(identity=(VP_UUID, "Viewport"))

    title        : str  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    width        : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    height       : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    min_width    : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    min_height   : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    max_width    : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    max_height   : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    x_pos        : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    y_pos        : int  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    resizable    : bool = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    vsync        : bool = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    always_on_top: bool = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    decorated    : bool = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    clear_color  : bool = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_config)
    small_icon   : str  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_fickle_config)
    large_icon   : str  = __dearpypixl__.set_configuration(_get_viewport_config, _set_viewport_fickle_config)


    __primary_window_uuid = None

    @property
    @__dearpypixl__.as_configuration
    def primary_window(self) -> Window:
        p_window = registry.get_item(self.__primary_window_uuid, None)
        if not p_window:
            self.__primary_window_uuid = None  # possibly deleted
        return p_window
    @primary_window.setter
    def primary_window(self, value: Window) -> None:
        # Unset the current primary window (value is None)
        if not value and self.__primary_window_uuid:
            _dearpygui.set_primary_window(self.__primary_window_uuid, False)
            self.__primary_window_uuid = None
        # Both are None; do nothing.
        elif not value:
            self.__primary_window_uuid = None
        # Set new primary window.
        else:
            self.__primary_window_uuid = int(value)
            _dearpygui.set_primary_window(self.__primary_window_uuid, True)


    ## Information properties ##
    @classproperty
    @__dearpypixl__.as_information
    def client_width(cls) -> int:
        return _get_viewport_config(cls, "client_width")

    @classproperty
    @__dearpypixl__.as_information
    def client_height(cls) -> int:
        return _get_viewport_config(cls, "client_height")

    @classproperty
    @__dearpypixl__.as_information
    def active_window(cls):
        return registry.get_item(get_active_window(), None)

    @classproperty
    @__dearpypixl__.as_information
    def mouse_drag_delta(cls):
        return get_mouse_drag_delta()

    @classproperty
    @__dearpypixl__.as_information
    def local_mouse_pos(cls) -> list[float]:
        return get_mouse_pos()

    @classproperty
    @__dearpypixl__.as_information
    def global_mouse_pos(cls) -> list[float]:
        return get_mouse_pos(local=False)

    @classproperty
    @__dearpypixl__.as_information
    def drawing_mouse_pos(cls) -> list[float]:
        return get_drawing_mouse_pos()

    @classproperty
    @__dearpypixl__.as_information
    def plot_mouse_pos(cls) -> list[float]:
        return get_plot_mouse_pos()


    ## State properties ##
    __is_maximized  = False
    __is_minimized  = False
    __is_fullscreen = False

    @classproperty
    @__dearpypixl__.as_state
    def is_showing(cls) -> bool:
        return _dearpygui.is_viewport_ok()

    @classproperty
    @__dearpypixl__.as_state
    def is_maximized(cls) -> bool:
        return cls.__is_maximized

    @classproperty
    @__dearpypixl__.as_state
    def is_minimized(cls) -> bool:
        return cls.__is_minimized

    @classproperty
    @__dearpypixl__.as_state
    def is_fullscreen(cls) -> bool:
        return cls.__is_fullscreen


    ################################
    ######## Event Handling ########
    ################################
    _resize_events = ...  # set at runtime

    @classproperty
    def resize_events(cls) -> list[Callback]:
        return cls._resize_events[0]

    @classmethod
    def on_resize(cls, callback: Callable = None, /, *, user_data: Any = None, **kwargs):
        """(Decorator) Schedules a callback to run when the viewport is resized.

        Args:
            * callback (Callable): Callable object to run.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            argument to <callback>. Defaults to None.
        """
        def register():
            return cls._resize_events.on_frame(callback, user_data=user_data, **kwargs)

        if callback is None:
            return register
        return register()


    ################################
    ######## Other Methods #########
    ################################
    __restore_width  = None
    __restore_height = None
    __restore_pos    = None

    @classmethod
    def __set_restore_states(cls, *args, **kwargs) -> None:
        cls.__restore_width  = cls.width
        cls.__restore_height = cls.height
        cls.__restore_pos    = cls.x_pos, cls.y_pos

    @classmethod
    def maximize(cls, *args, **kwargs) -> None:
        """Maximizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        if not cls.__is_maximized and not cls.__is_maximized:
            cls.__set_restore_states()

        cls.__is_maximized = True
        cls.__is_minimized = False
        _dearpygui.maximize_viewport()

    @classmethod
    def minimize(cls, *args, **kwargs) -> None:
        """Minimizes the viewport.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        if not cls.is_maximized and not cls.is_maximized:
            cls.__set_restore_states

        cls.__is_maximized = False
        cls.__is_minimized = True
        _dearpygui.minimize_viewport()

    @classmethod
    def restore_down(cls, *args, **kwargs) -> None:
        """Restores the viewport to its previous non-maximized, non-
        minimized size and position.
        """
        if cls.is_fullscreen:
            cls.toggle_fullscreen()

        width    = cls.__restore_width
        height   = cls.__restore_height
        position = cls.__restore_pos

        if width and height and position:
            cls.configure(width=width, height=height, x_pos=position[0], y_pos=position[1])
            cls.__restore_width  = None
            cls.__restore_height = None
            cls.__restore_pos    = None

    @classmethod
    def toggle_fullscreen(cls, *args, **kwargs) -> None:
        cls.__is_maximized  = False
        cls.__is_minimized  = False
        cls.__is_fullscreen = not cls.__is_fullscreen
        _dearpygui.toggle_viewport_fullscreen()

    @classmethod
    def show(cls) -> None:
        """Begin rendering the viewport. Some Application and Viewport configurations
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


Viewport.configure(title="Application")
