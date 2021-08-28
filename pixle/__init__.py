from dearpygui import dearpygui as _dearpygui
from pixle.application import Application
from pixle.theming import Theme, Font, FontRangeHint
from pixle.keycodes import Key, Mouse


__all__ = [
    "Application",
    "Theme",
    "Font",
    "FontRangeHint",
    "Key",
    "Mouse",
]


_dearpygui.setup_registries()
