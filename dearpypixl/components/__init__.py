from abc import ABCMeta, abstractmethod
from dearpygui import _dearpygui
from dearpypixl.item import (
    item_attribute,
    ItemAttribute,
    ConfigContainer,
    Item,

    ItemT,
)
from dearpypixl.components.registries import *
from dearpypixl.components.other import UniqueItemMeta, ItemLike, UpdaterList


__all__ = [
    # NOTE: Limiting what objects are exported to appitem modules.
    "ItemAttribute",
    "item_attribute",

    "Container",
    "Widget",
]


class Widget(Item, metaclass=ABCMeta):
    ...


class Container(Widget, metaclass=ABCMeta):
    def __enter__(self):
        _dearpygui.push_container_stack(self._tag)
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        _dearpygui.pop_container_stack()


    def reset_pos(self) -> None:
        """Sets the item position (`pos`) to it's original position.
        """
        _dearpygui.reset_pos(self.tag)
