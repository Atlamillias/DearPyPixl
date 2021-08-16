from typing import (
    Any,
    Callable,
    Union,
    Dict,
    Tuple,
    Set,
    List,
)
import dearpygui.dearpygui
from dpgwidgets.item import Item, ContextSupport

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "ColormapRegistry",
    "FontRegistry",
    "HandlerRegistry",
    "TextureRegistry",
    "ValueRegistry",
]


class ColormapRegistry(Item, ContextSupport):
    """Adds a colormap registry.
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_colormap_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = False, 
        **kwargs, 
    ):
        super().__init__(
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


class FontRegistry(Item, ContextSupport):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_font_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
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


class HandlerRegistry(Item, ContextSupport):
    """Adds a handler registry.
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_handler_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
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


class TextureRegistry(Item, ContextSupport):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_texture_registry

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = False, 
        **kwargs, 
    ):
        super().__init__(
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


class ValueRegistry(Item, ContextSupport):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_value_registry

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
