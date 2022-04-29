import ctypes
import functools
from ctypes import wintypes
from dearpygui import dearpygui


__all__ = [
    "toggle_dpg_viewport_transparency",
    "toggle_process_dpi_awareness",
]


# Wintypes
_WINFUNCTYPE = ctypes.WINFUNCTYPE
_HWND = wintypes.HWND
_BOOL = wintypes.BOOL
_COLORREF = wintypes.COLORREF
_BYTE = wintypes.BYTE
_DWORD = wintypes.DWORD
_LONG = wintypes.LONG
_NULL = 0


# For color transparency
_APP_HANDLE = _NULL
_ATTR_IS_SET = False

_WS_EX_LAYERED = 0x00080000  # layered window
_GWL_EXSTYLE = -20  # "extended window style"

_LWA_COLORKEY: _DWORD = 0x00000001
_LWA_ALPHA: _DWORD = 0x00000002


# High-level functions use these
_is_transparent = False
_dpi_scaling    = True


# C "Structs"
def _get_func_GetLayeredWindowAttributes():
    _func = _WINFUNCTYPE(_BOOL, _HWND, _COLORREF, _BYTE, _DWORD)
    return _func(
        ("SetLayeredWindowAttributes", ctypes.windll.user32),
        ((1, "hwnd"), (1, "*pcrKey", _NULL),
         (1, "*pbAlpha", _NULL), (1, "*pdwFlags", _NULL)),
    )


def _get_func_SetLayeredWindowAttributes():
    _func = _WINFUNCTYPE(_BOOL, _HWND, _COLORREF, _BYTE, _DWORD)
    return _func(
        ("SetLayeredWindowAttributes", ctypes.windll.user32),
        ((1, "hwnd"), (1, "crKey"), (1, "bAlpha"), (1, "dwFlags")),
    )


def _get_func_SetWindowLongA():
    _func = _WINFUNCTYPE(_LONG, _HWND, ctypes.c_int, _LONG)
    return _func(
        ("SetWindowLongA", ctypes.windll.user32),
        ((1, "hwnd"), (1, "nIndex"), (1, "dwNewLong"))
    )


def _get_func_GetWindowLongA():
    _func = _WINFUNCTYPE(
        _LONG,
        _HWND,
        ctypes.c_int,
    )
    return _func(
        ("GetWindowLongA", ctypes.windll.user32),
        ((1, "hwnd"), (1, "nIndex"))
    )


# Raw py-wrapped windll commands
_GetWindowLongA = _get_func_GetWindowLongA()
_SetWindowLongA = _get_func_SetWindowLongA()
_GetLayeredWindowAttributes = _get_func_GetLayeredWindowAttributes()
_SetLayeredWindowAttributes = _get_func_SetLayeredWindowAttributes()


def GetLayeredWindowAttributes(hwnd: _HWND, rgba: tuple = None, flag: _DWORD = None):
    args = [hwnd]
    if rgba and len(rgba) == 4:
        *rgb, alpha = rgba
        rgb = wintypes.RGB(*rgb)
        args += [rgb, alpha]
    elif rgba:
        rgb = wintypes.RGB(*rgba)
        alpha = _NULL
        args += [rgb]
    else:
        rgb = _NULL
        alpha = _NULL

    if flag:
        args.append(flag)

    return _GetLayeredWindowAttributes(hwnd, *args)


def SetLayeredWindowAttributes(hwnd: _HWND, rgba: tuple[int, int, int, int], flag: _DWORD):
    *rgb, alpha = rgba
    rgb = wintypes.RGB(*rgb)
    _SetLayeredWindowAttributes(hwnd, rgb, alpha, flag)


def _setup():  # NOTE: call on conditional
    global _ATTR_IS_SET, _APP_HANDLE

    _ATTR_IS_SET = True
    _APP_HANDLE = ctypes.windll.user32.GetForegroundWindow()
    # Set placeholder int32 value in memory for `index`.
    _SetWindowLongA(
        _APP_HANDLE,  # window handle
        _GWL_EXSTYLE, # index i.e. attribute to change
        # replacement value
        _GetWindowLongA(_APP_HANDLE, _GWL_EXSTYLE) | _WS_EX_LAYERED
    )

def _check_setup(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        global _ATTR_IS_SET

        if _ATTR_IS_SET is False:
            _setup()
        return func(*args, **kwargs)
    return wrapped


# High-level functions
@_check_setup
def set_transparent_color(rgb: tuple[int, int, int] = (0, 0, 0)) -> None:
    """Applies 100% transparency to <rgb>. A application window using
    this value as it's clear color ("background") will also be transparent.
    This may cause other renders of the same color within the application
    window to also be transparent.

    Args:
        rgb (tuple[int, int, int]): The color that will be transparent.

    # NOTE: This will bork the functionality of the window title bar,
    and does not hide it. Calling `unset_transparent_color` should restore
    functionality.

    # NOTE: Make certain that this call is scheduled AFTER your application/
    viewport has been made and is showing.
    """
    global _LWA_COLORKEY, _is_transparent

    _is_transparent = True
    SetLayeredWindowAttributes(_APP_HANDLE, rgb + (255,), _LWA_COLORKEY)


@_check_setup
def unset_transparent_color() -> None:
    """Removes the effects of `set_transparent_color`.

    NOTE: From my observations the window (title bar included) operate
    perfectly fine. That does not mean side-effects do not exist.
    """
    global _LWA_COLORKEY, _LWA_ALPHA, _is_transparent

    # Do nothing...?
    if _is_transparent is False:
        return None
    _is_transparent = False
    SetLayeredWindowAttributes(_APP_HANDLE, (255, 255, 255, 255), _LWA_ALPHA)

import win32gui
win32gui.SetLayeredWindowAttributes


# For DearPyPixl
def toggle_dpg_viewport_transparency(
    *,
    rgb: tuple[int] = (73, 59, 16),
    always_on_top: bool = True
) -> None:
    """Applies 100% transparency to the color <rgb>, as well as various
    configuration settings to the DearPyGui viewport to help ensure that
    it remains fully functional. `clear_color` will be set to the value 
    of <rgb>, `decorated` will be set to False, and `always_on_top` to
    <always_on_top>. The viewport will also be maximized. Keep in mind
    that you will not have access to the viewport title bar to close the
    application -- set another means of doing so via `stop_dearpygui` or
    using the taskbar.

    If the "transparency" effect is already applied, it will be removed
    and ...

    The "strange" rgb default value of (69, 59, 9) is intentional -- It
    is possible that other renders of the exact same color within the
    application window will also be affected by the transparency setting,
    and the default value is a color that DearPyGui does not use for its
    defaults (while also just being a rather unpleasant color in my opinion).


    NOTE: Call this AFTER showing the viewport via `dearpygui.show_viewport`.
    Otherwise, the color transparency setting may affect the wrong
    application window...

    Args:
        * rgb (tuple, optional): The color that will not be painted. Default
        is (73, 59, 16).
        * always_on_top (bool, optional): If True, the DearPyGui viewport
        will be rendered above all other application windows. Default is True.
    """
    viewport = "DPG NOT USED YET"
    # Applying the effect if it's not applied.
    if _is_transparent is False:
        # `clear_color` must match `rgb` so it won't be painted by Windows.
        #
        # `decorated` *should* be set to False to hide the title bar and viewport
        # border. The transparency adjustment completely breaks the functionality
        # of the title bar, the border, and the title bar buttons. Trying to
        # use them can cause weird errors.
        #
        # `always_on_top` is True by default because this "hack" is typically
        # desired to create overlays, but is exposed to the user as a parameter
        # if this is not the case.
        configuration = {
                        "clear_color": rgb,
                        "always_on_top": always_on_top,
                        "decorated": False
                        }
        # The viewport is maximized because appitems can become lost when dragged
        # outside of the drawn viewport area. I have also observed some generally
        # undesirable effects/bugs when dragging an item, like window item, to
        # and from the drawn viewport boundries such as a less unresponsive UI
        # and fubar'd renders. I've never observed this while interacting with
        # the UI while its maximized, and the application can still be minimized
        # using the taskbar.

        # Applying the color to not be painted.
        dearpygui.maximize_viewport()
        set_transparent_color(rgb)
        return dearpygui.configure_viewport(viewport, **configuration)
    # Otherwise, revert the effect. Leave the viewport maximized.
    # NOTE: Any arguments passed to this func are ignored for this.
    dearpygui.configure_viewport(
        viewport,
        decorated=True,
        always_on_top=False,
        clear_color=(0,0,0,255)  # DPG default. Not many people change it anyway.
    )
    unset_transparent_color()
    dearpygui.maximize_viewport()



def toggle_process_dpi_awareness():
    if _dpi_scaling:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    else:
        ctypes.windll.shcore.SetProcessDpiAwareness(0)
