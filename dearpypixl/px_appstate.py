"""Contains DearPyGui's untracked global states."""

# This is the closest thing this lib has to an internal-only module. The
# settings below are not normally exposed via DPG -- Several DPG functions
# have been monkeypatched to update the globals below (see`px_patcher.py`)
# so high-level modules (`runtime.py`, etc.) *can* expose them.

_APPLICATION_THEME  : int | str | None = None     # |- no getter, set via `bind_theme`/`bind_font` (patched)
_APPLICATION_FONT   : int | str | None = None     # |
_APPLICATION_PREPPED: bool             = False    # no getter, set once via `setup_dearpygui` (patched) and never again

_VIEWPORT_PRIMARY_WINDOW    : int | str | None = None   # |- no getter, set via `set_primary_window` (patched)
_VIEWPORT_USE_PRIMARY_WINDOW: bool             = False  # |
_VIEWPORT_CREATED           : bool             = False  # no getter, set once via `create_viewport` (patched) and never again
_VIEWPORT_FULLSCREEN        : bool             = False  # no getter, set via `toggle_viewport_fullscreen` (patched)
