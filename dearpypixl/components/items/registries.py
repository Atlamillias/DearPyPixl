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

    __is_container__ : bool     = True                                                                                                                                                            
    __is_root_item__ : bool     = True                                                                                                                                                            
    __is_value_able__: bool     = False                                                                                                                                                           
    __able_parents__ : tuple    = ()                                                                                                                                                              
    __able_children__: tuple    = ('BoolValue', 'IntValue', 'Int4Value', 'FloatValue', 'Float4Value', 'StringValue', 'DoubleValue', 'Double4Value', 'ColorValue', 'FloatVectValue', 'SeriesValue')
    __commands__     : tuple    = ()                                                                                                                                                              
    __constants__    : tuple    = ('mvValueRegistry',)                                                                                                                                            
    __command__      : Callable = dearpygui.add_value_registry                                                                                                                                    

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

    __is_container__ : bool     = True                                                                      
    __is_root_item__ : bool     = True                                                                      
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ()                                                                        
    __able_children__: tuple    = ('StaticTexture', 'DynamicTexture', 'RawTexture')                         
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvTextureRegistry',)                                                    
    __command__      : Callable = dearpygui.add_texture_registry                                            

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

    __is_container__ : bool     = True                                                                                                                                                                                                              
    __is_root_item__ : bool     = True                                                                                                                                                                                                              
    __is_value_able__: bool     = False                                                                                                                                                                                                             
    __able_parents__ : tuple    = ()                                                                                                                                                                                                                
    __able_children__: tuple    = ('KeyDownHandler', 'KeyPressHandler', 'KeyReleaseHandler', 'MouseMoveHandler', 'MouseWheelHandler', 'MouseClickHandler', 'MouseDoubleClickHandler', 'MouseDownHandler', 'MouseReleaseHandler', 'MouseDragHandler')
    __commands__     : tuple    = ()                                                                                                                                                                                                                
    __constants__    : tuple    = ('mvHandlerRegistry',)                                                                                                                                                                                            
    __command__      : Callable = dearpygui.add_handler_registry                                                                                                                                                                                    

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

    __is_container__ : bool     = True                                                                                                                                                                                                                  
    __is_root_item__ : bool     = True                                                                                                                                                                                                                  
    __is_value_able__: bool     = False                                                                                                                                                                                                                 
    __able_parents__ : tuple    = ()                                                                                                                                                                                                                    
    __able_children__: tuple    = ('ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    __commands__     : tuple    = ()                                                                                                                                                                                                                    
    __constants__    : tuple    = ('mvItemHandlerRegistry',)                                                                                                                                                                                            
    __command__      : Callable = dearpygui.add_item_handler_registry                                                                                                                                                                                   

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

    __is_container__ : bool     = True                                                                      
    __is_root_item__ : bool     = True                                                                      
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ()                                                                        
    __able_children__: tuple    = ('ColorMap',)                                                             
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvColorMapRegistry',)                                                   
    __command__      : Callable = dearpygui.add_colormap_registry                                           

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

    __is_container__ : bool     = True                                                                      
    __is_root_item__ : bool     = True                                                                      
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ()                                                                        
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvTemplateRegistry',)                                                   
    __command__      : Callable = dearpygui.add_template_registry                                           

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

    __is_container__ : bool     = True                                                                      
    __is_root_item__ : bool     = True                                                                      
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ()                                                                        
    __able_children__: tuple    = ('Font',)                                                                 
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvFontRegistry',)                                                       
    __command__      : Callable = dearpygui.add_font_registry                                               

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
