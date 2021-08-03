from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.widget import Container

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Child",
    "Clipper",
    "CollapsingHeader",
    "DragPayload",
    "FileDialog",
    "FilterSet",
    "Group",
    "Menu",
    "MenuBar",
    "StagingContainer",
    "Tab",
    "TabBar",
    "Table",
    "TableRow",
    "Tooltip",
    "TreeNode",
    "ViewportMenuBar",
    "Window",
]


class Child(Container):
    """Adds an embedded child window. Will show scrollbars when items do not fit. Must be followed by a call to end.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
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
            **border (bool): Shows/Hides the border around the sides.
            **autosize_x (bool): Autosize the window to fit it's items in the x.
            **autosize_y (bool): Autosize the window to fit it's items in the y.
            **no_scrollbar (bool):  Disable scrollbars (window can still scroll with mouse or programmatically).
            **horizontal_scrollbar (bool): Allow horizontal scrollbar to appear (off by default).
            **menubar (bool): Shows/Hides the menubar at the top.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_child

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
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
            width=width,
            height=height,
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
            user_data=user_data,
            border=border,
            autosize_x=autosize_x,
            autosize_y=autosize_y,
            no_scrollbar=no_scrollbar,
            horizontal_scrollbar=horizontal_scrollbar,
            menubar=menubar,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
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
        self.border = border
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar


class Clipper(Container):
    """Helper to manually clip large list of items. Increases performance by not searching or drawing widgets outside of the clipped region.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_clipper

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            delay_search=delay_search,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.delay_search = delay_search
        self.user_data = user_data


class CollapsingHeader(Container):
    """Adds a collapsing header to add items to. Must be closed with the end command.
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
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **closable (bool): Adds the ability to hide this widget by pressing the (x) in the top right of widget.
            **default_open (bool): Sets the collapseable header open by default.
            **open_on_double_click (bool): Need double-click to open node.
            **open_on_arrow (bool): Only open when clicking on the arrow part.
            **leaf (bool): No collapsing, no arrow (use as a convenience for leaf nodes).
            **bullet (bool): Display a bullet instead of arrow.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_collapsing_header

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
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
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
            user_data=user_data,
            closable=closable,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
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
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.closable = closable
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


class DragPayload(Container):
    """User data payload for drag and drop operations.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **drag_data (Any): Drag data
            **payload_type (str): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_payload

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        drag_data: Any = None, 
        payload_type: str = '$$DPG_PAYLOAD', 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            show=show,
            user_data=user_data,
            drag_data=drag_data,
            payload_type=payload_type,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.show = show
        self.user_data = user_data
        self.drag_data = drag_data
        self.payload_type = payload_type


class FileDialog(Container):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by default.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **default_path (str): Path that the file dialog will default to when opened.
            **default_filename (str): Default name that will show in the file name input.
            **file_count (int): Number of visible files in the dialog.
            **modal (bool): Forces user interaction with the file selector.
            **directory_selector (bool): Shows only directory/paths as options. Allows selection of directory/paths only.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_file_dialog

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        default_path: str = '', 
        default_filename: str = '.', 
        file_count: int = 0, 
        modal: bool = False, 
        directory_selector: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            callback=callback,
            show=show,
            user_data=user_data,
            default_path=default_path,
            default_filename=default_filename,
            file_count=file_count,
            modal=modal,
            directory_selector=directory_selector,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.default_path = default_path
        self.default_filename = default_filename
        self.file_count = file_count
        self.modal = modal
        self.directory_selector = directory_selector


class FilterSet(Container):
    """Helper to parse and apply text filters (e.g. aaaaa[, bbbbb][, ccccc])
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_filter_set

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            delay_search=delay_search,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.delay_search = delay_search
        self.user_data = user_data


class Group(Container):
    """Creates a group that other widgets can belong to. The group allows item commands to be issued for all of its members. Must be closed with the end command.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
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
            **horizontal (bool): Forces child widgets to be added in a horizontal layout.
            **horizontal_spacing (float): Spacing for the horizontal layout.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_group

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
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
        horizontal: bool = False, 
        horizontal_spacing: float = -1, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            horizontal=horizontal,
            horizontal_spacing=horizontal_spacing,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.indent = indent
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
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing


class Menu(Container):
    """Adds a menu to an existing menu bar. Must be followed by a call to end.
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
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_menu

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
        enabled: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
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
            enabled=enabled,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
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
        self.enabled = enabled
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data


class MenuBar(Container):
    """Adds a menu bar to a window.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **show (bool): Attempt to render widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_menu_bar

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.show = show
        self.delay_search = delay_search
        self.user_data = user_data


class StagingContainer(Container):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_staging_container

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data


class Tab(Container):
    """Adds a tab to a tab bar. Must be closed with thes end command.
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
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **closable (bool): Creates a button on the tab that can hide the tab.
            **no_tooltip (bool): Disable tooltip for the given tab.
            **order_mode (bool): set using a constant: mvTabOrder_Reorderable: allows reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to front, mvTabOrder_Trailing: adds tab to back
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_tab

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
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        closable: bool = False, 
        no_tooltip: bool = False, 
        order_mode: bool = 0, 
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
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            closable=closable,
            no_tooltip=no_tooltip,
            order_mode=order_mode,
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
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.closable = closable
        self.no_tooltip = no_tooltip
        self.order_mode = order_mode


class TabBar(Container):
    """Adds a tab bar.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **reorderable (bool): Allows for the user to change the order of the tabs.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_tab_bar

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        reorderable: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            reorderable=reorderable,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.reorderable = reorderable


class Table(Container):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
            **header_row (bool): show headers at the top of the columns
            **inner_width (int): 
            **policy (int): 
            **freeze_rows (int): 
            **freeze_columns (int): 
            **sort_multi (bool): Hold shift when clicking headers to sort on multiple column.
            **sort_tristate (bool): Allow no sorting, disable default sorting.
            **resizable (bool): Enable resizing columns
            **reorderable (bool): Enable reordering columns in header row (need calling TableSetupColumn() + TableHeadersRow() to display headers)
            **hideable (bool): Enable hiding/disabling columns in context menu.
            **sortable (bool): Enable sorting. Call TableGetSortSpecs() to obtain sort specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.
            **context_menu_in_body (bool): Right-click on columns body/contents will display table context menu. By default it is available in TableHeadersRow().
            **row_background (bool): Set each RowBg color with ImGuiCol_TableRowBg or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with ImGuiTableBgFlags_RowBg0 on each row manually)
            **borders_innerH (bool): Draw horizontal borders between rows.
            **borders_outerH (bool): Draw horizontal borders at the top and bottom.
            **borders_innerV (bool): Draw vertical borders between columns.
            **borders_outerV (bool): Draw vertical borders on the left and right sides.
            **no_host_extendX (bool): Make outer width auto-fit to columns, overriding outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch columns are not used.
            **no_host_extendY (bool): Make outer height stop exactly at outer_size.y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY are disabled. Data below the limit will be clipped and not visible.
            **no_keep_columns_visible (bool): Disable keeping column always minimally visible when ScrollX is off and table gets too small. Not recommended if columns are resizable.
            **precise_widths (bool): Disable distributing remainder width to stretched columns (width allocation on a 100-wide table with 3 columns: Without this flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will appear to be less smooth.
            **no_clip (bool): Disable clipping rectangle for every individual columns.
            **pad_outerX (bool): Default if BordersOuterV is on. Enable outer-most padding. Generally desirable if you have headers.
            **no_pad_outerX (bool): Default if BordersOuterV is off. Disable outer-most padding.
            **no_pad_innerX (bool): Disable inner padding between columns (double inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).
            **scrollX (bool): Enable horizontal scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size. Changes default sizing policy. Because this create a child window, ScrollY is currently generally recommended when using ScrollX.
            **scrollY (bool): Enable vertical scrolling.
            **no_saved_settings (bool): Never load/save settings in .ini file.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_table

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        user_data: Any = None, 
        header_row: bool = True, 
        inner_width: int = 0, 
        policy: int = 0, 
        freeze_rows: int = 0, 
        freeze_columns: int = 0, 
        sort_multi: bool = False, 
        sort_tristate: bool = False, 
        resizable: bool = False, 
        reorderable: bool = False, 
        hideable: bool = False, 
        sortable: bool = False, 
        context_menu_in_body: bool = False, 
        row_background: bool = False, 
        borders_innerH: bool = False, 
        borders_outerH: bool = False, 
        borders_innerV: bool = False, 
        borders_outerV: bool = False, 
        no_host_extendX: bool = False, 
        no_host_extendY: bool = False, 
        no_keep_columns_visible: bool = False, 
        precise_widths: bool = False, 
        no_clip: bool = False, 
        pad_outerX: bool = False, 
        no_pad_outerX: bool = False, 
        no_pad_innerX: bool = False, 
        scrollX: bool = False, 
        scrollY: bool = False, 
        no_saved_settings: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            user_data=user_data,
            header_row=header_row,
            inner_width=inner_width,
            policy=policy,
            freeze_rows=freeze_rows,
            freeze_columns=freeze_columns,
            sort_multi=sort_multi,
            sort_tristate=sort_tristate,
            resizable=resizable,
            reorderable=reorderable,
            hideable=hideable,
            sortable=sortable,
            context_menu_in_body=context_menu_in_body,
            row_background=row_background,
            borders_innerH=borders_innerH,
            borders_outerH=borders_outerH,
            borders_innerV=borders_innerV,
            borders_outerV=borders_outerV,
            no_host_extendX=no_host_extendX,
            no_host_extendY=no_host_extendY,
            no_keep_columns_visible=no_keep_columns_visible,
            precise_widths=precise_widths,
            no_clip=no_clip,
            pad_outerX=pad_outerX,
            no_pad_outerX=no_pad_outerX,
            no_pad_innerX=no_pad_innerX,
            scrollX=scrollX,
            scrollY=scrollY,
            no_saved_settings=no_saved_settings,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.user_data = user_data
        self.header_row = header_row
        self.inner_width = inner_width
        self.policy = policy
        self.freeze_rows = freeze_rows
        self.freeze_columns = freeze_columns
        self.sort_multi = sort_multi
        self.sort_tristate = sort_tristate
        self.resizable = resizable
        self.reorderable = reorderable
        self.hideable = hideable
        self.sortable = sortable
        self.context_menu_in_body = context_menu_in_body
        self.row_background = row_background
        self.borders_innerH = borders_innerH
        self.borders_outerH = borders_outerH
        self.borders_innerV = borders_innerV
        self.borders_outerV = borders_outerV
        self.no_host_extendX = no_host_extendX
        self.no_host_extendY = no_host_extendY
        self.no_keep_columns_visible = no_keep_columns_visible
        self.precise_widths = precise_widths
        self.no_clip = no_clip
        self.pad_outerX = pad_outerX
        self.no_pad_outerX = no_pad_outerX
        self.no_pad_innerX = no_pad_innerX
        self.scrollX = scrollX
        self.scrollY = scrollY
        self.no_saved_settings = no_saved_settings


class TableRow(Container):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **height (int): Height of the item.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_table_row

    def __init__(
        self, 
        label: str = None, 
        height: int = 0, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        filter_key: str = '', 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            height=height,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.height = height
        self.parent = parent
        self.before = before
        self.show = show
        self.filter_key = filter_key
        self.user_data = user_data


class Tooltip(Container):
    """Adds an advanced tool tip for an item. This command must come immediately after the item the tip is for.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_tooltip

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.show = show
        self.user_data = user_data


class TreeNode(Container):
    """Adds a tree node to add items to. Must be closed with the end command.
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
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_open (bool): Sets the tree node open by default.
            **open_on_double_click (bool): Need double-click to open node.
            **open_on_arrow (bool): Only open when clicking on the arrow part.
            **leaf (bool): No collapsing, no arrow (use as a convenience for leaf nodes).
            **bullet (bool): Display a bullet instead of arrow.
            **selectable (bool): Makes the tree selectable.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_tree_node

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
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
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
            user_data=user_data,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
            selectable=selectable,
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
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet
        self.selectable = selectable


class ViewportMenuBar(Container):
    """Adds a menu bar to the viewport.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **show (bool): Attempt to render widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_viewport_menu_bar

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        show: bool = True, 
        delay_search: bool = False, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.show = show
        self.delay_search = delay_search
        self.user_data = user_data


class Window(Container):
    """Creates a new window for following items to be added to.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
            **min_size (List[int]): Minimum window size.
            **max_size (List[int]): Maximum window size.
            **menubar (bool): Shows or hides the menubar.
            **collapsed (bool): Collapse the window.
            **autosize (bool): Autosized the window to fit it's items.
            **no_resize (bool): Allows for the window size to be changed or fixed.
            **no_title_bar (bool): Title name for the title bar of the window.
            **no_move (bool): Allows for the window's position to be changed or fixed.
            **no_scrollbar (bool):  Disable scrollbars. (window can still scroll with mouse or programmatically)
            **no_collapse (bool): Disable user collapsing window by double-clicking on it.
            **horizontal_scrollbar (bool): Allow horizontal scrollbar to appear. (off by default)
            **no_focus_on_appearing (bool): Disable taking focus when transitioning from hidden to visible state.
            **no_bring_to_front_on_focus (bool): Disable bringing window to front when taking focus. (e.g. clicking on it or programmatically giving it focus)
            **no_close (bool): Disable user closing the window by removing the close button.
            **no_background (bool): Sets Background and border alpha to transparent.
            **modal (bool): Fills area behind window according to the theme and disables user ability to interact with anything except the window.
            **popup (bool): Fills area behind window according to the theme, removes title bar, collapse and close. Window can be closed by selecting area in the background behind the window.
            **no_saved_settings (bool): Never load/save settings in .ini file.
            **on_close (Callable): Callback ran when window is closed.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_window

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        show: bool = True, 
        pos: list[int] = [], 
        delay_search: bool = False, 
        user_data: Any = None, 
        min_size: list[int] = [100, 100], 
        max_size: list[int] = [30000, 30000], 
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
            width=width,
            height=height,
            indent=indent,
            show=show,
            pos=pos,
            delay_search=delay_search,
            user_data=user_data,
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
        self.width = width
        self.height = height
        self.indent = indent
        self.show = show
        self.pos = pos
        self.delay_search = delay_search
        self.user_data = user_data
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
