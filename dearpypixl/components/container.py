from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Union

from dearpygui import _dearpygui
from dearpygui._dearpygui import (
    get_item_state
)

from dearpypixl.items import Item, ItemAttribute, item_attribute
from dearpypixl.components.support import (
    ContextSupport,
    AddinSupport,
    CommandSupport,
)


__all__ = [
    "Container"
]


class Container(
    ContextSupport,
    AddinSupport,
    CommandSupport,
    Item,
    metaclass=ABCMeta,
):
    @abstractmethod
    def _command() -> Callable: ...

    def reset_pos(self) -> None:
        """Sets the container's position to it's original position upon creation.
        """
        _dearpygui.reset_pos(self.tag)
