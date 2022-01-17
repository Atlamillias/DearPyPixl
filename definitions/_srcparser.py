import re
import inspect
import importlib
import functools
from typing import Callable, Any
from re import Pattern
from typing import Any, Mapping, Union
from dataclasses import dataclass, asdict, field
from pathlib import Path
from inspect import Parameter, getmodule


DEARPYGUI_DIR      = r"dearpygui_src\DearPyGui\dearpygui\dearpygui.py"
DearPyGui_Commands = {}

# NOTE: Importing the source version of `dearpygui` and not the installed one.
spec = importlib.util.spec_from_file_location("dearpygui", DEARPYGUI_DIR)
dearpygui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dearpygui)

for cmd in dir(dearpygui):
    try:
        module_name = getmodule(getattr(dearpygui, cmd)).__name__
        if module_name not in ("_dearpygui", "dearpygui"):
            continue
    except AttributeError:  # dunders
        continue
    DearPyGui_Commands[cmd] = getattr(dearpygui, cmd)







@dataclass
class AppItem(Mapping):
    name            : str
    item_type       : int

    category        : str  = None
    command         : str  = None
    is_root_item    : bool = False
    is_container    : bool = False
    is_value_able   : bool = False
    parameters      : dict = field(default_factory=dict)
    states          : list = field(default_factory=list)
    unique_parents  : list = field(default_factory=list)
    unique_children : list = field(default_factory=list)
    unique_commands : list = field(default_factory=list)
    unique_constants: list = field(default_factory=list)
    docstring       : str  = None

        
    ## Misc. Methods ##
    @classmethod
    def get_from_items(cls, key: str, value: Any, exact: bool = False) -> list['AppItem']:
        """Return all appitems where <value> is in appitem[<key>]. If <exact> is True,
        <value> and appitem[<key>] must be equal for it to be included.
        """
        if not exact:
            return list(filter(lambda item: value in item[key], cls._appitems))
        return list(filter(lambda item: value == item[key], cls._appitems))

    @classmethod
    def all_categories(cls) -> tuple[str, ...]:
        """Return a tuple of all unique categories.
        """
        return tuple({item.category for item in cls._appitems})

    @classmethod
    def all_parameters(cls) -> tuple[str, ...]:
        """Return a tuple of all unique parameter names.
        """
        return tuple({param for item in cls._appitems for param in item.parameters})

    @classmethod
    def all_unique_commands(cls) -> tuple[str, ...]:
        """Return a tuple of the unique command names for all
        appitems.
        """
        return tuple({cmd for item in cls._appitems for cmd in item.unique_commands})

    @classmethod
    def deprecated_commands(cls) -> tuple[str, ...]:
        """Return a tuple containing the names of all callables in
        `dearpygui.dearpygui` that are decorated with `deprecated`.
        """
        commands = []
        for name, obj in DearPyGui_Commands.items():
            if not hasattr(obj, "__wrapped__"):
                continue
            module_name = Path(obj.__code__.co_filename).stem
            # NOTE: This is an inference. Could be another decorator
            # function in `dearpygui` in the future.
            if module_name == "dearpygui":
                commands.append(name)
        return tuple(commands)

    @classmethod
    def context_commands(cls) -> tuple[str, ...]:
        """Return a tuple containing the names of all callables in
        `dearpygui.dearpygui` that are decorated with `contextmanager`.
        """
        commands = []
        for name, obj in DearPyGui_Commands.items():
            if not hasattr(obj, "__wrapped__"):
                continue
            module_name = Path(obj.__code__.co_filename).stem
            # NOTE: This is an inference. 99% likely to be `contextmanager`
            # though.
            if module_name == "contextlib":
                commands.append(name)
        return tuple(commands)

    @classmethod
    def misc_commands(cls) -> tuple[str, ...]:
        """Return a tuple of all command names in `dearpygui.dearpygui`
        that are not included as the `command` for any appitem nor in the
        return of `cls.all_unique_commands`.
        """
        registered_cmds = [*cls.all_unique_commands()] + [item.command for item in cls._appitems]
        return tuple((cmd for cmd in DearPyGui_Commands if cmd not in registered_cmds))



    _appitems = []


    _REMOVE_TXT      = ["mvAppItemType::",
                        "AppItem",
                        "MV_REGISTER_WIDGET",
                        "MV_APPLY_WIDGET_REGISTRATION",
                        "MV_START_PARENTS",
                        "MV_START_CHILDREN",
                        "MV_START_CONSTANTS",
                        "MV_START_COMMANDS",
                        "MV_END_COMMANDS",
                        "MV_END_PARENTS",
                        "MV_END_CONSTANTS",
                        "MV_END_CHILDREN",
                        "MV_ADD_CHILD",
                        "MV_ADD_CONSTANT",
                        "MV_ADD_COMMAND",
                        "MV_ADD_PARENT",
                        "MV_SET_STATES",
                        "MV_STATE_",
                        ")",
                        "(",
                        ";",]

    def __post_init__(self):
        self._h_file = ...
        self._appitems.append(self)
        #self._filepath = Path(APPITEM_SRC, self.category, self.name)
        #self._appitems.append(self)
        #self.unique_constants.append(self.name)
        
        # self._import_py_info()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(item, value)
    
    def __iter__(self):
        yield from asdict(self)

    def __len__(self):
        return len(asdict(self))

    ### Text filter methods ###
    @classmethod
    def _find_first(cls, pattern: Pattern, text: str, filter_and_split: bool = False) -> Union[str, list[str]]:
        """Safely return the first match in the return of `re.findall(<pattern>, <text>).
        If a match isn't found, an empty string is returned instead. If <filter_and_split>
        is True, the result of `cls._filter_delimited(<match>)` is returned instead of
        <match>.
        """
        try:
            match = re.findall(pattern, text)[0]
        except IndexError:
            match = ""

        if filter_and_split:
            return cls._filter_delimited(match)
        return match

    @classmethod
    def _filter_delimited(cls, text: str, remove_text: list[str] = ()) -> list[str]:
        default_remove_text = [ "mvAppItemType::",
                        "AppItem",
                        "MV_REGISTER_WIDGET",
                        "MV_APPLY_WIDGET_REGISTRATION",
                        "MV_START_PARENTS",
                        "MV_START_CHILDREN",
                        "MV_START_CONSTANTS",
                        "MV_START_COMMANDS",
                        "MV_END_COMMANDS",
                        "MV_END_PARENTS",
                        "MV_END_CONSTANTS",
                        "MV_END_CHILDREN",
                        "MV_ADD_CHILD",
                        "MV_ADD_CONSTANT",
                        "MV_ADD_COMMAND",
                        "MV_ADD_PARENT",
                        "MV_SET_STATES",
                        "MV_STATE_",
                        ")",
                        "(",
                        ";",]
        all_remove_text = [*default_remove_text, *list(remove_text)]
        new_text = " ".join(text.split())
        for rtxt in all_remove_text:
            new_text = new_text.replace(rtxt, "")
        # Delimiters are single spaces, single commas, and single seperators.
        return [info.strip() for info in re.split(r"[,| ]", new_text) if info]


APPITEM_SRC_DIR  = Path(r"E:\code\repos\dearpygui-definitions\dearpygui_src\DearPyGui\src\ui\AppItems")
ITEM_DESC_FLAGS  = ("MV_ITEM_DESC_ROOT"     ,  # top-level item that cannot be parented
                    "MV_ITEM_DESC_CONTAINER",  # item can parent other non-root items
                    "MV_ITEM_DESC_HANDLER"  ,    
                    "MV_ITEM_DESC_DRAW_CMP" ,) # has draw component





def _read_src_file(filename: str, func: Callable = None):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open(APPITEM_SRC_DIR / filename) as file:
            raw_text = file.read()
        return func(raw_text, *args, **kwargs)

    return wrapper


def _remove_addtl_whtspace(text: str) -> str:
    """Removes addtl. whitespace, newlines, etc. from a string."""
    return " ".join(text.split())


def _filter_delimited(cls, text: str, replace_txt: list[str] = ()) -> list[str]:
    replace_text = ["mvAppItemType::",
                    "AppItem",
                    "MV_START_PARENTS",
                    "MV_START_CHILDREN",
                    "MV_START_CONSTANTS",
                    "MV_START_COMMANDS",
                    "MV_END_COMMANDS",
                    "MV_END_PARENTS",
                    "MV_END_CONSTANTS",
                    "MV_END_CHILDREN",
                    "MV_ADD_CHILD",
                    "MV_ADD_CONSTANT",
                    "MV_ADD_COMMAND",
                    "MV_ADD_PARENT",
                    "MV_SET_STATES",
                    "MV_STATE_",
                    ")",
                    "(",
                    ";",
                    *list(replace_txt)]
    new_text = " ".join(text.split())
    for rtxt in replace_text:
        new_text = new_text.replace(rtxt, "")
    # Delimiters are single spaces, single commas, and single seperators.
    return [info.strip() for info in re.split(r"[,| ]", new_text) if info]




## data import methods ###
@_read_src_file("mvAppItemTypes.inc")
def _get_appitem_indexes(text: str) -> dict[str, int]:
    item_names_text = text.split("#define MV_ITEM_TYPES \\\n", maxsplit=1)[-1]

    _replace_chars = ("X(", ")", "\\")
    for char in _replace_chars:
        item_names_text = item_names_text.replace(char, "")

    item_info_data = _remove_addtl_whtspace(item_names_text)

    return {name.strip(): idx for idx, name in enumerate(item_info_data.split())}


@_read_src_file("mvAppItem.h")
def _get_appitem_commands(text: str) -> dict[str, str]:
    split_at_text  = "GetEntityCommand(mvAppItemType type) { switch (type) {"
    item_info_text = text.replace("case mvAppItemType::", "")  \
                              .replace("return", "")
    item_info_data = _remove_addtl_whtspace(item_info_text)   \
                        .split(split_at_text, maxsplit=1)[-1] \
                        .split("default:"   , maxsplit=1)[0]  \
                        .split(";")
    item_cmds      = {}
    for data in item_info_data:
        try:
            name, cmd = data.split(": ")
        except ValueError:
            continue
        item_cmds[name.strip()] = cmd.strip()
    
    return item_cmds


@_read_src_file("mvAppItem.cpp")
def _get_appitem_parameters(text: str) -> dict[str, list[str]]:
    item_info_text   = text.split("GetEntityParser(mvAppItemType type)", maxsplit=1)[-1] \
                           .split("switch (type) {")[-1]                                 
    item_info_blocks = _remove_addtl_whtspace(item_info_text).split("break; }")

    item_data = {}
    for code_block in item_info_blocks:
        # trimming needless text
        code_block = code_block.split("::", maxsplit=1)[-1] \
                               .split("setup.about", maxsplit=1)[0]

        name       = code_block.split(":", maxsplit=1)[0]



@_read_src_file("mvAppItem.cpp")
def _get_appitem_states(text: str) -> dict[str, list[str]]:
    ...




def import_appitem_data():
    appitem_names = _get_appitem_indexes()




