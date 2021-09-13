from typing import Callable, Any, Union

from dearpygui import dearpygui, _dearpygui

import pixle.appitems.containers
from pixle.appitems.containers import *
from pixle.itemtypes import Item
from pixle.itemtypes.container import Container
from pixle.events import ClickedHandler



__all__ = [
    *pixle.appitems.containers.__all__,
    "Popup",
]


class Popup(Window):
    _repr_attrs = ["parent", "button"]

    def __init__(
        self,
        parent: Item,
        button: int = -1,
        modal: bool = False,
        **kwargs,
    ):
        popup = not modal
        super().__init__(
            show=False,
            popup=popup,
            modal=modal,
            min_size=[25, 25],
            autosize=True,
            **kwargs,
        )

        self.__on_click_handler = ClickedHandler(
            parent,
            button,
            callback=self.__on_click_callback
        )

    @property
    def button(self):
        return self.__on_click_handler.button

    @button.setter
    def button(self, value: int):
        self.__on_click_handler.button = value

    @property
    def parent(self):
        return _dearpygui.get_item_info(self.__on_click_handler.id)["parent"]

    def __on_click_callback(self):
        self.configure(show=True)


class StagingContainer(Container):
    """Undocumented function
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
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label

    def __enter__(self):
        _dearpygui.set_staging_mode(True)
        super().__enter__()

    def __exit__(self, exec_type, exec_value, traceback):
        super().__exit__(exec_type, exec_value, traceback)
        _dearpygui.set_staging_mode(False)


class Tooltip(Container):
    """Adds an advanced tool tip for an item. This command must come immediately after the item the tip is for.
    Args:
            parent (Union[int, str]): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.add_tooltip

    def __init__(
        self,
        parent: Union[int, str],
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        show: bool = True,
        **kwargs,
    ):
        super().__init__(
            parent=parent,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.show = show
