""""""
_is_initialized: bool = False


def initialize_dearpypixl():
    """Perform setup for DearPyGui and DearPyPixl if it has not been
    done already. Does nothing if already initialized.
    """
    if _is_initialized is False:
        from dearpygui import dearpygui
        # Prepare DearPyGui for use.
        dearpygui.create_context()
        dearpygui.create_viewport()  # created but not shown
        dearpygui.setup_dearpygui()
        dearpygui.configure_viewport("DPG NOT USED YET", title="Application")
        # DearPyPixl does not expose this registry. The `Font` class
        # manages all font-related items on its own. All this does is
        # create a default parent for font items.
        # TODO: Probably move this to the `Font` class. Once it's refactored...
        dearpygui.add_font_registry(tag=dearpygui.mvReservedUUID_0)


def cleanup_dearpypixl():
    """Release resources and destroy contexts used by DearPyGui.
    Does nothing if not initialized.
    """
    if _is_initialized is True:
        from dearpygui import dearpygui
        try:
            dearpygui.destroy_context()
        except:
            pass


# I try to avoid calls to dearpygui on dearpypixl module/package import, but
# initializing before the imports just to be safe because it's annoying to debug an
# on-import segfault.
initialize_dearpypixl()


from dearpypixl.application.application import Application
from dearpypixl.application.viewport import Viewport
from dearpypixl.components import (
    AppEvents,
    ItemEvents
)
# Item classes are registered when they are created. Importing each module
# ensures that they are registered. Otherwise, they may not exist in the
# registry when they are required. 

# BUG: importing the `colors` module is somehow a circular import, yet
# all of the modules below have the identical structure and import fine.
from dearpypixl import (
    # item modules
    basic,
    containers,
    colors,
    drawing,
    misc,
    nodes,
    plotting,
    tables,
    textures,
    values,
    themes,

    # misc modules
    constants,
)
