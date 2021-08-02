from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any
import functools
import inspect
import copy

from dearpygui import dearpygui as dpg

from dpgwidgets.constants import Registry as Registry

# NOTE: Widget-level and global-level handlers are different from
# each other in DPG. Global handlers (AppHandlerSupport) can be toggled
# using the "show" keyword and also have their own unique registry (because
# they lack parenting widgets). Widget handlers can't be toggled in the 
# same way and must be deleted. For now, both cases will be handled in
# the former manner. The classes below try not to expose the handler
# items directly and manages them internally.

class HandlerBase(metaclass=ABCMeta):
    @abstractmethod
    def _handler_map(self): ...  # {method_name_str: dpg.handler_callable}

    def __init__(self):
        super().__init__()
        self._registered_handlers = {}

    def registered_handlers(self):
        """Returns a copied dict of the handlers currently registered to the item."""
        return copy.deepcopy(self._registered_handlers)

    def unregister_handler(self, handler: str, callback: Callable):
        """Unregisters a handler that is currently registered to the item.

        Args:
            handler (str): Name of the handler/method the callback is registered to.
            callback (Callable): Callable that the handler is registered with.
        """
        handler = self._pop_handler(handler, callback)
        dpg.delete_item(handler)

    def _pop_handler(self, handler_type: str, callback: Callable):
        # Removes <callback> from <handler_type> in self._registered_handlers.
        key = self._registered_handlers[handler_type]
        for idx, h_info in enumerate(key):
            if h_info[0] == callback:
                handler = key.pop(idx)[-1]
                return handler
        return None

    def _set_handler(self, callback: Callable = None,**kwargs):
        # Generic handler. This should be called in every handler method.
        @functools.wraps(callback)
        def wrapper(callback):
            handler = self._handler_map[method_name](
                self.id,
                callback=callback,
                **kwargs
            )
            self._registered_handlers.setdefault(getattr(self, method_name).__name__, []).append(
                (callback, handler),
            )
            return callback

        # Calling str creating a "copy" to ensure that there
        # are no references to the frame itself once the call
        # resolves. See "Note" in
        # https://docs.python.org/3/library/inspect.html#the-interpreter-stack.
        method_name = str(inspect.stack()[1].function)

        if not callback:
            return wrapper
        
        return wrapper(callback)


class HandlerSupport(HandlerBase):
    """Mixin for the Widget class that supports the addition/removal of handlers.
    """
    _handler_map = {
        "while_active": dpg.add_active_handler,
        "on_activation": dpg.add_activated_handler,
        "on_click": dpg.add_clicked_handler,
        "on_deactivation_after_edit": dpg.add_deactivated_after_edit_handler,
        "on_deactivation": dpg.add_deactivated_handler,
        "on_edit": dpg.add_edited_handler,
        "on_focus": dpg.add_focus_handler,
        "on_hover": dpg.add_hover_handler,
        "on_resize": dpg.add_resize_handler,
        "on_toggle_open": dpg.add_toggled_open_handler,
        "on_visible": dpg.add_visible_handler,
    }

    def while_active(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_activation(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)
    
    def on_deactivation(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_deactivation_after_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_click(self, callback: Callable = None, *, user_data: Any = None, button=-1, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, button=button, **kwargs)

    def on_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_focus(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_hover(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)
    
    def on_resize(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_toggle_open(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_visible(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)


class AppHandlerSupport(HandlerBase):
    """Mixin for the Application class that supports the addition/removal of handlers.
    """
    _handler_map = {
        "while_key_down": dpg.add_key_down_handler,
        "on_key_down": dpg.add_key_press_handler,
        "on_key_up": dpg.add_key_release_handler,
        "while_mouse_key_down":  dpg.add_mouse_down_handler,
        "on_mouse_key_click": dpg.add_mouse_click_handler,
        "on_mouse_key_double_click": dpg.add_mouse_double_click_handler,
        "on_mouse_key_up": dpg.add_mouse_release_handler,
        "on_mouse_wheel_scroll": dpg.add_mouse_wheel_handler,
        "on_mouse_move": dpg.add_mouse_move_handler,
        "on_mouse_drag": dpg.add_mouse_drag_handler,
    }

    # Global-level handlers use a handler registry parent and
    # not a typical widget.
    def _set_handler(self, callback: Callable = None, **kwargs):
        @functools.wraps(callback)
        def wrapper(callback):
            handler = self._handler_map[method_name](
                parent=Registry.APPHANDLER.value,
                callback=callback,
                **kwargs
            )
            self._registered_handlers.setdefault(getattr(self, method_name).__name__, []).append(
                (callback, handler),
            )
            return callback

        # Calling str creating a "copy" to ensure that there
        # are no references to the frame itself once the call
        # resolves. See "Note" in
        # https://docs.python.org/3/library/inspect.html#the-interpreter-stack.
        method_name = str(inspect.stack()[1].function)

        if not callback:
            return wrapper

        return wrapper(callback)

    def while_key_down(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_key_down(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        # NOTE: Most OS have a key-repeat feature for keys that
        # are held down for a period of time - it will fire this
        # callback repeatedly if enabled (not NEARLY as much as
        # "while_key_down").
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_key_up(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def while_mouse_key_down(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_key_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_key_double_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_key_up(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_drag(self, callback: Callable = None, *, button: int = -1, threshold: float = 10.0, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)
