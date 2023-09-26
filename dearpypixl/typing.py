from dearpygui import dearpygui
from ._typing import (
    Item,
    ItemUUID,
    ItemAlias,
    Interface,
    ItemCallback,
    ItemCommand,
    ItemInfoDict,
    ItemStateDict,

    mvBuffer,
    mvMat4,
    mvVec4,

    cast,
)
from ._interface import (
    AppItemMeta,
    AppItemType,

    ABCAppItemMeta,
    ABCAppItemType,

    BasicType,
    ContainerType,
    RootType,
    RegistryType,

    HandlerType,
    NodeType,
    NodeEditorType,
    ThemeType,
    ThemeElementType,
    FontType,
    DrawingType,
    DrawNodeType,
    PlottingType,
    PlotType,
    PlotAxisType,
    TableType,
    TableItemType,
    WindowType,

    SupportsCallback,
    SupportsSized,
    SupportsValueArray,
)
from .api import (
    _AppConfigDict as AppConfigDict,
    _ViewportConfigDict as ViewportConfigDict,
    _RuntimeConfigDict as RuntimeConfigDict,
)


mvBuffer = cast(type[mvBuffer], dearpygui.mvBuffer)
mvMat4   = cast(type[mvMat4], dearpygui.mvMat4)
mvVec4   = cast(type[mvVec4], dearpygui.mvVec4)
