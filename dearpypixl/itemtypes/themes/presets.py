from contextlib import contextmanager
from typing import Generator
from . import Theme


_theme_presets: tuple[Theme, ...] = []


@contextmanager
def _theme_preset(*args, _theme: Theme = None, **kwargs) -> Generator[Theme, None, None]:
    """Yields an instance of Theme and registers it as a preset. It cannot be
    easily deleted.
    """
    try:
        if not _theme:
            theme = Theme(*args, **kwargs)
        else:
            theme = _theme
        yield theme
    finally:
        theme.delete = lambda self, **kwargs: NotImplementedError
        theme.label = f"{theme.label} [PRESET]"
        _theme_presets.append(theme)


################################
#### Complete System Themes ####
################################

# These themes have been fully "fleshed-out". Ideal for the
# Application-level.

with _theme_preset(label="DearPyGui - Default") as dearpygui_internal:
    """A theme preset mirroring DearPyGui's internal default theme.
    """
    # Frequently-used values
    bg_color_normal     =  37,  37,  38, 255
    bg_color_light      =  82,  82,  85, 255
    bg_color_bright     =  90,  90,  95, 255
    panel_color_idle    =  51,  51,  55, 255
    panel_color_hovered =  29, 151, 236, 103
    panel_color_active  =   0, 119, 200, 153
    text_color_enabled  = 255, 255, 255, 255
    text_color_disabled = 151, 151, 151, 255
    border_color        =  78,  78,  78, 255

    t_color = dearpygui_internal.color

    # Color: "Core"
    t_color.border                             = border_color
    t_color.border_shadow                      = border_color
    t_color.button                             = panel_color_idle
    t_color.button_active                      = panel_color_active
    t_color.button_hovered                     = panel_color_hovered
    t_color.check_mark                         = panel_color_active
    t_color.child_bg                           = bg_color_normal
    t_color.docking_empty_bg                   =  51,  51,  51, 255
    t_color.docking_preview                    = panel_color_active
    t_color.drag_drop_target                   = 255, 255,   0, 179
    t_color.frame_bg                           = panel_color_idle
    t_color.frame_bg_active                    = panel_color_active
    t_color.frame_bg_hovered                   = panel_color_hovered
    t_color.header                             = panel_color_idle
    t_color.header_active                      = panel_color_active
    t_color.header_hovered                     = panel_color_hovered
    t_color.menu_bar_bg                        = panel_color_idle
    t_color.modal_window_dim_bg                =  37,  37,  38, 250
    t_color.nav_highlight                      = bg_color_normal
    t_color.nav_windowing_dim_bg               = 204, 204, 204,  51
    t_color.nav_windowing_highlight            = 255, 255, 255, 179
    t_color.plot_histogram                     = panel_color_active
    t_color.plot_histogram_hovered             = panel_color_hovered
    t_color.plot_lines                         = panel_color_active
    t_color.plot_lines_hovered                 = panel_color_hovered
    t_color.popup_bg                           = bg_color_normal
    t_color.resize_grip                        = bg_color_normal
    t_color.resize_grip_active                 = panel_color_idle
    t_color.resize_grip_hovered                = bg_color_light
    t_color.scrollbar_bg                       = bg_color_normal
    t_color.scrollbar_grab                     = bg_color_light
    t_color.scrollbar_grab_active              = bg_color_bright
    t_color.scrollbar_grab_hovered             = bg_color_bright
    t_color.separator                          = border_color
    t_color.separator_active                   = border_color
    t_color.separator_hovered                  = border_color
    t_color.slider_grab                        = panel_color_hovered
    t_color.slider_grab_active                 = panel_color_active
    t_color.tab                                = panel_color_idle
    t_color.tab_active                         = panel_color_active
    t_color.tab_hovered                        = panel_color_hovered
    t_color.tab_unfocused                      = panel_color_idle
    t_color.tab_unfocused_active               = panel_color_active
    t_color.table_border_light                 =  59,  59,  64, 255
    t_color.table_border_strong                =  79,  79,  89, 255
    t_color.table_header_bg                    =  48,  48,  51, 255
    t_color.table_row_bg                       =   0,   0,   0,   0
    t_color.table_row_bg_alt                   = 255, 255, 255,  15
    t_color.text                               = text_color_enabled
    t_color.text_disabled                      = text_color_disabled
    t_color.text_selected_bg                   = panel_color_active
    t_color.title_bg                           = bg_color_normal
    t_color.title_bg_active                    =  15,  86, 135, 255
    t_color.title_bg_collapsed                 = bg_color_normal
    t_color.window_bg                          = bg_color_normal

    # Color: "Node"
    t_color.node_bg                            =  62,  62,  62, 255
    t_color.node_bg_hovered                    =  75,  75,  75, 255
    t_color.node_bg_selected                   =  75,  75,  75, 255
    t_color.node_box_selector                  =  61, 133, 224,  30
    t_color.node_box_selector_outline          =  61, 133, 224,  30
    t_color.node_grid_bg                       =  35,  35,  35, 255
    t_color.node_grid_line                     =   0,   0,   0, 255
    t_color.node_link                          = 255, 255, 255, 200
    t_color.node_link_hovered                  =  66, 150, 250, 255
    t_color.node_link_selected                 =  66, 150, 250, 255
    t_color.node_outline                       = 100, 100, 100, 255
    t_color.node_pin                           = 199, 199,  41, 255
    t_color.node_pin_hovered                   = 255, 255,  50, 255
    t_color.node_title_bar                     =  37,  37,  38, 255
    t_color.node_title_bar_hovered             =  75,  75,  75, 255
    t_color.node_title_bar_selected            =  75,  75,  75, 255
    t_color.node_grid_line_primary             = 240, 240, 240,  60
    t_color.node_minimap_bg                    =  25,  25,  25, 150
    t_color.node_minimap_bg_hovered            =  25,  25,  25, 200
    t_color.node_minimap_outline               = 150, 150, 150, 100
    t_color.node_minimap_outline_hovered       = 150, 150, 150, 200
    t_color.node_minimap_node_bg               = 200, 200, 200, 100
    t_color.node_minimap_node_bg_hovered       = 200, 200, 200, 255
    t_color.node_minimap_node_bg_selected      = 200, 200, 200, 255
    t_color.node_minimap_node_outline          = 200, 200, 200, 100
    t_color.node_minimap_link                  =  61, 133, 224, 200
    t_color.node_minimap_link_selected         =  66, 150, 250, 255
    t_color.node_minimap_canvas                = 200, 200, 200,  25
    t_color.node_minimap_canvas_outline        = 200, 200, 200, 200

    # Color: "Plot"
    t_color.plot_bg                            =   0,   0,   0, -255
    t_color.plot_border                        =   0,   0,   0, -255
    t_color.plot_crosshairs                    =   0,   0,   0, -255
    t_color.plot_error_bar                     =   0,   0,   0, -255
    t_color.plot_fill                          =   0,   0,   0, -255
    t_color.plot_frame_bg                      =   0,   0,   0, -255
    t_color.plot_inlay_text                    =   0,   0,   0, -255
    t_color.plot_legend_bg                     =   0,   0,   0, -255
    t_color.plot_legend_border                 =   0,   0,   0, -255
    t_color.plot_legend_text                   =   0,   0,   0, -255
    t_color.plot_line                          =   0,   0,   0, -255
    t_color.plot_marker_fill                   =   0,   0,   0, -255
    t_color.plot_marker_outline                =   0,   0,   0, -255
    t_color.plot_query                         =   0,   0,   0, -255
    t_color.plot_selection                     =   0,   0,   0, -255
    t_color.plot_title_text                    =   0,   0,   0, -255
    t_color.plot_x_axis                        =   0,   0,   0, -255
    t_color.plot_x_axis_grid                   =   0,   0,   0, -255
    t_color.plot_y_axis                        =   0,   0,   0, -255
    t_color.plot_y_axis2                       =   0,   0,   0, -255
    t_color.plot_y_axis3                       =   0,   0,   0, -255
    t_color.plot_y_axis_grid                   =   0,   0,   0, -255
    t_color.plot_y_axis_grid2                  =   0,   0,   0, -255
    t_color.plot_y_axis_grid3                  =   0,   0,   0, -255


    t_style = dearpygui_internal.style

    # Style: "Core"
    t_style.alpha                              = 1.0
    t_style.button_text_align                  = 0.5, 0.5
    t_style.cell_padding                       =   4,   2
    t_style.child_border_size                  =   1
    t_style.child_rounding                     =   0
    t_style.frame_border_size                  =   0
    t_style.frame_padding                      =   8,   3
    t_style.frame_rounding                     =   0
    t_style.grab_min_size                      =  10
    t_style.grab_rounding                      =   0
    t_style.indent_spacing                     =  21
    t_style.item_inner_spacing                 =   4,   4
    t_style.item_spacing                       =   8,   4
    t_style.popup_border_size                  =   1
    t_style.popup_rounding                     =   0
    t_style.scrollbar_rounding                 =   9
    t_style.scrollbar_size                     =  14
    t_style.selectable_text_align              = 0.0, 0.0
    t_style.tab_rounding                       =   4
    t_style.window_border_size                 =   1
    # t_style.window_min_size                    =
    t_style.window_padding                     =   8,   8
    t_style.window_rounding                    =   0
    t_style.window_title_align                 = 0.0, 0.5

    # Style: "Node"
    t_style.node_border_thickness              =   1
    t_style.node_corner_rounding               =   4
    t_style.node_grid_spacing                  =  32
    t_style.node_link_hover_distance           =  10
    t_style.node_link_line_segments_per_length =   0
    t_style.node_link_thickness                =   3
    t_style.node_padding                       =   8
    t_style.node_pin_circle_radius             =   4
    t_style.node_pin_hover_radius              =  10
    t_style.node_pin_line_thickness            =   1
    t_style.node_pin_offset                    =   0
    t_style.node_pin_quad_side_length          =   7
    t_style.node_pin_triangle_side_length      =  10
    t_style.node_minimap_padding               =   8,   8
    # t_style.node_minimap_offset                =   4, 0  DPG 1.6.1 not working

    # Style: "Plot"
    t_style.plot_annotation_padding            =   2,   2
    t_style.plot_border_size                   =   1
    t_style.plot_default_size                  = 400, 300
    t_style.plot_digital_bit_gap               = 4.0
    t_style.plot_digital_bit_height            = 8.0
    t_style.plot_error_bar_size                = 5.0
    t_style.plot_error_bar_weight              = 1.5
    t_style.plot_fill_alpha                    = 1.0
    t_style.plot_fit_padding                   =   0,   0
    t_style.plot_label_padding                 =   5,   5
    t_style.plot_legend_inner_padding          =   5,   5
    t_style.plot_legend_padding                =  10,  10
    t_style.plot_legend_spacing                =   5,   0
    t_style.plot_line_weight                   = 1.0
    t_style.plot_major_grid_size               = 1.0, 1.0
    t_style.plot_major_tick_len                =  10,  10
    t_style.plot_major_tick_size               = 1.0, 1.0
    t_style.plot_marker                        =   0
    t_style.plot_marker_size                   = 4.0
    t_style.plot_marker_weight                 = 1.0
    t_style.plot_min_size                      = 200, 150
    t_style.plot_minor_alpha                   = 0.25
    t_style.plot_minor_grid_size               = 1.0, 1.0
    t_style.plot_minor_tick_len                =   5,   5
    t_style.plot_minor_tick_size               = 1.0, 1.0
    t_style.plot_mouse_pos_padding             =  10,  10
    t_style.plot_padding                       =  10,  10



################################
#### Layout-Friendly Themes ####
################################

# Item-level themes allowing for maximum layout control.

with _theme_preset(label="Core - No Padding/Spacing") as dearpypixl_core_no_pad:
    """A theme preset where several Core-category style elements have values set to
    0. Useful when creating accurate layouts as these style elements would otherwise
    skew alignments.
    """
    t_core_style = dearpypixl_core_no_pad.style

    t_core_style.indent_spacing      =   0
    t_core_style.cell_padding        =   0,   0
    t_core_style.frame_padding       =   0,   0
    t_core_style.item_inner_spacing  =   0,   0
    t_core_style.item_spacing        =   0,   0
    t_core_style.window_padding      =   0,   0

with _theme_preset(label="Plotting - No Padding/Spacing") as dearpypixl_plot_no_pad:
    """A theme preset where several Plot-category style elements have values set to
    0. Useful when creating accurate layouts as these style elements would otherwise
    skew alignments.
    """
    t_plot_style = dearpypixl_plot_no_pad.style

    t_plot_style.plot_annotation_padding   =   0,   0
    t_plot_style.plot_fit_padding          =   0,   0
    t_plot_style.plot_label_padding        =   0,   0
    t_plot_style.plot_legend_inner_padding =   0,   0
    t_plot_style.plot_legend_padding       =   0,   0
    t_plot_style.plot_legend_spacing       =   0,   0
    t_plot_style.plot_mouse_pos_padding    =   0,   0
    t_plot_style.plot_padding              =   0,   0


_theme_presets = tuple(_theme_presets)
