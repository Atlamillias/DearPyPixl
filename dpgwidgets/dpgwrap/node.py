from typing import Callable, Any

from . import idpg
from ._widget import Container, Widget


##################################################
## Note: this file was automatically generated. ##
##################################################


class Node(Container):
    _command: Callable = idpg.add_node

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
        self.draggable = draggable


class NodeAttribute(Container):
    _command: Callable = idpg.add_node_attribute

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
        attribute_type: int = 0,
        shape: int = 1,
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
        attribute_type=attribute_type,
        shape=shape,
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
        self.attribute_type = attribute_type
        self.shape = shape


class NodeEditor(Container):
    _command: Callable = idpg.add_node_editor

    def __init__(
        self,
        label: str = None,
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
        delink_callback: Callable = None,
        **kwargs
    ):
        super().__init__(
        label=label,
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
        delink_callback=delink_callback,
        **kwargs
        )
        self.label = label
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
        self.delink_callback = delink_callback


class NodeLink(Widget):
    _command: Callable = idpg.add_node_link

    def __init__(
        self,
        node_1: int,
        node_2: int,
        label: str = None,
        parent: int = 0,
        show: bool = True,
        **kwargs
    ):
        super().__init__(
        node_1=node_1,
        node_2=node_2,
        label=label,
        parent=parent,
        show=show,
        **kwargs
        )
        self.node_1 = node_1
        self.node_2 = node_2
        self.label = label
        self.parent = parent
        self.show = show
