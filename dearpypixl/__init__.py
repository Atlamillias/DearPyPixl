from dearpygui import dearpygui as _dearpygui


# BUG: This allows modules in `_subpackages` to be imported from the
# `dearpypixl` namespace. However, linters (PyLint) do not like this.
# TODO: Find out how to fix the above WITHOUT needing dummy modules...
#_subpackages = (
#    "itemtypes",
#    "items",
#)
#
#__path__ += [os.path.join(__path__[0], _pkg) for _pkg in _subpackages]

## DearPyGui prep ##
_dearpygui.create_context()
_dearpygui.create_viewport()
_dearpygui.setup_dearpygui()
_dearpygui.configure_viewport("DPG NOT USED YET", title="Application")
# DearPyPixl doesn't expose `mvFontRegistry` -- the `Font` class has been
# customized to accomidate. This sets up auto-parenting for font items.
_dearpygui.add_font_registry(tag=_dearpygui.mvReservedUUID_0)

## DearPyPixl prep ##
# Item types are registered when they are created. Importing each module
# ensures that they are registered. Otherwise, they may not exist in the
# registry when they are required (mainly for reconstitutional purposes).
from . import (
    # itemtypes
    events,
    themes,
    # items
    basic,
    containers,
    colors,
    drawing,
    misc,
    nodes,
    plotting,
    tables,
    textures,
    values,
)

from .application import Application
from .viewport import Viewport
