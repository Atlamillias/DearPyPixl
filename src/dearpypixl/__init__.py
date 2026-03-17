import sys as _sys
from dearpypixl.core import management as _management

if "dearpygui" in _sys.modules:
    _management.warn(
        "`dearpypixl` should be imported before `dearpygui` — "
        "references to objects in `dearpygui` may be invalidated",
        stacklevel=2
    )

del _sys, _management


from dearpypixl.lib import *
from dearpypixl import lib as _lib
globals()["__all__"] = getattr(_lib, "__all__")
