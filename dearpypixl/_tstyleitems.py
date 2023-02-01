"""Interfaces for specific DearPyGui theme style items."""

from dearpygui import dearpygui
from .px_theme import *


__all__ = [
    'Alpha',
    'AnnotationPadding',
    'ButtonTextAlign',
    'CellPadding',
    'ChildBorderSize',
    'ChildRounding',
    'DigitalBitGap',
    'DigitalBitHeight',
    'ErrorBarSize',
    'ErrorBarWeight',
    'FillAlpha',
    'FitPadding',
    'FrameBorderSize',
    'FramePadding',
    'FrameRounding',
    'GrabMinSize',
    'GrabRounding',
    'GridSpacing',
    'IndentSpacing',
    'ItemInnerSpacing',
    'ItemSpacing',
    'LabelPadding',
    'LegendInnerPadding',
    'LegendPadding',
    'LegendSpacing',
    'LineWeight',
    'LinkHoverDistance',
    'LinkLineSegmentsPerLength',
    'LinkThickness',
    'MajorGridSize',
    'MajorTickLen',
    'MajorTickSize',
    'Marker',
    'MarkerSize',
    'MarkerWeight',
    'MiniMapOffset',
    'MiniMapPadding',
    'MinorAlpha',
    'MinorGridSize',
    'MinorTickLen',
    'MinorTickSize',
    'MousePosPadding',
    'NodeBorderThickness',
    'NodeCornerRounding',
    'NodePadding',
    'PinCircleRadius',
    'PinHoverRadius',
    'PinLineThickness',
    'PinOffset',
    'PinQuadSideLength',
    'PinTriangleSideLength',
    'PlotBorderSize',
    'PlotDefaultSize',
    'PlotMinSize',
    'PlotPadding',
    'PopupBorderSize',
    'PopupRounding',
    'ScrollbarRounding',
    'ScrollbarSize',
    'SelectableTextAlign',
    'TabRounding',
    'WindowBorderSize',
    'WindowMinSize',
    'WindowPadding',
    'WindowRounding',
    'WindowTitleAlign'
]




class Alpha(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_Alpha


class AnnotationPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_AnnotationPadding


class ButtonTextAlign(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ButtonTextAlign


class CellPadding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_CellPadding


class ChildBorderSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ChildBorderSize


class ChildRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ChildRounding


class DigitalBitGap(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_DigitalBitGap


class DigitalBitHeight(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_DigitalBitHeight


class ErrorBarSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_ErrorBarSize


class ErrorBarWeight(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_ErrorBarWeight


class FillAlpha(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_FillAlpha


class FitPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_FitPadding


class FrameBorderSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_FrameBorderSize


class FramePadding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_FramePadding


class FrameRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_FrameRounding


class GrabMinSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_GrabMinSize


class GrabRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_GrabRounding


class GridSpacing(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_GridSpacing


class IndentSpacing(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_IndentSpacing


class ItemInnerSpacing(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ItemInnerSpacing


class ItemSpacing(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ItemSpacing


class LabelPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_LabelPadding


class LegendInnerPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_LegendInnerPadding


class LegendPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_LegendPadding


class LegendSpacing(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_LegendSpacing


class LineWeight(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_LineWeight


class LinkHoverDistance(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_LinkHoverDistance


class LinkLineSegmentsPerLength(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_LinkLineSegmentsPerLength


class LinkThickness(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_LinkThickness


class MajorGridSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MajorGridSize


class MajorTickLen(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MajorTickLen


class MajorTickSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MajorTickSize


class Marker(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_Marker


class MarkerSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MarkerSize


class MarkerWeight(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MarkerWeight


class MiniMapOffset(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodesStyleVar_MiniMapOffset


class MiniMapPadding(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodesStyleVar_MiniMapPadding


class MinorAlpha(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MinorAlpha


class MinorGridSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MinorGridSize


class MinorTickLen(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MinorTickLen


class MinorTickSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MinorTickSize


class MousePosPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_MousePosPadding


class NodeBorderThickness(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_NodeBorderThickness


class NodeCornerRounding(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_NodeCornerRounding


class NodePadding(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_NodePadding


class PinCircleRadius(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinCircleRadius


class PinHoverRadius(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinHoverRadius


class PinLineThickness(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinLineThickness


class PinOffset(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinOffset


class PinQuadSideLength(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinQuadSideLength


class PinTriangleSideLength(pxThemeStyle, ThemeCatNode):
    target = dearpygui.mvNodeStyleVar_PinTriangleSideLength


class PlotBorderSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_PlotBorderSize


class PlotDefaultSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_PlotDefaultSize


class PlotMinSize(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_PlotMinSize


class PlotPadding(pxThemeStyle, ThemeCatPlot):
    target = dearpygui.mvPlotStyleVar_PlotPadding


class PopupBorderSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_PopupBorderSize


class PopupRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_PopupRounding


class ScrollbarRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ScrollbarRounding


class ScrollbarSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_ScrollbarSize


class SelectableTextAlign(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_SelectableTextAlign


class TabRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_TabRounding


class WindowBorderSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_WindowBorderSize


class WindowMinSize(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_WindowMinSize


class WindowPadding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_WindowPadding


class WindowRounding(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_WindowRounding


class WindowTitleAlign(pxThemeStyle, ThemeCatCore):
    target = dearpygui.mvStyleVar_WindowTitleAlign


