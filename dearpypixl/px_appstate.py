"""Contains DearPyGui's untracked global states.

This is an internal module, and its contents may change without warning.
"""
from .px_typing import DPGCallback, Any

# The settings below are, for whatever reason, not exposed via DPG. Several
# DPG functions have been monkeypatched (see`px_patcher.py`) to update the
# variables below so high-level modules (`runtime.py`, etc.) *can* expose them.
#
# To add a global state, a default value for the state should be set in this
# module. Then, a DPG function needs to be patched to update the value.
# Optionally, update `px_typing.py` structures to include the new setting.

_APPLICATION_THEME : int | str | None = None     # `bind_theme`
_APPLICATION_FONT  : int | str | None = None     # `bind_font`
_APPLICATION_SET_UP:  bool            = False    # `setup_dearpygui` (once and never again)

_VIEWPORT_PRIMARY_WINDOW    : int | str | None   = None   # `set_primary_window`
_VIEWPORT_USE_PRIMARY_WINDOW: bool               = False  # `set_primary_window`
_VIEWPORT_RESIZE_CALLBACK   : DPGCallback | None = None   # `set_viewport_resize_callback`
_VIEWPORT_USER_DATA         : Any                = None   # `set_viewport_resize_callback`
_VIEWPORT_CREATED           : bool               = False  # `create_viewport` (once and never again)
_VIEWPORT_FULLSCREEN        : bool               = False  # `toggle_viewport_fullscreen`
