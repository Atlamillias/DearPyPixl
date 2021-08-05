import sys


def set_transparent_color(): return NotImplemented

def restore_color(): return NotImplemented

def enable_virtual_scaling(): return NotImplemented

def disable_virtual_scaling(): return NotImplemented


if sys.platform == "win32":
    from . import windows

    set_transparent_color = windows.set_transparent_color
    restore_color = windows.restore_color
    enable_virtual_scaling = windows.enable_virtual_scaling
    disable_virtual_scaling = windows.disable_virtual_scaling
