import sys

sys.path.append("./dpgwrap/")

from dearpygui import dearpygui as dpg

# order is to avoid circular imports
from dpgwrap._item import Item, Context
from dpgwidgets.widget import Container, Widget

from dpgwidgets.app import Application, Viewport
from dpgwidgets.theme import Font
from dpgwrap import (
    containers, 
    drawing, 
    node, 
    plotting, 
    widgets, 
    registries
)


def update_wrappers():
    import importlib
    import dpgwrap
    from dpgwidgets import _generate

    _generate.main()

    importlib.reload(dpgwrap)

    for module in dpgwrap.__all__:
        try:
            importlib.import_module(module, dpgwrap)
        except:
            continue


update_wrappers()