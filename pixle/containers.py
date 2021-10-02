from typing import Callable, Any, Union
from time import sleep

from dearpygui import dearpygui, _dearpygui

import pixle.appitems.containers
from pixle.appitems.containers import *
from pixle.itemtypes import Item
from pixle.itemtypes.container import Container
from pixle.itemtypes.widget import Widget
from pixle.events import ClickedHandler, HoverHandler, VisibleHandler

__all__ = [
    *pixle.appitems.containers.__all__,
    "Popup",
]


##########################
### Rewrites/homebrew ####
##########################
class Tooltip(Window):
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
    # NOTE: Current bug where focus is lost on the currently focused item
    # when this item is displayed. Also, this item does not display above
    # all other items when it is not focused...
    def __init__(
        self,
        target: Union[Container, Widget] = None,
        delay: int = 0,
        x_offset: int = 25,
        y_offset: int = 0,
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
            **kwargs,
        )
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.__target = None
        self.__delay = delay

        self.__on_hover_handler = None
        self.__is_hovering = False
        VisibleHandler(parent=self, callback=self.__on_visible_callback, untrack=True)

        if target:
            self.target = target

    @property
    def target(self) -> Union[Container, Widget]:
        """The item that will cause this item to be displayed when hovered.
        """
        return self.__target
    @target.setter
    def target(self, value: Union[Container, Widget]):
        self.__target = value

        if self.__on_hover_handler:
            self.__on_hover_handler.delete()
        # Avoid creating a new handler if value is None
        if value is not None:
            self.__on_hover_handler = HoverHandler(
                parent=value,
                callback=self.__on_hover_callback,
                untrack=True,
            )

    @property
    def delay(self) -> int:
        """The time (milliseconds) between the hovering the target and showing
        the item.
        """
        return self.__delay
    @delay.setter
    def delay(self, value: int) -> None:
        self.__delay = value

    def __on_hover_callback(self, *args):
        # If the target was not being hovered prior to this call,
        # add the delay.
        delay = self.__delay
        if not self.__is_hovering and delay != 0:
            self.__is_hovering = True
            sleep(delay / 1000)

        mouse_x, mouse_y = _dearpygui.get_mouse_pos(local=False)
        self.pos = mouse_x + self.x_offset, mouse_y + self.y_offset
        self.show = True

    def __on_visible_callback(self, *args):
        # Hide the item if the target is no longer being hovered and
        # reset the is_hovering state.
        if self.target and not self.target.is_hovered:
            self.show = False
            self.__is_hovering = False
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
        target: Union[Container, Widget],
        button: int = -1,
        modal: bool = False,
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
        self.__target = None
        self.__button = button
        self.__on_click_handler = None

        if target:
            self.target = target

    @property
    def button(self) -> int:
        """The mouse button that must be clicked to display this item.
        """
        return self.__button
    @button.setter
    def button(self, value: int) -> None:
        self.__button = value
        if self.__on_click_handler:
            self.__on_click_handler.button = value
            
    @property
    def target(self) -> Union[Container, Widget]:
        """The item that will cause this item to be displayed when clicked.
        """
        return self.__target
    @target.setter
    def target(self, value: Union[Container, Widget]) -> None:
        self.__target = value
        if self.__on_click_handler:
            self.__on_click_handler.delete()
        # Avoid creating a new handler if value is None
        if value is not None:
            self.__on_click_handler = ClickedHandler(
                parent=value,
                button=self.__button,
                callback=self.__on_click_callback
            )

    def __on_click_callback(self):
        self.configure(show=True)


class Test_Stage(Container):
    """A container that automatically sets staging mode for all items it parents.
    When its `unstage` method is called, all children are placed into the parent
    in the current context. For example, calling `unstage` in the scope of
    `with Window() as window:` will cause "window" to parent all of the staging
    container's children.


    Args:
        **label (str): Overrides 'name' as label.
        **user_data (Any): User data for callbacks.
        **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
        **id (Union[int, str]): Unique id used to programmatically refer to the item. If label is unused this will be the label.

    Returns:
        Union[int, str]
    
    """
    _command = dearpygui.add_staging_container

    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        **kwargs,
    ):
        _dearpygui.set_staging_mode(True)
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        _dearpygui.set_staging_mode(False)

    def __enter__(self):
        _dearpygui.set_staging_mode(True)
        super().__enter__()
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        super().__exit__(exec_type, exec_value, traceback)
        _dearpygui.set_staging_mode(False)


##########################
########## Tabs ##########
##########################
class TabBar(TabBar):
    @property
    def active_tab(self) -> Tab:
        """The currently selected tab.
        """
        active_tab_id = _dearpygui.get_value(self.tag)
        if active_tab_id == 0 and (childs := self.children()):
            return childs[0]
        return self.APPITEMS.get(active_tab_id, active_tab_id)

    @active_tab.setter
    def active_tab(self, value: Tab):
        _dearpygui.set_value(self.tag, value.tag)


class Tab(Tab):
    @property
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




##########################
#### Work-in-progress ####
##########################

