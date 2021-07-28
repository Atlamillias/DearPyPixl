"""
This package serves to wrap DearPyGui into an object-oriented
interface. Much of this is still undocumented, but I'm working on it!
DPGwidgets tries to preserve the overall feel of the existing DearPyGui
framework - most of that documentation is applicable to this package.

Please consider supporting Jonathan Hoffstadt and Preston Cothren for
all of their hard work in creating DearPyGui
(https://github.com/hoffstadt/DearPyGui).

"""
import sys
sys.path.append("./dpgwrap/")
sys.path.append("./dpgwrap/tools/")

from dearpygui import dearpygui as dpg, _dearpygui as idpg
from dpgwrap._item import Item, ContextSupport  # avoids circular imports
from dpgwidgets.constants import Registry as _Registry, Key, Mouse

# registries
with dpg.font_registry(id=_Registry.FONT.value, label="AppFontRegistry"):
    pass
with dpg.handler_registry(id=_Registry.APPHANDLER.value, label="AppHandlerRegistry"):
    pass
with dpg.texture_registry(id=_Registry.TEXTURE.value, label="AppTextureRegistry"):
    pass
with dpg.value_registry(id=_Registry.VALUE.value, label="AppValueRegistry"):
    pass

from dpgwidgets.app import Viewport
from dpgwidgets.theme import Font, Theme
from dpgwrap import (
    containers,
    drawing,
    node,
    plotting,
    widgets
)

__version__ = "0.1.1"

__all__ = [
    # high-level objects
    "Application",
    "Viewport",
    "Theme",
    "Font",
    "Key",
    "Mouse",
    # imports
    "containers",
    "drawing",
    "node",
    "plotting",
    "widgets",
    "themes",
    "tools",
    # dearpygui.dearpygui
    "dpg",
]


# Typically, UI code is in main.py and not split across other
# modules. For larger projects it's almost impossible to avoid.
# "Application" exists to make it easier to split a UI across
# multiple files. Instead of creating a Viewport instance in
# one file and having every other file import it, they can import
# Application instead.
Application = Viewport(is_dummy=True)


def _update_wrappers():
    """Generates an object-oriented framework (dpgwrap) for 
    DearPyGui and writes it to files based on the currently
    installed DPG version. The existing (overwritten) files 
    in dpgwrap will be backed up in dpgwrap/_backup.

    This function is not intended to be private/internal use -
    It is marked as such only to avoid accidental calls. Because
    this writes files, a PermissionError will be raised if
    Python is installed in a read-only directory (like
    'C:\Program Files' on Windows).
    """
    import importlib
    from dpgwrap import _generate

    _generate.main()

    modules = [containers, drawing, widgets, node, plotting]

    for module in modules:
        try:
            importlib.reload(module)
        except:
            continue

