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


    # x_scroll
    @property
    def y_scroll_pos(self):
        return dpg.get_y_scroll(self.id)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        dpg.set_y_scroll(self.id, value)

    @property
    def y_scroll_max(self):
        return dpg.get_y_scroll_max(self.id)


    # y_scroll
    @property
    def x_scroll_pos(self):
        return dpg.get_x_scroll(self.id)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return dpg.set_x_scroll(self.id, value)

    @property
    def x_scroll_max(self):
        return dpg.get_x_scroll_max(self.id)


    def reset_pos(self):
        dpg.reset_pos(self.id)

    def children(self) -> list:
        """Returns a list containing the id of all *high-level children
        within a container.

        *Slots 1 and 2 in dpg.get_item_children(self.id, slot)
        """
        return [child for slot, childs in 
                dpg.get_item_children(self.id, -1).items()
                for child in childs 
                if any(slot == i for i in (1, 2))]
        
    

