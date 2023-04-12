"""This module exposes "built-in" DearPyGui item types as class objects.
Instances of item type classes act as interfaces to a specific item
throughout their lifetime. Users do not need to import this module --
All objects are added to the `dearpypixl` namespace automatically.
"""
# Workarounds for DearPyGui/Imgui bugs/lack of fundamental
# features, additional DearPyGui hooks, and *small* API
# extensions are added here.

from .px_items import AppItemType
from ._appitems import *
from . import _appitems


__all__ = [
    "AppItemType",
    "mvAll",
    "mvWindow",
    *_appitems.__all__,
]


mvAll    = AppItemType
mvWindow = mvWindowAppItem
