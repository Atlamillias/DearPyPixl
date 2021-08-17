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
from dpgwidgets import _writelib

# NOTE: For releases/distributions that include this library, I'd
# advise you to set AUTO_UPDATE to False.
AUTO_UPDATE = True

def update_library():
    try:
        _writelib.main()
    except PermissionError as e:
        warnings.warn(f"A PermissionError was raised trying to update the library - {str(e)}.")

if AUTO_UPDATE and __name__ != "__main__":
    update_library()


from dearpygui.dearpygui import setup_registries as _setup_registries
_setup_registries()



import dpgwidgets.libsrc as dpglib

from dpgwidgets.app import Viewport, _Viewport
from dpgwidgets.theme import Font, Theme
from dpgwidgets.keycodes import Key, Mouse


__version__ = "0.2.51"

__all__ = [
    # high-level objects
    "Application",
    "Viewport",
    "Theme",
    "Font",
    "Key",
    "Mouse",
    # modules
    "containers",
    "drawing",
    "node",
    "plotting",
    "widgets",
    "theme",
    "themes",
    "tools",
]



Application = _Viewport()
