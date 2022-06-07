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
from dearpypixl.components.item import Item, ItemAttribute

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Font",
    "FontChars",
    "FontRange",
    "FontRangeHint",
    "CharRemap",
]


class Font(Item):
    """Adds font to a font registry.
    
    	Args:
    		file (str): 
    		size (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    		default_font (bool, optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    file              : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    size              : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  

    __is_container__ : bool     = True                                                                        
    __is_root_item__ : bool     = False                                                                       
    __is_value_able__: bool     = False                                                                       
    __able_parents__ : tuple    = ('FontRegistry',)                                                           
    __able_children__: tuple    = ('FontChars', 'FontRange', 'CharRemap', 'FontRangeHint', 'TemplateRegistry')
    __commands__     : tuple    = ('bind_font', 'get_text_size')                                              
    __constants__    : tuple    = ('mvFont',)                                                                 
    __command__      : Callable = dearpygui.add_font                                                          

    def __init__(
        self                                      ,
        file              : str                   ,
        size              : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 10  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            file=file,
            size=size,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontChars(Item):
    """Adds specific font characters to a font.
    
    	Args:
    		chars (Union[List[int], Tuple[int, ...]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    chars             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool                              = False                                                                     
    __is_root_item__ : bool                              = False                                                                     
    __is_value_able__: bool                              = False                                                                     
    __able_parents__ : tuple                             = ('Font', 'TemplateRegistry')                                              
    __able_children__: tuple                             = ()                                                                        
    __commands__     : tuple                             = ()                                                                        
    __constants__    : tuple                             = ('mvFontChars',)                                                          
    __command__      : Callable                          = dearpygui.add_font_chars                                                  

    def __init__(
        self                                                       ,
        chars             : Union[List[int], Tuple[int, ...]]      ,
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Union[int, str]                  = 0   ,
        **kwargs                                                   ,
    ) -> None:
        super().__init__(
            chars=chars,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontRange(Item):
    """Adds a range of font characters to a font.
    
    	Args:
    		first_char (int): 
    		last_char (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    first_char        : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    last_char         : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Font', 'TemplateRegistry')                                              
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvFontRange',)                                                          
    __command__      : Callable = dearpygui.add_font_range                                                  

    def __init__(
        self                                      ,
        first_char        : int                   ,
        last_char         : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            first_char=first_char,
            last_char=last_char,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontRangeHint(Item):
    """Adds a range of font characters (mvFontRangeHint_ constants).
    
    	Args:
    		hint (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    hint             : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                     

    __is_container__ : bool     = False                                                                                                                                                                                                                                                              
    __is_root_item__ : bool     = False                                                                                                                                                                                                                                                              
    __is_value_able__: bool     = False                                                                                                                                                                                                                                                              
    __able_parents__ : tuple    = ('Font', 'TemplateRegistry')                                                                                                                                                                                                                                       
    __able_children__: tuple    = ()                                                                                                                                                                                                                                                                 
    __commands__     : tuple    = ()                                                                                                                                                                                                                                                                 
    __constants__    : tuple    = ('mvFontRangeHint', 'mvFontRangeHint_Default', 'mvFontRangeHint_Japanese', 'mvFontRangeHint_Korean', 'mvFontRangeHint_Chinese_Full', 'mvFontRangeHint_Chinese_Simplified_Common', 'mvFontRangeHint_Cyrillic', 'mvFontRangeHint_Thai', 'mvFontRangeHint_Vietnamese')
    __command__      : Callable = dearpygui.add_font_range_hint                                                                                                                                                                                                                                      

    def __init__(
        self                                      ,
        hint              : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            hint=hint,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class CharRemap(Item):
    """Remaps a character.
    
    	Args:
    		source (int): 
    		target (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    source            : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    target            : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Font', 'TemplateRegistry')                                              
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvCharRemap',)                                                          
    __command__      : Callable = dearpygui.add_char_remap                                                  

    def __init__(
        self                                      ,
        source            : int                   ,
        target            : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
