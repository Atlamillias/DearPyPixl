"""A lightweight framework and toolkit for DearPyGui."""

# public imports, in order of lib dependency; none/little (top) to alot/all (bottom)
try:
    from dearpypixl.appitems import *
except:
    pass



def _optimize(mod = None) -> None:
    """Replaces a few Python objects used in performance-critical areas with
    an equivelent written in rust."""
    import sys
    from . import grid

    # TODO: crossplatform optimization
    if not mod and sys.platform() != "win32":
        return
    try:
        from . import _dearpypixl
    except:
        return

    grid._draw_cells = _dearpypixl.grid.draw_cells


