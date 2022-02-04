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
    "ColorButton",
    "ColorEdit",
    "ColorPicker",
    "ColorMapScale",
    "ColorMap",
    "ColorMapButton",
    "ColorMapSlider",
]


class ColorButton(Widget):
    """Adds a color button.
    
    	Args:
    		default_value (Union[List[int], Tuple[int, ...]], optional): 
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
    		no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
    		no_border (bool, optional): Disable border around the image.
    		no_drag_drop (bool, optional): Disable ability to drag and drop small preview (color square) to apply colors to other items.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    default_value       : Union[List[int], Tuple[int, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type        : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key          : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset        : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_alpha            : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_border           : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_drag_drop        : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value               : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

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
    _unique_constants   : tuple                             = ('mvColorButton',)                                                                 
    _command            : Callable                          = dearpygui.add_color_button                                                         

    def __init__(
        self                                                                   ,
        default_value     : Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255) ,
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
        no_alpha          : bool                              = False          ,
        no_border         : bool                              = False          ,
        no_drag_drop      : bool                              = False          ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_border=no_border,
            no_drag_drop=no_drag_drop,
            **kwargs,
        )


class ColorEdit(Widget):
    """Adds an RGBA color editor. Left clicking the small color preview will provide a color picker. Click and draging the small color preview will copy the color to be applied on any other color widget.
    
    	Args:
    		default_value (Union[List[int], Tuple[int, ...]], optional): 
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
    		no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
    		no_picker (bool, optional): Disable picker popup when color square is clicked.
    		no_options (bool, optional): Disable toggling options menu when right-clicking on inputs/small preview.
    		no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
    		no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
    		no_tooltip (bool, optional): Disable tooltip when hovering the preview.
    		no_label (bool, optional): Disable display of inline text label.
    		no_drag_drop (bool, optional): Disable ability to drag and drop small preview (color square) to apply colors to other items.
    		alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
    		alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
    		display_mode (int, optional): mvColorEdit_rgb, mvColorEdit_hsv, or mvColorEdit_hex
    		display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
    		input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    default_value            : Union[List[int], Tuple[int, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                                                                                                                                                                                                     
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
    no_alpha                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_picker                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_options               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_small_preview         : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_inputs                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_tooltip               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_label                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    no_drag_drop             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    alpha_bar                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    alpha_preview            : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    display_mode             : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    display_type             : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    input_mode               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    value                    : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")                                                                                                                                                                             

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
    _unique_constants        : tuple                             = ('mvColorEdit', 'mvColorEdit_AlphaPreviewNone', 'mvColorEdit_AlphaPreview', 'mvColorEdit_AlphaPreviewHalf', 'mvColorEdit_uint8', 'mvColorEdit_float', 'mvColorEdit_rgb', 'mvColorEdit_hsv', 'mvColorEdit_hex', 'mvColorEdit_input_rgb', 'mvColorEdit_input_hsv')
    _command                 : Callable                          = dearpygui.add_color_edit                                                                                                                                                                                                                                        

    def __init__(
        self                                                                   ,
        default_value     : Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255) ,
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
        no_alpha          : bool                              = False          ,
        no_picker         : bool                              = False          ,
        no_options        : bool                              = False          ,
        no_small_preview  : bool                              = False          ,
        no_inputs         : bool                              = False          ,
        no_tooltip        : bool                              = False          ,
        no_label          : bool                              = False          ,
        no_drag_drop      : bool                              = False          ,
        alpha_bar         : bool                              = False          ,
        alpha_preview     : int                               = 0              ,
        display_mode      : int                               = 1048576        ,
        display_type      : int                               = 8388608        ,
        input_mode        : int                               = 134217728      ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_picker=no_picker,
            no_options=no_options,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            no_drag_drop=no_drag_drop,
            alpha_bar=alpha_bar,
            alpha_preview=alpha_preview,
            display_mode=display_mode,
            display_type=display_type,
            input_mode=input_mode,
            **kwargs,
        )


class ColorPicker(Widget):
    """Adds an RGB color picker. Right click the color picker for options. Click and drag the color preview to copy the color and drop on any other color widget to apply. Right Click allows the style of the color picker to be changed.
    
    	Args:
    		default_value (Union[List[int], Tuple[int, ...]], optional): 
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
    		no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
    		no_side_preview (bool, optional): Disable bigger color preview on right side of the picker, use small colored square preview instead , unless small preview is also hidden.
    		no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
    		no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
    		no_tooltip (bool, optional): Disable tooltip when hovering the preview.
    		no_label (bool, optional): Disable display of inline text label.
    		alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
    		display_rgb (bool, optional): Override _display_ type among RGB/HSV/Hex.
    		display_hsv (bool, optional): Override _display_ type among RGB/HSV/Hex.
    		display_hex (bool, optional): Override _display_ type among RGB/HSV/Hex.
    		picker_mode (int, optional): mvColorPicker_bar or mvColorPicker_wheel
    		alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
    		display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
    		input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    default_value            : Union[List[int], Tuple[int, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
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
    no_alpha                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_side_preview          : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_small_preview         : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_inputs                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_tooltip               : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    no_label                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    alpha_bar                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    display_rgb              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    display_hsv              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    display_hex              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    picker_mode              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    alpha_preview            : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    display_type             : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    input_mode               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value                    : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

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
    _unique_constants        : tuple                             = ('mvColorPicker', 'mvColorPicker_bar', 'mvColorPicker_wheel')                      
    _command                 : Callable                          = dearpygui.add_color_picker                                                         

    def __init__(
        self                                                                   ,
        default_value     : Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255) ,
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
        no_alpha          : bool                              = False          ,
        no_side_preview   : bool                              = False          ,
        no_small_preview  : bool                              = False          ,
        no_inputs         : bool                              = False          ,
        no_tooltip        : bool                              = False          ,
        no_label          : bool                              = False          ,
        alpha_bar         : bool                              = False          ,
        display_rgb       : bool                              = False          ,
        display_hsv       : bool                              = False          ,
        display_hex       : bool                              = False          ,
        picker_mode       : int                               = 33554432       ,
        alpha_preview     : int                               = 0              ,
        display_type      : int                               = 8388608        ,
        input_mode        : int                               = 134217728      ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_side_preview=no_side_preview,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            alpha_bar=alpha_bar,
            display_rgb=display_rgb,
            display_hsv=display_hsv,
            display_hex=display_hex,
            picker_mode=picker_mode,
            alpha_preview=alpha_preview,
            display_type=display_type,
            input_mode=input_mode,
            **kwargs,
        )


class ColorMapScale(Widget):
    """Adds a legend that pairs values with colors. This is typically used with a heat series. 
    
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
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		colormap (Union[int, str], optional): mvPlotColormap_* constants or mvColorMap uuid from a color map registry
    		min_scale (float, optional): Sets the min number of the color scale. Typically is the same as the min scale from the heat series.
    		max_scale (float, optional): Sets the max number of the color scale. Typically is the same as the max scale from the heat series.
    		id (Union[int, str], optional): (deprecated) 
    		drag_callback (Callable, optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source              : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type        : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    colormap            : Union[int, str]                   = ItemAttribute('configuration', 'get_item_cached', 'set_item_cached_colormap', None)
    min_scale           : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    max_scale           : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         

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
    _unique_constants   : tuple                             = ('mvColorMapScale',)                                                               
    _command            : Callable                          = dearpygui.add_colormap_scale                                                       

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
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        colormap          : Union[int, str]                   = 0              ,
        min_scale         : float                             = 0.0            ,
        max_scale         : float                             = 1.0            ,
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
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            colormap=colormap,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )


class ColorMap(Widget):
    """Adds a legend that pairs colors with normalized value 0.0->1.0. Each color will be  This is typically used with a heat series. (ex. [[0, 0, 0, 255], [255, 255, 255, 255]] will be mapped to a soft transition from 0.0-1.0)
    
    	Args:
    		colors (Any): colors that will be mapped to the normalized value 0.0->1.0
    		qualitative (bool): Qualitative will create hard transitions for color boundries across the value range when enabled.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    colors            : List[Union[List[int], Tuple[int, ...]]] = ItemAttribute("configuration", "get_item_cached", None, None)                                                                                                                                                                                                                                                                                                                                                              
    qualitative       : bool                                    = ItemAttribute("configuration", "get_item_cached", None, None)                                                                                                                                                                                                                                                                                                                                                                  
    label             : str                                     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                              
    user_data         : Any                                     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                              
    use_internal_label: bool                                    = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                              
    show              : bool                                    = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                              

    _is_container     : bool                                    = False                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _is_root_item     : bool                                    = False                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _is_value_able    : bool                                    = False                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _unique_parents   : tuple                                   = ('ColorMapRegistry', 'TemplateRegistry')                                                                                                                                                                                                                                                                                                                                                                                                
    _unique_children  : tuple                                   = ()                                                                                                                                                                                                                                                                                                                                                                                                                                      
    _unique_commands  : tuple                                   = ('bind_colormap', 'sample_colormap', 'get_colormap_color')                                                                                                                                                                                                                                                                                                                                                                              
    _unique_constants : tuple                                   = ('mvColorMap', 'mvPlotColormap_Default', 'mvPlotColormap_Deep', 'mvPlotColormap_Dark', 'mvPlotColormap_Pastel', 'mvPlotColormap_Paired', 'mvPlotColormap_Viridis', 'mvPlotColormap_Plasma', 'mvPlotColormap_Hot', 'mvPlotColormap_Cool', 'mvPlotColormap_Pink', 'mvPlotColormap_Jet', 'mvPlotColormap_Twilight', 'mvPlotColormap_RdBu', 'mvPlotColormap_BrBG', 'mvPlotColormap_PiYG', 'mvPlotColormap_Spectral', 'mvPlotColormap_Greys')
    _command          : Callable                                = dearpygui.add_colormap                                                                                                                                                                                                                                                                                                                                                                                                                  

    def __init__(
        self                                                             ,
        colors            : List[Union[List[int], Tuple[int, ...]]]      ,
        qualitative       : bool                                         ,
        label             : str                                    = None,
        user_data         : Any                                    = None,
        use_internal_label: bool                                   = True,
        show              : bool                                   = True,
        parent            : Union[int, str]                        = 14  ,
        **kwargs                                                         ,
    ) -> None:
        super().__init__(
            colors=colors,
            qualitative=qualitative,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            parent=parent,
            **kwargs,
        )


class ColorMapButton(Widget):
    """Adds a button that a color map can be bound to.
    
    	Args:
    		default_value (Union[List[int], Tuple[int, ...]], optional): 
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
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    default_value       : Union[List[int], Tuple[int, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type        : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    enabled             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key          : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset        : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value               : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

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
    _unique_constants   : tuple                             = ('mvColorMapButton',)                                                              
    _command            : Callable                          = dearpygui.add_colormap_button                                                      

    def __init__(
        self                                                                   ,
        default_value     : Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255) ,
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
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            **kwargs,
        )


class ColorMapSlider(Widget):
    """Adds a color slider that a color map can be bound to.
    
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
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    		drag_callback (Callable, optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data                : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width                    : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback                 : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_callback", None)         
    show                     : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)          
    filter_key               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset             : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value            : float                             = ItemAttribute('information', 'get_item_cached', None, None)                        
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
    _unique_constants        : tuple                             = ('mvColorMapSlider',)                                                              
    _command                 : Callable                          = dearpygui.add_colormap_slider                                                      

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
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
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
            payload_type=payload_type,
            callback=callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            **kwargs,
        )
