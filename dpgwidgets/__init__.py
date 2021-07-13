import sys

sys.path.append("./dpgwrap/")

from dearpygui import dearpygui as dpg
# order is to avoid circular imports
from dpgwrap._item import Item, ContextSupport
from dpgwidgets.widget import Container, Widget
from dpgwidgets.constants import Registry as _Registry

from dpgwidgets.app import Application, Viewport
from dpgwidgets.theme import Font
from dpgwrap import (
    containers, 
    drawing, 
    node, 
    plotting, 
    widgets
)


UPDATE_ON_IMPORT = False
# registries


def update_wrappers():
    import importlib
    import dpgwrap
    from dpgwrap import _generate

    _generate.main()

    importlib.reload(dpgwrap)

    for module in dpgwrap.__all__:
        try:
            importlib.import_module(module, dpgwrap)
        except:
            continue


## Setup ##
if UPDATE_ON_IMPORT:
    update_wrappers()
