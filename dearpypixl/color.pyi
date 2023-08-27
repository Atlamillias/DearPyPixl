from ._dearpypixl.common import (
    Item,
    ItemAlias,
    ItemUUID,
    ItemCommand,
    Array,
    Literal,
    Sequence,
    Callable,
    Property,
    Any,
    Color,
    Point,
)
from ._dearpypixl.interface import (
    BasicType,
    ContainerType,
    DrawNodeType,
    DrawingType,
    FontType,
    HandlerType,
    NodeEditorType,
    NodeType,
    PlotAxisType,
    PlotType,
    PlottingType,
    RegistryType,
    RootType,
    SupportsCallback,
    SupportsSized,
    SupportsValueArray,
    TableItemType,
    TableType,
    ThemeColor,
    ThemeStyle,
    ThemeType,
    WindowType,
    mvAll,
)


class Border(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class BorderShadow(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Button(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ButtonActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ButtonHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class CheckMark(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ChildBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class DockingEmptyBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class DockingPreview(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class DragDropTarget(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class FrameBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class FrameBgActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class FrameBgHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Header(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class HeaderActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class HeaderHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MenuBarBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ModalWindowDimBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NavHighlight(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NavWindowingDimBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NavWindowingHighlight(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotHistogram(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotHistogramHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotLines(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotLinesHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PopupBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ResizeGrip(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ResizeGripActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ResizeGripHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ScrollbarBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ScrollbarGrab(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ScrollbarGrabActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ScrollbarGrabHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Separator(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class SeparatorActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class SeparatorHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class SliderGrab(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class SliderGrabActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Tab(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TabActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TabHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TabUnfocused(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TabUnfocusedActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TableBorderLight(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TableBorderStrong(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TableHeaderBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TableRowBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TableRowBgAlt(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Text(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TextDisabled(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TextSelectedBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBgActive(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBgCollapsed(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class WindowBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Crosshairs(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class ErrorBar(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Fill(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotFrameBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class InlayText(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class LegendBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class LegendBorder(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class LegendText(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Line(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MarkerFill(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MarkerOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PlotBorder(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Query(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Selection(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleText(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class XAxis(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class XAxisGrid(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxis(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxis2(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxis3(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxisGrid(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxisGrid2(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class YAxisGrid3(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class BoxSelector(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class BoxSelectorOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class GridBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class GridLine(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Link(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class LinkHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class LinkSelected(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NodeBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NodeBgHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NodeBgSelected(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class NodeOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class Pin(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class PinHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBar(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBarHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class TitleBarSelected(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class GridLinePrimary(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapBgHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapCanvas(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapCanvasOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapLink(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapLinkSelected(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapNodeBg(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapNodeBgHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapNodeBgSelected(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapNodeOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapOutline(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    

class MiniMapOutlineHovered(ThemeColor):
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    