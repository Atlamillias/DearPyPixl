import sys
import warnings
import importlib
import importlib.util
import importlib.metadata

# HACK: DPX uses a custom `generate_uuid` function. This patch
# is necessary to ensure the C++ side doesn't auto-increment its
# internal uuid counter (reserved uuids aside).
if 'dearpygui.dearpygui' in sys.modules:
    warnings.warn((
        "Importing `dearpygui` before importing `dearpypixl` may cause "
        "issues. Please consider re-arranging your imports."
    ))

# Get the full path to 'dearpygui.dearpygui'. Unfortunately, this
# requires importing it...
from dearpygui import dearpygui
_fpath = dearpygui.__file__
with open(_fpath, 'r') as file:  # type: ignore
    _patch_src = file.read().replace(
        "tag=tag", "tag=(tag or internal_dpg.generate_uuid())"
    )
del dearpygui  # type: ignore
importlib.invalidate_caches()

dearpygui = importlib.util.module_from_spec(
    importlib.util.spec_from_loader(  # type: ignore
        'dearpygui.dearpygui', None
    )
)
dearpygui.__file__ = _fpath
exec(_patch_src, dearpygui.__dict__)
# The default loader caches submodules in the package namespace.
# It needs to be reset, too.
sys.modules['dearpygui'].dearpygui = sys.modules['dearpygui.dearpygui'] = dearpygui  # type: ignore

from . import api  # bulk patching


from .api import (
    Application as Application,
    Viewport as Viewport,
    Runtime as Runtime,
    Registry as Registry,
)
from .items import *
