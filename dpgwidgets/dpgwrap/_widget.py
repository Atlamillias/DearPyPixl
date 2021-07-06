from abc import ABCMeta, abstractmethod
from typing import Callable

from . import idpg
from ._item import Item, Context
from dpgwidgets.widget import Widget


class Container(Widget, Context, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
