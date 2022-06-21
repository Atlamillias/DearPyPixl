from typing import Callable, Any
from time import sleep

from dearpygui import _dearpygui

import dearpypixl.appitems.containers
from dearpypixl.appitems.containers import *
from dearpypixl.itemtypes import Widget, ItemEvents, ItemProperty, CONFIG, INFORM, STATES, WidgetT
from dearpypixl.components.handlers import (
    ClickedHandler,
    HoverHandler,
    VisibleHandler
)
from dearpypixl.constants import Mouse

__all__ = [
    *dearpypixl.appitems.containers.__all__,
    "Popup",
]


##########################
######## Rewrites ########
##########################
class Tooltip(Window):
    """A tooltip window that is displayed only when its target item is
    hovered.
    """
    # x_offset = ItemProperty.register("x_offset", category="configuration")
    # y_offset = ItemProperty.register("y_offset", category="configuration")
    # delay    = ItemProperty.register("delay"   , category="configuration")

    # BUG: Focus is dropped on the currently (previously?) focused item
    # when this item is displayed. Also, this item does not display above
    # all other items when it is not focused. Awaiting DPG update.
    def __init__(
        self,
        target  : WidgetT = None,
        delay   : int      = 0,
        x_offset: int      = 25,
        y_offset: int      = 0,
        **kwargs,
    ):
        """Args:
            * target (Widget, optional): the item that causes this
        item to be shown when hovered. Defaults to None.
            * delay (int, optional): the time (milliseconds) between the hovering the
        target and showing the item.
            * x_offset (int, optional): the horizontal distance (pixels) between the
        cursor and the position of the item when displayed. Defaults to 25.
            * y_offset (int, optional): the vertical distance (pixels) between the
        cursor and the position of the item when displayed. Defaults to 0.
        """
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
        self.__target              : WidgetT     = None
        self.__target_uuid         : int          = None
        self.__target_hover_handler: HoverHandler = None
        # This is only used if a delay is needed.
        self.__target_is_hovered   : bool         = False

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.delay    = delay
        self.target   = target

    @property
    @ItemProperty.register(category=CONFIG)
    def target(self) -> WidgetT | None:
        """The item that, when hovered, will cause this item to display.
        """
        return self.__target
    @target.setter
    def target(self, value: WidgetT | None):
        if not isinstance(value, Widget) and value is not None:
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

    """
    def __init__(
        self,
        target: WidgetT | None = None,
        button: Mouse | int        = Mouse.ANY,
        modal : bool               = False,
        **kwargs,
    ):
        """Args:
            * target (Container, Widget): the item that causes this item to
        be displayed when clicked.
            * button (int, optional): the mouse button that must be clicked to
        display this item. Defaults to -1 (all/any).
            * modal (bool, optional): if True, all other items in the interface
        are disabled until the popup is closed. Defaults to False.
        """
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
    @ItemProperty.register(category=CONFIG)
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
    @ItemProperty.register(category=CONFIG)
    def target(self) -> WidgetT | None:
        """The item that, when clicked, will cause this item to display.
        """
        return self.__target
    @target.setter
    def target(self, value: WidgetT | None) -> None:
        if not isinstance(value, Widget) and value is not None:
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
