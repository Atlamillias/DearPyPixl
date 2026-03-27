from dearpygui import _dearpygui

from dearpypixl.lib.items import mvTheme
from dearpypixl.lib.items import mvThemeComponent
from dearpypixl.lib.items import mvThemeColor
from dearpypixl.lib.items import mvThemeStyle


__all__ = (
    "alpha",
    "disabled_alpha",
    "window_padding",
    "window_rounding",
    "window_border_size",
    "window_min_size",
    "window_title_align",
    "child_rounding",
    "child_border_size",
    "popup_rounding",
    "popup_border_size",
    "frame_padding",
    "frame_rounding",
    "frame_border_size",
    "item_spacing",
    "item_inner_spacing",
    "indent_spacing",
    "cell_padding",
    "scrollbar_size",
    "scrollbar_rounding",
    "grab_min_size",
    "grab_rounding",
    "tab_rounding",
    "tab_border_size",
    "tab_bar_border_size",
    "table_angled_headers_angle",
    "table_angled_headers_text_align",
    "button_text_align",
    "selectable_text_align",
    "separator_text_border_size",
    "separator_text_align",
    "separator_text_padding",
    "docking_separator_size",
    "plot_line_weight",
    "plot_marker",
    "plot_marker_size",
    "plot_marker_weight",
    "plot_fill_alpha",
    "plot_error_bar_size",
    "plot_error_bar_weight",
    "plot_digital_bit_height",
    "plot_digital_bit_gap",
    "plot_border_size",
    "plot_minor_alpha",
    "plot_major_tick_len",
    "plot_minor_tick_len",
    "plot_major_tick_size",
    "plot_minor_tick_size",
    "plot_major_grid_size",
    "plot_minor_grid_size",
    "plot_padding",
    "plot_label_padding",
    "plot_legend_padding",
    "plot_legend_inner_padding",
    "plot_legend_spacing",
    "plot_mouse_pos_padding",
    "plot_annotation_padding",
    "plot_fit_padding",
    "plot_default_size",
    "plot_min_size",
    "node_grid_spacing",
    "node_corner_rounding",
    "node_padding",
    "node_border_thickness",
    "node_link_thickness",
    "node_link_line_segments_per_length",
    "node_link_hover_distance",
    "node_pin_circle_radius",
    "node_pin_quad_side_length",
    "node_pin_triangle_side_length",
    "node_pin_line_thickness",
    "node_pin_hover_radius",
    "node_pin_offset",
    "node_mini_map_padding",
    "node_mini_map_offset",
)




def alpha(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_Alpha, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def disabled_alpha(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_DisabledAlpha, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_WindowPadding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_WindowRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_WindowBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_min_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_WindowMinSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_title_align(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_WindowTitleAlign, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def child_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ChildRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def child_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ChildBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def popup_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_PopupRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def popup_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_PopupBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_FramePadding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_FrameRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_FrameBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def item_spacing(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ItemSpacing, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def item_inner_spacing(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ItemInnerSpacing, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def indent_spacing(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_IndentSpacing, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def cell_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_CellPadding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ScrollbarSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ScrollbarRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def grab_min_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_GrabMinSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def grab_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_GrabRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_TabRounding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_TabBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_bar_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_TabBarBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_angled_headers_angle(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_TableAngledHeadersAngle, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_angled_headers_text_align(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_TableAngledHeadersTextAlign, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def button_text_align(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_ButtonTextAlign, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def selectable_text_align(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_SelectableTextAlign, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator_text_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_SeparatorTextBorderSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator_text_align(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_SeparatorTextAlign, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator_text_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_SeparatorTextPadding, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def docking_separator_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvStyleVar_DockingSeparatorSize, x, y, category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_line_weight(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_LineWeight, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_marker(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_Marker, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_marker_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MarkerSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_marker_weight(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MarkerWeight, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_fill_alpha(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_FillAlpha, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_error_bar_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_ErrorBarSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_error_bar_weight(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_ErrorBarWeight, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_digital_bit_height(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_DigitalBitHeight, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_digital_bit_gap(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_DigitalBitGap, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_border_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_PlotBorderSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_minor_alpha(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MinorAlpha, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_major_tick_len(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MajorTickLen, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_minor_tick_len(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MinorTickLen, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_major_tick_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MajorTickSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_minor_tick_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MinorTickSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_major_grid_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MajorGridSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_minor_grid_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MinorGridSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_PlotPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_label_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_LabelPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_LegendPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_inner_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_LegendInnerPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_spacing(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_LegendSpacing, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_mouse_pos_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_MousePosPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_annotation_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_AnnotationPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_fit_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_FitPadding, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_default_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_PlotDefaultSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_min_size(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvPlotStyleVar_PlotMinSize, x, y, category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_grid_spacing(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_GridSpacing, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_corner_rounding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_NodeCornerRounding, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_NodePadding, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_border_thickness(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_NodeBorderThickness, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link_thickness(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_LinkThickness, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link_line_segments_per_length(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_LinkLineSegmentsPerLength, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link_hover_distance(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_LinkHoverDistance, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_circle_radius(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinCircleRadius, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_quad_side_length(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinQuadSideLength, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_triangle_side_length(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinTriangleSideLength, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_line_thickness(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinLineThickness, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_hover_radius(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinHoverRadius, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_offset(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodeStyleVar_PinOffset, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_padding(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodesStyleVar_MiniMapPadding, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_offset(x = 1, y = -1, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeStyle, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    if hasattr(x, "__iter__"): x, y = x  # type: ignore
    return __itemtype.create(__dearpygui.mvNodesStyleVar_MiniMapOffset, x, y, category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


