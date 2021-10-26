from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Union
from dearpygui import _dearpygui
from dearpypixl.components import Item, configuration_override, information_override
from dearpypixl.items.support import(
    ContextSupport,
    ThemeSupport,
    EventSupport,
    StateSupport,
    CommandSupport,
)

__all__ = [
    "Container"
]


class Container(
    ThemeSupport,
    EventSupport,
    StateSupport,
    CommandSupport,
    ContextSupport,
    Item,
    metaclass=ABCMeta,
):
    @abstractmethod
    def _command() -> Callable: ...

    def reset_pos(self) -> None:
        """Sets the container's position to it's original position upon creation.
        """
        _dearpygui.reset_pos(self.tag)

    @property
    @information_override
    def is_root_item(self) -> bool:
        """Checks if the item is a top-level container.
        """
        # This container item won't have a parent if True.
        if not _dearpygui.get_item_info(self._tag)["parent"]:
            return True
        return False

    # Scroll position
    @property
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_y_scroll(self.tag)

    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        _dearpygui.set_y_scroll(self.tag, value)

    @property
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return _dearpygui.get_y_scroll_max(self.tag)

    @property
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_x_scroll(self.tag)

    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return _dearpygui.set_x_scroll(self.tag, value)

    @property
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return _dearpygui.get_x_scroll_max(self.tag)
