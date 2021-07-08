import sys

sys.path.append("./dpgwrap/")

from dearpygui import core as idpg, dearpygui as dpg

# order is to avoid circular imports
from dpgwrap._item import Item, Context
from dpgwidgets.widget import Container, Widget

from dpgwidgets.app import Application, Viewport
from dpgwrap import *


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

