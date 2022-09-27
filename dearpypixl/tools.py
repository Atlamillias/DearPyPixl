"""Useful tools and general-case helper objects.

Several functions that operate on items support raw item integer identifiers in
addition to ItemType instances. Also includes some functions/tools from DearPyGui
that are unused, not implemented, or not publicly exposed in DearPyPixl's API.

Setting the configuration or managing an ItemType instance directly through
DearPyGui may cause the instance to become outdated. Doing so is not recommended,
although may be useful in some situations.
"""
import inspect
import warnings
from typing import Callable, Any, TypeAlias
from dearpygui import dearpygui as dpg
from dearpygui.dearpygui import (
    mvVec4,    # tools.pyi
    mvMat4,    # tools.pyi
    mvBuffer,  # tools.pyi
    mutex,
    does_item_exist,
    does_alias_exist,
    get_all_items,
    show_about,
    show_debug,
    show_documentation,
    show_font_manager,
    show_imgui_demo,
    show_implot_demo,
    show_item_registry,
    show_item_debug,
)
from ._internal.callback import _get_parg_count
from ._internal.utilities import (
    classproperty,
    generate_itemtype_uuid,
    itemized_return,
    is_unbound_item,
)
from .itemtypes import Item, WidgetItem
from .application import Application, AppStateKey
from .theme import Theme
from .font import Font


__all__ = [
    # from DearPyGui
    "mutex",
    "does_item_exist",
    "does_alias_exist",
    "get_all_items",
    "mvBuffer",
    "mvVec4",
    "mvMat4",
    "show_about",
    "show_debug",
    "show_documentation",
    "show_font_manager",
    "show_imgui_demo",
    "show_implot_demo",
    "show_item_registry",
    "show_item_debug",

    # from DearPyPixl
    "classproperty",
    "generate_itemtype_uuid",
    "itemized_return",
    "is_unbound_item",

    # this module
    "get_text_size",
    "get_reflected_theme",
    "get_reflected_font",
    "is_valid_callback",
    "set_item_callback",
]


ItemRef: TypeAlias = Item | int



def get_text_size(text: str, wrap_width: float = -1.0, font: ItemRef = 0) -> tuple[int, int]:
    """Return a tuple of the width and height of text rendered with a specific font
    (default font otherwise). A warning will be displayed if the application is not running.
    """
    if not dpg.is_dearpygui_running():
        warnings.warn("Expect innaccurate return value for `get_text_size` -- Application is not running.")
    if not font:
        font_uuid = Application.__itemdict__[AppStateKey.FONT_UUID]
    else:
        font_uuid = int(font)
    return tuple(get_text_size(text, wrap_width=wrap_width, font=font_uuid))


def get_reflected_theme(item: ItemRef) -> Theme | None:
    """Return the first Theme item found affecting <item>."""
    return WidgetItem.get_reflected_theme(item)


def get_reflected_font(item: ItemRef) -> Font | None:
    """Return the first Font item found affecting <item>."""
    return WidgetItem.get_reflected_font(item)


def is_valid_callback(_object: Any) -> bool:
    """Return True if the object can be accepted as DearPyGui or DearPyPixl
    callback-related value.

    A value of None is an accepted value, and will return True.
    """
    if inspect.isfunction(_object):
        return True
    elif _object is None:
        return True
    # `inspect.isfunction` is too strict, and `callable` is inaccurate. Other
    # objects can be used, albiet requiring some tenacity.
    obj_call = getattr(_object, "__call__", None)
    obj_code = getattr(_object, "__code__", None)
    try:
        obj_call_code = obj_call.__self__.__code__
    except AttributeError:
        try:
            obj_call_code = obj_call.__code__
        except AttributeError:
            return False
    if (obj_call and obj_code) and callable(obj_call) and (obj_code == obj_call_code):
        return True
    return False


def set_item_callback(item: ItemRef, option: str, value: Callable[[int | None, Any | None, Any | None], None] | None) -> None:
    """Convenience method for setting a callback-related configuration option value directly
    through DearPyGui, bypassing all other implementations. This is the functional equivelent
    of `configure_item(..., option=value)`, with the addition of some error handling
    in an attempt to provide useful information for the user.
    """
    try:
        dpg.configure_item(int(item), **{option: value})
    except SystemError:
        if isinstance(item, Item) and option not in item.__dearpypixl__.members[0]:
            raise AttributeError(f"{type(item).__qualname__!r} object has no attribute {option!r}.")
        elif not inspect.isfunction(value) or value is not None:
            raise TypeError(f"Incorrect value type (expected `FunctionType` or None.")
        raise
