from typing import Any
from dearpygui import dearpygui
from dearpypixl.components.primitives import RegistryItem


__all__ = [
    "ColormapRegistry",
    "TemplateRegistry",
    "TextureRegistry",
    "ValueRegistry",
]


class ColormapRegistry(RegistryItem):
    """Adds a colormap registry.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.add_colormap_registry

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
        self.show = show


class TemplateRegistry(RegistryItem):
    """Adds a template registry.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.add_template_registry


class TextureRegistry(RegistryItem):
    """Adds a dynamic texture.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.add_texture_registry

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
        self.show = show


class ValueRegistry(RegistryItem):
    """Adds a value registry.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.add_value_registry
