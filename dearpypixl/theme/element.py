from enum import Enum, IntEnum
from typing import Any, Literal, Sequence, NamedTuple
from decimal import Decimal
from dearpygui import _dearpygui, dearpygui
from dearpygui.dearpygui import add_theme_color, add_theme_style, add_theme_component
from dearpygui._dearpygui import get_value, set_value, delete_item, get_item_configuration, configure_item
from .._internal import registry
from .._internal.item import ItemData, Item
from .._internal.comtypes import RGBA, X, XY


####################################################################################
################################ Theme-Related Data ################################
####################################################################################
THEME_COLOR = 0
THEME_STYLE = 1


class ThemeElementData(NamedTuple):
    """Contains information regarding a DearPyGui theme element.

    Args:
        * category (ThemeCategory): DearPyGui `mvThemeCat` constant value.
        * kind (Literal[0, 1]): Number representing the element's type (color = 0, style = 1).
        * target (int): DearPyGui's `ThemeCol`/`StyleVar` constant value for the item.
        * components (Literal[1, 2, 3, 4]): The number of values the target uses. Ranges from 1 to 4.
        * value_type (type[float] | type[int]): Accepted type of all inner values for the element.
    """
    category  : 'ThemeCategory'
    kind      : Literal[0, 1]
    target    : int
    components: Literal[1, 2, 3, 4]
    value_type: type[float] | type[int]

    # NOTE: DearPyPixl does not strictly enforce `value_type` and is actually unused.
    # DearPyGui doesn't care as long as they are numeric (`Decimal` also works) -- it
    # even returns RGBA color values as floats!...
    # ...


class ThemeCategory(IntEnum):
    Core = _dearpygui.mvThemeCat_Core
    Plot = _dearpygui.mvThemeCat_Plots
    Node = _dearpygui.mvThemeCat_Nodes


class ThemeElementType(Enum):
    Text                  = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Text                 , 4 , int  )
    TextDisabled          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TextDisabled         , 4 , int  )
    WindowBg              = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_WindowBg             , 4 , int  )
    ChildBg               = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ChildBg              , 4 , int  )
    PopupBg               = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_PopupBg              , 4 , int  )
    Border                = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Border               , 4 , int  )
    BorderShadow          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_BorderShadow         , 4 , int  )
    FrameBg               = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_FrameBg              , 4 , int  )
    FrameBgHovered        = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_FrameBgHovered       , 4 , int  )
    FrameBgActive         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_FrameBgActive        , 4 , int  )
    TitleBg               = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TitleBg              , 4 , int  )
    TitleBgActive         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TitleBgActive        , 4 , int  )
    TitleBgCollapsed      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TitleBgCollapsed     , 4 , int  )
    MenuBarBg             = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_MenuBarBg            , 4 , int  )
    ScrollbarBg           = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ScrollbarBg          , 4 , int  )
    ScrollbarGrab         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ScrollbarGrab        , 4 , int  )
    ScrollbarGrabHovered  = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ScrollbarGrabHovered , 4 , int  )
    ScrollbarGrabActive   = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ScrollbarGrabActive  , 4 , int  )
    CheckMark             = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_CheckMark            , 4 , int  )
    SliderGrab            = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_SliderGrab           , 4 , int  )
    SliderGrabActive      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_SliderGrabActive     , 4 , int  )
    Button                = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Button               , 4 , int  )
    ButtonHovered         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ButtonHovered        , 4 , int  )
    ButtonActive          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ButtonActive         , 4 , int  )
    Header                = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Header               , 4 , int  )
    HeaderHovered         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_HeaderHovered        , 4 , int  )
    HeaderActive          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_HeaderActive         , 4 , int  )
    Separator             = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Separator            , 4 , int  )
    SeparatorHovered      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_SeparatorHovered     , 4 , int  )
    SeparatorActive       = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_SeparatorActive      , 4 , int  )
    ResizeGrip            = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ResizeGrip           , 4 , int  )
    ResizeGripHovered     = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ResizeGripHovered    , 4 , int  )
    ResizeGripActive      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ResizeGripActive     , 4 , int  )
    Tab                   = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_Tab                  , 4 , int  )
    TabHovered            = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TabHovered           , 4 , int  )
    TabActive             = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TabActive            , 4 , int  )
    TabUnfocused          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TabUnfocused         , 4 , int  )
    TabUnfocusedActive    = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TabUnfocusedActive   , 4 , int  )
    DockingPreview        = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_DockingPreview       , 4 , int  )
    DockingEmptyBg        = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_DockingEmptyBg       , 4 , int  )
    PlotLines             = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_PlotLines            , 4 , int  )
    PlotLinesHovered      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_PlotLinesHovered     , 4 , int  )
    PlotHistogram         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_PlotHistogram        , 4 , int  )
    PlotHistogramHovered  = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_PlotHistogramHovered , 4 , int  )
    TableHeaderBg         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TableHeaderBg        , 4 , int  )
    TableBorderStrong     = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TableBorderStrong    , 4 , int  )
    TableBorderLight      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TableBorderLight     , 4 , int  )
    TableRowBg            = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TableRowBg           , 4 , int  )
    TableRowBgAlt         = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TableRowBgAlt        , 4 , int  )
    TextSelectedBg        = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_TextSelectedBg       , 4 , int  )
    DragDropTarget        = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_DragDropTarget       , 4 , int  )
    NavHighlight          = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_NavHighlight         , 4 , int  )
    NavWindowingHighlight = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_NavWindowingHighlight, 4 , int  )
    NavWindowingDimBg     = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_NavWindowingDimBg    , 4 , int  )
    ModalWindowDimBg      = ThemeElementData(ThemeCategory.Core, THEME_COLOR, _dearpygui.mvThemeCol_ModalWindowDimBg     , 4 , int  )
    Alpha                 = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_Alpha                , 1 , float)
    WindowPadding         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_WindowPadding        , 2 , int  )
    WindowRounding        = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_WindowRounding       , 1 , int  )
    WindowBorderSize      = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_WindowBorderSize     , 1 , int  )
    WindowMinSize         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_WindowMinSize        , 2 , int  )
    WindowTitleAlign      = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_WindowTitleAlign     , 2 , float)
    ChildRounding         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ChildRounding        , 1 , int  )
    ChildBorderSize       = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ChildBorderSize      , 1 , int  )
    PopupRounding         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_PopupRounding        , 1 , int  )
    PopupBorderSize       = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_PopupBorderSize      , 1 , int  )
    FramePadding          = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_FramePadding         , 2 , int  )
    FrameRounding         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_FrameRounding        , 1 , int  )
    FrameBorderSize       = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_FrameBorderSize      , 1 , int  )
    ItemSpacing           = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ItemSpacing          , 2 , int  )
    ItemInnerSpacing      = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ItemInnerSpacing     , 2 , int  )
    IndentSpacing         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_IndentSpacing        , 1 , int  )
    CellPadding           = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_CellPadding          , 2 , int  )
    ScrollbarSize         = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ScrollbarSize        , 1 , int  )
    ScrollbarRounding     = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ScrollbarRounding    , 1 , int  )
    GrabMinSize           = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_GrabMinSize          , 1 , int  )
    GrabRounding          = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_GrabRounding         , 1 , int  )
    TabRounding           = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_TabRounding          , 1 , int  )
    ButtonTextAlign       = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_ButtonTextAlign      , 2 , float)
    SelectableTextAlign   = ThemeElementData(ThemeCategory.Core, THEME_STYLE, _dearpygui.mvStyleVar_SelectableTextAlign  , 2 , float)

    PlotLine               = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_Line                   , 4 , int  )
    PlotFill               = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_Fill                   , 4 , int  )
    PlotMarkerOutline      = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_MarkerOutline          , 4 , int  )
    PlotMarkerFill         = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_MarkerFill             , 4 , int  )
    PlotErrorBar           = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_ErrorBar               , 4 , int  )
    PlotFrameBg            = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_FrameBg                , 4 , int  )
    PlotBg                 = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_PlotBg                 , 4 , int  )
    PlotBorder             = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_PlotBorder             , 4 , int  )
    PlotLegendBg           = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_LegendBg               , 4 , int  )
    PlotLegendBorder       = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_LegendBorder           , 4 , int  )
    PlotLegendText         = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_LegendText             , 4 , int  )
    PlotTitleText          = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_TitleText              , 4 , int  )
    PlotInlayText          = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_InlayText              , 4 , int  )
    PlotXAxis              = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_XAxis                  , 4 , int  )
    PlotXAxisGrid          = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_XAxisGrid              , 4 , int  )
    PlotYAxis              = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxis                  , 4 , int  )
    PlotYAxisGrid          = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxisGrid              , 4 , int  )
    PlotYAxis2             = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxis2                 , 4 , int  )
    PlotYAxisGrid2         = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxisGrid2             , 4 , int  )
    PlotYAxis3             = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxis3                 , 4 , int  )
    PlotYAxisGrid3         = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_YAxisGrid3             , 4 , int  )
    PlotSelection          = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_Selection              , 4 , int  )
    PlotQuery              = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_Query                  , 4 , int  )
    PlotCrosshairs         = ThemeElementData(ThemeCategory.Plot, THEME_COLOR, _dearpygui.mvPlotCol_Crosshairs             , 4 , int  )
    PlotLineWeight         = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_LineWeight        , 1 , float)
    PlotMarker             = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_Marker            , 1 , float)
    PlotMarkerSize         = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MarkerSize        , 1 , float)
    PlotMarkerWeight       = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MarkerWeight      , 1 , float)
    PlotFillAlpha          = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_FillAlpha         , 1 , float)
    PlotErrorBarSize       = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_ErrorBarSize      , 1 , float)
    PlotErrorBarWeight     = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_ErrorBarWeight    , 1 , float)
    PlotDigitalBitHeight   = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_DigitalBitHeight  , 1 , float)
    PlotDigitalBitGap      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_DigitalBitGap     , 1 , float)
    PlotPlotBorderSize     = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_PlotBorderSize    , 1 , float)
    PlotMinorAlpha         = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MinorAlpha        , 1 , float)
    PlotMajorTickLen       = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MajorTickLen      , 2 , float)
    PlotMinorTickLen       = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MinorTickLen      , 2 , float)
    PlotMajorTickSize      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MajorTickSize     , 2 , float)
    PlotMinorTickSize      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MinorTickSize     , 2 , float)
    PlotMajorGridSize      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MajorGridSize     , 2 , float)
    PlotMinorGridSize      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MinorGridSize     , 2 , float)
    PlotPadding            = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_PlotPadding       , 2 , float)
    PlotLabelPadding       = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_LabelPadding      , 2 , float)
    PlotLegendPadding      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_LegendPadding     , 2 , float)
    PlotLegendInnerPadding = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_LegendInnerPadding, 2 , float)
    PlotLegendSpacing      = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_LegendSpacing     , 2 , float)
    PlotMousePosPadding    = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_MousePosPadding   , 2 , float)
    PlotAnnotationPadding  = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_AnnotationPadding , 2 , float)
    PlotFitPadding         = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_FitPadding        , 2 , float)
    PlotDefaultSize        = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_PlotDefaultSize   , 2 , int  )
    PlotMinSize            = ThemeElementData(ThemeCategory.Plot, THEME_STYLE, _dearpygui.mvPlotStyleVar_PlotMinSize       , 2 , int  )

    # BUG: I don't think it is intended to have both "mvNode" and "mvNodes" prefixes...
    NodeBackground                    = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_NodeBackground                , 4 , int  )
    NodeBackgroundHovered             = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_NodeBackgroundHovered         , 4 , int  )
    NodeBackgroundSelected            = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_NodeBackgroundSelected        , 4 , int  )
    NodeOutline                       = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_NodeOutline                   , 4 , int  )
    NodeTitleBar                      = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_TitleBar                      , 4 , int  )
    NodeTitleBarHovered               = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_TitleBarHovered               , 4 , int  )
    NodeTitleBarSelected              = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_TitleBarSelected              , 4 , int  )
    NodeLink                          = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_Link                          , 4 , int  )
    NodeLinkHovered                   = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_LinkHovered                   , 4 , int  )
    NodeLinkSelected                  = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_LinkSelected                  , 4 , int  )
    NodePin                           = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_Pin                           , 4 , int  )
    NodePinHovered                    = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_PinHovered                    , 4 , int  )
    NodeBoxSelector                   = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_BoxSelector                   , 4 , int  )
    NodeBoxSelectorOutline            = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_BoxSelectorOutline            , 4 , int  )
    NodeGridBackground                = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_GridBackground                , 4 , int  )
    NodeGridLine                      = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodeCol_GridLine                      , 4 , int  )
    NodeGridLinePrimary               = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_GridLinePrimary              , 4 , int  )
    NodeMiniMapBackground             = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapBackground            , 4 , int  )
    NodeMiniMapBackgroundHovered      = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapBackgroundHovered     , 4 , int  )
    NodeMiniMapOutline                = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapOutline               , 4 , int  )
    NodeMiniMapOutlineHovered         = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapOutlineHovered        , 4 , int  )
    NodeMiniMapNodeBackground         = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapNodeBackground        , 4 , int  )
    NodeMiniMapNodeBackgroundHovered  = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapNodeBackgroundHovered , 4 , int  )
    NodeMiniMapNodeBackgroundSelected = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapNodeBackgroundSelected, 4 , int  )
    NodeMiniMapNodeOutline            = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapNodeOutline           , 4 , int  )
    NodeMiniMapLink                   = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapLink                  , 4 , int  )
    NodeMiniMapLinkSelected           = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapLinkSelected          , 4 , int  )
    NodeMiniMapCanvas                 = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapCanvas                , 4 , int  )
    NodeMiniMapCanvasOutline          = ThemeElementData(ThemeCategory.Node, THEME_COLOR, _dearpygui.mvNodesCol_MiniMapCanvasOutline         , 4 , int  )
    NodeGridSpacing                   = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_GridSpacing              , 1 , float)
    NodeCornerRounding                = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_NodeCornerRounding       , 1 , float)
    NodePadding                       = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_NodePadding              , 1 , float)
    NodeBorderThickness               = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_NodeBorderThickness      , 1 , float)
    NodeLinkThickness                 = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_LinkThickness            , 1 , float)
    NodeLinkLineSegmentsPerLength     = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_LinkLineSegmentsPerLength, 1 , float)
    NodeLinkHoverDistance             = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_LinkHoverDistance        , 1 , float)
    NodePinCircleRadius               = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinCircleRadius          , 1 , float)
    NodePinQuadSideLength             = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinQuadSideLength        , 1 , float)
    NodePinTriangleSideLength         = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinTriangleSideLength    , 1 , float)
    NodePinLineThickness              = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinLineThickness         , 1 , float)
    NodePinHoverRadius                = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinHoverRadius           , 1 , float)
    NodePinOffset                     = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodeStyleVar_PinOffset                , 1 , float)
    NodeMiniMapPadding                = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodesStyleVar_MiniMapPadding          , 2 , float)
    NodeMiniMapOffset                 = ThemeElementData(ThemeCategory.Node, THEME_STYLE, _dearpygui.mvNodesStyleVar_MiniMapOffset           , 2 , float)

    @classmethod
    def get(cls, category: ThemeCategory, kind: Literal[0, 1], target: int):
        args = ThemeCategory(category), kind, target
        for element in cls.__members__.values():
            element_data = element[:3]
            if args == element_data:
                return element
        return None


class ItemState(Enum):
    Enabled  = True
    Disabled = False

    def __bool__(self):
        return self.value


####################################################################################
############################### Theme Element Proxys ###############################
####################################################################################

# These structures are intended to be managed by a parent item and are not
# directly exposed to the user.

# Due to how DearPyGui's theme system works, this isn't a subclass of `Item`.
# Theme component and element (i.e color/style items) are fairly immutable once
# created. They can't be hidden, disabled, or even parented by stage items --
# their values are always reflected in their parenting theme item simply by
# existing. The only relevant, mutable configuration option for a theme element
# are their values, and they (or their inner values) cannot be set to None.



class TElementProxy(Sequence):
    __slots__ = ("_tag", "_target", "_target_val", "_parent", "_one_component", "_command")

    __FILLVALUE = object()  # sentinel for "use existing value"

    def __init__(
        self,
        parent : Item,
        target : ThemeElementType,
    ):
        self._tag           = None          # changes, unlike the Item instance equivelent
        self._target        = target
        self._target_val    = target.value
        self._parent        = int(parent)
        self._one_component = True if self._target_val[3] == 1 else False

        match self._target_val[1]:
            case 0:
                self._command = add_theme_color
            case 1:
                self._command = add_theme_style
            case _:
                raise TypeError("Cannot identify correct command.")

    def __getitem__(self, index: int):
        return self.get_value()[index]

    def __setitem__(self, index: int, value: int | float):
        # This should be invoked whenever a specific value value needs
        # to be set as it preps a template structure that `set_value`
        # can work with.
        v_template = [self.__FILLVALUE] * self._target_val[3]
        v_template[index] = value
        self.set_value(v_template)

    def __len__(self) -> int:
        return len(self.get_value())

    def __eq__(self, other) -> bool:
        return self.get_value() == other

    def __bool__(self) -> bool:
        if self.get_value():
            return True
        return False

    def __repr__(self) -> str:
        # The intention is to *not* give this object a unique
        # representation. Its identity will be a part of another.
        return str(self.get_value())

    def _new_element_item(self) -> None:
        self._tag = self._command(
            target=self._target_val[2],
            category=self._target_val[0],
            parent=self._parent,
        )

    def _set_value(self, value: Sequence) -> None:
        try:
            set_value(self._tag, value)
        except SystemError:
            # Since this is a private method, `value` *should* be a sequence, but...
            if not isinstance(value, (list, tuple)):
                raise TypeError(f"Expected a list or tuple (got {type(value).__qualname__!r}.")
            # Verify that `value` is the correct length.
            components = self._target_val[3]
            if len(value) != components:
                raise ValueError(f"Expected {components} values (got {len(value)}.")
            # Check value types
            # Not using ThemeElement's `value_type` since DPG will accept any
            # numeric and just convert it.
            for v in value:
                if not isinstance(v, (int, float, Decimal)):
                    raise TypeError(f"Expected {self._target_val[4].__qualname__} type for inner values (got {type(v).__qualname__!r}.")
            raise

    def set_value(self, value: RGBA | RGBA | XY | X | None) -> None:
        if not value:
            if self._tag:
                return delete_item(self._tag)
            return None
        # Ensure of an existing item before messing with the value.
        if not self._tag:
            self._new_element_item()
        # Swap any filler value for the current/default value amongst
        # the newer values.
        filler_value  = self.__FILLVALUE
        if self._one_component and not isinstance(value, Sequence):
            value = (value, filler_value)
        current_value = get_value(self._tag)
        value = [nv if nv is not filler_value else cv
                 for nv, cv in zip(value, current_value)]
        set_value(self._tag, value)

    def get_value(self) -> Sequence | X | None:
        value = None
        if self._tag:
            value = get_value(self._tag)
            if self._one_component:
                value = value[0]
        return value


class ThemeColor(TElementProxy):
    __slots__ = ()

    __command__ = add_theme_color

    def __init__(
        self,
        parent: Item,
        target: ThemeElementType,
    ):
        super().__init__(parent, target)


class ThemeStyle(TElementProxy):
    __slots__ = ()

    __command__ = add_theme_style

    def __init__(
        self,
        parent: Item,
        target: ThemeElementType,
    ):
        super().__init__(parent, target)



####################################################################################
################################## "ThemeElement" ##################################
####################################################################################

class _BoundTElement(tuple):
    """Type marker, see `ThemeElement.bind`, `_Theme.__init_subclass__`.
    """
    ...


class ThemeElement(Sequence, Item):
    """"""
    # Theme component item that masquerades as a theme element item through
    # composition. Several method calls are forwarded to the bound TElementProxy
    # object.
    __slots__ = ("_element",)
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvThemeComponent, "mvThemeComponent"),
        is_container=False,  # `True`internally,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvTheme,),
        able_children=(),
        command=add_theme_component,
    )

    ALL_ITEMS = 0

    def __init__(
        self,
        target             : ThemeElementType,
        value              : Sequence[int | float] = None,
        item_type          : int  | type[Item]     = 0,
        item_state         : bool | ItemState      = ItemState.Enabled,
        *,
        label              : str                   = None,
        user_data          : Any                   = None,
        use_internal_label : bool                  = True,
        parent             : Item | int            = 0   ,
        before             : Item | int            = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            item_type=int(item_type),
            label=label or target.name,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            **kwargs,
        )
        self.item_state = item_state

        self._element = TElementProxy(self, target)
        self.set_value(value)

    def __repr__(self) -> str:
        return f"{type(self).__qualname__}(tag={self.tag}, value={self.get_value()})"

    def __getitem__(self, index: int):
        return self._element.__getitem__(index)

    def __setitem__(self, index: int, value: int | float):
        return self._element.__setitem__(index, value)

    def __len__(self) -> int:
        return self._element.__len__()

    def __eq__(self, other):
        return self._element.__eq__(other)

    def __bool__(self):
        return self._element.__bool__()

    def get_value(self) -> RGBA | XY | X | None:
        return self._element.get_value()

    def set_value(self, value: RGBA | RGBA | XY | X | None) -> None:
        return self._element.set_value(value)

    def children(self, slot: int = None) -> tuple[Item]:
        return ()

    @classmethod
    def bind(
        cls,
        target    : ThemeElementType,
        value     : Sequence[int | float] = None,
        item_type : int  | type[Item]     = ALL_ITEMS,
        item_state: bool | ItemState      = ItemState.Enabled,
    ) -> RGBA | XY:
        """Adds data descriptor access to a Theme subclass' class attribute.

        Args:
            * target (ThemeElementType): The theme element to affect (MUST be
            a member of `ThemeElementType`).

            * value (Sequence[int | float], optional): The element's default
            value. If None, no value will be set. Defaults to None.

            * item_type (int | ItemT, optional): The type of item to affect.
            If 0, all item types are affected. Defaults to 0.

            * item_state (bool | ItemState, optional): The element will only
            apply to <item_type> if the item's overall state matches this
            value. Defaults to `ItemState.Enabled` (True).

        >>> class UserTheme(Theme):
        ...     window_bg = ThemeElement.bind(ThemeElementType.WindowBg)
        >>>
        >>> user_theme = UserTheme()
        isinstance(type(user_theme).window_bg, property) is True
        >>>
        >>> user_theme.window_bg = 255, 0, 0, 150
        >>> user_theme.window_bg[1] = 100
        user_theme.window_bg == [255, 100, 0, 150]
        """
        # `_Theme.__init_subclass__` has special handling for class attributes
        # bound to a `_BoundTElement` instance. The attribute will basically
        # act as a descriptor/property that gets/sets the value of a theme
        # element directly for its instances.
        return _BoundTElement((cls, target, value, item_type, item_state))

    @property
    @__dearpypixl__.as_configuration
    def target(self) -> ThemeElementType:
        """A member of `ThemeElementType`.
        """
        return self._element._target

    @property
    @__dearpypixl__.as_configuration
    def value(self) -> RGBA | XY | X | None:  # TElementProxy
        return self._element.get_value()
    @value.setter
    def value(self, value: Sequence[float] | None | None) -> None:
        return self._element.set_value(value)

    @property
    @__dearpypixl__.as_configuration
    def item_type(self) -> Item:
        """This element will affect this item type (when the item(s) state
        matches <item_state>). If it is 0, all item types are affected.
        """
        value = get_item_configuration(self._tag)["item_type"]
        try:
            itemt = registry._itemtypes.get.by_typeid_number(value)[0]
        except IndexError:
            return value
        return itemt[0]

    @property
    @__dearpypixl__.as_configuration
    def item_state(self) -> ItemState:
        """This element will affect <item_type> only when the item(s) are in
        this state.
        """
        return ItemState(get_item_configuration(self._tag)["enabled_state"])
    @item_state.setter
    def item_state(self, value: ItemState | bool) -> None:
        configure_item(self._tag, enabled_state=bool(value))
