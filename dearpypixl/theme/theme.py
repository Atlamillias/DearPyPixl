from typing import Any
from dearpygui import dearpygui
from dearpygui.dearpygui import add_theme, bind_item_theme
from .._internal.item import ItemT, LinkedItem, ItemData
from .._internal.comtypes import RGBA, RGBA, X, XY
from .element import (
    ThemeElement,
    ThemeElementType,
    ItemState,
    TElementProxy,
    _BoundTElement,
)

__all__ = [
    "Theme",
]


class ThemeItem(LinkedItem):
    """Changes the appearance of items.

    Items will visually reflect any element (of value) parented by a theme.
    This reflection is propegated to an item's children. Elements of the
    "nearest" theme are reflected over ones that are "further away". For
    example; an element of a theme bound directly to an item has priority
    over the same element propegated down from the item's parent's theme,
    while elements of the application-level theme have the least priority.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTheme, "mvTheme"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvThemeComponent,),
        command=add_theme,
        internal_only=True,
    )

    _bound_elements: dict[str, tuple] = {}  # ThemeElement.bind(...) in subclass body
    _bind = bind_item_theme  # ABC

    CATEGORY = True

    def __init_subclass__(cls):
        super().__init_subclass__()
        # Copy over bound element attributes and data from the parent class,
        # but ignore them if the new class includes the attribute in its
        # definition. Then, include any bound elements defined on just this
        # class (NOTE: Exact same implementation that is used when registering
        # managed attributes in `ItemType.__init_subclass__`).
        cls_members = {*getattr(cls, "__dict__", ()), *getattr(cls, "__slots__", ())}
        cls._bound_elements = {k:v for k,v in cls._bound_elements.items()
                               if k not in cls_members}
        for attr in cls_members:
            value = getattr(cls, attr)
            if not isinstance(value, _BoundTElement):
                # Attribute was re-defined as a non-`_BoundTElement`, so remove
                # any existing entry.
                cls._bound_elements.pop(attr, None)
                continue
            cls._bound_elements[attr] = value
        # Bind a descriptor instance to each attribute in place of the data
        # tuple.
        for attr in cls._bound_elements:
            fget = lambda self, _name=attr: self._bound_elements[_name]
            fset = lambda self, value, _name=attr: self._bound_elements[_name].set_value(value)
            elem_prop = property(fget, fset)
            setattr(cls, attr, elem_prop)
            elem_prop.__set_name__(cls, attr)

    def __init__(
        self,
        label: str = None,
        *,
        item_type         : int | ItemT      = None,
        item_state        : bool | ItemState = None,
        user_data         : Any              = None,
        use_internal_label: bool             = True,
        **kwargs
    ):
        """Args:
            * label (str, optional): Display name for the item. Defaults to None.

            The following are optional, keyword-only arguments:

            * item_type (int | ItemT): All bound theme elements will use this value instead
            of their individual pre-assigned value for <item_type>. Defaults to None.

            * item_state (bool | ItemState): All bound theme elements will use this value
            instead of their individual pre-assigned value for <item_state>. Defaults to None.

            * user_data (Any): Passed as the third positional argument to related callbacks.
            Defaults to None.
            for callbacks. Unused otherwise. Default is None.

            * use_internal_label (bool): If True, `##{self.tag}` will be appended to the
            item's label (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.
        """
        super().__init__(label=label, user_data=user_data, use_internal_label=use_internal_label, **kwargs)
        cls_bound_elements = type(self)._bound_elements
        self._bound_elements = dict.fromkeys(cls_bound_elements)  # != cls._bound_elements
        # Instantiate all bound theme elements so the descriptors work
        # properly.
        for attr in self._bound_elements:
            te_cls, target, value, _item_type, _item_state = cls_bound_elements[attr]
            # Use the user settings if included.
            item_type  = _item_type if item_type is None else item_type
            item_state = _item_state if item_state is None else item_state
            self._bound_elements[attr] = te_cls(
                target=target,
                value=value,
                item_type=item_type,
                item_state=item_state,
                parent=self,
            )


class Theme(ThemeItem):
    border                       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Border)
    border_shadow                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.BorderShadow)
    button                       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Button)
    button_active                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ButtonActive)
    button_hovered               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ButtonHovered)
    check_mark                   : RGBA | RGBA = ThemeElement.bind(ThemeElementType.CheckMark)
    child_bg                     : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ChildBg)
    docking_empty_bg             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.DockingEmptyBg)
    docking_preview              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.DockingPreview)
    drag_drop_target             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.DragDropTarget)
    frame_bg                     : RGBA | RGBA = ThemeElement.bind(ThemeElementType.FrameBg)
    frame_bg_active              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.FrameBgActive)
    frame_bg_hovered             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.FrameBgHovered)
    header                       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Header)
    header_active                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.HeaderActive)
    header_hovered               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.HeaderHovered)
    menu_bar_bg                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.MenuBarBg)
    modal_window_dim_bg          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ModalWindowDimBg)
    nav_highlight                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NavHighlight)
    nav_windowing_dim_bg         : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NavWindowingDimBg)
    nav_windowing_highlight      : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NavWindowingHighlight)
    plot_histogram               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotHistogram)
    plot_histogram_hovered       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotHistogramHovered)
    plot_lines                   : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLines)
    plot_lines_hovered           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLinesHovered)
    popup_bg                     : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PopupBg)
    resize_grip                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ResizeGrip)
    resize_grip_active           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ResizeGripActive)
    resize_grip_hovered          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ResizeGripHovered)
    scrollbar_bg                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ScrollbarBg)
    scrollbar_grab               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ScrollbarGrab)
    scrollbar_grab_active        : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ScrollbarGrabActive)
    scrollbar_grab_hovered       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.ScrollbarGrabHovered)
    separator                    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Separator)
    separator_active             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.SeparatorActive)
    separator_hovered            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.SeparatorHovered)
    slider_grab                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.SliderGrab)
    slider_grab_active           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.SliderGrabActive)
    tab                          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Tab)
    tab_active                   : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TabActive)
    tab_hovered                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TabHovered)
    tab_unfocused                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TabUnfocused)
    tab_unfocused_active         : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TabUnfocusedActive)
    table_border_light           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TableBorderLight)
    table_border_strong          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TableBorderStrong)
    table_header_bg              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TableHeaderBg)
    table_row_bg                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TableRowBg)
    table_row_bg_alt             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TableRowBgAlt)
    text                         : RGBA | RGBA = ThemeElement.bind(ThemeElementType.Text)
    text_disabled                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TextDisabled)
    text_selected_bg             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TextSelectedBg)
    title_bg                     : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TitleBg)
    title_bg_active              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TitleBgActive)
    title_bg_collapsed           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.TitleBgCollapsed)
    window_bg                    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.WindowBg)

    node_bg                      : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeBackground)
    node_bg_hovered              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeBackgroundHovered)
    node_bg_selected             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeBackgroundSelected)
    node_box_selector            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeBoxSelector)
    node_box_selector_outline    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeBoxSelectorOutline)
    node_grid_bg                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeGridBackground)
    node_grid_line               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeGridLine)
    node_grid_line_primary       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeGridLinePrimary)
    node_link                    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeLink)
    node_link_hovered            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeLinkHovered)
    node_link_selected           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeLinkSelected)
    node_outline                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeOutline)
    node_minimap_bg              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapBackground)
    node_minimap_bg_hovered      : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapBackgroundHovered)
    node_minimap_outline         : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapOutline)
    node_minimap_outline_hovered : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapOutlineHovered)
    node_minimap_node_bg         : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapNodeBackground)
    node_minimap_node_bg_hovered : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapNodeBackgroundHovered)
    node_minimap_node_bg_selected: RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapNodeBackgroundSelected)
    node_minimap_node_outline    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapNodeOutline)
    node_minimap_link            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapLink)
    node_minimap_link_selected   : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapLinkSelected)
    node_minimap_canvas          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapCanvas)
    node_minimap_canvas_outline  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeMiniMapCanvasOutline)
    node_pin                     : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodePin)
    node_pin_hovered             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodePinHovered)
    node_title_bar               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeTitleBar)
    node_title_bar_hovered       : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeTitleBarHovered)
    node_title_bar_selected      : RGBA | RGBA = ThemeElement.bind(ThemeElementType.NodeTitleBarSelected)

    plot_bg                      : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotBg)
    plot_border                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotBorder)
    plot_crosshairs              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotCrosshairs)
    plot_error_bar               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotErrorBar)
    plot_fill                    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotFill)
    plot_frame_bg                : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotFrameBg)
    plot_inlay_text              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotInlayText)
    plot_legend_bg               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLegendBg)
    plot_legend_border           : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLegendBorder)
    plot_legend_text             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLegendText)
    plot_line                    : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotLine)
    plot_marker_fill             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotMarkerFill)
    plot_marker_outline          : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotMarkerOutline)
    plot_query                   : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotQuery)
    plot_selection               : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotSelection)
    plot_title_text              : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotTitleText)
    plot_x_axis                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotXAxis)
    plot_x_axis_grid             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotXAxisGrid)
    plot_y_axis                  : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxis)
    plot_y_axis2                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxis2)
    plot_y_axis3                 : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxis3)
    plot_y_axis_grid             : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxisGrid)
    plot_y_axis_grid2            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxisGrid2)
    plot_y_axis_grid3            : RGBA | RGBA = ThemeElement.bind(ThemeElementType.PlotYAxisGrid3)


    alpha                           : X  = ThemeElement.bind(ThemeElementType.Alpha)
    child_border_size               : X  = ThemeElement.bind(ThemeElementType.ChildBorderSize)
    child_rounding                  : X  = ThemeElement.bind(ThemeElementType.ChildRounding)
    frame_border_size               : X  = ThemeElement.bind(ThemeElementType.FrameBorderSize)
    frame_rounding                  : X  = ThemeElement.bind(ThemeElementType.FrameRounding)
    grab_min_size                   : X  = ThemeElement.bind(ThemeElementType.GrabMinSize)
    grab_rounding                   : X  = ThemeElement.bind(ThemeElementType.GrabRounding)
    indent_spacing                  : X  = ThemeElement.bind(ThemeElementType.IndentSpacing)
    popup_border_size               : X  = ThemeElement.bind(ThemeElementType.PopupBorderSize)
    popup_rounding                  : X  = ThemeElement.bind(ThemeElementType.PopupRounding)
    scrollbar_rounding              : X  = ThemeElement.bind(ThemeElementType.ScrollbarRounding)
    scrollbar_size                  : X  = ThemeElement.bind(ThemeElementType.ScrollbarSize)
    tab_rounding                    : X  = ThemeElement.bind(ThemeElementType.TabRounding)
    window_border_size              : X  = ThemeElement.bind(ThemeElementType.WindowBorderSize)
    window_rounding                 : X  = ThemeElement.bind(ThemeElementType.WindowRounding)
    button_text_align               : XY = ThemeElement.bind(ThemeElementType.ButtonTextAlign)
    cell_padding                    : XY = ThemeElement.bind(ThemeElementType.CellPadding)
    frame_padding                   : XY = ThemeElement.bind(ThemeElementType.FramePadding)
    item_inner_spacing              : XY = ThemeElement.bind(ThemeElementType.ItemInnerSpacing)
    item_spacing                    : XY = ThemeElement.bind(ThemeElementType.ItemSpacing)
    selectable_text_align           : XY = ThemeElement.bind(ThemeElementType.SelectableTextAlign)
    window_min_size                 : XY = ThemeElement.bind(ThemeElementType.WindowMinSize)
    window_padding                  : XY = ThemeElement.bind(ThemeElementType.WindowPadding)
    window_title_align              : XY = ThemeElement.bind(ThemeElementType.WindowTitleAlign)

    node_border_thickness           : X  = ThemeElement.bind(ThemeElementType.NodeBorderThickness)
    node_corner_rounding            : X  = ThemeElement.bind(ThemeElementType.NodeCornerRounding)
    node_grid_spacing               : X  = ThemeElement.bind(ThemeElementType.NodeGridSpacing)
    node_link_hover_distance        : X  = ThemeElement.bind(ThemeElementType.NodeLinkHoverDistance)
    node_link_ln_segments_per_length: X  = ThemeElement.bind(ThemeElementType.NodeLinkLineSegmentsPerLength)
    node_link_thickness             : X  = ThemeElement.bind(ThemeElementType.NodeLinkThickness)
    node_padding                    : X  = ThemeElement.bind(ThemeElementType.NodePadding)
    node_pin_circle_radius          : X  = ThemeElement.bind(ThemeElementType.NodePinCircleRadius)
    node_pin_hover_radius           : X  = ThemeElement.bind(ThemeElementType.NodePinHoverRadius)
    node_pin_line_thickness         : X  = ThemeElement.bind(ThemeElementType.NodeLinkThickness)
    node_pin_offset                 : X  = ThemeElement.bind(ThemeElementType.NodePinOffset)
    node_pin_quad_side_length       : X  = ThemeElement.bind(ThemeElementType.NodePinQuadSideLength)
    node_pin_tri_side_length        : X  = ThemeElement.bind(ThemeElementType.NodePinTriangleSideLength)
    node_minimap_padding            : XY = ThemeElement.bind(ThemeElementType.NodeMiniMapPadding)
    node_minimap_offset             : XY = ThemeElement.bind(ThemeElementType.NodeMiniMapOffset)

    plot_border_size                : X  = ThemeElement.bind(ThemeElementType.PlotPlotBorderSize)
    plot_digital_bit_gap            : X  = ThemeElement.bind(ThemeElementType.PlotDigitalBitGap)
    plot_digital_bit_height         : X  = ThemeElement.bind(ThemeElementType.PlotDigitalBitHeight)
    plot_error_bar_weight           : X  = ThemeElement.bind(ThemeElementType.PlotErrorBarWeight)
    plot_fill_alpha                 : X  = ThemeElement.bind(ThemeElementType.PlotFillAlpha)
    plot_line_weight                : X  = ThemeElement.bind(ThemeElementType.PlotLineWeight)
    plot_marker                     : X  = ThemeElement.bind(ThemeElementType.PlotMarker)
    plot_marker_size                : X  = ThemeElement.bind(ThemeElementType.PlotMarkerSize)
    plot_marker_weight              : X  = ThemeElement.bind(ThemeElementType.PlotMarkerWeight)
    plot_minor_alpha                : X  = ThemeElement.bind(ThemeElementType.PlotMinorAlpha)
    plot_annotation_padding         : XY = ThemeElement.bind(ThemeElementType.PlotAnnotationPadding)
    plot_default_size               : XY = ThemeElement.bind(ThemeElementType.PlotDefaultSize)
    plot_error_bar_size             : XY = ThemeElement.bind(ThemeElementType.PlotErrorBarSize)
    plot_fit_padding                : XY = ThemeElement.bind(ThemeElementType.PlotFitPadding)
    plot_label_padding              : XY = ThemeElement.bind(ThemeElementType.PlotLabelPadding)
    plot_legend_inner_padding       : XY = ThemeElement.bind(ThemeElementType.PlotLegendInnerPadding)
    plot_legend_padding             : XY = ThemeElement.bind(ThemeElementType.PlotLegendPadding)
    plot_legend_spacing             : XY = ThemeElement.bind(ThemeElementType.PlotLegendSpacing)
    plot_major_grid_size            : XY = ThemeElement.bind(ThemeElementType.PlotMajorGridSize)
    plot_major_tick_len             : XY = ThemeElement.bind(ThemeElementType.PlotMajorTickLen)
    plot_major_tick_size            : XY = ThemeElement.bind(ThemeElementType.PlotMajorTickSize)
    plot_min_size                   : XY = ThemeElement.bind(ThemeElementType.PlotMinSize)
    plot_minor_grid_size            : XY = ThemeElement.bind(ThemeElementType.PlotMinorGridSize)
    plot_minor_tick_len             : XY = ThemeElement.bind(ThemeElementType.PlotMinorTickLen)
    plot_minor_tick_size            : XY = ThemeElement.bind(ThemeElementType.PlotMinorTickSize)
    plot_mouse_pos_padding          : XY = ThemeElement.bind(ThemeElementType.PlotMousePosPadding)
    plot_padding                    : XY = ThemeElement.bind(ThemeElementType.PlotPadding)


