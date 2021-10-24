from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, Union
import inspect
import functools

from dearpygui import _dearpygui, dearpygui

from dearpypixl.item import configuration_override, ItemSupport
from dearpypixl.events import *  # handlers
from dearpypixl.theming import *  # theme, font
from dearpypixl.errors import DearPyGuiErrorHandler

__all__ = [
    "ContextSupport",
    "ThemeSupport",
    "EventSupport",
    "EventHandlerSupport",
    "StateSupport",
    "_appitemsupport",
]



###################################
##### Item subclass mixins ########
###################################
class ContextSupport(ItemSupport):
    """A mixin for *Item* subclasses. Allows context manager syntax usage
    for container-like items.
    """
    def __enter__(self):
        _dearpygui.push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        _dearpygui.pop_container_stack()


class ThemeSupport(ItemSupport):
    """A mixin for *Item* subclasses. Adds a `theme` (getter/setter) property.
    """
    def __init__(self, theme: Theme = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if theme:
            self.theme = theme

    @property
    @configuration_override
    def theme(self) -> Theme:
        if not (theme_uuid := _dearpygui.get_item_info(self._tag)["theme"]):
            theme_item = Theme(include_presets=True)
            theme_item.bind(self)
            return theme_item
        return self._appitems[theme_uuid]
    @theme.setter
    def theme(self, value: Union[Theme, None]) -> None:
        if value is None:
            value.unbind(self)
        value.bind(self)

            

class EventSupport(ItemSupport, metaclass=ABCMeta):
    """Base class for event support mixins.
    """
    @abstractmethod
    def _handler_map(self): ...  # {method_name_str: EventHandlerItem}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registered_handlers: dict[str, tuple] = {}
        

    def _pop_handler(self, handler_type: str, callback: Callable):
        # Removes <callback> from <handler_type> in self._registered_handlers.
        key = self._registered_handlers[handler_type]
        for idx, h_info in enumerate(key):
            if h_info[0] == callback:
                handler = key.pop(idx)[-1]
                return handler
        return None

    def _set_handler(self, callback: Callable = None, **kwargs):
        # Generic handler. This should be called in every handler method.
        @functools.wraps(callback)
        def wrapper(callback):
            id = self._tag
            if type(id) == int:
                handler = self._handler_map[method_name](
                    self._tag,
                    callback=callback,
                    **kwargs
                )
            # `self` is a viewport/application item. Parent is the
            # default handler registry and doesn't need to be passed.
            else:
                handler = self._handler_map[method_name](
                    callback=callback,
                    **kwargs
                )
            self._registered_handlers.setdefault(getattr(self, method_name).__name__, []).append(
                (callback, handler),
            )
            return callback

        method_name = f"{inspect.stack()[1].function}"

        if not callback:
            return wrapper
        return wrapper(callback)


class EventItemSupport(EventSupport, ItemSupport):
    """A mixin for *Item* subclasses. Includes decorators for conveniently
    registering event handlers to items.
    """
    _handler_map = {
        "while_active": ItemActiveHandler,
        "on_activation": ItemActivatedHandler,
        "on_click": ItemClickedHandler,
        "on_deactivation_after_edit": ItemDeactivatedAfterEditHandler,
        "on_deactivation": ItemDeactivatedHandler,
        "on_edit": ItemEditedHandler,
        "on_focus": ItemFocusHandler,
        "on_hover": ItemHoverHandler,
        "on_resize": ItemResizeHandler,
        "on_toggle_open": ItemToggledOpenHandler,
        "on_visible": ItemVisibleHandler,
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


class StateSupport(ItemSupport):
    """A mixin for Item subclasses. Includes properties for fetching various
    states of an item.
    """
    @property
    def is_container(self) -> bool:
        """Checks if the widget is a container item.
        """
        return _dearpygui.get_item_info(self._tag)["container"]

    @property
    def is_hovered(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["hovered"]

    @property
    def is_active(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["active"]

    @property
    def is_focused(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["focused"]

    @property
    def is_clicked(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["clicked"]

    @property
    def is_visible(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["visible"]

    @property
    def is_edited(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["edited"]

    @property
    def is_activated(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["activated"]

    @property
    def is_deactivated(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["deactivated"]

    @property
    def is_deactivated_after_edit(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["deactivated_after_edit"]

    @property
    def is_toggled_open(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["toggled_open"]

    @property
    def is_ok(self) -> bool:
        return _dearpygui.get_item_state(self._tag)["ok"]


class CommandSupport(ItemSupport):
    """A mixin for Item subclasses. Has general-purpose methods suitable
    for most items.
    """
    def focus(self):
        """Brings the widget into focus.
        """
        _dearpygui.focus_item(self._tag)

    def move_up(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it.
        """
        _dearpygui.move_item_up(self._tag)

    def move_down(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it.
        """
        _dearpygui.move_item_down(self._tag)

    def move(self, parent, before: int = 0) -> None:
        """If the widget is a child, it will be moved to another
        parent and placed above/before another item.

        Args:
            parent (int): id of the new parent.
            before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        with DearPyGuiErrorHandler(self, "parent", parent):
            _dearpygui.move_item(self._tag, parent=int(parent), before=before)


