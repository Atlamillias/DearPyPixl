from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, Union
import inspect
import functools
from dearpygui import _dearpygui as idpg


from pixle.events import *  # handlers
from pixle.theming import *  # theme, font

__all__ = [
    "ContextSupport",
    "ThemeSupport",
    "EventSupport",
    "EventHandlerSupport",
    "StateSupport",
    "CallbackSupport",
    "AppItemSupport",
]



###################################
##### Item subclass mixins ########
###################################
class ContextSupport:
    """A mixin for *Item* subclasses. Allows context manager syntax usage
    for container-like items.
    """

    def __enter__(self):
        # If the container is still staged, commit its setup.
        if not self._is_initialized:
            self.commit_setup()

        idpg.push_container_stack(self._id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        idpg.pop_container_stack()


class ThemeSupport:
    """A mixin for *Item* subclasses. Allows for items to have their
    own self-contained theme.
    """
    def __init__(self, theme: Theme=None, *args, **kwargs):
        self._theme = theme or Theme()
        super().__init__(*args, **kwargs)

    def commit_setup(self):
        # Item.commit_setup needs to be ran first to create the item.
        super().commit_setup()
        self.theme = self._theme

    @property
    def theme(self):
        return self._theme
    @theme.setter
    def theme(self, value: Theme):
        self._theme = value

        if self._is_initialized:
            value.apply(self)
            

class EventSupport(metaclass=ABCMeta):
    """Base class for event support mixins.
    """
    @abstractmethod
    def _handler_map(self): ...  # {method_name_str: EventHandlerItem}

    def __init__(self, *args, **kwargs):
        self._registered_handlers: dict[str, tuple] = {}
        super().__init__(*args, **kwargs)
        

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
            id = self._id
            if type(id) == int:
                handler = self._handler_map[method_name](
                    self._id,
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


class EventItemSupport(EventSupport):
    """A mixin for *Item* subclasses. Includes decorators for conveniently
    registering event handlers to items.
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


class StateSupport:
    """A mixin for Item subclasses. Includes properties for fetching various
    states of an item.
    """
    @property
    def is_container(self) -> bool:
        """Checks if the widget is a container item.
        """
        return idpg.get_item_info(self._id)["container"]

    @property
    def is_hovered(self) -> bool:
        return idpg.get_item_state(self._id)["hovered"]

    @property
    def is_active(self) -> bool:
        return idpg.get_item_state(self._id)["active"]

    @property
    def is_focused(self) -> bool:
        return idpg.get_item_state(self._id)["focused"]

    @property
    def is_clicked(self) -> bool:
        return idpg.get_item_state(self._id)["clicked"]

    @property
    def is_visible(self) -> bool:
        return idpg.get_item_state(self._id)["visible"]

    @property
    def is_edited(self) -> bool:
        return idpg.get_item_state(self._id)["edited"]

    @property
    def is_activated(self) -> bool:
        return idpg.get_item_state(self._id)["activated"]

    @property
    def is_deactivated(self) -> bool:
        return idpg.get_item_state(self._id)["deactivated"]

    @property
    def is_deactivated_after_edit(self) -> bool:
        return idpg.get_item_state(self._id)["deactivated_after_edit"]

    @property
    def is_toggled_open(self) -> bool:
        return idpg.get_item_state(self._id)["toggled_open"]

    @property
    def is_ok(self) -> bool:
        return idpg.get_item_state(self._id)["ok"]


class CallbackSupport:
    """A mixin for Item subclasses. Has methods that can be used as decorators
    for registering item (drag) callbacks.
    """
    ...

class ItemMethodSupport:
    """A mixin for Item subclasses. Has general-purpose methods suitable
    for most items.
    """
    def focus(self):
        """Brings the widget into focus.
        """
        idpg.focus_item(self._id)

    def move_up(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it.
        """
        idpg.move_item_up(self._id)

    def move_down(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it.
        """
        idpg.move_item_down(self._id)

    def move(self, parent: int, before: int = 0) -> None:
        """If the widget is a child, it will be moved to another
        parent and placed above/before another item.

        Args:
            parent (int): id of the new parent.
            before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        idpg.move_item(self._id, parent, before)
