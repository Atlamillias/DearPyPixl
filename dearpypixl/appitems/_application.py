from typing import Callable, Any
from typing_extensions import Self
import functools
import warnings
import sys
import os
# Many of these tend to be called between frames as render
# callbacks -- trying to avoid lookup overhead with these
# imports.
from dearpygui import _dearpygui, dearpygui
from dearpygui._dearpygui import (
    # mainloop
    render_dearpygui_frame,
    is_dearpygui_running,
    stop_dearpygui,
    # getters
    get_total_time,
    get_frame_count,
    is_key_pressed,
    is_key_down,
    is_key_released,
    get_global_font_scale,
    get_app_configuration,
    # setters
    set_global_font_scale,
    configure_app,
    # misc
    split_frame,
)
from dearpypixl.itemtypes.events import FrameEvents
from dearpypixl.constants import AppUUID, Platform, Key
from dearpypixl.itemtypes import CONFIG, INFORM, STATES, Item, ItemProperty, Theme, ItemType
from dearpypixl.themes import _theme_presets, dearpygui_internal

