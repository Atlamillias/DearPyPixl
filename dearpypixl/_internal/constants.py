"""DearPyGui-related constants."""
from enum import IntEnum
from dearpygui import _dearpygui as dpg


APP_UUID = dpg.mvAppUUID
VP_UUID  = "DPG NOT USED YET"

NULL_THEME_UUID = 0
NULL_FONT_UUID  = 0

NONE    = -1
DEFAULT =  0


class Dir(IntEnum):
    NONE  = NONE
    LEFT  =  dpg.mvDir_Left
    RIGHT =  dpg.mvDir_Right
    UP    =  dpg.mvDir_Up
    DOWN  =  dpg.mvDir_Down


class NodeAttr(IntEnum):
    INPUT  = dpg.mvNode_Attr_Input
    OUTPUT = dpg.mvNode_Attr_Output
    STATIC = dpg.mvNode_Attr_Static


class NodePinShape(IntEnum):
    CIRCLE          = dpg.mvNode_PinShape_Circle
    FILLED_CIRCLE   = dpg.mvNode_PinShape_CircleFilled
    TRIANGLE        = dpg.mvNode_PinShape_Triangle
    FILLED_TRIANGLE = dpg.mvNode_PinShape_TriangleFilled
    QUAD            = dpg.mvNode_PinShape_Quad
    FILLED_QUAD     = dpg.mvNode_PinShape_QuadFilled


class NodeMinimapLoc(IntEnum):
    LOWER_LEFT  = dpg.mvNodeMiniMap_Location_BottomLeft
    LOWER_RIGHT = dpg.mvNodeMiniMap_Location_BottomRight
    UPPER_LEFT  = dpg.mvNodeMiniMap_Location_TopLeft
    UPPER_RIGHT = dpg.mvNodeMiniMap_Location_TopRight
    LL          = LOWER_LEFT
    LR          = LOWER_RIGHT
    UL          = UPPER_LEFT
    UR          = UPPER_RIGHT


class DatePickerLevel(IntEnum):
    DAY   = dpg.mvDatePickerLevel_Day
    MONTH = dpg.mvDatePickerLevel_Month
    YEAR  = dpg.mvDatePickerLevel_Year
    D     = DAY
    M     = MONTH
    Y     = YEAR


class PlotMarker(IntEnum):
    NONE     = NONE
    DEFAULT  = DEFAULT
    CIRCLE   = dpg.mvPlotMarker_Circle
    SQUARE   = dpg.mvPlotMarker_Square
    DIAMOND  = dpg.mvPlotMarker_Diamond
    UP       = dpg.mvPlotMarker_Up
    DOWN     = dpg.mvPlotMarker_Down
    LEFT     = dpg.mvPlotMarker_Left
    RIGHT    = dpg.mvPlotMarker_Right
    CROSS    = dpg.mvPlotMarker_Cross
    PLUS     = dpg.mvPlotMarker_Plus
    ASTERISK = dpg.mvPlotMarker_Asterisk


class PlotBin(IntEnum):
    SQRT    = dpg.mvPlotBin_Sqrt
    STURGES = dpg.mvPlotBin_Sturges
    RICE    = dpg.mvPlotBin_Rice
    SCOTT   = dpg.mvPlotBin_Scott


class PlotColormap(IntEnum):
    DEFAULT  = DEFAULT
    Deep     = dpg.mvPlotColormap_Deep
    Dark     = dpg.mvPlotColormap_Dark
    Pastel   = dpg.mvPlotColormap_Pastel
    Paired   = dpg.mvPlotColormap_Paired
    Viridis  = dpg.mvPlotColormap_Viridis
    Plasma   = dpg.mvPlotColormap_Plasma
    Hot      = dpg.mvPlotColormap_Hot
    Cool     = dpg.mvPlotColormap_Cool
    Pink     = dpg.mvPlotColormap_Pink
    Jet      = dpg.mvPlotColormap_Jet
    Twilight = dpg.mvPlotColormap_Twilight
    RdBu     = dpg.mvPlotColormap_RdBu
    BrBG     = dpg.mvPlotColormap_BrBG
    PiYG     = dpg.mvPlotColormap_PiYG
    Spectral = dpg.mvPlotColormap_Spectral
    Grey     = dpg.mvPlotColormap_Greys


class PlotLocation(IntEnum):
    CENTER    = dpg.mvPlot_Location_Center
    NORTH     = dpg.mvPlot_Location_North
    SOUTH     = dpg.mvPlot_Location_South
    WEST      = dpg.mvPlot_Location_West
    NORTHWEST = dpg.mvPlot_Location_NorthWest
    SOUTHWEST = dpg.mvPlot_Location_SouthWest
    EAST      = dpg.mvPlot_Location_East
    NORTHEAST = dpg.mvPlot_Location_NorthEast
    SOUTHEAST = dpg.mvPlot_Location_SouthEast
    N         = NORTH
    S         = SOUTH
    W         = WEST
    E         = EAST
    NW        = NORTHWEST
    SW        = SOUTHWEST
    NE        = NORTHEAST
    SE        = SOUTHEAST


class ColorEditType(IntEnum):
    FLOAT     = dpg.mvColorEdit_float
    HEX       = dpg.mvColorEdit_hex
    HSV       = dpg.mvColorEdit_hsv
    INPUT_HSV = dpg.mvColorEdit_input_hsv
    INPUT_RGB = dpg.mvColorEdit_input_rgb
    RGB       = dpg.mvColorEdit_rgb
    UINT_8    = dpg.mvColorEdit_uint8


class ColorEditAlphaPreview(IntEnum):
    FULL = dpg.mvColorEdit_AlphaPreview
    HALF = dpg.mvColorEdit_AlphaPreviewHalf
    NONE = dpg.mvColorEdit_AlphaPreviewNone


class ColorPickerInput(IntEnum):
    BAR   = dpg.mvColorPicker_bar
    WHEEL = dpg.mvColorPicker_wheel


class ComboHeight(IntEnum):
    SMALL  = dpg.mvComboHeight_Small
    MEDIUM = dpg.mvComboHeight_Regular
    LARGE  = dpg.mvComboHeight_Large
    XLARGE = dpg.mvComboHeight_Largest
    S      = SMALL
    M      = MEDIUM
    L      = LARGE
    XL     = XLARGE


class TabOrder(IntEnum):
    REORDERABLE = dpg.mvTabOrder_Reorderable
    FIXED       = dpg.mvTabOrder_Fixed
    LEADING     = dpg.mvTabOrder_Leading
    TRAILING    = dpg.mvTabOrder_Trailing


class TableSizing(IntEnum):
    FixedFit    = dpg.mvTable_SizingFixedFit
    FixedSame   = dpg.mvTable_SizingFixedSame
    StretchProp = dpg.mvTable_SizingStretchProp
    StretchSame = dpg.mvTable_SizingStretchSame


class Tool(IntEnum):
    ABOUT         = dpg.mvTool_About
    DEBUG         = dpg.mvTool_Debug
    DOC           = dpg.mvTool_Doc
    FONT          = dpg.mvTool_Font
    ITEM_REGISTRY = dpg.mvTool_ItemRegistry
    METRICS       = dpg.mvTool_Metrics
    STYLE         = dpg.mvTool_Style


class FormatFloat(IntEnum):
    RGB  = dpg.mvFormat_Float_rgb
    RGBA = dpg.mvFormat_Float_rgba


class FontRangeHint(IntEnum):
    DEFAULT                 = dpg.mvFontRangeHint_Default
    Japanese                = dpg.mvFontRangeHint_Japanese
    Korean                  = dpg.mvFontRangeHint_Korean
    ChineseFull             = dpg.mvFontRangeHint_Chinese_Full
    ChineseSimplifiedCommon = dpg.mvFontRangeHint_Chinese_Simplified_Common
    Cyrillic                = dpg.mvFontRangeHint_Cyrillic
    Thai                    = dpg.mvFontRangeHint_Thai
    Vietnamese              = dpg.mvFontRangeHint_Vietnamese
