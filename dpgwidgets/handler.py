from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any
import functools
import inspect
import copy

from dearpygui import dearpygui as dpg

from dpgwidgets.libsrc.handlers import *


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
        self._registered_handlers: dict[str,tuple] = {}

    def unregister_handler(self, handler: str, callback: Callable):
        """Unregisters a handler that is currently registered to the item.

        Args:
            handler (str): Name of the handler/method the callback is registered to.
            callback (Callable): Callable that the handler is registered with.
        """
        handler = self._pop_handler(handler, callback)
        handler.delete()

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
        method_name = f"{inspect.stack()[1].function}"

        if not callback:
            return wrapper
        
        return wrapper(callback)


class HandlerSupport(HandlerBase):
    """Mixin for the Widget class that supports the addition/removal of 
    """
    _handler_map = {
        "while_active": ActiveHandler,
        "on_activation": ActivatedHandler,
        "on_click": ClickedHandler,
        "on_deactivation_after_edit": DeactivatedAfterEditHandler,
        "on_deactivation": DeactivatedHandler,
        "on_edit": EditedHandler,
        "on_focus": FocusHandler,
        "on_hover": HoverHandler,
        "on_resize": ResizeHandler,
        "on_toggle_open": ToggledOpenHandler,
        "on_visible": VisibleHandler,
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
    """Mixin for the Application class that supports the addition/removal of 
    """
    _handler_map = {
        "while_key_down": KeyDownHandler, 
        "on_key_press": KeyPressHandler,
        "on_key_up": KeyReleaseHandler,
        "while_mouse_down":  MouseDownHandler,
        "on_mouse_click": MouseClickHandler,
        "on_mouse_double_click": MouseDoubleClickHandler,
        "on_mouse_up": MouseReleaseHandler,
        "on_mouse_wheel_scroll": MouseWheelHandler,
        "on_mouse_move": MouseMoveHandler,
        "on_mouse_drag": MouseDragHandler,
    }

    # Global-level handlers use a handler registry parent and
    # not a typical widget.
    def _set_handler(self, callback: Callable = None, **kwargs):
        @functools.wraps(callback)
        def wrapper(callback):
            handler = self._handler_map[method_name](
                parent=dpg.mvReservedUUID_1,
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
        method_name = f"{inspect.stack()[1].function}"

        if not callback:
            return wrapper

        return wrapper(callback)

    def while_key_down(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_key_press(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        # NOTE: Most OS have a key-repeat feature for keys that
        # are held down for a period of time - it will fire this
        # callback repeatedly if enabled (not NEARLY as much as
        # "while_key_down").
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_key_up(self, callback: Callable = None, *, key: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def while_mouse_down(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_double_click(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_up(self, callback: Callable = None, *, button: int = -1, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)

    def on_mouse_drag(self, callback: Callable = None, *, button: int = -1, threshold: float = 10.0, user_data: Any = None, **kwargs):
        return self._set_handler(callback=callback, user_data=user_data, **kwargs)
