"""
This package serves to wrap DearPyGui into an object-oriented
interface. Much of this is still undocumented, but I'm working on it!
dearpyguiwidgets tries to preserve the overall feel of the existing DearPyGui
framework - most of that documentation is applicable to this package.

Please consider supporting Jonathan Hoffstadt and Preston Cothren for
all of their hard work in creating DearPyGui
(https://github.com/hoffstadt/DearPyGui).

"""
import sys
sys.path.extend(["./libsrc", "./tools"])

import warnings
import dearpygui.dearpygui as dearpygui
from . import _writelib

AUTO_UPDATE = True

def update_library():
    try:
        _writelib.main()
    except PermissionError as e:
        warnings.warn(f"A PermissionError was raised trying to update the library - {str(e)}.")

if AUTO_UPDATE and __name__ != "__main__":
    update_library()


from dpgwidgets.constants import Registry as Registry, Key, Mouse
# registries
with dearpygui.font_registry(id=Registry.FONT.value, label="AppFontRegistry"):
    pass
with dearpygui.handler_registry(id=Registry.APPHANDLER.value, label="AppHandlerRegistry"):
    pass
with dearpygui.texture_registry(id=Registry.TEXTURE.value, label="AppTextureRegistry"):
    pass
with dearpygui.value_registry(id=Registry.VALUE.value, label="AppValueRegistry"):
    pass



from dpgwidgets.libsrc import containers, widgets, node, drawing, plotting

from dpgwidgets.app import Viewport, _Viewport
from dpgwidgets.theme import Font, Theme
from dpgwidgets import constants


__version__ = "0.2.01"

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
]


# Typically, UI code is in main.py and not split across other
# modules. For larger projects though it is better for organization.
# "Application" exists to make it easier to split a UI across
# multiple files. Instead of creating a Viewport instance in
# one file and having every other file import it, they can import
# Application instead.
#
# When an instance of the real Viewport class is created, the
# variable below is re-bound to the real one.
Application = _Viewport()
