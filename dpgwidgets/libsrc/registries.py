from typing import Any, Callable
import dearpygui.dearpygui
from item import Item, ContextSupport

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "FontRegistry",
    "HandlerRegistry",
    "TextureRegistry",
    "ValueRegistry",
]


class FontRegistry(Item, ContextSupport):
    _command = dearpygui.dearpygui.add_font_registry

    def __init__(
        self, 
        label: str = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.show = show
        self.user_data = user_data


class HandlerRegistry(Item, ContextSupport):
    _command = dearpygui.dearpygui.add_handler_registry

    def __init__(
        self, 
        label: str = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.show = show
        self.user_data = user_data


class TextureRegistry(Item, ContextSupport):
    _command = dearpygui.dearpygui.add_texture_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        show: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.show = show


class ValueRegistry(Item, ContextSupport):
    _command = dearpygui.dearpygui.add_value_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
