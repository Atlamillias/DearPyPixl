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


class Widget(
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    ItemMethodSupport,
    Item,
    metaclass=ABCMeta
    ):
    @abstractmethod
    def _command() -> Callable: ...
