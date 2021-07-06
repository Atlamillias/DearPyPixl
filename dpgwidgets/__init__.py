import sys
import importlib


sys.path.append("./dpgwrap/")

from dearpygui import core as idpg, dearpygui as dpg
from .widget import Widget

from . import dpgwrap
from dpgwrap import _widget

_widget.Widget = Widget

importlib.reload(dpgwrap)

from dpgwrap import containers, widgets, drawing, plot, node
