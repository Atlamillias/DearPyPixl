from dearpypixl.menu import *
from dearpypixl import api, items, Runtime, Application, Viewport, console, constants


with ContextMenu("Root") as menu:
    ContextItem("Open File...##Ctrl+O")
    ContextItem("Open Folder...##Ctrl+K Ctrl+O")

    with ContextMenu("Open Recent"):
        ContextItem(r"C:\Users\..\w8w09xtm8jmb1.png")
        ContextItem(r"C:\Users\..\5cliellv0anb1.jpg")
        ContextItem(r"C:\Users\..\esz3b7bs4olb1.png")
        ContextItem(r"C:\Users\..\3iz7qyk1fplb1.jpg")

    items.mvSeparator(label='-')
    ContextItem("Save##Ctrl+S")
    ContextItem("Save As...##Ctrl+Shift+S", callback=lambda: print(api.Viewport.active_window()))
    items.mvSeparator(label='-')

    with ContextMenu("Preferences"):
        ContextItem('...')
        ContextItem('...')
        items.mvSeparator(label='-')
        ContextItem('...')
        ContextItem('...')
    items.mvSeparator(label='-')
    ContextItem("Exit##Ctrl+Alt+F4", callback=lambda: Runtime.stop())


with items.mvHandlerRegistry():
    items.mvMouseClickHandler(constants.MouseInput.R, callback=menu.to_cursor)








console.InteractivePython(globals())



Runtime.start(debug_aware=True)
