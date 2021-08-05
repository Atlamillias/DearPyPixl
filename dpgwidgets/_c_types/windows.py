import ctypes
from ctypes import wintypes


class cWin32:
    """Misc. imports from ctypes module (Windows)."""
    EnumWindowsProc = ctypes.WINFUNCTYPE(
        ctypes.c_bool,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int)
    )
    EnumChildProc = ctypes.WINFUNCTYPE(
        ctypes.c_bool,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int)
    )
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumChildWindows = ctypes.windll.user32.EnumChildWindows
    GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

########################################
############### C Types ################
########################################
WINFUNCTYPE = ctypes.WINFUNCTYPE
HWND = wintypes.HWND
BOOL = wintypes.BOOL
COLORREF = wintypes.COLORREF
BYTE = wintypes.BYTE
DWORD = wintypes.DWORD
LONG = wintypes.LONG
NULL = 0

########################################
########## Function factories###########
########################################
def _get_func_GetLayeredWindowAttributes():
    _func = WINFUNCTYPE(
        BOOL,
        HWND,
        COLORREF,
        BYTE,
        DWORD
    )
    return _func(
        ("SetLayeredWindowAttributes", ctypes.windll.user32),
        ((1, "hwnd"), (1, "*pcrKey", NULL), (1, "*pbAlpha", NULL), (1, "*pdwFlags", NULL)),
    )
def _get_func_SetLayeredWindowAttributes():
    _func = WINFUNCTYPE(
        BOOL,
        HWND,
        COLORREF,
        BYTE,
        DWORD
    )
    return _func(
        ("SetLayeredWindowAttributes", ctypes.windll.user32), 
        ((1, "hwnd"),(1, "crKey"),(1, "bAlpha"),(1, "dwFlags")),
    )
def _get_func_SetWindowLongA():
    _func = WINFUNCTYPE(
        LONG,
        HWND,
        ctypes.c_int,
        LONG,
    )
    return _func(
        ("SetWindowLongA", ctypes.windll.user32), 
        ((1, "hwnd"),(1, "nIndex"),(1, "dwNewLong"))
    )
def _get_func_GetWindowLongA():
    _func = WINFUNCTYPE(
        LONG,
        HWND,
        ctypes.c_int,
    )
    return _func(
        ("GetWindowLongA", ctypes.windll.user32), 
        ((1, "hwnd"), (1, "nIndex"))
    )

########################################
########## Py-wrapped C funcs###########
########################################
_GetWindowLongA = _get_func_GetWindowLongA()
_SetWindowLongA = _get_func_SetWindowLongA()
_GetLayeredWindowAttributes = _get_func_GetLayeredWindowAttributes()
_SetLayeredWindowAttributes = _get_func_SetLayeredWindowAttributes()

def _EnumWindows() -> list[HWND]:
    handles = []

    def callback(hwnd, lparam):
        handles.append(hwnd)
        return True

    cWin32.EnumWindows(cWin32.EnumWindowsProc(callback), 0)
    return handles

def EnumWindows(hwnd: HWND = None):
    if not hwnd:
        return _EnumWindows()
    handles = []

    def callback(hwnd, lparam):
        handles.append(hwnd)
        return True

    cWin32.EnumChildWindows(hwnd, cWin32.EnumChildProc(callback), 0)
    return handles

def GetForegroundWindow() -> HWND:
    return cWin32.GetForegroundWindow()

def GetWindowTitle(hwnd: HWND) -> str:
    handles = EnumWindows()
    for h in handles:
        if h == hwnd:
            text_len = cWin32.GetWindowTextLength(h) + 1
            buffer = ctypes.create_unicode_buffer(text_len)
            cWin32.GetWindowText(h, buffer, text_len)
            return buffer.value
    return None

def GetWindowsAndTitles(parent_hwnd: HWND = None, visible_only: bool = True) -> list[tuple[HWND, str]]:
    handles = EnumWindows(parent_hwnd)
    _return = []
    for h in handles:
        if visible_only and not cWin32.IsWindowVisible(h):
            continue
        text_len = cWin32.GetWindowTextLength(h) + 1
        buffer = ctypes.create_unicode_buffer(text_len)
        cWin32.GetWindowText(h, buffer, text_len)
        _return.append((h, buffer.value))
    return _return

def GetLayeredWindowAttributes(hwnd: HWND, rgba: tuple = None, flag: DWORD = None):
    args = [hwnd]
    if rgba and len(rgba) == 4:
        *rgb, alpha = rgba
        rgb = wintypes.RGB(*rgb)
        args += [rgb, alpha]
    elif rgba:
        rgb = wintypes.RGB(*rgba)
        alpha = NULL
        args += [rgb]
    else:
        rgb = NULL
        alpha = NULL

    if flag:
        args.append(flag)

    return _GetLayeredWindowAttributes(hwnd, *args)

def SetLayeredWindowAttributes(hwnd: HWND, rgba: tuple[int,int,int,int], flag: DWORD):
    *rgb, alpha = rgba
    rgb = wintypes.RGB(*rgb)
    _SetLayeredWindowAttributes(hwnd, rgb, alpha, flag)




#########################################################################################
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#########################################################################################

__all__ = [
    "set_transparent_color",
    "restore_color",
    "disable_virtual_scaling",
    "enable_virtual_scaling",
]

APP_HANDLE = NULL
ATTR_IS_SET = False

WS_EX_LAYERED = 0x00080000  # layered window
GWL_EXSTYLE = -20  # "extended window style"

LWA_COLORKEY: DWORD = 0x00000001
LWA_ALPHA: DWORD = 0x00000002


def _setup():  # NOTE: call on conditional
    global ATTR_IS_SET, APP_HANDLE

    ATTR_IS_SET = True
    APP_HANDLE = cWin32.GetForegroundWindow()
    _SetWindowLongA(
        APP_HANDLE,
        GWL_EXSTYLE,
        _GetWindowLongA(APP_HANDLE, GWL_EXSTYLE) | WS_EX_LAYERED
    )


def set_transparent_color(rgb: tuple[int, int, int]):
    """Sets a color to be transparent. Anything painted that color
    will be transparent instead. Transparent parts of items can
    be clicked through. Only one color can be set as transparent
    at a time - the old one will be unset for subsequent calls.

    NOTE: If the application is intended to be an overlay, make sure
    to set `Viewport().always_on_top` to True.

    Args:
        rgb (tuple[int, int, int]): The color that will be transparent.

    """
    global ATTR_IS_SET, LWA_COLORKEY

    if ATTR_IS_SET is False:
        _setup()
    SetLayeredWindowAttributes(APP_HANDLE, rgb + (255,), LWA_COLORKEY)


def restore_color():
    """Removes the transparency from the set transparent color
    i.e. color is no longer transparent.

    """
    global ATTR_IS_SET, LWA_COLORKEY

    if ATTR_IS_SET is False:
        return
        
    SetLayeredWindowAttributes(APP_HANDLE, (255,255,255), 255, LWA_ALPHA)


def disable_virtual_scaling():
    """Ignore the 'Scale and layout' display setting in Windows
    for this process. Recommended.

    """

    ctypes.windll.shcore.SetProcessDpiAwareness(2)


def enable_virtual_scaling():
    """Use the current 'Scale and layout' display setting in Windows
    for this process. Renders may suffer from quality loss (from being
    stretched), and may also affect how well items scale within the
    application window.

    """

    ctypes.windll.shcore.SetProcessDpiAwareness(0)
