from abc import ABCMeta, abstractmethod
from typing import Callable

from dpgwrap._item import Item, ContextSupport
from dpgwidgets import dpg
from dpgwidgets.handler import HandlerSupport
from dpgwidgets.theme import ThemeSupport, Theme


class Widget(Item, ThemeSupport, HandlerSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move_up(self):
        dpg.move_item_up(self.id)

    def move_down(self):
        dpg.move_item_down(self.id)

    def move(self, parent: int, before: int):
        """Move a widget to another <parent> before <before>."""
        dpg.move_item(self.id, parent, before)


class Container(Widget, ContextSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
