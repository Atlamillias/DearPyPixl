
from . import Theme


with Theme(label="[Internal]") as _dpg_internal_theme:
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

    # Color: "Core"
    _dpg_internal_theme.border                             = border_color
    _dpg_internal_theme.border_shadow                      = border_color
    _dpg_internal_theme.button                             = panel_color_idle
    _dpg_internal_theme.button_active                      = panel_color_active
    _dpg_internal_theme.button_hovered                     = panel_color_hovered
    _dpg_internal_theme.check_mark                         = panel_color_active
    _dpg_internal_theme.child_bg                           = bg_color_normal
    _dpg_internal_theme.docking_empty_bg                   =  51,  51,  51, 255
    _dpg_internal_theme.docking_preview                    = panel_color_active
    _dpg_internal_theme.drag_drop_target                   = 255, 255,   0, 179
    _dpg_internal_theme.frame_bg                           = panel_color_idle
    _dpg_internal_theme.frame_bg_active                    = panel_color_active
    _dpg_internal_theme.frame_bg_hovered                   = panel_color_hovered
    _dpg_internal_theme.header                             = panel_color_idle
    _dpg_internal_theme.header_active                      = panel_color_active
    _dpg_internal_theme.header_hovered                     = panel_color_hovered
    _dpg_internal_theme.menu_bar_bg                        = panel_color_idle
    _dpg_internal_theme.modal_window_dim_bg                =  37,  37,  38, 250
    _dpg_internal_theme.nav_highlight                      = bg_color_normal
    _dpg_internal_theme.nav_windowing_dim_bg               = 204, 204, 204,  51
    _dpg_internal_theme.nav_windowing_highlight            = 255, 255, 255, 179
    _dpg_internal_theme.plot_histogram                     = panel_color_active
    _dpg_internal_theme.plot_histogram_hovered             = panel_color_hovered
    _dpg_internal_theme.plot_lines                         = panel_color_active
    _dpg_internal_theme.plot_lines_hovered                 = panel_color_hovered
    _dpg_internal_theme.popup_bg                           = bg_color_normal
    _dpg_internal_theme.resize_grip                        = bg_color_normal
    _dpg_internal_theme.resize_grip_active                 = panel_color_idle
    _dpg_internal_theme.resize_grip_hovered                = bg_color_light
    _dpg_internal_theme.scrollbar_bg                       = bg_color_normal
    _dpg_internal_theme.scrollbar_grab                     = bg_color_light
    _dpg_internal_theme.scrollbar_grab_active              = bg_color_bright
    _dpg_internal_theme.scrollbar_grab_hovered             = bg_color_bright
    _dpg_internal_theme.separator                          = border_color
    _dpg_internal_theme.separator_active                   = border_color
    _dpg_internal_theme.separator_hovered                  = border_color
    _dpg_internal_theme.slider_grab                        = panel_color_hovered
    _dpg_internal_theme.slider_grab_active                 = panel_color_active
    _dpg_internal_theme.tab                                = panel_color_idle
    _dpg_internal_theme.tab_active                         = panel_color_active
    _dpg_internal_theme.tab_hovered                        = panel_color_hovered
    _dpg_internal_theme.tab_unfocused                      = panel_color_idle
    _dpg_internal_theme.tab_unfocused_active               = panel_color_active
    _dpg_internal_theme.table_border_light                 =  59,  59,  64, 255
    _dpg_internal_theme.table_border_strong                =  79,  79,  89, 255
    _dpg_internal_theme.table_header_bg                    =  48,  48,  51, 255
    _dpg_internal_theme.table_row_bg                       =   0,   0,   0,   0
    _dpg_internal_theme.table_row_bg_alt                   = 255, 255, 255,  15
    _dpg_internal_theme.text                               = text_color_enabled
    _dpg_internal_theme.text_disabled                      = text_color_disabled
    _dpg_internal_theme.text_selected_bg                   = panel_color_active
    _dpg_internal_theme.title_bg                           = bg_color_normal
    _dpg_internal_theme.title_bg_active                    =  15,  86, 135, 255
    _dpg_internal_theme.title_bg_collapsed                 = bg_color_normal
    _dpg_internal_theme.window_bg                          = bg_color_normal
    # Color: "Node"
    _dpg_internal_theme.node_bg                            =  62,  62,  62, 255
    _dpg_internal_theme.node_bg_hovered                    =  75,  75,  75, 255
    _dpg_internal_theme.node_bg_selected                   =  75,  75,  75, 255
    _dpg_internal_theme.node_box_selector                  =  61, 133, 224,  30
    _dpg_internal_theme.node_box_selector_outline          =  61, 133, 224,  30
    _dpg_internal_theme.node_grid_bg                       =  35,  35,  35, 255
    _dpg_internal_theme.node_grid_line                     =   0,   0,   0, 255
    _dpg_internal_theme.node_link                          = 255, 255, 255, 200
    _dpg_internal_theme.node_link_hovered                  =  66, 150, 250, 255
    _dpg_internal_theme.node_link_selected                 =  66, 150, 250, 255
    _dpg_internal_theme.node_outline                       = 100, 100, 100, 255
    _dpg_internal_theme.node_pin                           = 199, 199,  41, 255
    _dpg_internal_theme.node_pin_hovered                   = 255, 255,  50, 255
    _dpg_internal_theme.node_title_bar                     =  37,  37,  38, 255
    _dpg_internal_theme.node_title_bar_hovered             =  75,  75,  75, 255
    _dpg_internal_theme.node_title_bar_selected            =  75,  75,  75, 255
    _dpg_internal_theme.node_grid_line_primary             = 240, 240, 240,  60
    _dpg_internal_theme.node_minimap_bg                    =  25,  25,  25, 150
    _dpg_internal_theme.node_minimap_bg_hovered            =  25,  25,  25, 200
    _dpg_internal_theme.node_minimap_outline               = 150, 150, 150, 100
    _dpg_internal_theme.node_minimap_outline_hovered       = 150, 150, 150, 200
    _dpg_internal_theme.node_minimap_node_bg               = 200, 200, 200, 100
    _dpg_internal_theme.node_minimap_node_bg_hovered       = 200, 200, 200, 255
    _dpg_internal_theme.node_minimap_node_bg_selected      = 200, 200, 200, 255
    _dpg_internal_theme.node_minimap_node_outline          = 200, 200, 200, 100
    _dpg_internal_theme.node_minimap_link                  =  61, 133, 224, 200
    _dpg_internal_theme.node_minimap_link_selected         =  66, 150, 250, 255
    _dpg_internal_theme.node_minimap_canvas                = 200, 200, 200,  25
    _dpg_internal_theme.node_minimap_canvas_outline        = 200, 200, 200, 200
    # Color: "Plot"
    _dpg_internal_theme.plot_bg                            =   0,   0,   0, -255
    _dpg_internal_theme.plot_border                        =   0,   0,   0, -255
    _dpg_internal_theme.plot_crosshairs                    =   0,   0,   0, -255
    _dpg_internal_theme.plot_error_bar                     =   0,   0,   0, -255
    _dpg_internal_theme.plot_fill                          =   0,   0,   0, -255
    _dpg_internal_theme.plot_frame_bg                      =   0,   0,   0, -255
    _dpg_internal_theme.plot_inlay_text                    =   0,   0,   0, -255
    _dpg_internal_theme.plot_legend_bg                     =   0,   0,   0, -255
    _dpg_internal_theme.plot_legend_border                 =   0,   0,   0, -255
    _dpg_internal_theme.plot_legend_text                   =   0,   0,   0, -255
    _dpg_internal_theme.plot_line                          =   0,   0,   0, -255
    _dpg_internal_theme.plot_marker_fill                   =   0,   0,   0, -255
    _dpg_internal_theme.plot_marker_outline                =   0,   0,   0, -255
    _dpg_internal_theme.plot_query                         =   0,   0,   0, -255
    _dpg_internal_theme.plot_selection                     =   0,   0,   0, -255
    _dpg_internal_theme.plot_title_text                    =   0,   0,   0, -255
    _dpg_internal_theme.plot_x_axis                        =   0,   0,   0, -255
    _dpg_internal_theme.plot_x_axis_grid                   =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis                        =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis2                       =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis3                       =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis_grid                   =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis_grid2                  =   0,   0,   0, -255
    _dpg_internal_theme.plot_y_axis_grid3                  =   0,   0,   0, -255


    # Style: "Core"
    _dpg_internal_theme.alpha                              = 1.0
    _dpg_internal_theme.button_text_align                  = 0.5, 0.5
    _dpg_internal_theme.cell_padding                       =   4,   2
    _dpg_internal_theme.child_border_size                  =   1
    _dpg_internal_theme.child_rounding                     =   0
    _dpg_internal_theme.frame_border_size                  =   0
    _dpg_internal_theme.frame_padding                      =   8,   3
    _dpg_internal_theme.frame_rounding                     =   0
    _dpg_internal_theme.grab_min_size                      =  10
    _dpg_internal_theme.grab_rounding                      =   0
    _dpg_internal_theme.indent_spacing                     =  21
    _dpg_internal_theme.item_inner_spacing                 =   4,   4
    _dpg_internal_theme.item_spacing                       =   8,   4
    _dpg_internal_theme.popup_border_size                  =   1
    _dpg_internal_theme.popup_rounding                     =   0
    _dpg_internal_theme.scrollbar_rounding                 =   9
    _dpg_internal_theme.scrollbar_size                     =  14
    _dpg_internal_theme.selectable_text_align              = 0.0, 0.0
    _dpg_internal_theme.tab_rounding                       =   4
    _dpg_internal_theme.window_border_size                 =   1
    # t_style.window_min_size                    =
    _dpg_internal_theme.window_padding                     =   8,   8
    _dpg_internal_theme.window_rounding                    =   0
    _dpg_internal_theme.window_title_align                 = 0.0, 0.5
    # Style: "Node"
    _dpg_internal_theme.node_border_thickness              =   1
    _dpg_internal_theme.node_corner_rounding               =   4
    _dpg_internal_theme.node_grid_spacing                  =  32
    _dpg_internal_theme.node_link_hover_distance           =  10
    _dpg_internal_theme.node_link_ln_segments_per_length   =   0
    _dpg_internal_theme.node_link_thickness                =   3
    _dpg_internal_theme.node_padding                       =   8
    _dpg_internal_theme.node_pin_circle_radius             =   4
    _dpg_internal_theme.node_pin_hover_radius              =  10
    _dpg_internal_theme.node_pin_line_thickness            =   1
    _dpg_internal_theme.node_pin_offset                    =   0
    _dpg_internal_theme.node_pin_quad_side_length          =   7
    _dpg_internal_theme.node_pin_tri_side_length           =  10
    _dpg_internal_theme.node_minimap_padding               =   8,   8
    # t_style.node_minimap_offset                =   4, 0  DPG 1.6.1 not working
    # Style: "Plot"
    _dpg_internal_theme.plot_annotation_padding            =   2,   2
    _dpg_internal_theme.plot_border_size                   =   1
    _dpg_internal_theme.plot_default_size                  = 400, 300
    _dpg_internal_theme.plot_digital_bit_gap               = 4.0
    _dpg_internal_theme.plot_digital_bit_height            = 8.0
    _dpg_internal_theme.plot_error_bar_size                = 5.0
    _dpg_internal_theme.plot_error_bar_weight              = 1.5
    _dpg_internal_theme.plot_fill_alpha                    = 1.0
    _dpg_internal_theme.plot_fit_padding                   =   0,   0
    _dpg_internal_theme.plot_label_padding                 =   5,   5
    _dpg_internal_theme.plot_legend_inner_padding          =   5,   5
    _dpg_internal_theme.plot_legend_padding                =  10,  10
    _dpg_internal_theme.plot_legend_spacing                =   5,   0
    _dpg_internal_theme.plot_line_weight                   = 1.0
    _dpg_internal_theme.plot_major_grid_size               = 1.0, 1.0
    _dpg_internal_theme.plot_major_tick_len                =  10,  10
    _dpg_internal_theme.plot_major_tick_size               = 1.0, 1.0
    _dpg_internal_theme.plot_marker                        =   0
    _dpg_internal_theme.plot_marker_size                   = 4.0
    _dpg_internal_theme.plot_marker_weight                 = 1.0
    _dpg_internal_theme.plot_min_size                      = 200, 150
    _dpg_internal_theme.plot_minor_alpha                   = 0.25
    _dpg_internal_theme.plot_minor_grid_size               = 1.0, 1.0
    _dpg_internal_theme.plot_minor_tick_len                =   5,   5
    _dpg_internal_theme.plot_minor_tick_size               = 1.0, 1.0
    _dpg_internal_theme.plot_mouse_pos_padding             =  10,  10
    _dpg_internal_theme.plot_padding                       =  10,  10


# with ThemePreset() as _core_zero_pad:
#     _core_zero_pad.indent_spacing      =   0
#     _core_zero_pad.cell_padding        =   0,   0
#     _core_zero_pad.frame_padding       =   0,   0
#     _core_zero_pad.item_inner_spacing  =   0,   0
#     _core_zero_pad.item_spacing        =   0,   0
#     _core_zero_pad.window_padding      =   0,   0
#
# with ThemePreset() as _plot_zero_pad:
#     _plot_zero_pad.plot_annotation_padding   =   0,   0
#     _plot_zero_pad.plot_fit_padding          =   0,   0
#     _plot_zero_pad.plot_label_padding        =   0,   0
#     _plot_zero_pad.plot_legend_inner_padding =   0,   0
#     _plot_zero_pad.plot_legend_padding       =   0,   0
#     _plot_zero_pad.plot_legend_spacing       =   0,   0
#     _plot_zero_pad.plot_mouse_pos_padding    =   0,   0
#     _plot_zero_pad.plot_padding              =   0,   0


