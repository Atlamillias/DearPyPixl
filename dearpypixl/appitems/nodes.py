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
    "NodeEditor",
    "Node",
    "NodeAttribute",
    "NodeLink",
]


class NodeEditor(Container):
    """Adds a node editor.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		width (int, optional): Width of the item.
    		height (int, optional): Height of the item.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		delink_callback (Callable, optional): Callback ran when a link is detached.
    		menubar (bool, optional): Shows or hides the menubar.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                                                                  
    user_data         : Any            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                                                              
    use_internal_label: bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                                                     
    width             : int            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "width")                                                                                                                                                                  
    height            : int            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "height")                                                                                                                                                                 
    callback          : Callable       = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")                                                                                                                                                               
    show              : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                                                   
    filter_key        : str            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")                                                                                                                                                             
    delay_search      : bool           = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                                                                                                                                                                                
    tracked           : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")                                                                                                                                                                
    track_offset      : float          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")                                                                                                                                                           
    delink_callback   : Callable       = ItemAttribute("configuration", "get_item_configuration", "configure_item", "delink_callback")                                                                                                                                                        
    menubar           : bool           = ItemAttribute("configuration", "get_item_configuration", "configure_item", "menubar")                                                                                                                                                                

    is_resized        : bool           = ItemAttribute("state", "get_item_state", None, "resized")                                                                                                                                                                                            
    is_hovered        : bool           = ItemAttribute("state", "get_item_state", None, "hovered")                                                                                                                                                                                            
    is_visible        : bool           = ItemAttribute("state", "get_item_state", None, "visible")                                                                                                                                                                                            
    rect_size         : list[int, int] = ItemAttribute("state", "get_item_state", None, "rect_size")                                                                                                                                                                                          

    _is_container     : bool           = True                                                                                                                                                                                                                                                 
    _is_root_item     : bool           = False                                                                                                                                                                                                                                                
    _is_value_able    : bool           = False                                                                                                                                                                                                                                                
    _unique_parents   : tuple          = ()                                                                                                                                                                                                                                                   
    _unique_children  : tuple          = ('MenuBar', 'Node', 'NodeLink', 'ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    _unique_commands  : tuple          = ('get_selected_nodes', 'get_selected_links', 'clear_selected_nodes', 'clear_selected_links')                                                                                                                                                         
    _unique_constants : tuple          = ('mvNodeEditor',)                                                                                                                                                                                                                                    
    _command          : Callable       = dearpygui.add_node_editor                                                                                                                                                                                                                            

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        width             : int             = 0    ,
        height            : int             = 0    ,
        parent            : Union[int, str] = 0    ,
        before            : Union[int, str] = 0    ,
        callback          : Callable        = None ,
        show              : bool            = True ,
        filter_key        : str             = ''   ,
        delay_search      : bool            = False,
        tracked           : bool            = False,
        track_offset      : float           = 0.5  ,
        delink_callback   : Callable        = ''   ,
        menubar           : bool            = False,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            callback=callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            delink_callback=delink_callback,
            menubar=menubar,
            **kwargs,
        )


class Node(Container):
    """Adds a node to a node editor.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
    		draggable (bool, optional): Allow node to be draggable.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                  
    user_data         : Any                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")              
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")     
    payload_type      : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "payload_type")           
    drag_callback     : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drag_callback")          
    drop_callback     : Callable                          = ItemAttribute("configuration", "get_item_configuration", "configure_item", "drop_callback")          
    show              : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                   
    pos               : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'configure_item', 'pos')                            
    filter_key        : str                               = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")             
    delay_search      : bool                              = ItemAttribute('information', 'get_unmanagable', None, 'delay_search')                                
    tracked           : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")                
    track_offset      : float                             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")           
    draggable         : bool                              = ItemAttribute("configuration", "get_item_configuration", "configure_item", "draggable")              

    is_resized        : bool                              = ItemAttribute("state", "get_item_state", None, "resized")                                            
    is_middle_clicked : bool                              = ItemAttribute("state", "get_item_state", None, "middle_clicked")                                     
    is_right_clicked  : bool                              = ItemAttribute("state", "get_item_state", None, "right_clicked")                                      
    is_left_clicked   : bool                              = ItemAttribute("state", "get_item_state", None, "left_clicked")                                       
    is_hovered        : bool                              = ItemAttribute("state", "get_item_state", None, "hovered")                                            
    is_clicked        : bool                              = ItemAttribute("state", "get_item_state", None, "clicked")                                            
    is_visible        : bool                              = ItemAttribute("state", "get_item_state", None, "visible")                                            
    rect_size         : list[int, int]                    = ItemAttribute("state", "get_item_state", None, "rect_size")                                          

    _is_container     : bool                              = True                                                                                                 
    _is_root_item     : bool                              = False                                                                                                
    _is_value_able    : bool                              = False                                                                                                
    _unique_parents   : tuple                             = ('TemplateRegistry', 'Stage', 'NodeEditor')                                                          
    _unique_children  : tuple                             = ('NodeAttribute', 'ActiveHandler', 'ClickedHandler', 'HoverHandler', 'VisibleHandler', 'DragPayload')
    _unique_commands  : tuple                             = ()                                                                                                   
    _unique_constants : tuple                             = ('mvNode',)                                                                                          
    _command          : Callable                          = dearpygui.add_node                                                                                   

    def __init__(
        self                                                                   ,
        label             : str                               = None           ,
        user_data         : Any                               = None           ,
        use_internal_label: bool                              = True           ,
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
        draggable         : bool                              = True           ,
        **kwargs                                                               ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            draggable=draggable,
            **kwargs,
        )


class NodeAttribute(Container):
    """Adds a node attribute to a node.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		filter_key (str, optional): Used by filter widget.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		attribute_type (int, optional): mvNode_Attr_Input, mvNode_Attr_Output, or mvNode_Attr_Static.
    		shape (int, optional): Pin shape.
    		category (str, optional): Category
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                                                                               
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                                                                           
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                                                                  
    indent            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "indent")                                                                                                                                                                              
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                                                                
    filter_key        : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "filter_key")                                                                                                                                                                          
    tracked           : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "tracked")                                                                                                                                                                             
    track_offset      : float    = ItemAttribute("configuration", "get_item_configuration", "configure_item", "track_offset")                                                                                                                                                                        
    attribute_type    : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "attribute_type")                                                                                                                                                                      
    shape             : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "shape")                                                                                                                                                                               
    category          : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "category")                                                                                                                                                                            

    is_hovered        : bool     = ItemAttribute("state", "get_item_state", None, "hovered")                                                                                                                                                                                                         

    _is_container     : bool     = True                                                                                                                                                                                                                                                              
    _is_root_item     : bool     = False                                                                                                                                                                                                                                                             
    _is_value_able    : bool     = False                                                                                                                                                                                                                                                             
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'Node')                                                                                                                                                                                                                             
    _unique_children  : tuple    = ()                                                                                                                                                                                                                                                                
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                                                                
    _unique_constants : tuple    = ('mvNodeAttribute', 'mvNode_PinShape_Circle', 'mvNode_PinShape_CircleFilled', 'mvNode_PinShape_Triangle', 'mvNode_PinShape_TriangleFilled', 'mvNode_PinShape_Quad', 'mvNode_PinShape_QuadFilled', 'mvNode_Attr_Input', 'mvNode_Attr_Output', 'mvNode_Attr_Static')
    _command          : Callable = dearpygui.add_node_attribute                                                                                                                                                                                                                                      

    def __init__(
        self                                           ,
        label             : str             = None     ,
        user_data         : Any             = None     ,
        use_internal_label: bool            = True     ,
        indent            : int             = -1       ,
        parent            : Union[int, str] = 0        ,
        before            : Union[int, str] = 0        ,
        show              : bool            = True     ,
        filter_key        : str             = ''       ,
        tracked           : bool            = False    ,
        track_offset      : float           = 0.5      ,
        attribute_type    : int             = 0        ,
        shape             : int             = 1        ,
        category          : str             = 'general',
        **kwargs                                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            attribute_type=attribute_type,
            shape=shape,
            category=category,
            **kwargs,
        )


class NodeLink(Widget):
    """Adds a node link between 2 node attributes.
    
    	Args:
    		attr_1 (Union[int, str]): 
    		attr_2 (Union[int, str]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    attr_1            : Union[int, str] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "attr_1")            
    attr_2            : Union[int, str] = ItemAttribute("configuration", "get_item_configuration", "configure_item", "attr_2")            
    label             : str             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any             = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    show              : bool            = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    is_hovered        : bool            = ItemAttribute("state", "get_item_state", None, "hovered")                                       

    _is_container     : bool            = False                                                                                           
    _is_root_item     : bool            = False                                                                                           
    _is_value_able    : bool            = False                                                                                           
    _unique_parents   : tuple           = ('TemplateRegistry', 'Stage', 'NodeEditor')                                                     
    _unique_children  : tuple           = ()                                                                                              
    _unique_commands  : tuple           = ()                                                                                              
    _unique_constants : tuple           = ('mvNodeLink',)                                                                                 
    _command          : Callable        = dearpygui.add_node_link                                                                         

    def __init__(
        self                                      ,
        attr_1            : Union[int, str]       ,
        attr_2            : Union[int, str]       ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            attr_1=attr_1,
            attr_2=attr_2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            show=show,
            **kwargs,
        )
