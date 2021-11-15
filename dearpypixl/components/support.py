"""High-level mixins for Item subclasses (appitems)."""
from typing import Any, Union, Callable
from dearpygui import _dearpygui
from dearpypixl.items import (
    Item,
    ItemAttribute,
    item_attribute,
    ItemAttributeCache,
    Theme,
    ItemEvents,
    ItemAttributeCache,
)
from dearpygui._dearpygui import (
    push_container_stack,
    pop_container_stack,
    get_item_info,
    get_item_state
)



class ContextSupport(ItemAttributeCache):
    """Allows using context manager syntax for (container) appitems.
    """

    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        pop_container_stack()


class AddinSupport(ItemAttributeCache):
    """Optional "extras" for appitems.
    """
    def __init__(self, events: ItemEvents = None, theme: Theme = None, **kwargs):
        super().__init__(**kwargs)
        # Information regarding the bound events registry can't be fetched
        # like theme can...
        self.__event_uuid = None
        if events:
            self.events = events
        if theme:
            self.theme = theme

    @property
    @item_attribute(category="configuration")
    def events(self) -> ItemEvents:
        return self._appitems.get(self.__event_uuid, None)
    @events.setter
    def events(self, value: Union[ItemEvents, None]) -> None:
        if value is None:
            self.__appitems[self.__event_uuid].unbind(self)
            self.__event_uuid = None
            return None
        value.bind(self)
        self.__event_uuid = int(value)

    @property
    @item_attribute(category="configuration")
    def theme(self) -> Union[Theme, None]:
        if not (theme_uuid := get_item_info(self._tag)["theme"]):
            return None
        return self._appitems[theme_uuid]
    @theme.setter
    def theme(self, value: Union[Theme, None]) -> None:
        if value is None and not (theme_uuid := get_item_info(self._tag)["theme"]):
            return self._appitems[theme_uuid].unbind(self)
        value.bind(self)


class CommandSupport(ItemAttributeCache):
    """Misc. methods for appitems.
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

    def move(self, * , parent: Item = 0, before: Item = 0) -> None:
        """If the item is a child, it will be moved to another
        parent and placed above/before another item.

        Args:
            parent (int): id of the new parent.
            before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        _dearpygui.move_item(self._tag, parent=int(parent), before=int(before))
