from contextlib import contextmanager
from typing import Union
from dearpygui import _dearpygui, dearpygui
from pixle.tools.dpgtools import (
    show_about,
    show_debug,
    show_documentation,
    show_font_manager,
    show_item_registry,
    show_metrics,
    show_style_editor,
)
from pixle.tools.pyconsole import PyConsole
from pixle.tools.appinfo import AppInfo
from pixle.itemtypes import Item

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
def stage() -> None:
    """Temporarily sets staging mode. An item created in staging mode
    is not rendered and has limited functionality until its `unstage`
    method is called. Useful for creating items within existential
    paradoxes -- For example; a `Button` item where the parent does
    not exist at the time of the button's creation.

    Yields:
        None
    """
    try:
        yield _dearpygui.set_staging_mode(True)
    finally:
        _dearpygui.set_staging_mode(False)


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
    return Item.APPITEMS.get(tag, None)
