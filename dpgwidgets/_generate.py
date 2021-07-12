from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, is_dataclass
from inspect import signature, getfile
import shutil
import typing

from dearpygui import dearpygui as dpg, core as idpg


DEFAULT_DIR = "./dpgwidgets/dpgwrap"
DEFAULT_BACKUP_DIR = "./_backup"

DPG_CONSTANTS = {}


@dataclass
class ItemFile:
    category: str
    import_lines: list = field(default_factory=list)
    mapping: dict = field(default_factory=dict)


class ItemMaps:
    @classmethod
    def files(cls):
        items = []
        for attr in dir(cls):
            if "__" in attr:
                continue
            elif not is_dataclass(getattr(cls, attr)):
                continue
            items.append(getattr(cls, attr))
        return items

    @classmethod
    def commands(cls):
        values = [file.mapping for file in cls.files()]

        return {cmd for filedict in values for _, cmd in filedict.values()}

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

    containers = ItemFile(
        "containers",
        ["from ._widget import Container", ],
        {
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
            "ViewportMenuBar": ("Container", "add_viewport_menu_bar"),
            "Window": ("Container", "add_window"),
        }
    )
    widgets = ItemFile(
        "widgets",
        ["from ._widget import Widget", ],
    )
    drawing = ItemFile(
        "drawing",
        ["from ._widget import Container, Widget", ],
        {
            "ViewportDrawlist": ("Container", "add_viewport_drawlist"),
            "Drawlist": ("Container", "add_drawlist"),
            "DrawLayer": ("Container", "add_draw_layer"),
        }
    )
    plotting = ItemFile(
        "plotting",
        ["from ._widget import Container, Widget"],
        {
            "Plot": ("Container", "add_plot")
        }
    )
    node = ItemFile(
        "node",
        ["from ._widget import Container, Widget"],
        {
            "Node": ("Container", "add_node"),
            "NodeAttribute": ("Container", "add_node_attribute"),
            "NodeEditor": ("Container", "add_node_editor"),
        }
    )
    valueitems = ItemFile(
        "valueitems",
        ["from ._item import Item"],

    )
    registries = ItemFile(
        "registries",
        ["from ._item import Item, Context"],
        {
            "FontRegistry": ("Item, Context", "add_font_registry"),
            "HandlerRegistry": ("Item, Context", "add_handler_registry"),
            "TextureRegistry": ("Item, Context", "add_texture_registry"),
            "ValueRegistry": ("Item, Context", "add_value_registry"),
        }
    )
    handlers = ItemFile(
        "handlers",
        ["from ._item import Item"],

    )
    stylize = ItemFile(
        "stylize",
        ["from ._item import Item, Context"],
        {
            "Theme": ("Item, Context", "add_theme"),
            "Font": ("Item, Context", "add_font"),
        }
    )


def _organize(mapping: dict):
    mapping = sorted(mapping.items(), key=lambda x: x[1][0])
    return mapping


def _backup_existing():
    for pyfile in Path(DEFAULT_DIR).iterdir():
        if pyfile.suffix == ".py":
            shutil.copy(str(pyfile), DEFAULT_BACKUP_DIR)


def populate():
    def name_fix(string):  # if name starts with any number
        if string[0].isdigit():
            return string[2:]
        return string

    # fetching containers
    with open(getfile(dpg), "r") as dpgfile:
        lines = dpgfile.readlines()

    commands = ItemMaps.commands()  # just for containers
    core_dir = [attr for attr in dir(idpg) 
                if not attr.startswith("__") 
                or attr in typing.__all__]

    for index, line in enumerate(lines):
        if line.startswith("@contextmanager"):
            name = lines[index + 1].split("(")[0].replace("def ", "")
            func_str = f"add_{name}"
            if func_str in commands or func_str not in core_dir:
                continue

            name = name.title().replace("_", "")

            ItemMaps.containers.mapping[name] = "Container", func_str


    # iterating core
    for attr in core_dir:
        # undesirables
        if not any(attr.startswith(kw) for kw in ("add_", "draw_", "mv")):
            continue
        if "mutex" in attr or attr in ItemMaps.commands():
            continue

        if attr.startswith("add_"):
            name = attr.replace("add_", "").title().replace("_", "")
            if attr.startswith("add_node"):
                mapping, info = ItemMaps.node.mapping, ("Widget", attr)
            elif attr.endswith("_registry"):
                mapping, info = ItemMaps.registries.mapping, (
                    "Item, Context", attr)
            elif attr.endswith("_value"):
                mapping, info = ItemMaps.valueitems.mapping, ("Item", attr)
            elif attr.endswith("_handler"):
                mapping, info = ItemMaps.handlers.mapping, ("Item", attr)
            elif any(kw in attr for kw in ("theme", "font")):
                mapping, info = ItemMaps.stylize.mapping, ("Item", attr)
            elif any(kw in attr for kw in ("plot", "series", "_point")):
                mapping, info = ItemMaps.plotting.mapping, ("Widget", attr)
            else:
                mapping, info = ItemMaps.widgets.mapping, ("Widget", attr)
            mapping[name_fix(name)] = info
        elif attr.startswith("draw_"):
            name = attr.replace("draw_", "").title().replace("_", "")
            ItemMaps.drawing.mapping[name_fix(name)] = "Widget", attr
        # currently unused
        elif attr.startswith("mv"):
            DPG_CONSTANTS[attr.replace("mv", "")] = attr


def writefiles(dirpath: str = DEFAULT_DIR):
    def indent(indents: int = 1):
        ind = "    " * indents
        return ind

    _backup_existing()

    files = [[Path(dirpath, f"{ifile.category}.py"),
              ifile.import_lines,
              ifile.mapping] for ifile in ItemMaps.files()]

    for filename, ilines, mapping in files:
        with open(filename, "w") as pyfile:
            importlines = [
                "from typing import Callable, Any\n",
                "\n"
                "from . import dpg\n",
            ]
            [importlines.append(f"{iline}\n") for iline in ilines]
            importlines += [
                "\n\n"
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
                    f"    _command: Callable = dpg.{cmd}\n"
                    "\n",
                ]

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
                        para = para.replace("(", "[").replace(")", "]")
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
                    line += ", ".join(f"{attr}={attr}" for attr in instance_attrs) + \
                        ", **kwargs)\n"
                else:
                    line += f"\n{indent(2)}"
                    line += f",\n{indent(2)}".join(
                        [*[f"{attr}={attr}" for attr in instance_attrs], "**kwargs"])
                    line += f"\n{indent(2)})\n"
                clslines.append(line)

                # instance attributes
                line = "".join(
                    f"{indent(2)}self.{attr} = {attr}\n" for attr in instance_attrs)
                clslines.append(line)

                pyfile.writelines(clslines)

    # __init__.py
    with open(Path(dirpath, "__init__.py"), "w") as pyfile:
        lines = [
            "from dearpygui import dearpygui as dpg\n",
            "\n",
        ]

        # __all__
        line = f"__all__ = [\n"
        line += "\n".join(f"{indent()}'{item.category}'," for item in ItemMaps.files())
        line += "]\n\n"
        lines.append(line)

        lines += [
            f"__updated__ = '{datetime.today().date()}'\n",
            f"__dpg_ver__ = '{dpg.get_dearpygui_version()}'\n",
        ]

        pyfile.writelines(lines)


def main():
    populate()
    writefiles()


if __name__ == '__main__':
    main()
