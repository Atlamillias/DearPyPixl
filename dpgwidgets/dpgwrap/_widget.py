from abc import ABCMeta, abstractmethod
from typing import Callable

from . import idpg
from ._item import Item, Context


class Widget(Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move_up(self):
        idpg.move_item_up(self.__id)

    def move_down(self):
        idpg.move_item_down(self.__id)

    def move(self, parent: int, before: int):
        """Move a widget to another <parent> before <before>."""
        idpg.move_item(self.__id, parent, before)

    def refresh(self):
        """Deletes all children in the widget, if any."""
        idpg.delete_item(self.__id, children_only=True)


class Container(Widget, Context, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
