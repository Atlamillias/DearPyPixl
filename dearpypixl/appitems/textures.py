from typing import (
    Callable,
    Any,
    Union,
    Dict,
    Tuple,
    Set,
    List,
)
from dearpygui import dearpygui
from dearpypixl.components import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "StaticTexture",
    "DynamicTexture",
    "RawTexture",
]


class StaticTexture(Widget):
    """Adds a static texture.
    
        Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float, ...]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
        Returns:
            Union[int, str]
    """

    width             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('Stage', 'TemplateRegistry', 'TextureRegistry')                                   
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvStaticTexture',)                                                               
    _command          : Callable                              = dearpygui.add_static_texture                                                       

    def __init__(
        self                                                           ,
        width             : int                                        ,
        height            : int                                        ,
        default_value     : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 12  ,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class DynamicTexture(Widget):
    """Adds a dynamic texture.
    
        Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float, ...]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
        Returns:
            Union[int, str]
    """

    width             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('Stage', 'TemplateRegistry', 'TextureRegistry')                                   
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvDynamicTexture',)                                                              
    _command          : Callable                              = dearpygui.add_dynamic_texture                                                      

    def __init__(
        self                                                           ,
        width             : int                                        ,
        height            : int                                        ,
        default_value     : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 12  ,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class RawTexture(Widget):
    """Adds a raw texture.
    
        Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float, ...]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            format (int, optional): Data format.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
        Returns:
            Union[int, str]
    """

    width             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    format            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = False                                                                              
    _unique_parents   : tuple                                 = ('Stage', 'TemplateRegistry', 'TextureRegistry')                                   
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvRawTexture', 'mvFormat_Float_rgba', 'mvFormat_Float_rgb')                      
    _command          : Callable                              = dearpygui.add_raw_texture                                                          

    def __init__(
        self                                                           ,
        width             : int                                        ,
        height            : int                                        ,
        default_value     : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        format            : int                                  = 0   ,
        parent            : Union[int, str]                      = 12  ,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            format=format,
            parent=parent,
            **kwargs,
        )
