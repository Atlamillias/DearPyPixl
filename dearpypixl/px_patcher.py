"""DearPyGui monkeypatcher module.

Replaces various functions in `dearpygui` library. Reasons for the replacement
vary between functions, but most are to accomodate for missing critical features,
bug fixes, or to include exceptions when the result of calling the function would
be irregular, misleading, or undesireable.

From a user's perspective, patched functions do not operate differently from the
original implementations, nor do they manipulate arguments or return values.
"""
import sys
import itertools
import inspect
from dearpygui import dearpygui, _dearpygui
from .px_typing import DPGCallback, Callable, Sequence, Any, TypeVar
from . import px_appstate as _appstate




_T = TypeVar("_T")


PATCHED_COMMAND = "_dpx_patch_"


def patch_command(fn: _T) -> _T:
    dpg_fn  = getattr(dearpygui, fn.__name__)
    _dpg_fn = getattr(_dearpygui, fn.__name__, None)
    fn.__wrapped__   = dpg_fn if _dpg_fn is None else _dpg_fn
    fn.__doc__       = dpg_fn.__doc__
    fn.__signature__ = inspect.signature(dpg_fn)
    setattr(fn, PATCHED_COMMAND, True)
    return fn


def apply_patch():
    self_mod = sys.modules[__name__]
    for member in dir(self_mod):
        obj = getattr(self_mod, member)
        if not hasattr(obj, PATCHED_COMMAND):
            continue
        module = dearpygui if obj.__wrapped__ == getattr(dearpygui, obj.__name__, None) else _dearpygui
        setattr(module, obj.__name__, obj)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################# Monkeypatched DPG Functions #############################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# BUG (`generate_uuid`): Default implementation is very slow when creating items
# en masse. The below is a more performant alternative. Both users and dearpypixl
# MUST use the same implementation to avoid uuid collisions.
_dearpygui.generate_uuid = itertools.count(start=1_000).__next__
dearpygui.generate_uuid  = _dearpygui.generate_uuid


# BUG (`run_callbacks`): Default implementation assumes callbacks do not accept more
# than 3 arguments, nor does it consider variadic positionals. A callback that accepts
# `sender` `app_data` and `user_data` positional arguments and other (optional)
# keyword-only arguments will result in the former. A callback with a single variadic
# parameter will work, but will only receive `sender`.
@patch_command
def run_callbacks(jobs: Sequence[tuple[Callable | None, Any, Any, Any]]) -> None:
    if not jobs:
        return
    for callback, *args in jobs:
        try:
            parameters = tuple(inspect.signature(callback).parameters.values())
        except TypeError:
            if callback is None:
                continue
            raise
        # This should be 3 if `jobs` is the result of `get_callback_queue`. Could be
        # different if `jobs` was constructed by a user.
        dpg_args_count  = len(args)
        pos_param_count = 0
        for p in parameters:
            if pos_param_count >= dpg_args_count or p.kind in (p.KEYWORD_ONLY, p.VAR_KEYWORD):
                break
            elif p.kind == p.VAR_POSITIONAL:
                pos_param_count = dpg_args_count
                break
            pos_param_count += 1
        callback(*args[:pos_param_count])


@patch_command  # no getter for DPG setup state
def setup_dearpygui(**kwargs):
    if _appstate._APPLICATION_SET_UP:
        raise SystemError("DearPyGui already set up.")
    setup_dearpygui.__wrapped__()
    _appstate._APPLICATION_SET_UP = True


@patch_command
def bind_font(font: int | str, **kwargs) -> None:
    bind_font.__wrapped__(font or 0)
    _appstate._APPLICATION_FONT = font or None


@patch_command
def bind_theme(theme: int | str, **kwargs):
    bind_theme.__wrapped__(theme or 0)
    _appstate._APPLICATION_THEME = theme or None


@patch_command
def create_viewport(**kwargs):
    if _appstate._VIEWPORT_CREATED:
        raise SystemError("viewport already exists.")
    create_viewport.__wrapped__(**kwargs)
    _appstate._VIEWPORT_CREATED = True

create_viewport.__wrapped__ = dearpygui.create_viewport   # default kwargs


@patch_command
def set_primary_window(window: int | str, value: bool, **kwargs) -> None:
    set_primary_window.__wrapped__(window, value)
    _appstate._VIEWPORT_PRIMARY_WINDOW = window or None
    _appstate._VIEWPORT_USE_PRIMARY_WINDOW = bool(value)


@patch_command
def toggle_viewport_fullscreen(**kwargs) -> None:
    toggle_viewport_fullscreen.__wrapped__()
    _appstate._VIEWPORT_FULLSCREEN = not _appstate._VIEWPORT_FULLSCREEN


@patch_command
def maximize_viewport(**kwargs):
    if _appstate._VIEWPORT_FULLSCREEN:
        _dearpygui.toggle_viewport_fullscreen()
    maximize_viewport.__wrapped__()


@patch_command
def minimize_viewport(**kwargs):
    if _appstate._VIEWPORT_FULLSCREEN:
        _dearpygui.toggle_viewport_fullscreen()
    minimize_viewport.__wrapped__()


@patch_command
def show_viewport(**kwargs) -> None:
    if not _dearpygui.is_viewport_ok():
        show_viewport.__wrapped__(**kwargs)


@patch_command
def set_viewport_resize_callback(callback: DPGCallback | None, *, user_data: Any = None, **kwargs):
    set_viewport_resize_callback.__wrapped__(callback, user_data=user_data, **kwargs)
    _appstate._VIEWPORT_RESIZE_CALLBACK = callback
    _appstate._VIEWPORT_USER_DATA       = user_data



# XXX: This will probably be removed as there are not many performance-critical
# things that warrant optimizations.
def _apply_optimizations(mod = None) -> None:

    import sys
    from . import grid

    if not mod and sys.platform() != "win32":
        return
    try:
        from . import _dearpypixl
    except:
        return

    grid._draw_cells = _dearpypixl.grid.draw_cells
