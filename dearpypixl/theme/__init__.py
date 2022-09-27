
from .element import (
    RGBA,
    XY,

    ThemeElementType,
    ItemState,

    ThemeElement,
)
from .theme import Theme
from .presets import _dpg_internal_theme
from ..application import Application as _App, AppStateKey as _AppStateKey


_App.__itemdict__[_AppStateKey.DEFAULT_THEME] = _dpg_internal_theme
_App.configure(theme=_dpg_internal_theme)
