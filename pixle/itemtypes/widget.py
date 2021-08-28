from __future__ import annotations
from typing import Callable
from abc import ABCMeta, abstractmethod

from pixle.itemtypes import Item
from pixle.itemtypes.support import (
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    ItemMethodSupport,
)


_WIDGET_MIXINS = (
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    ItemMethodSupport,
)

class Widget(*_WIDGET_MIXINS, Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
