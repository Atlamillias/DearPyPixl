import enum
from dearpygui import dearpygui


class Platform(enum.IntEnum):
    WINDOWS =  dearpygui.mvPlatform_Windows   # 0
    MAC     =  dearpygui.mvPlatform_Apple     # 1
    LINUX   =  dearpygui.mvPlatform_Linux     # 2
    OTHER   = -1

    @classmethod
    def _missing_(cls, value: object):
        if isinstance(value, int):
            return cls.OTHER
        return None


class MouseInput(enum.IntEnum):
    ANY        = -1
    LEFT   = L = dearpygui.mvMouseButton_Left    # 0
    RIGHT  = R = dearpygui.mvMouseButton_Right   # 1
    MIDDLE = M = dearpygui.mvMouseButton_Middle  # 2
    X1         = dearpygui.mvMouseButton_X1      # 3
    X2         = dearpygui.mvMouseButton_X2      # 4


class KeyInput(enum.IntEnum):
    ANY                      = -1
    BREAK                    = 3
    BACKSPACE                = 8
    TAB                      = 9
    CLEAR                    = 12
    RETURN = ENTER           = 13
    SHIFT                    = 16
    CTRL                     = 17
    ALT                      = 18
    PAUSE                    = 19
    CAPS_LOCK                = 20
    ESC                      = 27
    SPACEBAR = SPACE         = 32
    PAGE_UP = PG_UP          = 33
    PAGE_DN = PG_DN          = 34
    END                      = 35
    HOME                     = 36
    ARROW_LEFT               = 37
    ARROW_RIGHT              = 38
    ARROW_UP                 = 39
    ARROW_DN                 = 40
    SELECT                   = 41
    PRINT                    = 42
    EXEC                     = 43
    PRINTSCREEN = PRTSCR     = 44
    INSERT = INS             = 45
    DELETE = DEL             = 46
    HELP                     = 47
    DIGIT_0                  = 48
    DIGIT_1                  = 49
    DIGIT_2                  = 50
    DIGIT_3                  = 51
    DIGIT_4                  = 52
    DIGIT_5                  = 53
    DIGIT_6                  = 54
    DIGIT_7                  = 55
    DIGIT_8                  = 56
    DIGIT_9                  = 57
    A                        = 65
    B                        = 66
    C                        = 67
    D                        = 68
    E                        = 69
    F                        = 70
    G                        = 71
    H                        = 72
    I                        = 73
    J                        = 74
    K                        = 75
    L                        = 76
    M                        = 77
    N                        = 78
    O                        = 79
    P                        = 80
    Q                        = 81
    R                        = 82
    S                        = 83
    T                        = 84
    U                        = 85
    V                        = 86
    W                        = 87
    X                        = 88
    Y                        = 89
    Z                        = 90
    L_META = L_WIN           = 91
    R_META = R_WIN           = 92
    APPS                     = 93
    SLEEP                    = 95
    NUMPAD_0                 = 96
    NUMPAD_1                 = 97
    NUMPAD_2                 = 98
    NUMPAD_3                 = 99
    NUMPAD_4                 = 100
    NUMPAD_5                 = 101
    NUMPAD_6                 = 102
    NUMPAD_7                 = 103
    NUMPAD_8                 = 104
    NUMPAD_9                 = 105
    NUMPAD_MUL               = 106
    NUMPAD_ADD               = 107
    NUMPAD_SEP               = 108
    NUMPAD_SUB               = 109
    NUMPAD_DEC               = 110
    NUMPAD_DIV               = 111
    F1                       = 112
    F2                       = 113
    F3                       = 114
    F4                       = 115
    F5                       = 116
    F6                       = 117
    F7                       = 118
    F8                       = 119
    F9                       = 120
    F10                      = 121
    F11                      = 122
    F12                      = 123
    F13                      = 124
    F14                      = 125
    F15                      = 126
    F16                      = 127
    F17                      = 128
    F18                      = 129
    F19                      = 130
    F20                      = 131
    F21                      = 132
    F22                      = 133
    F23                      = 134
    F24                      = 135
    NUM_LOCK                 = 144
    SCR_LOCK                 = 145
    L_SHIFT                  = 160
    R_SHIFT                  = 161
    L_CTRL                   = 162
    R_CTRL                   = 163
    L_MENU                   = 164
    R_MENU                   = 165
    BROWSER_BACK             = 166
    BROWSER_FORWARD          = 167
    BROWSER_REFRESH          = 168
    BROWSER_STOP             = 169
    BROWSER_SEARCH           = 170
    BROWSER_FAVS             = 171
    BROWSER_HOME             = 172
    VOL_MUTE                 = 173
    VOL_DN                   = 174
    VOL_UP                   = 175
    MEDIA_TRACK_NEXT         = 176
    MEDIA_TRACK_PREV         = 177
    MEDIA_STOP               = 178
    MEDIA_PLAY = MEDIA_PAUSE = 179
    LAUNCH_MAIL              = 180
    MEDIA_SELECT             = 181
    LAUNCH_APP1              = 182
    LAUNCH_APP2              = 183
    SEMICOLON                = 186
    PLUS                     = 187
    COMMA                    = 188
    MINUS                    = 189
    PERIOD                   = 190
    FORWARD_SLASH            = 191
    TILDE                    = 192  # ~
    BRACKET_OPEN             = 219  # [
    BACKSLASH                = 220  #
    BRACKET_CLOSE            = 221
    QUOTE                    = 222
    INTL_BACKSLASH           = 226  # \
    UNIDENTIFIED             = 255


class ThemeCategory(enum.IntEnum):
    CORE = dearpygui.mvThemeCat_Core   # 0
    PLOT = dearpygui.mvThemeCat_Plots  # 1
    NODE = dearpygui.mvThemeCat_Nodes  # 2


class NodeLink(enum.IntEnum):
    INPUT  = dearpygui.mvNode_Attr_Input
    OUTPUT = dearpygui.mvNode_Attr_Output
    STATIC = dearpygui.mvNode_Attr_Static


class NodeMiniMapLoc(enum.IntEnum):
    BOTTOM_LEFT  = BL = dearpygui.mvNodeMiniMap_Location_BottomLeft
    BOTTOM_RIGHT = BR = dearpygui.mvNodeMiniMap_Location_BottomRight
    TOP_RIGHT    = TR = dearpygui.mvNodeMiniMap_Location_TopRight
    TOP_LEFT     = TL = dearpygui.mvNodeMiniMap_Location_TopLeft


class PlotAxis(enum.IntEnum):
    X = dearpygui.mvXAxis
    Y = dearpygui.mvYAxis


class PlotLocation(enum.IntEnum):
    CENTER    = C  = dearpygui.mvPlot_Location_Center
    NORTH     = N  = dearpygui.mvPlot_Location_North
    NORTHEAST = NE = dearpygui.mvPlot_Location_NorthEast
    EAST      = E  = dearpygui.mvPlot_Location_East
    SOUTHEAST = SE = dearpygui.mvPlot_Location_SouthEast
    SOUTH     = S  = dearpygui.mvPlot_Location_South
    SOUTHWEST = SW = dearpygui.mvPlot_Location_SouthWest
    WEST      = W  = dearpygui.mvPlot_Location_West
    NORTHWEST = NW = dearpygui.mvPlot_Location_NorthWest


class TablePolicy(enum.IntEnum):
    FIXED_FIT    = dearpygui.mvTable_SizingFixedFit
    FIXED_SAME   = dearpygui.mvTable_SizingFixedSame
    STRETCH_PROP = dearpygui.mvTable_SizingStretchProp
    STRETCH_SAME = dearpygui.mvTable_SizingStretchSame


class ColorFormat(enum.IntEnum):
    RGBA = dearpygui.mvFormat_Float_rgba
    RGB  = dearpygui.mvFormat_Float_rgb


class PlotMarker(enum.IntEnum):
    NONE     = dearpygui.mvPlotMarker_None
    CIRCLE   = dearpygui.mvPlotMarker_Circle
    SQUARE   = dearpygui.mvPlotMarker_Square
    DIAMOND  = dearpygui.mvPlotMarker_Diamond
    UP       = dearpygui.mvPlotMarker_Up
    DOWN     = dearpygui.mvPlotMarker_Down
    LEFT     = dearpygui.mvPlotMarker_Left
    RIGHT    = dearpygui.mvPlotMarker_Right
    CROSS    = dearpygui.mvPlotMarker_Cross
    PLUS     = dearpygui.mvPlotMarker_Plus
    ASTERISK = dearpygui.mvPlotMarker_Asterisk


class PlotBin(enum.IntEnum):
    SQRT    = dearpygui.mvPlotBin_Sqrt
    STURGES = dearpygui.mvPlotBin_Sturges
    RICE    = dearpygui.mvPlotBin_Rice
    SCOTT   = dearpygui.mvPlotBin_Scott


class ColorEdit(enum.IntEnum):
    ALPHA_PREVIEW_NONE = dearpygui.mvColorEdit_AlphaPreviewNone
    ALPHA_PREVIEW      = dearpygui.mvColorEdit_AlphaPreview
    ALPHA_PREVIEW_HALF = dearpygui.mvColorEdit_AlphaPreviewHalf
    UINT8              = dearpygui.mvColorEdit_uint8
    FLOAT              = dearpygui.mvColorEdit_float
    RGB                = dearpygui.mvColorEdit_rgb
    HSV                = dearpygui.mvColorEdit_hsv
    HEX                = dearpygui.mvColorEdit_hex
    INPUT_RGB          = dearpygui.mvColorEdit_input_rgb
    INPUT_HSV          = dearpygui.mvColorEdit_input_hsv


class PlotColorMap(enum.IntEnum):
    DEFAULT  = dearpygui.mvPlotColormap_Default
    DEEP     = dearpygui.mvPlotColormap_Deep
    DARK     = dearpygui.mvPlotColormap_Dark
    PASTEL   = dearpygui.mvPlotColormap_Pastel
    PAIRED   = dearpygui.mvPlotColormap_Paired
    VIRIDIS  = dearpygui.mvPlotColormap_Viridis
    PLASMA   = dearpygui.mvPlotColormap_Plasma
    HOT      = dearpygui.mvPlotColormap_Hot
    COOL     = dearpygui.mvPlotColormap_Cool
    PINK     = dearpygui.mvPlotColormap_Pink
    JET      = dearpygui.mvPlotColormap_Jet
    TWILIGHT = dearpygui.mvPlotColormap_Twilight
    RDBU     = dearpygui.mvPlotColormap_RdBu
    BRBG     = dearpygui.mvPlotColormap_BrBG
    PIYG     = dearpygui.mvPlotColormap_PiYG
    SPECTRAL = dearpygui.mvPlotColormap_Spectral
    GREYS    = dearpygui.mvPlotColormap_Greys


class ColorPickerDisplay(enum.IntEnum):
    BAR   = dearpygui.mvColorPicker_bar
    WHEEL = dearpygui.mvColorPicker_wheel


class TabOrder(enum.IntEnum):
    REORDERABLE = dearpygui.mvTabOrder_Reorderable
    FIXED       = dearpygui.mvTabOrder_Fixed
    LEADING     = dearpygui.mvTabOrder_Leading
    TRAILING    = dearpygui.mvTabOrder_Trailing


class TimeUnit(enum.IntEnum):
    MICROSECOND = uS = dearpygui.mvTimeUnit_Us
    MILLISECOND = mS = dearpygui.mvTimeUnit_Ms
    SECOND      =  S = dearpygui.mvTimeUnit_S
    MINUTE      =  M = dearpygui.mvTimeUnit_Min
    HOUR        = HR = dearpygui.mvTimeUnit_Hr
    DAY              = dearpygui.mvTimeUnit_Day
    MONTH            = dearpygui.mvTimeUnit_Mo
    YEAR             = dearpygui.mvTimeUnit_Yr


class DatePickerLevel(enum.IntEnum):
    DAY   = dearpygui.mvDatePickerLevel_Day
    MONTH = dearpygui.mvDatePickerLevel_Month
    YEAR  = dearpygui.mvDatePickerLevel_Year


class CullMode(enum.IntEnum):
    NONE  = dearpygui.mvCullMode_None
    BACK  = dearpygui.mvCullMode_Back
    FRONT = dearpygui.mvCullMode_Front


class FontRangeHint(enum.IntEnum):
    DEFAULT                   = dearpygui.mvFontRangeHint_Default
    JAPANESE                  = dearpygui.mvFontRangeHint_Japanese
    KOREAN                    = dearpygui.mvFontRangeHint_Korean
    CHINESE_FULL              = dearpygui.mvFontRangeHint_Chinese_Full
    CHINESE_SIMPLIFIED_COMMON = dearpygui.mvFontRangeHint_Chinese_Simplified_Common
    CYRILLIC                  = dearpygui.mvFontRangeHint_Cyrillic
    THAI                      = dearpygui.mvFontRangeHint_Thai
    VIETNAMESE                = dearpygui.mvFontRangeHint_Vietnamese


class NodePinShape(enum.IntEnum):
    CIRCLE          = dearpygui.mvNode_PinShape_Circle
    CIRCLE_FILLED   = dearpygui.mvNode_PinShape_CircleFilled
    TRIANGLE        = dearpygui.mvNode_PinShape_Triangle
    TRIANGLE_FILLED = dearpygui.mvNode_PinShape_TriangleFilled
    QUAD            = dearpygui.mvNode_PinShape_Quad
    QUAD_FILLED     = dearpygui.mvNode_PinShape_QuadFilled


class Direction(enum.IntEnum):
    NONE  = dearpygui.mvDir_None
    LEFT  = dearpygui.mvDir_Left
    RIGHT = dearpygui.mvDir_Right
    UP    = dearpygui.mvDir_Up
    DOWN  = dearpygui.mvDir_Down


class ComboHeight(enum.IntEnum):
    SMALL   = dearpygui.mvComboHeight_Small
    REGULAR = dearpygui.mvComboHeight_Regular
    LARGE   = dearpygui.mvComboHeight_Large
    LARGEST = dearpygui.mvComboHeight_Largest


class GraphicsBackend(enum.IntEnum):
    D3D11 = DX11 = dearpygui.mvGraphicsBackend_D3D11
    D3D12 = DX12 = dearpygui.mvGraphicsBackend_D3D12
    VULKAN       = dearpygui.mvGraphicsBackend_VULKAN
    METAL        = dearpygui.mvGraphicsBackend_METAL
    OPENGL       = dearpygui.mvGraphicsBackend_OPENGL
