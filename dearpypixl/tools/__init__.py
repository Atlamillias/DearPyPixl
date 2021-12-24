from contextlib import contextmanager
from typing import Union
from dearpygui import _dearpygui, dearpygui
from dearpypixl.tools.dpgtools import (
    show_about,
    show_debug,
    show_documentation,
    show_font_manager,
    show_item_registry,
    show_metrics,
    show_style_editor,
)
from dearpypixl.tools.pyconsole import PyConsole
from dearpypixl.tools.appinfo import AppInfo
from dearpypixl.components import Item

__all__ = [
    # from DPG
    "show_about",
    "show_debug",
    "show_documentation",
    "show_font_manager",
    "show_item_registry",
    "show_metrics",
    "show_style_editor",
    # classes
    "PyConsole",
    "AppInfo",
    # functions/helpers
    "stage",
    "mutex",
    "find_reference",
]


@contextmanager
def mutex() -> None:
    """Locks the mutex within context of this call.

    Yields:
        None
    """
    try:
        yield _dearpygui.lock_mutex()
    finally:
        _dearpygui.unlock_mutex()


def find_reference(tag: Union[str, int]) -> Union[Item, None]:
    """Returns a reference of an Item object that has a unique identifier
    of <tag>. Returns None if it doesn't exist or is not found.

    Args:
        * tag (Union[str, int]): Unique identifier of an item.

    Returns:
        Union[Item, None]
    """
    return Item._AppItemsRegistry.get(tag, None)
