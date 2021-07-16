from abc import ABCMeta, abstractmethod
from typing import Callable

from dpgwidgets import dpg, Item, ContextSupport
from dpgwidgets.handler import HandlerSupport
from dpgwidgets.theme import ThemeSupport


class Widget(Item, ThemeSupport, HandlerSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move_up(self) -> None:
        dpg.move_item_up(self.id)

    def move_down(self) -> None:
        dpg.move_item_down(self.id)

    def move(self, parent: int, before: int) -> None:
        """Move a widget to another <parent> before <before>."""
        dpg.move_item(self.id, parent, before)

    def slots(self, slot: int = -1) -> dict:
        """Returns the item's slots and the list of children (id) in each
        as a dict ({slot: [],...})."""


class Container(Widget, ContextSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def children(self) -> list:
        """Returns a list containing the id of all *high-level children
        within a container.

        *Slots 1 and 2 in dpg.get_item_children(self.id, slot)
        """
        return [child for slot, childs in 
                dpg.get_item_children(self.id, -1).items()
                for child in childs 
                if any(slot == i for i in (1, 2))]

