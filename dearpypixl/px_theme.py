import dearpygui.dearpygui as dpg
from .px_items import ValueArrayItem, AppItemType
from .px_typing import overload, Any, Array, Sequence


__all__ = [
    # bases/mixins
    "ThemeCatCore",
    "ThemeCatPlot",
    "ThemeCatNode",
    "pxThemeColor",
    "pxThemeStyle",

    # functions
    "itp_from_tconst",
]





class ThemeCatCore(AppItemType):
    category = dpg.mvThemeCat_Core


class ThemeCatPlot(AppItemType):
    category = dpg.mvThemeCat_Core


class ThemeCatNode(AppItemType):
    category = dpg.mvThemeCat_Core




class pxThemeColor(ValueArrayItem, AppItemType):
    command  = dpg.add_theme_color
    identity = dpg.mvThemeColor, "mvAppItemType::mvThemeColor"

    value: Array[int, int, int, int]

    category: int = 0
    target  : int = 0

    @overload
    def __init__(self, value: Array[int, int, int, int | None], /, **kwargs) -> None: ...
    @overload
    def __init__(self, r: int, g: int, b: int, a: int = 255, /, **kwargs) -> None: ...
    def __init__(self,  value: Sequence[int] | int, *args: tuple[int], **kwargs) -> None:
        if args:
            value = (value, *args)
        super().__init__(value=value, category=self.category, target=self.target, **kwargs)



class pxThemeStyle(ValueArrayItem, AppItemType):
    command  = dpg.add_theme_style
    identity = dpg.mvThemeStyle, "mvAppItemType::mvThemeStyle"

    value: Array[int, int]

    category: int = 0
    target  : int = 0

    def __init__(self, x: float = 1, y: float = -1, **kwargs) -> None:
        super().__init__(x=x, y=y, category=self.category, target=self.target, **kwargs)



_CONSTPFX_TO_BASES = {
    "mvThemeCol_"     : (pxThemeColor, ThemeCatCore,),
    "mvPlotCol_"      : (pxThemeColor, ThemeCatPlot,),
    "mvNodeCol_"      : (pxThemeColor, ThemeCatNode,),
    "mvNodesCol_"     : (pxThemeColor, ThemeCatNode,),
    "mvStyleVar_"     : (pxThemeStyle, ThemeCatCore,),
    "mvPlotStyleVar_" : (pxThemeStyle, ThemeCatPlot,),
    "mvNodeStyleVar_" : (pxThemeStyle, ThemeCatNode,),
    "mvNodesStyleVar_": (pxThemeStyle, ThemeCatNode,),
}

def itp_from_tconst(const_name: str) -> type[pxThemeColor | pxThemeStyle]:
    try:
        const_pfx, theme_const = const_name.split("_", maxsplit=1)
        const_val = getattr(dpg, const_name)
    except (TypeError, KeyError, AttributeError):
        raise ValueError(f"expected DearPyGui theme constant name (got {const_name!r}).")

    clsname = theme_const.replace("_", "").replace("Background", "Bg").replace("bg", "Bg")
    clsdict = {
        "constant": const_name,  # makes source file generation easier, unused otherwise
        "target"  : const_val,
    }
    cls: Any = type(clsname, _CONSTPFX_TO_BASES[f"{const_pfx}_"], clsdict)  # type: ignore
    return cls
