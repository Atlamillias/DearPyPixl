from contextlib import contextmanager
from dearpygui import _dearpygui, dearpygui
from pixle.tools.dpgtools import (
    show_about,
    show_debug,
    show_documentation,
    show_font_manager,
    show_item_registry,
    show_metrics,
    show_style_editor
)
from pixle.tools.pyconsole import PyConsole
from pixle.tools.appinfo import AppInfo



@contextmanager
def stage():
    """Temporarily sets staging mode. An item created in staging mode
    is not rendered and has limited functionality until its `unstage`
    method is called. Useful for creating items within existential
    paradoxes -- For example; a `Button` item where the parent does
    not exist at the time of the button's creation.

    Yields:
        None
    """
    try:
        yield _dearpygui.set_staging_mode(True)
    finally:
        _dearpygui.set_staging_mode(False)


@contextmanager
def mutex():
    """Locks the mutex within context of this call. Mutex is unlocked
    once out-of-scope.

    Yields:
        None
    """
    try:
        yield _dearpygui.lock_mutex()
    finally:
        _dearpygui.unlock_mutex()
