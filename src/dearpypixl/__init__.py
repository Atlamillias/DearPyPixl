import sys as _sys

if "dearpygui" in _sys.modules:
    from dearpypixl.core import management as _management
    _management.warn(
        "`dearpypixl` should be imported before `dearpygui` — "
        "references to objects in `dearpygui` may be invalidated",
        stacklevel=2
    )
    del _management

del _sys


from dearpypixl.core.protocols import mvBuffer
from dearpypixl.core.protocols import mvVec4
from dearpypixl.core.protocols import mvMat4
from dearpypixl.core.appitem import AppItem
from dearpypixl.core.appitem import ContainerItem
from dearpypixl.core.appitem import ChildItem
from dearpypixl.core.appitem import CompositeItem

from dearpypixl.lib.application import *
from dearpypixl.lib.viewport import *
from dearpypixl.lib.items import *
from dearpypixl.lib.constants import *
from dearpypixl.lib.functions import *  # must be last to pull any patched API
