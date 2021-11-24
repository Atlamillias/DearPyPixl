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
    "ProgressBar",
    "ItemSet",
    "Spacer",
    "Separator",
    "TimePicker",
    "DatePicker",
    "Slider3D",
    "KnobFloat",
    "LoadingIndicator",
    "FileDialog",
    "FileExtension",
]


class ProgressBar(Widget):
    """Adds a progress bar.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		overlay (str, optional): Overlayed text onto the bar that typically used to display the value of the progress.
    		default_value (float, optional): Normalized value to fill the bar from 0.0 to 1.0.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    indent            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    source            : Union[int, str]                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "source")            
    payload_type      : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    drag_callback     : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback     : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos               : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    tracked           : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset      : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    overlay           : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "overlay")           
    default_value     : float                             = ItemAttribute('information', 'get_unmanagable', None, 'default_value')                          
    value             : float                             = ItemAttribute("configuration", "get_value", "set_value", "default_value")                       

    _is_container     : bool                              = False                                                                                           
    _is_root_item     : bool                              = False                                                                                           
    _is_value_able    : bool                              = True                                                                                            
    _unique_parents   : tuple                             = ()                                                                                              
    _unique_children  : tuple                             = ()                                                                                              
    _unique_commands  : tuple                             = ()                                                                                              
    _unique_constants : tuple                             = ('mvProgressBar',)                                                                              
    _command          : Callable                          = dearpygui.add_progress_bar                                                                      

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        height            : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        overlay           : str                               = ''             ,
        default_value     : float                             = 0.0            ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            overlay=overlay,
            default_value=default_value,
            **kwargs,
        )


class ItemSet(Widget):
    """Adds an item set to an item pool.
    
    	Args:
    		type (int): 
    		count (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    count             : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "count")             
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('ItemPool',)                                                                                   
    _unique_children  : tuple    = ('ItemSet',)                                                                                    
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvItemPool',)                                                                                 
    _command          : Callable = dearpygui.add_item_set                                                                          

    def __init__(
        self                           ,
        item_type         : int        ,
        count             : int        ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            item_type=item_type,
            count=count,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class Spacer(Widget):
    """Adds a spacer item that can be used to help with layouts or can be used as a placeholder item.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    indent            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos               : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       

    _is_container     : bool                              = False                                                                                           
    _is_root_item     : bool                              = False                                                                                           
    _is_value_able    : bool                              = False                                                                                           
    _unique_parents   : tuple                             = ()                                                                                              
    _unique_children  : tuple                             = ()                                                                                              
    _unique_commands  : tuple                             = ()                                                                                              
    _unique_constants : tuple                             = ('mvSpacer',)                                                                                   
    _command          : Callable                          = dearpygui.add_spacer                                                                            

    def __init__(
        self                                                        ,
        label             : str                               = None,
        user_data         : Any                               = None,
        use_internal_label: bool                              = True,
        width             : int                               = 0   ,
        height            : int                               = 0   ,
        indent            : int                               = -1  ,
        parent            : Union[int, str]                   = 0   ,
        before            : Union[int, str]                   = 0   ,
        show              : bool                              = True,
        pos               : Union[List[int], Tuple[int, ...]] = []  ,
        **kwargs                                                    ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            **kwargs,
        )


class Separator(Widget):
    """Adds a horizontal line separator.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos               : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       

    _is_container     : bool                              = False                                                                                           
    _is_root_item     : bool                              = False                                                                                           
    _is_value_able    : bool                              = False                                                                                           
    _unique_parents   : tuple                             = ()                                                                                              
    _unique_children  : tuple                             = ()                                                                                              
    _unique_commands  : tuple                             = ()                                                                                              
    _unique_constants : tuple                             = ('mvSeparator',)                                                                                
    _command          : Callable                          = dearpygui.add_separator                                                                         

    def __init__(
        self                                                        ,
        label             : str                               = None,
        user_data         : Any                               = None,
        use_internal_label: bool                              = True,
        indent            : int                               = -1  ,
        parent            : Union[int, str]                   = 0   ,
        before            : Union[int, str]                   = 0   ,
        show              : bool                              = True,
        pos               : Union[List[int], Tuple[int, ...]] = []  ,
        **kwargs                                                    ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            **kwargs,
        )


class TimePicker(Widget):
    """Adds a time picker.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (dict, optional): 
    		hour24 (bool, optional): Show 24 hour clock instead of 12 hour.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    callback            : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    default_value       : dict                              = ItemAttribute('information', 'get_unmanagable', None, 'default_value')                          
    hour24              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "hour24")            
    value               : dict                              = ItemAttribute("configuration", "get_value", "set_value", "default_value")                       

    is_resized          : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_visible          : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                       
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                      
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                      
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool                              = False                                                                                           
    _is_root_item       : bool                              = False                                                                                           
    _is_value_able      : bool                              = True                                                                                            
    _unique_parents     : tuple                             = ()                                                                                              
    _unique_children    : tuple                             = ()                                                                                              
    _unique_commands    : tuple                             = ()                                                                                              
    _unique_constants   : tuple                             = ('mvTimePicker',)                                                                               
    _command            : Callable                          = dearpygui.add_time_picker                                                                       

    def __init__(
        self                                                                                      ,
        label             : str                               = None                              ,
        user_data         : Any                               = None                              ,
        use_internal_label: bool                              = True                              ,
        indent            : int                               = -1                                ,
        parent            : Union[int, str]                   = 0                                 ,
        before            : Union[int, str]                   = 0                                 ,
        payload_type      : str                               = '$$DPG_PAYLOAD'                   ,
        callback          : Callable                          = None                              ,
        drag_callback     : Callable                          = None                              ,
        drop_callback     : Callable                          = None                              ,
        show              : bool                              = True                              ,
        pos               : Union[List[int], Tuple[int, ...]] = []                                ,
        filter_key        : str                               = ''                                ,
        tracked           : bool                              = False                             ,
        track_offset      : float                             = 0.5                               ,
        default_value     : dict                              = {'hour': 14, 'min': 32, 'sec': 23},
        hour24            : bool                              = False                             ,
        **kwargs                                                                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hour24=hour24,
            **kwargs,
        )


class DatePicker(Widget):
    """Adds a data picker.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (dict, optional): 
    		level (int, optional): Use avaliable constants. mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    callback            : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    default_value       : dict                              = ItemAttribute('information', 'get_unmanagable', None, 'default_value')                          
    level               : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "level")             
    value               : dict                              = ItemAttribute("configuration", "get_value", "set_value", "default_value")                       

    is_resized          : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_middle_clicked   : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                
    is_right_clicked    : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                 
    is_left_clicked     : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                  
    is_hovered          : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                       
    is_active           : bool                              = ItemAttribute("state", "get_item_state", None, "active")                                        
    is_focused          : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                       
    is_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                       
    is_visible          : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                       
    is_activated        : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                                     
    is_deactivated      : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                                   
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                      
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                      
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool                              = False                                                                                           
    _is_root_item       : bool                              = False                                                                                           
    _is_value_able      : bool                              = True                                                                                            
    _unique_parents     : tuple                             = ()                                                                                              
    _unique_children    : tuple                             = ()                                                                                              
    _unique_commands    : tuple                             = ()                                                                                              
    _unique_constants   : tuple                             = ('mvDatePicker', 'mvDatePickerLevel_Day', 'mvDatePickerLevel_Month', 'mvDatePickerLevel_Year')  
    _command            : Callable                          = dearpygui.add_date_picker                                                                       

    def __init__(
        self                                                                                             ,
        label             : str                               = None                                     ,
        user_data         : Any                               = None                                     ,
        use_internal_label: bool                              = True                                     ,
        indent            : int                               = -1                                       ,
        parent            : Union[int, str]                   = 0                                        ,
        before            : Union[int, str]                   = 0                                        ,
        payload_type      : str                               = '$$DPG_PAYLOAD'                          ,
        callback          : Callable                          = None                                     ,
        drag_callback     : Callable                          = None                                     ,
        drop_callback     : Callable                          = None                                     ,
        show              : bool                              = True                                     ,
        pos               : Union[List[int], Tuple[int, ...]] = []                                       ,
        filter_key        : str                               = ''                                       ,
        tracked           : bool                              = False                                    ,
        track_offset      : float                             = 0.5                                      ,
        default_value     : dict                              = {'month_day': 14, 'year': 20, 'month': 5},
        level             : int                               = 0                                        ,
        **kwargs                                                                                         ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            level=level,
            **kwargs,
        )


class Slider3D(Widget):
    """Adds a 3D box slider.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (Union[List[float], Tuple[float, ...]], optional): 
    		max_x (float, optional): Applies upper limit to slider.
    		max_y (float, optional): Applies upper limit to slider.
    		max_z (float, optional): Applies upper limit to slider.
    		min_x (float, optional): Applies lower limit to slider.
    		min_y (float, optional): Applies lower limit to slider.
    		min_z (float, optional): Applies lower limit to slider.
    		scale (float, optional): Size of the widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width               : int                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height              : int                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    indent              : int                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_configuration", "configure_item", "source")            
    payload_type        : str                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    callback            : Callable                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    drag_callback       : Callable                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback       : Callable                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                : bool                                  = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                 : Union[List[int], Tuple[int, ...]]     = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key          : str                                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    tracked             : bool                                  = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset        : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    default_value       : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_unmanagable', None, 'default_value')                          
    max_x               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "max_x")             
    max_y               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "max_y")             
    max_z               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "max_z")             
    min_x               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "min_x")             
    min_y               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "min_y")             
    min_z               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "min_z")             
    scale               : float                                 = ItemAttribute("configuration", "get_item_configuration", "configure_item", "scale")             
    value               : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_value", "set_value", "default_value")                       

    is_resized          : bool                                  = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_hovered          : bool                                  = ItemAttribute("state", "get_item_state", None, "hovered")                                       
    is_visible          : bool                                  = ItemAttribute("state", "get_item_state", None, "visible")                                       
    rect_min            : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_min")                                      
    rect_max            : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_max")                                      
    rect_size           : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int]                        = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool                                  = False                                                                                           
    _is_root_item       : bool                                  = False                                                                                           
    _is_value_able      : bool                                  = True                                                                                            
    _unique_parents     : tuple                                 = ()                                                                                              
    _unique_children    : tuple                                 = ()                                                                                              
    _unique_commands    : tuple                                 = ()                                                                                              
    _unique_constants   : tuple                                 = ('mvSlider3D',)                                                                                 
    _command            : Callable                              = dearpygui.add_3d_slider                                                                         

    def __init__(
        self                                                                            ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        width             : int                                   = 0                   ,
        height            : int                                   = 0                   ,
        indent            : int                                   = -1                  ,
        parent            : Union[int, str]                       = 0                   ,
        before            : Union[int, str]                       = 0                   ,
        source            : Union[int, str]                       = 0                   ,
        payload_type      : str                                   = '$$DPG_PAYLOAD'     ,
        callback          : Callable                              = None                ,
        drag_callback     : Callable                              = None                ,
        drop_callback     : Callable                              = None                ,
        show              : bool                                  = True                ,
        pos               : Union[List[int], Tuple[int, ...]]     = []                  ,
        filter_key        : str                                   = ''                  ,
        tracked           : bool                                  = False               ,
        track_offset      : float                                 = 0.5                 ,
        default_value     : Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0),
        max_x             : float                                 = 100.0               ,
        max_y             : float                                 = 100.0               ,
        max_z             : float                                 = 100.0               ,
        min_x             : float                                 = 0.0                 ,
        min_y             : float                                 = 0.0                 ,
        min_z             : float                                 = 0.0                 ,
        scale             : float                                 = 1.0                 ,
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            max_x=max_x,
            max_y=max_y,
            max_z=max_z,
            min_x=min_x,
            min_y=min_y,
            min_z=min_z,
            scale=scale,
            **kwargs,
        )


class KnobFloat(Widget):
    """Adds a knob that rotates based on change in x mouse position.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (float, optional): 
    		min_value (float, optional): Applies lower limit to value.
    		max_value (float, optional): Applies upper limit to value.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width               : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    source              : Union[int, str]                   = ItemAttribute("configuration", "get_item_configuration", "configure_item", "source")            
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    callback            : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    default_value       : float                             = ItemAttribute('information', 'get_unmanagable', None, 'default_value')                          
    min_value           : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "min_scale")         
    max_value           : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "max_scale")         
    value               : float                             = ItemAttribute("configuration", "get_value", "set_value", "default_value")                       

    is_resized          : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_middle_clicked   : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                
    is_right_clicked    : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                 
    is_left_clicked     : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                  
    is_hovered          : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                       
    is_active           : bool                              = ItemAttribute("state", "get_item_state", None, "active")                                        
    is_focused          : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                       
    is_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                       
    is_visible          : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                       
    is_edited           : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                                        
    is_activated        : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                                     
    is_deactivated      : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                                   
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                      
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                      
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool                              = False                                                                                           
    _is_root_item       : bool                              = False                                                                                           
    _is_value_able      : bool                              = True                                                                                            
    _unique_parents     : tuple                             = ()                                                                                              
    _unique_children    : tuple                             = ()                                                                                              
    _unique_commands    : tuple                             = ()                                                                                              
    _unique_constants   : tuple                             = ('mvKnob',)                                                                                     
    _command            : Callable                          = dearpygui.add_knob_float                                                                        

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        height            : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : float                             = 0.0            ,
        min_value         : float                             = 0.0            ,
        max_value         : float                             = 100.0          ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            **kwargs,
        )


class LoadingIndicator(Widget):
    """Adds a rotating animated loading symbol.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		style (int, optional): 0 is rotating dots style, 1 is rotating bar style.
    		circle_count (int, optional): Number of dots show if dots or size of circle if circle.
    		speed (float, optional): Speed the anamation will rotate.
    		radius (float, optional): Radius size of the loading indicator.
    		thickness (float, optional): Thickness of the circles or line.
    		color (Union[List[int], Tuple[int, ...]], optional): Color of the growing center circle.
    		secondary_color (Union[List[int], Tuple[int, ...]], optional): Background of the dots in dot mode.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width               : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    style               : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "style")             
    circle_count        : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "circle_count")      
    speed               : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "speed")             
    radius              : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "radius")            
    thickness           : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "thickness")         
    color               : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "color")             
    secondary_color     : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "secondary_color")   

    is_resized          : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_middle_clicked   : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                
    is_right_clicked    : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                 
    is_left_clicked     : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                  
    is_hovered          : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                       
    is_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                       
    is_visible          : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                       
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                      
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                      
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool                              = False                                                                                           
    _is_root_item       : bool                              = False                                                                                           
    _is_value_able      : bool                              = False                                                                                           
    _unique_parents     : tuple                             = ()                                                                                              
    _unique_children    : tuple                             = ()                                                                                              
    _unique_commands    : tuple                             = ()                                                                                              
    _unique_constants   : tuple                             = ('mvLoadingIndicator',)                                                                         
    _command            : Callable                          = dearpygui.add_loading_indicator                                                                 

    def __init__(
        self                                                                       ,
        label             : str                               = None               ,
        user_data         : Any                               = None               ,
        use_internal_label: bool                              = True               ,
        width             : int                               = 0                  ,
        height            : int                               = 0                  ,
        indent            : int                               = -1                 ,
        parent            : Union[int, str]                   = 0                  ,
        before            : Union[int, str]                   = 0                  ,
        payload_type      : str                               = '$$DPG_PAYLOAD'    ,
        drop_callback     : Callable                          = None               ,
        show              : bool                              = True               ,
        pos               : Union[List[int], Tuple[int, ...]] = []                 ,
        style             : int                               = 0                  ,
        circle_count      : int                               = 8                  ,
        speed             : float                             = 1.0                ,
        radius            : float                             = 3.0                ,
        thickness         : float                             = 1.0                ,
        color             : Union[List[int], Tuple[int, ...]] = (51, 51, 55, 255)  ,
        secondary_color   : Union[List[int], Tuple[int, ...]] = (29, 151, 236, 103),
        **kwargs                                                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            style=style,
            circle_count=circle_count,
            speed=speed,
            radius=radius,
            thickness=thickness,
            color=color,
            secondary_color=secondary_color,
            **kwargs,
        )


class FileDialog(Container):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by default. Callback will be ran when the file or directory picker is closed. The app_data arguemnt will be populated with information related to the file and directory as a dictionary.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		default_path (str, optional): Path that the file dialog will default to when opened.
    		default_filename (str, optional): Default name that will show in the file name input.
    		file_count (int, optional): Number of visible files in the dialog.
    		modal (bool, optional): Forces user interaction with the file selector.
    		directory_selector (bool, optional): Shows only directory/paths as options. Allows selection of directory/paths only.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    default_path      : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "default_path")      
    default_filename  : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "default_filename")  
    file_count        : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "file_count")        
    modal             : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "modal")             
    directory_selector: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "directory_selector")

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = True                                                                                            
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ('get_file_dialog_info',)                                                                       
    _unique_constants : tuple    = ('mvFileDialog',)                                                                               
    _command          : Callable = dearpygui.add_file_dialog                                                                       

    def __init__(
        self                                ,
        label             : str      = None ,
        user_data         : Any      = None ,
        use_internal_label: bool     = True ,
        width             : int      = 0    ,
        height            : int      = 0    ,
        callback          : Callable = None ,
        show              : bool     = True ,
        default_path      : str      = ''   ,
        default_filename  : str      = '.'  ,
        file_count        : int      = 0    ,
        modal             : bool     = False,
        directory_selector: bool     = False,
        **kwargs                            ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            callback=callback,
            show=show,
            default_path=default_path,
            default_filename=default_filename,
            file_count=file_count,
            modal=modal,
            directory_selector=directory_selector,
            **kwargs,
        )


class FileExtension(Widget):
    """Creates a file extension filter option in the file dialog.
    
    	Args:
    		extension (str): Extension that will show as an when the parent is a file dialog.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		custom_text (str, optional): Replaces the displayed text in the drop down for this extension.
    		color (Union[List[int], Tuple[int, ...]], optional): Color for the text that will be shown with specified extensions.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    extension         : str                               = ItemAttribute("configuration", "get_unmanagable", "configure_item", "extension")         
    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    height            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")            
    custom_text       : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "custom_text")       
    color             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "color")             

    _is_container     : bool                              = False                                                                                           
    _is_root_item     : bool                              = False                                                                                           
    _is_value_able    : bool                              = False                                                                                           
    _unique_parents   : tuple                             = ('Stage', 'FileDialog', 'TemplateRegistry')                                                     
    _unique_children  : tuple                             = ()                                                                                              
    _unique_commands  : tuple                             = ()                                                                                              
    _unique_constants : tuple                             = ('mvFileExtension',)                                                                            
    _command          : Callable                          = dearpygui.add_file_extension                                                                    

    def __init__(
        self                                                                     ,
        extension         : str                                                  ,
        label             : str                               = None             ,
        user_data         : Any                               = None             ,
        use_internal_label: bool                              = True             ,
        width             : int                               = 0                ,
        height            : int                               = 0                ,
        parent            : Union[int, str]                   = 0                ,
        before            : Union[int, str]                   = 0                ,
        custom_text       : str                               = ''               ,
        color             : Union[List[int], Tuple[int, ...]] = (-255, 0, 0, 255),
        **kwargs                                                                 ,
    ) -> None:
        super().__init__(
            extension=extension,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            custom_text=custom_text,
            color=color,
            **kwargs,
        )
