from __future__ import annotations
from typing import TYPE_CHECKING, Callable, Any
import functools
import inspect

from . import dpg
from .dpgwrap._item import Item, Context

if TYPE_CHECKING:
    from .widget import Widget


# Even though handlers are also items in DPG, they are
# the only items that I have treated differently in this package.
# Instead of exposing the handlers and handler registries seperately
# (like containers and widgets), only the registry itself is exposed
# (as the "handler") while the handlers are are exposed as methods 
# of each registry. 

# Handlers are injected into HandlerRegistry subclasses at runtime.
# This could have been done using metaclasses and descriptors (probably will)
# but I wanted the code itself to be readable.

_HANDLER_METHOD = """
def {mname}(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
    @functools.wraps(callback)
    def wrapper(callback):
        handler = dpg.{cmd}(
            self.parent.id,
            callback=callback,
            user_data=user_data,
            **kwargs
        )
        self.handlers.setdefault(self.{mname}.__name__, []).append(
            (callback, handler),
        )
        return callback

    if not callback:
        return wrapper

    handler = dpg.{cmd}(
        self.parent.id,
        callback=callback,
        user_data=user_data,
        **kwargs
        )
    self.handlers.setdefault(self.{mname}.__name__, []).append(
        (callback, handler),
    )
    return callback
"""

class HandlerRegistry:  # Mixin
    __handlers: dict[list[tuple]] = {}

    @property
    def handlers(self):
        return self.__handlers

    def unhandle(self, handler_type: str, callback: Callable):
        handler = self._pop_handler(handler_type, callback)

        dpg.delete_item(handler)

    def _pop_handler(self, handler_type: str, callback: Callable):
        key = self.__handlers[handler_type]
        for idx, h_info in enumerate(key):
            if h_info[0] == callback:
                handler = key.pop(idx)[-1]
                return handler

        return None



# Method "templates" are defined in HandlerRegistry subclasses
# to allow intellisense and language servers to do its thing. They
# are actually redefined at runtime using the
# "HandlerRegistry.__handler_method" code template.
class AppHandler(Item, Context, HandlerRegistry):
    _command = dpg.add_handler_registry

    _HANDLERS = {
        "while_key_down": "add_key_down_handler",  # mvKeyDownHandler
        "on_key_press": "add_key_press_handler",  # mvKeyPressHandler
        "on_key_up": "add_key_release_handler",  # mvKeyReleaseHandler
        "while_mouse_key_down":  "add_mouse_down_handler",  # mvMouseDownHandler
        "on_mouse_key_click": "add_mouse_click_handler",  # mvMouseClickHandler
        # mvMouseDoubleClickHandler
        "on_mouse_key_double_click": "add_mouse_double_click_handler",
        "on_mouse_key_up": "add_mouse_release_handler",  # mvMouseReleaseHandler
        "on_mouse_wheel_scroll": "add_mouse_wheel_handler",  # mvMouseWheelHandler
        "on_mouse_move": "add_mouse_move_handler",  # mvMouseMoveHandler
        "on_mouse_drag": "add_mouse_drag_handler",  # mvMouseDragHandler
    }

    def __init__(self, show: bool = True, label: str = None, **kwargs):
        super().__init__(show=show, label=label, **kwargs)
        self.__handlers = {}
        self.show = show
        self.label = label

    def while_key_down(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_key_press(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_key_up(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def while_mouse_key_down(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_key_click(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_key_double_click(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_key_up(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_mouse_drag(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...


# DPG doesn't have a specific widget handler registry item.
# Probably because there is a parenting widget instead
class WidgetHandler(HandlerRegistry):
    _HANDLERS = {
        "while_active": "add_active_handler",  # mvActivatedHandler
        "on_activation": "add_activated_handler",  # mvActiveHandler
        "on_click": "add_clicked_handler",  # mvClickedHandler
        # mvDeactivatedAfterEditHandler
        "on_deactivation_after_edit": "add_deactivated_after_edit_handler",
        "on_deactivation": "add_deactivated_handler",  # mvDeactivatedHandler
        "on_edit": "add_edited_handler",  # mvEditedHandler
        "on_focus": "add_focus_handler",  # mvFocusHandler
        "on_hover": "add_hover_handler",  # mvHoverHandler
        "on_resize": "add_resize_handler",  # mvResizeHandler
        "on_toggle_open": "add_toggled_open_handler",  # mvToggledOpenHandler
        "on_visible": "add_visible_handler",  # mvVisibleHandler
    }

    def __init__(self, parent: "Widget"):
        self.__handlers = {}
        self.parent = parent

    def while_active(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_activation(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...
    
    def on_deactivation(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_deactivation_after_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_click(self, callback: Callable = None, *, user_data: Any = None, button=-1, **kwargs):
        ...

    def on_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_focus(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_hover(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...
    
    def on_resize(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_toggle_open(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    def on_visible(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...


def _patch_handlers():
    filepath = ""
    template_str = _HANDLER_METHOD

    for m_name, cmd in AppHandler._HANDLERS.items():
        m_template = template_str.format(cmd=cmd, mname=m_name)
        method = compile(m_template, filename=filepath, mode="exec")
        exec(method)  # m_name

        setattr(AppHandler, m_name, eval(m_name))

    for m_name, cmd in WidgetHandler._HANDLERS.items():
        m_template = template_str.format(cmd=cmd, mname=m_name)
        method = compile(m_template, filename=filepath, mode="exec")
        exec(method)  # m_name

        setattr(WidgetHandler, m_name, eval(m_name))


_patch_handlers()