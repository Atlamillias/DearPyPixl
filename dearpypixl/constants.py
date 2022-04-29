from __future__ import annotations
from enum import Enum, IntEnum
from typing import Union, NamedTuple
from dearpygui import dearpygui, _dearpygui


InvalidUUID  = 0
AppUUID      = 1
ViewportUUID = "DPG NOT USED YET"


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
######### Key Codes #########
#############################
class Key(IntEnum):
    ANY = -1
    Break = 3
    Backspace = 8
    Tab = 9
    Clear = 12
    Return = 13
    Enter = 13
    Shift = 16
    Ctrl = 17
    Alt = 18
    Pause = 19
    CapsLock = 20
    Esc = 27
    Spacebar = 32
    PgUp = 33
    PgDn = 34
    End = 35
    Home = 36
    ArrowLeft = 37
    ArrowRight = 38
    ArrowUp = 39
    ArrowDn = 40
    Select = 41
    Print = 42
    Exec = 43
    PrtScr = 44
    Ins = 45
    Del = 46
    Help = 47
    Digit0 = 48
    Digit1 = 49
    Digit2 = 50
    Digit3 = 51
    Digit4 = 52
    Digit5 = 53
    Digit6 = 54
    Digit7 = 55
    Digit8 = 56
    Digit9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    L_Meta = 91
    R_Meta = 92
    L_Win = 91
    R_Win = 92
    Apps = 93
    Sleep = 95
    Numpad0 = 96
    Numpad1 = 97
    Numpad2 = 98
    Numpad3 = 99
    Numpad4 = 100
    Numpad5 = 101
    Numpad6 = 102
    Numpad7 = 103
    Numpad8 = 104
    Numpad9 = 105
    NumpadMultiply = 106
    NumpadAdd = 107
    NumpadSeparator = 108
    NumpadSubtract = 109
    NumpadDecimal = 110
    NumpadDivide = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    NumLock = 144
    ScrollLock = 145
    L_Shift = 160
    R_Shift = 161
    L_Ctrl = 162
    R_Ctrl = 163
    L_Menu = 164
    R_Menu = 165
    BrowserBack = 166
    BrowserForward = 167
    BrowserRefresh = 168
    BrowserStop = 169
    BrowserSearch = 170
    BrowserFavorites = 171
    BrowserHome = 172
    VolMute = 173
    VolDown = 174
    VolUp = 175
    MediaTrackNext = 176
    MediaTrackPrev = 177
    MediaStop = 178
    MediaPlayPause = 179
    LaunchMail = 180
    MediaSelect = 181
    LaunchApp1 = 182
    LaunchApp2 = 183  # calc on Win32
    Semicolon = 186
    Plus = 187
    Comma = 188
    Minus = 189
    Period = 190
    ForwardSlash = 191
    Tilde = 192
    BracketOpen = 219
    Backslash = 220
    BracketClose = 221
    Quote = 222
    IntlBackslash = 226  # \
    UNIDENTIFIED = 255

class Mouse(IntEnum):
    ANY = -1
    Left = 0
    Right = 1
    Middle = 2
    Button1 = 3
    Button2 = 4


#############################
########## Theming ##########
#############################
class ThemeElementTData(NamedTuple):
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
    value_min   : Union[int, float]
    value_max   : Union[int, float]

class _ThemeCategoryT: ...  # type checking

class ThemeCategoryCore(_ThemeCategoryT, Enum):
    # Color
    Text                      = ThemeElementTData(  0 ,   0 ,   0 ,   4 ,  int ,    0  ,   255  )
    TextDisabled              = ThemeElementTData(  0 ,   0 ,   1 ,   4 ,  int ,    0  ,   255  )
    WindowBg                  = ThemeElementTData(  0 ,   0 ,   2 ,   4 ,  int ,    0  ,   255  )
    ChildBg                   = ThemeElementTData(  0 ,   0 ,   3 ,   4 ,  int ,    0  ,   255  )
    PopupBg                   = ThemeElementTData(  0 ,   0 ,   4 ,   4 ,  int ,    0  ,   255  )
    Border                    = ThemeElementTData(  0 ,   0 ,   5 ,   4 ,  int ,    0  ,   255  )
    BorderShadow              = ThemeElementTData(  0 ,   0 ,   6 ,   4 ,  int ,    0  ,   255  )
    FrameBg                   = ThemeElementTData(  0 ,   0 ,   7 ,   4 ,  int ,    0  ,   255  )
    FrameBgHovered            = ThemeElementTData(  0 ,   0 ,   8 ,   4 ,  int ,    0  ,   255  )
    FrameBgActive             = ThemeElementTData(  0 ,   0 ,   9 ,   4 ,  int ,    0  ,   255  )
    TitleBg                   = ThemeElementTData(  0 ,   0 ,  10 ,   4 ,  int ,    0  ,   255  )
    TitleBgActive             = ThemeElementTData(  0 ,   0 ,  11 ,   4 ,  int ,    0  ,   255  )
    TitleBgCollapsed          = ThemeElementTData(  0 ,   0 ,  12 ,   4 ,  int ,    0  ,   255  )
    MenuBarBg                 = ThemeElementTData(  0 ,   0 ,  13 ,   4 ,  int ,    0  ,   255  )
    ScrollbarBg               = ThemeElementTData(  0 ,   0 ,  14 ,   4 ,  int ,    0  ,   255  )
    ScrollbarGrab             = ThemeElementTData(  0 ,   0 ,  15 ,   4 ,  int ,    0  ,   255  )
    ScrollbarGrabHovered      = ThemeElementTData(  0 ,   0 ,  16 ,   4 ,  int ,    0  ,   255  )
    ScrollbarGrabActive       = ThemeElementTData(  0 ,   0 ,  17 ,   4 ,  int ,    0  ,   255  )
    CheckMark                 = ThemeElementTData(  0 ,   0 ,  18 ,   4 ,  int ,    0  ,   255  )
    SliderGrab                = ThemeElementTData(  0 ,   0 ,  19 ,   4 ,  int ,    0  ,   255  )
    SliderGrabActive          = ThemeElementTData(  0 ,   0 ,  20 ,   4 ,  int ,    0  ,   255  )
    Button                    = ThemeElementTData(  0 ,   0 ,  21 ,   4 ,  int ,    0  ,   255  )
    ButtonHovered             = ThemeElementTData(  0 ,   0 ,  22 ,   4 ,  int ,    0  ,   255  )
    ButtonActive              = ThemeElementTData(  0 ,   0 ,  23 ,   4 ,  int ,    0  ,   255  )
    Header                    = ThemeElementTData(  0 ,   0 ,  24 ,   4 ,  int ,    0  ,   255  )
    HeaderHovered             = ThemeElementTData(  0 ,   0 ,  25 ,   4 ,  int ,    0  ,   255  )
    HeaderActive              = ThemeElementTData(  0 ,   0 ,  26 ,   4 ,  int ,    0  ,   255  )
    Separator                 = ThemeElementTData(  0 ,   0 ,  27 ,   4 ,  int ,    0  ,   255  )
    SeparatorHovered          = ThemeElementTData(  0 ,   0 ,  28 ,   4 ,  int ,    0  ,   255  )
    SeparatorActive           = ThemeElementTData(  0 ,   0 ,  29 ,   4 ,  int ,    0  ,   255  )
    ResizeGrip                = ThemeElementTData(  0 ,   0 ,  30 ,   4 ,  int ,    0  ,   255  )
    ResizeGripHovered         = ThemeElementTData(  0 ,   0 ,  31 ,   4 ,  int ,    0  ,   255  )
    ResizeGripActive          = ThemeElementTData(  0 ,   0 ,  32 ,   4 ,  int ,    0  ,   255  )
    Tab                       = ThemeElementTData(  0 ,   0 ,  33 ,   4 ,  int ,    0  ,   255  )
    TabHovered                = ThemeElementTData(  0 ,   0 ,  34 ,   4 ,  int ,    0  ,   255  )
    TabActive                 = ThemeElementTData(  0 ,   0 ,  35 ,   4 ,  int ,    0  ,   255  )
    TabUnfocused              = ThemeElementTData(  0 ,   0 ,  36 ,   4 ,  int ,    0  ,   255  )
    TabUnfocusedActive        = ThemeElementTData(  0 ,   0 ,  37 ,   4 ,  int ,    0  ,   255  )
    DockingPreview            = ThemeElementTData(  0 ,   0 ,  38 ,   4 ,  int ,    0  ,   255  )
    DockingEmptyBg            = ThemeElementTData(  0 ,   0 ,  39 ,   4 ,  int ,    0  ,   255  )
    PlotLines                 = ThemeElementTData(  0 ,   0 ,  40 ,   4 ,  int ,    0  ,   255  )
    PlotLinesHovered          = ThemeElementTData(  0 ,   0 ,  41 ,   4 ,  int ,    0  ,   255  )
    PlotHistogram             = ThemeElementTData(  0 ,   0 ,  42 ,   4 ,  int ,    0  ,   255  )
    PlotHistogramHovered      = ThemeElementTData(  0 ,   0 ,  43 ,   4 ,  int ,    0  ,   255  )
    TableHeaderBg             = ThemeElementTData(  0 ,   0 ,  44 ,   4 ,  int ,    0  ,   255  )
    TableBorderStrong         = ThemeElementTData(  0 ,   0 ,  45 ,   4 ,  int ,    0  ,   255  )
    TableBorderLight          = ThemeElementTData(  0 ,   0 ,  46 ,   4 ,  int ,    0  ,   255  )
    TableRowBg                = ThemeElementTData(  0 ,   0 ,  47 ,   4 ,  int ,    0  ,   255  )
    TableRowBgAlt             = ThemeElementTData(  0 ,   0 ,  48 ,   4 ,  int ,    0  ,   255  )
    TextSelectedBg            = ThemeElementTData(  0 ,   0 ,  49 ,   4 ,  int ,    0  ,   255  )
    DragDropTarget            = ThemeElementTData(  0 ,   0 ,  50 ,   4 ,  int ,    0  ,   255  )
    NavHighlight              = ThemeElementTData(  0 ,   0 ,  51 ,   4 ,  int ,    0  ,   255  )
    NavWindowingHighlight     = ThemeElementTData(  0 ,   0 ,  52 ,   4 ,  int ,    0  ,   255  )
    NavWindowingDimBg         = ThemeElementTData(  0 ,   0 ,  53 ,   4 ,  int ,    0  ,   255  )
    ModalWindowDimBg          = ThemeElementTData(  0 ,   0 ,  54 ,   4 ,  int ,    0  ,   255  )
    # Style
    Alpha                     = ThemeElementTData(  0 ,   1 ,   0 ,   1 , float,   0.0 ,   1.0  )
    WindowPadding             = ThemeElementTData(  0 ,   1 ,   1 ,   2 ,  int ,    0  ,   20   )
    WindowRounding            = ThemeElementTData(  0 ,   1 ,   2 ,   1 ,  int ,    0  ,   12   )
    WindowBorderSize          = ThemeElementTData(  0 ,   1 ,   3 ,   1 ,  int ,    0  ,   None )
    WindowMinSize             = ThemeElementTData(  0 ,   1 ,   4 ,   2 ,  int ,    0  ,   20   )
    WindowTitleAlign          = ThemeElementTData(  0 ,   1 ,   5 ,   2 , float,   0.0 ,   1.0  )
    ChildRounding             = ThemeElementTData(  0 ,   1 ,   6 ,   1 ,  int ,    0  ,   12   )
    ChildBorderSize           = ThemeElementTData(  0 ,   1 ,   7 ,   1 ,  int ,    0  ,   None )
    PopupRounding             = ThemeElementTData(  0 ,   1 ,   8 ,   1 ,  int ,    0  ,   12   )
    PopupBorderSize           = ThemeElementTData(  0 ,   1 ,   9 ,   1 ,  int ,    0  ,   None )
    FramePadding              = ThemeElementTData(  0 ,   1 ,  10 ,   2 ,  int ,    0  ,   20   )
    FrameRounding             = ThemeElementTData(  0 ,   1 ,  11 ,   1 ,  int ,    0  ,   12   )
    FrameBorderSize           = ThemeElementTData(  0 ,   1 ,  12 ,   1 ,  int ,    0  ,   None )
    ItemSpacing               = ThemeElementTData(  0 ,   1 ,  13 ,   2 ,  int ,    0  ,   20   )
    ItemInnerSpacing          = ThemeElementTData(  0 ,   1 ,  14 ,   2 ,  int ,    0  ,   20   )
    IndentSpacing             = ThemeElementTData(  0 ,   1 ,  15 ,   1 ,  int ,    0  ,   30   )
    CellPadding               = ThemeElementTData(  0 ,   1 ,  16 ,   2 ,  int ,    0  ,   20   )
    ScrollbarSize             = ThemeElementTData(  0 ,   1 ,  17 ,   1 ,  int ,    0  ,   20   )
    ScrollbarRounding         = ThemeElementTData(  0 ,   1 ,  18 ,   1 ,  int ,    0  ,   12   )
    GrabMinSize               = ThemeElementTData(  0 ,   1 ,  19 ,   1 ,  int ,    0  ,   20   )
    GrabRounding              = ThemeElementTData(  0 ,   1 ,  20 ,   1 ,  int ,    0  ,   12   )
    TabRounding               = ThemeElementTData(  0 ,   1 ,  21 ,   1 ,  int ,    0  ,   12   )
    ButtonTextAlign           = ThemeElementTData(  0 ,   1 ,  22 ,   2 , float,   0.0 ,   1.0  )
    SelectableTextAlign       = ThemeElementTData(  0 ,   1 ,  23 ,   2 , float,   0.0 ,   1.0  )


class ThemeCategoryPlot(_ThemeCategoryT, Enum):
    # Color
    Line                      = ThemeElementTData(  1 ,   0 ,   0 ,   4 ,  int ,    0  ,   255  )
    Fill                      = ThemeElementTData(  1 ,   0 ,   1 ,   4 ,  int ,    0  ,   255  )
    MarkerOutline             = ThemeElementTData(  1 ,   0 ,   2 ,   4 ,  int ,    0  ,   255  )
    MarkerFill                = ThemeElementTData(  1 ,   0 ,   3 ,   4 ,  int ,    0  ,   255  )
    ErrorBar                  = ThemeElementTData(  1 ,   0 ,   4 ,   4 ,  int ,    0  ,   255  )
    FrameBg                   = ThemeElementTData(  1 ,   0 ,   5 ,   4 ,  int ,    0  ,   255  )
    PlotBg                    = ThemeElementTData(  1 ,   0 ,   6 ,   4 ,  int ,    0  ,   255  )
    PlotBorder                = ThemeElementTData(  1 ,   0 ,   7 ,   4 ,  int ,    0  ,   255  )
    LegendBg                  = ThemeElementTData(  1 ,   0 ,   8 ,   4 ,  int ,    0  ,   255  )
    LegendBorder              = ThemeElementTData(  1 ,   0 ,   9 ,   4 ,  int ,    0  ,   255  )
    LegendText                = ThemeElementTData(  1 ,   0 ,  10 ,   4 ,  int ,    0  ,   255  )
    TitleText                 = ThemeElementTData(  1 ,   0 ,  11 ,   4 ,  int ,    0  ,   255  )
    InlayText                 = ThemeElementTData(  1 ,   0 ,  12 ,   4 ,  int ,    0  ,   255  )
    XAxis                     = ThemeElementTData(  1 ,   0 ,  13 ,   4 ,  int ,    0  ,   255  )
    XAxisGrid                 = ThemeElementTData(  1 ,   0 ,  14 ,   4 ,  int ,    0  ,   255  )
    YAxis                     = ThemeElementTData(  1 ,   0 ,  15 ,   4 ,  int ,    0  ,   255  )
    YAxisGrid                 = ThemeElementTData(  1 ,   0 ,  16 ,   4 ,  int ,    0  ,   255  )
    YAxis2                    = ThemeElementTData(  1 ,   0 ,  17 ,   4 ,  int ,    0  ,   255  )
    YAxisGrid2                = ThemeElementTData(  1 ,   0 ,  18 ,   4 ,  int ,    0  ,   255  )
    YAxis3                    = ThemeElementTData(  1 ,   0 ,  19 ,   4 ,  int ,    0  ,   255  )
    YAxisGrid3                = ThemeElementTData(  1 ,   0 ,  20 ,   4 ,  int ,    0  ,   255  )
    Selection                 = ThemeElementTData(  1 ,   0 ,  21 ,   4 ,  int ,    0  ,   255  )
    Query                     = ThemeElementTData(  1 ,   0 ,  22 ,   4 ,  int ,    0  ,   255  )
    Crosshairs                = ThemeElementTData(  1 ,   0 ,  23 ,   4 ,  int ,    0  ,   255  )
    # Style
    LineWeight                = ThemeElementTData(  1 ,   1 ,   0 ,   1 , float,   0.0 ,   5.0  )
    Marker                    = ThemeElementTData(  1 ,   1 ,   1 ,   1 , float,   0.0 ,  None  )
    MarkerSize                = ThemeElementTData(  1 ,   1 ,   2 ,   1 , float,   0.0 ,  10.0  )
    MarkerWeight              = ThemeElementTData(  1 ,   1 ,   3 ,   1 , float,   0.0 ,   5.0  )
    FillAlpha                 = ThemeElementTData(  1 ,   1 ,   4 ,   1 , float,   0.0 ,   1.0  )
    ErrorBarSize              = ThemeElementTData(  1 ,   1 ,   5 ,   1 , float,   0.0 ,  10.0  )
    ErrorBarWeight            = ThemeElementTData(  1 ,   1 ,   6 ,   1 , float,   0.0 ,   5.0  )
    DigitalBitHeight          = ThemeElementTData(  1 ,   1 ,   7 ,   1 , float,   0.0 ,  20.0  )
    DigitalBitGap             = ThemeElementTData(  1 ,   1 ,   8 ,   1 , float,   0.0 ,  20.0  )
    PlotBorderSize            = ThemeElementTData(  1 ,   1 ,   9 ,   1 , float,   0.0 ,   2.0  )
    MinorAlpha                = ThemeElementTData(  1 ,   1 ,  10 ,   1 , float,   0.0 ,   1.0  )
    MajorTickLen              = ThemeElementTData(  1 ,   1 ,  11 ,   2 , float,   0.0 ,  20.0  )
    MinorTickLen              = ThemeElementTData(  1 ,   1 ,  12 ,   2 , float,   0.0 ,  20.0  )
    MajorTickSize             = ThemeElementTData(  1 ,   1 ,  13 ,   2 , float,   0.0 ,   2.0  )
    MinorTickSize             = ThemeElementTData(  1 ,   1 ,  14 ,   2 , float,   0.0 ,   2.0  )
    MajorGridSize             = ThemeElementTData(  1 ,   1 ,  15 ,   2 , float,   0.0 ,   2.0  )
    MinorGridSize             = ThemeElementTData(  1 ,   1 ,  16 ,   2 , float,   0.0 ,   2.0  )
    PlotPadding               = ThemeElementTData(  1 ,   1 ,  17 ,   2 , float,   0.0 ,  20.0  )
    LabelPadding              = ThemeElementTData(  1 ,   1 ,  18 ,   2 , float,   0.0 ,  20.0  )
    LegendPadding             = ThemeElementTData(  1 ,   1 ,  19 ,   2 , float,   0.0 ,  20.0  )
    LegendInnerPadding        = ThemeElementTData(  1 ,   1 ,  20 ,   2 , float,   0.0 ,  10.0  )
    LegendSpacing             = ThemeElementTData(  1 ,   1 ,  21 ,   2 , float,   0.0 ,   5.0  )
    MousePosPadding           = ThemeElementTData(  1 ,   1 ,  22 ,   2 , float,   0.0 ,  20.0  )
    AnnotationPadding         = ThemeElementTData(  1 ,   1 ,  23 ,   2 , float,   0.0 ,   5.0  )
    FitPadding                = ThemeElementTData(  1 ,   1 ,  24 ,   2 , float,   0.0 ,   0.2  )
    PlotDefaultSize           = ThemeElementTData(  1 ,   1 ,  25 ,   2 ,  int ,   0.0 ,  1000  )
    PlotMinSize               = ThemeElementTData(  1 ,   1 ,  26 ,   2 ,  int ,   0.0 ,   300  )


class ThemeCategoryNode(_ThemeCategoryT, Enum):
    # Color
    NodeBackground                = ThemeElementTData(  2 ,   0 ,   0 ,   4 ,  int ,    0  ,   255  )
    NodeBackgroundHovered         = ThemeElementTData(  2 ,   0 ,   1 ,   4 ,  int ,    0  ,   255  )
    NodeBackgroundSelected        = ThemeElementTData(  2 ,   0 ,   2 ,   4 ,  int ,    0  ,   255  )
    NodeOutline                   = ThemeElementTData(  2 ,   0 ,   3 ,   4 ,  int ,    0  ,   255  )
    TitleBar                      = ThemeElementTData(  2 ,   0 ,   4 ,   4 ,  int ,    0  ,   255  )
    TitleBarHovered               = ThemeElementTData(  2 ,   0 ,   5 ,   4 ,  int ,    0  ,   255  )
    TitleBarSelected              = ThemeElementTData(  2 ,   0 ,   6 ,   4 ,  int ,    0  ,   255  )
    Link                          = ThemeElementTData(  2 ,   0 ,   7 ,   4 ,  int ,    0  ,   255  )
    LinkHovered                   = ThemeElementTData(  2 ,   0 ,   8 ,   4 ,  int ,    0  ,   255  )
    LinkSelected                  = ThemeElementTData(  2 ,   0 ,   9 ,   4 ,  int ,    0  ,   255  )
    Pin                           = ThemeElementTData(  2 ,   0 ,  10 ,   4 ,  int ,    0  ,   255  )
    PinHovered                    = ThemeElementTData(  2 ,   0 ,  11 ,   4 ,  int ,    0  ,   255  )
    BoxSelector                   = ThemeElementTData(  2 ,   0 ,  12 ,   4 ,  int ,    0  ,   255  )
    BoxSelectorOutline            = ThemeElementTData(  2 ,   0 ,  13 ,   4 ,  int ,    0  ,   255  )
    GridBackground                = ThemeElementTData(  2 ,   0 ,  14 ,   4 ,  int ,    0  ,   255  )
    GridLine                      = ThemeElementTData(  2 ,   0 ,  15 ,   4 ,  int ,    0  ,   255  )
    GridLinePrimary               = ThemeElementTData(  2 ,   0 ,  16 ,   4 ,  int ,    0  ,   255  )
    MiniMapBackground             = ThemeElementTData(  2 ,   0 ,  17 ,   4 ,  int ,    0  ,   255  )
    MiniMapBackgroundHovered      = ThemeElementTData(  2 ,   0 ,  18 ,   4 ,  int ,    0  ,   255  )
    MiniMapOutline                = ThemeElementTData(  2 ,   0 ,  19 ,   4 ,  int ,    0  ,   255  )
    MiniMapOutlineHovered         = ThemeElementTData(  2 ,   0 ,  20 ,   4 ,  int ,    0  ,   255  )
    MiniMapNodeBackground         = ThemeElementTData(  2 ,   0 ,  21 ,   4 ,  int ,    0  ,   255  )
    MiniMapNodeBackgroundHovered  = ThemeElementTData(  2 ,   0 ,  22 ,   4 ,  int ,    0  ,   255  )
    MiniMapNodeBackgroundSelected = ThemeElementTData(  2 ,   0 ,  23 ,   4 ,  int ,    0  ,   255  )
    MiniMapNodeOutline            = ThemeElementTData(  2 ,   0 ,  24 ,   4 ,  int ,    0  ,   255  )
    MiniMapLink                   = ThemeElementTData(  2 ,   0 ,  25 ,   4 ,  int ,    0  ,   255  )
    MiniMapLinkSelected           = ThemeElementTData(  2 ,   0 ,  26 ,   4 ,  int ,    0  ,   255  )
    MiniMapCanvas                 = ThemeElementTData(  2 ,   0 ,  27 ,   4 ,  int ,    0  ,   255  )
    MiniMapCanvasOutline          = ThemeElementTData(  2 ,   0 ,  28 ,   4 ,  int ,    0  ,   255  )
    # Style
    GridSpacing               = ThemeElementTData(  2 ,   1 ,   0 ,   1 , float,   0.0 ,  None  )
    NodeCornerRounding        = ThemeElementTData(  2 ,   1 ,   1 ,   1 , float,   0.0 ,  None  )
    NodePadding               = ThemeElementTData(  2 ,   1 ,   2 ,   1 , float,   0.0 ,  None  )
    NodeBorderThickness       = ThemeElementTData(  2 ,   1 ,   3 ,   1 , float,   0.0 ,  None  )
    LinkThickness             = ThemeElementTData(  2 ,   1 ,   4 ,   1 , float,   0.0 ,  None  )
    LinkLineSegmentsPerLength = ThemeElementTData(  2 ,   1 ,   5 ,   1 , float,   0.0 ,  None  )
    LinkHoverDistance         = ThemeElementTData(  2 ,   1 ,   6 ,   1 , float,   0.0 ,  None  )
    PinCircleRadius           = ThemeElementTData(  2 ,   1 ,   7 ,   1 , float,   0.0 ,  None  )
    PinQuadSideLength         = ThemeElementTData(  2 ,   1 ,   8 ,   1 , float,   0.0 ,  None  )
    PinTriangleSideLength     = ThemeElementTData(  2 ,   1 ,   9 ,   1 , float,   0.0 ,  None  )
    PinLineThickness          = ThemeElementTData(  2 ,   1 ,  10 ,   1 , float,   0.0 ,  None  )
    PinHoverRadius            = ThemeElementTData(  2 ,   1 ,  11 ,   1 , float,   0.0 ,  None  )
    PinOffset                 = ThemeElementTData(  2 ,   1 ,  12 ,   1 , float,   0.0 ,  None  )
    MiniMapPadding            = ThemeElementTData(  2 ,   1 ,  13 ,   2 , float,   0.0 ,  None  )
    MiniMapOffset             = ThemeElementTData(  2 ,   1 ,  14 ,   2 , float,   0.0 ,  None  )

#############################
########### Misc. ###########
#############################
class Platform(IntEnum):
    Windows = 0
    Linux   = 1
    MacOS   = 2


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
    Font = (_dearpygui.add_font_registry, ReservedUUID.UUID_1.value)
    Event = (_dearpygui.add_handler_registry, ReservedUUID.UUID_2.value)
    Texture = (_dearpygui.add_texture_registry, ReservedUUID.UUID_3.value)
    Value = (_dearpygui.add_value_registry, ReservedUUID.UUID_4.value)
    ColorMap = (_dearpygui.add_colormap_registry, ReservedUUID.UUID_5.value)
    Template = (_dearpygui.add_template_registry, ReservedUUID.UUID_6.value)

    @classmethod
    def setup_registries(cls):
        for value in cls.__members__.values():
            func, tag = value.value
            func(label=None, user_data=None, use_internal_label=True, tag=tag)


class DPIAwareness(IntEnum):
    Unaware = 0
    SystemAware = 1
    PerMonitorAware = 2





