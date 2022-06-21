from __future__ import annotations
from enum import Enum, IntEnum
from typing import NamedTuple
from dearpygui import _dearpygui as dpg
from dearpygui._dearpygui import mvThemeCat_Core, mvThemeCat_Nodes, mvThemeCat_Plots

# TODO: Finish cleanup (i.e. yeet this module)

class ItemIndex(IntEnum):
    ALL = 0
    ActivatedHandler = 119
    ActiveHandler = 115
    Annotation = 71
    AreaSeries = 88
    BarSeries = 76
    BoolValue = 141
    Button = 2
    CandleSeries = 87
    CharRemap = 135
    Checkbox = 26
    ChildWindow = 11
    ClickedHandler = 123
    Clipper = 21
    CollapsingHeader = 24
    ColorButton = 41
    ColorEdit = 20
    ColorMap = 150
    ColorMapButton = 152
    ColorMapRegistry = 151
    ColorMapScale = 89
    ColorMapSlider = 153
    ColorPicker = 22
    ColorValue = 145
    Combo = 29
    DatePicker = 40
    DeactivatedAfterEditHandler = 121
    DeactivatedHandler = 120
    Double4Value = 144
    DoubleValue = 143
    DragFloat = 16
    DragFloatMulti = 63
    DragInt = 17
    DragIntMulti = 64
    DragLine = 70
    DragPayload = 124
    DragPoint = 69
    DrawArrow = 51
    DrawBezierCubic = 55
    DrawBezierQuadratic = 56
    DrawCircle = 53
    DrawEllipse = 54
    DrawImage = 62
    DrawLayer = 98
    DrawLine = 50
    DrawPolygon = 60
    DrawPolyline = 61
    DrawQuad = 57
    DrawRect = 58
    DrawText = 59
    DrawTriangle = 52
    Drawlist = 32
    DynamicTexture = 96
    EditedHandler = 118
    ErrorSeries = 77
    FileDialog = 42
    FileExtension = 100
    FilterSet = 15
    Float4Value = 139
    FloatValue = 138
    FloatVectValue = 146
    FocusHandler = 116
    Font = 126
    FontAtlas = 2
    FontChars = 134
    FontRange = 133
    FontRegistry = 127
    Group = 12
    HLineSeries = 79
    HandlerRegistry = 103
    HeatSeries = 80
    HistogramSeries = 85
    HistogramSeries2D = 86
    HoverHandler = 114
    Image = 6
    ImageButton = 38
    ImageSeries = 81
    InputFloat = 18
    InputFloatMulti = 68
    InputInt = 19
    InputIntMulti = 67
    InputText = 1
    Int4Value = 140
    IntValue = 137
    ItemHandlerRegistry = 158
    ItemPool = 154
    ItemSet = 155
    KeyDownHandler = 104
    KeyPressHandler = 105
    KeyReleaseHandler = 106
    KnobFloat = 91
    LabelSeries = 84
    LineSeries = 72
    Listbox = 27
    LoadingIndicator = 92
    Menu = 9
    MenuBar = 7
    MenuItem = 10
    MouseClickHandler = 109
    MouseDoubleClickHandler = 110
    MouseDownHandler = 111
    MouseDragHandler = 113
    MouseMoveHandler = 107
    MouseReleaseHandler = 112
    MouseWheelHandler = 108
    Node = 45
    NodeAttribute = 46
    NodeEditor = 44
    NodeLink = 93
    PieSeries = 82
    Plot = 30
    PlotAxis = 102
    PlotLegend = 101
    ProgressBar = 36
    RadioButton = 3
    RawTexture = 148
    ResizeHandler = 125
    ScatterSeries = 73
    Selectable = 34
    Separator = 25
    SeriesValue = 147
    ShadeSeries = 83
    SimplePlot = 31
    Slider3D = 90
    SliderFloat = 13
    SliderFloatMulti = 65
    SliderInt = 14
    SliderIntMulti = 66
    Spacer = 37
    Stage = 97
    StairSeries = 75
    StaticTexture = 95
    StemSeries = 74
    StringValue = 142
    SubPlots = 149
    Tab = 5
    TabBar = 4
    TabButton = 43
    Table = 47
    TableCell = 157
    TableColumn = 48
    TableRow = 49
    TemplateRegistry = 156
    Text = 28
    TextureRegistry = 94
    Theme = 128
    ThemeColor = 129
    ThemeComponent = 131
    ThemeStyle = 130
    TimePicker = 39
    ToggledOpenHandler = 122
    Tooltip = 23
    TreeNode = 35
    VLineSeries = 78
    ValueRegistry = 136
    ViewportDrawlist = 99
    ViewportMenuBar = 8
    VisibleHandler = 117
    Window = 33
    XAxis = 0
    YAxis = 1


#############################
########## Theming ##########
#############################
class ThemeElementType(NamedTuple):
    """Contains information on DearPyGui theming elements.

    Args:
        * category (int): DearPyGui `mvThemeCat` constant value.
        * element_type (int): Integer index of the target's type (color = 0, style = 1).
        * target (int): DearPyGui's `ThemeCol`/`StyleVar` constant value for the item.
        * components (int): The number of values the target uses. Ranges from 1 to 4.
        * value_type (int): The object that all `values` must be instances of.
        * value_min (int): The floor of every value supported by `target`.
        * value_max (int): The ceiling of every value supported by `target`. A value of
        `...` or `None` indicates "no maximum".
    """
    category    : int
    element_type: int
    target      : int
    components  : int
    value_type  : type
    value_min   : int | float
    value_max   : int | float

class _ThemeCategoryT: ...  # type checking

THEME_COLOR = 0
THEME_STYLE = 1


class ThemeCategoryCore(_ThemeCategoryT, Enum):
    Text                  = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Text                 , 4 , int  , 0   , 255 )
    TextDisabled          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TextDisabled         , 4 , int  , 0   , 255 )
    WindowBg              = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_WindowBg             , 4 , int  , 0   , 255 )
    ChildBg               = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ChildBg              , 4 , int  , 0   , 255 )
    PopupBg               = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_PopupBg              , 4 , int  , 0   , 255 )
    Border                = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Border               , 4 , int  , 0   , 255 )
    BorderShadow          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_BorderShadow         , 4 , int  , 0   , 255 )
    FrameBg               = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_FrameBg              , 4 , int  , 0   , 255 )
    FrameBgHovered        = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_FrameBgHovered       , 4 , int  , 0   , 255 )
    FrameBgActive         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_FrameBgActive        , 4 , int  , 0   , 255 )
    TitleBg               = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TitleBg              , 4 , int  , 0   , 255 )
    TitleBgActive         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TitleBgActive        , 4 , int  , 0   , 255 )
    TitleBgCollapsed      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TitleBgCollapsed     , 4 , int  , 0   , 255 )
    MenuBarBg             = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_MenuBarBg            , 4 , int  , 0   , 255 )
    ScrollbarBg           = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ScrollbarBg          , 4 , int  , 0   , 255 )
    ScrollbarGrab         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ScrollbarGrab        , 4 , int  , 0   , 255 )
    ScrollbarGrabHovered  = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ScrollbarGrabHovered , 4 , int  , 0   , 255 )
    ScrollbarGrabActive   = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ScrollbarGrabActive  , 4 , int  , 0   , 255 )
    CheckMark             = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_CheckMark            , 4 , int  , 0   , 255 )
    SliderGrab            = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_SliderGrab           , 4 , int  , 0   , 255 )
    SliderGrabActive      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_SliderGrabActive     , 4 , int  , 0   , 255 )
    Button                = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Button               , 4 , int  , 0   , 255 )
    ButtonHovered         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ButtonHovered        , 4 , int  , 0   , 255 )
    ButtonActive          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ButtonActive         , 4 , int  , 0   , 255 )
    Header                = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Header               , 4 , int  , 0   , 255 )
    HeaderHovered         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_HeaderHovered        , 4 , int  , 0   , 255 )
    HeaderActive          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_HeaderActive         , 4 , int  , 0   , 255 )
    Separator             = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Separator            , 4 , int  , 0   , 255 )
    SeparatorHovered      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_SeparatorHovered     , 4 , int  , 0   , 255 )
    SeparatorActive       = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_SeparatorActive      , 4 , int  , 0   , 255 )
    ResizeGrip            = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ResizeGrip           , 4 , int  , 0   , 255 )
    ResizeGripHovered     = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ResizeGripHovered    , 4 , int  , 0   , 255 )
    ResizeGripActive      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ResizeGripActive     , 4 , int  , 0   , 255 )
    Tab                   = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_Tab                  , 4 , int  , 0   , 255 )
    TabHovered            = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TabHovered           , 4 , int  , 0   , 255 )
    TabActive             = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TabActive            , 4 , int  , 0   , 255 )
    TabUnfocused          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TabUnfocused         , 4 , int  , 0   , 255 )
    TabUnfocusedActive    = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TabUnfocusedActive   , 4 , int  , 0   , 255 )
    DockingPreview        = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_DockingPreview       , 4 , int  , 0   , 255 )
    DockingEmptyBg        = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_DockingEmptyBg       , 4 , int  , 0   , 255 )
    PlotLines             = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_PlotLines            , 4 , int  , 0   , 255 )
    PlotLinesHovered      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_PlotLinesHovered     , 4 , int  , 0   , 255 )
    PlotHistogram         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_PlotHistogram        , 4 , int  , 0   , 255 )
    PlotHistogramHovered  = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_PlotHistogramHovered , 4 , int  , 0   , 255 )
    TableHeaderBg         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TableHeaderBg        , 4 , int  , 0   , 255 )
    TableBorderStrong     = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TableBorderStrong    , 4 , int  , 0   , 255 )
    TableBorderLight      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TableBorderLight     , 4 , int  , 0   , 255 )
    TableRowBg            = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TableRowBg           , 4 , int  , 0   , 255 )
    TableRowBgAlt         = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TableRowBgAlt        , 4 , int  , 0   , 255 )
    TextSelectedBg        = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_TextSelectedBg       , 4 , int  , 0   , 255 )
    DragDropTarget        = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_DragDropTarget       , 4 , int  , 0   , 255 )
    NavHighlight          = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_NavHighlight         , 4 , int  , 0   , 255 )
    NavWindowingHighlight = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_NavWindowingHighlight, 4 , int  , 0   , 255 )
    NavWindowingDimBg     = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_NavWindowingDimBg    , 4 , int  , 0   , 255 )
    ModalWindowDimBg      = ThemeElementType(mvThemeCat_Core, THEME_COLOR, dpg.mvThemeCol_ModalWindowDimBg     , 4 , int  , 0   , 255 )
    Alpha                 = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_Alpha                , 1 , float, 0.0 , 1.0 )
    WindowPadding         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_WindowPadding        , 2 , int  , 0   , 20  )
    WindowRounding        = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_WindowRounding       , 1 , int  , 0   , 12  )
    WindowBorderSize      = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_WindowBorderSize     , 1 , int  , 0   , None)
    WindowMinSize         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_WindowMinSize        , 2 , int  , 0   , 20  )
    WindowTitleAlign      = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_WindowTitleAlign     , 2 , float, 0.0 , 1.0 )
    ChildRounding         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ChildRounding        , 1 , int  , 0   , 12  )
    ChildBorderSize       = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ChildBorderSize      , 1 , int  , 0   , None)
    PopupRounding         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_PopupRounding        , 1 , int  , 0   , 12  )
    PopupBorderSize       = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_PopupBorderSize      , 1 , int  , 0   , None)
    FramePadding          = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_FramePadding         , 2 , int  , 0   , 20  )
    FrameRounding         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_FrameRounding        , 1 , int  , 0   , 12  )
    FrameBorderSize       = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_FrameBorderSize      , 1 , int  , 0   , None)
    ItemSpacing           = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ItemSpacing          , 2 , int  , 0   , 20  )
    ItemInnerSpacing      = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ItemInnerSpacing     , 2 , int  , 0   , 20  )
    IndentSpacing         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_IndentSpacing        , 1 , int  , 0   , 30  )
    CellPadding           = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_CellPadding          , 2 , int  , 0   , 20  )
    ScrollbarSize         = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ScrollbarSize        , 1 , int  , 0   , 20  )
    ScrollbarRounding     = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ScrollbarRounding    , 1 , int  , 0   , 12  )
    GrabMinSize           = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_GrabMinSize          , 1 , int  , 0   , 20  )
    GrabRounding          = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_GrabRounding         , 1 , int  , 0   , 12  )
    TabRounding           = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_TabRounding          , 1 , int  , 0   , 12  )
    ButtonTextAlign       = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_ButtonTextAlign      , 2 , float, 0.0 , 1.0 )
    SelectableTextAlign   = ThemeElementType(mvThemeCat_Core, THEME_STYLE, dpg.mvStyleVar_SelectableTextAlign  , 2 , float, 0.0 , 1.0 )


class ThemeCategoryPlot(_ThemeCategoryT, Enum):
    Line               = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_Line, 4 , int , 0 , 255 )
    Fill               = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_Fill, 4 , int , 0 , 255 )
    MarkerOutline      = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_MarkerOutline, 4 , int , 0 , 255 )
    MarkerFill         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_MarkerFill, 4 , int , 0 , 255 )
    ErrorBar           = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_ErrorBar, 4 , int , 0 , 255 )
    FrameBg            = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_FrameBg, 4 , int , 0 , 255 )
    PlotBg             = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_PlotBg, 4 , int , 0 , 255 )
    PlotBorder         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_PlotBorder, 4 , int , 0 , 255 )
    LegendBg           = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_LegendBg, 4 , int , 0 , 255 )
    LegendBorder       = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_LegendBorder, 4 , int , 0 , 255 )
    LegendText         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_LegendText, 4 , int , 0 , 255 )
    TitleText          = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_TitleText, 4 , int , 0 , 255 )
    InlayText          = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_InlayText, 4 , int , 0 , 255 )
    XAxis              = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_XAxis, 4 , int , 0 , 255 )
    XAxisGrid          = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_XAxisGrid, 4 , int , 0 , 255 )
    YAxis              = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxis, 4 , int , 0 , 255 )
    YAxisGrid          = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxisGrid, 4 , int , 0 , 255 )
    YAxis2             = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxis2, 4 , int , 0 , 255 )
    YAxisGrid2         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxisGrid2, 4 , int , 0 , 255 )
    YAxis3             = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxis3, 4 , int , 0 , 255 )
    YAxisGrid3         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_YAxisGrid3, 4 , int , 0 , 255 )
    Selection          = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_Selection, 4 , int , 0 , 255 )
    Query              = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_Query, 4 , int , 0 , 255 )
    Crosshairs         = ThemeElementType(mvThemeCat_Plots, THEME_COLOR, dpg.mvPlotCol_Crosshairs, 4 , int , 0 , 255 )
    LineWeight         = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_LineWeight,  1 , float, 0.0 , 5.0 )
    Marker             = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_Marker, 1 , float, 0.0 , None )
    MarkerSize         = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MarkerSize, 1 , float, 0.0 , 10.0 )
    MarkerWeight       = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MarkerWeight, 1 , float, 0.0 , 5.0 )
    FillAlpha          = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_FillAlpha, 1 , float, 0.0 , 1.0 )
    ErrorBarSize       = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_ErrorBarSize, 1 , float, 0.0 , 10.0 )
    ErrorBarWeight     = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_ErrorBarWeight, 1 , float, 0.0 , 5.0 )
    DigitalBitHeight   = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_DigitalBitHeight , 1 , float, 0.0 , 20.0 )
    DigitalBitGap      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_DigitalBitGap, 1 , float, 0.0 , 20.0 )
    PlotBorderSize     = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_PlotBorderSize, 1 , float, 0.0 , 2.0 )
    MinorAlpha         = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MinorAlpha, 1 , float, 0.0 , 1.0 )
    MajorTickLen       = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MajorTickLen, 2 , float, 0.0 , 20.0 )
    MinorTickLen       = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MinorTickLen, 2 , float, 0.0 , 20.0 )
    MajorTickSize      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MajorTickSize, 2 , float, 0.0 , 2.0 )
    MinorTickSize      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MinorTickSize, 2 , float, 0.0 , 2.0 )
    MajorGridSize      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MajorGridSize, 2 , float, 0.0 , 2.0 )
    MinorGridSize      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MinorGridSize, 2 , float, 0.0 , 2.0 )
    PlotPadding        = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_PlotPadding, 2 , float, 0.0 , 20.0 )
    LabelPadding       = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_LabelPadding, 2 , float, 0.0 , 20.0 )
    LegendPadding      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_LegendPadding, 2 , float, 0.0 , 20.0 )
    LegendInnerPadding = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_LegendInnerPadding, 2 , float, 0.0 , 10.0 )
    LegendSpacing      = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_LegendSpacing, 2 , float, 0.0 , 5.0 )
    MousePosPadding    = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_MousePosPadding, 2 , float, 0.0 , 20.0 )
    AnnotationPadding  = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_AnnotationPadding, 2 , float, 0.0 , 5.0 )
    FitPadding         = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_FitPadding, 2 , float, 0.0 , 0.2 )
    PlotDefaultSize    = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_PlotDefaultSize, 2 , int , 0.0 , 1000 )
    PlotMinSize        = ThemeElementType(mvThemeCat_Plots, THEME_STYLE, dpg.mvPlotStyleVar_PlotMinSize, 2 , int , 0.0 , 300 )


class ThemeCategoryNode(_ThemeCategoryT,  Enum):
    # BUG: I don't think it is intended to have both "mvNode" and "mvNodes" prefixes...
    NodeBackground                = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_NodeBackground                , 4 , int , 0 , 255 )
    NodeBackgroundHovered         = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_NodeBackgroundHovered         , 4 , int , 0 , 255 )
    NodeBackgroundSelected        = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_NodeBackgroundSelected        , 4 , int , 0 , 255 )
    NodeOutline                   = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_NodeOutline                   , 4 , int , 0 , 255 )
    TitleBar                      = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_TitleBar                      , 4 , int , 0 , 255 )
    TitleBarHovered               = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_TitleBarHovered               , 4 , int , 0 , 255 )
    TitleBarSelected              = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_TitleBarSelected              , 4 , int , 0 , 255 )
    Link                          = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_Link                          , 4 , int , 0 , 255 )
    LinkHovered                   = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_LinkHovered                   , 4 , int , 0 , 255 )
    LinkSelected                  = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_LinkSelected                  , 4 , int , 0 , 255 )
    Pin                           = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_Pin                           , 4 , int , 0 , 255 )
    PinHovered                    = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_PinHovered                    , 4 , int , 0 , 255 )
    BoxSelector                   = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_BoxSelector                   , 4 , int , 0 , 255 )
    BoxSelectorOutline            = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_BoxSelectorOutline            , 4 , int , 0 , 255 )
    GridBackground                = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_GridBackground                , 4 , int , 0 , 255 )
    GridLine                      = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodeCol_GridLine                      , 4 , int , 0 , 255 )
    GridLinePrimary               = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_GridLinePrimary              , 4 , int , 0 , 255 )
    MiniMapBackground             = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapBackground            , 4 , int , 0 , 255 )
    MiniMapBackgroundHovered      = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapBackgroundHovered     , 4 , int , 0 , 255 )
    MiniMapOutline                = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapOutline               , 4 , int , 0 , 255 )
    MiniMapOutlineHovered         = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapOutlineHovered        , 4 , int , 0 , 255 )
    MiniMapNodeBackground         = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapNodeBackground        , 4 , int , 0 , 255 )
    MiniMapNodeBackgroundHovered  = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapNodeBackgroundHovered , 4 , int , 0 , 255 )
    MiniMapNodeBackgroundSelected = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapNodeBackgroundSelected, 4 , int , 0 , 255 )
    MiniMapNodeOutline            = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapNodeOutline           , 4 , int , 0 , 255 )
    MiniMapLink                   = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapLink                  , 4 , int , 0 , 255 )
    MiniMapLinkSelected           = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapLinkSelected          , 4 , int , 0 , 255 )
    MiniMapCanvas                 = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapCanvas                , 4 , int , 0 , 255 )
    MiniMapCanvasOutline          = ThemeElementType(mvThemeCat_Nodes, THEME_COLOR, dpg.mvNodesCol_MiniMapCanvasOutline         , 4 , int , 0 , 255 )
    GridSpacing                   = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_GridSpacing              , 1 , float, 0.0 , None )
    NodeCornerRounding            = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_NodeCornerRounding       , 1 , float, 0.0 , None )
    NodePadding                   = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_NodePadding              , 1 , float, 0.0 , None )
    NodeBorderThickness           = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_NodeBorderThickness      , 1 , float, 0.0 , None )
    LinkThickness                 = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_LinkThickness            , 1 , float, 0.0 , None )
    LinkLineSegmentsPerLength     = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_LinkLineSegmentsPerLength, 1 , float, 0.0 , None )
    LinkHoverDistance             = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_LinkHoverDistance        , 1 , float, 0.0 , None )
    PinCircleRadius               = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinCircleRadius          , 1 , float, 0.0 , None )
    PinQuadSideLength             = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinQuadSideLength        , 1 , float, 0.0 , None )
    PinTriangleSideLength         = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinTriangleSideLength    , 1 , float, 0.0 , None )
    PinLineThickness              = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinLineThickness         , 1 , float, 0.0 , None )
    PinHoverRadius                = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinHoverRadius           , 1 , float, 0.0 , None )
    PinOffset                     = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodeStyleVar_PinOffset                , 1 , float, 0.0 , None )
    MiniMapPadding                = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodesStyleVar_MiniMapPadding          , 2 , float, 0.0 , None )
    MiniMapOffset                 = ThemeElementType(mvThemeCat_Nodes, THEME_STYLE, dpg.mvNodesStyleVar_MiniMapOffset           , 2 , float, 0.0 , None )

#############################
########### Misc. ###########
#############################

class Dir(IntEnum):
    NONE = -1
    Left = 0
    Right = 1
    Up = 2
    Down = 3


class NodeAttr(IntEnum):
    Input = 0
    Output = 1
    Static = 2


class NodePinShape(IntEnum):
    Circle = 0
    CircleFilled = 1
    Triangle = 2
    TriangleFilled = 3
    Quad = 4
    QuadFilled = 5


class NodeMinimapLoc(IntEnum):
    BottomLeft  = 0
    BottomRight = 1
    TopLeft     = 2
    TopRight    = 3


class DatePickerLevel(IntEnum):
    Day = 0
    Month = 1
    Year = 2


class PlotMarker(IntEnum):
    NONE = -1
    DEFAULT = 0
    Circle = 0
    Square = 1
    Diamond = 2
    Up = 3
    Down = 4
    Left = 5
    Right = 6
    Cross = 7
    Plus = 8
    Asterisk = 9


class PlotBin(IntEnum):
    Sqrt = -1
    Sturges = -2
    Rice = -3
    Scott = -4


class PlotColormap(IntEnum):
    DEFAULT = 0
    Deep = 0
    Dark = 1
    Pastel = 2
    Paired = 3
    Viridis = 4
    Plasma = 5
    Hot = 6
    Cool = 7
    Pink = 8
    Jet = 9
    Twilight = 10
    RdBu = 11  # rename
    BrBG = 12  # rename
    PiYG = 13  # rename
    Spectral = 14
    Grey = 15


class PlotLocation(IntEnum):
    Center = 0
    North = 1
    South = 2
    West = 4
    NorthWest = 5
    SouthWest = 6
    East = 8
    NorthEast = 9
    SouthEast = 10
    N = 1
    S = 2
    W = 4
    E = 8
    NW = 5
    SW = 6
    NE = 9
    SE = 10


class ColorEditType(IntEnum):
    FLOAT     = 16777216
    HEX       = 4194304
    HSV       = 2097152
    INPUT_HSV = 268435456
    INPUT_RGB = 134217728
    RGB       = 1048576
    UINT_8    = 8388608


class ColorEditorAlpha(IntEnum):
    Preview = 131072
    PreviewHalf = 262144
    PreviewNone = 0


class ColorPickerInput(IntEnum):
    Bar = 33554432
    Wheel = 67108864


class ReservedUUID(IntEnum):
    UUID_0 = 10
    UUID_1 = 11
    UUID_2 = 12
    UUID_3 = 13
    UUID_4 = 14
    UUID_5 = 15
    UUID_6 = 16
    UUID_7 = 17
    UUID_8 = 18
    UUID_9 = 19


class ComboHeight(IntEnum):
    Large = 2
    Largest = 3
    Regular = 1
    Small = 0


class TabOrder(IntEnum):
    Reorderable = 0
    Fixed = 1
    Leading = 2
    Trailing = 3


class TableSizing(IntEnum):
    FixedFit = 8192
    FixedSame = 16384
    StretchProp = 24576
    StretchSame = 32768


class Tool(IntEnum):
    About = 3
    Debug = 4
    Doc = 5
    Font = 9
    ItemRegistry = 6
    Metrics = 7
    Style = 8


class FormatFloat(IntEnum):
    RGB  = 1
    RGBA = 0


class FontRangeHint(IntEnum):
    DEFAULT = 0
    Japanese = 1
    Korean = 2
    ChineseFull = 3
    ChineseSimplifiedCommon = 4
    Cyrillic = 5
    Thai = 6
    Vietnamese = 7


class DefaultRegistries(Enum):
    Font = (dpg.add_font_registry, ReservedUUID.UUID_1.value)
    Event = (dpg.add_handler_registry, ReservedUUID.UUID_2.value)
    Texture = (dpg.add_texture_registry, ReservedUUID.UUID_3.value)
    Value = (dpg.add_value_registry, ReservedUUID.UUID_4.value)
    ColorMap = (dpg.add_colormap_registry, ReservedUUID.UUID_5.value)
    Template = (dpg.add_template_registry, ReservedUUID.UUID_6.value)

    @classmethod
    def setup_registries(cls):
        for value in cls.__members__.values():
            func, tag = value.value
            func(label=None, user_data=None, use_internal_label=True, tag=tag)

