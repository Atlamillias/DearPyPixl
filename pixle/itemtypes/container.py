from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable
from dearpygui import _dearpygui as idpg

from pixle.itemtypes import Item
from pixle.itemtypes.support import(
    ContextSupport,
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    ItemMethodSupport,
)


class Container(
    EventItemSupport,
    ThemeSupport,
    StateSupport,
    ItemMethodSupport,
    ContextSupport,
    Item,
    metaclass=ABCMeta,
    ):
    @abstractmethod
    def _command() -> Callable: ...

    def reset_pos(self) -> None:
        """Sets the container's position to the default.
        """
        idpg.reset_pos(self.id)

    def renew(self) -> None:
        """Deletes all children in the widget, if any.
        """
        idpg.delete_item(self._id, children_only=True)

    @property
    def is_top_level(self) -> bool:
        """Checks if the item is a top-level container.
        """
        # If the
        if not idpg.get_item_info(self._id)["parent"]:
            return True
        return False

    # Scroll position
    @property
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return idpg.get_y_scroll(self.id)

    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        idpg.set_y_scroll(self.id, value)

    @property
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return idpg.get_y_scroll_max(self.id)

    @property
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return idpg.get_x_scroll(self.id)

    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return idpg.set_x_scroll(self.id, value)

    @property
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return idpg.get_x_scroll_max(self.id)
