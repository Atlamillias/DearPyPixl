from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

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


class FilterSet(Widget):
    """Helper to parse and apply text filters (e.g. aaaaa[, bbbbb][, ccccc])

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): Attempt to render widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    width        : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent       : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show         : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search : bool = ItemProperty(INFORM, None, None)

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFilterSet, "mvFilterSet")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_filter_set

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        width              : int       = 0,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        delay_search       : bool      = False,
        **kwargs
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


class Clipper(Widget):
    """Helper to manually clip large list of items. Increases performance by not searching or drawing widgets outside of the clipped region.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): Attempt to render widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    width        : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent       : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show         : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search : bool = ItemProperty(INFORM, None, None)

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvClipper, "mvClipper")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_clipper

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        width              : int       = 0,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        delay_search       : bool      = False,
        **kwargs
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


class Stage(Widget):
    """Adds a stage.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    """
    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvStage, "mvStage")
    __is_container__ : bool       = True
    __is_root_item__ : bool       = True
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = ()
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_stage

    def __init__(
        self,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class TreeNode(Widget):
    """Adds a tree node to add items to.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_open (bool, optional): Sets the tree node open by default.
            * open_on_double_click (bool, optional): Need double-click to open node.
            * open_on_arrow (bool, optional): Only open when clicking on the arrow part.
            * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf nodes).
            * bullet (bool, optional): Display a bullet instead of arrow.
            * selectable (bool, optional): Makes the tree selectable.
    """
    indent               : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type         : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback        : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback        : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show                 : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                  : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key           : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search         : bool                        = ItemProperty(INFORM, None, None)
    tracked              : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset         : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_open         : bool                        = ItemProperty(INFORM, None, None)
    open_on_double_click : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    open_on_arrow        : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    leaf                 : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    bullet               : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    selectable           : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused           : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_activated         : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_toggled_open      : bool           = ItemProperty(STATES, "get_item_state", None, target="toggled_open")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTreeNode, "mvTreeNode")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_tree_node

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        indent               : int                         = -1,
        parent               : int | str                   = 0,
        before               : int | str                   = 0,
        payload_type         : str                         = '$$DPG_PAYLOAD',
        drag_callback        : Callable                    = None,
        drop_callback        : Callable                    = None,
        show                 : bool                        = True,
        pos                  : list[int] | tuple[int, ...] = [],
        filter_key           : str                         = '',
        delay_search         : bool                        = False,
        tracked              : bool                        = False,
        track_offset         : float                       = 0.5,
        default_open         : bool                        = False,
        open_on_double_click : bool                        = False,
        open_on_arrow        : bool                        = False,
        leaf                 : bool                        = False,
        bullet               : bool                        = False,
        selectable           : bool                        = False,
        **kwargs
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


class ChildWindow(Widget):
    """Adds an embedded child window. Will show scrollbars when items do not fit.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * border (bool, optional): Shows/Hides the border around the sides.
            * autosize_x (bool, optional): Autosize the window to fit it's items in the x.
            * autosize_y (bool, optional): Autosize the window to fit it's items in the y.
            * no_scrollbar (bool, optional):  Disable scrollbars (window can still scroll with mouse or programmatically).
            * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear (off by default).
            * menubar (bool, optional): Shows/Hides the menubar at the top.
    """
    width                : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height               : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent               : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type         : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback        : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show                 : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                  : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key           : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search         : bool                        = ItemProperty(INFORM, None, None)
    tracked              : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset         : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    border               : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    autosize_x           : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    autosize_y           : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_scrollbar         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    horizontal_scrollbar : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    menubar              : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused           : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvChildWindow, "mvChildWindow")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_child_window

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        width                : int                         = 0,
        height               : int                         = 0,
        indent               : int                         = -1,
        parent               : int | str                   = 0,
        before               : int | str                   = 0,
        payload_type         : str                         = '$$DPG_PAYLOAD',
        drop_callback        : Callable                    = None,
        show                 : bool                        = True,
        pos                  : list[int] | tuple[int, ...] = [],
        filter_key           : str                         = '',
        delay_search         : bool                        = False,
        tracked              : bool                        = False,
        track_offset         : float                       = 0.5,
        border               : bool                        = True,
        autosize_x           : bool                        = False,
        autosize_y           : bool                        = False,
        no_scrollbar         : bool                        = False,
        horizontal_scrollbar : bool                        = False,
        menubar              : bool                        = False,
        **kwargs
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

    @property
    @ItemProperty.register(category=INFORM)
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return dearpygui.get_y_scroll_max(self.tag)

    @property
    @ItemProperty.register(category=INFORM)
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        dearpygui.set_y_scroll(self.tag, value)

    @property
    @ItemProperty.register(category=INFORM)
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return dearpygui.get_x_scroll_max(self.tag)

    @property
    @ItemProperty.register(category=INFORM)
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return dearpygui.set_x_scroll(self.tag, value)


class Group(Widget):
    """Creates a group that other widgets can belong to. The group allows item commands to be issued for all of its members.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * horizontal (bool, optional): Forces child widgets to be added in a horizontal layout.
            * horizontal_spacing (float, optional): Spacing for the horizontal layout.
            * xoffset (float, optional): Offset from containing window x item location within group.
    """
    width              : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent             : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type       : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show               : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key         : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search       : bool                        = ItemProperty(INFORM, None, None)
    tracked            : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset       : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    horizontal         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    horizontal_spacing : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    xoffset            : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked         : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered                : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                 : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused                : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked                : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible                : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited                 : bool           = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated              : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated            : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvGroup, "mvGroup")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_group

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        delay_search       : bool                        = False,
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        horizontal         : bool                        = False,
        horizontal_spacing: float                        = -1,
        xoffset            : float                       = 0.0,
        **kwargs
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


class CollapsingHeader(Widget):
    """Adds a collapsing header to add items to. Must be closed with the end command.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * closable (bool, optional): Adds the ability to hide this widget by pressing the (x) in the top right of widget.
            * default_open (bool, optional): Sets the collapseable header open by default.
            * open_on_double_click (bool, optional): Need double-click to open node.
            * open_on_arrow (bool, optional): Only open when clicking on the arrow part.
            * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf nodes).
            * bullet (bool, optional): Display a bullet instead of arrow.
    """
    indent              : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type        : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback       : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback       : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show                : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                 : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state" , "set_item_config")
    filter_key          : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    tracked             : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset        : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    closable            : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    open_on_double_click: bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    open_on_arrow       : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    leaf                : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    bullet              : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    open                : bool                              = ItemProperty(CONFIG, "get_item_value",  "set_item_value" )

    default_open        : bool                              = ItemProperty(INFORM, None, None             )
    delay_search        : bool                              = ItemProperty(INFORM, None, None             )

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused           : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_activated         : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_toggled_open      : bool           = ItemProperty(STATES, "get_item_state", None, target="toggled_open")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvCollapsingHeader, "mvCollapsingHeader")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_collapsing_header

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        indent               : int                         = -1,
        parent               : int | str                   = 0,
        before               : int | str                   = 0,
        payload_type         : str                         = '$$DPG_PAYLOAD',
        drag_callback        : Callable                    = None,
        drop_callback        : Callable                    = None,
        show                 : bool                        = True,
        pos                  : list[int] | tuple[int, ...] = [],
        filter_key           : str                         = '',
        delay_search         : bool                        = False,
        tracked              : bool                        = False,
        track_offset         : float                       = 0.5,
        closable             : bool                        = False,
        default_open         : bool                        = False,
        open_on_double_click : bool                        = False,
        open_on_arrow        : bool                        = False,
        leaf                 : bool                        = False,
        bullet               : bool                        = False,
        **kwargs
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


class Tab(Widget):
    """Adds a tab to a tab bar.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * closable (bool, optional): Creates a button on the tab that can hide the tab.
            * no_tooltip (bool, optional): Disable tooltip for the given tab.
            * order_mode (bool, optional): set using a constant: mvTabOrder_Reorderable: allows reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to front, mvTabOrder_Trailing: adds tab to back
    """
    indent        : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key    : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search  : bool     = ItemProperty(INFORM, None, None)
    tracked       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    closable      : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_tooltip    : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    order_mode    : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_activated         : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTab, "mvTab")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvTabBar, dearpygui.mvStage, dearpygui.mvTemplateRegistry)
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvTab', 'mvTabOrder_Reorderable', 'mvTabOrder_Fixed', 'mvTabOrder_Leading', 'mvTabOrder_Trailing')
    __command__       : Callable   = dearpygui.add_tab

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        payload_type       : str       = '$$DPG_PAYLOAD',
        drop_callback      : Callable  = None,
        show               : bool      = True,
        filter_key         : str       = '',
        delay_search       : bool      = False,
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        closable           : bool      = False,
        no_tooltip         : bool      = False,
        order_mode         : bool      = 0,
        **kwargs
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


class TabBar(Widget):
    """Adds a tab bar.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * reorderable (bool, optional): Allows for the user to change the order of the tabs.
    """
    indent       : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback     : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key   : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search : bool                        = ItemProperty(INFORM, None, None)
    tracked      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    reorderable  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_visible : bool = ItemProperty(STATES, "get_item_state", None, target="visible")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTabBar, "mvTabBar")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = (dearpygui.mvTab, dearpygui.mvTabButton, dearpygui.mvActivatedHandler, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvDeactivatedAfterEditHandler, dearpygui.mvDeactivatedHandler, dearpygui.mvEditedHandler, dearpygui.mvFocusHandler, dearpygui.mvHoverHandler, dearpygui.mvResizeHandler, dearpygui.mvToggledOpenHandler, dearpygui.mvVisibleHandler)
    __command__       : Callable   = dearpygui.add_tab_bar

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        callback           : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        delay_search       : bool                        = False,
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        reorderable        : bool                        = False,
        **kwargs
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


class Menu(Widget):
    """Adds a menu to an existing menu bar.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    """
    indent        : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key    : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search  : bool     = ItemProperty(INFORM, None, None)
    tracked       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float    = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized     : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_hovered     : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active      : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused     : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_activated   : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    rect_size      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvMenu, "mvMenu")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_menu

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        payload_type       : str       = '$$DPG_PAYLOAD',
        drop_callback      : Callable  = None,
        show               : bool      = True,
        enabled            : bool      = True,
        filter_key         : str       = '',
        delay_search       : bool      = False,
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        **kwargs
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


class MenuBar(Widget):
    """Adds a menu bar to a window.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * show (bool, optional): Attempt to render widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    indent       : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show         : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search : bool = ItemProperty(INFORM, None, None)

    is_visible : bool = ItemProperty(STATES, "get_item_state", None, target="visible")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvMenuBar, "mvMenuBar")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvWindowAppItem, dearpygui.mvChildWindow, dearpygui.mvNodeEditor, dearpygui.mvStage, dearpygui.mvTemplateRegistry)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_menu_bar

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        show               : bool      = True,
        delay_search       : bool      = False,
        **kwargs
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


class Tooltip(Widget):
    """Adds a tooltip window.

        Args:
            * parent (int | str):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * show (bool, optional): Attempt to render widget.
    """
    show : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTooltip, "mvTooltip")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_tooltip

    def __init__(
        self,
        parent            : int | str,
        label             : str            = None,
        user_data         : Any            = None,
        use_internal_label: bool           = True,
        show              : bool           = True,
        **kwargs
    ) -> None:
        super().__init__(
            parent=parent,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class Window(Widget):
    """Creates a new window for following items to be added to.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * min_size (list[int] | tuple[int, ...], optional): Minimum window size.
            * max_size (list[int] | tuple[int, ...], optional): Maximum window size.
            * menubar (bool, optional): Shows or hides the menubar.
            * collapsed (bool, optional): Collapse the window.
            * autosize (bool, optional): Autosized the window to fit it's items.
            * no_resize (bool, optional): Allows for the window size to be changed or fixed.
            * no_title_bar (bool, optional): Title name for the title bar of the window.
            * no_move (bool, optional): Allows for the window's position to be changed or fixed.
            * no_scrollbar (bool, optional):  Disable scrollbars. (window can still scroll with mouse or programmatically)
            * no_collapse (bool, optional): Disable user collapsing window by double-clicking on it.
            * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear. (off by default)
            * no_focus_on_appearing (bool, optional): Disable taking focus when transitioning from hidden to visible state.
            * no_bring_to_front_on_focus (bool, optional): Disable bringing window to front when taking focus. (e.g. clicking on it or programmatically giving it focus)
            * no_close (bool, optional): Disable user closing the window by removing the close button.
            * no_background (bool, optional): Sets Background and border alpha to transparent.
            * modal (bool, optional): Fills area behind window according to the theme and disables user ability to interact with anything except the window.
            * popup (bool, optional): Fills area behind window according to the theme, removes title bar, collapse and close. Window can be closed by selecting area in the background behind the window.
            * no_saved_settings (bool, optional): Never load/save settings in .ini file.
            * on_close (Callable, optional): Callback ran when window is closed.
    """
    width                       : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height                      : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent                      : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show                        : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                         : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    delay_search                : bool                        = ItemProperty(INFORM, None, None)
    min_size                    : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_size                    : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    menubar                     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    collapsed                   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    autosize                    : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_resize                   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_title_bar                : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_move                     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_scrollbar                : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_collapse                 : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    horizontal_scrollbar        : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_focus_on_appearing       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_bring_to_front_on_focus  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_open_over_existing_popup : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_close                    : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_background               : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    modal                       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    popup                       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_saved_settings           : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_close                    : Callable                    = ItemProperty(CONFIG, None, "set_item_callback")

    is_resized      : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_hovered      : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_focused      : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_visible      : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_size       : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    is_toggled_open : bool           = ItemProperty(STATES, "get_item_state", None, target="toggled_open")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvWindowAppItem, "mvWindowAppItem")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = True
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __commands__      : tuple      = ('set_x_scroll', 'set_y_scroll', 'get_x_scroll', 'get_y_scroll', 'get_x_scroll_max', 'get_y_scroll_max')
    __command__       : Callable   = dearpygui.add_window

    def __init__(
        self,
        label                      : str                         = None,
        user_data                  : Any                         = None,
        use_internal_label         : bool                        = True,
        width                      : int                         = 0,
        height                     : int                         = 0,
        indent                     : int                         = -1,
        show                       : bool                        = True,
        pos                        : list[int] | tuple[int, ...] = [],
        delay_search               : bool                        = False,
        min_size                   : list[int] | tuple[int, ...] = [100, 100],
        max_size                   : list[int] | tuple[int, ...] = [30000, 30000],
        menubar                    : bool                        = False,
        collapsed                  : bool                        = False,
        autosize                   : bool                        = False,
        no_resize                  : bool                        = False,
        no_title_bar               : bool                        = False,
        no_move                    : bool                        = False,
        no_scrollbar               : bool                        = False,
        no_collapse                : bool                        = False,
        horizontal_scrollbar       : bool                        = False,
        no_focus_on_appearing      : bool                        = False,
        no_bring_to_front_on_focus : bool                        = False,
        no_close                   : bool                        = False,
        no_background              : bool                        = False,
        modal                      : bool                        = False,
        popup                      : bool                        = False,
        no_saved_settings          : bool                        = False,
        on_close                   : Callable                    = None,
        **kwargs
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

    @property
    @ItemProperty.register(category=INFORM)
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return dearpygui.get_y_scroll_max(self.tag)

    @property
    @ItemProperty.register(category=INFORM)
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        dearpygui.set_y_scroll(self.tag, value)

    @property
    @ItemProperty.register(category=INFORM)
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return dearpygui.get_x_scroll_max(self.tag)

    @property
    @ItemProperty.register(category=INFORM)
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return dearpygui.set_x_scroll(self.tag, value)


class DragPayload(Widget):
    """User data payload for drag and drop operations.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * show (bool, optional): Attempt to render widget.
            * drag_data (Any, optional): Drag data
            * drop_data (Any, optional): Drop data
            * payload_type (str, optional):
    """
    show         : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_data    : Any  = ItemProperty(CONFIG, None, "set_item_config")
    drop_data    : Any  = ItemProperty(CONFIG, None, "set_item_config")
    payload_type : str  = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDragPayload, "mvDragPayload")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvButton, dearpygui.mvCheckbox, dearpygui.mvCombo, dearpygui.mvDragIntMulti, dearpygui.mvDragFloatMulti, dearpygui.mvDragInt, dearpygui.mvDragFloat, dearpygui.mvImage, dearpygui.mvImageButton, dearpygui.mvInputIntMulti, dearpygui.mvInputFloatMulti, dearpygui.mvInputInt, dearpygui.mvInputFloat, dearpygui.mvInputText, dearpygui.mvListbox, dearpygui.mvMenuItem, dearpygui.mvRadioButton, dearpygui.mvSelectable, dearpygui.mvSliderIntMulti, dearpygui.mvSliderFloatMulti, dearpygui.mvSliderInt, dearpygui.mvSliderFloat, dearpygui.mvTabButton, dearpygui.mvText, dearpygui.mvColorButton, dearpygui.mvColorEdit, dearpygui.mvColorMapButton, dearpygui.mvColorPicker, dearpygui.mvCollapsingHeader, dearpygui.mvGroup, dearpygui.mvTreeNode, dearpygui.mvDatePicker, dearpygui.mvKnobFloat, dearpygui.mvLoadingIndicator, dearpygui.mvSlider3D, dearpygui.mvTimePicker, dearpygui.mvProgressBar, dearpygui.mvNode, dearpygui.mvPlot)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_drag_payload

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        parent             : int | str = 0,
        show               : bool      = True,
        drag_data          : Any       = None,
        drop_data          : Any       = None,
        payload_type       : str       = '$$DPG_PAYLOAD',
        **kwargs
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


class ViewportMenuBar(Widget):
    """Adds a menubar to the viewport.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * show (bool, optional): Attempt to render widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    indent       : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show         : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search : bool = ItemProperty(INFORM, None, None)

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvViewportMenuBar, "mvViewportMenuBar")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = True
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_viewport_menu_bar

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        show               : bool      = True,
        delay_search       : bool      = False,
        **kwargs
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
