"""A lightweight framework and toolkit for DearPyGui."""

from . import px_patcher as _px_patcher

_px_patcher._patch_dearpygui()



try:
    from dearpypixl.appitems import *
except ImportError:
    import warnings
    warnings.warn(
        'Could not build basic item types because the definition files are (possibly) '
        'out-of-date. You can update these files to match the installed version of '
        'DearPyGui by running "python -m dearpypixl" in your shell or terminal.'
    )
