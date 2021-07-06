from inspect import signature
from dearpygui import dearpygui as dpg, core as idpg


# To-do: 
# - Edit misc info in __init__.py
# - Encapsulate file info (imports, etc) w/mappings


class ItemMaps:
    @classmethod
    def item_categories(cls):
        attrs = []
        for attr in dir(cls):
            if "__" in attr:
                continue
            elif attr in ("registered_cmds", "items"):
                continue
            elif type(getattr(cls, attr)) != dict:
                continue
            attrs.append(attr)
        return attrs

    @classmethod
    def commands(cls):
        cmds = (getattr(cls, item) for item in cls.item_categories())
        return {cmd[-1] for sublist in cmds for cmd in sublist.values()}


    # Only container items need to be specifically listed.
    # Remaining items are inferred from their function
    # name.

    # The pre-populated items are all "containers". They are
    # organized into categories. They are populated as:
    # "Item": ("baseclasses", "dpg_command"). Even though the
    # items hard-coded below are all containers, some inherit
    # from "Item, Context" which is basically the "Container"
    # class without "extras" (handlers, themes, etc). Items that
    # subclass the Item and Context classes add those extras to 
    # items subclassing Container and Widget.

    containers = {
        "Child": ("Container", "add_child",),
        "Clipper": ("Container", "add_clipper"),
        "CollapsingHeader": ("Container", "add_collapsing_header"),
        "DragPayload": ("Container", "add_drag_payload"),
        "FileDialog": ("Container", "add_file_dialog"),
        "FilterSet": ("Container", "add_filter_set"),
        "Group": ("Container", "add_group"),
        "Menu": ("Container", "add_menu"),
        "MenuBar": ("Container", "add_menu_bar"),
        "StagingContainer": ("Container", "add_staging_container"),
        "Tab": ("Container", "add_tab"),
        "TabBar": ("Container", "add_tab_bar"),
        "Table": ("Container", "add_table"),
        "TableRow": ("Container", "add_table_row"),
        "Tooltip": ("Container", "add_tooltip"),
        "TreeNode": ("Container", "add_tree_node"),
        "Window": ("Container", "add_window"),
    }
    widgets = {}
    drawing = {
        "ViewportDrawlist": ("Container", "add_viewport_drawlist"),
        "Drawlist": ("Container", "add_drawlist"),
        "DrawLayer": ("Container", "add_draw_layer"),
    }
    plotting = {
        "Plot": ("Container", "add_plot")
    }
    node = {
        "Node": ("Container", "add_node"),
        "NodeAttribute": ("Container", "add_node_attribute"),
        "NodeEditor": ("Container", "add_node_editor"),
    }
    valueitems = {}
    registries = {
        "FontRegistry": ("Item, Context", "add_font_registry"),
        "HandlerRegistry": ("Item, Context", "add_handler_registry"),
        "TextureRegistry": ("Item, Context", "add_texture_registry"),
        "ValueRegistry": ("Item, Context", "add_value_registry"),
    }
    handlers = {}
    stylize = {
        "Theme": ("Item, Context", "add_theme"),
        "Font": ("Item, Context", "add_font"),
    }


DPG_CONSTANTS = {}

def _organize(mapping: dict):
    mapping = sorted(mapping.items(), key=lambda x: x[1][0])
    return mapping


def populate():
    def name_fix(string):
        if string[0].isdigit():
            return string[2:]
        return string

    # iterating dearpygui
    for attr in dir(idpg):
        # undesirables
        if not any(attr.startswith(kw) for kw in ("add_", "draw_", "mv")):
            continue
        if "mutex" in attr or attr in ItemMaps.commands():
            continue

        if attr.startswith("add_"):
            name = attr.replace("add_", "").title().replace("_","")
            if attr.startswith("add_node_"):
                mapping, info = ItemMaps.node, ("Widget", attr)
            elif attr.endswith("_registry"):
                mapping, info = ItemMaps.registries, ("Item, Context", attr)
            elif attr.endswith("_value"):
                mapping, info = ItemMaps.valueitems, ("Item", attr)
            elif attr.endswith("_handler"):
                mapping, info = ItemMaps.handlers, ("Item", attr)
            elif any(kw in attr for kw in ("theme", "font")):
                mapping, info = ItemMaps.stylize, ("Item", attr)
            elif any(kw in attr for kw in ("plot", "series")):
                mapping, info = ItemMaps.plotting, ("Widget", attr)
            else:
                mapping, info = ItemMaps.widgets, ("Widget", attr)
            mapping[name_fix(name)] = info

        elif attr.startswith("draw_"):
            name = attr.replace("draw_", "").title().replace("_","")
            ItemMaps.drawing[name_fix(name)] = "Widget", attr

        elif attr.startswith("mv"):
            DPG_CONSTANTS[attr.replace("mv","")] = attr

        else:
            print(attr,":", attr)



def writefiles():
    def indent(indents: int = 1):
        ind = "    " * indents
        return ind

    dirname = "dpgwidgets/dpgwrap/"
    files = (
        (f"{dirname}containers.py", "._widget", "Container", ItemMaps.containers),
        (f"{dirname}widgets.py", "._widget", "Widget", ItemMaps.widgets),
        (f"{dirname}handlers.py", "._item", "Item", ItemMaps.handlers),
        (f"{dirname}stylize.py", "._item", "Item, Context", ItemMaps.stylize),
        (f"{dirname}registries.py", "._item", "Item, Context", ItemMaps.registries),
        (f"{dirname}valueitems.py", "._item", "Item", ItemMaps.valueitems),
        (f"{dirname}node.py", "._widget", "Container, Widget", ItemMaps.node),
        (f"{dirname}plotting.py", "._widget", "Container, Widget", ItemMaps.plotting),
        (f"{dirname}drawing.py", "._widget", "Container, Widget", ItemMaps.drawing)
    )


    for filename, module, obj, mapping in files:
        with open(filename, "w") as pyfile:
            importlines = [
                "from typing import Callable, Any\n",
                "\n"
                "from . import idpg\n",
                f"from {module} import {obj}\n\n\n",
                "##################################################\n"                
                "## Note: this file was automatically generated. ##\n"
                "##################################################\n"
            ]

            pyfile.writelines(importlines)

            mapping = _organize(mapping)
            for item, info in mapping:
                baseclass, cmd = info

                clslines = [
                    f"\n\nclass {item}({baseclass}):\n",
                    f"    _command: Callable = idpg.{cmd}\n"
                    "\n",
                ]

                # Getting params from dearpygui.dearpygui and not
                # dearpygui.core because objects in core(.pyi) are
                # considered built-in's and don't yield signatures.
                params = signature(getattr(dpg, cmd)).parameters
                instance_attrs = [str(attr) for attr in params.keys()]
                init_params = []

                

                for para in params.values():
                    para = str(para)
                    # Some type hints are unnecessarily used from the
                    # typing module. Python 3.9 supports using
                    # the built-in types as hints.
                    for t in ("List", "Tuple", "Dict", "Set"):
                        para = para.replace(t, t.lower())
                    # For some reason if the hint is list and the default
                    # value isn't falsy, that value will be a tuple and
                    # not a list...? Maybe a bug in mvPythonParser.
                    if "list" in para:
                        para = para.replace("(","[").replace(")","]")
                    init_params.append(para)
                if "id" in instance_attrs:
                    idx = instance_attrs.index("id")
                    instance_attrs.remove("id")
                    init_params.pop(idx)

                # making __init__ and parameter line
                line = f"    def __init__("
                if len(init_params) == 0:
                    line += f"self, **kwargs):\n{indent(2)}"
                elif len(init_params) < 4:
                    line += "self, " + \
                        ", ".join(init_params) + f", **kwargs):\n{indent(2)}"
                else:
                    init_params.insert(0, "self")
                    line += f"\n{indent(2)}"
                    line += f",\n{indent(2)}".join([*init_params, "**kwargs"])
                    line += f"\n    ):\n{indent(2)}"
                clslines.append(line)



                # super()
                line = "super().__init__("
                if len(instance_attrs) == 0:
                    line += "**kwargs)\n"
                elif len(instance_attrs) < 4:
                    line += ", ".join(f"{attr}={attr}" for attr in instance_attrs) + ", **kwargs)\n"
                else:
                    line += f"\n{indent(2)}"
                    line += f",\n{indent(2)}".join(
                        [*[f"{attr}={attr}" for attr in instance_attrs], "**kwargs"])
                    line += f"\n{indent(2)})\n"
                clslines.append(line)

                # instance attributes
                line = "".join(f"{indent(2)}self.{attr} = {attr}\n" for attr in instance_attrs)
                clslines.append(line)
                
                pyfile.writelines(clslines)



