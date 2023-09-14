"""Contains functions that return preset themes.

A preset is created only if it doesn't exist. Otherwise,
the existing preset(s) are returned. Each preset is
assigned an alias that remains constant throughout
sessions. The collection of available Dear PyPixl presets
can be obtained by calling the `load_presets` function.

Presets can be cloned by calling their `.__copy__` method.
"""
import functools
import contextlib
from . import _typing, api
from . import color, style
from .items import (
    mvTheme,
    mvThemeComponent,
)




def _onetime_setup():
    if not api.Application.state()['ok']:
        api.Application.setup()
    global _onetime_setup
    _onetime_setup = lambda: None


_preset_fns: tuple[_typing.Callable[[], mvTheme], ...] = ()

def _dearpypixl_preset(preset_name: str):
    def capture_fn(fn: _typing.Callable[[], mvTheme]):
        @functools.wraps(fn)
        def get_theme_preset():
            _onetime_setup()
            if api.Registry.alias_exists(preset_name):
                return mvTheme.new(preset_name)
            return fn()
        global _preset_fns
        _preset_fns += (fn,)
        return get_theme_preset
    preset_name = f'[{mvTheme.__name__}] {preset_name}'
    return capture_fn


@contextlib.contextmanager
def _theme_preset(name: str):
    with mvTheme.aliased(tag=f'[mvTheme] {name}', label=f'[mvTheme] {name}') as theme:
        color_c = mvThemeComponent.aliased(
            tag=f'[mvThemeComponent] color ({name})',
            label=f'[mvThemeComponent] color ({name})',
        )
        style_c = mvThemeComponent.aliased(
            tag=f'[mvThemeComponent] style ({name})',
            label=f'[mvThemeComponent] style ({name})',
        )
    try:
        yield theme
    finally:
        id_element = api.ThemeElement.identify
        for elem_tp, c in (('mvThemeColor', color_c), ('mvThemeStyle', style_c)):
            label_pfx = elem_tp.removeprefix('mvTheme').lower()
            for e in c.children(1):
                alias = f'[{elem_tp}] {id_element(e)} ({name}.{label_pfx})'
                api.Item.set_alias(
                    e,
                    alias,
                )
                api.Item.configure(e, label=alias)




def load_presets() -> tuple[mvTheme, ...]:
    """Return all Dear PyPixl presets, loading them if they do
    not exist.
    """
    return tuple(fn() for fn in _preset_fns)




# [ THEMES ]

# "Complete" themes use most but not all elements. The
# functions that make the unused elements are simply left
# uncalled; this makes it easier to tell which elements are
# missing at a glance.


@_dearpypixl_preset('Default')
def default():
    """Return the preset that emulates Dear PyGui's internal
    default theme.
    """
    with _theme_preset('Default') as theme:
        with mvThemeComponent.new(theme[1][0]):
            color.border(78, 78, 78, 255)
            color.border_shadow(78, 78, 78, 255)
            color.button(51, 51, 55, 255)
            color.button_active(0, 119, 200, 153)
            color.button_hovered(29, 151, 236, 103)
            color.check_mark(0, 119, 200, 153)
            color.child_bg(37, 37, 38, 255)
            color.docking_empty_bg(51, 51, 51, 255)
            color.docking_preview(0, 119, 200, 153)
            color.drag_drop_target(255, 255, 0, 179)
            color.frame_bg(51, 51, 55, 255)
            color.frame_bg_active(0, 119, 200, 153)
            color.frame_bg_hovered(29, 151, 236, 103)
            color.header(51, 51, 55, 255)
            color.header_active(0, 119, 200, 153)
            color.header_hovered(29, 151, 236, 103)
            color.menu_bar_bg(51, 51, 55, 255)
            color.modal_window_dim_bg(37, 37, 38, 150)
            color.nav_highlight(37, 37, 38, 255)
            color.nav_windowing_dim_bg(204, 204, 204, 51)
            color.nav_windowing_highlight(255, 255, 255, 179)
            color.popup_bg(37, 37, 38, 255)
            color.resize_grip(37, 37, 38, 255)
            color.resize_grip_hovered(51, 51, 55, 255)
            color.resize_grip_active(51, 51, 55, 255)
            color.scrollbar_bg(51, 51, 55, 255)
            color.scrollbar_grab(82, 82, 85, 255)
            color.scrollbar_grab_active(90, 90, 95, 255)
            color.scrollbar_grab_hovered(90, 90, 95, 255)
            color.separator(78, 78, 78, 255)
            color.separator_active(78, 78, 78, 255)
            color.separator_hovered(78, 78, 78, 255)
            color.slider_grab(29, 151, 236, 103)
            color.slider_grab_active(0, 119, 200, 153)
            color.tab(51, 51, 55, 255)
            color.tab_active(0, 119, 200, 153)
            color.tab_hovered(29, 151, 236, 103)
            color.tab_unfocused(51, 51, 55, 255)
            color.tab_unfocused_active(0, 119, 200, 153)
            color.table_border_light(59, 59, 64, 255)
            color.table_border_strong(79, 79, 89, 255)
            color.table_header_bg(48, 48, 51, 255)
            color.table_row_bg(0, 0, 0, 0)
            color.table_row_bg_alt(255, 255, 255, 15)
            color.text(255, 255, 255, 255)
            color.text_disabled(151, 151, 151, 255)
            color.text_selected_bg(0, 119, 200, 153)
            color.title_bg(37, 37, 38, 255)
            color.title_bg_active(15, 86, 135, 255)
            color.title_bg_collapsed(37, 37, 38, 255)
            color.window_bg(37, 37, 38, 255)
            color.plot_bg
            color.plot_border
            color.plot_crosshairs
            color.plot_error_bar
            color.plot_fill
            color.plot_frame_bg
            color.plot_histogram(0, 119, 200, 153)
            color.plot_histogram_hovered(29, 151, 236, 103)
            color.plot_inlay_text
            color.plot_legend_bg
            color.plot_legend_border
            color.plot_legend_text
            color.plot_line
            color.plot_lines(0, 119, 200, 153)
            color.plot_lines_hovered(29, 151, 236, 103)
            color.plot_marker_fill
            color.plot_marker_outline
            color.plot_query
            color.plot_selection
            color.plot_title_text
            color.plot_x_axis
            color.plot_x_axis_grid
            color.plot_y_axis
            color.plot_y_axis2
            color.plot_y_axis3
            color.plot_y_axis_grid
            color.plot_y_axis_grid2
            color.plot_y_axis_grid3
            color.node_bg(62, 62, 62, 255)
            color.node_bg_hovered(75, 75, 75, 255)
            color.node_bg_selected(75, 75, 75, 255)
            color.node_box_selector(61, 133, 224, 30)
            color.node_box_selector_outline(61, 133, 224, 150)
            color.node_grid_bg(35, 35, 35, 255)
            color.node_grid_line(0, 0, 0, 255)
            color.node_grid_line_primary(240, 240, 240, 60)
            color.node_link(255, 255, 255, 200)
            color.node_link_hovered(66, 150, 250, 255)
            color.node_link_selected(66, 150, 250, 255)
            color.node_mini_map_bg(25, 25, 25, 150)
            color.node_mini_map_bg_hovered(150, 150, 150, 200)
            color.node_mini_map_canvas(200, 200, 200, 25)
            color.node_mini_map_canvas_outline(200, 200, 200, 200)
            color.node_mini_map_link(61, 133, 224, 200)
            color.node_mini_map_link_selected(66, 150, 250, 255)
            color.node_mini_map_node_bg(200, 200, 200, 100)
            color.node_mini_map_node_bg_hovered(200, 200, 200, 255)
            color.node_mini_map_node_bg_selected(200, 200, 200, 255)
            color.node_mini_map_node_outline(200, 200, 200, 100)
            color.node_mini_map_outline(150, 150, 150, 100)
            color.node_mini_map_outline_hovered(150, 150, 150, 200)
            color.node_outline(100, 100, 100, 255)
            color.node_pin(199, 199, 41, 255)
            color.node_pin_hovered(255, 255, 50, 255)
            color.node_title_bar(37, 37, 38, 255)
            color.node_title_bar_hovered(15, 86, 135, 255)
            color.node_title_bar_selected(0, 119, 200, 153)
        with mvThemeComponent.new(theme[1][1]):
            style.alpha
            style.button_text_align(0.5, 0.5)
            style.cell_padding(4.0, 2.0)
            style.child_border_size(1)
            style.child_rounding(0)
            style.frame_border_size(0)
            style.frame_padding(4.0, 3.0)
            style.frame_rounding(0)
            style.grab_min_size(10.0)
            style.grab_rounding(0)
            style.indent_spacing(21.0)
            style.item_inner_spacing(4, 4)
            style.item_spacing(8, 4)
            style.popup_border_size(1)
            style.popup_rounding(0)
            style.scrollbar_rounding(9)
            style.scrollbar_size(14)
            style.selectable_text_align(0.0, 0.5)
            style.tab_rounding(4)
            style.window_border_size(1)
            style.window_min_size(100, 100)
            style.window_padding(8, 8)
            style.window_rounding(0)
            style.window_title_align(0.0, 0.5)
            style.plot_annotation_padding(2.0, 2.0)
            style.plot_border_size(1)
            style.plot_default_size(400, 300)
            style.plot_digital_bit_gap(8.0)
            style.plot_digital_bit_height(4.0)
            style.plot_error_bar_size(5.0)
            style.plot_error_bar_weight(1.0)
            style.plot_fill_alpha(1.0)
            style.plot_fit_padding(0.0, 0.0)
            style.plot_label_padding(5, 5)
            style.plot_legend_inner_padding(5, 5)
            style.plot_legend_padding(10, 10)
            style.plot_legend_spacing(5, 0)
            style.plot_line_weight(1.0)
            style.plot_major_grid_size(1.0, 1.0)
            style.plot_major_tick_len(10, 10)
            style.plot_major_tick_size(1.0, 1.0)
            style.plot_marker(4.0)
            style.plot_marker_size(4.0)
            style.plot_marker_weight(1.0)
            style.plot_min_size(200, 150)
            style.plot_minor_alpha(0.25)
            style.plot_minor_grid_size(1.0, 1.0)
            style.plot_minor_tick_len(5, 5)
            style.plot_minor_tick_size(1.0, 1.0)
            style.plot_mouse_pos_padding(10, 10)
            style.plot_padding(10, 10)
            style.node_border_thickness(1)
            style.node_corner_rounding(4)
            style.node_grid_spacing(24)
            style.node_link_hover_distance(10)
            style.node_link_line_segments_per_length(0)
            style.node_link_thickness(3)
            #style.node_mini_map_offset(4, 0)  DPG BUG?
            style.node_mini_map_padding(8, 8)
            style.node_padding(8, 8)
            style.node_pin_circle_radius(4)
            style.node_pin_hover_radius(10)
            style.node_pin_line_thickness(1)
            style.node_pin_offset(0)
            style.node_pin_quad_side_length(7)
            style.node_pin_triangle_side_length(10)
    return theme


@_dearpypixl_preset('ImGui Dark')
def imgui_dark():
    """Return the preset emulating `dearpygui_ext`s "imgui dark"
    theme.
    """
    with _theme_preset('ImGui Dark') as theme:
        with mvThemeComponent.new(theme[1][0]):
            color.border(110, 110, 128, 128)
            color.border_shadow(0, 0, 0, 0)
            color.button(66, 150, 250, 102)
            color.button_active(15, 135, 250, 255)
            color.button_hovered(66, 150, 250, 255)
            color.check_mark(66, 150, 250, 255)
            color.child_bg(0, 0, 0, 0)
            color.docking_empty_bg(51, 51, 51, 255)
            color.docking_preview(66, 150, 250, 178)
            color.drag_drop_target(255, 255, 0, 230)
            color.frame_bg(41, 74, 122, 138)
            color.frame_bg_active(66, 150, 250, 171)
            color.frame_bg_hovered(66, 150, 250, 102)
            color.header(66, 150, 250, 79)
            color.header_active(66, 150, 250, 255)
            color.header_hovered(66, 150, 250, 204)
            color.menu_bar_bg(36, 36, 36, 255)
            color.modal_window_dim_bg(204, 204, 204, 89)
            color.nav_highlight(66, 150, 250, 255)
            color.nav_windowing_dim_bg(204, 204, 204, 51)
            color.nav_windowing_highlight(255, 255, 255, 178)
            color.popup_bg(20, 20, 20, 240)
            color.resize_grip(66, 150, 250, 51)
            color.resize_grip_active(66, 150, 250, 242)
            color.resize_grip_hovered(66, 150, 250, 171)
            color.scrollbar_bg(5, 5, 5, 135)
            color.scrollbar_grab(79, 79, 79, 255)
            color.scrollbar_grab_active(130, 130, 130, 255)
            color.scrollbar_grab_hovered(105, 105, 105, 255)
            color.separator(110, 110, 128, 128)
            color.separator_active(26, 102, 191, 255)
            color.separator_hovered(26, 102, 191, 199)
            color.slider_grab(61, 133, 224, 255)
            color.slider_grab_active(66, 150, 250, 255)
            color.tab(46, 89, 148, 219)
            color.tab_active(51, 105, 173, 255)
            color.tab_hovered(66, 150, 250, 204)
            color.tab_unfocused(18, 26, 38, 247)
            color.tab_unfocused_active(36, 66, 107, 255)
            color.table_border_light(59, 59, 64, 255)
            color.table_border_strong(79, 79, 89, 255)
            color.table_header_bg(48, 48, 51, 255)
            color.table_row_bg(0, 0, 0, 0)
            color.table_row_bg_alt(255, 255, 255, 15)
            color.text(255, 255, 255, 255)
            color.text_disabled(128, 128, 128, 255)
            color.text_selected_bg(66, 150, 250, 89)
            color.title_bg(10, 10, 10, 255)
            color.title_bg_active(41, 74, 122, 255)
            color.title_bg_collapsed(0, 0, 0, 130)
            color.window_bg(15, 15, 15, 240)
            color.plot_bg(0, 0, 0, 128)
            color.plot_border(110, 110, 128, 128)
            color.plot_crosshairs(255, 255, 255, 128)
            color.plot_error_bar
            color.plot_fill
            color.plot_frame_bg(255, 255, 255, 18)
            color.plot_histogram(230, 178, 0, 255)
            color.plot_histogram_hovered(255, 153, 0, 255)
            color.plot_inlay_text(255, 255, 255, 255)
            color.plot_legend_bg(20, 20, 20, 240)
            color.plot_legend_border(110, 110, 128, 128)
            color.plot_legend_text(255, 255, 255, 255)
            color.plot_line
            color.plot_lines(156, 156, 156, 255)
            color.plot_lines_hovered(255, 110, 89, 255)
            color.plot_marker_fill
            color.plot_marker_outline
            color.plot_query(0, 255, 112, 255)
            color.plot_selection(255, 153, 0, 255)
            color.plot_title_text(255, 255, 255, 255)
            color.plot_x_axis(255, 255, 255, 255)
            color.plot_x_axis_grid(255, 255, 255, 64)
            color.plot_y_axis(255, 255, 255, 255)
            color.plot_y_axis2(255, 255, 255, 255)
            color.plot_y_axis3(255, 255, 255, 255)
            color.plot_y_axis_grid(255, 255, 255, 64)
            color.plot_y_axis_grid2(255, 255, 255, 64)
            color.plot_y_axis_grid3(255, 255, 255, 64)
            color.node_bg(50, 50, 50, 255)
            color.node_bg_hovered(75, 75, 75, 255)
            color.node_bg_selected(75, 75, 75, 255)
            color.node_box_selector(61, 133, 224, 30)
            color.node_box_selector_outline(61, 133, 224, 150)
            color.node_grid_bg(40, 40, 50, 200)
            color.node_grid_line(200, 200, 200, 40)
            color.node_grid_line_primary
            color.node_link(61, 133, 224, 200)
            color.node_link_hovered(66, 150, 250, 255)
            color.node_link_selected(66, 150, 250, 255)
            color.node_mini_map_bg
            color.node_mini_map_bg_hovered
            color.node_mini_map_canvas
            color.node_mini_map_canvas_outline
            color.node_mini_map_link
            color.node_mini_map_link_selected
            color.node_mini_map_node_bg
            color.node_mini_map_node_bg_hovered
            color.node_mini_map_node_bg_selected
            color.node_mini_map_node_outline
            color.node_mini_map_outline
            color.node_mini_map_outline_hovered
            color.node_outline(100, 100, 100, 255)
            color.node_pin(53, 150, 250, 180)
            color.node_pin_hovered(53, 150, 250, 255)
            color.node_title_bar(41, 74, 122, 255)
            color.node_title_bar_hovered(66, 150, 250, 255)
            color.node_title_bar_selected(66, 150, 250, 255)
        with mvThemeComponent.new(theme[1][1]):
            style.alpha
            style.button_text_align(0.5, 0.5)
            style.cell_padding(4.0, 2.0)
            style.child_border_size(1)
            style.child_rounding(0)
            style.frame_border_size(0)
            style.frame_padding(4.0, 3.0)
            style.frame_rounding(0)
            style.grab_min_size(10.0)
            style.grab_rounding(0)
            style.indent_spacing(21.0)
            style.item_inner_spacing(4, 4)
            style.item_spacing(8, 4)
            style.popup_border_size(1)
            style.popup_rounding(0)
            style.scrollbar_rounding(9)
            style.scrollbar_size(14)
            style.selectable_text_align(0.0, 0.5)
            style.tab_rounding(4)
            style.window_border_size(1)
            style.window_min_size(100, 100)
            style.window_padding(8, 8)
            style.window_rounding(0)
            style.window_title_align(0.0, 0.5)
            style.plot_annotation_padding(2.0, 2.0)
            style.plot_border_size(1)
            style.plot_default_size(400, 300)
            style.plot_digital_bit_gap(8.0)
            style.plot_digital_bit_height(4.0)
            style.plot_error_bar_size(5.0)
            style.plot_error_bar_weight(1.0)
            style.plot_fill_alpha(1.0)
            style.plot_fit_padding(0.0, 0.0)
            style.plot_label_padding(5, 5)
            style.plot_legend_inner_padding(5, 5)
            style.plot_legend_padding(10, 10)
            style.plot_legend_spacing(5, 0)
            style.plot_line_weight(1.0)
            style.plot_major_grid_size(1.0, 1.0)
            style.plot_major_tick_len(10, 10)
            style.plot_major_tick_size(1.0, 1.0)
            style.plot_marker(4.0)
            style.plot_marker_size(4.0)
            style.plot_marker_weight(1.0)
            style.plot_min_size(200, 150)
            style.plot_minor_alpha(0.25)
            style.plot_minor_grid_size(1.0, 1.0)
            style.plot_minor_tick_len(5, 5)
            style.plot_minor_tick_size(1.0, 1.0)
            style.plot_mouse_pos_padding(10, 10)
            style.plot_padding(10, 10)
            style.node_border_thickness(1)
            style.node_corner_rounding(4)
            style.node_grid_spacing(24)
            style.node_link_hover_distance(10)
            style.node_link_line_segments_per_length(0)
            style.node_link_thickness(3)
            #style.node_mini_map_offset(4, 0)  DPG BUG?
            style.node_mini_map_padding(8, 8)
            style.node_padding(8, 8)
            style.node_pin_circle_radius(4)
            style.node_pin_hover_radius(10)
            style.node_pin_line_thickness(1)
            style.node_pin_offset(0)
            style.node_pin_quad_side_length(7)
            style.node_pin_triangle_side_length(10)
    return theme


# TODO
# @_dearpypixl_preset('ImGui Light')
def _imgui_light():
    """Return the preset emulating `dearpygui_ext`s "imgui light"
    theme.
    """
    with _theme_preset('ImGui Light') as theme:
        with mvThemeComponent.new(theme[1][0]):
            color.border
            color.border_shadow
            color.button
            color.button_active
            color.button_hovered
            color.check_mark
            color.child_bg
            color.docking_empty_bg
            color.docking_preview
            color.drag_drop_target
            color.frame_bg
            color.frame_bg_active
            color.frame_bg_hovered
            color.header
            color.header_active
            color.header_hovered
            color.menu_bar_bg
            color.modal_window_dim_bg
            color.nav_highlight
            color.nav_windowing_dim_bg
            color.nav_windowing_highlight
            color.popup_bg
            color.resize_grip
            color.resize_grip_active
            color.resize_grip_hovered
            color.scrollbar_bg
            color.scrollbar_grab
            color.scrollbar_grab_active
            color.scrollbar_grab_hovered
            color.separator
            color.separator_active
            color.separator_hovered
            color.slider_grab
            color.slider_grab_active
            color.tab
            color.tab_active
            color.tab_hovered
            color.tab_unfocused
            color.tab_unfocused_active
            color.table_border_light
            color.table_border_strong
            color.table_header_bg
            color.table_row_bg
            color.table_row_bg_alt
            color.text
            color.text_disabled
            color.text_selected_bg
            color.title_bg
            color.title_bg_active
            color.title_bg_collapsed
            color.window_bg
            color.plot_bg
            color.plot_border
            color.plot_crosshairs
            color.plot_error_bar
            color.plot_fill
            color.plot_frame_bg
            color.plot_histogram
            color.plot_histogram_hovered
            color.plot_inlay_text
            color.plot_legend_bg
            color.plot_legend_border
            color.plot_legend_text
            color.plot_line
            color.plot_lines
            color.plot_lines_hovered
            color.plot_marker_fill
            color.plot_marker_outline
            color.plot_query
            color.plot_selection
            color.plot_title_text
            color.plot_x_axis
            color.plot_x_axis_grid
            color.plot_y_axis
            color.plot_y_axis2
            color.plot_y_axis3
            color.plot_y_axis_grid
            color.plot_y_axis_grid2
            color.plot_y_axis_grid3
            color.node_bg
            color.node_bg_hovered
            color.node_bg_selected
            color.node_box_selector
            color.node_box_selector_outline
            color.node_grid_bg
            color.node_grid_line
            color.node_grid_line_primary
            color.node_link
            color.node_link_hovered
            color.node_link_selected
            color.node_mini_map_bg
            color.node_mini_map_bg_hovered
            color.node_mini_map_canvas
            color.node_mini_map_canvas_outline
            color.node_mini_map_link
            color.node_mini_map_link_selected
            color.node_mini_map_node_bg
            color.node_mini_map_node_bg_hovered
            color.node_mini_map_node_bg_selected
            color.node_mini_map_node_outline
            color.node_mini_map_outline
            color.node_mini_map_outline_hovered
            color.node_outline
            color.node_pin
            color.node_pin_hovered
            color.node_title_bar
            color.node_title_bar_hovered
            color.node_title_bar_selected
        with mvThemeComponent.new(theme[1][1]):
            style.alpha
            style.button_text_align(0.5, 0.5)
            style.cell_padding(4.0, 2.0)
            style.child_border_size(1)
            style.child_rounding(0)
            style.frame_border_size(0)
            style.frame_padding(4.0, 3.0)
            style.frame_rounding(0)
            style.grab_min_size(10.0)
            style.grab_rounding(0)
            style.indent_spacing(21.0)
            style.item_inner_spacing(4, 4)
            style.item_spacing(8, 4)
            style.popup_border_size(1)
            style.popup_rounding(0)
            style.scrollbar_rounding(9)
            style.scrollbar_size(14)
            style.selectable_text_align(0.0, 0.5)
            style.tab_rounding(4)
            style.window_border_size(1)
            style.window_min_size(100, 100)
            style.window_padding(8, 8)
            style.window_rounding(0)
            style.window_title_align(0.0, 0.5)
            style.plot_annotation_padding(2.0, 2.0)
            style.plot_border_size(1)
            style.plot_default_size(400, 300)
            style.plot_digital_bit_gap(8.0)
            style.plot_digital_bit_height(4.0)
            style.plot_error_bar_size(5.0)
            style.plot_error_bar_weight(1.0)
            style.plot_fill_alpha(1.0)
            style.plot_fit_padding(0.0, 0.0)
            style.plot_label_padding(5, 5)
            style.plot_legend_inner_padding(5, 5)
            style.plot_legend_padding(10, 10)
            style.plot_legend_spacing(5, 0)
            style.plot_line_weight(1.0)
            style.plot_major_grid_size(1.0, 1.0)
            style.plot_major_tick_len(10, 10)
            style.plot_major_tick_size(1.0, 1.0)
            style.plot_marker(4.0)
            style.plot_marker_size(4.0)
            style.plot_marker_weight(1.0)
            style.plot_min_size(200, 150)
            style.plot_minor_alpha(0.25)
            style.plot_minor_grid_size(1.0, 1.0)
            style.plot_minor_tick_len(5, 5)
            style.plot_minor_tick_size(1.0, 1.0)
            style.plot_mouse_pos_padding(10, 10)
            style.plot_padding(10, 10)
            style.node_border_thickness(1)
            style.node_corner_rounding(4)
            style.node_grid_spacing(24)
            style.node_link_hover_distance(10)
            style.node_link_line_segments_per_length(0)
            style.node_link_thickness(3)
            #style.node_mini_map_offset(4, 0)  DPG BUG?
            style.node_mini_map_padding(8, 8)
            style.node_padding(8, 8)
            style.node_pin_circle_radius(4)
            style.node_pin_hover_radius(10)
            style.node_pin_line_thickness(1)
            style.node_pin_offset(0)
            style.node_pin_quad_side_length(7)
            style.node_pin_triangle_side_length(10)
    return theme


@_dearpypixl_preset("Padless")
def padless():
    with _theme_preset("Padless") as theme:
        with mvThemeComponent.new(theme[1][1]):
            style.cell_padding(0, 0)
            style.item_spacing(0, 0)
            style.window_padding(0, 0)
    return theme
