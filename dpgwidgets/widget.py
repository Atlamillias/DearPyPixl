from abc import ABCMeta, abstractmethod
from typing import Callable

from . import idpg
from .dpgwrap._item import Item, Context
from .handlers import WidgetHandler


class Widget(Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__handler = WidgetHandler(self)
        self.__theme = None
        self.__disabled_theme = None
        self.__font = None
        

    @property
    def handle(self):
        return self.__handler

    def unhandle(self, handler_type: str, callback: Callable):
        return self.__handler.unhandle(handler_type, callback)

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

    def remove(self):
        """Deletes the widget (and children)."""
        idpg.delete_item(self.__id)

    def configure(self, **config):
        """Updates the widget configuration."""
        idpg.configure_item(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current widget configuration, or
        only <option> if specified."""
        if option:
            return idpg.get_item_configuration(self.__id)[option]

        return idpg.get_item_configuration(self.__id)


class Container(Widget, Context, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
