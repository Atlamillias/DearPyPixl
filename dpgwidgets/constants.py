from typing import Union, TYPE_CHECKING
from dearpygui import dearpygui as dpg

AppItemType = None
ItemType = None

if TYPE_CHECKING:
    from dpgwidgets.item import Item
    from dpgwidgets.widget import Widget, Container

    AppItemType = Union[Item, Widget, Container]
    ItemType = Union[int, AppItemType]


## Theming ##
COLOR_OPTN = dict(
    border = (dpg.mvThemeCol_Border, dpg.mvThemeCat_Core),
    border_shadow = (dpg.mvThemeCol_BorderShadow, dpg.mvThemeCat_Core),
    button = (dpg.mvThemeCol_Button, dpg.mvThemeCat_Core),
    button_active = (dpg.mvThemeCol_ButtonActive, dpg.mvThemeCat_Core),
    button_hovered = (dpg.mvThemeCol_ButtonHovered, dpg.mvThemeCat_Core),
    check_mark = (dpg.mvThemeCol_CheckMark, dpg.mvThemeCat_Core),
    child_bg = (dpg.mvThemeCol_ChildBg, dpg.mvThemeCat_Core),
    docking_empty_bg = (dpg.mvThemeCol_DockingEmptyBg, dpg.mvThemeCat_Core),
    docking_preview = (dpg.mvThemeCol_DockingPreview, dpg.mvThemeCat_Core),
    drag_drop_target = (dpg.mvThemeCol_DragDropTarget, dpg.mvThemeCat_Core),
    frame_bg = (dpg.mvThemeCol_FrameBg, dpg.mvThemeCat_Core),
    frame_bg_active = (dpg.mvThemeCol_FrameBgActive, dpg.mvThemeCat_Core),
    frame_bg_hovered = (dpg.mvThemeCol_FrameBgHovered, dpg.mvThemeCat_Core),
    header = (dpg.mvThemeCol_Header, dpg.mvThemeCat_Core),
    header_active = (dpg.mvThemeCol_HeaderActive, dpg.mvThemeCat_Core),
    header_hovered = (dpg.mvThemeCol_HeaderHovered, dpg.mvThemeCat_Core),
    menu_bar_bg = (dpg.mvThemeCol_MenuBarBg, dpg.mvThemeCat_Core),
    modal_window_dim_bg = (
        dpg.mvThemeCol_ModalWindowDimBg, dpg.mvThemeCat_Core),
    nav_highlight = (dpg.mvThemeCol_NavHighlight, dpg.mvThemeCat_Core),
    nav_windowing_dim_bg = (
        dpg.mvThemeCol_NavWindowingDimBg, dpg.mvThemeCat_Core),
    nav_windowing_highlight = (
        dpg.mvThemeCol_NavWindowingHighlight, dpg.mvThemeCat_Core),
    plot_histogram = (dpg.mvThemeCol_PlotHistogram, dpg.mvThemeCat_Core),
    plot_histogram_hovered = (
        dpg.mvThemeCol_PlotHistogramHovered, dpg.mvThemeCat_Core),
    plot_lines = (dpg.mvThemeCol_PlotLines, dpg.mvThemeCat_Core),
    plot_lines_hovered = (
        dpg.mvThemeCol_PlotLinesHovered, dpg.mvThemeCat_Core),
    popup_bg = (dpg.mvThemeCol_PopupBg, dpg.mvThemeCat_Core),
    resize_grip = (dpg.mvThemeCol_ResizeGrip, dpg.mvThemeCat_Core),
    resize_grip_active = (
        dpg.mvThemeCol_ResizeGripActive, dpg.mvThemeCat_Core),
    resize_grip_hovered = (
        dpg.mvThemeCol_ResizeGripHovered, dpg.mvThemeCat_Core),
    scrollbar_bg = (dpg.mvThemeCol_ScrollbarBg, dpg.mvThemeCat_Core),
    scrollbar_grab = (dpg.mvThemeCol_ScrollbarGrab, dpg.mvThemeCat_Core),
    scrollbar_grab_active = (
        dpg.mvThemeCol_ScrollbarGrabActive, dpg.mvThemeCat_Core),
    scrollbar_grab_hovered = (
        dpg.mvThemeCol_ScrollbarGrabHovered, dpg.mvThemeCat_Core),
    separator = (dpg.mvThemeCol_Separator, dpg.mvThemeCat_Core),
    separator_active = (dpg.mvThemeCol_SeparatorActive, dpg.mvThemeCat_Core),
    separator_hovered = (dpg.mvThemeCol_SeparatorHovered,
                         dpg.mvThemeCat_Core),
    slider_grab = (dpg.mvThemeCol_SliderGrab, dpg.mvThemeCat_Core),
    slider_grab_active = (
        dpg.mvThemeCol_SliderGrabActive, dpg.mvThemeCat_Core),
    tab = (dpg.mvThemeCol_Tab, dpg.mvThemeCat_Core),
    tab_active = (dpg.mvThemeCol_TabActive, dpg.mvThemeCat_Core),
    tab_hovered = (dpg.mvThemeCol_TabHovered, dpg.mvThemeCat_Core),
    tab_unfocused = (dpg.mvThemeCol_TabUnfocused, dpg.mvThemeCat_Core),
    tab_unfocused_active = (
        dpg.mvThemeCol_TabUnfocusedActive, dpg.mvThemeCat_Core),
    table_border_light = (
        dpg.mvThemeCol_TableBorderLight, dpg.mvThemeCat_Core),
    table_border_strong = (
        dpg.mvThemeCol_TableBorderStrong, dpg.mvThemeCat_Core),
    table_header_bg = (dpg.mvThemeCol_TableHeaderBg, dpg.mvThemeCat_Core),
    table_row_bg = (dpg.mvThemeCol_TableRowBg, dpg.mvThemeCat_Core),
    table_row_bg_alt = (dpg.mvThemeCol_TableRowBgAlt, dpg.mvThemeCat_Core),
    text = (dpg.mvThemeCol_Text, dpg.mvThemeCat_Core),
    text_disabled = (dpg.mvThemeCol_TextDisabled, dpg.mvThemeCat_Core),
    text_selected_bg = (dpg.mvThemeCol_TextSelectedBg, dpg.mvThemeCat_Core),
    title_bg = (dpg.mvThemeCol_TitleBg, dpg.mvThemeCat_Core),
    title_bg_active = (dpg.mvThemeCol_TitleBgActive, dpg.mvThemeCat_Core),
    title_bg_collapsed = (
        dpg.mvThemeCol_TitleBgCollapsed, dpg.mvThemeCat_Core),
    window_bg = (dpg.mvThemeCol_WindowBg, dpg.mvThemeCat_Core),
    plot_crosshairs = (dpg.mvPlotCol_Crosshairs, dpg.mvThemeCat_Plots),
    plot_error_bar = (dpg.mvPlotCol_ErrorBar, dpg.mvThemeCat_Plots),
    plot_fill = (dpg.mvPlotCol_Fill, dpg.mvThemeCat_Plots),
    plot_frame_bg = (dpg.mvPlotCol_FrameBg, dpg.mvThemeCat_Plots),
    plot_inlay_text = (dpg.mvPlotCol_InlayText, dpg.mvThemeCat_Plots),
    plot_legend_bg = (dpg.mvPlotCol_LegendBg, dpg.mvThemeCat_Plots),
    plot_legend_border = (dpg.mvPlotCol_LegendBorder, dpg.mvThemeCat_Plots),
    plot_legend_text = (dpg.mvPlotCol_LegendText, dpg.mvThemeCat_Plots),
    plot_line = (dpg.mvPlotCol_Line, dpg.mvThemeCat_Plots),
    plot_marker_fill = (dpg.mvPlotCol_MarkerFill, dpg.mvThemeCat_Plots),
    plot_marker_outline = (dpg.mvPlotCol_MarkerOutline, dpg.mvThemeCat_Plots),
    plot_bg = (dpg.mvPlotCol_PlotBg, dpg.mvThemeCat_Plots),
    plot_border = (dpg.mvPlotCol_PlotBorder, dpg.mvThemeCat_Plots),
    plot_query = (dpg.mvPlotCol_Query, dpg.mvThemeCat_Plots),
    plot_selection = (dpg.mvPlotCol_Selection, dpg.mvThemeCat_Plots),
    plot_title_text = (dpg.mvPlotCol_TitleText, dpg.mvThemeCat_Plots),
    plot_x_axis = (dpg.mvPlotCol_XAxis, dpg.mvThemeCat_Plots),
    plot_x_axis_grid = (dpg.mvPlotCol_XAxisGrid, dpg.mvThemeCat_Plots),
    plot_y_axis = (dpg.mvPlotCol_YAxis, dpg.mvThemeCat_Plots),
    plot_y_axis2 = (dpg.mvPlotCol_YAxis2, dpg.mvThemeCat_Plots),
    plot_y_axis3 = (dpg.mvPlotCol_YAxis3, dpg.mvThemeCat_Plots),
    plot_y_axis_grid = (dpg.mvPlotCol_YAxisGrid, dpg.mvThemeCat_Plots),
    plot_y_axis_grid2 = (dpg.mvPlotCol_YAxisGrid2, dpg.mvThemeCat_Plots),
    plot_y_axis_grid3 = (dpg.mvPlotCol_YAxisGrid3, dpg.mvThemeCat_Plots),
    node_box_selector = (dpg.mvNodeCol_BoxSelector, dpg.mvThemeCat_Nodes),
    node_box_selector_outline = (
        dpg.mvNodeCol_BoxSelectorOutline, dpg.mvThemeCat_Nodes),
    node_grid_background = (
        dpg.mvNodeCol_GridBackground, dpg.mvThemeCat_Nodes),
    node_grid_line = (dpg.mvNodeCol_GridLine, dpg.mvThemeCat_Nodes),
    node_link = (dpg.mvNodeCol_Link, dpg.mvThemeCat_Nodes),
    node_link_hovered = (dpg.mvNodeCol_LinkHovered, dpg.mvThemeCat_Nodes),
    node_link_selected = (dpg.mvNodeCol_LinkSelected, dpg.mvThemeCat_Nodes),
    node_background = (dpg.mvNodeCol_NodeBackground, dpg.mvThemeCat_Nodes),
    node_background_hovered = (
        dpg.mvNodeCol_NodeBackgroundHovered, dpg.mvThemeCat_Nodes),
    node_background_selected = (
        dpg.mvNodeCol_NodeBackgroundSelected, dpg.mvThemeCat_Nodes),
    node_outline = (dpg.mvNodeCol_NodeOutline, dpg.mvThemeCat_Nodes),
    node_pin = (dpg.mvNodeCol_Pin, dpg.mvThemeCat_Nodes),
    node_pin_hovered = (dpg.mvNodeCol_PinHovered, dpg.mvThemeCat_Nodes),
    node_title_bar = (dpg.mvNodeCol_TitleBar, dpg.mvThemeCat_Nodes),
    node_title_bar_hovered = (
        dpg.mvNodeCol_TitleBarHovered, dpg.mvThemeCat_Nodes),
    node_title_bar_selected = (
        dpg.mvNodeCol_TitleBarSelected, dpg.mvThemeCat_Nodes),
)

STYLE_OPTN = dict(
    alpha = (dpg.mvStyleVar_Alpha, dpg.mvThemeCat_Core),
    button_text_align = (dpg.mvStyleVar_ButtonTextAlign, dpg.mvThemeCat_Core),
    cell_padding = (dpg.mvStyleVar_CellPadding, dpg.mvThemeCat_Core),
    child_border_size = (dpg.mvStyleVar_ChildBorderSize, dpg.mvThemeCat_Core),
    child_rounding = (dpg.mvStyleVar_ChildRounding, dpg.mvThemeCat_Core),
    frame_border_size = (dpg.mvStyleVar_FrameBorderSize, dpg.mvThemeCat_Core),
    frame_padding = (dpg.mvStyleVar_FramePadding, dpg.mvThemeCat_Core),
    frame_rounding = (dpg.mvStyleVar_FrameRounding, dpg.mvThemeCat_Core),
    grab_min_size = (dpg.mvStyleVar_GrabMinSize, dpg.mvThemeCat_Core),
    grab_rounding = (dpg.mvStyleVar_GrabRounding, dpg.mvThemeCat_Core),
    indent_spacing = (dpg.mvStyleVar_IndentSpacing, dpg.mvThemeCat_Core),
    item_inner_spacing = (
        dpg.mvStyleVar_ItemInnerSpacing, dpg.mvThemeCat_Core),
    item_spacing = (dpg.mvStyleVar_ItemSpacing, dpg.mvThemeCat_Core),
    popup_border_size = (dpg.mvStyleVar_PopupBorderSize, dpg.mvThemeCat_Core),
    popup_rounding = (dpg.mvStyleVar_PopupRounding, dpg.mvThemeCat_Core),
    scrollbar_rounding = (
        dpg.mvStyleVar_ScrollbarRounding, dpg.mvThemeCat_Core),
    scrollbar_size = (dpg.mvStyleVar_ScrollbarSize, dpg.mvThemeCat_Core),
    selectable_text_align = (
        dpg.mvStyleVar_SelectableTextAlign, dpg.mvThemeCat_Core),
    tab_rounding = (dpg.mvStyleVar_TabRounding, dpg.mvThemeCat_Core),
    window_border_size = (
        dpg.mvStyleVar_WindowBorderSize, dpg.mvThemeCat_Core),
    window_min_size = (dpg.mvStyleVar_WindowMinSize, dpg.mvThemeCat_Core),
    window_padding = (dpg.mvStyleVar_WindowPadding, dpg.mvThemeCat_Core),
    window_rounding = (dpg.mvStyleVar_WindowRounding, dpg.mvThemeCat_Core),
    window_title_align = (
        dpg.mvStyleVar_WindowTitleAlign, dpg.mvThemeCat_Core),
    plot_annotation_padding = (
        dpg.mvPlotStyleVar_AnnotationPadding, dpg.mvThemeCat_Plots),
    plot_digital_bit_gap = (
        dpg.mvPlotStyleVar_DigitalBitGap, dpg.mvThemeCat_Plots),
    plot_digital_bit_height = (
        dpg.mvPlotStyleVar_DigitalBitHeight, dpg.mvThemeCat_Plots),
    plot_error_bar_size = (
        dpg.mvPlotStyleVar_ErrorBarSize, dpg.mvThemeCat_Plots),
    plot_error_bar_weight = (
        dpg.mvPlotStyleVar_ErrorBarWeight, dpg.mvThemeCat_Plots),
    plot_fill_alpha = (dpg.mvPlotStyleVar_FillAlpha, dpg.mvThemeCat_Plots),
    plot_fit_padding = (dpg.mvPlotStyleVar_FitPadding, dpg.mvThemeCat_Plots),
    plot_label_padding = (
        dpg.mvPlotStyleVar_LabelPadding, dpg.mvThemeCat_Plots),
    plot_legend_inner_padding = (
        dpg.mvPlotStyleVar_LegendInnerPadding, dpg.mvThemeCat_Plots),
    plot_legend_padding = (
        dpg.mvPlotStyleVar_LegendPadding, dpg.mvThemeCat_Plots),
    plot_legend_spacing = (
        dpg.mvPlotStyleVar_LegendSpacing, dpg.mvThemeCat_Plots),
    plot_line_weight = (dpg.mvPlotStyleVar_LineWeight, dpg.mvThemeCat_Plots),
    plot_major_grid_size = (
        dpg.mvPlotStyleVar_MajorGridSize, dpg.mvThemeCat_Plots),
    plot_major_tick_len = (
        dpg.mvPlotStyleVar_MajorTickLen, dpg.mvThemeCat_Plots),
    plot_major_tick_size = (
        dpg.mvPlotStyleVar_MajorTickSize, dpg.mvThemeCat_Plots),
    plot_marker = (dpg.mvPlotStyleVar_Marker, dpg.mvThemeCat_Plots),
    plot_marker_size = (dpg.mvPlotStyleVar_MarkerSize, dpg.mvThemeCat_Plots),
    plot_marker_weight = (
        dpg.mvPlotStyleVar_MarkerWeight, dpg.mvThemeCat_Plots),
    plot_minor_alpha = (dpg.mvPlotStyleVar_MinorAlpha, dpg.mvThemeCat_Plots),
    plot_minor_grid_size = (
        dpg.mvPlotStyleVar_MinorGridSize, dpg.mvThemeCat_Plots),
    plot_minor_tick_len = (
        dpg.mvPlotStyleVar_MinorTickLen, dpg.mvThemeCat_Plots),
    plot_minor_tick_size = (
        dpg.mvPlotStyleVar_MinorTickSize, dpg.mvThemeCat_Plots),
    plot_mouse_pos_padding = (
        dpg.mvPlotStyleVar_MousePosPadding, dpg.mvThemeCat_Plots),
    plot_border_size = (dpg.mvPlotStyleVar_PlotBorderSize,
                        dpg.mvThemeCat_Plots),
    plot_default_size = (
        dpg.mvPlotStyleVar_PlotDefaultSize, dpg.mvThemeCat_Plots),
    plot_min_size = (dpg.mvPlotStyleVar_PlotMinSize, dpg.mvThemeCat_Plots),
    plot_padding = (dpg.mvPlotStyleVar_PlotPadding, dpg.mvThemeCat_Plots),
    node_grid_spacing = (dpg.mvNodeStyleVar_GridSpacing,
                         dpg.mvThemeCat_Nodes),
    node_link_hover_distance = (
        dpg.mvNodeStyleVar_LinkHoverDistance, dpg.mvThemeCat_Nodes),
    node_link_line_segments_per_length = (
        dpg.mvNodeStyleVar_LinkLineSegmentsPerLength, dpg.mvThemeCat_Nodes),
    node_link_thickness = (
        dpg.mvNodeStyleVar_LinkThickness, dpg.mvThemeCat_Nodes),
    node_border_thickness = (
        dpg.mvNodeStyleVar_NodeBorderThickness, dpg.mvThemeCat_Nodes),
    node_corner_rounding = (
        dpg.mvNodeStyleVar_NodeCornerRounding, dpg.mvThemeCat_Nodes),
    node_padding_horizontal = (
        dpg.mvNodeStyleVar_NodePaddingHorizontal, dpg.mvThemeCat_Nodes),
    node_padding_vertical = (
        dpg.mvNodeStyleVar_NodePaddingVertical, dpg.mvThemeCat_Nodes),
    node_pin_circle_radius = (
        dpg.mvNodeStyleVar_PinCircleRadius, dpg.mvThemeCat_Nodes),
    node_pin_hover_radius = (
        dpg.mvNodeStyleVar_PinHoverRadius, dpg.mvThemeCat_Nodes),
    node_pin_line_thickness = (
        dpg.mvNodeStyleVar_PinLineThickness, dpg.mvThemeCat_Nodes),
    node_pin_offset = (dpg.mvNodeStyleVar_PinOffset, dpg.mvThemeCat_Nodes),
    node_pin_quad_side_length = (
        dpg.mvNodeStyleVar_PinQuadSideLength, dpg.mvThemeCat_Nodes),
    node_pin_triangle_side_length = (
        dpg.mvNodeStyleVar_PinTriangleSideLength, dpg.mvThemeCat_Nodes),
)

