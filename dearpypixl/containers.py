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


class FilterSet(WidgetItem):
    """Helper to parse and apply text filters (e.g. aaaaa[, bbbbb][, ccccc])

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFilterSet, "mvFilterSet"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_filter_set,
    )

    width        : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent       : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool = __dearpypixl__.set_information(None, None)

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


class Clipper(WidgetItem):
    """Helper to manually clip large list of items. Increases performance by not searching or drawing widgets outside of the clipped region.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvClipper, "mvClipper"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_clipper,
    )

    width        : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent       : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool = __dearpypixl__.set_information(None, None)

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


class Stage(WidgetItem):
    """Adds a stage.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvStage, "mvStage"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_stage,
    )

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


class TreeNode(WidgetItem):
    """Adds a tree node to add items to.

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
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTreeNode, "mvTreeNode"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_tree_node,
    )

    indent               : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type         : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback        : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback        : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                  : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key           : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search         : bool                        = __dearpypixl__.set_information(None, None)
    tracked              : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset         : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_open         : bool                        = __dearpypixl__.set_information(None, None)
    open_on_double_click : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    open_on_arrow        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    leaf                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bullet               : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    selectable           : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_toggled_open      : bool           = __dearpypixl__.set_state("get_item_state", None, target="toggled_open")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        indent               : int                         = -1,
        parent               : Item | int                  = 0,
        before               : Item | int                  = 0,
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


class ChildWindow(WidgetItem):
    """Adds an embedded child window. Will show scrollbars when items do not fit.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvChildWindow, "mvChildWindow"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_child_window,
    )

    width                : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height               : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent               : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type         : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback        : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                  : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key           : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search         : bool                        = __dearpypixl__.set_information(None, None)
    tracked              : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset         : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    border               : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    autosize_x           : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    autosize_y           : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_scrollbar         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal_scrollbar : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    menubar              : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        width                : int                         = 0,
        height               : int                         = 0,
        indent               : int                         = -1,
        parent               : Item | int                  = 0,
        before               : Item | int                  = 0,
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
    @__dearpypixl__.as_information
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return dearpygui.get_y_scroll_max(self.tag)

    @property
    @__dearpypixl__.as_information
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        dearpygui.set_y_scroll(self.tag, value)

    @property
    @__dearpypixl__.as_information
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return dearpygui.get_x_scroll_max(self.tag)

    @property
    @__dearpypixl__.as_information
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return dearpygui.set_x_scroll(self.tag, value)


class Group(WidgetItem):
    """Creates a group that other widgets can belong to. The group allows item commands to be issued for all of its members.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
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
            * horizontal (bool, optional): Forces child widgets to be added in a horizontal layout.
            * horizontal_spacing (float, optional): Spacing for the horizontal layout.
            * xoffset (float, optional): Offset from containing window x item location within group.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvGroup, "mvGroup"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_group,
    )

    width              : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent             : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type       : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show               : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key         : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search       : bool                        = __dearpypixl__.set_information(None, None)
    tracked            : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset       : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal_spacing : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    xoffset            : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized                : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered                : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused                : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked                : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible                : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated              : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated            : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        indent             : int                         = -1,
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


class CollapsingHeader(WidgetItem):
    """Adds a collapsing header to add items to. Must be closed with the end command.

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
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvCollapsingHeader, "mvCollapsingHeader"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_collapsing_header,
    )

    indent              : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type        : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback       : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback       : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                 : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key          : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    tracked             : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset        : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    closable            : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    open_on_double_click: bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    open_on_arrow       : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    leaf                : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bullet              : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    open                : bool                              = __dearpypixl__.set_configuration("get_item_value",  "set_item_value" )

    default_open        : bool                              = __dearpypixl__.set_information(None, None             )
    delay_search        : bool                              = __dearpypixl__.set_information(None, None             )

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_toggled_open      : bool           = __dearpypixl__.set_state("get_item_state", None, target="toggled_open")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label                : str                         = None,
        user_data            : Any                         = None,
        use_internal_label   : bool                        = True,
        indent               : int                         = -1,
        parent               : Item | int                  = 0,
        before               : Item | int                  = 0,
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


class Tab(WidgetItem):
    """Adds a tab to a tab bar.

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
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * closable (bool, optional): Creates a button on the tab that can hide the tab.
            * no_tooltip (bool, optional): Disable tooltip for the given tab.
            * order_mode (bool, optional): set using a constant: mvTabOrder_Reorderable: allows reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to front, mvTabOrder_Trailing: adds tab to back
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTab, "mvTab"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvTabBar, dearpygui.mvStage,dearpygui.mvTemplateRegistry),
        able_children=(),
        constants=('mvTab', 'mvTabOrder_Reorderable', 'mvTabOrder_Fixed', 'mvTabOrder_Leading', 'mvTabOrder_Trailing'),
        command=dearpygui.add_tab,
    )

    indent        : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key    : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search  : bool     = __dearpypixl__.set_information(None, None)
    tracked       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    closable      : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tooltip    : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    order_mode    : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

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


class TabBar(WidgetItem):
    """Adds a tab bar.

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
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * reorderable (bool, optional): Allows for the user to change the order of the tabs.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTabBar, "mvTabBar"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(dearpygui.mvTab, dearpygui.mvTabButton, dearpygui.mvActivatedHandler, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvDeactivatedAfterEditHandler, dearpygui.mvDeactivatedHandler, dearpygui.mvEditedHandler, dearpygui.mvFocusHandler, dearpygui.mvHoverHandler, dearpygui.mvResizeHandler, dearpygui.mvToggledOpenHandler,dearpygui.mvVisibleHandler),
        command=dearpygui.add_tab_bar,
    )

    indent       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback     : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key   : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool                        = __dearpypixl__.set_information(None, None)
    tracked      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    reorderable  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_visible : bool = __dearpypixl__.set_state("get_item_state", None, target="visible")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
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


class Menu(WidgetItem):
    """Adds a menu to an existing menu bar.

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
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMenu, "mvMenu"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_menu,
    )

    indent        : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key    : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search  : bool     = __dearpypixl__.set_information(None, None)
    tracked       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized     : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_hovered     : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active      : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused     : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_activated   : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_size      : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")

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


class MenuBar(WidgetItem):
    """Adds a menu bar to a window.

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
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMenuBar, "mvMenuBar"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvWindowAppItem, dearpygui.mvChildWindow, dearpygui.mvNodeEditor, dearpygui.mvStage,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_menu_bar,
    )

    indent       : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool = __dearpypixl__.set_information(None, None)

    is_visible : bool = __dearpypixl__.set_state("get_item_state", None, target="visible")

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


class Tooltip(WidgetItem):
    """Adds a tooltip window.

        Args:
            * parent (int | str):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTooltip, "mvTooltip"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_tooltip,
    )

    show : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

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


class Window(WidgetItem):
    """Creates a new window for following items to be added to.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvWindowAppItem, "mvWindowAppItem"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        commands=('set_x_scroll', 'set_y_scroll', 'get_x_scroll', 'get_y_scroll', 'get_x_scroll_max', 'get_y_scroll_max'),
        command=dearpygui.add_window,
    )

    width                       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height                      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent                      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    delay_search                : bool                        = __dearpypixl__.set_information(None, None)
    min_size                    : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_size                    : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    menubar                     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    collapsed                   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    autosize                    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_resize                   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_title_bar                : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_move                     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_scrollbar                : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_collapse                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal_scrollbar        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_focus_on_appearing       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_bring_to_front_on_focus  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_open_over_existing_popup : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_close                    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_background               : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    modal                       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    popup                       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_saved_settings           : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_close                    : Callable                    = __dearpypixl__.set_configuration(None, "set_item_callback")

    is_resized      : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_hovered      : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_focused      : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_visible      : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_size       : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    is_toggled_open : bool           = __dearpypixl__.set_state("get_item_state", None, target="toggled_open")

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
    @__dearpypixl__.as_information
    def y_scroll_max(self) -> float:
        """Maximum vertical scroll position.
        """
        return dearpygui.get_y_scroll_max(self.tag)

    @property
    @__dearpypixl__.as_information
    def y_scroll_pos(self) -> float:
        """Vertical scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_y_scroll(self.tag)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value):  # -1.0 will set it to max/end
        dearpygui.set_y_scroll(self.tag, value)

    @property
    @__dearpypixl__.as_information
    def x_scroll_max(self) -> float:
        """Maximum horizontal scroll position.
        """
        return dearpygui.get_x_scroll_max(self.tag)

    @property
    @__dearpypixl__.as_information
    def x_scroll_pos(self) -> float:
        """Horizontal scroll position of the container. If set to -1.0,
        its position will be set to the end.
        """
        return dearpygui.get_x_scroll(self.tag)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):  # -1.0 will set it to max/end
        return dearpygui.set_x_scroll(self.tag, value)


class DragPayload(WidgetItem):
    """User data payload for drag and drop operations.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * drag_data (Any, optional): Drag data
            * drop_data (Any, optional): Drop data
            * payload_type (str, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDragPayload, "mvDragPayload"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvButton, dearpygui.mvCheckbox, dearpygui.mvCombo, dearpygui.mvDragIntMulti, dearpygui.mvDragFloatMulti, dearpygui.mvDragInt, dearpygui.mvDragFloat, dearpygui.mvImage, dearpygui.mvImageButton, dearpygui.mvInputIntMulti, dearpygui.mvInputFloatMulti, dearpygui.mvInputInt, dearpygui.mvInputFloat, dearpygui.mvInputText, dearpygui.mvListbox, dearpygui.mvMenuItem, dearpygui.mvRadioButton, dearpygui.mvSelectable, dearpygui.mvSliderIntMulti, dearpygui.mvSliderFloatMulti, dearpygui.mvSliderInt, dearpygui.mvSliderFloat, dearpygui.mvTabButton, dearpygui.mvText, dearpygui.mvColorButton, dearpygui.mvColorEdit, dearpygui.mvColorMapButton, dearpygui.mvColorPicker, dearpygui.mvCollapsingHeader, dearpygui.mvGroup, dearpygui.mvTreeNode, dearpygui.mvDatePicker, dearpygui.mvKnobFloat, dearpygui.mvLoadingIndicator, dearpygui.mvSlider3D, dearpygui.mvTimePicker, dearpygui.mvProgressBar, dearpygui.mvNode,dearpygui.mvPlot),
        able_children=(),
        command=dearpygui.add_drag_payload,
    )

    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_data    : Any  = __dearpypixl__.set_configuration(None, "set_item_config")
    drop_data    : Any  = __dearpypixl__.set_configuration(None, "set_item_config")
    payload_type : str  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ViewportMenuBar(WidgetItem):
    """Adds a menubar to the viewport.

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
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvViewportMenuBar, "mvViewportMenuBar"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_viewport_menu_bar,
    )

    indent       : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool = __dearpypixl__.set_information(None, None)

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
