from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.item import Item, ContextSupport

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
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
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
    """Adds a handler registry.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
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
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **show (bool): Attempt to render widget.
    Returns:
            int
    
    """
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
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
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
