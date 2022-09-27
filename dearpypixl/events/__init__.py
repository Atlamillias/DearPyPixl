from .events import AppEvents, ItemEvents, FrameEvents, Callback
from .keycodes import Key, Mouse
from . import handlers
from ..application import Application as _App, AppStateKey as _AppStateKey


_App.__itemdict__[_AppStateKey.FRAME_EVENTS] = FrameEvents(locked=True)
