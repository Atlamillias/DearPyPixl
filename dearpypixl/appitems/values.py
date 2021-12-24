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
    "IntValue",
    "Int4Value",
    "BoolValue",
    "FloatValue",
    "Float4Value",
    "StringValue",
    "DoubleValue",
    "Double4Value",
    "ColorValue",
    "FloatVectValue",
    "SeriesValue",
]


class IntValue(Widget):
    """Adds a int value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (int, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : int             = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : int             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvIntValue',)                                                                    
    _command          : Callable        = dearpygui.add_int_value                                                            

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Union[int, str] = 0   ,
        default_value     : int             = 0   ,
        parent            : Union[int, str] = 13  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Int4Value(Widget):
    """Adds a int4 value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Union[List[int], Tuple[int, ...]], optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[int], Tuple[int, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                              = False                                                                              
    _is_root_item     : bool                              = False                                                                              
    _is_value_able    : bool                              = True                                                                               
    _unique_parents   : tuple                             = ('ValueRegistry',)                                                                 
    _unique_children  : tuple                             = ()                                                                                 
    _unique_commands  : tuple                             = ()                                                                                 
    _unique_constants : tuple                             = ('mvInt4Value',)                                                                   
    _command          : Callable                          = dearpygui.add_int4_value                                                           

    def __init__(
        self                                                                ,
        label             : str                               = None        ,
        user_data         : Any                               = None        ,
        use_internal_label: bool                              = True        ,
        source            : Union[int, str]                   = 0           ,
        default_value     : Union[List[int], Tuple[int, ...]] = (0, 0, 0, 0),
        parent            : Union[int, str]                   = 13          ,
        **kwargs                                                            ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class BoolValue(Widget):
    """Adds a bool value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (bool, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : bool            = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : bool            = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvBoolValue',)                                                                   
    _command          : Callable        = dearpygui.add_bool_value                                                           

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        source            : Union[int, str] = 0    ,
        default_value     : bool            = False,
        parent            : Union[int, str] = 13   ,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class FloatValue(Widget):
    """Adds a float value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (float, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : float           = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : float           = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvFloatValue',)                                                                  
    _command          : Callable        = dearpygui.add_float_value                                                          

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Union[int, str] = 0   ,
        default_value     : float           = 0.0 ,
        parent            : Union[int, str] = 13  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Float4Value(Widget):
    """Adds a float4 value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Union[List[float], Tuple[float, ...]], optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('ValueRegistry',)                                                                 
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvFloat4Value',)                                                                 
    _command          : Callable                              = dearpygui.add_float4_value                                                         

    def __init__(
        self                                                                            ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        source            : Union[int, str]                       = 0                   ,
        default_value     : Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0),
        parent            : Union[int, str]                       = 13                  ,
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class StringValue(Widget):
    """Adds a string value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (str, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : str             = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : str             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvStringValue',)                                                                 
    _command          : Callable        = dearpygui.add_string_value                                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Union[int, str] = 0   ,
        default_value     : str             = ''  ,
        parent            : Union[int, str] = 13  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class DoubleValue(Widget):
    """Adds a double value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (float, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : float           = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : float           = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvDoubleValue',)                                                                 
    _command          : Callable        = dearpygui.add_double_value                                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Union[int, str] = 0   ,
        default_value     : float           = 0.0 ,
        parent            : Union[int, str] = 13  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Double4Value(Widget):
    """Adds a double value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Any, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Any             = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Any             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvDouble4Value',)                                                                
    _command          : Callable        = dearpygui.add_double4_value                                                        

    def __init__(
        self                                                      ,
        label             : str             = None                ,
        user_data         : Any             = None                ,
        use_internal_label: bool            = True                ,
        source            : Union[int, str] = 0                   ,
        default_value     : Any             = (0.0, 0.0, 0.0, 0.0),
        parent            : Union[int, str] = 13                  ,
        **kwargs                                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class ColorValue(Widget):
    """Adds a color value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Union[List[float], Tuple[float, ...]], optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('ValueRegistry',)                                                                 
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvColorValue',)                                                                  
    _command          : Callable                              = dearpygui.add_color_value                                                          

    def __init__(
        self                                                                            ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        source            : Union[int, str]                       = 0                   ,
        default_value     : Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0),
        parent            : Union[int, str]                       = 13                  ,
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class FloatVectValue(Widget):
    """Adds a float vect value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Union[List[float], Tuple[float, ...]], optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('ValueRegistry',)                                                                 
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvFloatVectValue',)                                                              
    _command          : Callable                              = dearpygui.add_float_vect_value                                                     

    def __init__(
        self                                                            ,
        label             : str                                   = None,
        user_data         : Any                                   = None,
        use_internal_label: bool                                  = True,
        source            : Union[int, str]                       = 0   ,
        default_value     : Union[List[float], Tuple[float, ...]] = ()  ,
        parent            : Union[int, str]                       = 13  ,
        **kwargs                                                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class SeriesValue(Widget):
    """Adds a plot series value.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		default_value (Any, optional): 
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Any             = ItemAttribute('information', 'get_item_cached', None, None)                        
    value             : Any             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool            = False                                                                              
    _is_root_item     : bool            = False                                                                              
    _is_value_able    : bool            = True                                                                               
    _unique_parents   : tuple           = ('ValueRegistry',)                                                                 
    _unique_children  : tuple           = ()                                                                                 
    _unique_commands  : tuple           = ()                                                                                 
    _unique_constants : tuple           = ('mvSeriesValue',)                                                                 
    _command          : Callable        = dearpygui.add_series_value                                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Union[int, str] = 0   ,
        default_value     : Any             = ()  ,
        parent            : Union[int, str] = 13  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
