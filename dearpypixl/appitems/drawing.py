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
    "Drawlist",
    "DrawLine",
    "DrawArrow",
    "DrawTriangle",
    "DrawCircle",
    "DrawEllipse",
    "DrawBezierCubic",
    "DrawBezierQuadratic",
    "DrawQuad",
    "DrawRect",
    "DrawText",
    "DrawPolygon",
    "DrawPolyline",
    "DrawImage",
    "DrawLayer",
    "ViewportDrawlist",
    "DrawImageQuad",
    "DrawNode",
]


class Drawlist(Widget):
    """Adds a drawing canvas.
    
    	Args:
    		width (int): 
    		height (int): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		tracked (bool, optional): Scroll tracking
    		track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    width               : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    height              : int                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    label               : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    user_data           : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    use_internal_label  : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    callback            : Callable                          = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    show                : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    pos                 : Union[List[int], Tuple[int, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)                                                                                                                                                                 
    filter_key          : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    delay_search        : bool                              = ItemAttribute('information', 'get_item_cached', None, None)                                                                                                                                                                               
    tracked             : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    track_offset        : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                

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

    _is_container       : bool                              = True                                                                                                                                                                                                                                      
    _is_root_item       : bool                              = False                                                                                                                                                                                                                                     
    _is_value_able      : bool                              = False                                                                                                                                                                                                                                     
    _unique_parents     : tuple                             = ()                                                                                                                                                                                                                                        
    _unique_children    : tuple                             = ('DrawLayer', 'DrawLine', 'DrawArrow', 'DrawTriangle', 'DrawCircle', 'DrawEllipse', 'DrawBezierCubic', 'DrawBezierQuadratic', 'DrawQuad', 'DrawRect', 'DrawText', 'DrawPolygon', 'DrawPolyline', 'DrawImageQuad', 'DrawImage', 'DrawNode')
    _unique_commands    : tuple                             = ()                                                                                                                                                                                                                                        
    _unique_constants   : tuple                             = ('mvDrawlist',)                                                                                                                                                                                                                           
    _command            : Callable                          = dearpygui.add_drawlist                                                                                                                                                                                                                    

    def __init__(
        self                                                         ,
        width             : int                                      ,
        height            : int                                      ,
        label             : str                               = None ,
        user_data         : Any                               = None ,
        use_internal_label: bool                              = True ,
        parent            : Union[int, str]                   = 0    ,
        before            : Union[int, str]                   = 0    ,
        callback          : Callable                          = None ,
        show              : bool                              = True ,
        pos               : Union[List[int], Tuple[int, ...]] = []   ,
        filter_key        : str                               = ''   ,
        delay_search      : bool                              = False,
        tracked           : bool                              = False,
        track_offset      : float                             = 0.5  ,
        **kwargs                                                     ,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            callback=callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            **kwargs,
        )


class DrawLine(Widget):
    """Adds a line.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): Start of line.
    		p2 (Union[List[float], Tuple[float, ...]]): End of line.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawLine',)                                                                                         
    _command          : Callable                              = dearpygui.draw_line                                                                                     

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        thickness         : float                                = 1.0                 ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            **kwargs,
        )


class DrawArrow(Widget):
    """Adds an arrow.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): Arrow tip.
    		p2 (Union[List[float], Tuple[float, ...]]): Arrow tail.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		size (int, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    size              : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist', 'TemplateRegistry')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawArrow',)                                                                                        
    _command          : Callable                              = dearpygui.draw_arrow                                                                                    

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        thickness         : float                                = 1.0                 ,
        size              : int                                  = 4                   ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            size=size,
            **kwargs,
        )


class DrawTriangle(Widget):
    """Adds a triangle.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): 
    		p2 (Union[List[float], Tuple[float, ...]]): 
    		p3 (Union[List[float], Tuple[float, ...]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p3                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'DrawNode', 'Window', 'Plot', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawTriangle', 'mvCullMode_None', 'mvCullMode_Back', 'mvCullMode_Front')                            
    _command          : Callable                              = dearpygui.draw_triangle                                                                                 

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        p3                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255)     ,
        thickness         : float                                = 1.0                 ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawCircle(Widget):
    """Adds a circle
    
    	Args:
    		center (Union[List[float], Tuple[float, ...]]): 
    		radius (float): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		segments (int, optional): Number of segments to approximate circle.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    center            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    radius            : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    segments          : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawCircle',)                                                                                       
    _command          : Callable                              = dearpygui.draw_circle                                                                                   

    def __init__(
        self                                                                           ,
        center            : Union[List[float], Tuple[float, ...]]                      ,
        radius            : float                                                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255)     ,
        thickness         : float                                = 1.0                 ,
        segments          : int                                  = 0                   ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            center=center,
            radius=radius,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawEllipse(Widget):
    """Adds an ellipse.
    
    	Args:
    		pmin (Union[List[float], Tuple[float, ...]]): Min point of bounding rectangle.
    		pmax (Union[List[float], Tuple[float, ...]]): Max point of bounding rectangle.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		segments (int, optional): Number of segments to approximate bezier curve.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    pmin              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    pmax              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    segments          : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawEllipse',)                                                                                      
    _command          : Callable                              = dearpygui.draw_ellipse                                                                                  

    def __init__(
        self                                                                           ,
        pmin              : Union[List[float], Tuple[float, ...]]                      ,
        pmax              : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255)     ,
        thickness         : float                                = 1.0                 ,
        segments          : int                                  = 32                  ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawBezierCubic(Widget):
    """Adds a cubic bezier curve.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): First point in curve.
    		p2 (Union[List[float], Tuple[float, ...]]): Second point in curve.
    		p3 (Union[List[float], Tuple[float, ...]]): Third point in curve.
    		p4 (Union[List[float], Tuple[float, ...]]): Fourth point in curve.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		segments (int, optional): Number of segments to approximate bezier curve.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p3                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p4                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    segments          : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('Stage', 'TemplateRegistry', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawBezierCubic',)                                                                                  
    _command          : Callable                              = dearpygui.draw_bezier_cubic                                                                             

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        p3                : Union[List[float], Tuple[float, ...]]                      ,
        p4                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        thickness         : float                                = 1.0                 ,
        segments          : int                                  = 0                   ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawBezierQuadratic(Widget):
    """Adds a quadratic bezier curve.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): First point in curve.
    		p2 (Union[List[float], Tuple[float, ...]]): Second point in curve.
    		p3 (Union[List[float], Tuple[float, ...]]): Third point in curve.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		segments (int, optional): Number of segments to approximate bezier curve.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p3                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    segments          : int                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawBezierQuadratic',)                                                                              
    _command          : Callable                              = dearpygui.draw_bezier_quadratic                                                                         

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        p3                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        thickness         : float                                = 1.0                 ,
        segments          : int                                  = 0                   ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawQuad(Widget):
    """Adds a quad.
    
    	Args:
    		p1 (Union[List[float], Tuple[float, ...]]): 
    		p2 (Union[List[float], Tuple[float, ...]]): 
    		p3 (Union[List[float], Tuple[float, ...]]): 
    		p4 (Union[List[float], Tuple[float, ...]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p3                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p4                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawQuad',)                                                                                         
    _command          : Callable                              = dearpygui.draw_quad                                                                                     

    def __init__(
        self                                                                           ,
        p1                : Union[List[float], Tuple[float, ...]]                      ,
        p2                : Union[List[float], Tuple[float, ...]]                      ,
        p3                : Union[List[float], Tuple[float, ...]]                      ,
        p4                : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255)     ,
        thickness         : float                                = 1.0                 ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawRect(Widget):
    """Adds a rectangle.
    
    	Args:
    		pmin (Union[List[float], Tuple[float, ...]]): Min point of bounding rectangle.
    		pmax (Union[List[float], Tuple[float, ...]]): Max point of bounding rectangle.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		color_upper_left (Union[List[int], Tuple[int, ...]], optional): 'multicolor' must be set to 'True'
    		color_upper_right (Union[List[int], Tuple[int, ...]], optional): 'multicolor' must be set to 'True'
    		color_bottom_right (Union[List[int], Tuple[int, ...]], optional): 'multicolor' must be set to 'True'
    		color_bottom_left (Union[List[int], Tuple[int, ...]], optional): 'multicolor' must be set to 'True'
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		multicolor (bool, optional): 
    		rounding (float, optional): Number of pixels of the radius that will round the corners of the rectangle. Note: doesn't work with multicolor
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    pmin              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    pmax              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color_upper_left  : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color_upper_right : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color_bottom_right: Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color_bottom_left : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    multicolor        : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    rounding          : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawRect',)                                                                                         
    _command          : Callable                              = dearpygui.draw_rectangle                                                                                

    def __init__(
        self                                                                           ,
        pmin              : Union[List[float], Tuple[float, ...]]                      ,
        pmax              : Union[List[float], Tuple[float, ...]]                      ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        color_upper_left  : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        color_upper_right : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        color_bottom_right: Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        color_bottom_left : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]]    = (0, 0, 0, -255)     ,
        multicolor        : bool                                 = False               ,
        rounding          : float                                = 0.0                 ,
        thickness         : float                                = 1.0                 ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            color_upper_left=color_upper_left,
            color_upper_right=color_upper_right,
            color_bottom_right=color_bottom_right,
            color_bottom_left=color_bottom_left,
            fill=fill,
            multicolor=multicolor,
            rounding=rounding,
            thickness=thickness,
            **kwargs,
        )


class DrawText(Widget):
    """Adds text (drawlist).
    
    	Args:
    		pos (Union[List[float], Tuple[float, ...]]): Top left point of bounding text rectangle.
    		text (str): Text to draw.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		size (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    pos               : Union[List[float], Tuple[float, ...]] = ItemAttribute('configuration', 'get_item_state', 'set_item_config', None)                               
    text              : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    size              : float                                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawText',)                                                                                         
    _command          : Callable                              = dearpygui.draw_text                                                                                     

    def __init__(
        self                                                                           ,
        pos               : Union[List[float], Tuple[float, ...]]                      ,
        text              : str                                                        ,
        label             : str                                  = None                ,
        user_data         : Any                                  = None                ,
        use_internal_label: bool                                 = True                ,
        parent            : Union[int, str]                      = 0                   ,
        before            : Union[int, str]                      = 0                   ,
        show              : bool                                 = True                ,
        color             : Union[List[int], Tuple[int, ...]]    = (255, 255, 255, 255),
        size              : float                                = 10.0                ,
        **kwargs                                                                       ,
    ) -> None:
        super().__init__(
            pos=pos,
            text=text,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            size=size,
            **kwargs,
        )


class DrawPolygon(Widget):
    """Adds a polygon.
    
    	Args:
    		points (List[List[float]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		fill (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    points            : List[List[float]]                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    fill              : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                              = False                                                                                                   
    _is_root_item     : bool                              = False                                                                                                   
    _is_value_able    : bool                              = False                                                                                                   
    _unique_parents   : tuple                             = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                             = ()                                                                                                      
    _unique_commands  : tuple                             = ()                                                                                                      
    _unique_constants : tuple                             = ('mvDrawPolygon',)                                                                                      
    _command          : Callable                          = dearpygui.draw_polygon                                                                                  

    def __init__(
        self                                                                        ,
        points            : List[List[float]]                                       ,
        label             : str                               = None                ,
        user_data         : Any                               = None                ,
        use_internal_label: bool                              = True                ,
        parent            : Union[int, str]                   = 0                   ,
        before            : Union[int, str]                   = 0                   ,
        show              : bool                              = True                ,
        color             : Union[List[int], Tuple[int, ...]] = (255, 255, 255, 255),
        fill              : Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255)     ,
        thickness         : float                             = 1.0                 ,
        **kwargs                                                                    ,
    ) -> None:
        super().__init__(
            points=points,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawPolyline(Widget):
    """Adds a polyline.
    
    	Args:
    		points (List[List[float]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		closed (bool, optional): Will close the polyline by returning to the first point.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		thickness (float, optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    points            : List[List[float]]                 = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                               = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    closed            : bool                              = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    thickness         : float                             = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                              = False                                                                                                   
    _is_root_item     : bool                              = False                                                                                                   
    _is_value_able    : bool                              = False                                                                                                   
    _unique_parents   : tuple                             = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                             = ()                                                                                                      
    _unique_commands  : tuple                             = ()                                                                                                      
    _unique_constants : tuple                             = ('mvDrawPolyline',)                                                                                     
    _command          : Callable                          = dearpygui.draw_polyline                                                                                 

    def __init__(
        self                                                                        ,
        points            : List[List[float]]                                       ,
        label             : str                               = None                ,
        user_data         : Any                               = None                ,
        use_internal_label: bool                              = True                ,
        parent            : Union[int, str]                   = 0                   ,
        before            : Union[int, str]                   = 0                   ,
        show              : bool                              = True                ,
        closed            : bool                              = False               ,
        color             : Union[List[int], Tuple[int, ...]] = (255, 255, 255, 255),
        thickness         : float                             = 1.0                 ,
        **kwargs                                                                    ,
    ) -> None:
        super().__init__(
            points=points,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            closed=closed,
            color=color,
            thickness=thickness,
            **kwargs,
        )


class DrawImage(Widget):
    """Adds an image (for a drawing).
    
    	Args:
    		texture_tag (Union[int, str]): 
    		pmin (Union[List[float], Tuple[float, ...]]): Point of to start drawing texture.
    		pmax (Union[List[float], Tuple[float, ...]]): Point to complete drawing texture.
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		uv_min (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		uv_max (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    texture_tag       : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    pmin              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    pmax              : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv_min            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv_max            : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawImage',)                                                                                        
    _command          : Callable                              = dearpygui.draw_image                                                                                    

    def __init__(
        self                                                                            ,
        texture_tag       : Union[int, str]                                             ,
        pmin              : Union[List[float], Tuple[float, ...]]                       ,
        pmax              : Union[List[float], Tuple[float, ...]]                       ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        parent            : Union[int, str]                       = 0                   ,
        before            : Union[int, str]                       = 0                   ,
        show              : bool                                  = True                ,
        uv_min            : Union[List[float], Tuple[float, ...]] = (0.0, 0.0)          ,
        uv_max            : Union[List[float], Tuple[float, ...]] = (1.0, 1.0)          ,
        color             : Union[List[int], Tuple[int, ...]]     = (255, 255, 255, 255),
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            uv_min=uv_min,
            uv_max=uv_max,
            color=color,
            **kwargs,
        )


class DrawLayer(Widget):
    """New in 1.1. Creates a layer useful for grouping drawlist items.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		perspective_divide (bool, optional): New in 1.1. apply perspective divide
    		depth_clipping (bool, optional): New in 1.1. apply depth clipping
    		cull_mode (int, optional): New in 1.1. culling mode, mvCullMode_* constants. Only works with triangles currently.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    perspective_divide: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    depth_clipping    : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   
    cull_mode         : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                   

    _is_container     : bool     = True                                                                                                                                                                                                                         
    _is_root_item     : bool     = False                                                                                                                                                                                                                        
    _is_value_able    : bool     = False                                                                                                                                                                                                                        
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'Drawlist', 'Window', 'Plot', 'ViewportDrawlist')                                                                                                                                              
    _unique_children  : tuple    = ('DrawLine', 'DrawArrow', 'DrawTriangle', 'DrawCircle', 'DrawEllipse', 'DrawBezierCubic', 'DrawBezierQuadratic', 'DrawQuad', 'DrawRect', 'DrawText', 'DrawPolygon', 'DrawPolyline', 'DrawImage', 'DrawImageQuad', 'DrawNode')
    _unique_commands  : tuple    = ('set_clip_space',)                                                                                                                                                                                                          
    _unique_constants : tuple    = ('mvDrawLayer',)                                                                                                                                                                                                             
    _command          : Callable = dearpygui.add_draw_layer                                                                                                                                                                                                     

    def __init__(
        self                                       ,
        label             : str             = None ,
        user_data         : Any             = None ,
        use_internal_label: bool            = True ,
        parent            : Union[int, str] = 0    ,
        before            : Union[int, str] = 0    ,
        show              : bool            = True ,
        perspective_divide: bool            = False,
        depth_clipping    : bool            = False,
        cull_mode         : int             = 0    ,
        **kwargs                                   ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            perspective_divide=perspective_divide,
            depth_clipping=depth_clipping,
            cull_mode=cull_mode,
            **kwargs,
        )


class ViewportDrawlist(Widget):
    """A container that is used to present draw items or layers directly to the viewport. By default this will draw to the back of the viewport. Layers and draw items should be added to this widget as children.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		filter_key (str, optional): Used by filter widget.
    		delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    		front (bool, optional): Draws to the front of the view port instead of the back.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    user_data         : Any      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    filter_key        : str      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                
    delay_search      : bool     = ItemAttribute('information', 'get_item_cached', None, None)                                                                                                                                                                               
    front             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                                                                                                                                                                

    _is_container     : bool     = True                                                                                                                                                                                                                                      
    _is_root_item     : bool     = True                                                                                                                                                                                                                                      
    _is_value_able    : bool     = False                                                                                                                                                                                                                                     
    _unique_parents   : tuple    = ()                                                                                                                                                                                                                                        
    _unique_children  : tuple    = ('DrawLine', 'DrawLayer', 'DrawArrow', 'DrawTriangle', 'DrawCircle', 'DrawEllipse', 'DrawBezierCubic', 'DrawBezierQuadratic', 'DrawQuad', 'DrawRect', 'DrawText', 'DrawPolygon', 'DrawPolyline', 'DrawImage', 'DrawImageQuad', 'DrawNode')
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                                        
    _unique_constants : tuple    = ('mvViewportDrawlist',)                                                                                                                                                                                                                   
    _command          : Callable = dearpygui.add_viewport_drawlist                                                                                                                                                                                                           

    def __init__(
        self                            ,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = True ,
        filter_key        : str  = ''   ,
        delay_search      : bool = False,
        front             : bool = True ,
        **kwargs                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            front=front,
            **kwargs,
        )


class DrawImageQuad(Widget):
    """Adds an image (for a drawing).
    
    	Args:
    		texture_tag (Union[int, str]): 
    		p1 (Union[List[float], Tuple[float, ...]]): 
    		p2 (Union[List[float], Tuple[float, ...]]): 
    		p3 (Union[List[float], Tuple[float, ...]]): 
    		p4 (Union[List[float], Tuple[float, ...]]): 
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
    		show (bool, optional): Attempt to render widget.
    		uv1 (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		uv2 (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		uv3 (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		uv4 (Union[List[float], Tuple[float, ...]], optional): Normalized coordinates on texture that will be drawn.
    		color (Union[List[int], Tuple[int, ...]], optional): 
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    texture_tag       : Union[int, str]                       = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p1                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p2                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p3                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    p4                : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    label             : str                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    user_data         : Any                                   = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    use_internal_label: bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    show              : bool                                  = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv1               : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv2               : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv3               : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    uv4               : Union[List[float], Tuple[float, ...]] = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              
    color             : Union[List[int], Tuple[int, ...]]     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)                              

    _is_container     : bool                                  = False                                                                                                   
    _is_root_item     : bool                                  = False                                                                                                   
    _is_value_able    : bool                                  = False                                                                                                   
    _unique_parents   : tuple                                 = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'DrawNode', 'ViewportDrawlist')
    _unique_children  : tuple                                 = ()                                                                                                      
    _unique_commands  : tuple                                 = ()                                                                                                      
    _unique_constants : tuple                                 = ('mvDrawImageQuad',)                                                                                    
    _command          : Callable                              = dearpygui.draw_image_quad                                                                               

    def __init__(
        self                                                                            ,
        texture_tag       : Union[int, str]                                             ,
        p1                : Union[List[float], Tuple[float, ...]]                       ,
        p2                : Union[List[float], Tuple[float, ...]]                       ,
        p3                : Union[List[float], Tuple[float, ...]]                       ,
        p4                : Union[List[float], Tuple[float, ...]]                       ,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        parent            : Union[int, str]                       = 0                   ,
        before            : Union[int, str]                       = 0                   ,
        show              : bool                                  = True                ,
        uv1               : Union[List[float], Tuple[float, ...]] = (0.0, 0.0)          ,
        uv2               : Union[List[float], Tuple[float, ...]] = (1.0, 0.0)          ,
        uv3               : Union[List[float], Tuple[float, ...]] = (1.0, 1.0)          ,
        uv4               : Union[List[float], Tuple[float, ...]] = (0.0, 1.0)          ,
        color             : Union[List[int], Tuple[int, ...]]     = (255, 255, 255, 255),
        **kwargs                                                                        ,
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            uv1=uv1,
            uv2=uv2,
            uv3=uv3,
            uv4=uv4,
            color=color,
            **kwargs,
        )


class DrawNode(Widget):
    """New in 1.1. Creates a drawing node to associate a transformation matrix. Child node matricies will concatenate.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
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
    _is_root_item     : bool     = False                                                                                                                                                                                                                        
    _is_value_able    : bool     = False                                                                                                                                                                                                                        
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'Drawlist', 'DrawLayer', 'Window', 'Plot', 'ViewportDrawlist', 'DrawNode')                                                                                                                     
    _unique_children  : tuple    = ('DrawLine', 'DrawArrow', 'DrawTriangle', 'DrawCircle', 'DrawEllipse', 'DrawBezierCubic', 'DrawBezierQuadratic', 'DrawQuad', 'DrawRect', 'DrawText', 'DrawPolygon', 'DrawPolyline', 'DrawImage', 'DrawNode', 'DrawImageQuad')
    _unique_commands  : tuple    = ('apply_transform', 'create_rotation_matrix', 'create_translation_matrix', 'create_scale_matrix', 'create_lookat_matrix', 'create_perspective_matrix', 'create_orthographic_matrix', 'create_fps_matrix')                    
    _unique_constants : tuple    = ('mvDrawNode',)                                                                                                                                                                                                              
    _command          : Callable = dearpygui.add_draw_node                                                                                                                                                                                                      

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        before            : Union[int, str] = 0   ,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            **kwargs,
        )
