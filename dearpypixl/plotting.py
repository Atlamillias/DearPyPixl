from typing import Callable, Any, Sequence
from dearpygui import dearpygui
from dearpypixl.itemtypes import *


__all__ = [
    "Plot",
    "PlotLegend",
    "PlotAxis",
    "PlotAxisX",
    "PlotAxisY",
    "DragPoint",
    "DragLine",
    "Annotation",
    "SubPlots",
    "SimplePlot",
    "LineSeries",
    "BarSeries",
    "ScatterSeries",
    "AreaSeries",
    "StemSeries",
    "LabelSeries",
    "PieSeries",
    "ShadeSeries",
    "ErrorSeries",
    "HeatSeries",
    "ImageSeries",
    "StairSeries",
    "CandleSeries",
    "VLineSeries",
    "HistogramSeries",
    "HistogramSeries2D",
]


class Plot(WidgetItem):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.

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
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * no_title (bool, optional):
            * no_menus (bool, optional):
            * no_box_select (bool, optional):
            * no_mouse_pos (bool, optional):
            * no_highlight (bool, optional):
            * no_child (bool, optional):
            * query (bool, optional):
            * crosshairs (bool, optional):
            * anti_aliased (bool, optional):
            * equal_aspects (bool, optional):
            * pan_button (int, optional): enables panning when held
            * pan_mod (int, optional): optional modifier that must be held for panning
            * fit_button (int, optional): fits visible data when double clicked
            * context_menu_button (int, optional): opens plot context menu (if enabled) when clicked
            * box_select_button (int, optional): begins box selection when pressed and confirms selection when released
            * box_select_mod (int, optional): begins box selection when pressed and confirms selection when released
            * box_select_cancel_button (int, optional): cancels active box selection when pressed
            * query_button (int, optional): begins query selection when pressed and end query selection when released
            * query_mod (int, optional): optional modifier that must be held for query selection
            * query_toggle_mod (int, optional): when held, active box selections turn into queries
            * horizontal_mod (int, optional): expands active box selection/query horizontally to plot edge when held
            * vertical_mod (int, optional): expands active box selection/query vertically to plot edge when held
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvPlot, "mvPlot"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvPlotLegend, dearpygui.mvPlotAxis, dearpygui.mvDragPoint, dearpygui.mvDragLine, dearpygui.mvAnnotation, dearpygui.mvDrawLine, dearpygui.mvDrawArrow, dearpygui.mvDrawTriangle, dearpygui.mvDrawCircle, dearpygui.mvDrawEllipse, dearpygui.mvDrawBezierCubic, dearpygui.mvDrawBezierQuadratic, dearpygui.mvDrawQuad, dearpygui.mvDrawRect, dearpygui.mvDrawText, dearpygui.mvDrawPolygon, dearpygui.mvDrawPolyline, dearpygui.mvDrawImage, dearpygui.mvDrawLayer, dearpygui.mvActivatedHandler, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvDeactivatedAfterEditHandler, dearpygui.mvDeactivatedHandler, dearpygui.mvEditedHandler, dearpygui.mvFocusHandler, dearpygui.mvHoverHandler, dearpygui.mvResizeHandler, dearpygui.mvToggledOpenHandler, dearpygui.mvVisibleHandler, dearpygui.mvDragPayload,dearpygui.mvDrawNode),
        commands=('is_plot_queried', 'get_plot_query_area'),
        constants=('mvPlot', 'mvPlotMarker_None', 'mvPlotMarker_Circle', 'mvPlotMarker_Square', 'mvPlotMarker_Diamond', 'mvPlotMarker_Up', 'mvPlotMarker_Down', 'mvPlotMarker_Left', 'mvPlotMarker_Right', 'mvPlotMarker_Cross', 'mvPlotMarker_Plus', 'mvPlotMarker_Asterisk'),
        command=dearpygui.add_plot,
    )

    width                    : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height                   : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent                   : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type             : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback                 : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback            : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback            : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                      : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key               : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search             : bool                        = __dearpypixl__.set_information(None, None)
    tracked                  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset             : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_title                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_menus                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_box_select            : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_mouse_pos             : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_highlight             : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_child                 : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    query                    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    crosshairs               : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    anti_aliased             : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    equal_aspects            : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pan_button               : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pan_mod                  : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fit_button               : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    context_menu_button      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    box_select_button        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    box_select_mod           : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    box_select_cancel_button : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    query_button             : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    query_mod                : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    query_toggle_mod         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal_mod           : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    vertical_mod             : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label                    : str                         = None,
        user_data                : Any                         = None,
        use_internal_label       : bool                        = True,
        width                    : int                         = 0,
        height                   : int                         = 0,
        indent                   : int                         = -1,
        parent                   : Item | int                  = 0,
        before                   : Item | int                  = 0,
        payload_type             : str                         = '$$DPG_PAYLOAD',
        callback                 : Callable                    = None,
        drag_callback            : Callable                    = None,
        drop_callback            : Callable                    = None,
        show                     : bool                        = True,
        pos                      : list[int] | tuple[int, ...] = [],
        filter_key               : str                         = '',
        delay_search             : bool                        = False,
        tracked                  : bool                        = False,
        track_offset             : float                       = 0.5,
        no_title                 : bool                        = False,
        no_menus                 : bool                        = False,
        no_box_select            : bool                        = False,
        no_mouse_pos             : bool                        = False,
        no_highlight             : bool                        = False,
        no_child                 : bool                        = False,
        query                    : bool                        = False,
        crosshairs               : bool                        = False,
        anti_aliased             : bool                        = False,
        equal_aspects            : bool                        = False,
        pan_button               : int                         = 0,
        pan_mod                  : int                         = -1,
        fit_button               : int                         = 0,
        context_menu_button      : int                         = 1,
        box_select_button        : int                         = 1,
        box_select_mod           : int                         = -1,
        box_select_cancel_button : int                         = 0,
        query_button             : int                         = 2,
        query_mod                : int                         = -1,
        query_toggle_mod         : int                         = 17,
        horizontal_mod           : int                         = 18,
        vertical_mod             : int                         = 16,
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


class PlotLegend(WidgetItem):
    """Adds a plot legend to a plot.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * location (int, optional): location, mvPlot_Location_*
            * horizontal (bool, optional):
            * outside (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvPlotLegend, "mvPlotLegend"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvPlot,dearpygui.mvSubPlots),
        able_children=(),
        constants=('mvPlotLegend', 'mvPlot_Location_Center', 'mvPlot_Location_North', 'mvPlot_Location_South', 'mvPlot_Location_West', 'mvPlot_Location_East', 'mvPlot_Location_NorthWest', 'mvPlot_Location_NorthEast', 'mvPlot_Location_SouthWest', 'mvPlot_Location_SouthEast'),
        command=dearpygui.add_plot_legend,
    )

    payload_type  : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    location      : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal    : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    outside       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        parent             : int | str = 0,
        payload_type       : str       = '$$DPG_PAYLOAD',
        drop_callback      : Callable  = None,
        show               : bool      = True,
        location           : int       = 5,
        horizontal         : bool      = False,
        outside            : bool      = False,
        **kwargs
    ) -> None:
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


class PlotAxis(WidgetItem):
    """Adds an axis to a plot.

        Args:
            * axis (int):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * no_gridlines (bool, optional):
            * no_tick_marks (bool, optional):
            * no_tick_labels (bool, optional):
            * log_scale (bool, optional):
            * invert (bool, optional):
            * lock_min (bool, optional):
            * lock_max (bool, optional):
            * time (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvPlotAxis, "mvPlotAxis"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvPlot),
        able_children=(),
        commands=('reset_axis_ticks', 'set_axis_ticks', 'set_axis_limits', 'set_axis_limits_auto', 'get_axis_limits', 'fit_axis_data'),
        constants=('mvPlotAxis', 'mvXAxis', 'mvYAxis'),
        command=dearpygui.add_plot_axis,
    )

    axis           : int      = __dearpypixl__.set_configuration(None, "set_item_config")
    payload_type   : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback  : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show           : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_gridlines   : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tick_marks  : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tick_labels : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    log_scale      : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    invert         : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    lock_min       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    lock_max       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    time           : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        axis              : int,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Item | int      = 0,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None,
        show              : bool            = True,
        no_gridlines      : bool            = False,
        no_tick_marks     : bool            = False,
        no_tick_labels    : bool            = False,
        log_scale         : bool            = False,
        invert            : bool            = False,
        lock_min          : bool            = False,
        lock_max          : bool            = False,
        time              : bool            = False,
        **kwargs
    ) -> None:
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

    @property
    def axis_limits(self) -> tuple[float, float]:
        return dearpygui.get_axis_limits(self._tag)
    @axis_limits.setter
    def axis_limits(self, value: tuple[float, float]) -> None:
        self.set_limits(*value)

    def get_limits(self) -> tuple[float, float]:
        """Return the current axis limits (ymin, ymax).
        """
        return dearpygui.get_axis_limits(self._tag)

    def set_limits(self, ymin: float | int = None, ymax: float | int = None, **kwargs) -> None:
        """Sets zoom and pan limits for the axis (ymin, ymax).

        Args:
            * ymin (float | int, optional):
            * ymax (float | int, optional):
        """
        try:
            dearpygui.set_axis_limits(self.tag, ymin, ymax, **kwargs)
        except SystemError:
            self._err_if_existential_crisis()
            raise

    def set_limits_fit_data(self, **kwargs) -> None:
        """Set the axis limits (ymin, ymax) to fit the largest set of data parented by the axis.
        """
        try:
            dearpygui.fit_axis_data()
        except SystemError:
            self._err_if_existential_crisis()
            raise

    def set_ticks(self, label_pairs: tuple[tuple[str, float | int], ...], **kwargs) -> None:
        """Replace the default axis ticks with <label_pairs>.

        Args:
            * label_pairs (tuple[tuple[str, float | int], ...]): A sequence of 2-item tuples.
            The first item of each inner tuple is the tick label, while the second is the value
            at which to set the tick.
        """
        return dearpygui.set_axis_ticks(self.tag, label_pairs)

    def reset_limits(self, **kwargs) -> None:
        """Remove any manually-set axis limits, and apply the default limits.
        """
        return dearpygui.set_axis_limits_auto(self.tag)

    def reset_ticks(self, **kwargs) -> None:
        """Remove any manually-set axis ticks, and apply the default ticks.
        """
        return dearpygui.reset_axis_ticks(self.tag)


class PlotAxisX(PlotAxis):  # NOTE: non built-in
    """Adds an X axis to a plot.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * no_gridlines (bool, optional):
            * no_tick_marks (bool, optional):
            * no_tick_labels (bool, optional):
            * log_scale (bool, optional):
            * invert (bool, optional):
            * lock_min (bool, optional):
            * lock_max (bool, optional):
            * time (bool, optional):
    """
    def __init__(
        self,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : Item | int      = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        no_gridlines      : bool            = False          ,
        no_tick_marks     : bool            = False          ,
        no_tick_labels    : bool            = False          ,
        log_scale         : bool            = False          ,
        invert            : bool            = False          ,
        lock_min          : bool            = False          ,
        lock_max          : bool            = False          ,
        time              : bool            = False          ,
        **kwargs
    ) -> None:
        super().__init__(
            axis=dearpygui.mvXAxis,
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


class PlotAxisY(PlotAxis):  # NOTE: non built-in
    """Adds an Y axis to a plot.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * no_gridlines (bool, optional):
            * no_tick_marks (bool, optional):
            * no_tick_labels (bool, optional):
            * log_scale (bool, optional):
            * invert (bool, optional):
            * lock_min (bool, optional):
            * lock_max (bool, optional):
            * time (bool, optional):
    """
    def __init__(
        self,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : Item | int      = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        no_gridlines      : bool            = False          ,
        no_tick_marks     : bool            = False          ,
        no_tick_labels    : bool            = False          ,
        log_scale         : bool            = False          ,
        invert            : bool            = False          ,
        lock_min          : bool            = False          ,
        lock_max          : bool            = False          ,
        time              : bool            = False          ,
        **kwargs
    ) -> None:
        super().__init__(
            axis=dearpygui.mvYAxis,
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


class DragPoint(WidgetItem):
    """Adds a drag point to a plot.

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
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * default_value (Any, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * show_label (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDragPoint, "mvDragPoint"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvPlot),
        able_children=(),
        command=dearpygui.add_drag_point,
    )

    source            : int | str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback          : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show              : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value     : Any                               = __dearpypixl__.set_information(None, None)
    color             : list[int] | tuple[int, ...]       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness         : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show_label        : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value             : Any                               = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        source             : Item | int                  = 0,
        callback           : Callable                    = None,
        show               : bool                        = True,
        default_value      : Any                         = (0.0, 0.0),
        color              : list[int] | tuple[int, ...] = (0, 0, 0, -255),
        thickness          : float                       = 1.0,
        show_label         : bool                        = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            **kwargs,
        )


class DragLine(WidgetItem):
    """Adds a drag line to a plot.

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
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * default_value (Any, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * show_label (bool, optional):
            * vertical (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDragLine, "mvDragLine"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvPlot),
        able_children=(),
        command=dearpygui.add_drag_line,
    )

    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : Any                         = __dearpypixl__.set_information(None, None)
    color         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show_label    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    vertical      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : Any                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        source             : Item | int                  = 0,
        callback           : Callable                    = None,
        show               : bool                        = True,
        default_value      : Any                         = 0.0,
        color              : list[int] | tuple[int, ...] = (0, 0, 0, -255),
        thickness          : float                       = 1.0,
        show_label         : bool                        = True,
        vertical           : bool                        = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            vertical=vertical,
            **kwargs,
        )


class Annotation(WidgetItem):
    """Adds an annotation to a plot.

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
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * default_value (Any, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * offset (list[float] | tuple[float, ...], optional):
            * color (list[int] | tuple[int, ...], optional):
            * clamped (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvAnnotation, "mvAnnotation"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvPlot),
        able_children=(),
        command=dearpygui.add_plot_annotation,
    )

    source        : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : Any                             = __dearpypixl__.set_information(None, None)
    offset        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color         : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    clamped       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : Any                             = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                             = None,
        user_data          : Any                             = None,
        use_internal_label : bool                            = True,
        parent             : Item | int                      = 0,
        before             : Item | int                      = 0,
        source             : Item | int                      = 0,
        show               : bool                            = True,
        default_value      : Any                             = (0.0, 0.0),
        offset             : list[float] | tuple[float, ...] = (0.0, 0.0),
        color              : list[int] | tuple[int, ...]     = (0, 0, 0, -255),
        clamped            : bool                            = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            default_value=default_value,
            offset=offset,
            color=color,
            clamped=clamped,
            **kwargs,
        )


class SubPlots(WidgetItem):
    """Adds a collection of plots.

        Args:
            * rows (int):
            * columns (int):
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
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * row_ratios (list[float] | tuple[float, ...], optional):
            * column_ratios (list[float] | tuple[float, ...], optional):
            * no_title (bool, optional):
            * no_menus (bool, optional): the user will not be able to open context menus with right-click
            * no_resize (bool, optional): resize splitters between subplot cells will be not be provided
            * no_align (bool, optional): subplot edges will not be aligned vertically or horizontally
            * link_rows (bool, optional): link the y-axis limits of all plots in each row (does not apply auxiliary y-axes)
            * link_columns (bool, optional): link the x-axis limits of all plots in each column
            * link_all_x (bool, optional): link the x-axis limits in every plot in the subplot
            * link_all_y (bool, optional): link the y-axis limits in every plot in the subplot (does not apply to auxiliary y-axes)
            * column_major (bool, optional): subplots are added in column major order instead of the default row major order
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSubPlots, "mvSubPlots"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvPlot,dearpygui.mvPlotLegend),
        command=dearpygui.add_subplots,
    )

    rows          : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    columns       : int                             = __dearpypixl__.set_configuration('get_item_config', "set_item_config", target='cols')
    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key    : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search  : bool                            = __dearpypixl__.set_information(None, None)
    tracked       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    row_ratios    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    column_ratios : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_title      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_menus      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_resize     : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_align      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    link_rows     : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    link_columns  : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    link_all_x    : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    link_all_y    : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    column_major  : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        rows              : int,
        columns           : int,
        label             : str                                   = None,
        user_data         : Any                                   = None,
        use_internal_label: bool                                  = True,
        width             : int                                   = 0,
        height            : int                                   = 0,
        indent            : int                                   = -1,
        parent            : Item | int                            = 0,
        before            : Item | int                            = 0,
        callback          : Callable                              = None,
        show              : bool                                  = True,
        pos               : list[int] | tuple[int, ...]           = [],
        filter_key        : str                                   = '',
        delay_search      : bool                                  = False,
        tracked           : bool                                  = False,
        track_offset      : float                                 = 0.5,
        row_ratios        : list[float] | tuple[float, ...] = [],
        column_ratios     : list[float] | tuple[float, ...] = [],
        no_title          : bool                                  = False,
        no_menus          : bool                                  = False,
        no_resize         : bool                                  = False,
        no_align          : bool                                  = False,
        link_rows         : bool                                  = False,
        link_columns      : bool                                  = False,
        link_all_x        : bool                                  = False,
        link_all_y        : bool                                  = False,
        column_major      : bool                                  = False,
        **kwargs
    ) -> None:
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


class SimplePlot(WidgetItem):
    """Adds a simple plot for visualization of a 1 dimensional set of values.

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
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (list[float] | tuple[float, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * overlay (str, optional): overlays text (similar to a plot title)
            * histogram (bool, optional):
            * autosize (bool, optional):
            * min_scale (float, optional):
            * max_scale (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSimplePlot, "mvSimplePlot"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_simple_plot,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key    : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = __dearpypixl__.set_information(None, None)
    overlay       : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    histogram     : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    autosize      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_scale     : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_scale     : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                             = None,
        user_data          : Any                             = None,
        use_internal_label : bool                            = True,
        width              : int                             = 0,
        height             : int                             = 0,
        indent             : int                             = -1,
        parent             : Item | int                      = 0,
        before             : Item | int                      = 0,
        source             : Item | int                      = 0,
        payload_type       : str                             = '$$DPG_PAYLOAD',
        drag_callback      : Callable                        = None,
        drop_callback      : Callable                        = None,
        show               : bool                            = True,
        filter_key         : str                             = '',
        tracked            : bool                            = False,
        track_offset       : float                           = 0.5,
        default_value      : list[float] | tuple[float, ...] = (),
        overlay            : str                             = '',
        histogram          : bool                            = False,
        autosize           : bool                            = True,
        min_scale          : float                           = 0.0,
        max_scale          : float                           = 0.0,
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
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            overlay=overlay,
            histogram=histogram,
            autosize=autosize,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )


class SeriesItem(WidgetItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_children=(),
        internal_only=True,
    )

    value : list[list[int], list[int]] = __dearpypixl__.set_configuration("get_item_value" , "set_item_value" )
    source: int | str                  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    # TODO: Make a SequenceValue descriptor and rm copy-pasted code.
    @property
    @__dearpypixl__.as_configuration
    def x(self) -> list[int]:
        return [v[0] for v in self.value]
    @x.setter
    def x(self, value: Sequence[int]) -> None:
        all_values    = self.value
        all_values[0] = value
        self.value    = all_values

    @property
    @__dearpypixl__.as_configuration
    def y(self) -> list[int]:
        return [v[1] for v in self.value]
    @y.setter
    def y(self, value: Sequence[int]) -> None:
        all_values    = self.value
        all_values[1] = value
        self.value    = all_values

    @property
    @__dearpypixl__.as_configuration
    def y1(self) -> list[int]:
        return [v[2] for v in self.value]
    @y1.setter
    def y1(self, value: Sequence[int]) -> None:
        all_values    = self.value
        all_values[2] = value
        self.value    = all_values

    @property
    @__dearpypixl__.as_configuration
    def y2(self) -> list[int]:
        return [v[3] for v in self.value]
    @y2.setter
    def y2(self, value: Sequence[int]) -> None:
        all_values    = self.value
        all_values[3] = value
        self.value    = all_values

    @property
    @__dearpypixl__.as_configuration
    def y3(self) -> list[int]:
        return [v[4] for v in self.value]
    @y3.setter
    def y3(self, value: Sequence[int]) -> None:
        all_values    = self.value
        all_values[4] = value
        self.value    = all_values



class LineSeries(WidgetItem):
    """Adds a line series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvLineSeries, "mvLineSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_line_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y                 : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        **kwargs
    ) -> None:
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


class BarSeries(WidgetItem):
    """Adds a bar series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * weight (float, optional):
            * horizontal (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvBarSeries, "mvBarSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_bar_series,
    )

    x          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source     : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    weight     : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y                 : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        weight            : float                                = 1.0,
        horizontal        : bool                                 = False,
        **kwargs
    ) -> None:
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


class ScatterSeries(WidgetItem):
    """Adds a scatter series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvScatterSeries, "mvScatterSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_scatter_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y                 : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        **kwargs
    ) -> None:
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


class AreaSeries(WidgetItem):
    """Adds an area series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * fill (list[int] | tuple[int, ...], optional):
            * contribute_to_bounds (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvAreaSeries, "mvAreaSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_area_series,
    )

    x                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source               : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill                 : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    contribute_to_bounds : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                   : list[float] | tuple[float, ...],
        y                   : list[float] | tuple[float, ...],
        label               : str                                  = None,
        user_data           : Any                                  = None,
        use_internal_label  : bool                                 = True,
        parent              : Item | int                           = 0,
        before              : Item | int                           = 0,
        source              : Item | int                           = 0,
        show                : bool                                 = True,
        fill                : list[int] | tuple[int, ...]          = (0, 0, 0, -255),
        contribute_to_bounds: bool                                 = True,
        **kwargs
    ) -> None:
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


class StemSeries(WidgetItem):
    """Adds a stem series to a plot.

        Args:
            * x (Any):
            * y (Any):
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
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvStemSeries, "mvStemSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_stem_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y                 : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        indent            : int                                  = -1,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        **kwargs
    ) -> None:
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


class LabelSeries(WidgetItem):
    """Adds a label series to a plot.

        Args:
            * x (float):
            * y (float):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * x_offset (int, optional):
            * y_offset (int, optional):
            * vertical (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvLabelSeries, "mvLabelSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_text_point,
    )

    x        : float     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y        : float     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source   : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show     : bool      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    x_offset : int       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y_offset : int       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    vertical : bool      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : float,
        y                 : float,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Item | int      = 0,
        before            : Item | int      = 0,
        source            : Item | int      = 0,
        show              : bool            = True,
        x_offset          : int             = Ellipsis,
        y_offset          : int             = Ellipsis,
        vertical          : bool            = False,
        **kwargs
    ) -> None:
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


class PieSeries(WidgetItem):
    """Adds an pie series to a plot.

        Args:
            * x (float):
            * y (float):
            * radius (float):
            * values (Any):
            * labels (list[str] | tuple[str, ...]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * format (str, optional):
            * angle (float, optional):
            * normalize (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvPieSeries, "mvPieSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_pie_series,
    )

    x         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    radius    : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    values    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    labels    : list[str] | tuple[str, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source    : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    format    : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    angle     : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    normalize : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : float,
        y                 : float,
        radius            : float,
        values            : list[float] | tuple[float, ...],
        labels            : list[str] | tuple[str, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        format            : str                                  = '%0.2f',
        angle             : float                                = 90.0,
        normalize         : bool                                 = False,
        **kwargs
    ) -> None:
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


class ShadeSeries(WidgetItem):
    """Adds a shade series to a plot.

        Args:
            * x (Any):
            * y1 (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * y2 (Any, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvShadeSeries, "mvShadeSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_shade_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y1     : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y2     : Any                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y1                : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        y2                : Any                                  = [],
        **kwargs
    ) -> None:
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


class ErrorSeries(WidgetItem):
    """Adds an error series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * negative (Any):
            * positive (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * contribute_to_bounds (bool, optional):
            * horizontal (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvErrorSeries, "mvErrorSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_error_series,
    )

    x                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    negative             : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    positive             : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source               : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    contribute_to_bounds : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    horizontal           : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                   : list[float] | tuple[float, ...],
        y                   : list[float] | tuple[float, ...],
        negative            : list[float] | tuple[float, ...],
        positive            : list[float] | tuple[float, ...],
        label               : str                                  = None,
        user_data           : Any                                  = None,
        use_internal_label  : bool                                 = True,
        parent              : Item | int                           = 0,
        before              : Item | int                           = 0,
        source              : Item | int                           = 0,
        show                : bool                                 = True,
        contribute_to_bounds: bool                                 = True,
        horizontal          : bool                                 = False,
        **kwargs
    ) -> None:
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


class HeatSeries(WidgetItem):
    """Adds a heat series to a plot.

        Args:
            * x (Any):
            * rows (int):
            * cols (int):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * scale_min (float, optional): Sets the color scale min. Typically paired with the color scale widget scale_min.
            * scale_max (float, optional): Sets the color scale max. Typically paired with the color scale widget scale_max.
            * bounds_min (Any, optional):
            * bounds_max (Any, optional):
            * format (str, optional):
            * contribute_to_bounds (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvHeatSeries, "mvHeatSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_heat_series,
    )

    x                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    rows                 : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    cols                 : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source               : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    scale_min            : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    scale_max            : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bounds_min           : Any                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bounds_max           : Any                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    format               : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    contribute_to_bounds : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                   : list[float] | tuple[float, ...],
        rows                : int,
        cols                : int,
        label               : str                                  = None,
        user_data           : Any                                  = None,
        use_internal_label  : bool                                 = True,
        parent              : Item | int                           = 0,
        before              : Item | int                           = 0,
        source              : Item | int                           = 0,
        show                : bool                                 = True,
        scale_min           : float                                = 0.0,
        scale_max           : float                                = 1.0,
        bounds_min          : Any                                  = (0.0, 0.0),
        bounds_max          : Any                                  = (1.0, 1.0),
        format              : str                                  = '%0.1f',
        contribute_to_bounds: bool                                 = True,
        **kwargs
    ) -> None:
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


class ImageSeries(WidgetItem):
    """Adds an image series to a plot.

        Args:
            * texture_tag (int | str      ):
            * bounds_min (Any):
            * bounds_max (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * uv_min (list[float] | tuple[float, ...], optional): normalized texture coordinates
            * uv_max (list[float] | tuple[float, ...], optional): normalized texture coordinates
            * tint_color (list[int] | tuple[int, ...], optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvImageSeries, "mvImageSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_image_series,
    )

    texture_tag : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bounds_min  : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bounds_max  : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source      : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show        : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_min      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_max      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tint_color  : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        texture_tag       : int | str,
        bounds_min        : list[float] | tuple[float, ...],
        bounds_max        : list[float] | tuple[float, ...],
        label             : str                                   = None,
        user_data         : Any                                   = None,
        use_internal_label: bool                                  = True,
        parent            : Item | int                            = 0,
        before            : Item | int                            = 0,
        source            : Item | int                            = 0,
        show              : bool                                  = True,
        uv_min            : list[float] | tuple[float, ...] = (0.0, 0.0),
        uv_max            : list[float] | tuple[float, ...] = (1.0, 1.0),
        tint_color        : list[int] | tuple[int, ...]           = (255, 255, 255, 255),
        **kwargs
    ) -> None:
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


class StairSeries(WidgetItem):
    """Adds a stair series to a plot.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvStairSeries, "mvStairSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_stair_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...],
        y                 : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        source            : Item | int                       = 0,
        show              : bool                             = True,
        **kwargs
    ) -> None:
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


class CandleSeries(WidgetItem):
    """Adds a candle series to a plot.

        Args:
            * dates (Any):
            * opens (Any):
            * closes (Any):
            * lows (Any):
            * highs (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * bull_color (list[int] | tuple[int, ...], optional):
            * bear_color (list[int] | tuple[int, ...], optional):
            * weight (int, optional):
            * tooltip (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvCandleSeries, "mvCandleSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_candle_series,
    )

    dates      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    opens      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    closes     : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    lows       : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    highs      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source     : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bull_color : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bear_color : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    weight     : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tooltip    : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        dates             : list[float] | tuple[float, ...],
        opens             : list[float] | tuple[float, ...],
        closes            : list[float] | tuple[float, ...],
        lows              : list[float] | tuple[float, ...],
        highs             : list[float] | tuple[float, ...],
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0,
        before            : Item | int                           = 0,
        source            : Item | int                           = 0,
        show              : bool                                 = True,
        bull_color        : list[int] | tuple[int, ...]          = (0, 255, 113, 255),
        bear_color        : list[int] | tuple[int, ...]          = (218, 13, 79, 255),
        weight            : int                                  = 0.25,
        tooltip           : bool                                 = True,
        **kwargs
    ) -> None:
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


class VLineSeries(WidgetItem):
    """Adds an infinite vertical line series to a plot.

        Args:
            * x (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvVLineSeries, "mvVLineSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_vline_series,
    )

    x      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                 : list[float] | tuple[float, ...]      ,
        label             : str                                  = None,
        user_data         : Any                                  = None,
        use_internal_label: bool                                 = True,
        parent            : Item | int                           = 0   ,
        before            : Item | int                           = 0   ,
        source            : Item | int                           = 0   ,
        show              : bool                                 = True,
        **kwargs
    ) -> None:
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


class HistogramSeries(WidgetItem):
    """Adds a histogram series to a plot.

        Args:
            * x (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * bins (int, optional):
            * bar_scale (float, optional):
            * min_range (float, optional):
            * max_range (float, optional):
            * cumlative (bool, optional):
            * density (bool, optional):
            * outliers (bool, optional):
            * contribute_to_bounds (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvHistogramSeries, "mvHistogramSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        constants=('mvHistogramSeries', 'mvPlotBin_Sqrt', 'mvPlotBin_Sturges', 'mvPlotBin_Rice', 'mvPlotBin_Scott'),
        command=dearpygui.add_histogram_series,
    )

    x                    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source               : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                 : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bins                 : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bar_scale            : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_range            : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_range            : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    cumlative            : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    density              : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    outliers             : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    contribute_to_bounds : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                   : list[float] | tuple[float, ...],
        label               : str                                  = None,
        user_data           : Any                                  = None,
        use_internal_label  : bool                                 = True,
        parent              : Item | int                           = 0,
        before              : Item | int                           = 0,
        source              : Item | int                           = 0,
        show                : bool                                 = True,
        bins                : int                                  = -1,
        bar_scale           : float                                = 1.0,
        min_range           : float                                = 0.0,
        max_range           : float                                = 1.0,
        cumlative           : bool                                 = False,
        density             : bool                                 = False,
        outliers            : bool                                 = True,
        contribute_to_bounds: bool                                 = True,
        **kwargs
    ) -> None:
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


class HistogramSeries2D(WidgetItem):
    """Adds a 2d histogram series.

        Args:
            * x (Any):
            * y (Any):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * xbins (int, optional):
            * ybins (int, optional):
            * xmin_range (float, optional):
            * xmax_range (float, optional):
            * ymin_range (float, optional):
            * ymax_range (float, optional):
            * density (bool, optional):
            * outliers (bool, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mv2dHistogramSeries, "mv2DHistogramSeries"),
        is_container=True,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvPlotAxis,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_2d_histogram_series,
    )

    x          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    y          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source     : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    xbins      : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    ybins      : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    xmin_range : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    xmax_range : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    ymin_range : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    ymax_range : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    density    : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    outliers   : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        x                  : list[float] | tuple[float, ...],
        y                  : list[float] | tuple[float, ...],
        label              : str                              = None,
        user_data          : Any                              = None,
        use_internal_label : bool                             = True,
        parent             : Item | int                       = 0,
        before             : Item | int                       = 0,
        source             : Item | int                       = 0,
        show               : bool                             = True,
        xbins              : int                              = -1,
        ybins              : int                              = -1,
        xmin_range         : float                            = 0.0,
        xmax_range         : float                            = 1.0,
        ymin_range         : float                            = 0.0,
        ymax_range         : float                            = 1.0,
        density            : bool                             = False,
        outliers           : bool                             = True,
        **kwargs
    ) -> None:
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
