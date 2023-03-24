"""A lightweight framework and toolkit for DearPyGui."""

from . import px_patcher as _px_patcher

_px_patcher.apply_patch()


try:
    from dearpypixl.appitems import *
except ImportError:
    pass
