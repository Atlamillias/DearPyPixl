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
    TemplateT,
    ItemLikeT,
    Template,
    ProtoItem,
    Item,  
    ItemLike,  
)
from dearpypixl.components.registries import *
from dearpypixl.components.themes import (
    Theme,
    ThemeComponent,
    ThemeColorComponent,
    ThemeStyleComponent,
    Font
)


__all__ = [
    # NOTE: Limiting what objects are exported to appitem modules.
    "ItemAttribute",
    "item_attribute",

    "ItemT",
    "Container",
    "Widget",
]


WidgetItemT     = TypeVar("WidgetItemT"      , bound='Widget'   )
ContainerItemT  = TypeVar("ContainerItemT"   , bound='Container')



class Widget(Item, metaclass=ABCMeta):
    __slots__ = ("__events_uuid")

    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, theme: Union[Theme, bool, None] = None, events: Union[ItemEvents, bool, None] = None, **kwargs):
        super().__init__(**kwargs)

        self.__events_uuid = None  # Temporary fix

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



class Container(Widget, metaclass=ABCMeta):
    __slots__ = ()
    
    @abstractmethod
    def _command() -> Callable: ...

    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        pop_container_stack()

    # TODO: This really should be handled the same way `default_value` and `value` is handled.
    def reset_pos(self) -> None:
        """Sets the item position (`pos`) to it's original position.
        """
        reset_pos(self.tag)
