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
    "Plot",
    "PlotLegend",
    "PlotAxis",
    "DragPoint",
    "DragLine",
    "Annotation",
    "SubPlots",
    "SimplePlot",
    "LineSeries",
    "BarSeries",
    "ScatterSeries",
    "AreaSeries",
    "StemSeries",
    "LabelSeries",
    "PieSeries",
    "ShadeSeries",
    "ErrorSeries",
    "HeatSeries",
    "ImageSeries",
    "StairSeries",
    "CandleSeries",
    "VLineSeries",
    "HistogramSeries",
    "HistogramSeries2D",
]


class Plot(Container):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.
    
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
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		no_title (bool, optional): 
    		no_menus (bool, optional): 
    		no_box_select (bool, optional): 
    		no_mouse_pos (bool, optional): 
    		no_highlight (bool, optional): 
    		no_child (bool, optional): 
    		query (bool, optional): 
    		crosshairs (bool, optional): 
    		anti_aliased (bool, optional): 
    		equal_aspects (bool, optional): 
    		pan_button (int, optional): enables panning when held
    		pan_mod (int, optional): optional modifier that must be held for panning
    		fit_button (int, optional): fits visible data when double clicked
    		context_menu_button (int, optional): opens plot context menu (if enabled) when clicked
    		box_select_button (int, optional): begins box selection when pressed and confirms selection when released
    		box_select_mod (int, optional): begins box selection when pressed and confirms selection when released
    		box_select_cancel_button (int, optional): cancels active box selection when pressed
    		query_button (int, optional): begins query selection when pressed and end query selection when released
    		query_mod (int, optional): optional modifier that must be held for query selection
    		query_toggle_mod (int, optional): when held, active box selections turn into queries
    		horizontal_mod (int, optional): expands active box selection/query horizontally to plot edge when held
    		vertical_mod (int, optional): expands active box selection/query vertically to plot edge when held
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                   : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    user_data               : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    use_internal_label      : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    width                   : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    height                  : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    indent                  : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    payload_type            : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    callback                : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    drag_callback           : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    drop_callback           : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    show                    : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    pos                     : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    filter_key              : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    delay_search            : bool                              = ItemAttribute('information', 'get_item_cached', None, None)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    tracked                 : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    track_offset            : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_title                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_menus                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_box_select           : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_mouse_pos            : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_highlight            : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    no_child                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    query                   : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    crosshairs              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    anti_aliased            : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    equal_aspects           : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    pan_button              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    pan_mod                 : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    fit_button              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    context_menu_button     : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    box_select_button       : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    box_select_mod          : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    box_select_cancel_button: int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    query_button            : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    query_mod               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    query_toggle_mod        : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    horizontal_mod          : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    vertical_mod            : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                                                                                                                                                                                                                                                                                     

    is_resized              : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    is_middle_clicked       : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    is_right_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    is_left_clicked         : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    is_hovered              : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    is_active               : bool                              = ItemAttribute("state", "get_item_state", None, "active")                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    is_focused              : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    is_clicked              : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    is_visible              : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    is_activated            : bool                              = ItemAttribute("state", "get_item_state", None, "activated")                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    is_deactivated          : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    rect_min                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    rect_max                : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    rect_size               : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    content_region_avail    : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    _is_container           : bool                              = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    _is_root_item           : bool                              = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    _is_value_able          : bool                              = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    _unique_parents         : tuple                             = ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    _unique_children        : tuple                             = ('PlotLegend', 'PlotAxis', 'DragPoint', 'DragLine', 'Annotation', 'DrawLine', 'DrawArrow', 'DrawTriangle', 'DrawCircle', 'DrawEllipse', 'DrawBezierCubic', 'DrawBezierQuadratic', 'DrawQuad', 'DrawRect', 'DrawText', 'DrawPolygon', 'DrawPolyline', 'DrawImage', 'DrawLayer', 'ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler', 'DragPayload', 'DrawNode')
    _unique_commands        : tuple                             = ('is_plot_queried', 'get_plot_query_area')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    _unique_constants       : tuple                             = ('mvPlot', 'mvPlotMarker_None', 'mvPlotMarker_Circle', 'mvPlotMarker_Square', 'mvPlotMarker_Diamond', 'mvPlotMarker_Up', 'mvPlotMarker_Down', 'mvPlotMarker_Left', 'mvPlotMarker_Right', 'mvPlotMarker_Cross', 'mvPlotMarker_Plus', 'mvPlotMarker_Asterisk')                                                                                                                                                                                                                                                                   
    _command                : Callable                          = dearpygui.add_plot                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

    def __init__(
        self                                                                         ,
        label                   : str                               = None           ,
        user_data               : Any                               = None           ,
        use_internal_label      : bool                              = True           ,
        width                   : int                               = 0              ,
        height                  : int                               = 0              ,
        indent                  : int                               = -1             ,
        parent                  : Union[int, str]                   = 0              ,
        before                  : Union[int, str]                   = 0              ,
        payload_type            : str                               = '$$DPG_PAYLOAD',
        callback                : Callable                          = None           ,
        drag_callback           : Callable                          = None           ,
        drop_callback           : Callable                          = None           ,
        show                    : bool                              = True           ,
        pos                     : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key              : str                               = ''             ,
        delay_search            : bool                              = False          ,
        tracked                 : bool                              = False          ,
        track_offset            : float                             = 0.5            ,
        no_title                : bool                              = False          ,
        no_menus                : bool                              = False          ,
        no_box_select           : bool                              = False          ,
        no_mouse_pos            : bool                              = False          ,
        no_highlight            : bool                              = False          ,
        no_child                : bool                              = False          ,
        query                   : bool                              = False          ,
        crosshairs              : bool                              = False          ,
        anti_aliased            : bool                              = False          ,
        equal_aspects           : bool                              = False          ,
        pan_button              : int                               = 0              ,
        pan_mod                 : int                               = -1             ,
        fit_button              : int                               = 0              ,
        context_menu_button     : int                               = 1              ,
        box_select_button       : int                               = 1              ,
        box_select_mod          : int                               = -1             ,
        box_select_cancel_button: int                               = 0              ,
        query_button            : int                               = 2              ,
        query_mod               : int                               = -1             ,
        query_toggle_mod        : int                               = 17             ,
        horizontal_mod          : int                               = 18             ,
        vertical_mod            : int                               = 16             ,
        **kwargs                                                                     ,
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
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            no_title=no_title,
            no_menus=no_menus,
            no_box_select=no_box_select,
            no_mouse_pos=no_mouse_pos,
            no_highlight=no_highlight,
            no_child=no_child,
            query=query,
            crosshairs=crosshairs,
            anti_aliased=anti_aliased,
            equal_aspects=equal_aspects,
            pan_button=pan_button,
            pan_mod=pan_mod,
            fit_button=fit_button,
            context_menu_button=context_menu_button,
            box_select_button=box_select_button,
            box_select_mod=box_select_mod,
            box_select_cancel_button=box_select_cancel_button,
            query_button=query_button,
            query_mod=query_mod,
            query_toggle_mod=query_toggle_mod,
            horizontal_mod=horizontal_mod,
            vertical_mod=vertical_mod,
            **kwargs,
        )


class PlotLegend(Container):
    """Adds a plot legend to a plot.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		location (int, optional): location, mvPlot_Location_*
    		horizontal (bool, optional): 
    		outside (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    payload_type      : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    drop_callback     : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    location          : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    horizontal        : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      
    outside           : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                                      

    _is_container     : bool     = True                                                                                                                                                                                                                                                            
    _is_root_item     : bool     = False                                                                                                                                                                                                                                                           
    _is_value_able    : bool     = False                                                                                                                                                                                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'Plot', 'SubPlots')                                                                                                                                                                                                               
    _unique_children  : tuple    = ()                                                                                                                                                                                                                                                              
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                                                              
    _unique_constants : tuple    = ('mvPlotLegend', 'mvPlot_Location_Center', 'mvPlot_Location_North', 'mvPlot_Location_South', 'mvPlot_Location_West', 'mvPlot_Location_East', 'mvPlot_Location_NorthWest', 'mvPlot_Location_NorthEast', 'mvPlot_Location_SouthWest', 'mvPlot_Location_SouthEast')
    _command          : Callable = dearpygui.add_plot_legend                                                                                                                                                                                                                                       

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        location          : int             = 5              ,
        horizontal        : bool            = False          ,
        outside           : bool            = False          ,
        **kwargs                                             ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            location=location,
            horizontal=horizontal,
            outside=outside,
            **kwargs,
        )


class PlotAxis(Container):
    """Adds an axis to a plot.
    
    	Args:
    		axis (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		no_gridlines (bool, optional): 
    		no_tick_marks (bool, optional): 
    		no_tick_labels (bool, optional): 
    		log_scale (bool, optional): 
    		invert (bool, optional): 
    		lock_min (bool, optional): 
    		lock_max (bool, optional): 
    		time (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    axis              : int      = ItemAttribute("configuration", "get_item_cached", "set_item_cached_config", None)                                       
    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    payload_type      : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    drop_callback     : Callable = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    no_gridlines      : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    no_tick_marks     : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    no_tick_labels    : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    log_scale         : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    invert            : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    lock_min          : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    lock_max          : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           
    time              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                           

    _is_container     : bool     = True                                                                                                                 
    _is_root_item     : bool     = False                                                                                                                
    _is_value_able    : bool     = False                                                                                                                
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'Plot')                                                                                
    _unique_children  : tuple    = ()                                                                                                                   
    _unique_commands  : tuple    = ('reset_axis_ticks', 'set_axis_ticks', 'set_axis_limits', 'set_axis_limits_auto', 'get_axis_limits', 'fit_axis_data')
    _unique_constants : tuple    = ('mvPlotAxis', 'mvXAxis', 'mvYAxis')                                                                                 
    _command          : Callable = dearpygui.add_plot_axis                                                                                              

    def __init__(
        self                                                 ,
        axis              : int                              ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        no_gridlines      : bool            = False          ,
        no_tick_marks     : bool            = False          ,
        no_tick_labels    : bool            = False          ,
        log_scale         : bool            = False          ,
        invert            : bool            = False          ,
        lock_min          : bool            = False          ,
        lock_max          : bool            = False          ,
        time              : bool            = False          ,
        **kwargs                                             ,
    ) -> None:
        super().__init__(
            axis=axis,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            no_gridlines=no_gridlines,
            no_tick_marks=no_tick_marks,
            no_tick_labels=no_tick_labels,
            log_scale=log_scale,
            invert=invert,
            lock_min=lock_min,
            lock_max=lock_max,
            time=time,
            **kwargs,
        )


class DragPoint(Widget):
    """Adds a drag point to a plot.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		default_value (Any, optional): 
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		show_label (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback          : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Any                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    color             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    thickness         : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show_label        : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Any                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                              = False                                                                              
    _is_root_item     : bool                              = False                                                                              
    _is_value_able    : bool                              = True                                                                               
    _unique_parents   : tuple                             = ('Stage', 'TemplateRegistry', 'Plot')                                              
    _unique_children  : tuple                             = ()                                                                                 
    _unique_commands  : tuple                             = ()                                                                                 
    _unique_constants : tuple                             = ('mvDragPoint',)                                                                   
    _command          : Callable                          = dearpygui.add_drag_point                                                           

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        callback          : Callable                          = None           ,
        show              : bool                              = True           ,
        default_value     : Any                               = (0.0, 0.0)     ,
        color             : Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255),
        thickness         : float                             = 1.0            ,
        show_label        : bool                              = True           ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            **kwargs,
        )


class DragLine(Widget):
    """Adds a drag line to a plot.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		default_value (Any, optional): 
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		show_label (bool, optional): 
    		vertical (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    callback          : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Any                               = ItemAttribute('information', 'get_item_cached', None, None)                        
    color             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    thickness         : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show_label        : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    vertical          : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Any                               = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                              = False                                                                              
    _is_root_item     : bool                              = False                                                                              
    _is_value_able    : bool                              = True                                                                               
    _unique_parents   : tuple                             = ('Stage', 'TemplateRegistry', 'Plot')                                              
    _unique_children  : tuple                             = ()                                                                                 
    _unique_commands  : tuple                             = ()                                                                                 
    _unique_constants : tuple                             = ('mvDragLine',)                                                                    
    _command          : Callable                          = dearpygui.add_drag_line                                                            

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        source            : Union[int, str]                   = 0              ,
        callback          : Callable                          = None           ,
        show              : bool                              = True           ,
        default_value     : Any                               = 0.0            ,
        color             : Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255),
        thickness         : float                             = 1.0            ,
        show_label        : bool                              = True           ,
        vertical          : bool                              = True           ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            vertical=vertical,
            **kwargs,
        )


class Annotation(Widget):
    """Adds an annotation to a plot.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		default_value (Any, optional): 
    		offset (Union[List[float], Tuple[float, ...]], optional): 
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		clamped (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Any                                   = ItemAttribute('information', 'get_item_cached', None, None)                        
    offset            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    clamped           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Any                                   = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ('Stage', 'TemplateRegistry', 'Plot')                                              
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvAnnotation',)                                                                  
    _command          : Callable                              = dearpygui.add_plot_annotation                                                      

    def __init__(
        self                                                                       ,
        label             : str                                   = None           ,
        user_data         : Any                                   = None           ,
        use_internal_label: bool                                  = True           ,
        parent            : Union[int, str]                       = 0              ,
        before            : Union[int, str]                       = 0              ,
        source            : Union[int, str]                       = 0              ,
        show              : bool                                  = True           ,
        default_value     : Any                                   = (0.0, 0.0)     ,
        offset            : Union[List[float], Tuple[float, ...]] = (0.0, 0.0)     ,
        color             : Union[List[int], Tuple[int, ...]]     = (0, 0, 0, -255),
        clamped           : bool                                  = True           ,
        **kwargs                                                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            default_value=default_value,
            offset=offset,
            color=color,
            clamped=clamped,
            **kwargs,
        )


class SubPlots(Container):
    """Adds a collection of plots.
    
    	Args:
    		rows (int): 
    		columns (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		row_ratios (Union[List[float], Tuple[float, ...]], optional): 
    		column_ratios (Union[List[float], Tuple[float, ...]], optional): 
    		no_title (bool, optional): 
    		no_menus (bool, optional): the user will not be able to open context menus with right-click
    		no_resize (bool, optional): resize splitters between subplot cells will be not be provided
    		no_align (bool, optional): subplot edges will not be aligned vertically or horizontally
    		link_rows (bool, optional): link the y-axis limits of all plots in each row (does not apply auxiliary y-axes)
    		link_columns (bool, optional): link the x-axis limits of all plots in each column
    		link_all_x (bool, optional): link the x-axis limits in every plot in the subplot
    		link_all_y (bool, optional): link the y-axis limits in every plot in the subplot (does not apply to auxiliary y-axes)
    		column_major (bool, optional): subplots are added in column major order instead of the default row major order
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    rows              : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    columns           : int                                   = ItemAttribute('configuration', 'get_item_config', 'set_item_config', 'cols')
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    width             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    height            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    indent            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    callback          : Callable                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    pos               : Union[List[int], Tuple[int, ...]]     = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)   
    filter_key        : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    delay_search      : bool                                  = ItemAttribute('information', 'get_item_cached', None, None)                 
    tracked           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    track_offset      : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    row_ratios        : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    column_ratios     : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    no_title          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    no_menus          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    no_resize         : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    no_align          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    link_rows         : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    link_columns      : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    link_all_x        : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    link_all_y        : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  
    column_major      : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)  

    _is_container     : bool                                  = True                                                                        
    _is_root_item     : bool                                  = False                                                                       
    _is_value_able    : bool                                  = False                                                                       
    _unique_parents   : tuple                                 = ()                                                                          
    _unique_children  : tuple                                 = ('Plot', 'PlotLegend')                                                      
    _unique_commands  : tuple                                 = ()                                                                          
    _unique_constants : tuple                                 = ('mvSubPlots',)                                                             
    _command          : Callable                              = dearpygui.add_subplots                                                      

    def __init__(
        self                                                             ,
        rows              : int                                          ,
        columns           : int                                          ,
        label             : str                                   = None ,
        user_data         : Any                                   = None ,
        use_internal_label: bool                                  = True ,
        width             : int                                   = 0    ,
        height            : int                                   = 0    ,
        indent            : int                                   = -1   ,
        parent            : Union[int, str]                       = 0    ,
        before            : Union[int, str]                       = 0    ,
        callback          : Callable                              = None ,
        show              : bool                                  = True ,
        pos               : Union[List[int], Tuple[int, ...]]     = []   ,
        filter_key        : str                                   = ''   ,
        delay_search      : bool                                  = False,
        tracked           : bool                                  = False,
        track_offset      : float                                 = 0.5  ,
        row_ratios        : Union[List[float], Tuple[float, ...]] = []   ,
        column_ratios     : Union[List[float], Tuple[float, ...]] = []   ,
        no_title          : bool                                  = False,
        no_menus          : bool                                  = False,
        no_resize         : bool                                  = False,
        no_align          : bool                                  = False,
        link_rows         : bool                                  = False,
        link_columns      : bool                                  = False,
        link_all_x        : bool                                  = False,
        link_all_y        : bool                                  = False,
        column_major      : bool                                  = False,
        **kwargs                                                         ,
    ) -> None:
        super().__init__(
            rows=rows,
            columns=columns,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            callback=callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            row_ratios=row_ratios,
            column_ratios=column_ratios,
            no_title=no_title,
            no_menus=no_menus,
            no_resize=no_resize,
            no_align=no_align,
            link_rows=link_rows,
            link_columns=link_columns,
            link_all_x=link_all_x,
            link_all_y=link_all_y,
            column_major=column_major,
            **kwargs,
        )


class SimplePlot(Widget):
    """Adds a simple plot for visualization of a 1 dimensional set of values.
    
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
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_value (Union[List[float], Tuple[float, ...]], optional): 
    		overlay (str, optional): overlays text (similar to a plot title)
    		histogram (bool, optional): 
    		autosize (bool, optional): 
    		min_scale (float, optional): 
    		max_scale (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    width             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    height            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    indent            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    payload_type      : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drag_callback     : Callable                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    drop_callback     : Callable                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    filter_key        : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    tracked           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    track_offset      : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    default_value     : Union[List[float], Tuple[float, ...]] = ItemAttribute('information', 'get_item_cached', None, None)                        
    overlay           : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    histogram         : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    autosize          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    min_scale         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    max_scale         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)         
    value             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")

    _is_container     : bool                                  = False                                                                              
    _is_root_item     : bool                                  = False                                                                              
    _is_value_able    : bool                                  = True                                                                               
    _unique_parents   : tuple                                 = ()                                                                                 
    _unique_children  : tuple                                 = ()                                                                                 
    _unique_commands  : tuple                                 = ()                                                                                 
    _unique_constants : tuple                                 = ('mvSimplePlot',)                                                                  
    _command          : Callable                              = dearpygui.add_simple_plot                                                          

    def __init__(
        self                                                                       ,
        label             : str                                   = None           ,
        user_data         : Any                                   = None           ,
        use_internal_label: bool                                  = True           ,
        width             : int                                   = 0              ,
        height            : int                                   = 0              ,
        indent            : int                                   = -1             ,
        parent            : Union[int, str]                       = 0              ,
        before            : Union[int, str]                       = 0              ,
        source            : Union[int, str]                       = 0              ,
        payload_type      : str                                   = '$$DPG_PAYLOAD',
        drag_callback     : Callable                              = None           ,
        drop_callback     : Callable                              = None           ,
        show              : bool                                  = True           ,
        filter_key        : str                                   = ''             ,
        tracked           : bool                                  = False          ,
        track_offset      : float                                 = 0.5            ,
        default_value     : Union[List[float], Tuple[float, ...]] = ()             ,
        overlay           : str                                   = ''             ,
        histogram         : bool                                  = False          ,
        autosize          : bool                                  = True           ,
        min_scale         : float                                 = 0.0            ,
        max_scale         : float                                 = 0.0            ,
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
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            overlay=overlay,
            histogram=histogram,
            autosize=autosize,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )


class LineSeries(Container):
    """Adds a line series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvLineSeries',)                                                         
    _command          : Callable                              = dearpygui.add_line_series                                                 

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        y                 : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )


class BarSeries(Container):
    """Adds a bar series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		weight (float, optional): 
    		horizontal (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    weight            : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    horizontal        : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvBarSeries',)                                                          
    _command          : Callable                              = dearpygui.add_bar_series                                                  

    def __init__(
        self                                                            ,
        x                 : Union[List[float], Tuple[float, ...]]       ,
        y                 : Union[List[float], Tuple[float, ...]]       ,
        label             : str                                  = None ,
        user_data         : Any                                  = None ,
        use_internal_label: bool                                 = True ,
        parent            : Union[int, str]                      = 0    ,
        before            : Union[int, str]                      = 0    ,
        source            : Union[int, str]                      = 0    ,
        show              : bool                                 = True ,
        weight            : float                                = 1.0  ,
        horizontal        : bool                                 = False,
        **kwargs                                                        ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            weight=weight,
            horizontal=horizontal,
            **kwargs,
        )


class ScatterSeries(Container):
    """Adds a scatter series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvScatterSeries',)                                                      
    _command          : Callable                              = dearpygui.add_scatter_series                                              

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        y                 : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )


class AreaSeries(Container):
    """Adds an area series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		contribute_to_bounds (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label               : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show                : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    fill                : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    contribute_to_bounds: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container       : bool                                  = True                                                                      
    _is_root_item       : bool                                  = False                                                                     
    _is_value_able      : bool                                  = True                                                                      
    _unique_parents     : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children    : tuple                                 = ()                                                                        
    _unique_commands    : tuple                                 = ()                                                                        
    _unique_constants   : tuple                                 = ('mvAreaSeries',)                                                         
    _command            : Callable                              = dearpygui.add_area_series                                                 

    def __init__(
        self                                                                        ,
        x                   : Union[List[float], Tuple[float, ...]]                 ,
        y                   : Union[List[float], Tuple[float, ...]]                 ,
        label               : str                                  = None           ,
        user_data           : Any                                  = None           ,
        use_internal_label  : bool                                 = True           ,
        parent              : Union[int, str]                      = 0              ,
        before              : Union[int, str]                      = 0              ,
        source              : Union[int, str]                      = 0              ,
        show                : bool                                 = True           ,
        fill                : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255),
        contribute_to_bounds: bool                                 = True           ,
        **kwargs                                                                    ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            fill=fill,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )


class StemSeries(Container):
    """Adds a stem series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    indent            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvStemSeries',)                                                         
    _command          : Callable                              = dearpygui.add_stem_series                                                 

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        y                 : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        indent            : int                                  = -1  ,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )


class LabelSeries(Container):
    """Adds a label series to a plot.
    
    	Args:
    		x (float): 
    		y (float): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		x_offset (int, optional): 
    		y_offset (int, optional): 
    		vertical (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : float           = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : float           = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    x_offset          : int             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y_offset          : int             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    vertical          : bool            = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool            = True                                                                      
    _is_root_item     : bool            = False                                                                     
    _is_value_able    : bool            = True                                                                      
    _unique_parents   : tuple           = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple           = ()                                                                        
    _unique_commands  : tuple           = ()                                                                        
    _unique_constants : tuple           = ('mvLabelSeries',)                                                        
    _command          : Callable        = dearpygui.add_text_point                                                  

    def __init__(
        self                                          ,
        x                 : float                     ,
        y                 : float                     ,
        label             : str             = None    ,
        user_data         : Any             = None    ,
        use_internal_label: bool            = True    ,
        parent            : Union[int, str] = 0       ,
        before            : Union[int, str] = 0       ,
        source            : Union[int, str] = 0       ,
        show              : bool            = True    ,
        x_offset          : int             = Ellipsis,
        y_offset          : int             = Ellipsis,
        vertical          : bool            = False   ,
        **kwargs                                      ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            x_offset=x_offset,
            y_offset=y_offset,
            vertical=vertical,
            **kwargs,
        )


class PieSeries(Container):
    """Adds an pie series to a plot.
    
    	Args:
    		x (float): 
    		y (float): 
    		radius (float): 
    		values (Any): 
    		labels (Union[List[str], Tuple[str, ...]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		format (str, optional): 
    		angle (float, optional): 
    		normalize (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    radius            : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    values            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    labels            : Union[List[str], Tuple[str, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    format            : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    angle             : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    normalize         : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvPieSeries',)                                                          
    _command          : Callable                              = dearpygui.add_pie_series                                                  

    def __init__(
        self                                                              ,
        x                 : float                                         ,
        y                 : float                                         ,
        radius            : float                                         ,
        values            : Union[List[float], Tuple[float, ...]]         ,
        labels            : Union[List[str], Tuple[str, ...]]             ,
        label             : str                                  = None   ,
        user_data         : Any                                  = None   ,
        use_internal_label: bool                                 = True   ,
        parent            : Union[int, str]                      = 0      ,
        before            : Union[int, str]                      = 0      ,
        source            : Union[int, str]                      = 0      ,
        show              : bool                                 = True   ,
        format            : str                                  = '%0.2f',
        angle             : float                                = 90.0   ,
        normalize         : bool                                 = False  ,
        **kwargs                                                          ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            radius=radius,
            values=values,
            labels=labels,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            format=format,
            angle=angle,
            normalize=normalize,
            **kwargs,
        )


class ShadeSeries(Container):
    """Adds a shade series to a plot.
    
    	Args:
    		x (Any): 
    		y1 (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		y2 (Any, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y2                : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvShadeSeries',)                                                        
    _command          : Callable                              = dearpygui.add_shade_series                                                

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        y1                : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        y2                : Any                                  = []  ,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            y1=y1,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            y2=y2,
            **kwargs,
        )


class ErrorSeries(Container):
    """Adds an error series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		negative (Any): 
    		positive (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		contribute_to_bounds (bool, optional): 
    		horizontal (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    negative            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    positive            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label               : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show                : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    contribute_to_bounds: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    horizontal          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container       : bool                                  = True                                                                      
    _is_root_item       : bool                                  = False                                                                     
    _is_value_able      : bool                                  = True                                                                      
    _unique_parents     : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children    : tuple                                 = ()                                                                        
    _unique_commands    : tuple                                 = ()                                                                        
    _unique_constants   : tuple                                 = ('mvErrorSeries',)                                                        
    _command            : Callable                              = dearpygui.add_error_series                                                

    def __init__(
        self                                                              ,
        x                   : Union[List[float], Tuple[float, ...]]       ,
        y                   : Union[List[float], Tuple[float, ...]]       ,
        negative            : Union[List[float], Tuple[float, ...]]       ,
        positive            : Union[List[float], Tuple[float, ...]]       ,
        label               : str                                  = None ,
        user_data           : Any                                  = None ,
        use_internal_label  : bool                                 = True ,
        parent              : Union[int, str]                      = 0    ,
        before              : Union[int, str]                      = 0    ,
        source              : Union[int, str]                      = 0    ,
        show                : bool                                 = True ,
        contribute_to_bounds: bool                                 = True ,
        horizontal          : bool                                 = False,
        **kwargs                                                          ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            negative=negative,
            positive=positive,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
            horizontal=horizontal,
            **kwargs,
        )


class HeatSeries(Container):
    """Adds a heat series to a plot.
    
    	Args:
    		x (Any): 
    		rows (int): 
    		cols (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		scale_min (float, optional): Sets the color scale min. Typically paired with the color scale widget scale_min.
    		scale_max (float, optional): Sets the color scale max. Typically paired with the color scale widget scale_max.
    		bounds_min (Any, optional): 
    		bounds_max (Any, optional): 
    		format (str, optional): 
    		contribute_to_bounds (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    rows                : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    cols                : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label               : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show                : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    scale_min           : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    scale_max           : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bounds_min          : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bounds_max          : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    format              : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    contribute_to_bounds: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container       : bool                                  = True                                                                      
    _is_root_item       : bool                                  = False                                                                     
    _is_value_able      : bool                                  = True                                                                      
    _unique_parents     : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children    : tuple                                 = ()                                                                        
    _unique_commands    : tuple                                 = ()                                                                        
    _unique_constants   : tuple                                 = ('mvHeatSeries',)                                                         
    _command            : Callable                              = dearpygui.add_heat_series                                                 

    def __init__(
        self                                                                   ,
        x                   : Union[List[float], Tuple[float, ...]]            ,
        rows                : int                                              ,
        cols                : int                                              ,
        label               : str                                  = None      ,
        user_data           : Any                                  = None      ,
        use_internal_label  : bool                                 = True      ,
        parent              : Union[int, str]                      = 0         ,
        before              : Union[int, str]                      = 0         ,
        source              : Union[int, str]                      = 0         ,
        show                : bool                                 = True      ,
        scale_min           : float                                = 0.0       ,
        scale_max           : float                                = 1.0       ,
        bounds_min          : Any                                  = (0.0, 0.0),
        bounds_max          : Any                                  = (1.0, 1.0),
        format              : str                                  = '%0.1f'   ,
        contribute_to_bounds: bool                                 = True      ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            x=x,
            rows=rows,
            cols=cols,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            scale_min=scale_min,
            scale_max=scale_max,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            format=format,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )


class ImageSeries(Container):
    """Adds an image series to a plot.
    
    	Args:
    		texture_tag (Union[int, str]): 
    		bounds_min (Any): 
    		bounds_max (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		uv_min (Union[List[float], Tuple[float, ...]], optional): normalized texture coordinates
    		uv_max (Union[List[float], Tuple[float, ...]], optional): normalized texture coordinates
    		tint_color (Union[List[int], Tuple[int, ...]], optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    texture_tag       : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bounds_min        : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bounds_max        : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    uv_min            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    uv_max            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    tint_color        : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvImageSeries',)                                                        
    _command          : Callable                              = dearpygui.add_image_series                                                

    def __init__(
        self                                                                            ,
        texture_tag       : Union[int, str]                                             ,
        bounds_min        : Union[List[float], Tuple[float, ...]]                       ,
        bounds_max        : Union[List[float], Tuple[float, ...]]                       ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        parent            : Union[int, str]                       = 0                   ,
        before            : Union[int, str]                       = 0                   ,
        source            : Union[int, str]                       = 0                   ,
        show              : bool                                  = True                ,
        uv_min            : Union[List[float], Tuple[float, ...]] = (0.0, 0.0)          ,
        uv_max            : Union[List[float], Tuple[float, ...]] = (1.0, 1.0)          ,
        tint_color        : Union[List[int], Tuple[int, ...]]     = (255, 255, 255, 255),
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            uv_min=uv_min,
            uv_max=uv_max,
            tint_color=tint_color,
            **kwargs,
        )


class StairSeries(Container):
    """Adds a stair series to a plot.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvStairSeries',)                                                        
    _command          : Callable                              = dearpygui.add_stair_series                                                

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        y                 : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )


class CandleSeries(Container):
    """Adds a candle series to a plot.
    
    	Args:
    		dates (Any): 
    		opens (Any): 
    		closes (Any): 
    		lows (Any): 
    		highs (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		bull_color (Union[List[int], Tuple[int, ...]], optional): 
    		bear_color (Union[List[int], Tuple[int, ...]], optional): 
    		weight (int, optional): 
    		tooltip (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    dates             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    opens             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    closes            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    lows              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    highs             : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bull_color        : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    bear_color        : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    weight            : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    tooltip           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvCandleSeries',)                                                       
    _command          : Callable                              = dearpygui.add_candle_series                                               

    def __init__(
        self                                                                         ,
        dates             : Union[List[float], Tuple[float, ...]]                    ,
        opens             : Union[List[float], Tuple[float, ...]]                    ,
        closes            : Union[List[float], Tuple[float, ...]]                    ,
        lows              : Union[List[float], Tuple[float, ...]]                    ,
        highs             : Union[List[float], Tuple[float, ...]]                    ,
        label             : str                                  = None              ,
        user_data         : Any                                  = None              ,
        use_internal_label: bool                                 = True              ,
        parent            : Union[int, str]                      = 0                 ,
        before            : Union[int, str]                      = 0                 ,
        source            : Union[int, str]                      = 0                 ,
        show              : bool                                 = True              ,
        bull_color        : Union[List[int], Tuple[int, ...]]    = (0, 255, 113, 255),
        bear_color        : Union[List[int], Tuple[int, ...]]    = (218, 13, 79, 255),
        weight            : int                                  = 0.25              ,
        tooltip           : bool                                 = True              ,
        **kwargs                                                                     ,
    ) -> None:
        super().__init__(
            dates=dates,
            opens=opens,
            closes=closes,
            lows=lows,
            highs=highs,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            bull_color=bull_color,
            bear_color=bear_color,
            weight=weight,
            tooltip=tooltip,
            **kwargs,
        )


class VLineSeries(Container):
    """Adds an infinite vertical line series to a plot.
    
    	Args:
    		x (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mvInfiniteLineSeries',)                                                 
    _command          : Callable                              = dearpygui.add_vline_series                                                

    def __init__(
        self                                                           ,
        x                 : Union[List[float], Tuple[float, ...]]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Union[int, str]                      = 0   ,
        before            : Union[int, str]                      = 0   ,
        source            : Union[int, str]                      = 0   ,
        show              : bool                                 = True,
        **kwargs                                                       ,
    ) -> None:
        super().__init__(
            x=x,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )


class HistogramSeries(Container):
    """Adds a histogram series to a plot.
    
    	Args:
    		x (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		bins (int, optional): 
    		bar_scale (float, optional): 
    		min_range (float, optional): 
    		max_range (float, optional): 
    		cumlative (bool, optional): 
    		density (bool, optional): 
    		outliers (bool, optional): 
    		contribute_to_bounds (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                   : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    label               : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    user_data           : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    use_internal_label  : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    source              : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    show                : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    bins                : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    bar_scale           : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    min_range           : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    max_range           : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    cumlative           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    density             : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    outliers            : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       
    contribute_to_bounds: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                       

    _is_container       : bool                                  = True                                                                                             
    _is_root_item       : bool                                  = False                                                                                            
    _is_value_able      : bool                                  = True                                                                                             
    _unique_parents     : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                                                 
    _unique_children    : tuple                                 = ()                                                                                               
    _unique_commands    : tuple                                 = ()                                                                                               
    _unique_constants   : tuple                                 = ('mvHistogramSeries', 'mvPlotBin_Sqrt', 'mvPlotBin_Sturges', 'mvPlotBin_Rice', 'mvPlotBin_Scott')
    _command            : Callable                              = dearpygui.add_histogram_series                                                                   

    def __init__(
        self                                                              ,
        x                   : Union[List[float], Tuple[float, ...]]       ,
        label               : str                                  = None ,
        user_data           : Any                                  = None ,
        use_internal_label  : bool                                 = True ,
        parent              : Union[int, str]                      = 0    ,
        before              : Union[int, str]                      = 0    ,
        source              : Union[int, str]                      = 0    ,
        show                : bool                                 = True ,
        bins                : int                                  = -1   ,
        bar_scale           : float                                = 1.0  ,
        min_range           : float                                = 0.0  ,
        max_range           : float                                = 1.0  ,
        cumlative           : bool                                 = False,
        density             : bool                                 = False,
        outliers            : bool                                 = True ,
        contribute_to_bounds: bool                                 = True ,
        **kwargs                                                          ,
    ) -> None:
        super().__init__(
            x=x,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            bins=bins,
            bar_scale=bar_scale,
            min_range=min_range,
            max_range=max_range,
            cumlative=cumlative,
            density=density,
            outliers=outliers,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )


class HistogramSeries2D(Container):
    """Adds a 2d histogram series.
    
    	Args:
    		x (Any): 
    		y (Any): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		source (Union[int, str], optional): Overrides 'id' as value storage key.
    		show (bool, optional): Attempt to render widget.
    		xbins (int, optional): 
    		ybins (int, optional): 
    		xmin_range (float, optional): 
    		xmax_range (float, optional): 
    		ymin_range (float, optional): 
    		ymax_range (float, optional): 
    		density (bool, optional): 
    		outliers (bool, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    x                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    y                 : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    source            : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    xbins             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    ybins             : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    xmin_range        : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    xmax_range        : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    ymin_range        : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    ymax_range        : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    density           : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    outliers          : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    _is_container     : bool                                  = True                                                                      
    _is_root_item     : bool                                  = False                                                                     
    _is_value_able    : bool                                  = True                                                                      
    _unique_parents   : tuple                                 = ('PlotAxis', 'TemplateRegistry')                                          
    _unique_children  : tuple                                 = ()                                                                        
    _unique_commands  : tuple                                 = ()                                                                        
    _unique_constants : tuple                                 = ('mv2dHistogramSeries',)                                                  
    _command          : Callable                              = dearpygui.add_2d_histogram_series                                         

    def __init__(
        self                                                            ,
        x                 : Union[List[float], Tuple[float, ...]]       ,
        y                 : Union[List[float], Tuple[float, ...]]       ,
        label             : str                                  = None ,
        user_data         : Any                                  = None ,
        use_internal_label: bool                                 = True ,
        parent            : Union[int, str]                      = 0    ,
        before            : Union[int, str]                      = 0    ,
        source            : Union[int, str]                      = 0    ,
        show              : bool                                 = True ,
        xbins             : int                                  = -1   ,
        ybins             : int                                  = -1   ,
        xmin_range        : float                                = 0.0  ,
        xmax_range        : float                                = 1.0  ,
        ymin_range        : float                                = 0.0  ,
        ymax_range        : float                                = 1.0  ,
        density           : bool                                 = False,
        outliers          : bool                                 = True ,
        **kwargs                                                        ,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            xbins=xbins,
            ybins=ybins,
            xmin_range=xmin_range,
            xmax_range=xmax_range,
            ymin_range=ymin_range,
            ymax_range=ymax_range,
            density=density,
            outliers=outliers,
            **kwargs,
        )
