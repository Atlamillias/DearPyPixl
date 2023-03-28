from typing import *
from types import MappingProxyType
import enum



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
################## Typing Primitives #####################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

T  = TypeVar("T")       # type
KT = TypeVar("KT")      # type (key)
VT = TypeVar("VT")      # type (val)
P  = ParamSpec("P")     # param
S  = TypeVarTuple("S")  # shape

ItemId = int | str


class Array(Generic[*S]):
    """A sequence of fixed-length."""

class _Null(type):
    def __bool__(cls):
        return False

class Null(metaclass=_Null): ...

NULL = Null




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############### Helper Functions & Types #################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class _FrozenNamespace(type):
    # I think the point is clear enough, so I'm not gonna go
    # nuts on patching the mutability holes.
    __members: frozenset[str]

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        cls.__members   = frozenset(namespace)
        cls.__new__     = None
        cls.__setattr__ = None
        return cls

    def __contains__(cls, other):
        return other in cls.__members

    def __getitem__(cls, name: str) -> Any:
        name = name.replace(" ", "_").upper()  # constants
        return getattr(cls, name)

class FrozenNamespace(metaclass=_FrozenNamespace):
    """A simple namespace containing constants. All members should be
    uppercase."""


class _TypingOverload:
    __slots__ = ()

    def __init__(self, mthd): ...

    def __set_name__(self, tp: type, name: str):
        if getattr(tp, name, None) == self:
            delattr(tp, name)

    def __get__(self, inst, tp):
        return self

def typing_overload(mthd: T) -> T:
    return _TypingOverload(mthd)

@overload
def frozenmap(**kwargs: dict[KT, VT]) -> MappingProxyType[KT, VT]: ...
@overload
def frozenmap(iterable: Sequence[Array[KT, VT]] | Mapping[KT, VT], /) -> MappingProxyType[KT, VT]: ...
def frozenmap(iterable: Sequence[Array[KT, VT]] | Mapping[KT, VT] | None = None, **kwargs) -> MappingProxyType[KT, VT]:
    kwds = iterable or kwargs
    return MappingProxyType(dict(kwds))


def typeddict_init(typed_dict: type[T], value: Any = None) -> T:
    """Return a dictionary initialized with all required and optional keys of a
    TypedDict."""
    keys = (k for k in typed_dict.__annotations__ if k in typed_dict.__required_keys__)  # keep order
    return dict.fromkeys(keys, value)


def overwrite_with(returned_obj: T, replace_docstring: bool = False) -> Callable[[Callable], T]:
    """Equivelent of assigning an object an alias using function-defining
    syntax. Use as a decorator.
    """
    # Forces pyright to identify object aliases as the actual objects
    # instead of variables/attributes.
    def wrap_placeholder(fn: Callable, *args) -> T:
        if replace_docstring:
            try:
                doc = fn.__doc__
            except AttributeError:
                doc = returned_obj.__doc__
            if doc:
                returned_obj.__doc__ = doc
        return returned_obj
    return wrap_placeholder




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
################### Types & Protocols ####################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class DPGTypeId(NamedTuple):
    """Contains the internal enumeration value and string representation of a
    DearPyGui item type.
    """
    int_id: int
    str_id: int


_T_co  = TypeVar("_T_co", int, str, covariant=True)

class DPGCommand(Protocol[P, _T_co]):
    """A function that returns an item's identifier (or `tag` if provided as
    an argument).
    """
    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> _T_co: ...


class DPGCallback(Protocol[P]):
    """A callable that can be invoked by DearPyGui without error. It should accept
    zero to three positional arguments; "sender", "app_data" and "user_data".
    """
    @overload
    def __call__(self, /) -> None: ...
    @overload
    def __call__(self, sender: ItemId, /) -> None: ...
    @overload
    def __call__(self, sender: ItemId, app_data: Any, /) -> None: ...
    @overload
    def __call__(self, sender: ItemId, app_data: Any, user_data: Any, /) -> None: ...
    def __call__(self, sender: ItemId = ..., app_data: Any = ..., user_data: Any = ..., /, **kwargs) -> None: ...

    __code__  = __call__.__code__


class DPXErrorFn(Protocol[P]):
    def __call__(self, item: ItemId, command: DPGCommand, *args: P.args, **kwargs: P.kwargs) -> Exception | None: ...




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############# TypeDicts, Templates & Enums ###############
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Each section has three structues;
#   * a TypedDict
#   * an enumeration
#   * a template of the former TypedDict, as a MappingProxyType
#
# TypedDict.__required_keys__ should be a valid (and supported) DPG setting. Non-
# required keys are settings made available by or through dearpypixl. The enumeration
# includes the names of all keys that can exist in the preceding TypedDict. It is
# followed by a read-only template of the preceding TypedDict


# Application
class DPGApplicationConfig(TypedDict):
    docking                   : bool
    docking_space             : bool
    load_init_file            : str
    init_file                 : str
    auto_save_init_file       : bool
    device                    : int
    auto_device               : bool
    allow_alias_overwrites    : bool
    manual_alias_management   : bool
    skip_required_args        : bool
    skip_positional_args      : bool
    skip_keyword_args         : bool
    wait_for_input            : bool
    manual_callback_management: bool
    # additional, via DPX
    theme                     : NotRequired[ItemId | None]
    font                      : NotRequired[ItemId | None]

class ApplicationConfig(enum.StrEnum):
    DOCKING                    = "docking"
    DOCKING_SPACE              = "docking_space"
    LOAD_INIT_FILE             = "load_init_file"
    INIT_FILE                  = "init_file"
    AUTO_SAVE_INIT_FILE        = "auto_save_init_file"
    DEVICE                     = "device"
    AUTO_DEVICE                = "auto_device"
    ALLOW_ALIAS_OVERWRITES     = "allow_alias_overwrites"
    MANUAL_ALIAS_MANAGEMENT    = "manual_alias_management"
    SKIP_REQUIRED_ARGS         = "skip_required_args"
    SKIP_POSITIONAL_ARGS       = "skip_positional_args"
    SKIP_KEYWORD_ARGS          = "skip_keyword_args"
    WAIT_FOR_INPUT             = "wait_for_input"
    MANUAL_CALLBACK_MANAGEMENT = "manual_callback_management"
    THEME                      = "theme"
    FONT                       = "font"

APPLICATION_CONFIG_TEMPLATE = frozenmap(typeddict_init(DPGApplicationConfig))


class DPGApplicationState(TypedDict):
    # additional, via DPX
    set_up: NotRequired[bool]

class ApplicationState(enum.StrEnum):
    SET_UP = "set_up"

APPLICATION_STATE_TEMPLATE = frozenmap(typeddict_init(DPGApplicationState))




# Viewport
class DPGViewportConfig(TypedDict):
    title             : str
    small_icon        : str
    large_icon        : str
    width             : int
    height            : int
    x_pos             : int
    y_pos             : int
    min_width         : int
    max_width         : int
    min_height        : int
    max_height        : int
    resizable         : bool
    vsync             : bool
    always_on_top     : bool
    decorated         : bool
    clear_color       : tuple[float, ...]
    # additional via DPX
    primary_window    : NotRequired[ItemId | None]
    use_primary_window: NotRequired[bool]
    callback          : NotRequired[DPGCallback | None]
    user_data         : NotRequired[Any]

class ViewportConfig(enum.StrEnum):
    TITLE              = "title"
    SMALL_ICON         = "small_icon"
    LARGE_ICON         = "large_icon"
    WIDTH              = "width"
    HEIGHT             = "height"
    X_POS              = "x_pos"
    Y_POS              = "y_pos"
    MIN_WIDTH          = "min_width"
    MAX_WIDTH          = "max_width"
    MIN_HEIGHT         = "min_height"
    MAX_HEIGHT         = "max_height"
    RESIZABLE          = "resizable"
    VSYNC              = "vsync"
    ALWAYS_ON_TOP      = "always_on_top"
    DECORATED          = "decorated"
    CLEAR_COLOR        = "clear_color"
    PRIMARY_WINDOW     = "primary_window"
    USE_PRIMARY_WINDOW = "use_primary_window"
    CALLBACK           = "callback"
    USER_DATA          = "user_data"

VIEWPORT_CONFIG_TEMPLATE = frozenmap(typeddict_init(DPGViewportConfig))


class DPGViewportState(TypedDict):
    # additional, via DPX
    created   : bool
    fullscreen: bool

class ViewportState(enum.StrEnum):
    CREATED    = "created"
    FULLSCREEN = "fullscreen"






# Items
class DPGItemConfig(TypedDict):
    label             : str
    show              : bool
    user_data         : Any
    use_internal_label: bool

class ItemConfig(enum.StrEnum):
    LABEL              = "label"
    SHOW               = "show"
    USER_DATA          = "user_data"
    USE_INTERNAL_LABEL = "use_internal_label"

ITEM_CONFIG_TEMPLATE = frozenmap(typeddict_init(DPGItemConfig))


class DPGItemInfo(TypedDict):
    children                        : dict[Literal[0, 1, 2, 3], list[ItemId]]
    type                            : str
    target                          : int
    parent                          : ItemId | None
    theme                           : ItemId | None
    handlers                        : ItemId | None
    font                            : ItemId | None
    container                       : bool
    hover_handler_applicable        : bool
    active_handler_applicable       : bool
    focus_handler_applicable        : bool
    clicked_handler_applicable      : bool
    visible_handler_applicable      : bool
    edited_handler_applicable       : bool
    activated_handler_applicable    : bool
    deactivated_handler_applicable  : bool
    deactivatedae_handler_applicable: bool
    toggled_open_handler_applicable : bool
    resized_handler_applicable      : bool

class ItemInfo(enum.StrEnum):
    CHILDREN                         = "children"
    TYPE                             = "type"
    TARGET                           = "target"
    PARENT                           = "parent"
    THEME                            = "theme"
    HANDLERS                         = "handlers"
    FONT                             = "font"
    CONTAINER                        = "container"
    HOVER_HANDLER_APPLICABLE         = "hover_handler_applicable"
    ACTIVE_HANDLER_APPLICABLE        = "active_handler_applicable"
    FOCUS_HANDLER_APPLICABLE         = "focus_handler_applicable"
    CLICKED_HANDLER_APPLICABLE       = "clicked_handler_applicable"
    VISIBLE_HANDLER_APPLICABLE       = "visible_handler_applicable"
    EDITED_HANDLER_APPLICABLE        = "edited_handler_applicable"
    ACTIVATED_HANDLER_APPLICABLE     = "activated_handler_applicable"
    DEACTIVATED_HANDLER_APPLICABLE   = "deactivated_handler_applicable"
    DEACTIVATEDAE_HANDLER_APPLICABLE = "deactivatedae_handler_applicable"
    TOGGLED_OPEN_HANDLER_APPLICABLE  = "toggled_open_handler_applicable"
    RESIZED_HANDLER_APPLICABLE       = "resized_handler_applicable"

ITEM_INFO_TEMPLATE = frozenmap(typeddict_init(DPGItemInfo) | {"children": dict.fromkeys((0, 1, 2, 3), ())})


class DPGItemState(TypedDict, total=False):
    ok                    : Required[bool]
    pos                   : Array[int, int] | None
    hovered               : bool | None
    active                : bool | None
    focused               : bool | None
    clicked               : bool | None
    left_clicked          : bool | None
    right_clicked         : bool | None
    middle_clicked        : bool | None
    visible               : bool | None
    edited                : bool | None
    activated             : bool | None
    deactivated           : bool | None
    deactivated_after_edit: bool | None
    rect_min              : Array[int, int] | None
    rect_max              : Array[int, int] | None
    rect_size             : Array[int, int] | None
    resized               : bool | None
    content_region_avail  : Array[int, int] | None

class ItemState(enum.StrEnum):
    OK                     = "ok"
    POS                    = "pos"
    HOVERED                = "hovered"
    ACTIVE                 = "active"
    FOCUSED                = "focused"
    CLICKED                = "clicked"
    LEFT_CLICKED           = "left_clicked"
    RIGHT_CLICKED          = "right_clicked"
    MIDDLE_CLICKED         = "middle_clicked"
    VISIBLE                = "visible"
    EDITED                 = "edited"
    ACTIVATED              = "activated"
    DEACTIVATED            = "deactivated"
    DEACTIVATED_AFTER_EDIT = "deactivated_after_edit"
    RECT_MIN               = "rect_min"
    RECT_MAX               = "rect_max"
    RECT_SIZE              = "rect_size"
    RESIZED                = "resized"
    CONTENT_REGION_AVAIL   = "content_region_avail"

ITEM_STATES_TEMPLATE = frozenmap(typeddict_init(DPGItemState))
