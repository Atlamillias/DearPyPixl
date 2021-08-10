from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any
import re
import inspect

from dearpygui import _dearpygui as idpg, dearpygui

from dpgwidgets.item import Item, ContextSupport
from dpgwidgets.handler import HandlerSupport
from dpgwidgets.theme import ThemeSupport


class Widget(Item, ThemeSupport, HandlerSupport, metaclass=ABCMeta):
    """Base class for all high-level items. Supports themes and
    handlers. Should not be instantiated directly.
    """
    __value = None

    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def focus(self):
        """Brings the widget into focus.
        """
        idpg.focus_item(self.id)

    def move_up(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it. Nothing happens if the widget
        is not a child or if there is no preceding item.
        """
        try:
            idpg.move_item_up(self.id)
        except SystemError:
            pass

    def move_down(self) -> None:
        """If the widget is a child, it is placed above the item
        that immediately precedes it. Nothing happens if the widget
        is not a child or if there is no preceding item.
        """
        try:
            idpg.move_item_down(self.id)
        except SystemError:
            pass

    def move(self, parent: int, before: int = 0) -> None:
        """If the widget is a child, it will be moved to another
        parent and placed above/before another item.

        Args:
            parent (int): id of the new parent.
            before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        try:
            idpg.move_item(self.id, parent, before)
        except SystemError:
            pass


    ## Value ##
    def set_value(self, value: Any):
        """Sets the value of a widget.

        NOTE: A SystemError should be thrown if the widget
        isn't capable of having a value set on it. But it
        is currently supressed internally. If you try
        setting a value, but the value doesn't "stick", 
        """
        idpg.set_value(self.id, value)

    @property
    def value(self) -> Any:
        """Return the widget value (if any).
        """
        # See setter comments.
        if self.__value:
            return self.value
 
        return idpg.get_value(self.id)

    @value.setter
    def value(self, value: Any):
        try:
            idpg.set_value(self.id, value)
        # A SystemError should be thrown if the widget
        # isn't capable of having a value set on it.
        except SystemError:
            self.__value = value
        # 2021-08-06 - The error is being supressed internally,
        # so the `except` code will never actually run. As a
        # workaround, we check to see if the value "sticks".
        if idpg.get_value(self.id) != value:
            self.__value

    ## Info ##
    @property
    def is_container(self) -> bool:
        """Checks if the widget is a container item.
        """
        return idpg.get_item_info(self.id)["container"]

    ## States ##
    @property
    def is_hovered(self) -> bool:
        return idpg.get_item_state(self.id)["hovered"]

    @property
    def is_active(self) -> bool:
        return idpg.get_item_state(self.id)["active"]

    @property
    def is_focused(self) -> bool:
        return idpg.get_item_state(self.id)["focused"]

    @property
    def is_clicked(self) -> bool:
        return idpg.get_item_state(self.id)["clicked"]

    @property
    def is_visible(self) -> bool:
        return idpg.get_item_state(self.id)["visible"]

    @property
    def is_edited(self) -> bool:
        return idpg.get_item_state(self.id)["edited"]

    @property
    def is_activated(self) -> bool:
        return idpg.get_item_state(self.id)["activated"]

    @property
    def is_deactivated(self) -> bool:
        return idpg.get_item_state(self.id)["deactivated"]

    @property
    def is_deactivated_after_edit(self) -> bool:
        return idpg.get_item_state(self.id)["deactivated_after_edit"]

    @property
    def is_toggled_open(self) -> bool:
        return idpg.get_item_state(self.id)["toggled_open"]

    @property
    def is_ok(self) -> bool:
        return idpg.get_item_state(self.id)["ok"]

    ## Misc ##
    def duplicate(self, **config) -> Widget:
        """ (WIP) Creates and returns a "shallow" copy of the widget. The
        configuration can be altered by passing configuration options
        and values.

        NOTE: In development. Handlers currently aren't duplicated in
        this process, and may also exclude some widgets. Currently
        only duplicates one level of "depth" for children.

        Args:
            config (optional): configuration options and values 
            that will overwrite the duplicated configuration.
        """ 
        parameters = [p.name for p in
                      inspect.signature(type(self)).parameters.values()]
        config = self.configuration() | config
        config = {optn: val for optn, val in config.items() if
                  optn in parameters}
        copy_parent = type(self)(**config)
        if self.theme:
            copy_parent.theme = self.theme
        # We don't have access to Python references to know if the
        # children are wrapped, so the internal API needs to be used.
        capwords = re.compile(r'[A-Z][^A-Z]*')
        children = idpg.get_item_info(self.id)["children"]
        children = [*children[1], *children[2]]
        for child_id in children:
            child_info = idpg.get_item_info(child_id)
            child_config = idpg.get_item_configuration(child_id)
            child_config["parent"] = copy_parent.id

            # determining and trying to create item
            item_type = child_info["type"].split("::")[-1].replace("AppItem","")
            item_type = re.findall(capwords, item_type)
            item_type = "add_" + "_".join((w.lower() for w in item_type)).rstrip("_")

            if command := getattr(dearpygui, item_type):
                parameters = [p.name for p in
                              inspect.signature(command).parameters.values()]
                cmd_params = {optn:val for optn, val in child_config.items() if
                              optn in parameters}
                c_child_id = command(**cmd_params)
                if theme_info := child_info.get("theme", None):
                    dearpygui.set_item_theme(c_child_id, theme_info)
                if dtheme_info := child_info.get("disabled_theme", None):
                     dearpygui.set_item_disabled_theme(c_child_id, dtheme_info)
                if font_info := child_info.get("font", None):
                    dearpygui.set_item_font(c_child_id, font_info)        

        return copy_parent

class Container(Widget, ContextSupport, metaclass=ABCMeta):
    """Base class for all high-level container items. Supports themes
    and handlers. Should not be instantiated directly.
    """
    @abstractmethod
    def _command() -> Callable: ...

    def reset_pos(self) -> None:
        """Sets the container's position to the default.
        """
        idpg.reset_pos(self.id)

    def renew(self) -> None:
        """Deletes all children in the widget, if any.
        """
        idpg.delete_item(self.id, children_only=True)

    def children(self) -> list[int]:
        """Returns a list containing the id of all *high-level children
        within a container.

        *Slots 1 and 2 in idpg.get_item_children(self.id, slot)
        """
        return [child for slot, childs in
                idpg.get_item_children(self.id, -1).items()
                for child in childs
                if any(slot == i for i in (1, 2))]


    # x_scroll
    @property
    def y_scroll_pos(self):
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return idpg.get_y_scroll(self.id)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        idpg.set_y_scroll(self.id, value)

    @property
    def y_scroll_max(self):
        """Maximum vertical scroll position.
        """
        return idpg.get_y_scroll_max(self.id)


    # y_scroll
    @property
    def x_scroll_pos(self):
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return idpg.get_x_scroll(self.id)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return idpg.set_x_scroll(self.id, value)

    @property
    def x_scroll_max(self):
        """Maximum horizontal scroll position.
        """
        return idpg.get_x_scroll_max(self.id)


