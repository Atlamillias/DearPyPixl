from typing import Callable
from abc import ABCMeta, abstractmethod

from dearpypixl.components import Item
from dearpypixl.items.support import (
    EventSupport,
    ThemeSupport,
    StateSupport,
    CommandSupport,
)


class Widget(
    EventSupport,
    ThemeSupport,
    StateSupport,
    CommandSupport,
    Item,
    metaclass=ABCMeta
):
    @abstractmethod
    def _command() -> Callable: ...
