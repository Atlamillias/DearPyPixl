from dearpygui import dearpygui
from ._typing import (
    Item as Item,
    ItemUUID as ItemUUID,
    ItemAlias as ItemAlias,
    Interface as Interface,
    ItemCallback as ItemCallback,
    ItemCommand as ItemCommand,
    ItemInfoDict as ItemInfoDict,
    ItemStateDict as ItemStateDict,
    mvBuffer as mvBuffer,
    mvMat4 as mvMat4,
    mvVec4 as mvVec4,

    cast,
)
from ._interface import (
    AppItemMeta as AppItemMeta,
    AppItemType as AppItemType,
    ABCAppItemMeta as ABCAppItemMeta,
    ABCAppItemType as ABCAppItemType,

    BasicType as BasicType,
    ContainerType as ContainerType,
    RootType as RootType,
    RegistryType as RegistryType,
    HandlerType as HandlerType,
    NodeType as NodeType,
    NodeEditorType as NodeEditorType,
    ThemeType as ThemeType,
    ThemeElementType as ThemeElementType,
    FontType as FontType,
    DrawingType as DrawingType,
    DrawNodeType as DrawNodeType,
    PlottingType as PlottingType,
    PlotType as PlotType,
    PlotAxisType as PlotAxisType,
    TableType as TableType,
    TableItemType as TableItemType,
    WindowType as WindowType,

    SupportsCallback as SupportsCallback,
    SupportsSized as SupportsSized,
    SupportsValueArray as SupportsValueArray,
)
from .api import (
    AppConfigDict as AppConfigDict,
    ViewportConfigDict as ViewportConfigDict,
    RuntimeConfigDict as RuntimeConfigDict,
)


mvBuffer = cast(type[mvBuffer], dearpygui.mvBuffer)
mvMat4   = cast(type[mvMat4], dearpygui.mvMat4)
mvVec4   = cast(type[mvVec4], dearpygui.mvVec4)
