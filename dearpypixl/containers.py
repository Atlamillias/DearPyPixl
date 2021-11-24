from typing import Union
from time import sleep

from dearpygui import _dearpygui

import dearpypixl.appitems.containers
from dearpypixl.appitems.containers import *
from dearpypixl.components import Container, Widget, ItemEvents, item_attribute, ItemAttribute, ContainerItemT, AppItemT
from dearpypixl.components.handlers import (
    ClickedHandler,
    HoverHandler,
    VisibleHandler
)
from dearpypixl.constants import Key, Mouse


__all__ = [
    *dearpypixl.appitems.containers.__all__,
    "Popup",
]


##########################
######## Rewrites ########
##########################
class Tooltip(Window):
    x_offset = item_attribute("x_offset", category="configuration")
    y_offset = item_attribute("y_offset", category="configuration")
    delay    = item_attribute("delay"   , category="configuration")

    """A tooltip window that is displayed only when its target item is
    hovered.

    Args:
        * target (Union[Container, Widget], optional): the item that causes this
        item to be shown when hovered. Defaults to None.
        * delay (int, optional): the time (milliseconds) between the hovering the
        target and showing the item.
        * x_offset (int, optional): the horizontal distance (pixels) between the
        cursor and the position of the item when displayed. Defaults to 25.
        * y_offset (int, optional): the vertical distance (pixels) between the
        cursor and the position of the item when displayed. Defaults to 0.

    Returns:
        *Tooltip*
    """
    # BUG: Focus is dropped on the currently (previously?) focused item
    # when this item is displayed. Also, this item does not display above
    # all other items when it is not focused. Awaiting DPG update.
    def __init__(
        self,
        target  : AppItemT = None,
        delay   : int      = 0,
        x_offset: int      = 25,
        y_offset: int      = 0,
        **kwargs,
    ):
        super().__init__(
            autosize=True,
            min_size=[10, 10],
            no_title_bar=True,
            no_resize=False,
            no_close=True,
            no_collapse=True,
            no_move=True,
            show=False,
            events=ItemEvents(),
            **kwargs,
        )
        VisibleHandler(parent=self.events, callback=self.__call_on_visible)
        self.__target              : AppItemT     = None
        self.__target_uuid         : int          = None
        self.__target_hover_handler: HoverHandler = None
        # This is only used if a delay is needed.
        self.__target_is_hovered   : bool         = False

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.delay    = delay
        self.target   = target

    @property
    @item_attribute(category="configuration")
    def target(self) -> Union[AppItemT, None]:
        """The item that, when hovered, will cause this item to display.
        """
        return self.__target
    @target.setter
    def target(self, value: Union[AppItemT, None]):
        if not isinstance(value, (Widget, None)):
            raise TypeError(f"`target` must `Widget` or `None` type (got {type(value).__qualname__!r}).")
        elif value and not hasattr(value, "is_hovered"):
            raise ValueError(f"`target` is unsupported: {type(value).__qualname__!r} does not have `is_hovered` state.")

        self.__target            = value
        self.__target_is_hovered = False
        if self.__target_uuid:
            self.__target_hover_handler.delete()
            self.__target_hover_handler = None

        if value is None:
            self.__target_uuid = None
            return None

        if not value.events:
            value.events = ItemEvents()
        self.__target_uuid          = value._tag
        self.__target_hover_handler = HoverHandler(
            parent  =value.events,
            callback=self.__call_on_target_hover
        )

    def __call_on_target_hover(self, *callback_args):
        # If the target was not being hovered prior to this call,
        # add the delay.
        if not self.__target_is_hovered and self.delay != 0:
            self.__target_is_hovered = True
            sleep(self.delay / 1000)

        mouse_x, mouse_y = _dearpygui.get_mouse_pos(local=False)
        self.pos = mouse_x + self.x_offset, mouse_y + self.y_offset
        self.show = True

    def __call_on_visible(self, *callback_args):
        # Hide the item if the target is no longer being hovered and
        # reset the `target_is_hovered` state.
        if self.target and not self.target.is_hovered:
            self.show = False
            self.__target_is_hovered = False
            pass


class Popup(Window):
    """A popup window that is displayed only when its target item is
    clicked. It hides when anything other than itself is clicked.


    Args:
        * target (Container, Widget): the item that causes this item to
        be displayed when clicked.
        * button (int, optional): the mouse button that must be clicked to
        display this item. Defaults to -1 (all/any).
        * modal (bool, optional): if True, all other items in the interface
        are disabled until the popup is closed. Defaults to False.

    Returns:
        *Popup*
    """
    def __init__(
        self,
        target: Union[AppItemT, None] = None,
        button: Union[Mouse, int]     = Mouse.ANY,
        modal : bool                  = False,
        **kwargs,
    ):
        popup = not modal
        super().__init__(
            autosize=True,
            min_size=[25, 25],
            modal=modal,
            popup=popup,
            show=False,
            **kwargs,
        )
        self.__target_uuid          = None
        self.__target               = None
        self.__button               = None
        self.__target_click_handler = None

        self.button = button
        self.target = target

    @property
    @item_attribute(category="configuration")
    def button(self) -> int:
        """The mouse button that must be clicked to display this item.
        """
        return self.__button
    @button.setter
    def button(self, value: int) -> None:
        self.__button = int(value)
        if self.__target_click_handler:
            self.__target_click_handler.button = value
            
    @property
    @item_attribute(category="configuration")
    def target(self) -> Union[AppItemT, None]:
        """The item that, when clicked, will cause this item to display.
        """
        return self.__target
    @target.setter
    def target(self, value: Union[AppItemT, None]) -> None:
        if not isinstance(value, (Widget, None)):
            raise TypeError(f"`target` must `Widget` or `None` type (got {type(value).__qualname__!r}).")
        elif value and not hasattr(value, "is_clicked"):
            raise ValueError(f"`target` is unsupported: {type(value).__qualname__!r} does not have `is_clicked` state.")

        self.__target = value
        if self.__target_uuid:
            self.__target_click_handler.delete()
            self.__target_click_handler = None

        if value is None:
            self.__target_uuid = None
            return None

        if not value.events:
            value.events = ItemEvents()
        self.__target_uuid = value._tag
        self.__target_click_handler = ClickedHandler(
                parent=value.events,
                button=self.__button,
                callback=self.__on_click_callback
        )

    def __on_click_callback(self):
        self.configure(show=True)



##########################
####### Extensions #######
##########################
class Window(Window):
    def __init__(self, on_close = None, **kwargs):
        self._call_on_close = []
        super().__init__(on_close=self.__on_close, **kwargs)

    def __on_close(self):
        return [f() for f in self._call_on_close]

    @property
    @item_attribute(category="information")
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        _dearpygui.set_y_scroll(self.tag, value)


    @property
    @item_attribute(category="information")
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return _dearpygui.get_y_scroll_max(self.tag)


    @property
    @item_attribute(category="information")
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return _dearpygui.set_x_scroll(self.tag, value)


    @property
    @item_attribute(category="information")
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return _dearpygui.get_x_scroll_max(self.tag)


class ChildWindow(ChildWindow):
    # Scroll position
    @property
    @item_attribute(category="information")
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        _dearpygui.set_y_scroll(self.tag, value)


    @property
    @item_attribute(category="information")
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return _dearpygui.get_y_scroll_max(self.tag)


    @property
    @item_attribute(category="information")
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return _dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return _dearpygui.set_x_scroll(self.tag, value)


    @property
    @item_attribute(category="information")
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return _dearpygui.get_x_scroll_max(self.tag)



class TabBar(TabBar):
    # Allows the active tab to be selected programatically through the
    # tab bar and tabs themselves.
    @property
    @item_attribute(category="information")
    def active_tab(self) -> Tab:
        """The currently selected tab.
        """
        active_tab_id = _dearpygui.get_value(self.tag)
        if active_tab_id == 0 and (childs := self.children()):
            return childs[0]
        return self._raw_items.get(active_tab_id, active_tab_id)
    @active_tab.setter
    def active_tab(self, value: Tab):
        _dearpygui.set_value(self.tag, value.tag)


class Tab(Tab):
    # Allows the active tab to be selected programatically through the
    # tab bar and tabs themselves.
    @property
    @item_attribute(category="state")
    def is_active_tab(self) -> bool:
        """If this item is currently the active/selected tab within its parent
        this returns True. Otherwise, this returns False.
        """
        try:
            return True if self == self.parent.active_tab else False
        # Tab is likely staged if it exists without a parent...
        except SystemError:
            return False

    def set_as_active(self) -> None:
        """Sets this tab item as the currently active/selected tab within its parent.
        """
        self.parent.active_tab = self
