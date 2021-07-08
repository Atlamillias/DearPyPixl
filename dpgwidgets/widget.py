from abc import ABCMeta, abstractmethod
from typing import Callable

from dearpygui import core as idpg
from .dpgwrap._item import Item, Context
from .handler import WidgetHandler
from .theme import WidgetTheme


class Widget(Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__handler = WidgetHandler(self)
        self.__theme = WidgetTheme(self)
        self.__disabled_theme = WidgetTheme(self, is_disabled_theme=True)
        self.__font = None
        
        
    # WidgetHandler
    @property
    def handle(self):
        return self.__handler

    def unhandle(self, handler_type: str, callback: Callable):
        return self.__handler.unhandle(handler_type, callback)


    # WidgetTheme
    @property
    def theme(self):
        return self.__theme
    
    @property
    def color(self):
        return self.__theme.color

    @property
    def style(self):
        return self.__theme.style
    
    @property
    def d_theme(self):
        return self.__disabled_theme

    @property
    def d_color(self):
        return self.__disabled_theme.color

    @property
    def d_style(self):
        return self.__disabled_theme.style


    # Misc
    def move_up(self):
        idpg.move_item_up(self.id)

    def move_down(self):
        idpg.move_item_down(self.id)

    def move(self, parent: int, before: int):
        """Move a widget to another <parent> before <before>."""
        idpg.move_item(self.id, parent, before)


class Container(Widget, Context, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
