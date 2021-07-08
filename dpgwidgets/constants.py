from enum import Enum

from . import idpg


## Input ##
class Key(Enum):
    Key0 = idpg.mvKey_0
    Key1 = idpg.mvKey_1
    Key2 = idpg.mvKey_2
    Key3 = idpg.mvKey_3
    Key4 = idpg.mvKey_4
    Key5 = idpg.mvKey_5
    Key6 = idpg.mvKey_6
    Key7 = idpg.mvKey_7
    Key8 = idpg.mvKey_8
    Key9 = idpg.mvKey_9
    Num0 = idpg.mvKey_NumPad0
    Num1 = idpg.mvKey_NumPad1
    Num2 = idpg.mvKey_NumPad2
    Num3 = idpg.mvKey_NumPad3
    Num4 = idpg.mvKey_NumPad4
    Num5 = idpg.mvKey_NumPad5
    Num6 = idpg.mvKey_NumPad6
    Num7 = idpg.mvKey_NumPad7
    Num8 = idpg.mvKey_NumPad8
    Num9 = idpg.mvKey_NumPad9
    A = idpg.mvKey_A
    B = idpg.mvKey_B
    C = idpg.mvKey_C
    D = idpg.mvKey_D
    E = idpg.mvKey_E
    F = idpg.mvKey_F
    G = idpg.mvKey_G
    H = idpg.mvKey_H
    I = idpg.mvKey_I
    J = idpg.mvKey_J
    K = idpg.mvKey_K
    L = idpg.mvKey_L
    M = idpg.mvKey_M
    N = idpg.mvKey_N
    O = idpg.mvKey_O
    P = idpg.mvKey_P
    Q = idpg.mvKey_Q
    R = idpg.mvKey_R
    S = idpg.mvKey_S
    T = idpg.mvKey_T
    U = idpg.mvKey_U
    V = idpg.mvKey_V
    W = idpg.mvKey_W
    X = idpg.mvKey_X
    Y = idpg.mvKey_Y
    Z = idpg.mvKey_Z
    F1 = idpg.mvKey_F1
    F2 = idpg.mvKey_F2
    F3 = idpg.mvKey_F3
    F4 = idpg.mvKey_F4
    F5 = idpg.mvKey_F5
    F6 = idpg.mvKey_F6
    F7 = idpg.mvKey_F7
    F8 = idpg.mvKey_F8
    F9 = idpg.mvKey_F9
    F10 = idpg.mvKey_F10
    F11 = idpg.mvKey_F11
    F12 = idpg.mvKey_F12
    F13 = idpg.mvKey_F13
    F14 = idpg.mvKey_F14
    F15 = idpg.mvKey_F15
    F16 = idpg.mvKey_F16
    F17 = idpg.mvKey_F17
    F18 = idpg.mvKey_F18
    F19 = idpg.mvKey_F19
    F20 = idpg.mvKey_F20
    F21 = idpg.mvKey_F21
    F22 = idpg.mvKey_F22
    F23 = idpg.mvKey_F23
    F24 = idpg.mvKey_F24
    Up = idpg.mvKey_Up
    Left = idpg.mvKey_Left
    Down = idpg.mvKey_Down
    Right = idpg.mvKey_Right
    Add = idpg.mvKey_Add
    Divide = idpg.mvKey_Divide
    Plus = idpg.mvKey_Plus
    Minus = idpg.mvKey_Minus
    Multiply = idpg.mvKey_Multiply
    Subtract = idpg.mvKey_Subtract
    Alt = idpg.mvKey_Alt
    Apps = idpg.mvKey_Apps
    Back = idpg.mvKey_Back
    Backslash = idpg.mvKey_Backslash
    Browser_Back = idpg.mvKey_Browser_Back
    Browser_Favorites = idpg.mvKey_Browser_Favorites
    Browser_Forward = idpg.mvKey_Browser_Forward
    Browser_Home = idpg.mvKey_Browser_Home
    Browser_Refresh = idpg.mvKey_Browser_Refresh
    Browser_Search = idpg.mvKey_Browser_Search
    Browser_Stop = idpg.mvKey_Browser_Stop
    Caps_Lock = idpg.mvKey_Capital
    Clear = idpg.mvKey_Clear
    Close_Brace = idpg.mvKey_Close_Brace
    Colon = idpg.mvKey_Colon
    Comma = idpg.mvKey_Comma
    Control = idpg.mvKey_Control
    Decimal = idpg.mvKey_Decimal
    Delete = idpg.mvKey_Delete
    End = idpg.mvKey_End
    Escape = idpg.mvKey_Escape
    Execute = idpg.mvKey_Execute
    Help = idpg.mvKey_Help
    Home = idpg.mvKey_Home
    Insert = idpg.mvKey_Insert
    L_Control = idpg.mvKey_LControl
    L_Menu = idpg.mvKey_LMenu
    L_Shift = idpg.mvKey_LShift
    L_Win = idpg.mvKey_LWin
    Next = idpg.mvKey_Next
    Num_Lock = idpg.mvKey_NumLock
    Open_Brace = idpg.mvKey_Open_Brace
    Pause = idpg.mvKey_Pause
    Period = idpg.mvKey_Period
    Print = idpg.mvKey_Print
    Print_Screen = idpg.mvKey_PrintScreen
    Prior = idpg.mvKey_Prior
    Quote = idpg.mvKey_Quote
    R_Control = idpg.mvKey_RControl
    R_Menu = idpg.mvKey_RMenu
    R_Shift = idpg.mvKey_RShift
    R_Win = idpg.mvKey_RWin
    Return = idpg.mvKey_Return
    Scroll_Lock = idpg.mvKey_ScrollLock
    Select = idpg.mvKey_Select
    Separator = idpg.mvKey_Separator
    Shift = idpg.mvKey_Shift
    Slash = idpg.mvKey_Slash
    Sleep = idpg.mvKey_Sleep
    Spacebar = idpg.mvKey_Spacebar
    Tab = idpg.mvKey_Tab
    Tilde = idpg.mvKey_Tilde
    Launch_App1 = idpg.mvKey_Launch_App1
    Launch_App2 = idpg.mvKey_Launch_App2
    Launch_Mail = idpg.mvKey_Launch_Mail
    Launch_Media_Select = idpg.mvKey_Launch_Media_Select
    Next_Track = idpg.mvKey_Media_Next_Track
    Play_Pause = idpg.mvKey_Media_Play_Pause
    Prev_Track = idpg.mvKey_Media_Prev_Track
    Stop = idpg.mvKey_Media_Stop
    Vol_Down = idpg.mvKey_Volume_Down
    Vol_Mute = idpg.mvKey_Volume_Mute
    Vol_Up = idpg.mvKey_Volume_Up


class Mouse(Enum):
    Left = idpg.mvMouseButton_Left
    Right = idpg.mvMouseButton_Right
    Middle = idpg.mvMouseButton_Middle
    Button1 = idpg.mvMouseButton_X1
    Button2 = idpg.mvMouseButton_X2


## Theming ##
THEMECOLOR = dict(
    border = (idpg.mvThemeCol_Border, idpg.mvThemeCat_Core),
    border_shadow = (idpg.mvThemeCol_BorderShadow, idpg.mvThemeCat_Core),
    button = (idpg.mvThemeCol_Button, idpg.mvThemeCat_Core),
    button_active = (idpg.mvThemeCol_ButtonActive, idpg.mvThemeCat_Core),
    button_hovered = (idpg.mvThemeCol_ButtonHovered, idpg.mvThemeCat_Core),
    check_mark = (idpg.mvThemeCol_CheckMark, idpg.mvThemeCat_Core),
    child_bg = (idpg.mvThemeCol_ChildBg, idpg.mvThemeCat_Core),
    docking_empty_bg = (idpg.mvThemeCol_DockingEmptyBg, idpg.mvThemeCat_Core),
    docking_preview = (idpg.mvThemeCol_DockingPreview, idpg.mvThemeCat_Core),
    drag_drop_target = (idpg.mvThemeCol_DragDropTarget, idpg.mvThemeCat_Core),
    frame_bg = (idpg.mvThemeCol_FrameBg, idpg.mvThemeCat_Core),
    frame_bg_active = (idpg.mvThemeCol_FrameBgActive, idpg.mvThemeCat_Core),
    frame_bg_hovered = (idpg.mvThemeCol_FrameBgHovered, idpg.mvThemeCat_Core),
    header = (idpg.mvThemeCol_Header, idpg.mvThemeCat_Core),
    header_active = (idpg.mvThemeCol_HeaderActive, idpg.mvThemeCat_Core),
    header_hovered = (idpg.mvThemeCol_HeaderHovered, idpg.mvThemeCat_Core),
    menu_bar_bg = (idpg.mvThemeCol_MenuBarBg, idpg.mvThemeCat_Core),
    modal_window_dim_bg = (
        idpg.mvThemeCol_ModalWindowDimBg, idpg.mvThemeCat_Core),
    nav_highlight = (idpg.mvThemeCol_NavHighlight, idpg.mvThemeCat_Core),
    nav_windowing_dim_bg = (
        idpg.mvThemeCol_NavWindowingDimBg, idpg.mvThemeCat_Core),
    nav_windowing_highlight = (
        idpg.mvThemeCol_NavWindowingHighlight, idpg.mvThemeCat_Core),
    plot_histogram = (idpg.mvThemeCol_PlotHistogram, idpg.mvThemeCat_Core),
    plot_histogram_hovered = (
        idpg.mvThemeCol_PlotHistogramHovered, idpg.mvThemeCat_Core),
    plot_lines = (idpg.mvThemeCol_PlotLines, idpg.mvThemeCat_Core),
    plot_lines_hovered = (
        idpg.mvThemeCol_PlotLinesHovered, idpg.mvThemeCat_Core),
    popup_bg = (idpg.mvThemeCol_PopupBg, idpg.mvThemeCat_Core),
    resize_grip = (idpg.mvThemeCol_ResizeGrip, idpg.mvThemeCat_Core),
    resize_grip_active = (
        idpg.mvThemeCol_ResizeGripActive, idpg.mvThemeCat_Core),
    resize_grip_hovered = (
        idpg.mvThemeCol_ResizeGripHovered, idpg.mvThemeCat_Core),
    scrollbar_bg = (idpg.mvThemeCol_ScrollbarBg, idpg.mvThemeCat_Core),
    scrollbar_grab = (idpg.mvThemeCol_ScrollbarGrab, idpg.mvThemeCat_Core),
    scrollbar_grab_active = (
        idpg.mvThemeCol_ScrollbarGrabActive, idpg.mvThemeCat_Core),
    scrollbar_grab_hovered = (
        idpg.mvThemeCol_ScrollbarGrabHovered, idpg.mvThemeCat_Core),
    separator = (idpg.mvThemeCol_Separator, idpg.mvThemeCat_Core),
    separator_active = (idpg.mvThemeCol_SeparatorActive, idpg.mvThemeCat_Core),
    separator_hovered = (idpg.mvThemeCol_SeparatorHovered,
                         idpg.mvThemeCat_Core),
    slider_grab = (idpg.mvThemeCol_SliderGrab, idpg.mvThemeCat_Core),
    slider_grab_active = (
        idpg.mvThemeCol_SliderGrabActive, idpg.mvThemeCat_Core),
    tab = (idpg.mvThemeCol_Tab, idpg.mvThemeCat_Core),
    tab_active = (idpg.mvThemeCol_TabActive, idpg.mvThemeCat_Core),
    tab_hovered = (idpg.mvThemeCol_TabHovered, idpg.mvThemeCat_Core),
    tab_unfocused = (idpg.mvThemeCol_TabUnfocused, idpg.mvThemeCat_Core),
    tab_unfocused_active = (
        idpg.mvThemeCol_TabUnfocusedActive, idpg.mvThemeCat_Core),
    table_border_light = (
        idpg.mvThemeCol_TableBorderLight, idpg.mvThemeCat_Core),
    table_border_strong = (
        idpg.mvThemeCol_TableBorderStrong, idpg.mvThemeCat_Core),
    table_header_bg = (idpg.mvThemeCol_TableHeaderBg, idpg.mvThemeCat_Core),
    table_row_bg = (idpg.mvThemeCol_TableRowBg, idpg.mvThemeCat_Core),
    table_row_bg_alt = (idpg.mvThemeCol_TableRowBgAlt, idpg.mvThemeCat_Core),
    text = (idpg.mvThemeCol_Text, idpg.mvThemeCat_Core),
    text_disabled = (idpg.mvThemeCol_TextDisabled, idpg.mvThemeCat_Core),
    text_selected_bg = (idpg.mvThemeCol_TextSelectedBg, idpg.mvThemeCat_Core),
    title_bg = (idpg.mvThemeCol_TitleBg, idpg.mvThemeCat_Core),
    title_bg_active = (idpg.mvThemeCol_TitleBgActive, idpg.mvThemeCat_Core),
    title_bg_collapsed = (
        idpg.mvThemeCol_TitleBgCollapsed, idpg.mvThemeCat_Core),
    window_bg = (idpg.mvThemeCol_WindowBg, idpg.mvThemeCat_Core),
    plot_crosshairs = (idpg.mvPlotCol_Crosshairs, idpg.mvThemeCat_Plots),
    plot_error_bar = (idpg.mvPlotCol_ErrorBar, idpg.mvThemeCat_Plots),
    plot_fill = (idpg.mvPlotCol_Fill, idpg.mvThemeCat_Plots),
    plot_frame_bg = (idpg.mvPlotCol_FrameBg, idpg.mvThemeCat_Plots),
    plot_inlay_text = (idpg.mvPlotCol_InlayText, idpg.mvThemeCat_Plots),
    plot_legend_bg = (idpg.mvPlotCol_LegendBg, idpg.mvThemeCat_Plots),
    plot_legend_border = (idpg.mvPlotCol_LegendBorder, idpg.mvThemeCat_Plots),
    plot_legend_text = (idpg.mvPlotCol_LegendText, idpg.mvThemeCat_Plots),
    plot_line = (idpg.mvPlotCol_Line, idpg.mvThemeCat_Plots),
    plot_marker_fill = (idpg.mvPlotCol_MarkerFill, idpg.mvThemeCat_Plots),
    plot_marker_outline = (idpg.mvPlotCol_MarkerOutline, idpg.mvThemeCat_Plots),
    plot_bg = (idpg.mvPlotCol_PlotBg, idpg.mvThemeCat_Plots),
    plot_border = (idpg.mvPlotCol_PlotBorder, idpg.mvThemeCat_Plots),
    plot_query = (idpg.mvPlotCol_Query, idpg.mvThemeCat_Plots),
    plot_selection = (idpg.mvPlotCol_Selection, idpg.mvThemeCat_Plots),
    plot_title_text = (idpg.mvPlotCol_TitleText, idpg.mvThemeCat_Plots),
    plot_x_axis = (idpg.mvPlotCol_XAxis, idpg.mvThemeCat_Plots),
    plot_x_axis_grid = (idpg.mvPlotCol_XAxisGrid, idpg.mvThemeCat_Plots),
    plot_y_axis = (idpg.mvPlotCol_YAxis, idpg.mvThemeCat_Plots),
    plot_y_axis2 = (idpg.mvPlotCol_YAxis2, idpg.mvThemeCat_Plots),
    plot_y_axis3 = (idpg.mvPlotCol_YAxis3, idpg.mvThemeCat_Plots),
    plot_y_axis_grid = (idpg.mvPlotCol_YAxisGrid, idpg.mvThemeCat_Plots),
    plot_y_axis_grid2 = (idpg.mvPlotCol_YAxisGrid2, idpg.mvThemeCat_Plots),
    plot_y_axis_grid3 = (idpg.mvPlotCol_YAxisGrid3, idpg.mvThemeCat_Plots),
    node_box_selector = (idpg.mvNodeCol_BoxSelector, idpg.mvThemeCat_Nodes),
    node_box_selector_outline = (
        idpg.mvNodeCol_BoxSelectorOutline, idpg.mvThemeCat_Nodes),
    node_grid_background = (
        idpg.mvNodeCol_GridBackground, idpg.mvThemeCat_Nodes),
    node_grid_line = (idpg.mvNodeCol_GridLine, idpg.mvThemeCat_Nodes),
    node_link = (idpg.mvNodeCol_Link, idpg.mvThemeCat_Nodes),
    node_link_hovered = (idpg.mvNodeCol_LinkHovered, idpg.mvThemeCat_Nodes),
    node_link_selected = (idpg.mvNodeCol_LinkSelected, idpg.mvThemeCat_Nodes),
    node_background = (idpg.mvNodeCol_NodeBackground, idpg.mvThemeCat_Nodes),
    node_background_hovered = (
        idpg.mvNodeCol_NodeBackgroundHovered, idpg.mvThemeCat_Nodes),
    node_background_selected = (
        idpg.mvNodeCol_NodeBackgroundSelected, idpg.mvThemeCat_Nodes),
    node_outline = (idpg.mvNodeCol_NodeOutline, idpg.mvThemeCat_Nodes),
    node_pin = (idpg.mvNodeCol_Pin, idpg.mvThemeCat_Nodes),
    node_pin_hovered = (idpg.mvNodeCol_PinHovered, idpg.mvThemeCat_Nodes),
    node_title_bar = (idpg.mvNodeCol_TitleBar, idpg.mvThemeCat_Nodes),
    node_title_bar_hovered = (
        idpg.mvNodeCol_TitleBarHovered, idpg.mvThemeCat_Nodes),
    node_title_bar_selected = (
        idpg.mvNodeCol_TitleBarSelected, idpg.mvThemeCat_Nodes),
)

THEMESTYLE = dict(
    alpha = (idpg.mvStyleVar_Alpha, idpg.mvThemeCat_Core),
    button_text_align = (idpg.mvStyleVar_ButtonTextAlign, idpg.mvThemeCat_Core),
    cell_padding = (idpg.mvStyleVar_CellPadding, idpg.mvThemeCat_Core),
    child_border_size = (idpg.mvStyleVar_ChildBorderSize, idpg.mvThemeCat_Core),
    child_rounding = (idpg.mvStyleVar_ChildRounding, idpg.mvThemeCat_Core),
    frame_border_size = (idpg.mvStyleVar_FrameBorderSize, idpg.mvThemeCat_Core),
    frame_padding = (idpg.mvStyleVar_FramePadding, idpg.mvThemeCat_Core),
    frame_rounding = (idpg.mvStyleVar_FrameRounding, idpg.mvThemeCat_Core),
    grab_min_size = (idpg.mvStyleVar_GrabMinSize, idpg.mvThemeCat_Core),
    grab_rounding = (idpg.mvStyleVar_GrabRounding, idpg.mvThemeCat_Core),
    indent_spacing = (idpg.mvStyleVar_IndentSpacing, idpg.mvThemeCat_Core),
    item_inner_spacing = (
        idpg.mvStyleVar_ItemInnerSpacing, idpg.mvThemeCat_Core),
    item_spacing = (idpg.mvStyleVar_ItemSpacing, idpg.mvThemeCat_Core),
    popup_border_size = (idpg.mvStyleVar_PopupBorderSize, idpg.mvThemeCat_Core),
    popup_rounding = (idpg.mvStyleVar_PopupRounding, idpg.mvThemeCat_Core),
    scrollbar_rounding = (
        idpg.mvStyleVar_ScrollbarRounding, idpg.mvThemeCat_Core),
    scrollbar_size = (idpg.mvStyleVar_ScrollbarSize, idpg.mvThemeCat_Core),
    selectable_text_align = (
        idpg.mvStyleVar_SelectableTextAlign, idpg.mvThemeCat_Core),
    tab_rounding = (idpg.mvStyleVar_TabRounding, idpg.mvThemeCat_Core),
    window_border_size = (
        idpg.mvStyleVar_WindowBorderSize, idpg.mvThemeCat_Core),
    window_min_size = (idpg.mvStyleVar_WindowMinSize, idpg.mvThemeCat_Core),
    window_padding = (idpg.mvStyleVar_WindowPadding, idpg.mvThemeCat_Core),
    window_rounding = (idpg.mvStyleVar_WindowRounding, idpg.mvThemeCat_Core),
    window_title_align = (
        idpg.mvStyleVar_WindowTitleAlign, idpg.mvThemeCat_Core),
    plot_annotation_padding = (
        idpg.mvPlotStyleVar_AnnotationPadding, idpg.mvThemeCat_Plots),
    plot_digital_bit_gap = (
        idpg.mvPlotStyleVar_DigitalBitGap, idpg.mvThemeCat_Plots),
    plot_digital_bit_height = (
        idpg.mvPlotStyleVar_DigitalBitHeight, idpg.mvThemeCat_Plots),
    plot_error_bar_size = (
        idpg.mvPlotStyleVar_ErrorBarSize, idpg.mvThemeCat_Plots),
    plot_error_bar_weight = (
        idpg.mvPlotStyleVar_ErrorBarWeight, idpg.mvThemeCat_Plots),
    plot_fill_alpha = (idpg.mvPlotStyleVar_FillAlpha, idpg.mvThemeCat_Plots),
    plot_fit_padding = (idpg.mvPlotStyleVar_FitPadding, idpg.mvThemeCat_Plots),
    plot_label_padding = (
        idpg.mvPlotStyleVar_LabelPadding, idpg.mvThemeCat_Plots),
    plot_legend_inner_padding = (
        idpg.mvPlotStyleVar_LegendInnerPadding, idpg.mvThemeCat_Plots),
    plot_legend_padding = (
        idpg.mvPlotStyleVar_LegendPadding, idpg.mvThemeCat_Plots),
    plot_legend_spacing = (
        idpg.mvPlotStyleVar_LegendSpacing, idpg.mvThemeCat_Plots),
    plot_line_weight = (idpg.mvPlotStyleVar_LineWeight, idpg.mvThemeCat_Plots),
    plot_major_grid_size = (
        idpg.mvPlotStyleVar_MajorGridSize, idpg.mvThemeCat_Plots),
    plot_major_tick_len = (
        idpg.mvPlotStyleVar_MajorTickLen, idpg.mvThemeCat_Plots),
    plot_major_tick_size = (
        idpg.mvPlotStyleVar_MajorTickSize, idpg.mvThemeCat_Plots),
    plot_marker = (idpg.mvPlotStyleVar_Marker, idpg.mvThemeCat_Plots),
    plot_marker_size = (idpg.mvPlotStyleVar_MarkerSize, idpg.mvThemeCat_Plots),
    plot_marker_weight = (
        idpg.mvPlotStyleVar_MarkerWeight, idpg.mvThemeCat_Plots),
    plot_minor_alpha = (idpg.mvPlotStyleVar_MinorAlpha, idpg.mvThemeCat_Plots),
    plot_minor_grid_size = (
        idpg.mvPlotStyleVar_MinorGridSize, idpg.mvThemeCat_Plots),
    plot_minor_tick_len = (
        idpg.mvPlotStyleVar_MinorTickLen, idpg.mvThemeCat_Plots),
    plot_minor_tick_size = (
        idpg.mvPlotStyleVar_MinorTickSize, idpg.mvThemeCat_Plots),
    plot_mouse_pos_padding = (
        idpg.mvPlotStyleVar_MousePosPadding, idpg.mvThemeCat_Plots),
    plot_border_size = (idpg.mvPlotStyleVar_PlotBorderSize,
                        idpg.mvThemeCat_Plots),
    plot_default_size = (
        idpg.mvPlotStyleVar_PlotDefaultSize, idpg.mvThemeCat_Plots),
    plot_min_size = (idpg.mvPlotStyleVar_PlotMinSize, idpg.mvThemeCat_Plots),
    plot_padding = (idpg.mvPlotStyleVar_PlotPadding, idpg.mvThemeCat_Plots),
    node_grid_spacing = (idpg.mvNodeStyleVar_GridSpacing,
                         idpg.mvThemeCat_Nodes),
    node_link_hover_distance = (
        idpg.mvNodeStyleVar_LinkHoverDistance, idpg.mvThemeCat_Nodes),
    node_link_line_segments_per_length = (
        idpg.mvNodeStyleVar_LinkLineSegmentsPerLength, idpg.mvThemeCat_Nodes),
    node_link_thickness = (
        idpg.mvNodeStyleVar_LinkThickness, idpg.mvThemeCat_Nodes),
    node_border_thickness = (
        idpg.mvNodeStyleVar_NodeBorderThickness, idpg.mvThemeCat_Nodes),
    node_corner_rounding = (
        idpg.mvNodeStyleVar_NodeCornerRounding, idpg.mvThemeCat_Nodes),
    node_padding_horizontal = (
        idpg.mvNodeStyleVar_NodePaddingHorizontal, idpg.mvThemeCat_Nodes),
    node_padding_vertical = (
        idpg.mvNodeStyleVar_NodePaddingVertical, idpg.mvThemeCat_Nodes),
    node_pin_circle_radius = (
        idpg.mvNodeStyleVar_PinCircleRadius, idpg.mvThemeCat_Nodes),
    node_pin_hover_radius = (
        idpg.mvNodeStyleVar_PinHoverRadius, idpg.mvThemeCat_Nodes),
    node_pin_line_thickness = (
        idpg.mvNodeStyleVar_PinLineThickness, idpg.mvThemeCat_Nodes),
    node_pin_offset = (idpg.mvNodeStyleVar_PinOffset, idpg.mvThemeCat_Nodes),
    node_pin_quad_side_length = (
        idpg.mvNodeStyleVar_PinQuadSideLength, idpg.mvThemeCat_Nodes),
    node_pin_triangle_side_length = (
        idpg.mvNodeStyleVar_PinTriangleSideLength, idpg.mvThemeCat_Nodes),
)