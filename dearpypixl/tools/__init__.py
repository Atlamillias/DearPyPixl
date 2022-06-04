from contextlib import contextmanager
from dearpygui import _dearpygui, dearpygui
from dearpygui.dearpygui import (
    save_image,  # https://dearpygui.readthedocs.io/en/latest/documentation/textures.html#saving-images
    mutex,
)
from dearpypixl.tools.dpgtools import (
    show_about,
    show_debug,
    show_documentation,
    show_font_manager,
    show_item_registry,
    show_metrics,
    show_style_editor,
)
from dearpypixl.components import Item, ItemT
from dearpypixl.tools.pyconsole import PyConsole
from dearpypixl.tools.appinfo import AppInfo


__all__ = [
    # from DPG
    "show_about",
    "show_debug",
    "show_documentation",
    "show_font_manager",
    "show_item_registry",
    "show_metrics",
    "show_style_editor",
    "save_image",
    "mutex",
    # classes
    "PyConsole",
    "AppInfo",
    # functions/helpers
    "stage",
    "mutex",
    "get_reference",
    "get_text_size",
]


def get_text_size(text: str, wrap_width: float = -1.0, font: ItemT = 0) -> tuple[int, int]:
    """Return a tuple of the width and height of text rendered with a specific font
    (default font if none is included). Must be ran after the first frame.
    """
    return tuple(dearpygui.get_text_size(text, wrap_width=wrap_width, font=int(font)))


def get_reference(tag: str | int) -> Item | None:
    """Returns a reference of an Item object that uses the provided unique
    identifier. Returns None if it doesn't exist or is not found.

    Args:
        * tag (Union[str, int]): Unique identifier of an item.

    """
    return Item.__registry__[0].get(tag, None)
