from typing import Callable, Any

from . import dpg
from ._widget import Container, Widget


##################################################
## Note: this file was automatically generated. ##
##################################################


class Node(Container):
    _command: Callable = dpg.add_node

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
        delay_search: str = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        user_data: Any = None,
        draggable: bool = True,
        **kwargs
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
        draggable=draggable,
        **kwargs
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
        self.draggable = draggable


class NodeAttribute(Container):
    _command: Callable = dpg.add_node_attribute

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
        attribute_type: int = 0,
        shape: int = 1,
        category: str = 'general',
        **kwargs
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
        attribute_type=attribute_type,
        shape=shape,
        category=category,
        **kwargs
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
        self.attribute_type = attribute_type
        self.shape = shape
        self.category = category


class NodeEditor(Container):
    _command: Callable = dpg.add_node_editor

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
        delay_search: str = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        user_data: Any = None,
        delink_callback: Callable = None,
        menubar: bool = False,
        **kwargs
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
        delink_callback=delink_callback,
        menubar=menubar,
        **kwargs
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
        self.delink_callback = delink_callback
        self.menubar = menubar


class NodeLink(Widget):
    _command: Callable = dpg.add_node_link

    def __init__(
        self,
        node_1: int,
        node_2: int,
        label: str = None,
        parent: int = 0,
        show: bool = True,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        node_1=node_1,
        node_2=node_2,
        label=label,
        parent=parent,
        show=show,
        user_data=user_data,
        **kwargs
        )
        self.node_1 = node_1
        self.node_2 = node_2
        self.label = label
        self.parent = parent
        self.show = show
        self.user_data = user_data
