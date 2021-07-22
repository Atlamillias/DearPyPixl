from abc import ABCMeta, abstractmethod
from typing import Callable

from dpgwidgets import idpg, Item, ContextSupport
from dpgwidgets.handler import HandlerSupport
from dpgwidgets.theme import ThemeSupport


class Widget(Item, ThemeSupport, HandlerSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move_up(self) -> None:
        idpg.move_item_up(self.id)

    def move_down(self) -> None:
        idpg.move_item_down(self.id)

    def move(self, parent: int, before: int) -> None:
        """Move a widget to another <parent> before <before>."""
        idpg.move_item(self.id, parent, before)

    def slots(self, slot: int = -1) -> dict:
        """Returns the item's slots and the list of children (id) in each
        as a dict ({slot: [],...})."""


    ## State-getters ##
    @property
    def is_container(self):
        return idpg.get_item_info(self.__id)["container"]

    @property
    def is_hovered(self):
        return idpg.get_item_state(self.__id)["hovered"]

    @property
    def is_active(self):
        return idpg.get_item_state(self.__id)["active"]

    @property
    def is_focused(self):
        return idpg.get_item_state(self.__id)["focused"]

    @property
    def is_clicked(self):
        return idpg.get_item_state(self.__id)["clicked"]

    @property
    def is_visible(self):
        return idpg.get_item_state(self.__id)["visible"]

    @property
    def is_edited(self):
        return idpg.get_item_state(self.__id)["edited"]

    @property
    def is_activated(self):
        return idpg.get_item_state(self.__id)["activated"]

    @property
    def is_deactivated(self):
        return idpg.get_item_state(self.__id)["deactivated"]

    @property
    def is_deactivated_after_edit(self):
        return idpg.get_item_state(self.__id)["deactivated_after_edit"]

    @property
    def is_toggled_open(self):
        return idpg.get_item_state(self.__id)["toggled_open"]

    @property
    def is_ok(self):
        return idpg.get_item_state(self.__id)["ok"]



class Container(Widget, ContextSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...


    # x_scroll
    @property
    def y_scroll_pos(self):
        return idpg.get_y_scroll(self.id)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        idpg.set_y_scroll(self.id, value)

    @property
    def y_scroll_max(self):
        return idpg.get_y_scroll_max(self.id)


    # y_scroll
    @property
    def x_scroll_pos(self):
        return idpg.get_x_scroll(self.id)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return idpg.set_x_scroll(self.id, value)

    @property
    def x_scroll_max(self):
        return idpg.get_x_scroll_max(self.id)


    def reset_pos(self):
        idpg.reset_pos(self.id)

    def children(self) -> list:
        """Returns a list containing the id of all *high-level children
        within a container.

        *Slots 1 and 2 in idpg.get_item_children(self.id, slot)
        """
        return [child for slot, childs in 
                idpg.get_item_children(self.id, -1).items()
                for child in childs 
                if any(slot == i for i in (1, 2))]
        
    

