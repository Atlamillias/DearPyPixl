from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.widget import Container, Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Plot",
    "Subplots",
    "HistogramSeries",
    "AreaSeries",
    "BarSeries",
    "CandleSeries",
    "DragPoint",
    "ErrorSeries",
    "HeatSeries",
    "HistogramSeries",
    "HlineSeries",
    "ImageSeries",
    "LineSeries",
    "PieSeries",
    "PlotAnnotation",
    "PlotAxis",
    "PlotLegend",
    "ScatterSeries",
    "ShadeSeries",
    "SimplePlot",
    "StairSeries",
    "StemSeries",
    "TextPoint",
    "VlineSeries",
]


class Plot(Container):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
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
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **no_title (bool): 
            **no_menus (bool): 
            **no_box_select (bool): 
            **no_mouse_pos (bool): 
            **no_highlight (bool): 
            **no_child (bool): 
            **query (bool): 
            **crosshairs (bool): 
            **anti_aliased (bool): 
            **equal_aspects (bool): 
            **pan_button (int): enables panning when held
            **pan_mod (int): optional modifier that must be held for panning
            **fit_button (int): fits visible data when double clicked
            **context_menu_button (int): opens plot context menu (if enabled) when clicked
            **box_select_button (int): begins box selection when pressed and confirms selection when released
            **box_select_mod (int): begins box selection when pressed and confirms selection when released
            **box_select_cancel_button (int): cancels active box selection when pressed
            **query_button (int): begins query selection when pressed and end query selection when released
            **query_mod (int): optional modifier that must be held for query selection
            **query_toggle_mod (int): when held, active box selections turn into queries
            **horizontal_mod (int): expands active box selection/query horizontally to plot edge when held
            **vertical_mod (int): expands active box selection/query vertically to plot edge when held
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_plot

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
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
        use_internal_label: bool = True, 
        no_title: bool = False, 
        no_menus: bool = False, 
        no_box_select: bool = False, 
        no_mouse_pos: bool = False, 
        no_highlight: bool = False, 
        no_child: bool = False, 
        query: bool = False, 
        crosshairs: bool = False, 
        anti_aliased: bool = False, 
        equal_aspects: bool = False, 
        pan_button: int = 0, 
        pan_mod: int = -1, 
        fit_button: int = 0, 
        context_menu_button: int = 1, 
        box_select_button: int = 1, 
        box_select_mod: int = -1, 
        box_select_cancel_button: int = 0, 
        query_button: int = 2, 
        query_mod: int = -1, 
        query_toggle_mod: int = 17, 
        horizontal_mod: int = 18, 
        vertical_mod: int = 16, 
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
            use_internal_label=use_internal_label,
            no_title=no_title,
            no_menus=no_menus,
            no_box_select=no_box_select,
            no_mouse_pos=no_mouse_pos,
            no_highlight=no_highlight,
            no_child=no_child,
            query=query,
            crosshairs=crosshairs,
            anti_aliased=anti_aliased,
            equal_aspects=equal_aspects,
            pan_button=pan_button,
            pan_mod=pan_mod,
            fit_button=fit_button,
            context_menu_button=context_menu_button,
            box_select_button=box_select_button,
            box_select_mod=box_select_mod,
            box_select_cancel_button=box_select_cancel_button,
            query_button=query_button,
            query_mod=query_mod,
            query_toggle_mod=query_toggle_mod,
            horizontal_mod=horizontal_mod,
            vertical_mod=vertical_mod,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
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
        self.use_internal_label = use_internal_label
        self.no_title = no_title
        self.no_menus = no_menus
        self.no_box_select = no_box_select
        self.no_mouse_pos = no_mouse_pos
        self.no_highlight = no_highlight
        self.no_child = no_child
        self.query = query
        self.crosshairs = crosshairs
        self.anti_aliased = anti_aliased
        self.equal_aspects = equal_aspects
        self.pan_button = pan_button
        self.pan_mod = pan_mod
        self.fit_button = fit_button
        self.context_menu_button = context_menu_button
        self.box_select_button = box_select_button
        self.box_select_mod = box_select_mod
        self.box_select_cancel_button = box_select_cancel_button
        self.query_button = query_button
        self.query_mod = query_mod
        self.query_toggle_mod = query_toggle_mod
        self.horizontal_mod = horizontal_mod
        self.vertical_mod = vertical_mod


class Subplots(Container):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.
    Args:
            rows (int): 
            columns (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **row_ratios (List[float]): 
            **column_ratios (List[float]): 
            **no_title (bool): 
            **no_menus (bool): the user will not be able to open context menus with right-click
            **no_resize (bool): resize splitters between subplot cells will be not be provided
            **no_align (bool): subplot edges will not be aligned vertically or horizontally
            **link_rows (bool): link the y-axis limits of all plots in each row (does not apply auxiliary y-axes)
            **link_columns (bool): link the x-axis limits of all plots in each column
            **link_all_x (bool): link the x-axis limits in every plot in the subplot
            **link_all_y (bool): link the y-axis limits in every plot in the subplot (does not apply to auxiliary y-axes)
            **column_major (bool): subplots are added in column major order instead of the default row major order
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_subplots

    def __init__(
        self, 
        rows: int, 
        columns: int, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        row_ratios: list[float] = [], 
        column_ratios: list[float] = [], 
        no_title: bool = False, 
        no_menus: bool = False, 
        no_resize: bool = False, 
        no_align: bool = False, 
        link_rows: bool = False, 
        link_columns: bool = False, 
        link_all_x: bool = False, 
        link_all_y: bool = False, 
        column_major: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            rows=rows,
            columns=columns,
            label=label,
            width=width,
            height=height,
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            row_ratios=row_ratios,
            column_ratios=column_ratios,
            no_title=no_title,
            no_menus=no_menus,
            no_resize=no_resize,
            no_align=no_align,
            link_rows=link_rows,
            link_columns=link_columns,
            link_all_x=link_all_x,
            link_all_y=link_all_y,
            column_major=column_major,
            **kwargs,
        )
        self.rows = rows
        self.columns = columns
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.row_ratios = row_ratios
        self.column_ratios = column_ratios
        self.no_title = no_title
        self.no_menus = no_menus
        self.no_resize = no_resize
        self.no_align = no_align
        self.link_rows = link_rows
        self.link_columns = link_columns
        self.link_all_x = link_all_x
        self.link_all_y = link_all_y
        self.column_major = column_major


class HistogramSeries(Widget):
    """Undocumented function
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **xbins (int): 
            **ybins (int): 
            **xmin_range (float): 
            **xmax_range (float): 
            **ymin_range (float): 
            **ymax_range (float): 
            **density (bool): 
            **outliers (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_2d_histogram_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        xbins: int = -1, 
        ybins: int = -1, 
        xmin_range: float = 0.0, 
        xmax_range: float = 1.0, 
        ymin_range: float = 0.0, 
        ymax_range: float = 1.0, 
        density: bool = False, 
        outliers: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            xbins=xbins,
            ybins=ybins,
            xmin_range=xmin_range,
            xmax_range=xmax_range,
            ymin_range=ymin_range,
            ymax_range=ymax_range,
            density=density,
            outliers=outliers,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.xbins = xbins
        self.ybins = ybins
        self.xmin_range = xmin_range
        self.xmax_range = xmax_range
        self.ymin_range = ymin_range
        self.ymax_range = ymax_range
        self.density = density
        self.outliers = outliers


class AreaSeries(Widget):
    """Adds an area series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **fill (List[int]): 
            **contribute_to_bounds (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_area_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        fill: list[int] = (0, 0, 0, -255), 
        contribute_to_bounds: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            fill=fill,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.fill = fill
        self.contribute_to_bounds = contribute_to_bounds


class BarSeries(Widget):
    """Adds a bar series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **weight (float): 
            **horizontal (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_bar_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        weight: float = 1.0, 
        horizontal: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            weight=weight,
            horizontal=horizontal,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.weight = weight
        self.horizontal = horizontal


class CandleSeries(Widget):
    """Adds a candle series to a plot.
    Args:
            dates (Any): 
            opens (Any): 
            closes (Any): 
            lows (Any): 
            highs (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **bull_color (List[int]): 
            **bear_color (List[int]): 
            **weight (int): 
            **tooltip (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_candle_series

    def __init__(
        self, 
        dates: list[float], 
        opens: list[float], 
        closes: list[float], 
        lows: list[float], 
        highs: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        bull_color: list[int] = (0, 255, 113, 255), 
        bear_color: list[int] = (218, 13, 79, 255), 
        weight: int = 0.25, 
        tooltip: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            dates=dates,
            opens=opens,
            closes=closes,
            lows=lows,
            highs=highs,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            bull_color=bull_color,
            bear_color=bear_color,
            weight=weight,
            tooltip=tooltip,
            **kwargs,
        )
        self.dates = dates
        self.opens = opens
        self.closes = closes
        self.lows = lows
        self.highs = highs
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.bull_color = bull_color
        self.bear_color = bear_color
        self.weight = weight
        self.tooltip = tooltip


class DragPoint(Widget):
    """Adds a drag point to a plot.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (Any): 
            **color (List[int]): 
            **thickness (float): 
            **show_label (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_point

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: Any = (0.0, 0.0), 
        color: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        show_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.color = color
        self.thickness = thickness
        self.show_label = show_label


class ErrorSeries(Widget):
    """Adds an error series to a plot.
    Args:
            x (Any): 
            y (Any): 
            negative (Any): 
            positive (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **contribute_to_bounds (bool): 
            **horizontal (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_error_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        negative: list[float], 
        positive: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        contribute_to_bounds: bool = True, 
        horizontal: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            negative=negative,
            positive=positive,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            contribute_to_bounds=contribute_to_bounds,
            horizontal=horizontal,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.negative = negative
        self.positive = positive
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.contribute_to_bounds = contribute_to_bounds
        self.horizontal = horizontal


class HeatSeries(Widget):
    """Adds a heat series to a plot. Typically a color scale widget is also added to show the legend.
    Args:
            x (Any): 
            rows (int): 
            cols (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **scale_min (float): Sets the color scale min. Typically paired with the color scale widget scale_min.
            **scale_max (float): Sets the color scale max. Typically paired with the color scale widget scale_max.
            **bounds_min (Any): 
            **bounds_max (Any): 
            **format (str): 
            **contribute_to_bounds (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_heat_series

    def __init__(
        self, 
        x: list[float], 
        rows: int, 
        cols: int, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        scale_min: float = 0.0, 
        scale_max: float = 1.0, 
        bounds_min: Any = (0.0, 0.0), 
        bounds_max: Any = (1.0, 1.0), 
        format: str = '%0.1f', 
        contribute_to_bounds: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            rows=rows,
            cols=cols,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            scale_min=scale_min,
            scale_max=scale_max,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            format=format,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )
        self.x = x
        self.rows = rows
        self.cols = cols
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.scale_min = scale_min
        self.scale_max = scale_max
        self.bounds_min = bounds_min
        self.bounds_max = bounds_max
        self.format = format
        self.contribute_to_bounds = contribute_to_bounds


class HistogramSeries(Widget):
    """Adds a histogram series to a plot.
    Args:
            x (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **bins (int): 
            **bar_scale (float): 
            **min_range (float): 
            **max_range (float): 
            **cumlative (bool): 
            **density (bool): 
            **outliers (bool): 
            **contribute_to_bounds (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_histogram_series

    def __init__(
        self, 
        x: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        bins: int = -1, 
        bar_scale: float = 1.0, 
        min_range: float = 0.0, 
        max_range: float = 1.0, 
        cumlative: bool = False, 
        density: bool = False, 
        outliers: bool = True, 
        contribute_to_bounds: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            bins=bins,
            bar_scale=bar_scale,
            min_range=min_range,
            max_range=max_range,
            cumlative=cumlative,
            density=density,
            outliers=outliers,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.bins = bins
        self.bar_scale = bar_scale
        self.min_range = min_range
        self.max_range = max_range
        self.cumlative = cumlative
        self.density = density
        self.outliers = outliers
        self.contribute_to_bounds = contribute_to_bounds


class HlineSeries(Widget):
    """Adds a infinite horizontal line series to a plot.
    Args:
            x (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **contribute_to_bounds (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_hline_series

    def __init__(
        self, 
        x: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        contribute_to_bounds: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.contribute_to_bounds = contribute_to_bounds


class ImageSeries(Widget):
    """Adds a image series to a plot.
    Args:
            texture_id (int): 
            bounds_min (Any): 
            bounds_max (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **uv_min (List[float]): normalized texture coordinates
            **uv_max (List[float]): normalized texture coordinates
            **tint_color (List[int]): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_image_series

    def __init__(
        self, 
        texture_id: int, 
        bounds_min: list[float], 
        bounds_max: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        uv_min: list[float] = (0.0, 0.0), 
        uv_max: list[float] = (1.0, 1.0), 
        tint_color: list[int] = (255, 255, 255, 255), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            uv_min=uv_min,
            uv_max=uv_max,
            tint_color=tint_color,
            **kwargs,
        )
        self.texture_id = texture_id
        self.bounds_min = bounds_min
        self.bounds_max = bounds_max
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.uv_min = uv_min
        self.uv_max = uv_max
        self.tint_color = tint_color


class LineSeries(Widget):
    """Adds a line series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_line_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class PieSeries(Widget):
    """Adds a pie series to a plot.
    Args:
            x (float): 
            y (float): 
            radius (float): 
            values (Any): 
            labels (List[str]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **format (str): 
            **angle (float): 
            **normalize (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_pie_series

    def __init__(
        self, 
        x: float, 
        y: float, 
        radius: float, 
        values: list[float], 
        labels: list[str], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        format: str = '%0.2f', 
        angle: float = 90.0, 
        normalize: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            radius=radius,
            values=values,
            labels=labels,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            format=format,
            angle=angle,
            normalize=normalize,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.radius = radius
        self.values = values
        self.labels = labels
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.format = format
        self.angle = angle
        self.normalize = normalize


class PlotAnnotation(Widget):
    """Adds an annotation to a plot.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (Any): 
            **offset (List[float]): 
            **color (List[int]): 
            **clamped (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_plot_annotation

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: Any = (0.0, 0.0), 
        offset: list[float] = (0.0, 0.0), 
        color: list[int] = (0, 0, 0, -255), 
        clamped: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            offset=offset,
            color=color,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.offset = offset
        self.color = color
        self.clamped = clamped


class PlotAxis(Widget):
    """Adds a plot legend to a plot.
    Args:
            axis (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **no_gridlines (bool): 
            **no_tick_marks (bool): 
            **no_tick_labels (bool): 
            **log_scale (bool): 
            **invert (bool): 
            **lock_min (bool): 
            **lock_max (bool): 
            **time (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_plot_axis

    def __init__(
        self, 
        axis: int, 
        label: str = None, 
        parent: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        no_gridlines: bool = False, 
        no_tick_marks: bool = False, 
        no_tick_labels: bool = False, 
        log_scale: bool = False, 
        invert: bool = False, 
        lock_min: bool = False, 
        lock_max: bool = False, 
        time: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            axis=axis,
            label=label,
            parent=parent,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            no_gridlines=no_gridlines,
            no_tick_marks=no_tick_marks,
            no_tick_labels=no_tick_labels,
            log_scale=log_scale,
            invert=invert,
            lock_min=lock_min,
            lock_max=lock_max,
            time=time,
            **kwargs,
        )
        self.axis = axis
        self.label = label
        self.parent = parent
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.no_gridlines = no_gridlines
        self.no_tick_marks = no_tick_marks
        self.no_tick_labels = no_tick_labels
        self.log_scale = log_scale
        self.invert = invert
        self.lock_min = lock_min
        self.lock_max = lock_max
        self.time = time


class PlotLegend(Widget):
    """Adds a plot legend to a plot.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **location (int): location, mvPlot_Location_*
            **horizontal (bool): 
            **outside (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_plot_legend

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        location: int = 5, 
        horizontal: bool = False, 
        outside: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            location=location,
            horizontal=horizontal,
            outside=outside,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.location = location
        self.horizontal = horizontal
        self.outside = outside


class ScatterSeries(Widget):
    """Adds a scatter series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_scatter_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class ShadeSeries(Widget):
    """Adds a shade series to a plot.
    Args:
            x (Any): 
            y1 (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **y2 (Any): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_shade_series

    def __init__(
        self, 
        x: list[float], 
        y1: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        y2: Any = [], 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y1=y1,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            y2=y2,
            **kwargs,
        )
        self.x = x
        self.y1 = y1
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.y2 = y2


class SimplePlot(Widget):
    """A simple plot for visualization of a 1 dimensional set of values.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (List[float]): 
            **overlay (str): overlays text (similar to a plot title)
            **histogram (bool): 
            **autosize (bool): 
            **min_scale (float): 
            **max_scale (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_simple_plot

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: list[float] = (), 
        overlay: str = '', 
        histogram: bool = False, 
        autosize: bool = True, 
        min_scale: float = 0.0, 
        max_scale: float = 0.0, 
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
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            overlay=overlay,
            histogram=histogram,
            autosize=autosize,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.overlay = overlay
        self.histogram = histogram
        self.autosize = autosize
        self.min_scale = min_scale
        self.max_scale = max_scale


class StairSeries(Widget):
    """Adds a stair series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_stair_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class StemSeries(Widget):
    """Adds a stem series to a plot.
    Args:
            x (Any): 
            y (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_stem_series

    def __init__(
        self, 
        x: list[float], 
        y: list[float], 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class TextPoint(Widget):
    """Adds a labels series to a plot.
    Args:
            x (float): 
            y (float): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **x_offset (int): 
            **y_offset (int): 
            **vertical (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_text_point

    def __init__(
        self, 
        x: float, 
        y: float, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        x_offset: int = Ellipsis, 
        y_offset: int = Ellipsis, 
        vertical: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            x_offset=x_offset,
            y_offset=y_offset,
            vertical=vertical,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.vertical = vertical


class VlineSeries(Widget):
    """Adds a infinite vertical line series to a plot.
    Args:
            x (Any): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_vline_series

    def __init__(
        self, 
        x: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
