from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from dearpypixl.items import Container
from dearpypixl.items import Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Plot",
    "PlotAxis",
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
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int, ...]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_title (bool, optional): 
            no_menus (bool, optional): 
            no_box_select (bool, optional): 
            no_mouse_pos (bool, optional): 
            no_highlight (bool, optional): 
            no_child (bool, optional): 
            query (bool, optional): 
            crosshairs (bool, optional): 
            anti_aliased (bool, optional): 
            equal_aspects (bool, optional): 
            pan_button (int, optional): enables panning when held
            pan_mod (int, optional): optional modifier that must be held for panning
            fit_button (int, optional): fits visible data when double clicked
            context_menu_button (int, optional): opens plot context menu (if enabled) when clicked
            box_select_button (int, optional): begins box selection when pressed and confirms selection when released
            box_select_mod (int, optional): begins box selection when pressed and confirms selection when released
            box_select_cancel_button (int, optional): cancels active box selection when pressed
            query_button (int, optional): begins query selection when pressed and end query selection when released
            query_mod (int, optional): optional modifier that must be held for query selection
            query_toggle_mod (int, optional): when held, active box selections turn into queries
            horizontal_mod (int, optional): expands active box selection/query horizontally to plot edge when held
            vertical_mod (int, optional): expands active box selection/query vertically to plot edge when held
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_plot

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
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int, ...]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
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


class PlotAxis(Container):
    """Adds an axis to a plot.
    
    Args:
            axis (int): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            no_gridlines (bool, optional): 
            no_tick_marks (bool, optional): 
            no_tick_labels (bool, optional): 
            log_scale (bool, optional): 
            invert (bool, optional): 
            lock_min (bool, optional): 
            lock_max (bool, optional): 
            time (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_plot_axis

    def __init__(
        self, 
        axis: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.no_gridlines = no_gridlines
        self.no_tick_marks = no_tick_marks
        self.no_tick_labels = no_tick_labels
        self.log_scale = log_scale
        self.invert = invert
        self.lock_min = lock_min
        self.lock_max = lock_max
        self.time = time


class Subplots(Container):
    """Adds a collection of plots.
    
    Args:
            rows (int): 
            columns (int): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
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
            row_ratios (Union[List[float], Tuple[float, ...]], optional): 
            column_ratios (Union[List[float], Tuple[float, ...]], optional): 
            no_title (bool, optional): 
            no_menus (bool, optional): the user will not be able to open context menus with right-click
            no_resize (bool, optional): resize splitters between subplot cells will be not be provided
            no_align (bool, optional): subplot edges will not be aligned vertically or horizontally
            link_rows (bool, optional): link the y-axis limits of all plots in each row (does not apply auxiliary y-axes)
            link_columns (bool, optional): link the x-axis limits of all plots in each column
            link_all_x (bool, optional): link the x-axis limits in every plot in the subplot
            link_all_y (bool, optional): link the y-axis limits in every plot in the subplot (does not apply to auxiliary y-axes)
            column_major (bool, optional): subplots are added in column major order instead of the default row major order
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_subplots

    def __init__(
        self, 
        rows: int, 
        columns: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
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
        row_ratios: Union[List[float], Tuple[float, ...]] = [], 
        column_ratios: Union[List[float], Tuple[float, ...]] = [], 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
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
    """Adds a 2d histogram series.
    
    Args:
            x (Any): 
            y (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            xbins (int, optional): 
            ybins (int, optional): 
            xmin_range (float, optional): 
            xmax_range (float, optional): 
            ymin_range (float, optional): 
            ymax_range (float, optional): 
            density (bool, optional): 
            outliers (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_2d_histogram_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
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
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            fill (Union[List[int], Tuple[int, ...]], optional): 
            contribute_to_bounds (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_area_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        fill: Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255), 
        contribute_to_bounds: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            fill=fill,
            contribute_to_bounds=contribute_to_bounds,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.fill = fill
        self.contribute_to_bounds = contribute_to_bounds


class BarSeries(Widget):
    """Adds a bar series to a plot.
    
    Args:
            x (Any): 
            y (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            weight (float, optional): 
            horizontal (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_bar_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        weight: float = 1.0, 
        horizontal: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            weight=weight,
            horizontal=horizontal,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
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
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            bull_color (Union[List[int], Tuple[int, ...]], optional): 
            bear_color (Union[List[int], Tuple[int, ...]], optional): 
            weight (int, optional): 
            tooltip (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_candle_series

    def __init__(
        self, 
        dates: Union[List[float], Tuple[float, ...]], 
        opens: Union[List[float], Tuple[float, ...]], 
        closes: Union[List[float], Tuple[float, ...]], 
        lows: Union[List[float], Tuple[float, ...]], 
        highs: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        bull_color: Union[List[int], Tuple[int, ...]] = (0, 255, 113, 255), 
        bear_color: Union[List[int], Tuple[int, ...]] = (218, 13, 79, 255), 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.bull_color = bull_color
        self.bear_color = bear_color
        self.weight = weight
        self.tooltip = tooltip


class DragPoint(Widget):
    """Adds a drag point to a plot.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            default_value (Any, optional): 
            color (Union[List[int], Tuple[int, ...]], optional): 
            thickness (float, optional): 
            show_label (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_point

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        value: Any = (0.0, 0.0), 
        color: Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        show_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            value=value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.callback = callback
        self.show = show
        self.value = value
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
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            contribute_to_bounds (bool, optional): 
            horizontal (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_error_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        negative: Union[List[float], Tuple[float, ...]], 
        positive: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
            horizontal=horizontal,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.negative = negative
        self.positive = positive
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds
        self.horizontal = horizontal


class HeatSeries(Widget):
    """Adds a heat series to a plot.
    
    Args:
            x (Any): 
            rows (int): 
            cols (int): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            scale_min (float, optional): Sets the color scale min. Typically paired with the color scale widget scale_min.
            scale_max (float, optional): Sets the color scale max. Typically paired with the color scale widget scale_max.
            bounds_min (Any, optional): 
            bounds_max (Any, optional): 
            format (str, optional): 
            contribute_to_bounds (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_heat_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        rows: int, 
        cols: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
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
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            bins (int, optional): 
            bar_scale (float, optional): 
            min_range (float, optional): 
            max_range (float, optional): 
            cumlative (bool, optional): 
            density (bool, optional): 
            outliers (bool, optional): 
            contribute_to_bounds (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_histogram_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.bins = bins
        self.bar_scale = bar_scale
        self.min_range = min_range
        self.max_range = max_range
        self.cumlative = cumlative
        self.density = density
        self.outliers = outliers
        self.contribute_to_bounds = contribute_to_bounds


class HlineSeries(Widget):
    """Adds an infinite horizontal line series to a plot.
    
    Args:
            x (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_hline_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show


class ImageSeries(Widget):
    """Adds an image series to a plot.
    
    Args:
            texture_tag (Union[int, str]): 
            bounds_min (Any): 
            bounds_max (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            uv_min (Union[List[float], Tuple[float, ...]], optional): normalized texture coordinates
            uv_max (Union[List[float], Tuple[float, ...]], optional): normalized texture coordinates
            tint_color (Union[List[int], Tuple[int, ...]], optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_image_series

    def __init__(
        self, 
        texture_tag: Union[int, str], 
        bounds_min: Union[List[float], Tuple[float, ...]], 
        bounds_max: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        uv_min: Union[List[float], Tuple[float, ...]] = (0.0, 0.0), 
        uv_max: Union[List[float], Tuple[float, ...]] = (1.0, 1.0), 
        tint_color: Union[List[int], Tuple[int, ...]] = (255, 255, 255, 255), 
        **kwargs, 
    ):
        super().__init__(
            texture_tag=texture_tag,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            uv_min=uv_min,
            uv_max=uv_max,
            tint_color=tint_color,
            **kwargs,
        )
        self.texture_tag = texture_tag
        self.bounds_min = bounds_min
        self.bounds_max = bounds_max
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.uv_min = uv_min
        self.uv_max = uv_max
        self.tint_color = tint_color


class LineSeries(Widget):
    """Adds a line series to a plot.
    
    Args:
            x (Any): 
            y (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_line_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show


class PieSeries(Widget):
    """Adds an pie series to a plot.
    
    Args:
            x (float): 
            y (float): 
            radius (float): 
            values (Any): 
            labels (Union[List[str], Tuple[str, ...]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            format (str, optional): 
            angle (float, optional): 
            normalize (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_pie_series

    def __init__(
        self, 
        x: float, 
        y: float, 
        radius: float, 
        values: Union[List[float], Tuple[float, ...]], 
        labels: Union[List[str], Tuple[str, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
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
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
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
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.format = format
        self.angle = angle
        self.normalize = normalize


class PlotAnnotation(Widget):
    """Adds an annotation to a plot.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            default_value (Any, optional): 
            offset (Union[List[float], Tuple[float, ...]], optional): 
            color (Union[List[int], Tuple[int, ...]], optional): 
            clamped (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_plot_annotation

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        value: Any = (0.0, 0.0), 
        offset: Union[List[float], Tuple[float, ...]] = (0.0, 0.0), 
        color: Union[List[int], Tuple[int, ...]] = (0, 0, 0, -255), 
        clamped: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            value=value,
            offset=offset,
            color=color,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.value = value
        self.offset = offset
        self.color = color
        self.clamped = clamped


class PlotLegend(Widget):
    """Adds a plot legend to a plot.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            location (int, optional): location, mvPlot_Location_*
            horizontal (bool, optional): 
            outside (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_plot_legend

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        location: int = 5, 
        horizontal: bool = False, 
        outside: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            location=location,
            horizontal=horizontal,
            outside=outside,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.location = location
        self.horizontal = horizontal
        self.outside = outside


class ScatterSeries(Widget):
    """Adds a scatter series to a plot.
    
    Args:
            x (Any): 
            y (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_scatter_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show


class ShadeSeries(Widget):
    """Adds a shade series to a plot.
    
    Args:
            x (Any): 
            y1 (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            y2 (Any, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_shade_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y1: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        y2: Any = [], 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y1=y1,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            y2=y2,
            **kwargs,
        )
        self.x = x
        self.y1 = y1
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.y2 = y2


class SimplePlot(Widget):
    """Adds a simple plot for visualization of a 1 dimensional set of values.
    
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
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[float], Tuple[float, ...]], optional): 
            overlay (str, optional): overlays text (similar to a plot title)
            histogram (bool, optional): 
            autosize (bool, optional): 
            min_scale (float, optional): 
            max_scale (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_simple_plot

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
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[float], Tuple[float, ...]] = (), 
        overlay: str = '', 
        histogram: bool = False, 
        autosize: bool = True, 
        min_scale: float = 0.0, 
        max_scale: float = 0.0, 
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
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            value=value,
            overlay=overlay,
            histogram=histogram,
            autosize=autosize,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
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
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_stair_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show


class StemSeries(Widget):
    """Adds a stem series to a plot.
    
    Args:
            x (Any): 
            y (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_stem_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        y: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.source = source
        self.show = show


class TextPoint(Widget):
    """Adds a label series to a plot.
    
    Args:
            x (float): 
            y (float): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            x_offset (int, optional): 
            y_offset (int, optional): 
            vertical (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_text_point

    def __init__(
        self, 
        x: float, 
        y: float, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        x_offset: int = Ellipsis, 
        y_offset: int = Ellipsis, 
        vertical: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            x_offset=x_offset,
            y_offset=y_offset,
            vertical=vertical,
            **kwargs,
        )
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.vertical = vertical


class VlineSeries(Widget):
    """Adds an infinite vertical line series to a plot.
    
    Args:
            x (Any): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_vline_series

    def __init__(
        self, 
        x: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            x=x,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            **kwargs,
        )
        self.x = x
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.show = show
