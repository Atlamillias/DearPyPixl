from __future__ import annotations
from typing import Callable
from abc import ABCMeta, abstractmethod

from dearpypixl.item import Item
from dearpypixl.item.support import (
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    CommandSupport,
)


class Widget(
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    CommandSupport,
    Item,
    metaclass=ABCMeta
    ):
    @abstractmethod
    def _command() -> Callable: ...
