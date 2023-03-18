from typing import *
import types



###########################################
############ TYPING PRIMITIVES ############
###########################################

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

###########################################
############## MISC FN/TYPEs ##############
###########################################


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
def frozenmap(**kwargs: dict[KT, VT]) -> dict[KT, VT]: ...
@overload
def frozenmap(iterable: Sequence[Array[KT, VT]] | Mapping[KT, VT], /) -> dict[KT, VT]: ...
def frozenmap(iterable: Sequence[Array[KT, VT]] | Mapping[KT, VT] | None = None, **kwargs) -> dict[KT, VT]:
    kwds = iterable or kwargs
    return types.MappingProxyType(dict(kwds))


def typeddict_init(typed_dict: type[T], value: Any = None) -> T:
    """Return a dictionary initialized with all required and optional keys of a
    TypedDict."""
    return dict.fromkeys(typed_dict.__annotations__, value)




###########################################
############# DPG/PXL TYPING ##############
###########################################

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


class DPGViewportConfig(TypedDict):
    title        : str
    small_icon   : str
    large_icon   : str
    width        : int
    height       : int
    x_pos        : int
    y_pos        : int
    min_width    : int
    max_width    : int
    min_height   : int
    max_height   : int
    resizable    : bool
    vsync        : bool
    always_on_top: bool
    decorated    : bool
    clear_color  : tuple[int, ...]


class DPGItemConfig(TypedDict):
    label             : str
    show              : bool
    user_data         : Any
    use_internal_label: bool

DPG_CONFIG_DICT = frozenmap(typeddict_init(DPGItemConfig))


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

DPG_INFO_DICT = frozenmap(typeddict_init(DPGItemInfo) | {"children": dict.fromkeys((0, 1, 2, 3), ())})


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

DPG_STATES_DICT = frozenmap(typeddict_init(DPGItemState))


class PXLErrorFn(Protocol[P]):
    def __call__(self, item: ItemId, command: DPGCommand, *args: P.args, **kwargs: P.kwargs) -> Exception | None: ...
