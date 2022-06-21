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
from dearpypixl.itemtypes.events import FrameEvents
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

if not TYPE_CHECKING:
    Window = None
else:
    from dearpypixl.containers import Window


__all__ = ["Viewport"]




def _run_resize_events():
    for event in _RESIZE_EVENTS[0]:
        event()


_RESIZE_EVENTS = FrameEvents()

dict.__setitem__(_RESIZE_EVENTS, 0, [])  # bypass `set_frame_callback` hook
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
    title        : str  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    width        : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    height       : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    min_width    : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    min_height   : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    max_width    : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    max_height   : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    x_pos        : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    y_pos        : int  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    resizable    : bool = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    vsync        : bool = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    always_on_top: bool = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    decorated    : bool = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    clear_color  : bool = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_config)
    small_icon   : str  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_fickle_config)
    large_icon   : str  = ItemProperty(CONFIG, _get_viewport_config, _set_viewport_fickle_config)


    __primary_window_uuid = None

    @property
    @ItemProperty.register(category=CONFIG)
    def primary_window(self) -> Window:
        p_window = self.__registry__.get_item(self.__primary_window_uuid, None)
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
    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def tag(cls) -> str:
        return cls.__cached__["viewport_uuid"]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def client_width(cls) -> int:
        return _get_viewport_config(cls, "client_width")

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def client_height(cls) -> int:
        return _get_viewport_config(cls, "client_height")

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def active_window(cls):
        return cls.__registry__[0].get(get_active_window(), None)

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def mouse_drag_delta(cls):
        return get_mouse_drag_delta()

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def local_mouse_pos(cls) -> list[float]:
        return get_mouse_pos()

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def global_mouse_pos(cls) -> list[float]:
        return get_mouse_pos(local=False)

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def drawing_mouse_pos(cls) -> list[float]:
        return get_drawing_mouse_pos()

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def plot_mouse_pos(cls) -> list[float]:
        return get_plot_mouse_pos()


    ## State properties ##
    __is_maximized  = False
    __is_minimized  = False
    __is_fullscreen = False

    @classmethod
    @property
    @ItemProperty.register(category=STATES)
    def is_showing(cls) -> bool:
        return _dearpygui.is_viewport_ok()

    @classmethod
    @property
    @ItemProperty.register(category=STATES)
    def is_maximized(cls) -> bool:
        return cls.__is_maximized

    @classmethod
    @property
    @ItemProperty.register(category=STATES)
    def is_minimized(cls) -> bool:
        return cls.__is_minimized

    @classmethod
    @property
    @ItemProperty.register(category=STATES)
    def is_fullscreen(cls) -> bool:
        return cls.__is_fullscreen


    ################################
    ######## Event Handling ########
    ################################
    @classmethod
    @property
    def resize_events(cls) -> list:
        return _RESIZE_EVENTS[0]

    @classmethod
    def on_resize(cls, callback: Callable = None, /, *, user_data: Any = None, **kwargs):
        """(Decorator) Schedules a callback to run when the viewport is resized.

        Args:
            * callback (Callable): Callable object to run.
            * user_data (Any, optional): This will be sent as the third positional
            argument to <callback>. Defaults to None.
        """
        def register():
            return _RESIZE_EVENTS.on_frame(callback, user_data=user_data, **kwargs)

        if callback is None:
            return register
        return register()


    ################################
    ######## Other Methods #########
    ################################
    @classmethod
    def configure(cls, **config) -> None:
        # Set on internal instance.
        return Item.configure(_Viewport)

    @classmethod
    def configuration(cls) -> dict[str, Any]:
        # Set on internal instance.
        cfg_attrs  = cls.__internal__[0]
        dpg_config = get_viewport_configuration(cls.tag)
        config     = {attr:(dpg_config[attr] if attr in dpg_config else getattr(_Viewport, attr))
                      for attr in cfg_attrs}
        return config

    @classmethod
    def information(cls) -> dict[str, Any]:
        # These should all be classmethod properties, so this is straightforward.
        return Item.information(cls)

    @classmethod
    def state(cls) -> dict[str, Any]:
        return {attr:(getattr(cls, attr)) for attr in cls.__internal__[2]}

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


# Some Viewport classmethods use this as it's easier to get descriptor
# values from an instance.
_Viewport = Viewport()