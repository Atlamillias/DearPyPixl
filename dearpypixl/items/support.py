"""High-level mixins for Item subclasses (appitems)."""
from typing import Any, Union, Callable
from dearpygui import _dearpygui
from dearpypixl.components import (
    Theme,
    Events,
    ItemAttributeCache,
    configuration_override,
    information_override
)
from dearpypixl.errors import DearPyGuiErrorHandler




class ContextSupport(ItemAttributeCache):
    """A mixin for *Item* subclasses. Allows context manager syntax usage
    for container-like items.
    """

    def __enter__(self):
        _dearpygui.push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        _dearpygui.pop_container_stack()


class ThemeSupport(ItemAttributeCache):
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


class EventSupport(ItemAttributeCache):
    """A mixin for *Item* subclasses. Adds a `theme` (getter/setter) property.
    """
    def __init__(self, events: Events = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Information regarding the bound events registry can't be fetched
        # like theme can...
        self.__event_uuid = None
        self.events = events or Events()
        

    @property
    @configuration_override
    def events(self) -> Events:
        return self._appitems[self.__event_uuid]

    @events.setter
    def events(self, value: Union[Events, None]) -> None:
        if value is None:
            value.unbind(self)
        value.bind(self)
        self.__event_uuid = int(value)


class StateSupport(ItemAttributeCache):
    """A mixin for Item subclasses. Includes properties for fetching various
    states of an item.
    """
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




class CommandSupport(ItemAttributeCache):
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
