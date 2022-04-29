from abc import ABCMeta, abstractmethod
from typing import Callable, TypeVar, Union
from dearpygui._dearpygui import (
    reset_pos,
    push_container_stack,
    pop_container_stack,
    get_item_info,
)

from dearpypixl.components.configuration import ItemAttribute, item_attribute
from dearpypixl.components.item import (
    ItemT,
    ProtoItem,
    Item,    
)
from dearpypixl.components.registries import *
from dearpypixl.components.themes import Theme


__all__ = [
    # Limiting what objects are exported to appitem modules that import using `*`.
    "ItemAttribute",
    "item_attribute",

    "ItemT",
    "Widget",
]


WidgetItemT     = TypeVar("WidgetItemT"      , bound='Widget'   )


class Widget(Item, metaclass=ABCMeta):
    __slots__ = ("__events_uuid",)

    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, theme: Union[Theme, bool, None] = None, events: Union[ItemEvents, bool, None] = None, **kwargs):
        super().__init__(**kwargs)

        # Unlike themes, DearPyGui does not include a way of fetching the item handler
        # registry bound to an item, so it needs to be saved. However, this info can
        # become outdated if the `events` property isn't used to bind them. So this is,
        # at best, a quick tempfix.
        self.__events_uuid = None

        if not theme and not events:
            return None
        if theme:
            if theme is True:
                self.theme = Theme()
            else:
                self.theme = theme
        if events:
            if events is True:
                self.events = ItemEvents()
            else:
                self.events = events

    @property
    @item_attribute(category="configuration")
    def theme(self) -> Theme:
        return self._AppItemsRegistry.get(get_item_info(self._tag)["theme"], None)
    @theme.setter
    def theme(self, value: Theme) -> None:
        if value is None and (item_theme := self._AppItemsRegistry.get(get_item_info(self._tag)["theme"], None)):
            item_theme.unbind(self)
            return None
        elif value is None:
            return None
        value.bind(self)

    @property
    @item_attribute(category="configuration")
    def events(self) -> ItemEvents:
        self.__events_uuid
        return self._AppItemsRegistry.get(self.__events_uuid, None)
    @events.setter
    def events(self, value: ItemEvents) -> None:
        if value is None and self.__events_uuid:
            try:
                item_events = self._AppItemsRegistry[self.__events_uuid]
            except KeyError:
                self.__events_uuid = None
                return None
            return item_events.unbind(self)
        elif value is None:
            return None
        self.__events_uuid = value._tag
        value.bind(self)



