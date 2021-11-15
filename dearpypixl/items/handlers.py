from typing import (
    Any,
    Callable,
    Union,
)
from dearpygui import dearpygui
from dearpypixl.items.configuration import ItemAttribute
from dearpypixl.items.item import Item

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "KeyDownHandler",
    "KeyPressHandler",
    "KeyReleaseHandler",
    "MouseMoveHandler",
    "MouseWheelHandler",
    "MouseClickHandler",
    "MouseDoubleClickHandler",
    "MouseDownHandler",
    "MouseReleaseHandler",
    "MouseDragHandler",
    "HoverHandler",
    "ResizeHandler",
    "FocusHandler",
    "ActiveHandler",
    "VisibleHandler",
    "ActivatedHandler",
    "DeactivatedHandler",
    "EditedHandler",
    "DeactivatedAfterEditHandler",
    "ToggledOpenHandler",
    "ClickedHandler",
]



class KeyDownHandler(Item):
    """Adds a key down handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    key               : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "key")               
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvKeyDownHandler',)                                                                           
    _command          : Callable = dearpygui.add_key_down_handler                                                                  

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class KeyPressHandler(Item):
    """Adds a key press handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    key               : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "key")               
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvKeyPressHandler',)                                                                          
    _command          : Callable = dearpygui.add_key_press_handler                                                                 

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class KeyReleaseHandler(Item):
    """Adds a key release handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    key               : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "key")               
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvKeyReleaseHandler',)                                                                        
    _command          : Callable = dearpygui.add_key_release_handler                                                               

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseMoveHandler(Item):
    """Adds a mouse move handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseMoveHandler',)                                                                         
    _command          : Callable = dearpygui.add_mouse_move_handler                                                                

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseWheelHandler(Item):
    """Adds a mouse wheel handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseWheelHandler',)                                                                        
    _command          : Callable = dearpygui.add_mouse_wheel_handler                                                               

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseClickHandler(Item):
    """Adds a mouse click handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseClickHandler',)                                                                        
    _command          : Callable = dearpygui.add_mouse_click_handler                                                               

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDoubleClickHandler(Item):
    """Adds a mouse double click handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseDoubleClickHandler',)                                                                  
    _command          : Callable = dearpygui.add_mouse_double_click_handler                                                        

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDownHandler(Item):
    """Adds a mouse down handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseDownHandler',)                                                                         
    _command          : Callable = dearpygui.add_mouse_down_handler                                                                

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseReleaseHandler(Item):
    """Adds a mouse release handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseReleaseHandler',)                                                                      
    _command          : Callable = dearpygui.add_mouse_release_handler                                                             

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDragHandler(Item):
    """Adds a mouse drag handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		threshold (float, optional): The threshold the mouse must be dragged before the callback is ran
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    threshold         : float    = ItemAttribute("configuration", "get_item_configuration", "configure_item", "threshold")         
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                                                
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvMouseDragHandler',)                                                                         
    _command          : Callable = dearpygui.add_mouse_drag_handler                                                                

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        threshold         : float           = 10.0,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            threshold=threshold,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class HoverHandler(Item):
    """Adds a hover handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvHoverHandler',)                                                                             
    _command          : Callable = dearpygui.add_item_hover_handler                                                                

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ResizeHandler(Item):
    """Adds a resize handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvResizeHandler',)                                                                            
    _command          : Callable = dearpygui.add_item_resize_handler                                                               

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class FocusHandler(Item):
    """Adds a focus handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvFocusHandler',)                                                                             
    _command          : Callable = dearpygui.add_item_focus_handler                                                                

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActiveHandler(Item):
    """Adds a active handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvActiveHandler',)                                                                            
    _command          : Callable = dearpygui.add_item_active_handler                                                               

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class VisibleHandler(Item):
    """Adds a visible handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvVisibleHandler',)                                                                           
    _command          : Callable = dearpygui.add_item_visible_handler                                                              

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActivatedHandler(Item):
    """Adds a activated handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvActivatedHandler',)                                                                         
    _command          : Callable = dearpygui.add_item_activated_handler                                                            

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedHandler(Item):
    """Adds a deactivated handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvDeactivatedHandler',)                                                                       
    _command          : Callable = dearpygui.add_item_deactivated_handler                                                          

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class EditedHandler(Item):
    """Adds an edited handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvEditedHandler',)                                                                            
    _command          : Callable = dearpygui.add_item_edited_handler                                                               

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedAfterEditHandler(Item):
    """Adds a deactivated after edit handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvDeactivatedAfterEditHandler',)                                                              
    _command          : Callable = dearpygui.add_item_deactivated_after_edit_handler                                               

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ToggledOpenHandler(Item):
    """Adds a togged open handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvToggledOpenHandler',)                                                                       
    _command          : Callable = dearpygui.add_item_toggled_open_handler                                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ClickedHandler(Item):
    """Adds a clicked handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button            : int      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "button")            
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    callback          : Callable = ItemAttribute("configuration", "get_item_configuration", "configure_item", "callback")          
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = False                                                                                           
    _is_root_item     : bool     = False                                                                                           
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                                            
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvClickedHandler',)                                                                           
    _command          : Callable = dearpygui.add_item_clicked_handler                                                              

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )