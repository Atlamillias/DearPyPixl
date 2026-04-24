from dearpygui import _dearpygui

from dearpypixl.lib.items import mvTheme
from dearpypixl.lib.items import mvThemeComponent
from dearpypixl.lib.items import mvThemeColor
from dearpypixl.lib.items import mvThemeStyle


__all__ = (
    "text",
    "text_disabled",
    "window_bg",
    "child_bg",
    "popup_bg",
    "border",
    "border_shadow",
    "frame_bg",
    "frame_bg_hovered",
    "frame_bg_active",
    "title_bg",
    "title_bg_active",
    "title_bg_collapsed",
    "menu_bar_bg",
    "scrollbar_bg",
    "scrollbar_grab",
    "scrollbar_grab_hovered",
    "scrollbar_grab_active",
    "check_mark",
    "slider_grab",
    "slider_grab_active",
    "button",
    "button_hovered",
    "button_active",
    "header",
    "header_hovered",
    "header_active",
    "separator",
    "separator_hovered",
    "separator_active",
    "resize_grip",
    "resize_grip_hovered",
    "resize_grip_active",
    "input_text_cursor",
    "tab_hovered",
    "tab",
    "tab_selected",
    "tab_selected_overline",
    "tab_dimmed",
    "tab_dimmed_selected",
    "tab_dimmed_selected_overline",
    "docking_preview",
    "docking_empty_bg",
    "plot_lines",
    "plot_lines_hovered",
    "plot_histogram",
    "plot_histogram_hovered",
    "table_header_bg",
    "table_border_strong",
    "table_border_light",
    "table_row_bg",
    "table_row_bg_alt",
    "text_selected_bg",
    "tree_lines",
    "drag_drop_target",
    "drag_drop_target_bg",
    "unsaved_marker",
    "nav_cursor",
    "nav_windowing_highlight",
    "nav_windowing_dim_bg",
    "modal_window_dim_bg",
    "tab_active",
    "tab_unfocused",
    "tab_unfocused_active",
    "nav_highlight",
    "plot_line",
    "plot_fill",
    "plot_marker_outline",
    "plot_marker_fill",
    "plot_error_bar",
    "plot_frame_bg",
    "plot_bg",
    "plot_border",
    "plot_legend_bg",
    "plot_legend_border",
    "plot_legend_text",
    "plot_title_text",
    "plot_inlay_text",
    "plot_axis_text",
    "plot_axis_grid",
    "plot_axis_tick",
    "plot_axis_bg",
    "plot_axis_bg_hovered",
    "plot_axis_bg_active",
    "plot_selection",
    "plot_crosshairs",
    "node_bg",
    "node_bg_hovered",
    "node_bg_selected",
    "node_outline",
    "node_title_bar",
    "node_title_bar_hovered",
    "node_title_bar_selected",
    "node_link",
    "node_link_hovered",
    "node_link_selected",
    "node_pin",
    "node_pin_hovered",
    "node_box_selector",
    "node_box_selector_outline",
    "node_grid_bg",
    "node_grid_line",
    "node_grid_line_primary",
    "node_mini_map_bg",
    "node_mini_map_bg_hovered",
    "node_mini_map_outline",
    "node_mini_map_outline_hovered",
    "node_mini_map_bg",
    "node_mini_map_bg_hovered",
    "node_mini_map_bg_selected",
    "node_mini_map_outline",
    "node_mini_map_link",
    "node_mini_map_link_selected",
    "node_mini_map_canvas",
    "node_mini_map_canvas_outline",
)




def text(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Text, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def text_disabled(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TextDisabled, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def window_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_WindowBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def child_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ChildBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def popup_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_PopupBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def border(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Border, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def border_shadow(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_BorderShadow, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_FrameBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_bg_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_FrameBgHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def frame_bg_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_FrameBgActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def title_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TitleBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def title_bg_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TitleBgActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def title_bg_collapsed(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TitleBgCollapsed, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def menu_bar_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_MenuBarBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ScrollbarBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_grab(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ScrollbarGrab, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_grab_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ScrollbarGrabHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def scrollbar_grab_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ScrollbarGrabActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def check_mark(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_CheckMark, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def slider_grab(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_SliderGrab, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def slider_grab_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_SliderGrabActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def button(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Button, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def button_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ButtonHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def button_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ButtonActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def header(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Header, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def header_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_HeaderHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def header_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_HeaderActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Separator, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_SeparatorHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def separator_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_SeparatorActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def resize_grip(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ResizeGrip, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def resize_grip_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ResizeGripHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def resize_grip_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ResizeGripActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def input_text_cursor(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_InputTextCursor, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_Tab, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_selected_overline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabSelectedOverline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_dimmed(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabDimmed, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_dimmed_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabDimmedSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_dimmed_selected_overline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabDimmedSelectedOverline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def docking_preview(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_DockingPreview, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def docking_empty_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_DockingEmptyBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_lines(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_PlotLines, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_lines_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_PlotLinesHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_histogram(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_PlotHistogram, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_histogram_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_PlotHistogramHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_header_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TableHeaderBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_border_strong(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TableBorderStrong, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_border_light(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TableBorderLight, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_row_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TableRowBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def table_row_bg_alt(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TableRowBgAlt, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def text_selected_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TextSelectedBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tree_lines(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TreeLines, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def drag_drop_target(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_DragDropTarget, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def drag_drop_target_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_DragDropTargetBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def unsaved_marker(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_UnsavedMarker, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def nav_cursor(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_NavCursor, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def nav_windowing_highlight(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_NavWindowingHighlight, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def nav_windowing_dim_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_NavWindowingDimBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def modal_window_dim_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_ModalWindowDimBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_unfocused(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabUnfocused, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def tab_unfocused_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_TabUnfocusedActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def nav_highlight(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvThemeCol_NavHighlight, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Core, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_line(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_Line, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_fill(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_Fill, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_marker_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_MarkerOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_marker_fill(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_MarkerFill, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_error_bar(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_ErrorBar, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_frame_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_FrameBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_PlotBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_border(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_PlotBorder, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_LegendBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_border(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_LegendBorder, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_legend_text(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_LegendText, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_title_text(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_TitleText, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_inlay_text(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_InlayText, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_text(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisText, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_grid(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisGrid, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_tick(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisTick, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisBg, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_bg_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisBgHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_axis_bg_active(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_AxisBgActive, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_selection(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_Selection, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def plot_crosshairs(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvPlotCol_Crosshairs, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Plots, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_NodeBackground, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_bg_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_NodeBackgroundHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_bg_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_NodeBackgroundSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_NodeOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_title_bar(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_TitleBar, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_title_bar_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_TitleBarHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_title_bar_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_TitleBarSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_Link, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_LinkHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_link_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_LinkSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_Pin, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_pin_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_PinHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_box_selector(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_BoxSelector, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_box_selector_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_BoxSelectorOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_grid_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_GridBackground, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_grid_line(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodeCol_GridLine, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_grid_line_primary(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_GridLinePrimary, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapBackground, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_bg_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapBackgroundHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_outline_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapOutlineHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_bg(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapNodeBackground, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_bg_hovered(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapNodeBackgroundHovered, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_bg_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapNodeBackgroundSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapNodeOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_link(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapLink, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_link_selected(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapLinkSelected, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_canvas(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapCanvas, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


def node_mini_map_canvas_outline(obj, g = -1, b = -1, a = 255, /, *, __dearpygui=_dearpygui, __itemtype=mvThemeColor, label = None, use_internal_label = True, user_data = None, tag = 0, parent = 0):
    return __itemtype.create(__dearpygui.mvNodesCol_MiniMapCanvasOutline, obj if g == -1 else (obj, g, b, a), category=__dearpygui.mvThemeCat_Nodes, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent)


