from typing import Any
from dearpygui import dearpygui


def show_style_editor(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_Style)


def show_metrics(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_Metrics)


def show_about(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_About)


def show_debug(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_Debug)


def show_documentation(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_Doc)


def show_font_manager(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_Font)


def show_item_registry(sender: str = "", data: Any = None):
    dearpygui.show_tool(dearpygui.mvTool_ItemRegistry)


#def show_logger(sender: str = "", data: Any = None):
#    from dearpygui import logger
#    logger.mvLogger()
