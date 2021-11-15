from typing import Callable
from abc import ABCMeta, abstractmethod

from dearpygui._dearpygui import (
    get_item_state
)

from dearpypixl.items import Item, ItemAttribute
from dearpypixl.components.support import (
    AddinSupport,
    CommandSupport,
)


class Widget(
    AddinSupport,
    CommandSupport,
    Item,
    metaclass=ABCMeta
):
    @abstractmethod
    def _command() -> Callable: ...

