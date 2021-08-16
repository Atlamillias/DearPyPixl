from typing import Callable, Any

import dearpygui._dearpygui as idpg

import dpgwidgets.libsrc.containers
from dpgwidgets.libsrc.containers import *
from dpgwidgets.libsrc.handlers import ClickedHandler as _ClickedHandler
from dpgwidgets.constants import ItemType, AppItemType


__all__ = [
    *dpgwidgets.libsrc.containers.__all__,
    "Popup",
    ]


class Popup(Window):
    _repr_attrs = ["parent", "button"]

    def __init__(
        self,
        parent: AppItemType,
        button: int = -1,
        modal: bool = False,
        **kwargs,
    ):
        popup = not modal
        super().__init__(
            show=False,
            popup=popup,
            modal=modal,
            min_size=[25,25],
            autosize=True,
            **kwargs,
        )

        self.__on_click_handler = _ClickedHandler(
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
        return idpg.get_item_info(self.__on_click_handler.id)["parent"]


    def __on_click_callback(self):
        self.configure(show=True)



    
