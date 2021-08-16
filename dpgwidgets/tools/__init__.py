from typing import Any
import datetime

from dearpygui import dearpygui as dpg
from dearpygui.logger import mvLogger as Logger

from dpgwidgets import Application
from dpgwidgets.tools.pyconsole import PyConsole
from dpgwidgets.libsrc.containers import Window, Group, Child
from dpgwidgets.libsrc.widgets import Button, Text


__all__ = [
    "PyConsole",
    "show_developer_window",
    # these are mostly copy/paste from DPG
    # need to make my own implementations of these tools
    "show_about",
    "show_documentation",
    "show_metrics",
    "show_debug",
    "show_font_manager",
    "show_item_registry",
    "show_logger",
]


def show_developer_window():
    """Renders a window that allows users to launch a variety of helpful
    tools.
    """
    with Window("Dev Tools", width=310, no_move=False, no_close=True, no_resize=False) as dev:
        dev.pos = (Application.width - dev.width - 20, 20)
        dev.height = Application.height - 70

        dev.theme_style.window_padding = 5, 5
        dev.theme_color.title_bg = (
            0.14 * 255, 0.14 * 255, 0.14 * 255, 1.00 * 255)
        dev.theme_color.window_bg = (0.06 * 255, 0.06 * 255, 0.06 * 255, 125)
        dev.theme_color.title_bg_active = (
            0.14 * 255, 0.14 * 255, 0.14 * 255, 1.00 * 255)

        with Child(height=200):
            fields = ("Mouse POS", "Runtime",
                      "Frames (all)", "Frames (/s)",
                      "Key Input",
                      "Mouse Input"
                      )
            with Group(width=50) as headers:
                [Text(f) for f in fields]
            dpg.add_same_line(spacing=5)
            with Group():
                [Text(": ") for f in fields]
            dpg.add_same_line(spacing=5)
            with Group() as info:
                mouse_pos = Text("")
                runtime = Text("")
                frames = Text("")
                framerate = Text("")
                keycode = Text("")
                mousekey = Text("")
                

        btn_width = dev.width - 10
        Button("Documentation", callback=dpg.show_documentation, width=btn_width)
        Button("Debug", callback=dpg.show_debug, width=btn_width)
        Button("Style Editor", callback=dpg.show_style_editor, width=btn_width)
        Button("Metrics", callback=dpg.show_metrics, width=btn_width)
        Button("About", callback=dpg.show_about, width=btn_width)
        Button("Font Manager", callback=dpg.show_font_manager, width=btn_width)
        Button("Item Registry", callback=dpg.show_item_registry, width=btn_width)
        Button("Logger", callback=lambda: Logger(), width=btn_width)

    @Application.on_resize
    def devwin_pos():
        dev.pos = (Application.width - dev.width - 20, 20)
        dev.height = Application.height - 70

    @Application.on_render
    def update_dev():
        x, y = Application.get_mouse_pos(local=False)
        mouse_pos.value = f"{x}, {y}"
        runtime.value = f"{datetime.timedelta(seconds=Application.runtime())}"
        frames.value = f"{Application.frame_count()}"
        framerate.value = f"{Application.framerate()}"

    # Keyboard polling
    KeysDown = []
    @Application.on_key_press
    def capture_key(sender, sender_data):
        if sender_data not in KeysDown:
            KeysDown.append(sender_data)

        keycode.value = f"{KeysDown[-1]} ({chr(sum(KeysDown))})"

    @Application.on_key_up
    def clear_key(sender, sender_data):
        KeysDown.remove(sender_data)

        if KeysDown:
            keycode.value = f"{KeysDown[-1]} ({chr(sum(KeysDown))})"
        else:
            keycode.value = ""


    # Mouse polling
    MouseDown = []
    @Application.on_mouse_click
    def capture_mouse(sender, sender_data):
        if sender_data not in MouseDown:
            MouseDown.append(sender_data)

        mousekey.value = MouseDown[-1]

    @Application.on_mouse_up
    def clear_mouse(sender, sender_data):
        MouseDown.remove(sender_data)

        if KeysDown:
            mousekey.value = KeysDown[-1]

        else:
            mousekey.value = ""

        


def show_style_editor(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Style)


def show_metrics(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Metrics)


def show_about(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_About)


def show_debug(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Debug)


def show_documentation(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Doc)


def show_font_manager(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_Font)


def show_item_registry(sender: str = "", data: Any = None):
    dpg.show_tool(dpg.mvTool_ItemRegistry)


def show_logger(sender: str = "", data: Any = None):
    from dearpygui import logger
    logger.mvLogger()
