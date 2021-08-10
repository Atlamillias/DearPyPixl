from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.widget import Container, Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Node",
    "NodeAttribute",
    "NodeEditor",
    "NodeLink",
]


class Node(Container):
    """Adds a node to a node editor.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **draggable (bool): Allow node to be draggable.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_node

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        draggable: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            draggable=draggable,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.draggable = draggable


class NodeAttribute(Container):
    """Adds a node attribute.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **attribute_type (int): mvNode_Attr_Input, mvNode_Attr_Output, or mvNode_Attr_Static.
            **shape (int): Pin shape.
            **category (str): Category
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_node_attribute

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        attribute_type: int = 0, 
        shape: int = 1, 
        category: str = 'general', 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            use_internal_label=use_internal_label,
            attribute_type=attribute_type,
            shape=shape,
            category=category,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.attribute_type = attribute_type
        self.shape = shape
        self.category = category


class NodeEditor(Container):
    """Adds a node editor.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **delink_callback (Callable): Callback ran when a link is detached.
            **menubar (bool): Shows or hides the menubar.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_node_editor

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        delink_callback: Callable = None, 
        menubar: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            use_internal_label=use_internal_label,
            delink_callback=delink_callback,
            menubar=menubar,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.delink_callback = delink_callback
        self.menubar = menubar


class NodeLink(Widget):
    """Adds a node link between nodes.
    Args:
            attr_1 (int): 
            attr_2 (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_node_link

    def __init__(
        self, 
        attr_1: int, 
        attr_2: int, 
        label: str = None, 
        parent: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            attr_1=attr_1,
            attr_2=attr_2,
            label=label,
            parent=parent,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.label = label
        self.parent = parent
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
