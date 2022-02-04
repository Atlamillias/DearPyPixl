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
    "RadioButton",
    "Listbox",
    "Checkbox",
    "Button",
    "Selectable",
    "Combo",
    "InputText",
    "InputInt",
    "InputIntMulti",
    "InputFloat",
    "InputFloatMulti",
    "SliderFloat",
    "DragFloat",
    "Text",
    "TabButton",
    "MenuItem",
    "Image",
]


class InputFloat(Widget):
    """Adds input for an float. +/- buttons can be activated by setting the value of step.

    Args:
        label (str, optional): Overrides 'name' as label.
        user_data (Any, optional): User data for callbacks
        use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        width (int, optional): Width of the item.
        indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
        before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
        source (Union[int, str], optional): Overrides 'id' as value storage key.
        payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        callback (Callable, optional): Registers a callback.
        drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        show (bool, optional): Attempt to render widget.
        enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
        filter_key (str, optional): Used by filter widget.
        tracked (bool, optional): Scroll tracking
        track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        default_value (float, optional): 
        format (str, optional): Determines the format the float will be displayed as use python string formatting.
        min_value (float, optional): Value for lower limit of input. By default this limits the step buttons. Use min_clamped to limit manual input.
        max_value (float, optional): Value for upper limit of input. By default this limits the step buttons. Use max_clamped to limit manual input.
        step (float, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
        step_fast (float, optional): After holding the step buttons for extended time the increments will switch to this value.
        min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        on_enter (bool, optional): Only runs callback on enter key press.
        readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
        id (Union[int, str], optional): (deprecated) 
    """
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)      
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : ItemT                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : list[int] | tuple[int, ...]       = ItemAttribute('configuration', 'get_item_state' , 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : float                             = ItemAttribute('information'  , 'get_item_cached', None             , None)
    format                   : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    min_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    step                     : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    step_fast                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    min_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    on_enter                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    readonly                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    value                    : float                             = ItemAttribute("configuration", "get_item_value" , "set_item_value" , None)

    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvInputFloat',)                                                                       
    _command                 : Callable                          = dearpygui.add_input_float


    def __init__(
        self,
        label             : str = None,
        user_data         : Any = None,
        use_internal_label: bool = True,
        width             : int = 0,
        indent            : int = -1,
        parent            : int | str = 0,
        before            : int | str = 0,
        source            : int | str = 0,
        payload_type      : str = '$$DPG_PAYLOAD',
        callback          : Callable = None,
        drag_callback     : Callable = None,
        drop_callback     : Callable = None,
        show              : bool = True,
        enabled           : bool = True,
        pos               : list[int] | tuple[int,...] = (),
        filter_key        : str = '',
        tracked           : bool = False,
        track_offset      : float = 0.5,
        default_value     : float = 0.0,
        format            : str = '%.3f',
        min_value         : float = 0.0,
        max_value         : float = 100.0,
        step              : float = 0.1,
        step_fast         : float = 1.0,
        min_clamped       : bool = False,
        max_clamped       : bool = False,
        on_enter          : bool = False,
        readonly          : bool = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )
    


class InputFloatMulti(Widget):
    """Adds multi float input for up to 4 float values.

    Args:
        label (str, optional): Overrides 'name' as label.
        user_data (Any, optional): User data for callbacks
        use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        width (int, optional): Width of the item.
        indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
        before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
        source (Union[int, str], optional): Overrides 'id' as value storage key.
        payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        callback (Callable, optional): Registers a callback.
        drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        show (bool, optional): Attempt to render widget.
        enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
        filter_key (str, optional): Used by filter widget.
        tracked (bool, optional): Scroll tracking
        track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        default_value (Union[List[float], Tuple[float, ...]], optional): 
        format (str, optional): Determines the format the float will be displayed as (use python string formatting).
        min_value (float, optional): Value for lower limit of input for each cell. Use min_clamped to turn on.
        max_value (float, optional): Value for upper limit of input for each cell. Use max_clamped to turn on.
        size (int, optional): Number of components displayed for input.
        min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        on_enter (bool, optional): Only runs callback on enter key press.
        readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
        id (Union[int, str], optional): (deprecated) 
    """
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)          
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : ItemT                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : list[int] | tuple[int, ...]       = ItemAttribute('configuration', 'get_item_state' , 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    format                   : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    min_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    size                     : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    min_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    on_enter                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    readonly                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    value                    : list[float] | tuple[float, ...]   = ItemAttribute("configuration", "get_item_value", "set_item_value"  , None)
    
    default_value            : list[float] | tuple[float, ...]   = ItemAttribute('information'  , 'get_item_cached', None             , None)

    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvInputFloatMulti',)                                                                       
    _command                 : Callable                          = dearpygui.add_input_floatx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True,  
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        default_value: Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0), 
        format: str = '%.3f', 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        size: int = 4, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )



class InputInt(Widget):
    """Adds input for an int. +/- buttons can be activated by setting the value of step.

    Args:
        label (str, optional): Overrides 'name' as label.
        user_data (Any, optional): User data for callbacks
        use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        width (int, optional): Width of the item.
        indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
        before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
        source (Union[int, str], optional): Overrides 'id' as value storage key.
        payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        callback (Callable, optional): Registers a callback.
        drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        show (bool, optional): Attempt to render widget.
        enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
        filter_key (str, optional): Used by filter widget.
        tracked (bool, optional): Scroll tracking
        track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        default_value (int, optional): 
        min_value (int, optional): Value for lower limit of input. By default this limits the step buttons. Use min_clamped to limit manual input.
        max_value (int, optional): Value for upper limit of input. By default this limits the step buttons. Use max_clamped to limit manual input.
        step (int, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
        step_fast (int, optional): After holding the step buttons for extended time the increments will switch to this value.
        min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        on_enter (bool, optional): Only runs callback on enter key press.
        readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
        id (Union[int, str], optional): (deprecated)
    """
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)      
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : ItemT                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : list[int] | tuple[int, ...]       = ItemAttribute('configuration', 'get_item_state' , 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    min_value                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_value                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    step                     : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    step_fast                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    min_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    on_enter                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    readonly                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    value                    : int                               = ItemAttribute("configuration", "get_item_value", "set_item_value"  , None)

    default_value            : int                               = ItemAttribute('information'  , 'get_item_cached', None             , None)
                       
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvInputInt',)                                                                       
    _command                 : Callable                          = dearpygui.add_input_int 


    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        default_value: int = 0, 
        min_value: int = 0, 
        max_value: int = 100, 
        step: int = 1, 
        step_fast: int = 100, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )


class InputIntMulti(Widget):
    """Adds multi int input for up to 4 integer values.

    Args:
        label (str, optional): Overrides 'name' as label.
        user_data (Any, optional): User data for callbacks
        use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        width (int, optional): Width of the item.
        indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
        before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
        source (Union[int, str], optional): Overrides 'id' as value storage key.
        payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        callback (Callable, optional): Registers a callback.
        drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        show (bool, optional): Attempt to render widget.
        enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
        filter_key (str, optional): Used by filter widget.
        tracked (bool, optional): Scroll tracking
        track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        default_value (Union[List[int], Tuple[int, ...]], optional): 
        min_value (int, optional): Value for lower limit of input for each cell. Use min_clamped to turn on.
        max_value (int, optional): Value for upper limit of input for each cell. Use max_clamped to turn on.
        size (int, optional): Number of components displayed for input.
        min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        on_enter (bool, optional): Only runs callback on enter.
        readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
        id (Union[int, str], optional): (deprecated) 
    """
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)          
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : ItemT                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : list[int] | tuple[int, ...]       = ItemAttribute('configuration', 'get_item_state' , 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    min_value                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_value                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    size                     : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    min_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    max_clamped              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    on_enter                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    readonly                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None) 
    value                    : list[int] | tuple[int, ...]       = ItemAttribute("configuration", "get_item_value" , "set_item_value" , None)

    default_value            : list[int] | tuple[int, ...]       = ItemAttribute('information'  , 'get_item_cached', None             , None)
                     
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvInputIntMulti',)                                                                       
    _command                 : Callable                          = dearpygui.add_input_intx


    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = (), 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        default_value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 0), 
        min_value: int = 0, 
        max_value: int = 100, 
        size: int = 4, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )


class RadioButton(Widget):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.
    
    	Args:
    		items (Union[List[str], Tuple[str, ...]], optional): A tuple of items to be shown as radio options. Can consist of any combination of types. All types will be shown as strings.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (str, optional): Default selected radio option. Set by using the string value of the item.
    		horizontal (bool, optional): Displays the radio options horizontally.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    items                    : Union[List[str], Tuple[str, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : str                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    horizontal               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : str                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvRadioButton',)                                                                 
    _command                 : Callable                          = dearpygui.add_radio_button                                                         

    def __init__(
        self                                                                   ,
        items             : Union[List[str], Tuple[str, ...]] = ()             ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : str                               = ''             ,
        horizontal        : bool                              = False          ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            items=items,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            horizontal=horizontal,
            **kwargs,
        )


class Listbox(Widget):
    """Adds a listbox. If height is not large enough to show all items a scroll bar will appear.
    
    	Args:
    		items (Union[List[str], Tuple[str, ...]], optional): A tuple of items to be shown in the listbox. Can consist of any combination of types. All items will be displayed as strings.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (str, optional): String value fo the item that will be selected by default.
    		num_items (int, optional): Expands the height of the listbox to show specified number of items.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    items                    : Union[List[str], Tuple[str, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : str                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    num_items                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : str                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvListbox',)                                                                     
    _command                 : Callable                          = dearpygui.add_listbox                                                              

    def __init__(
        self                                                                   ,
        items             : Union[List[str], Tuple[str, ...]] = ()             ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : str                               = ''             ,
        num_items         : int                               = 3              ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            items=items,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            num_items=num_items,
            **kwargs,
        )


class Checkbox(Widget):
    """Adds a checkbox.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (bool, optional): Sets the default value of the checkmark
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : bool                              = ItemAttribute('information', 'get_item_cached', None, None)                        
    value                    : bool                              = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvCheckbox',)                                                                    
    _command                 : Callable                          = dearpygui.add_checkbox                                                             

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : bool                              = False          ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            **kwargs,
        )


class Button(Widget):
    """Adds a button.
    
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
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		small (bool, optional): Shrinks the size of the button to the text of the label it contains. Useful for embedding in text.
    		arrow (bool, optional): Displays an arrow in place of the text string. This requires the direction keyword.
    		direction (int, optional): Sets the cardinal direction for the arrow buy using constants mvDir_Left, mvDir_Up, mvDir_Down, mvDir_Right, mvDir_None. Arrow keyword must be set to True.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    width               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    height              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    indent              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    payload_type        : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)                                                                                                                                                                                   
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    enabled             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)                                                                                                                                                                                    
    filter_key          : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    tracked             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    track_offset        : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    small               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    arrow               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   
    direction           : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                   

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
    _is_value_able      : bool                              = False                                                                                                                                                                                                                                                        
    _unique_parents     : tuple                             = ()                                                                                                                                                                                                                                                           
    _unique_children    : tuple                             = ()                                                                                                                                                                                                                                                           
    _unique_commands    : tuple                             = ()                                                                                                                                                                                                                                                           
    _unique_constants   : tuple                             = ('mvButton', 'mvAll', 'mvTool_About', 'mvTool_Debug', 'mvTool_Doc', 'mvTool_ItemRegistry', 'mvTool_Metrics', 'mvTool_Style', 'mvTool_Font', 'mvFontAtlas', 'mvAppUUID', 'mvInvalidUUID', 'mvDir_None', 'mvDir_Left', 'mvDir_Right', 'mvDir_Up', 'mvDir_Down')
    _command            : Callable                          = dearpygui.add_button                                                                                                                                                                                                                                         

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
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        small             : bool                              = False          ,
        arrow             : bool                              = False          ,
        direction         : int                               = 0              ,
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
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            small=small,
            arrow=arrow,
            direction=direction,
            **kwargs,
        )


class Selectable(Widget):
    """Adds a selectable. Similar to a button but can indicate its selected state.
    
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
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (bool, optional): 
    		span_columns (bool, optional): Forces the selectable to span the width of all columns if placed in a table.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : bool                              = ItemAttribute('information', 'get_item_cached', None, None)                        
    span_columns             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : bool                              = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    is_toggled_open          : bool                              = ItemAttribute("state", "get_item_state", None, "toggled_open")                     
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvSelectable',)                                                                  
    _command                 : Callable                          = dearpygui.add_selectable                                                           

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
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : bool                              = False          ,
        span_columns      : bool                              = False          ,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            span_columns=span_columns,
            **kwargs,
        )


class Combo(Widget):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window. All items will be shown as selectables on the dropdown.
    
    	Args:
    		items (Union[List[str], Tuple[str, ...]], optional): A tuple of items to be shown in the drop down window. Can consist of any combination of types but will convert all items to strings to be shown.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (str, optional): Sets a selected item from the drop down by specifying the string value.
    		popup_align_left (bool, optional): Align the contents on the popup toward the left.
    		no_arrow_button (bool, optional): Display the preview box without the square arrow button indicating dropdown activity.
    		no_preview (bool, optional): Display only the square arrow button and not the selected value.
    		height_mode (int, optional): Controlls the number of items shown in the dropdown by the constants mvComboHeight_Small, mvComboHeight_Regular, mvComboHeight_Large, mvComboHeight_Largest
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    items                    : Union[List[str], Tuple[str, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)                                 
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)                                 
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)                                 
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)                                  
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    default_value            : str                               = ItemAttribute('information', 'get_item_cached', None, None)                                                
    popup_align_left         : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    no_arrow_button          : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    no_preview               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    height_mode              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                 
    value                    : str                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")                        

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                                  
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                           
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                            
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                             
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                                  
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                                                   
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                                  
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                                  
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                                  
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                                                   
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                                                
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                                              
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")                                   
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                                 
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                                 
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                                
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                                     

    _is_container            : bool                              = False                                                                                                      
    _is_root_item            : bool                              = False                                                                                                      
    _is_value_able           : bool                              = True                                                                                                       
    _unique_parents          : tuple                             = ()                                                                                                         
    _unique_children         : tuple                             = ()                                                                                                         
    _unique_commands         : tuple                             = ()                                                                                                         
    _unique_constants        : tuple                             = ('mvCombo', 'mvComboHeight_Small', 'mvComboHeight_Regular', 'mvComboHeight_Large', 'mvComboHeight_Largest')
    _command                 : Callable                          = dearpygui.add_combo                                                                                        

    def __init__(
        self                                                                   ,
        items             : Union[List[str], Tuple[str, ...]] = ()             ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : str                               = ''             ,
        popup_align_left  : bool                              = False          ,
        no_arrow_button   : bool                              = False          ,
        no_preview        : bool                              = False          ,
        height_mode       : int                               = 1              ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            items=items,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            popup_align_left=popup_align_left,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
            height_mode=height_mode,
            **kwargs,
        )


class InputText(Widget):
    """Adds input for text.
    
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
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (str, optional): 
    		hint (str, optional): Displayed only when value is an empty string. Will reappear if input value is set to empty string. Will not show if default value is anything other than default empty string.
    		multiline (bool, optional): Allows for multiline text input.
    		no_spaces (bool, optional): Filter out spaces and tabs.
    		uppercase (bool, optional): Automatically make all inputs uppercase.
    		tab_input (bool, optional): Allows tabs to be input into the string value instead of changing item focus.
    		decimal (bool, optional): Only allow characters 0123456789.+-*/
    		hexadecimal (bool, optional): Only allow characters 0123456789ABCDEFabcdef
    		readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
    		password (bool, optional): Display all input characters as '*'.
    		scientific (bool, optional): Only allow characters 0123456789.+-*/eE (Scientific notation input)
    		on_enter (bool, optional): Only runs callback on enter key press.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : str                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    hint                     : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    multiline                : bool                              = ItemAttribute('configuration', 'get_item_config', 'set_item_config', 'multline')   
    no_spaces                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    uppercase                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tab_input                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    decimal                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    hexadecimal              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    readonly                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    password                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    scientific               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    on_enter                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : str                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvInput',)                                                                       
    _command                 : Callable                          = dearpygui.add_input_text                                                           

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
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : str                               = ''             ,
        hint              : str                               = ''             ,
        multiline         : bool                              = False          ,
        no_spaces         : bool                              = False          ,
        uppercase         : bool                              = False          ,
        tab_input         : bool                              = False          ,
        decimal           : bool                              = False          ,
        hexadecimal       : bool                              = False          ,
        readonly          : bool                              = False          ,
        password          : bool                              = False          ,
        scientific        : bool                              = False          ,
        on_enter          : bool                              = False          ,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hint=hint,
            multiline=multiline,
            no_spaces=no_spaces,
            uppercase=uppercase,
            tab_input=tab_input,
            decimal=decimal,
            hexadecimal=hexadecimal,
            readonly=readonly,
            password=password,
            scientific=scientific,
            on_enter=on_enter,
            **kwargs,
        )


class SliderFloat(Widget):
    """Adds slider for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    
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
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (float, optional): 
    		vertical (bool, optional): Sets orientation of the slidebar and slider to vertical.
    		no_input (bool, optional): Disable direct entry methods double-click or ctrl+click or Enter key allowing to input text directly into the item.
    		clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    		min_value (float, optional): Applies a limit only to sliding entry only.
    		max_value (float, optional): Applies a limit only to sliding entry only.
    		format (str, optional): Determines the format the float will be displayed as use python string formatting.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : float                             = ItemAttribute('information', 'get_item_cached', None, None)                        
    vertical                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_input                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    clamped                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    min_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    max_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    format                   : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : float                             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvSlider',)                                                                      
    _command                 : Callable                          = dearpygui.add_slider_float                                                         

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
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : float                             = 0.0            ,
        vertical          : bool                              = False          ,
        no_input          : bool                              = False          ,
        clamped           : bool                              = False          ,
        min_value         : float                             = 0.0            ,
        max_value         : float                             = 100.0          ,
        format            : str                               = '%.3f'         ,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )


class DragFloat(Widget):
    """Adds drag for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		callback (Callable, optional): Registers a callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (float, optional): 
    		format (str, optional): Determines the format the float will be displayed as use python string formatting.
    		speed (float, optional): Sets the sensitivity the float will be modified while dragging.
    		min_value (float, optional): Applies a limit only to draging entry only.
    		max_value (float, optional): Applies a limit only to draging entry only.
    		no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
    		clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source                   : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : float                             = ItemAttribute('information', 'get_item_cached', None, None)                        
    format                   : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    speed                    : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    min_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    max_value                : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_input                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    clamped                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : float                             = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    is_resized               : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                          
    is_middle_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                   
    is_right_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                    
    is_left_clicked          : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                     
    is_hovered               : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                          
    is_active                : bool                              = ItemAttribute("state", "get_item_state", None, "active")                           
    is_focused               : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                          
    is_clicked               : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                          
    is_visible               : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                          
    is_edited                : bool                              = ItemAttribute("state", "get_item_state", None, "edited")                           
    is_activated             : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                        
    is_deactivated           : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                      
    is_deactivated_after_edit: bool                              = ItemAttribute("state", "get_item_state", None, "deactivated_after_edit")           
    rect_min                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                         
    rect_max                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                         
    rect_size                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                        
    content_region_avail     : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")             

    _is_container            : bool                              = False                                                                              
    _is_root_item            : bool                              = False                                                                              
    _is_value_able           : bool                              = True                                                                               
    _unique_parents          : tuple                             = ()                                                                                 
    _unique_children         : tuple                             = ()                                                                                 
    _unique_commands         : tuple                             = ()                                                                                 
    _unique_constants        : tuple                             = ('mvDrag',)                                                                        
    _command                 : Callable                          = dearpygui.add_drag_float                                                           

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        callback          : Callable                          = None           ,
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        enabled           : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        default_value     : float                             = 0.0            ,
        format            : str                               = '%0.3f'        ,
        speed             : float                             = 1.0            ,
        min_value         : float                             = 0.0            ,
        max_value         : float                             = 100.0          ,
        no_input          : bool                              = False          ,
        clamped           : bool                              = False          ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )


class Text(Widget):
    """Adds text. Text can have an optional label that will display to the right of the text.
    
    	Args:
    		default_value (str, optional): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
    		wrap (int, optional): Number of pixels from the start of the item until wrapping starts.
    		bullet (bool, optional): Places a bullet to the left of the text.
    		color (Union[List[int], Tuple[int, ...]], optional): Color of the text (rgba).
    		show_label (bool, optional): Displays the label to the right of the text.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    default_value       : str                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source              : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type        : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key          : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset        : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    wrap                : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    bullet              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    color               : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show_label          : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value               : str                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

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
    _is_value_able      : bool                              = True                                                                               
    _unique_parents     : tuple                             = ()                                                                                 
    _unique_children    : tuple                             = ()                                                                                 
    _unique_commands    : tuple                             = ()                                                                                 
    _unique_constants   : tuple                             = ('mvText',)                                                                        
    _command            : Callable                          = dearpygui.add_text                                                                 

    def __init__(
        self                                                                     ,
        default_value     : str                               = ''               ,
        label             : str                               = None             ,
        user_data         : Any                               = None             ,
        use_internal_label: bool                              = True             ,
        indent            : int                               = -1               ,
        parent            : Union[int, str]                   = 0                ,
        before            : Union[int, str]                   = 0                ,
        source            : Union[int, str]                   = 0                ,
        payload_type      : str                               = '$$DPG_PAYLOAD'  ,
        drag_callback     : Callable                          = None             ,
        drop_callback     : Callable                          = None             ,
        show              : bool                              = True             ,
        pos               : Union[List[int], Tuple[int, ...]] = []               ,
        filter_key        : str                               = ''               ,
        tracked           : bool                              = False            ,
        track_offset      : float                             = 0.5              ,
        wrap              : int                               = -1               ,
        bullet            : bool                              = False            ,
        color             : Union[List[int], Tuple[int, ...]] = (-255, 0, 0, 255),
        show_label        : bool                              = False            ,
        **kwargs                                                                 ,
    ) -> None:
        super().__init__(
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            wrap=wrap,
            bullet=bullet,
            color=color,
            show_label=show_label,
            **kwargs,
        )


class TabButton(Widget):
    """Adds a tab button to a tab bar.
    
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
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		no_reorder (bool, optional): Disable reordering this tab or having another tab cross over this tab. Fixes the position of this tab in relation to the order of neighboring tabs at start. 
    		leading (bool, optional): Enforce the tab position to the left of the tab bar (after the tab list popup button).
    		trailing (bool, optional): Enforce the tab position to the right of the tab bar (before the scrolling buttons).
    		no_tooltip (bool, optional): Disable tooltip for the given tab.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    indent            : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    payload_type      : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    callback          : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    drag_callback     : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    drop_callback     : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    filter_key        : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    tracked           : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    track_offset      : float    = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    no_reorder        : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    leading           : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    trailing          : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    no_tooltip        : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool     = False                                                                     
    _is_root_item     : bool     = False                                                                     
    _is_value_able    : bool     = False                                                                     
    _unique_parents   : tuple    = ('TabBar', 'Stage', 'TemplateRegistry')                                   
    _unique_children  : tuple    = ()                                                                        
    _unique_commands  : tuple    = ()                                                                        
    _unique_constants : tuple    = ('mvTabButton',)                                                          
    _command          : Callable = dearpygui.add_tab_button                                                  

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        indent            : int             = -1             ,
        parent            : Union[int, str] = 0              ,
        before            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        callback          : Callable        = None           ,
        drag_callback     : Callable        = None           ,
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        filter_key        : str             = ''             ,
        tracked           : bool            = False          ,
        track_offset      : float           = 0.5            ,
        no_reorder        : bool            = False          ,
        leading           : bool            = False          ,
        trailing          : bool            = False          ,
        no_tooltip        : bool            = False          ,
        **kwargs                                             ,
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
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            no_reorder=no_reorder,
            leading=leading,
            trailing=trailing,
            no_tooltip=no_tooltip,
            **kwargs,
        )


class MenuItem(Widget):
    """Adds a menu item to an existing menu. Menu items act similar to selectables and has a bool value. When placed in a menu the checkmark will reflect its value.
    
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
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (bool, optional): This value also controls the checkmark when shown.
    		shortcut (str, optional): Displays text on the menu item. Typically used to show a shortcut key command.
    		check (bool, optional): Displays a checkmark on the menu item when it is selected and placed in a menu.
    		id (Union[int, str], optional): (deprecated) 
    		drag_callback (Callable, optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent            : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type      : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback          : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback     : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled           : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    filter_key        : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked           : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset      : float    = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : bool     = ItemAttribute('information', 'get_item_cached', None, None)                        
    shortcut          : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    check             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : bool     = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool     = False                                                                              
    _is_root_item     : bool     = False                                                                              
    _is_value_able    : bool     = True                                                                               
    _unique_parents   : tuple    = ()                                                                                 
    _unique_children  : tuple    = ()                                                                                 
    _unique_commands  : tuple    = ()                                                                                 
    _unique_constants : tuple    = ('mvMenuItem',)                                                                    
    _command          : Callable = dearpygui.add_menu_item                                                            

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        indent            : int             = -1             ,
        parent            : Union[int, str] = 0              ,
        before            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        callback          : Callable        = None           ,
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        enabled           : bool            = True           ,
        filter_key        : str             = ''             ,
        tracked           : bool            = False          ,
        track_offset      : float           = 0.5            ,
        default_value     : bool            = False          ,
        shortcut          : str             = ''             ,
        check             : bool            = False          ,
        **kwargs                                             ,
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
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            shortcut=shortcut,
            check=check,
            **kwargs,
        )


class Image(Widget):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) for texture coordinates will generally display the entire texture.
    
    	Args:
    		texture_tag (Union[int, str]): The texture_tag should come from a texture that was added to a texture registry.
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
    		tint_color (Union[List[float], Tuple[float, ...]], optional): Applies a color tint to the entire texture.
    		border_color (Union[List[float], Tuple[float, ...]], optional): Displays a border of the specified color around the texture. If the theme style has turned off the border it will not be shown.
    		uv_min (Union[List[float], Tuple[float, ...]], optional): Normalized texture coordinates min point.
    		uv_max (Union[List[float], Tuple[float, ...]], optional): Normalized texture coordinates max point.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    texture_tag         : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label               : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    width               : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    height              : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    indent              : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    payload_type        : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    drag_callback       : Callable                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    drop_callback       : Callable                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show                : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    pos                 : Union[List[int], Tuple[int, ...]]     = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None) 
    filter_key          : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    tracked             : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    track_offset        : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    tint_color          : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    border_color        : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    uv_min              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    uv_max              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    is_resized          : bool                                  = ItemAttribute("state", "get_item_state", None, "resized")                 
    is_middle_clicked   : bool                                  = ItemAttribute("state", "get_item_state", None, "middle_clicked")          
    is_right_clicked    : bool                                  = ItemAttribute("state", "get_item_state", None, "right_clicked")           
    is_left_clicked     : bool                                  = ItemAttribute("state", "get_item_state", None, "left_clicked")            
    is_hovered          : bool                                  = ItemAttribute("state", "get_item_state", None, "hovered")                 
    is_clicked          : bool                                  = ItemAttribute("state", "get_item_state", None, "clicked")                 
    is_visible          : bool                                  = ItemAttribute("state", "get_item_state", None, "visible")                 
    rect_min            : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_min")                
    rect_max            : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_max")                
    rect_size           : list[int, int]                        = ItemAttribute("state", "get_item_state", None, "rect_size")               
    content_region_avail: list[int, int]                        = ItemAttribute("state", "get_item_state", None, "content_region_avail")    

    _is_container       : bool                                  = False                                                                     
    _is_root_item       : bool                                  = False                                                                     
    _is_value_able      : bool                                  = False                                                                     
    _unique_parents     : tuple                                 = ()                                                                        
    _unique_children    : tuple                                 = ()                                                                        
    _unique_commands    : tuple                                 = ()                                                                        
    _unique_constants   : tuple                                 = ('mvImageItems',)                                                         
    _command            : Callable                              = dearpygui.add_image                                                       

    def __init__(
        self                                                                            ,
        texture_tag       : Union[int, str]                                             ,
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
        drag_callback     : Callable                              = None                ,
        drop_callback     : Callable                              = None                ,
        show              : bool                                  = True                ,
        pos               : Union[List[int], Tuple[int, ...]]     = []                  ,
        filter_key        : str                                   = ''                  ,
        tracked           : bool                                  = False               ,
        track_offset      : float                                 = 0.5                 ,
        tint_color        : Union[List[float], Tuple[float, ...]] = (255, 255, 255, 255),
        border_color      : Union[List[float], Tuple[float, ...]] = (0, 0, 0, 0)        ,
        uv_min            : Union[List[float], Tuple[float, ...]] = (0.0, 0.0)          ,
        uv_max            : Union[List[float], Tuple[float, ...]] = (1.0, 1.0)          ,
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
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
            tint_color=tint_color,
            border_color=border_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )
