from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from dearpypixl.items import Container

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "ChildWindow",
    "Clipper",
    "CollapsingHeader",
    "DragPayload",
    "FileDialog",
    "FilterSet",
    "Group",
    "ItemPool",
    "ItemSet",
    "Menu",
    "MenuBar",
    "Stage",
    "Tab",
    "TabBar",
    "Tooltip",
    "TreeNode",
    "ViewportMenuBar",
    "Window",
]


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
    _command = dearpygui.dearpygui.add_child_window

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        border: bool = True, 
        autosize_x: bool = False, 
        autosize_y: bool = False, 
        no_scrollbar: bool = False, 
        horizontal_scrollbar: bool = False, 
        menubar: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.border = border
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar


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
    _command = dearpygui.dearpygui.add_clipper

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.show = show
        self.delay_search = delay_search


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
    _command = dearpygui.dearpygui.add_collapsing_header

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        closable: bool = False, 
        default_open: bool = False, 
        open_on_double_click: bool = False, 
        open_on_arrow: bool = False, 
        leaf: bool = False, 
        bullet: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.closable = closable
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


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
    _command = dearpygui.dearpygui.add_drag_payload

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        show: bool = True, 
        drag_data: Any = None, 
        drop_data: Any = None, 
        payload_type: str = '$$DPG_PAYLOAD', 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.show = show
        self.drag_data = drag_data
        self.drop_data = drop_data
        self.payload_type = payload_type


class FileDialog(Container):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by default. Callback will be ran when the file or directory picker is closed. The app_data arguemnt will be populated with information related to the file and directory as a dictionary.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            default_path (str, optional): Path that the file dialog will default to when opened.
            default_filename (str, optional): Default name that will show in the file name input.
            file_count (int, optional): Number of visible files in the dialog.
            modal (bool, optional): Forces user interaction with the file selector.
            directory_selector (bool, optional): Shows only directory/paths as options. Allows selection of directory/paths only.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_file_dialog

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        default_path: str = '', 
        default_filename: str = '.', 
        file_count: int = 0, 
        modal: bool = False, 
        directory_selector: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            callback=callback,
            show=show,
            default_path=default_path,
            default_filename=default_filename,
            file_count=file_count,
            modal=modal,
            directory_selector=directory_selector,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.callback = callback
        self.show = show
        self.default_path = default_path
        self.default_filename = default_filename
        self.file_count = file_count
        self.modal = modal
        self.directory_selector = directory_selector


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
    _command = dearpygui.dearpygui.add_filter_set

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.show = show
        self.delay_search = delay_search


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
    _command = dearpygui.dearpygui.add_group

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        horizontal: bool = False, 
        horizontal_spacing: float = -1, 
        xoffset: float = 0.0, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing
        self.xoffset = xoffset


class ItemPool(Container):
    """Adds an item pool.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_pool

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class ItemSet(Container):
    """Adds an item set to an item pool.
    
    Args:
            type (int): 
            count (int): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_set

    def __init__(
        self, 
        item_type: int, 
        count: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            item_type=item_type,
            count=count,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.count = count
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label


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
    _command = dearpygui.dearpygui.add_menu

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset


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
    _command = dearpygui.dearpygui.add_menu_bar

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.show = show
        self.delay_search = delay_search


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
    _command = dearpygui.dearpygui.add_stage

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label


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
    _command = dearpygui.dearpygui.add_tab

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        closable: bool = False, 
        no_tooltip: bool = False, 
        order_mode: bool = 0, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.closable = closable
        self.no_tooltip = no_tooltip
        self.order_mode = order_mode


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
    _command = dearpygui.dearpygui.add_tab_bar

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        reorderable: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.reorderable = reorderable


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
    _command = dearpygui.dearpygui.add_tooltip

    def __init__(
        self, 
        parent: Union[int, str], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.show = show


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
    _command = dearpygui.dearpygui.add_tree_node

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        default_open: bool = False, 
        open_on_double_click: bool = False, 
        open_on_arrow: bool = False, 
        leaf: bool = False, 
        bullet: bool = False, 
        selectable: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet
        self.selectable = selectable


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
    _command = dearpygui.dearpygui.add_viewport_menu_bar

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.show = show
        self.delay_search = delay_search


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
    _command = dearpygui.dearpygui.add_window

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        delay_search: bool = False, 
        min_size: Union[List[int], Tuple[int, ...]] = [100, 100], 
        max_size: Union[List[int], Tuple[int, ...]] = [30000, 30000], 
        menubar: bool = False, 
        collapsed: bool = False, 
        autosize: bool = False, 
        no_resize: bool = False, 
        no_title_bar: bool = False, 
        no_move: bool = False, 
        no_scrollbar: bool = False, 
        no_collapse: bool = False, 
        horizontal_scrollbar: bool = False, 
        no_focus_on_appearing: bool = False, 
        no_bring_to_front_on_focus: bool = False, 
        no_close: bool = False, 
        no_background: bool = False, 
        modal: bool = False, 
        popup: bool = False, 
        no_saved_settings: bool = False, 
        on_close: Callable = None, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.show = show
        self.pos = pos
        self.delay_search = delay_search
        self.min_size = min_size
        self.max_size = max_size
        self.menubar = menubar
        self.collapsed = collapsed
        self.autosize = autosize
        self.no_resize = no_resize
        self.no_title_bar = no_title_bar
        self.no_move = no_move
        self.no_scrollbar = no_scrollbar
        self.no_collapse = no_collapse
        self.horizontal_scrollbar = horizontal_scrollbar
        self.no_focus_on_appearing = no_focus_on_appearing
        self.no_bring_to_front_on_focus = no_bring_to_front_on_focus
        self.no_close = no_close
        self.no_background = no_background
        self.modal = modal
        self.popup = popup
        self.no_saved_settings = no_saved_settings
        self.on_close = on_close
