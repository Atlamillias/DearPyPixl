from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "NodeEditor",
    "Node",
    "NodeAttribute",
    "NodeLink",
]


class NodeEditor(WidgetItem):
    """Adds a node editor.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * delink_callback (Callable, optional): Callback ran when a link is detached.
            * menubar (bool, optional): Shows or hides the menubar.
            * minimap (bool, optional): Shows or hides the minimap.
            * minimap_location (int, optional): mvNodeMiniMap_Location_* constants.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvNodeEditor, "mvNodeEditor"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvMenuBar, dearpygui.mvNode, dearpygui.mvNodeLink, dearpygui.mvActivatedHandler, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvDeactivatedAfterEditHandler, dearpygui.mvDeactivatedHandler, dearpygui.mvEditedHandler, dearpygui.mvFocusHandler, dearpygui.mvHoverHandler, dearpygui.mvResizeHandler, dearpygui.mvToggledOpenHandler,dearpygui.mvVisibleHandler),
        commands=('get_selected_nodes', 'get_selected_links', 'clear_selected_nodes', 'clear_selected_links'),
        command=dearpygui.add_node_editor,
    )

    width            : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height           : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback         : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show             : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key       : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search     : bool     = __dearpypixl__.set_information(None, None)
    tracked          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset     : float    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delink_callback  : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    menubar          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    minimap          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")  # Needs testing
    minimap_location : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")  # Needs testing

    is_resized : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_hovered : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_visible : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_size  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        width              : int       = 0,
        height             : int       = 0,
        parent             : int | str = 0,
        before             : int | str = 0,
        callback           : Callable  = None,
        show               : bool      = True,
        filter_key         : str       = '',
        delay_search       : bool      = False,
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        delink_callback    : Callable  = '',
        menubar            : bool      = False,
        **kwargs
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


class Node(WidgetItem):
    """Adds a node to a node editor.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * draggable (bool, optional): Allow node to be draggable.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvNode, "mvNode"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage,dearpygui.mvNodeEditor),
        able_children=(dearpygui.mvNodeAttribute, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvHoverHandler, dearpygui.mvVisibleHandler,dearpygui.mvDragPayload),
        command=dearpygui.add_node,
    )

    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search  : bool                        = __dearpypixl__.set_information(None, None)
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    draggable     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized        : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked  : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked   : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered        : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_clicked        : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible        : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_size         : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        delay_search       : bool                        = False,
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        draggable          : bool                        = True,
        **kwargs
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


class NodeAttribute(WidgetItem):
    """Adds a node attribute to a node.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * indent (int, optional): Outer horizontal padding (in pixels) to add to the left side of
            the item, multiplied by the value of the indent/horizontal padding theme element affecting
            the item (1.0 by default). If -1, no additional padding is added. Defaults to -1.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * attribute_type (int, optional): mvNode_Attr_Input, mvNode_Attr_Output, or mvNode_Attr_Static.
            * shape (int, optional): Pin shape.
            * category (str, optional): Category
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvNodeAttribute, "mvNodeAttribute"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage,dearpygui.mvNode),
        able_children=(),
        constants=('mvNodeAttribute', 'mvNode_PinShape_Circle', 'mvNode_PinShape_CircleFilled', 'mvNode_PinShape_Triangle', 'mvNode_PinShape_TriangleFilled', 'mvNode_PinShape_Quad', 'mvNode_PinShape_QuadFilled', 'mvNode_Attr_Input', 'mvNode_Attr_Output', 'mvNode_Attr_Static'),
        command=dearpygui.add_node_attribute,
    )

    indent         : int   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show           : bool  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key     : str   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked        : bool  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset   : float = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    attribute_type : int   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    shape          : int   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    category       : str   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_hovered        : bool     = __dearpypixl__.set_state("get_item_state", None, target="hovered")

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        filter_key         : str       = '',
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        attribute_type     : int       = 0,
        shape              : int       = 1,
        category           : str       = 'general',
        **kwargs
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


class NodeLink(WidgetItem):
    """Adds a node link between 2 node attributes.

        Args:
            * attr_1 (int | str):
            * attr_2 (int | str):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvNodeLink, "mvNodeLink"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage,dearpygui.mvNodeEditor),
        able_children=(),
        command=dearpygui.add_node_link,
    )

    attr_1 : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    attr_2 : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_hovered : bool = __dearpypixl__.set_state("get_item_state", None, target="hovered")

    def __init__(
        self,
        attr_1            : int | str,
        attr_2            : int | str,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Item | int      = 0,
        show              : bool            = True,
        **kwargs
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
