from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from dearpypixl.item.container import Container
from dearpypixl.item.widget import Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Table",
    "TableCell",
    "TableRow",
    "TableColumn",
]


class Table(Container):
    """Adds a table.
    
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
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            header_row (bool, optional): show headers at the top of the columns
            clipper (bool, optional): Use clipper (rows must be same height).
            inner_width (int, optional): 
            policy (int, optional): 
            freeze_rows (int, optional): 
            freeze_columns (int, optional): 
            sort_multi (bool, optional): Hold shift when clicking headers to sort on multiple column.
            sort_tristate (bool, optional): Allow no sorting, disable default sorting.
            resizable (bool, optional): Enable resizing columns
            reorderable (bool, optional): Enable reordering columns in header row (need calling TableSetupColumn() + TableHeadersRow() to display headers)
            hideable (bool, optional): Enable hiding/disabling columns in context menu.
            sortable (bool, optional): Enable sorting. Call TableGetSortSpecs() to obtain sort specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.
            context_menu_in_body (bool, optional): Right-click on columns body/contents will display table context menu. By default it is available in TableHeadersRow().
            row_background (bool, optional): Set each RowBg color with ImGuiCol_TableRowBg or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with ImGuiTableBgFlags_RowBg0 on each row manually)
            borders_innerH (bool, optional): Draw horizontal borders between rows.
            borders_outerH (bool, optional): Draw horizontal borders at the top and bottom.
            borders_innerV (bool, optional): Draw vertical borders between columns.
            borders_outerV (bool, optional): Draw vertical borders on the left and right sides.
            no_host_extendX (bool, optional): Make outer width auto-fit to columns, overriding outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch columns are not used.
            no_host_extendY (bool, optional): Make outer height stop exactly at outer_size.y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY are disabled. Data below the limit will be clipped and not visible.
            no_keep_columns_visible (bool, optional): Disable keeping column always minimally visible when ScrollX is off and table gets too small. Not recommended if columns are resizable.
            precise_widths (bool, optional): Disable distributing remainder width to stretched columns (width allocation on a 100-wide table with 3 columns: Without this flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will appear to be less smooth.
            no_clip (bool, optional): Disable clipping rectangle for every individual columns.
            pad_outerX (bool, optional): Default if BordersOuterV is on. Enable outer-most padding. Generally desirable if you have headers.
            no_pad_outerX (bool, optional): Default if BordersOuterV is off. Disable outer-most padding.
            no_pad_innerX (bool, optional): Disable inner padding between columns (double inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).
            scrollX (bool, optional): Enable horizontal scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size. Changes default sizing policy. Because this create a child window, ScrollY is currently generally recommended when using ScrollX.
            scrollY (bool, optional): Enable vertical scrolling.
            no_saved_settings (bool, optional): Never load/save settings in .ini file.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_table

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
        source: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        header_row: bool = True, 
        clipper: bool = False, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            header_row=header_row,
            clipper=clipper,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.source = source
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.header_row = header_row
        self.clipper = clipper
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


class TableCell(Container):
    """Adds a table.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            height (int, optional): Height of the item.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            filter_key (str, optional): Used by filter widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_table_cell

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        height: int = 0, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        filter_key: str = '', 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            height=height,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.height = height
        self.show = show
        self.filter_key = filter_key


class TableRow(Container):
    """Adds a table row.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            height (int, optional): Height of the item.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            filter_key (str, optional): Used by filter widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_table_row

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        height: int = 0, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        filter_key: str = '', 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            height=height,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.height = height
        self.show = show
        self.filter_key = filter_key


class TableColumn(Widget):
    """Adds a table column.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            init_width_or_weight (float, optional): 
            default_hide (bool, optional): Default as a hidden/disabled column.
            default_sort (bool, optional): Default as a sorting column.
            width_stretch (bool, optional): Column will stretch. Preferable with horizontal scrolling disabled (default if table sizing policy is _SizingStretchSame or _SizingStretchProp).
            width_fixed (bool, optional): Column will not stretch. Preferable with horizontal scrolling enabled (default if table sizing policy is _SizingFixedFit and table is resizable).
            no_resize (bool, optional): Disable manual resizing.
            no_reorder (bool, optional): Disable manual reordering this column, this will also prevent other columns from crossing over this column.
            no_hide (bool, optional): Disable ability to hide/disable this column.
            no_clip (bool, optional): Disable clipping for this column (all NoClip columns will render in a same draw command).
            no_sort (bool, optional): Disable ability to sort on this field (even if ImGuiTableFlags_Sortable is set on the table).
            no_sort_ascending (bool, optional): Disable ability to sort in the ascending direction.
            no_sort_descending (bool, optional): Disable ability to sort in the descending direction.
            no_header_width (bool, optional): Disable header text width contribution to automatic column width.
            prefer_sort_ascending (bool, optional): Make the initial sort direction Ascending when first sorting on this column (default).
            prefer_sort_descending (bool, optional): Make the initial sort direction Descending when first sorting on this column.
            indent_enable (bool, optional): Use current Indent value when entering cell (default for column 0).
            indent_disable (bool, optional): Ignore current Indent value when entering cell (default for columns > 0). Indentation changes _within_ the cell will still be honored.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_table_column

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        enabled: bool = True, 
        init_width_or_weight: float = 0.0, 
        default_hide: bool = False, 
        default_sort: bool = False, 
        width_stretch: bool = False, 
        width_fixed: bool = False, 
        no_resize: bool = False, 
        no_reorder: bool = False, 
        no_hide: bool = False, 
        no_clip: bool = False, 
        no_sort: bool = False, 
        no_sort_ascending: bool = False, 
        no_sort_descending: bool = False, 
        no_header_width: bool = False, 
        prefer_sort_ascending: bool = True, 
        prefer_sort_descending: bool = False, 
        indent_enable: bool = False, 
        indent_disable: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            parent=parent,
            before=before,
            show=show,
            enabled=enabled,
            init_width_or_weight=init_width_or_weight,
            default_hide=default_hide,
            default_sort=default_sort,
            width_stretch=width_stretch,
            width_fixed=width_fixed,
            no_resize=no_resize,
            no_reorder=no_reorder,
            no_hide=no_hide,
            no_clip=no_clip,
            no_sort=no_sort,
            no_sort_ascending=no_sort_ascending,
            no_sort_descending=no_sort_descending,
            no_header_width=no_header_width,
            prefer_sort_ascending=prefer_sort_ascending,
            prefer_sort_descending=prefer_sort_descending,
            indent_enable=indent_enable,
            indent_disable=indent_disable,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.show = show
        self.enabled = enabled
        self.init_width_or_weight = init_width_or_weight
        self.default_hide = default_hide
        self.default_sort = default_sort
        self.width_stretch = width_stretch
        self.width_fixed = width_fixed
        self.no_resize = no_resize
        self.no_reorder = no_reorder
        self.no_hide = no_hide
        self.no_clip = no_clip
        self.no_sort = no_sort
        self.no_sort_ascending = no_sort_ascending
        self.no_sort_descending = no_sort_descending
        self.no_header_width = no_header_width
        self.prefer_sort_ascending = prefer_sort_ascending
        self.prefer_sort_descending = prefer_sort_descending
        self.indent_enable = indent_enable
        self.indent_disable = indent_disable
