from typing import Any, Callable
import dearpygui.dearpygui
from widget import Container, Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Plot",
    "Subplots",
    "HistograSeries",
    "AreaSeries",
    "BarSeries",
    "CandleSeries",
    "DragPoint",
    "ErrorSeries",
    "HeatSeries",
    "HistograSeries",
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


class HistograSeries(Widget):
    _command = dearpygui.dearpygui.add_2d_histogra_series

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
        self.xbins = xbins
        self.ybins = ybins
        self.xmin_range = xmin_range
        self.xmax_range = xmax_range
        self.ymin_range = ymin_range
        self.ymax_range = ymax_range
        self.density = density
        self.outliers = outliers


class AreaSeries(Widget):
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
        self.fill = fill
        self.contribute_to_bounds = contribute_to_bounds


class BarSeries(Widget):
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
        self.weight = weight
        self.horizontal = horizontal


class CandleSeries(Widget):
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
        self.bull_color = bull_color
        self.bear_color = bear_color
        self.weight = weight
        self.tooltip = tooltip


class DragPoint(Widget):
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
        self.default_value = default_value
        self.color = color
        self.thickness = thickness
        self.show_label = show_label


class ErrorSeries(Widget):
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
        self.contribute_to_bounds = contribute_to_bounds
        self.horizontal = horizontal


class HeatSeries(Widget):
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
        self.scale_min = scale_min
        self.scale_max = scale_max
        self.bounds_min = bounds_min
        self.bounds_max = bounds_max
        self.format = format
        self.contribute_to_bounds = contribute_to_bounds


class HistograSeries(Widget):
    _command = dearpygui.dearpygui.add_histogra_series

    def __init__(
        self, 
        x: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
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
        self.bins = bins
        self.bar_scale = bar_scale
        self.min_range = min_range
        self.max_range = max_range
        self.cumlative = cumlative
        self.density = density
        self.outliers = outliers
        self.contribute_to_bounds = contribute_to_bounds


class HlineSeries(Widget):
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
        self.contribute_to_bounds = contribute_to_bounds


class ImageSeries(Widget):
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
        self.uv_min = uv_min
        self.uv_max = uv_max
        self.tint_color = tint_color


class LineSeries(Widget):
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


class PieSeries(Widget):
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
        self.format = format
        self.angle = angle
        self.normalize = normalize


class PlotAnnotation(Widget):
    _command = dearpygui.dearpygui.add_plot_annotation

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
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
        self.default_value = default_value
        self.offset = offset
        self.color = color
        self.clamped = clamped


class PlotAxis(Widget):
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
        self.no_gridlines = no_gridlines
        self.no_tick_marks = no_tick_marks
        self.no_tick_labels = no_tick_labels
        self.log_scale = log_scale
        self.invert = invert
        self.lock_min = lock_min
        self.lock_max = lock_max
        self.time = time


class PlotLegend(Widget):
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
        self.location = location
        self.horizontal = horizontal
        self.outside = outside


class ScatterSeries(Widget):
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


class ShadeSeries(Widget):
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
        self.y2 = y2


class SimplePlot(Widget):
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
        self.default_value = default_value
        self.overlay = overlay
        self.histogram = histogram
        self.autosize = autosize
        self.min_scale = min_scale
        self.max_scale = max_scale


class StairSeries(Widget):
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


class StemSeries(Widget):
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


class TextPoint(Widget):
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
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.vertical = vertical


class VlineSeries(Widget):
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
            **kwargs,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.user_data = user_data
