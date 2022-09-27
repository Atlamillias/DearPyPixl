import logging as _logging
from dearpygui import dearpygui as _dearpygui

_logging.getLogger(__name__).addHandler(_logging.NullHandler())

## DearPyGui prep
_dearpygui.create_context()
_dearpygui.create_viewport()
_dearpygui.setup_dearpygui()

## DearPyPixl prep
# Item types are registered when they are created. Importing each module
# ensures that they are registered. Otherwise, they may not exist in the
# registry when they are required -- specifically when reconstituting a
# UI.
from . import (
    # in order, based on their dependency to other resources in the framework
    application,
    viewport,

    events,
    font,
    theme,

    basic,
    containers,
    colors,
    drawing,
    inputs,
    misc,
    nodes,
    plotting,
    tables,
    textures,
    values,
)
from .application import Application
from .viewport import Viewport
