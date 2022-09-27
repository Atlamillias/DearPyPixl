from dearpygui import _dearpygui
from .font import (
    FontRangeHintValue,

    FontRangeHint,
    FontRange,
    FontChars,
    FontCharRemap,

    Font,
    FontRegistry,
    FontFamily,
)
from .presets import _dpg_internal_font
from ..application import Application as _App, AppStateKey as _AppStateKey


_App.__itemdict__[_AppStateKey.DEFAULT_FONT] = _dpg_internal_font
_App.configure(font=_dpg_internal_font)
