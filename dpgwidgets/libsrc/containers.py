from typing import Any, Callable
import dearpygui.dearpygui
from widget import Container

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
