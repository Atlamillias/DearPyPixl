from typing import Callable, Any

import dearpygui._dearpygui as idpg

import pixle.appitems.containers
from pixle.appitems.containers import *
from pixle.itemtypes import Item
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
        return idpg.get_item_info(self.__on_click_handler.id)["parent"]

    def __on_click_callback(self):
        self.configure(show=True)
