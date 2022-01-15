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
from dearpypixl.components.item import Item
from dearpypixl.components.configuration import ItemAttribute

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "ValueRegistry",
    "TextureRegistry",
    "HandlerRegistry",
    "ItemHandlerRegistry",
    "ColorMapRegistry",
    "TemplateRegistry",
    "FontRegistry",
]


class ValueRegistry(Item):
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                      
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                      
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                      

    _is_container     : bool     = True                                                                                                                                                            
    _is_root_item     : bool     = True                                                                                                                                                            
    _is_value_able    : bool     = False                                                                                                                                                           
    _unique_parents   : tuple    = ()                                                                                                                                                              
    _unique_children  : tuple    = ('BoolValue', 'IntValue', 'Int4Value', 'FloatValue', 'Float4Value', 'StringValue', 'DoubleValue', 'Double4Value', 'ColorValue', 'FloatVectValue', 'SeriesValue')
    _unique_commands  : tuple    = ()                                                                                                                                                              
    _unique_constants : tuple    = ('mvValueRegistry',)                                                                                                                                            
    _command          : Callable = dearpygui.add_value_registry                                                                                                                                    

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class TextureRegistry(Item):
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool     = True                                                                      
    _is_root_item     : bool     = True                                                                      
    _is_value_able    : bool     = False                                                                     
    _unique_parents   : tuple    = ()                                                                        
    _unique_children  : tuple    = ('StaticTexture', 'DynamicTexture', 'RawTexture')                         
    _unique_commands  : tuple    = ()                                                                        
    _unique_constants : tuple    = ('mvTextureRegistry',)                                                    
    _command          : Callable = dearpygui.add_texture_registry                                            

    def __init__(
        self                            ,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = False,
        **kwargs                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class HandlerRegistry(Item):
    """Adds a handler registry.
    
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                        
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                        
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                        
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                        

    _is_container     : bool     = True                                                                                                                                                                                                              
    _is_root_item     : bool     = True                                                                                                                                                                                                              
    _is_value_able    : bool     = False                                                                                                                                                                                                             
    _unique_parents   : tuple    = ()                                                                                                                                                                                                                
    _unique_children  : tuple    = ('KeyDownHandler', 'KeyPressHandler', 'KeyReleaseHandler', 'MouseMoveHandler', 'MouseWheelHandler', 'MouseClickHandler', 'MouseDoubleClickHandler', 'MouseDownHandler', 'MouseReleaseHandler', 'MouseDragHandler')
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                
    _unique_constants : tuple    = ('mvHandlerRegistry',)                                                                                                                                                                                            
    _command          : Callable = dearpygui.add_handler_registry                                                                                                                                                                                    

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class ItemHandlerRegistry(Item):
    """Adds an item handler registry.
    
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                            
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                            
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                            
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                            

    _is_container     : bool     = True                                                                                                                                                                                                                  
    _is_root_item     : bool     = True                                                                                                                                                                                                                  
    _is_value_able    : bool     = False                                                                                                                                                                                                                 
    _unique_parents   : tuple    = ()                                                                                                                                                                                                                    
    _unique_children  : tuple    = ('ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                    
    _unique_constants : tuple    = ('mvItemHandlerRegistry',)                                                                                                                                                                                            
    _command          : Callable = dearpygui.add_item_handler_registry                                                                                                                                                                                   

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class ColorMapRegistry(Item):
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool     = True                                                                      
    _is_root_item     : bool     = True                                                                      
    _is_value_able    : bool     = False                                                                     
    _unique_parents   : tuple    = ()                                                                        
    _unique_children  : tuple    = ('ColorMap',)                                                             
    _unique_commands  : tuple    = ()                                                                        
    _unique_constants : tuple    = ('mvColorMapRegistry',)                                                   
    _command          : Callable = dearpygui.add_colormap_registry                                           

    def __init__(
        self                            ,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = False,
        **kwargs                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class TemplateRegistry(Item):
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool     = True                                                                      
    _is_root_item     : bool     = True                                                                      
    _is_value_able    : bool     = False                                                                     
    _unique_parents   : tuple    = ()                                                                        
    _unique_children  : tuple    = ()                                                                        
    _unique_commands  : tuple    = ()                                                                        
    _unique_constants : tuple    = ('mvTemplateRegistry',)                                                   
    _command          : Callable = dearpygui.add_template_registry                                           

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class FontRegistry(Item):
    """Adds a font registry.
    
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

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool     = True                                                                      
    _is_root_item     : bool     = True                                                                      
    _is_value_able    : bool     = False                                                                     
    _unique_parents   : tuple    = ()                                                                        
    _unique_children  : tuple    = ('Font',)                                                                 
    _unique_commands  : tuple    = ()                                                                        
    _unique_constants : tuple    = ('mvFontRegistry',)                                                       
    _command          : Callable = dearpygui.add_font_registry                                               

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
