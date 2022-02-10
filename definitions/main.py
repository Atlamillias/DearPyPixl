import typing
from collections import ChainMap
from typing import Callable, Any, Union, Dict, Tuple, Set, List
from pathlib import Path
from inspect import Parameter
from copy import deepcopy

from dearpygui import dearpygui

import srcparser
from srcwriter import PyTextNamespace, PyTextClass, PyTextObject, PyFile


# Output target path
DIRPATH = Path(__file__).parent / "_appitems"
EXCL_DPATH = DIRPATH.parent / "_item"

CONFIGURATION = "configuration"
INFORMATION   = "information"
STATE         = "state"
# By default, all parameters are included as class attributes bound
# to the ItemAttribute descriptor. If the param name is listed here,
# it will not be included, but will still be used in __init__.
EXCLUDED_CONFIGURATION = (
    "parent",
    "before",
    "tag",
    "id",
    "args",
    "kwargs",
    "item_type",
    "type",
)
# These categories will not be written to files (before renaming).
EXCLUDED_CATEGORY = (
    # DearPyPixl considers these low-level and has custom implementations
    # for all of these.
    "themes",
    "widget_handlers",
    "handlers",
    "fonts",
)
# Items with these names will be added to the "exclusions.py" file
# (only if they're not within an excluded category).
EXCLUDED_ITEMS = (
    "ValueRegistry",
    "ColorMapRegistry",
    "TextureRegistry",
    "HandlerRegistry",
    "ItemHandlerRegistry",
    "TemplateRegistry",
    "FontRegistry",
)
EXCL_ITEMS_CATEGORY_OVERRIDE = {
    (
        "ValueRegistry",
        "ColorMapRegistry",
        "TextureRegistry",
        "HandlerRegistry",
        "ItemHandlerRegistry",
        "TemplateRegistry",
        "FontRegistry",
    ): "registries",
    (
        "Theme",
        "ThemeComponent",
        "ThemeColor",
        "ThemeStyle",
    ): "themes"
}
EXCLUDED_STATE = ()
ITEM_ATTRIBUTE_SETTINGS = {
    "ALL": {"pos"          : ("configuration", "get_item_state", "set_item_config", None),
            "default_value": ("information", "get_item_cached", None, None),
            "delay_search" : ("information", "get_item_cached", None, None),
            "default_open" : ("information", "get_item_cached", None, None),
            "colormap"     : ("configuration", "get_item_cached", "set_item_cached_colormap", None),
            "value"        : ("configuration", "get_item_value", "set_item_value", "default_value"),},
    # DPG BUGFIX's
    "Window"          : {"on_close"   : ("configuration", "get_item_cached", "set_item_cached_config", None),},
    "InputText"       : {"multiline"  : ("configuration", "get_item_config", "set_item_config", "multline"),},
    "SubPlots"        : {"columns"    : ("configuration", "get_item_config", "set_item_config", "cols"),},
    "DragPayload"     : {"drag_data"  : ("configuration", "get_item_cached", "set_item_cached_config", None),
                         "drop_data"  : ("configuration", "get_item_cached", "set_item_cached_config", None),},
    "KnobFloat"       : {"min_value"  : ("configuration", "get_item_config", "set_item_config", "min_scale"),
                         "max_value"  : ("configuration", "get_item_config", "set_item_config", "max_scale"),},
    "FileExtension"   : {"extension"  : ("configuration", "get_item_cached", "set_item_cached_config", None),},
    "ColorMap"        : {"colors"     : ("configuration", "get_item_cached", None, None),
                         "qualitative": ("configuration", "get_item_cached", None, None),},
    "PlotAxis"        : {"axis"       : ("configuration", "get_item_cached", "set_item_cached_config", None),},
}
ITEM_ATTRIBUTE_ADDTL_PARAMS  = {
    "CollapsingHeader": {
                            CONFIGURATION: (
                                                Parameter(name="collapsed",
                                                kind=Parameter.POSITIONAL_OR_KEYWORD,
                                                annotation=bool,
                                                default='ItemAttribute("configuration", "get_item_value", "set_item_value", "default_open")'),
                                           ),
                            STATE        : (
                                                Parameter(name="is_collapsed",
                                                kind=Parameter.POSITIONAL_OR_KEYWORD,
                                                annotation=bool,
                                                default='ItemAttribute("state", "get_item_value", None, None)'),
                                           )
                        }                       
}
ITEM_ATTRIBUTE_ADDL_STATE  = {
    "CollapsingHeader": (Parameter(name="is_collapsed",
                                   kind=Parameter.POSITIONAL_OR_KEYWORD,
                                   annotation=bool,
                                   default='ItemAttribute("configuration", "get_item_value", "set_item_value", "default_open")'),)
}

RENAME_CATEGORY = {
    "widget_handlers": "handlers",
    "custom": "misc",
    "plots": "plotting",
    "composite": "misc",
}
RENAME_PARAM = {"type": "item_type", "id": "tag"}
RENAME_STATE = {
    "HOVER": "is_hovered",
    "ACTIVE": "is_active",
    "FOCUSED": "is_focused",
    "CLICKED": "is_clicked",
    "VISIBLE": "is_visible",
    "EDITED": "is_edited",
    "ACTIVATED": "is_activated",
    "DEACTIVATED": "is_deactivated",
    "DEACTIVATEDAE": "is_deactivated_after_edit",
    "TOGGLED_OPEN": "is_toggled_open",
    "CONT_AVAIL": "content_region_avail"
}

STATE_TYPE = {
    (
        "rect_max",
        "rect_min",
        "rect_size",
        "content_region_avail"
    ): PyTextObject("list[int, int]"),
}


# File imports
_typing_ = PyTextNamespace(typing, imports=[Callable, Any, Union, Dict, Tuple, Set, List])
_dearpygui_ = PyTextNamespace("dearpygui", imports=["dearpygui"])

_dearpypixl_item_item_ = PyTextNamespace("dearpypixl.item.item", imports=["Item"])
_dearpypixl_item_configuration_ = PyTextNamespace("dearpypixl.item.configuration", imports=["ItemAttribute"])
_dearpypixl_components_ = PyTextNamespace("dearpypixl.components", imports=["*"])

AppItem = srcparser.parse_dearpygui_src()


def make_textclass(appitem: AppItem, public: bool = True):
    # The "Parameter" class is used heavily here.
    params = appitem.parameters.values()
    init_params: list[Parameter] = []
    for param in params:
        if param._name in ("id", "tag"):
            continue
        param._name = RENAME_PARAM.get(param._name, param._name)
        init_params.append(param)

    class_attrs: list[Parameter] = [
        deepcopy(p) for p in init_params if p.name not in EXCLUDED_CONFIGURATION
    ]

    # Item attributes
    unique_attr_settings = ChainMap(
        ITEM_ATTRIBUTE_SETTINGS.get(appitem.name, {}), ITEM_ATTRIBUTE_SETTINGS["ALL"])
    value_param = None
    for param in class_attrs:
        # Check if param.name has specific settings: First check item-specific, then
        # specific settings for all items.
        non_default = unique_attr_settings.get(param.name, None)
        if non_default:
            value = PyTextObject(f"ItemAttribute{non_default!r}")
        else:
            value = PyTextObject(f'ItemAttribute("configuration", "get_item_config", "set_item_config", None)')
        param._default = value
        # If an appitem has `default_value``, create a `value` parameter.
        if param.name == "default_value":
            value_param = Parameter(
                "value",
                Parameter.POSITIONAL_OR_KEYWORD,
                default=PyTextObject('ItemAttribute("configuration", "get_item_value", "set_item_value", "default_value")'),
                annotation=param.annotation,
            )
    if value_param:
        class_attrs.append(value_param)

    # TODO: Add `ITEM_ATTRIBUTE_ADDTL_PARAMS`


    # ItemAttribute "state"
    states = [RENAME_STATE.get(state, state).lower() for state in appitem.states]
    # All items will have `resized` if they have `rect_size`.
    if "rect_size" in states:
        states.insert(0, "is_resized")
    # If an item supports the "clicked" state, it also has `left_clicked`, `right_clicked`, and `middle_clicked`.
    clicked_states = ["is_left_clicked", "is_right_clicked", "is_middle_clicked"]
    if "is_clicked" in states:
        [states.insert(1, c_state) for c_state in clicked_states]
    for state in states:
        if state in EXCLUDED_STATE:
            continue
        state_param = Parameter(
            state,
            Parameter.POSITIONAL_OR_KEYWORD,
            default=PyTextObject(f'ItemAttribute("state", "get_item_state", None, "{state.replace("is_", "")}")'),
        )
        for states, annotation in STATE_TYPE.items():
            if state in states:
                state_param._annotation = annotation
                break
        else:
            state_param._annotation = bool
        class_attrs.append(state_param)



    # misc
    class_attrs.append(
        Parameter(
            "_is_container",
            Parameter.POSITIONAL_OR_KEYWORD,
            default=appitem.is_container,
            annotation=bool,
        )
    )
    class_attrs.append(
        Parameter(
            "_is_root_item",
            Parameter.POSITIONAL_OR_KEYWORD,
            default=appitem.is_root_item,
            annotation=bool,
        )
    )
    class_attrs.append(
        Parameter(
            "_is_value_able",
            Parameter.POSITIONAL_OR_KEYWORD,
            default=appitem.is_value_able,
            annotation=bool,
        )
    )
    
    unique_parents = [
        parent.replace("mvAppItem", "").replace("mv", "")
        for parent in appitem.unique_parents
    ]
    unique_parents = tuple([parent for parent in unique_parents])
    class_attrs.append(
        Parameter(
            "_unique_parents",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=tuple,
            default=unique_parents,
        )
    )

    unique_children = [
        parent.replace("mvAppItem", "").replace("mv", "")
        for parent in appitem.unique_children
    ]
    unique_children = tuple([child for child in unique_children])
    class_attrs.append(
        Parameter(
            "_unique_children",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=tuple,
            default=unique_children,
        )
    )

    class_attrs.append(
        Parameter(
            "_unique_commands",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=tuple,
            default=tuple(appitem.unique_commands),
        )
    )

    class_attrs.append(
        Parameter(
            "_unique_constants",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=tuple,
            default=tuple(appitem.unique_constants),
        )
    )

    # dpg command
    class_attrs.append(
        Parameter(
            "_command",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=Callable,
            default=PyTextObject(appitem.command, _dearpygui_),
        )
    )



    # All objects need `kwargs` in `__init__` and `super().__init__`
    if "kwargs" not in (param.name for param in init_params):
        init_params.append(Parameter("kwargs", Parameter.VAR_KEYWORD))

    if public:
        baseclass = "Container" if appitem.is_container else "Widget"
    else:
        baseclass = "Item"
    return PyTextClass(
        name=appitem.name,
        baseclasses=[baseclass],
        metaclass=None,
        cls_attributes=class_attrs,
        init_parameters=init_params,
        docstring=appitem.docstring,
    )



def main(dirpath: Path = DIRPATH, excl_dirpath: Path = EXCL_DPATH, *, incl_headers: bool = False):
    public_files = {}
    private_files = {}


    # Creating file managers (public).
    for category in AppItem.all_categories():
        if category in EXCLUDED_CATEGORY:
            continue
        category = RENAME_CATEGORY.get(category, category)
        public_files[category] = PyFile(
            category, dirpath, imports=[_typing_, _dearpygui_, _dearpypixl_components_]
        )

    # Creating text classes.
    for appitem in AppItem._appitems:
        appitem.category = RENAME_CATEGORY.get(appitem.category, appitem.category)

        file: PyFile
        if appitem.category not in EXCLUDED_CATEGORY and appitem.name not in EXCLUDED_ITEMS:
            file = public_files[appitem.category]
            textclass = make_textclass(appitem)
        else:
            for item_names, cat_ovrrde in EXCL_ITEMS_CATEGORY_OVERRIDE.items():
                if appitem.name in item_names:
                    appitem.category = cat_ovrrde
                    break
            file = private_files.setdefault(
                appitem.category,
                PyFile(appitem.category, excl_dirpath, imports=[
                    _typing_,
                    _dearpygui_,
                    _dearpypixl_item_item_,
                    _dearpypixl_item_configuration_
                    ]
                )
            )
            textclass = make_textclass(appitem, public = False)
        file.objects.append(textclass)

    # Writing source files.
    for file, value in public_files.items():
        value.write()
    for file, value in private_files.items():
        value.write()

    # Writing __init__.py
    with open(DIRPATH / "__init__.py", "w") as pyfile:
        dearpygui.create_context()
        dearpygui.create_viewport()
        dearpygui.setup_dearpygui()

        lines = []
        # __all__
        line = f"__all__ = [\n"
        line += "\n".join(f"    '{file}'," for file in public_files)
        line += "\n]\n\n"
        lines.append(line)

        lines += [
            f"__version__ = '{dearpygui.get_app_configuration()['version']}'\n",
        ]
        pyfile.writelines(lines)
        dearpygui.destroy_context()

    
    # Writing headers in one directory above `dirpath`
    if incl_headers:
        headers_path = dirpath.parent

        for filename in public_files:
            fpath = headers_path / f"{filename}.py"
            # Do not overwrite existing files.
            if fpath.exists():
                continue
            with open(fpath, "w") as file:
                try:
                    pkgname = _dearpypixl_components_.name.split(".")[0]
                except IndexError:
                    pkgname = _dearpypixl_components_.name

                import_line = f"{pkgname}.{dirpath.stem}.{filename}"
            
                lines = []
                lines.append(f"import {import_line}\n")
                lines.append(f"from {import_line} import *\n")
                lines.append("\n\n\n")
                lines.append(f"__all__ = [*{import_line}.__all__]\n\n")
                file.writelines(lines,)


if __name__ == '__main__':
    main()