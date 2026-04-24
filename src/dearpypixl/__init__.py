import sys as _sys

if "dearpygui" in _sys.modules:
    from dearpypixl.core import management as _management
    _management.warn(
        "`dearpypixl` should be imported before `dearpygui` — "
        "references to objects in `dearpygui` may be invalidated",
        stacklevel=2
    )
else:
    from dearpypixl.core import management as _management

from dearpypixl.core.protocols import mvBuffer as mvBuffer
from dearpypixl.core.protocols import mvVec4 as mvVec4
from dearpypixl.core.protocols import mvMat4 as mvMat4
from dearpypixl.core.appitem import AppItem as AppItem
from dearpypixl.core.appitem import ContainerItem as ContainerItem
from dearpypixl.core.appitem import ChildItem as ChildItem
from dearpypixl.core.appitem import CompositeItem as CompositeItem

if not _management._DPX_NO_INIT:
    from dearpypixl.lib.application import *
    from dearpypixl.lib.viewport import *
    from dearpypixl.lib.items import *
    from dearpypixl.lib.constants import *
    from dearpypixl.lib.functions import *  # must be last to pull any patched API

del _sys, _management
