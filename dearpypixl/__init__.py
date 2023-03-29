"""A lightweight framework and toolkit for DearPyGui."""

from . import px_patcher as _px_patcher

_px_patcher._patch_dearpygui()


try:
    from dearpypixl.appitems import *
except ImportError:
    pass
