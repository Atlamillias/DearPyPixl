import re
import inspect
import importlib
import ctypes
from re import Pattern
from typing import Any, Mapping, Union
from dataclasses import dataclass, asdict, field
from pathlib import Path
from inspect import Parameter, getmodule


# Directory paths
APPITEM_SRC           = Path(r"dearpygui_src\DearPyGui\src\core\AppItems")
MV_APPITEM_COMMONS_H  = r"mvAppItemCommons.h"
MV_APPITEM_TYPES_INC  = r"mvAppItemTypes.inc"
MV_APPITEM_CPP        = r"mvAppItem.cpp"
DEARPYGUI_DIR         = r"dearpygui_src\DearPyGui\dearpygui\dearpygui.py"


# Header file regex patterns
RePattern_RegisterItem   = re.compile(r"MV_REGISTER_WIDGET\(.+?\);")
RePattern_ItemStates     = re.compile(r"MV_SET_STATES\(.+?\);")
RePattern_ApplyItemReg   = re.compile(r"MV_APPLY_WIDGET_REGISTRATION\(.*?\)")
RePattern_RegCommands    = re.compile(r"MV_START_COMMANDS.+?MV_END_COMMANDS")
RePattern_RegParentItems = re.compile(r"MV_START_PARENTS.+?MV_END_PARENTS")
RePattern_RegChildItems  = re.compile(r"MV_START_CHILDREN.+?MV_END_CHILDREN")
RePattern_Constants      = re.compile(r"MV_START_CONSTANTS.+?MV_END_CONSTANTS")


# NOTE: Importing the source version of `dearpygui` and not the installed one.
spec = importlib.util.spec_from_file_location("dearpygui", DEARPYGUI_DIR)
dearpygui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dearpygui)

DearPyGui_Commands = {}

for cmd in dir(dearpygui):
    try:
        module_name = getmodule(getattr(dearpygui, cmd)).__name__
        if module_name not in ("_dearpygui", "dearpygui"):
            continue
    except AttributeError:  # dunders
        continue
    DearPyGui_Commands[cmd] = getattr(dearpygui, cmd)


def get_appitem_paths():
    fpath_data: dict[str, Path] = {}
    for dir in APPITEM_SRC.iterdir():
        if dir.is_dir():
            for h_file in dir.glob("*.h"):
                with open(h_file, "r") as file:
                    raw_text = file.read()
                class_objs = [line.split("class ")[-1].split(" ", maxsplit=1)[0].strip()
                              for line in raw_text.splitlines() if "class " in line]
                for item_type in class_objs:
                    fpath_data[item_type] = h_file
    return fpath_data
                    

def get_item_info():
    with open(APPITEM_SRC / MV_APPITEM_CPP) as file:
        _raw_text = file.read()

    cpp_func_names = (
        "CanItemTypeBeHovered",
        "CanItemTypeBeActive",
        "CanItemTypeBeFocused",
        "CanItemTypeBeClicked",
        "CanItemTypeBeVisible",
        "CanItemTypeBeEdited",
        "CanItemTypeBeActivated",
        "CanItemTypeBeDeactivated",
        "CanItemTypeBeDeactivatedAE",
        "CanItemTypeBeToggledOpen",
        "CanItemTypeHaveRectMin",
        "CanItemTypeHaveRectMax",
        "CanItemTypeHaveRectSize",
        "CanItemTypeHaveContAvail",
        "GetEntityDesciptionFlags",
        "GetEntityTargetSlot",
        "GetEntityValueType",
        "DoesEntityAcceptParent",
    )
    cpp_func_src = {}

    for func in cpp_func_names:
        pattern = f"    {func}(mvAppItemType type)\n    {{"
        src = _raw_text.split(pattern, maxsplit=1)[-1].split("    }")[0]
        cpp_func_src[func] = src

    print()




@dataclass
class AppItem(Mapping):
    name            : str
    item_type       : str
    category        : str

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


    _appitems = []
    _REMOVE_TXT = [
        "mvAppItemType::",
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
        ";",
    ]

    def __post_init__(self):
        self._h_file = APPITEM_SRC
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


    @classmethod
    def import_data(cls):
        appitem_data = get_appitem_paths()

        # Creating AppItem instances; `name`, `item_type`, `category`
        for item_type, path in appitem_data.items():
            name      = cls._filter_delimited(item_type)[0].replace("mv", "")
            appitem   = cls(name=name, item_type=item_type, category=path.parent.stem)
            appitem._h_file = path
        
        for appitem in cls._appitems:
            ...
        

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
    def _filter_delimited(cls, text: str, replace_txt: list[str] = ()) -> list[str]:
        replace_text = [*cls._REMOVE_TXT, *list(replace_txt)]
        new_text = " ".join(text.split())
        for rtxt in replace_text:
            new_text = new_text.replace(rtxt, "")
        # Delimiters are single spaces, single commas, and single seperators.
        return [info.strip() for info in re.split(r"[,| ]", new_text) if info]

    def _import_header_info(self):
        with open(f"{self._h_file}.h", "r") as appitem_header_file:
            raw_text       = appitem_header_file.read()
            appitem_h_text = " ".join(raw_text.splitlines())

        name, desc, value_type, *_= self._find_first(RePattern_RegisterItem, appitem_h_text).split(",")
        desc = self._filter_delimited(desc)
        value_type = value_type.split("StorageValueTypes::")[-1]

        self.name = self._filter_delimited(name)[0].replace("AppItem","").replace("mv", "")
        self.is_root_item = True if "MV_ITEM_DESC_ROOT" in desc else False
        self.is_container = True if "MV_ITEM_DESC_CONTAINER" in desc else False
        self.is_value_able= True if value_type != "None" else False

        self.command = self._find_first(RePattern_ApplyItemReg, appitem_h_text, True)[-1]

        raw_item_states = self._find_first(RePattern_ItemStates, appitem_h_text, True)
        self.states += [] if raw_item_states[0] == "NONE" else raw_item_states
        
        self.unique_parents   += self._find_first(RePattern_RegParentItems, appitem_h_text, True)
        self.unique_children  += self._find_first(RePattern_RegChildItems, appitem_h_text, True)
        self.unique_commands  += self._find_first(RePattern_RegCommands, appitem_h_text, True)
        self.unique_constants += self._find_first(RePattern_Constants, appitem_h_text, True)

    def _import_py_info(self):
        # Parameter info can be obtained from the cpp source, but it's easier to pull
        # from the py src.
        # Reminder that this is the `dearpygui` module from the source and
        # not from site-packages.
        dpg_command = getattr(dearpygui, self.command)
        signature   = inspect.signature(dpg_command)
        parameters = {name:param for name, param in signature.parameters.items()}
        self.parameters  |= parameters
        self.docstring = dpg_command.__doc__

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
    def dearpygui_deprecated_commands(cls) -> tuple[str, ...]:
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
    def dearpygui_context_commands(cls) -> tuple[str, ...]:
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
    def dearpygui_misc_commands(cls) -> tuple[str, ...]:
        """Return a tuple of all command names in `dearpygui.dearpygui`
        that are not included as the `command` for any appitem nor in the
        return of `cls.all_unique_commands`.
        """
        registered_cmds = [*cls.all_unique_commands()] + [item.command for item in cls._appitems]
        return tuple((cmd for cmd in DearPyGui_Commands if cmd not in registered_cmds))




def parse_dearpygui_src() -> type[AppItem]:
    # APPITEM_COMMONS is parsed first as it contains all
    # appitem header file names prefixed by their parent folders.
    appitem_cmn_dir = Path(APPITEM_SRC, MV_APPITEM_COMMONS_H)
    with open(str(appitem_cmn_dir), "r") as mvAppItemCommonsH:
        raw_text = mvAppItemCommonsH.read()
        # First line is `#pragma once`.
        mvAppItemCommons = [line for line in raw_text.splitlines()[1:] if line]

    for line in mvAppItemCommons:
        # Remove `#include` and string literal quotes.
        line = line.replace("#include ", "").replace('"', "")
        path = Path(line)
        # Building appitem...
        AppItem(path.stem, str(path.parent))
    # Everything can be accessed through the class in some fashion.
    return AppItem


if __name__ == '__main__':
    get_item_info()
    #AppItem.import_data()
    