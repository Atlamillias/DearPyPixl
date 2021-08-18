import inspect
from inspect import Parameter
import typing
from typing import Callable, Any, Union, Dict, Tuple, Set, List
from pathlib import Path

import dearpygui.dearpygui as dearpygui
import dearpygui._dearpygui as _dearpygui

from ._pyfiletext import (
    PyTextNamespace, 
    PyTextObject, 
    PyFile, 
    PyTextClass,
)


# Namespaces (imports)
_DEARPYGUI_ = PyTextNamespace(dearpygui)
_TYPING_ = PyTextNamespace(
    typing, imports=[Any, Callable, Union, Dict, Tuple, Set, List])
# These are strings and not references to avoid circular imports.
_ITEM_ = PyTextNamespace("dpgwidgets.item", imports=["Item", "ContextSupport"])
_WIDGETS_ = PyTextNamespace("dpgwidgets.widget", imports=["Container", "Widget"])

# paths
CWD = Path(__file__).parent
DIRPATH = CWD / "libsrc"


PYFILES: dict[str, PyFile] = {}
REGISTERED_COMMANDS = []




def make_textclass(item_name, command, baseclass: list[object] = []):
    return PyTextClass(
        cls_name=item_name,
        baseclass=baseclass,
        class_attribs=[("_command", PyTextObject(command, _DEARPYGUI_))],
        instance_parameters=_handle_parameters(command),
        docstring=inspect.getdoc(command)
    )

def _handle_parameters(command: Callable):
    parameters = [p for p in inspect.signature(command).parameters.values()
                  if p.name != "id" and p.name != "tag"]
    if "kwargs" not in (p.name for p in parameters):
        parameters.append(Parameter("kwargs", Parameter.VAR_KEYWORD))

    return parameters




def process_container(cmd_name: str, command: Callable, item_type: str):
    # Even though the container might not be written to
    # "containers.py", we're going to check and create it
    # here anyway since all other "process" functions
    # do the same.
    if "containers" not in PYFILES:
        PYFILES["containers"] = PyFile("containers", DIRPATH)
        PYFILES["containers"].imports = [
            _TYPING_, _DEARPYGUI_,
            PyTextNamespace("dpgwidgets.widget", imports=["Container"])
        ]
    item_name = cmd_name.replace("add_", "")
    container = make_textclass(item_name, command, ["Container"])
    PYFILES[item_type].objects.append(container)

def process_widget(cmd_name: str, command: Callable):
    if (item_type := "widgets") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [
            _TYPING_, _DEARPYGUI_,
            PyTextNamespace("dpgwidgets.widget", imports=["Widget"])
        ]
    item_name = cmd_name.replace("add_", "")
    widget = make_textclass(item_name, command, ["Widget"])
    PYFILES["widgets"].objects.append(widget)

def process_draw_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "drawing") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _WIDGETS_]

    if is_container:
        process_container(cmd_name, command, item_type)
    else:
        item_name = cmd_name.replace("draw_", "")
        widget = make_textclass(item_name, command, ["Widget"])
        PYFILES[item_type].objects.append(widget)

def process_plot_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "plotting") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _WIDGETS_]

    if is_container:
        process_container(cmd_name, command, item_type)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Widget"])
        PYFILES[item_type].objects.append(widget)

def process_node_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "node") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _WIDGETS_]

    if is_container:
        process_container(cmd_name, command, item_type)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Widget"])
        PYFILES[item_type].objects.append(widget)

def process_val_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "valuetypes") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _ITEM_]

    if is_container:
        item_name = cmd_name.replace("add_", "")
        container = make_textclass(item_name, command, ["Item", "ContextSupport"])
        PYFILES[item_type].objects.append(container)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Item"])
        PYFILES[item_type].objects.append(widget)

def process_style_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "stylize") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _ITEM_]

    if is_container:
        item_name = cmd_name.replace("add_", "")
        container = make_textclass(item_name, command, ["Item", "ContextSupport"])
        PYFILES[item_type].objects.append(container)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Item"])
        PYFILES[item_type].objects.append(widget)

def process_handler_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "handlers") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _ITEM_]

    if is_container:
        item_name = cmd_name.replace("add_", "")
        container = make_textclass(item_name, command, ["Item", "ContextSupport"])
        PYFILES[item_type].objects.append(container)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Item"])
        PYFILES[item_type].objects.append(widget)

def process_registry_item(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "registries") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = [_TYPING_, _DEARPYGUI_, _ITEM_]

    if is_container:
        item_name = cmd_name.replace("add_", "")
        container = make_textclass(item_name, command, ["Item", "ContextSupport"])
        PYFILES[item_type].objects.append(container)
    else:
        item_name = cmd_name.replace("add_", "")
        widget = make_textclass(item_name, command, ["Item"])
        PYFILES[item_type].objects.append(widget)

# WIP
def process_constant(cmd_name: str, command: Callable, is_container: bool = False):
    if (item_type := "constants") not in PYFILES:
        PYFILES[item_type] = PyFile(item_type, DIRPATH)
        PYFILES[item_type].imports = []

    item_name = cmd_name.replace("mv", "")




# Dispatch to a function depending on the item.
process_item = {
    "drawing": process_draw_item,
    "plotting": process_plot_item,
    "node": process_node_item,
    "valuetypes": process_val_item,
    "stylize": process_style_item,
    "handlers": process_handler_item,
    "registries": process_registry_item,
    "constants": process_constant,
}
# Another dispatch pattern to avoid copy/pasting the same
# conditional checks in several spots...
# Also, the order is intentional.
is_item = {
    "constants": lambda x: x.startswith("mv"),
    "drawing": lambda x: x.startswith("draw_") or "_draw" in x,
    "registries": lambda x: x.startswith("add_") and x.endswith("_registry"),
    "handlers": lambda x: x.startswith("add_") and x.endswith("_handler"),
    "valuetypes": lambda x: x.startswith("add_") and x.endswith("_value"),
    "plotting": lambda x: x.startswith("add_") and any(kw in x for kw in ("plot", "series", "_point")),
    "node": lambda x: x.startswith("add_node"),
    "stylize": lambda x: x.startswith("add_") and any(kw in x for kw in ("theme", "font")),
}




def main():
    ## NOTE: The script logic below *rarely* needs to be changed.
    ## Adding/changing item types, their conditions, and the process
    ## each needs to go through can be changed above this note.
    ##
    ## The summary of the script follows:
    ##    - Parse dearpygui as a text file, finding functions decorated w/
    ##    @contextmanager as potential containers.
    ##    - "Container"s are sorted and processed as they are found. "General"
    ##    containers are written to "containers.py".
    ##    - Non-containers are searched for next. Like containers they are
    ##    sorted and processed on-find. "General" non-containers are written
    ##    to "widgets.py".
    ##    - A Python file is created for each "file object" in the <files>
    ##    dictionary. Py* classes do all of the string formatting.


    # Parsing for wrappable items - containers first.
    # The only solid way I've come up with to identify them is if
    # they are decorated with contextlib.contextmanager. Parsing
    # the file as plain text is the easiest way to check.
    with open(inspect.getfile(dearpygui)) as file:
        dpgfile_text = file.readlines()
    for index, line in enumerate(dpgfile_text):
        if line.startswith("@contextmanager"):
            item_name = dpgfile_text[index + 1].split("(")[0].replace("def ", "")
            cmd_name = f"add_{item_name}"
            try:
                # Assuming that "add_<item_name>" exists. It usually does. But
                # some functions decorated this way might not. If it exists it WILL
                # be in _dearpygui...
                getattr(_dearpygui, cmd_name)
            except AttributeError:
                # If it doesn't exist in _dearpygui, then the decorated function is
                # either: not an item (like "mutex"), or is another item with a
                # unique configuration ("popup" actually just calls add_window that
                # parents a click handler). Either way, we don't care.
                continue
            command = getattr(dearpygui, cmd_name)
            # Finding which file the class will be written to...
            for item_type in is_item:
                if is_item[item_type](cmd_name):
                    process_item[item_type](cmd_name, command, True)
                    break
            else:
                # "Container"s w/o a specific home are written to containers.py.
                process_container(cmd_name, command, "containers")
            REGISTERED_COMMANDS.append(cmd_name)


    idpg_dir = (attr for attr in dir(_dearpygui) if not
                attr.startswith("__") or attr in typing.__all__)
    # Non-containers
    # Iterating through _dearpygui because there's less "fluff".
    for attr in idpg_dir:
        if not any(attr.startswith(x) for x in ("add_", "draw_", "mv")):
            continue
        if "mutex" in attr or attr in REGISTERED_COMMANDS:
            continue

        try:
            command = getattr(dearpygui, attr)
        except AttributeError:
            continue

        for item_type in is_item:
            if is_item[item_type](attr):
                process_item[item_type](attr, command)
                break
        else:
            process_widget(attr, command)
        REGISTERED_COMMANDS.append(cmd_name)

    # Writing files
    for pyfile in PYFILES:
        PYFILES[pyfile].write()
    with open(Path(DIRPATH, "__init__.py"), "w") as pyfile:
        lines = []

        # __all__
        line = f"__all__ = [\n"
        line += "\n".join(f"    '{file}'," for file in PYFILES)
        line += "\n]\n\n"
        lines.append(line)

        lines += [
            f"__version__ = '{dearpygui.get_dearpygui_version()}'\n",
        ]
        pyfile.writelines(lines)


if __name__ == '__main__':
    main()
