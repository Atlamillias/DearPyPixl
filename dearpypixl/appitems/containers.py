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
    "FilterSet",
    "Clipper",
    "Stage",
    "TreeNode",
    "ChildWindow",
    "Group",
    "CollapsingHeader",
    "Tab",
    "TabBar",
    "Menu",
    "MenuBar",
    "Tooltip",
    "Window",
    "DragPayload",
    "ViewportMenuBar",
]


class FilterSet(Container):
    """Helper to parse and apply text filters (e.g. aaaaa[, bbbbb][, ccccc])
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    indent            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    delay_search      : bool     = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvFilterSet',)                                                                                
    _command          : Callable = dearpygui.add_filter_set                                                                        

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        width             : int             = 0    ,
        indent            : int             = -1   ,
        parent            : Union[int, str] = 0    ,
        before            : Union[int, str] = 0    ,
        show              : bool            = True ,
        delay_search      : bool            = False,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            delay_search=delay_search,
            **kwargs,
        )


class Clipper(Container):
    """Helper to manually clip large list of items. Increases performance by not searching or drawing widgets outside of the clipped region.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width             : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    indent            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    delay_search      : bool     = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvClipper',)                                                                                  
    _command          : Callable = dearpygui.add_clipper                                                                           

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        width             : int             = 0    ,
        indent            : int             = -1   ,
        parent            : Union[int, str] = 0    ,
        before            : Union[int, str] = 0    ,
        show              : bool            = True ,
        delay_search      : bool            = False,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            delay_search=delay_search,
            **kwargs,
        )


class Stage(Container):
    """Adds a stage.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvStage',)                                                                                    
    _command          : Callable = dearpygui.add_stage                                                                             

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


class TreeNode(Container):
    """Adds a tree node to add items to.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		default_open (bool, optional): Sets the tree node open by default.
    		open_on_double_click (bool, optional): Need double-click to open node.
    		open_on_arrow (bool, optional): Only open when clicking on the arrow part.
    		leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf nodes).
    		bullet (bool, optional): Display a bullet instead of arrow.
    		selectable (bool, optional): Makes the tree selectable.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")               
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")           
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")  
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")              
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")        
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")       
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")       
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                         
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")          
    delay_search        : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                             
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")             
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")        
    default_open        : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'default_open')                             
    open_on_double_click: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "open_on_double_click")
    open_on_arrow       : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "open_on_arrow")       
    leaf                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "leaf")                
    bullet              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "bullet")              
    selectable          : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "selectable")          

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
    is_toggled_open     : bool                              = ItemAttribute("state", "get_item_state", None, "toggled_open")                                    
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                        
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                        
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                       
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                            

    _is_container       : bool                              = True                                                                                              
    _is_root_item       : bool                              = False                                                                                             
    _is_value_able      : bool                              = True                                                                                              
    _unique_parents     : tuple                             = ()                                                                                                
    _unique_children    : tuple                             = ()                                                                                                
    _unique_commands    : tuple                             = ()                                                                                                
    _unique_constants   : tuple                             = ('mvTreeNode',)                                                                                   
    _command            : Callable                          = dearpygui.add_tree_node                                                                           

    def __init__(
        self                                                                     ,
        label               : str                               = None           ,
        user_data           : Any                               = None           ,
        use_internal_label  : bool                              = True           ,
        indent              : int                               = -1             ,
        parent              : Union[int, str]                   = 0              ,
        before              : Union[int, str]                   = 0              ,
        payload_type        : str                               = '$$DPG_PAYLOAD',
        drag_callback       : Callable                          = None           ,
        drop_callback       : Callable                          = None           ,
        show                : bool                              = True           ,
        pos                 : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key          : str                               = ''             ,
        delay_search        : bool                              = False          ,
        tracked             : bool                              = False          ,
        track_offset        : float                             = 0.5            ,
        default_open        : bool                              = False          ,
        open_on_double_click: bool                              = False          ,
        open_on_arrow       : bool                              = False          ,
        leaf                : bool                              = False          ,
        bullet              : bool                              = False          ,
        selectable          : bool                              = False          ,
        **kwargs                                                                 ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
            selectable=selectable,
            **kwargs,
        )


class ChildWindow(Container):
    """Adds an embedded child window. Will show scrollbars when items do not fit.
    
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
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		border (bool, optional): Shows/Hides the border around the sides.
    		autosize_x (bool, optional): Autosize the window to fit it's items in the x.
    		autosize_y (bool, optional): Autosize the window to fit it's items in the y.
    		no_scrollbar (bool, optional):  Disable scrollbars (window can still scroll with mouse or programmatically).
    		horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear (off by default).
    		menubar (bool, optional): Shows/Hides the menubar at the top.
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
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")          
    delay_search        : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                             
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")             
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")        
    border              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "border")              
    autosize_x          : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "autosize_x")          
    autosize_y          : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "autosize_y")          
    no_scrollbar        : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_scrollbar")        
    horizontal_scrollbar: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "horizontal_scrollbar")
    menubar             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "menubar")             

    is_resized          : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                         
    is_hovered          : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                         
    is_active           : bool                              = ItemAttribute("state", "get_item_state", None, "active")                                          
    is_focused          : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                         
    is_deactivated      : bool                              = ItemAttribute("state", "get_item_state", None, "deactivated")                                     
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                       
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                            

    _is_container       : bool                              = True                                                                                              
    _is_root_item       : bool                              = False                                                                                             
    _is_value_able      : bool                              = True                                                                                              
    _unique_parents     : tuple                             = ()                                                                                                
    _unique_children    : tuple                             = ()                                                                                                
    _unique_commands    : tuple                             = ()                                                                                                
    _unique_constants   : tuple                             = ('mvChild',)                                                                                      
    _command            : Callable                          = dearpygui.add_child_window                                                                        

    def __init__(
        self                                                                     ,
        label               : str                               = None           ,
        user_data           : Any                               = None           ,
        use_internal_label  : bool                              = True           ,
        width               : int                               = 0              ,
        height              : int                               = 0              ,
        indent              : int                               = -1             ,
        parent              : Union[int, str]                   = 0              ,
        before              : Union[int, str]                   = 0              ,
        payload_type        : str                               = '$$DPG_PAYLOAD',
        drop_callback       : Callable                          = None           ,
        show                : bool                              = True           ,
        pos                 : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key          : str                               = ''             ,
        delay_search        : bool                              = False          ,
        tracked             : bool                              = False          ,
        track_offset        : float                             = 0.5            ,
        border              : bool                              = True           ,
        autosize_x          : bool                              = False          ,
        autosize_y          : bool                              = False          ,
        no_scrollbar        : bool                              = False          ,
        horizontal_scrollbar: bool                              = False          ,
        menubar             : bool                              = False          ,
        **kwargs                                                                 ,
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
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            border=border,
            autosize_x=autosize_x,
            autosize_y=autosize_y,
            no_scrollbar=no_scrollbar,
            horizontal_scrollbar=horizontal_scrollbar,
            menubar=menubar,
            **kwargs,
        )


class Group(Container):
    """Creates a group that other widgets can belong to. The group allows item commands to be issued for all of its members.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		horizontal (bool, optional): Forces child widgets to be added in a horizontal layout.
    		horizontal_spacing (float, optional): Spacing for the horizontal layout.
    		xoffset (float, optional): Offset from containing window x item location within group.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                    : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data                : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label       : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    width                    : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")             
    indent                   : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    payload_type             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    drag_callback            : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")     
    drop_callback            : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show                     : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    pos                      : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                       
    filter_key               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    delay_search             : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           
    tracked                  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset             : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      
    horizontal               : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "horizontal")        
    horizontal_spacing       : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "horizontal_spacing")
    xoffset                  : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "xoffset")           

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

    _is_container            : bool                              = True                                                                                            
    _is_root_item            : bool                              = False                                                                                           
    _is_value_able           : bool                              = False                                                                                           
    _unique_parents          : tuple                             = ()                                                                                              
    _unique_children         : tuple                             = ()                                                                                              
    _unique_commands         : tuple                             = ()                                                                                              
    _unique_constants        : tuple                             = ('mvGroup',)                                                                                    
    _command                 : Callable                          = dearpygui.add_group                                                                             

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
        width             : int                               = 0              ,
        indent            : int                               = -1             ,
        parent            : Union[int, str]                   = 0              ,
        before            : Union[int, str]                   = 0              ,
        payload_type      : str                               = '$$DPG_PAYLOAD',
        drag_callback     : Callable                          = None           ,
        drop_callback     : Callable                          = None           ,
        show              : bool                              = True           ,
        pos               : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key        : str                               = ''             ,
        delay_search      : bool                              = False          ,
        tracked           : bool                              = False          ,
        track_offset      : float                             = 0.5            ,
        horizontal        : bool                              = False          ,
        horizontal_spacing: float                             = -1             ,
        xoffset           : float                             = 0.0            ,
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
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            horizontal=horizontal,
            horizontal_spacing=horizontal_spacing,
            xoffset=xoffset,
            **kwargs,
        )


class CollapsingHeader(Container):
    """Adds a collapsing header to add items to. Must be closed with the end command.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drag_callback (Callable, optional): Registers a drag callback for drag and drop.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		closable (bool, optional): Adds the ability to hide this widget by pressing the (x) in the top right of widget.
    		default_open (bool, optional): Sets the collapseable header open by default.
    		open_on_double_click (bool, optional): Need double-click to open node.
    		open_on_arrow (bool, optional): Only open when clicking on the arrow part.
    		leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf nodes).
    		bullet (bool, optional): Display a bullet instead of arrow.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")               
    user_data           : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")           
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")  
    indent              : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")              
    payload_type        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")        
    drag_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")       
    drop_callback       : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")       
    show                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                         
    filter_key          : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")          
    delay_search        : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                             
    tracked             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")             
    track_offset        : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")        
    closable            : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "closable")            
    default_open        : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'default_open')                             
    open_on_double_click: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "open_on_double_click")
    open_on_arrow       : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "open_on_arrow")       
    leaf                : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "leaf")                
    bullet              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "bullet")              

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
    is_toggled_open     : bool                              = ItemAttribute("state", "get_item_state", None, "toggled_open")                                    
    rect_min            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_min")                                        
    rect_max            : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_max")                                        
    rect_size           : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                       
    content_region_avail: list[int, int]                    = ItemAttribute("state", "get_item_state", None, "content_region_avail")                            

    _is_container       : bool                              = True                                                                                              
    _is_root_item       : bool                              = False                                                                                             
    _is_value_able      : bool                              = True                                                                                              
    _unique_parents     : tuple                             = ()                                                                                                
    _unique_children    : tuple                             = ()                                                                                                
    _unique_commands    : tuple                             = ()                                                                                                
    _unique_constants   : tuple                             = ('mvCollapsingHeader',)                                                                           
    _command            : Callable                          = dearpygui.add_collapsing_header                                                                   

    def __init__(
        self                                                                     ,
        label               : str                               = None           ,
        user_data           : Any                               = None           ,
        use_internal_label  : bool                              = True           ,
        indent              : int                               = -1             ,
        parent              : Union[int, str]                   = 0              ,
        before              : Union[int, str]                   = 0              ,
        payload_type        : str                               = '$$DPG_PAYLOAD',
        drag_callback       : Callable                          = None           ,
        drop_callback       : Callable                          = None           ,
        show                : bool                              = True           ,
        pos                 : Union[List[int], Tuple[int, ...]] = []             ,
        filter_key          : str                               = ''             ,
        delay_search        : bool                              = False          ,
        tracked             : bool                              = False          ,
        track_offset        : float                             = 0.5            ,
        closable            : bool                              = False          ,
        default_open        : bool                              = False          ,
        open_on_double_click: bool                              = False          ,
        open_on_arrow       : bool                              = False          ,
        leaf                : bool                              = False          ,
        bullet              : bool                              = False          ,
        **kwargs                                                                 ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            closable=closable,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
            **kwargs,
        )


class Tab(Container):
    """Adds a tab to a tab bar.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		closable (bool, optional): Creates a button on the tab that can hide the tab.
    		no_tooltip (bool, optional): Disable tooltip for the given tab.
    		order_mode (bool, optional): set using a constant: mvTabOrder_Reorderable: allows reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to front, mvTabOrder_Trailing: adds tab to back
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                 
    user_data           : Any            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")             
    use_internal_label  : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")    
    indent              : int            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")                
    payload_type        : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")          
    drop_callback       : Callable       = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")         
    show                : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                  
    filter_key          : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")            
    delay_search        : bool           = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                               
    tracked             : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")               
    track_offset        : float          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")          
    closable            : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "closable")              
    no_tooltip          : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_tooltip")            
    order_mode          : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "order_mode")            

    is_resized          : bool           = ItemAttribute("state", "get_item_state", None, "resized")                                           
    is_middle_clicked   : bool           = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                    
    is_right_clicked    : bool           = ItemAttribute("state", "get_item_state", None, "right_clicked")                                     
    is_left_clicked     : bool           = ItemAttribute("state", "get_item_state", None, "left_clicked")                                      
    is_hovered          : bool           = ItemAttribute("state", "get_item_state", None, "hovered")                                           
    is_active           : bool           = ItemAttribute("state", "get_item_state", None, "active")                                            
    is_clicked          : bool           = ItemAttribute("state", "get_item_state", None, "clicked")                                           
    is_visible          : bool           = ItemAttribute("state", "get_item_state", None, "visible")                                           
    is_activated        : bool           = ItemAttribute("state", "get_item_state", None, "activated")                                         
    is_deactivated      : bool           = ItemAttribute("state", "get_item_state", None, "deactivated")                                       
    rect_min            : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_min")                                          
    rect_max            : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_max")                                          
    rect_size           : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_size")                                         
    content_region_avail: list[int, int] = ItemAttribute("state", "get_item_state", None, "content_region_avail")                              

    _is_container       : bool           = True                                                                                                
    _is_root_item       : bool           = False                                                                                               
    _is_value_able      : bool           = True                                                                                                
    _unique_parents     : tuple          = ('TabBar', 'Stage', 'TemplateRegistry')                                                             
    _unique_children    : tuple          = ()                                                                                                  
    _unique_commands    : tuple          = ()                                                                                                  
    _unique_constants   : tuple          = ('mvTab', 'mvTabOrder_Reorderable', 'mvTabOrder_Fixed', 'mvTabOrder_Leading', 'mvTabOrder_Trailing')
    _command            : Callable       = dearpygui.add_tab                                                                                   

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        indent            : int             = -1             ,
        parent            : Union[int, str] = 0              ,
        before            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        filter_key        : str             = ''             ,
        delay_search      : bool            = False          ,
        tracked           : bool            = False          ,
        track_offset      : float           = 0.5            ,
        closable          : bool            = False          ,
        no_tooltip        : bool            = False          ,
        order_mode        : bool            = 0              ,
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
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            closable=closable,
            no_tooltip=no_tooltip,
            order_mode=order_mode,
            **kwargs,
        )


class TabBar(Container):
    """Adds a tab bar.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
    		reorderable (bool, optional): Allows for the user to change the order of the tabs.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                                                       
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                                                   
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                                          
    indent            : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")                                                                                                                                                      
    callback          : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")                                                                                                                                                    
    show              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                                        
    pos               : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                                                                                                                                                                 
    filter_key        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")                                                                                                                                                  
    delay_search      : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                                                                                                                                                                     
    tracked           : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")                                                                                                                                                     
    track_offset      : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")                                                                                                                                                
    reorderable       : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "reorderable")                                                                                                                                                 

    is_visible        : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                                                                                                                                                                 

    _is_container     : bool                              = True                                                                                                                                                                                                                                      
    _is_root_item     : bool                              = False                                                                                                                                                                                                                                     
    _is_value_able    : bool                              = True                                                                                                                                                                                                                                      
    _unique_parents   : tuple                             = ()                                                                                                                                                                                                                                        
    _unique_children  : tuple                             = ('Tab', 'TabButton', 'ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    _unique_commands  : tuple                             = ()                                                                                                                                                                                                                                        
    _unique_constants : tuple                             = ('mvTabBar',)                                                                                                                                                                                                                             
    _command          : Callable                          = dearpygui.add_tab_bar                                                                                                                                                                                                                     

    def __init__(
        self                                                         ,
        label             : str                               = None ,
        user_data         : Any                               = None ,
        use_internal_label: bool                              = True ,
        indent            : int                               = -1   ,
        parent            : Union[int, str]                   = 0    ,
        before            : Union[int, str]                   = 0    ,
        callback          : Callable                          = None ,
        show              : bool                              = True ,
        pos               : Union[List[int], Tuple[int, ...]] = []   ,
        filter_key        : str                               = ''   ,
        delay_search      : bool                              = False,
        tracked           : bool                              = False,
        track_offset      : float                             = 0.5  ,
        reorderable       : bool                              = False,
        **kwargs                                                     ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            reorderable=reorderable,
            **kwargs,
        )


class Menu(Container):
    """Adds a menu to an existing menu bar.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
    		drop_callback (Callable, optional): Registers a drop callback for drag and drop.
    		show (bool, optional): Attempt to render widget.
    		enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent            : int            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    payload_type      : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")      
    drop_callback     : Callable       = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")     
    show              : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    enabled           : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "enabled")           
    filter_key        : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")        
    delay_search      : bool           = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           
    tracked           : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")           
    track_offset      : float          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")      

    is_resized        : bool           = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_hovered        : bool           = ItemAttribute("state", "get_item_state", None, "hovered")                                       
    is_active         : bool           = ItemAttribute("state", "get_item_state", None, "active")                                        
    is_focused        : bool           = ItemAttribute("state", "get_item_state", None, "focused")                                       
    is_activated      : bool           = ItemAttribute("state", "get_item_state", None, "activated")                                     
    is_deactivated    : bool           = ItemAttribute("state", "get_item_state", None, "deactivated")                                   
    rect_size         : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_size")                                     

    _is_container     : bool           = True                                                                                            
    _is_root_item     : bool           = False                                                                                           
    _is_value_able    : bool           = True                                                                                            
    _unique_parents   : tuple          = ()                                                                                              
    _unique_children  : tuple          = ()                                                                                              
    _unique_commands  : tuple          = ()                                                                                              
    _unique_constants : tuple          = ('mvMenu',)                                                                                     
    _command          : Callable       = dearpygui.add_menu                                                                              

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        indent            : int             = -1             ,
        parent            : Union[int, str] = 0              ,
        before            : Union[int, str] = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        enabled           : bool            = True           ,
        filter_key        : str             = ''             ,
        delay_search      : bool            = False          ,
        tracked           : bool            = False          ,
        track_offset      : float           = 0.5            ,
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
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            **kwargs,
        )


class MenuBar(Container):
    """Adds a menu bar to a window.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		show (bool, optional): Attempt to render widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    delay_search      : bool     = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           

    is_visible        : bool     = ItemAttribute("state", "get_item_state", None, "visible")                                       

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = True                                                                                            
    _unique_parents   : tuple    = ('Window', 'ChildWindow', 'NodeEditor', 'Stage', 'TemplateRegistry')                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMenuBar',)                                                                                  
    _command          : Callable = dearpygui.add_menu_bar                                                                          

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        indent            : int             = -1   ,
        parent            : Union[int, str] = 0    ,
        show              : bool            = True ,
        delay_search      : bool            = False,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
            **kwargs,
        )


class Tooltip(Container):
    """Adds a tooltip window.
    
    	Args:
    		parent (Union[int, str]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label               : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data           : Any            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label  : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    show                : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    is_resized          : bool           = ItemAttribute("state", "get_item_state", None, "resized")                                       
    is_visible          : bool           = ItemAttribute("state", "get_item_state", None, "visible")                                       
    rect_size           : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_size")                                     
    content_region_avail: list[int, int] = ItemAttribute("state", "get_item_state", None, "content_region_avail")                          

    _is_container       : bool           = True                                                                                            
    _is_root_item       : bool           = False                                                                                           
    _is_value_able      : bool           = True                                                                                            
    _unique_parents     : tuple          = ()                                                                                              
    _unique_children    : tuple          = ()                                                                                              
    _unique_commands    : tuple          = ()                                                                                              
    _unique_constants   : tuple          = ('mvTooltip',)                                                                                  
    _command            : Callable       = dearpygui.add_tooltip                                                                           

    def __init__(
        self                                     ,
        parent            : Union[int, str]      ,
        label             : str            = None,
        user_data         : Any            = None,
        use_internal_label: bool           = True,
        show              : bool           = True,
        **kwargs                                 ,
    ) -> None:
        super().__init__(
            parent=parent,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class Window(Container):
    """Creates a new window for following items to be added to.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		min_size (Union[List[int], Tuple[int, ...]], optional): Minimum window size.
    		max_size (Union[List[int], Tuple[int, ...]], optional): Maximum window size.
    		menubar (bool, optional): Shows or hides the menubar.
    		collapsed (bool, optional): Collapse the window.
    		autosize (bool, optional): Autosized the window to fit it's items.
    		no_resize (bool, optional): Allows for the window size to be changed or fixed.
    		no_title_bar (bool, optional): Title name for the title bar of the window.
    		no_move (bool, optional): Allows for the window's position to be changed or fixed.
    		no_scrollbar (bool, optional):  Disable scrollbars. (window can still scroll with mouse or programmatically)
    		no_collapse (bool, optional): Disable user collapsing window by double-clicking on it.
    		horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear. (off by default)
    		no_focus_on_appearing (bool, optional): Disable taking focus when transitioning from hidden to visible state.
    		no_bring_to_front_on_focus (bool, optional): Disable bringing window to front when taking focus. (e.g. clicking on it or programmatically giving it focus)
    		no_close (bool, optional): Disable user closing the window by removing the close button.
    		no_background (bool, optional): Sets Background and border alpha to transparent.
    		modal (bool, optional): Fills area behind window according to the theme and disables user ability to interact with anything except the window.
    		popup (bool, optional): Fills area behind window according to the theme, removes title bar, collapse and close. Window can be closed by selecting area in the background behind the window.
    		no_saved_settings (bool, optional): Never load/save settings in .ini file.
    		on_close (Callable, optional): Callback ran when window is closed.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label                     : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                     
    user_data                 : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                 
    use_internal_label        : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")        
    width                     : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")                     
    height                    : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")                    
    indent                    : int                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")                    
    show                      : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                      
    pos                       : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                               
    delay_search              : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                                   
    min_size                  : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "min_size")                  
    max_size                  : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "max_size")                  
    menubar                   : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "menubar")                   
    collapsed                 : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "collapsed")                 
    autosize                  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "autosize")                  
    no_resize                 : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_resize")                 
    no_title_bar              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_title_bar")              
    no_move                   : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_move")                   
    no_scrollbar              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_scrollbar")              
    no_collapse               : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_collapse")               
    horizontal_scrollbar      : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "horizontal_scrollbar")      
    no_focus_on_appearing     : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_focus_on_appearing")     
    no_bring_to_front_on_focus: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_bring_to_front_on_focus")
    no_close                  : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_close")                  
    no_background             : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_background")             
    modal                     : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "modal")                     
    popup                     : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "popup")                     
    no_saved_settings         : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "no_saved_settings")         
    on_close                  : Callable                          = ItemAttribute('information', 'get_unmanagable', None, 'on_close')                                       

    is_resized                : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                               
    is_hovered                : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                               
    is_focused                : bool                              = ItemAttribute("state", "get_item_state", None, "focused")                                               
    is_visible                : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                               
    rect_size                 : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                             
    is_toggled_open           : bool                              = ItemAttribute("state", "get_item_state", None, "toggled_open")                                          

    _is_container             : bool                              = True                                                                                                    
    _is_root_item             : bool                              = True                                                                                                    
    _is_value_able            : bool                              = False                                                                                                   
    _unique_parents           : tuple                             = ()                                                                                                      
    _unique_children          : tuple                             = ()                                                                                                      
    _unique_commands          : tuple                             = ('set_x_scroll', 'set_y_scroll', 'get_x_scroll', 'get_y_scroll', 'get_x_scroll_max', 'get_y_scroll_max')
    _unique_constants         : tuple                             = ('mvWindowAppItem',)                                                                                    
    _command                  : Callable                          = dearpygui.add_window                                                                                    

    def __init__(
        self                                                                          ,
        label                     : str                               = None          ,
        user_data                 : Any                               = None          ,
        use_internal_label        : bool                              = True          ,
        width                     : int                               = 0             ,
        height                    : int                               = 0             ,
        indent                    : int                               = -1            ,
        show                      : bool                              = True          ,
        pos                       : Union[List[int], Tuple[int, ...]] = []            ,
        delay_search              : bool                              = False         ,
        min_size                  : Union[List[int], Tuple[int, ...]] = [100, 100]    ,
        max_size                  : Union[List[int], Tuple[int, ...]] = [30000, 30000],
        menubar                   : bool                              = False         ,
        collapsed                 : bool                              = False         ,
        autosize                  : bool                              = False         ,
        no_resize                 : bool                              = False         ,
        no_title_bar              : bool                              = False         ,
        no_move                   : bool                              = False         ,
        no_scrollbar              : bool                              = False         ,
        no_collapse               : bool                              = False         ,
        horizontal_scrollbar      : bool                              = False         ,
        no_focus_on_appearing     : bool                              = False         ,
        no_bring_to_front_on_focus: bool                              = False         ,
        no_close                  : bool                              = False         ,
        no_background             : bool                              = False         ,
        modal                     : bool                              = False         ,
        popup                     : bool                              = False         ,
        no_saved_settings         : bool                              = False         ,
        on_close                  : Callable                          = None          ,
        **kwargs                                                                      ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            show=show,
            pos=pos,
            delay_search=delay_search,
            min_size=min_size,
            max_size=max_size,
            menubar=menubar,
            collapsed=collapsed,
            autosize=autosize,
            no_resize=no_resize,
            no_title_bar=no_title_bar,
            no_move=no_move,
            no_scrollbar=no_scrollbar,
            no_collapse=no_collapse,
            horizontal_scrollbar=horizontal_scrollbar,
            no_focus_on_appearing=no_focus_on_appearing,
            no_bring_to_front_on_focus=no_bring_to_front_on_focus,
            no_close=no_close,
            no_background=no_background,
            modal=modal,
            popup=popup,
            no_saved_settings=no_saved_settings,
            on_close=on_close,
            **kwargs,
        )


class DragPayload(Container):
    """User data payload for drag and drop operations.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		show (bool, optional): Attempt to render widget.
    		drag_data (Any, optional): Drag data
    		drop_data (Any, optional): Drop data
    		payload_type (str, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    drag_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_data")                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    drop_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_data")                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    payload_type      : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    _is_container     : bool     = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    _is_root_item     : bool     = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    _is_value_able    : bool     = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    _unique_parents   : tuple    = ('Button', 'Checkbox', 'Combo', 'DragIntMulti', 'DragFloatMulti', 'DragInt', 'DragFloat', 'Image', 'ImageButton', 'InputIntMulti', 'InputFloatMulti', 'InputInt', 'InputFloat', 'InputText', 'Listbox', 'MenuItem', 'RadioButton', 'Selectable', 'SliderIntMulti', 'SliderFloatMulti', 'SliderInt', 'SliderFloat', 'TabButton', 'Text', 'ColorButton', 'ColorEdit', 'ColorMapButton', 'ColorPicker', 'CollapsingHeader', 'Group', 'TreeNode', 'DatePicker', 'KnobFloat', 'LoadingIndicator', 'Slider3D', 'TimePicker', 'ProgressBar', 'Node', 'Plot')
    _unique_children  : tuple    = ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _unique_constants : tuple    = ('mvDragPayload',)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    _command          : Callable = dearpygui.add_drag_payload                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : Union[int, str] = 0              ,
        show              : bool            = True           ,
        drag_data         : Any             = None           ,
        drop_data         : Any             = None           ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        **kwargs                                             ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            show=show,
            drag_data=drag_data,
            drop_data=drop_data,
            payload_type=payload_type,
            **kwargs,
        )


class ViewportMenuBar(Container):
    """Adds a menubar to the viewport.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		show (bool, optional): Attempt to render widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    indent            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")            
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              
    delay_search      : bool     = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                           

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvViewportMenuBar',)                                                                          
    _command          : Callable = dearpygui.add_viewport_menu_bar                                                                 

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        indent            : int             = -1   ,
        parent            : Union[int, str] = 0    ,
        show              : bool            = True ,
        delay_search      : bool            = False,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
            **kwargs,
        )
