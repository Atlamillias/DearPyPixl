import sys
import abc
import datetime
from numbers import Number
from types import (
    CodeType,
    CodeType as Code,
    EllipsisType,
    GenericAlias,
    MappingProxyType,
    MappingProxyType as MappingProxy,
    MethodType,
    MethodType as Method,
)
from collections.abc import (
    Callable,
    Collection,
    Generator,
    Iterable,
    Iterator,
    Sequence,
    MutableSequence,
    Mapping,
    MutableMapping,
    KeysView,
    ValuesView,
    ItemsView,
)
from typing import (
    Any,
    Required,
    NotRequired,

    SupportsIndex,
    SupportsAbs,
    SupportsBytes,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    SupportsRound,

    Self,
    Literal,
    Generic,
    Protocol,
    TypedDict,

    Annotated,
    Concatenate,
    ClassVar,
    TypeAlias,
    TypeVar,
    TypeVarTuple,
    ParamSpec,
    Unpack,
    Union,

    NamedTuple,

    cast,
    final,
    get_overloads,
    overload,
    runtime_checkable,

    TYPE_CHECKING,
)
if sys.version_info < (3, 12):
    try:
        from typing_extensions import override
    except ImportError:
        raise ImportError("Python < 3.12 requires `typing-extensions` module.") from None
else:
    from typing import override
from . import _tools

if TYPE_CHECKING:
    from ._interface import AppItemType


# Super-primitive types and protocols are declared here.
# Parts of the lib rely on runtime type annotations, so
# `from __future__ import annotations` is rather destru-
# ctive.


_T     = TypeVar("_T")
_N     = TypeVar("_N", bound=float | int)
_T_co  = TypeVar("_T_co", covariant=True)
_P     = ParamSpec("_P")




# [ GENERAL ]

Vec  = tuple[_N, ...] | Sequence[_N]
Vec2 = tuple[_N, _N] | Sequence[_N]
Vec3 = tuple[_N, _N, _N] | Sequence[_N]
Vec4 = tuple[_N, _N, _N, _N] | Sequence[_N]

Color = Vec3[int] | Vec4[int]
Point = Vec2[int]


class Property(Protocol[_T_co]):
    def __get__(self, instance: Any, cls: type[Any] | None = None) -> _T_co: ...
    def __set__(self, instance: Any, value: Any): ...




# [ ITEM STUFF ]

# XXX: "uuid", "alias", and "item" are thrown around a lot in
# DPG. They are given specific meaning in the context of this
# project:
#   * uuid : A compatible integer id for an item, in-use or
#   otherwise.
#   * alias: A compatible string id for an item, in-use or
#   otherwise.
#   * item : A uuid or alias tied to an active widget in the
#   registry.
ItemAlias  = str
ItemUUID   = int
Item       = ItemUUID | ItemAlias

Interface = TypeVar("Interface", bound='AppItemType')
ItemType  = TypeVar("ItemType", bound=type['AppItemType'])


_Item_co = TypeVar("_Item_co", covariant=True, bound=int | str)

class ItemCommand(Protocol[_P, _Item_co]):
    __name__: str
    def __call__(self, *, tag: Item = 0, **kwargs) -> _Item_co: ...


class ItemCallback(Protocol):
    __code__: CodeType
    def __call__(self, *args: Unpack[tuple[Item, Any, Any]]) -> Any: ...




class _ItemProperty(Generic[_T]):
    __slots__ = ("_key",)

    def __init__(self, key: str = '', /):
        self._key = key

    def __set_name__(self, cls: type['ItemInterface'], name: str):
        self._key = self._key or name

    def __set__(self, instance: 'ItemInterface', value: Any):
        raise AttributeError(
            f'{type(instance).__qualname__!r} object attribute {self._key!r} is read-only.'
        )


class ItemConfig(_ItemProperty[_T]):
    """Item interface data descriptor. Uses the interface's `.configuration`
    and `.configure` hooks.
    """
    __slots__ = ('__set__',)

    __set__: Callable[..., None]

    def __set_name__(self, cls: type['ItemInterface'], name: str):
        self._key = self._key or name
        # Dynamically generated for performance. 5-million calls
        # ~ 1 second w/potato CPU -- it doesn't get any faster.
        # XXX: Unfortunately, `__get__` can't have the same treatment.
        #      Python will find the `__get__` member descriptor and,
        #      since it's a dunder method, will call the class-level
        #      member i.e. `member_descriptor.__call__`, which doesn't
        #      exist. Any other dunder would work fine, just not `__get__`.
        __set__ = _tools.create_function(
            '__set__',
            ('self', 'instance', 'value'),
            (f"instance.configure({self._key}=value)",)
        )
        self.__set__ = MethodType(__set__, self)

    def __get__(self, instance: 'ItemInterface', cls: type['ItemInterface'] | None = None) -> _T:
        if instance is None:
            return self  # type: ignore
        return instance.configuration()[self._key]



class ItemInfo(_ItemProperty[_T]):
    """Item interface descriptor. Uses the interface's `.information` hook.
    """
    __slots__ = ()

    def __get__(self, instance: 'ItemInterface', cls: type['ItemInterface'] | None = None) -> _T:
        if instance is None:
            return self  # type: ignore
        return instance.information()[self._key]


class ItemState(_ItemProperty[_T]):
    """Item interface descriptor. Uses the interface's `.state` hook.
    """
    __slots__ = ()

    def __get__(self, instance: 'ItemInterface', cls: type['ItemInterface'] | None = None) -> _T | None:
        if instance is None:
            return self  # type: ignore
        return instance.state().get(self._key, None)




null_itemtype = 0, "mvAppItemType::mvAppItem"  # 0 == dearpygui.mvAll

def null_command(*args, tag: Item = 0, **kwargs) -> Item:
    """Default 'command' value for item interface types."""
    return tag


class ItemInterfaceMeta(type(Protocol), abc.ABCMeta):
    __slots__ = ()

    identity: tuple[int, str]
    command : ItemCommand

    def __new__(__mcls: type[Self], __name: str, __bases: tuple[type, ...], __namespace: dict[str, Any], **kwargs: Any) -> Self:
        cls = super().__new__(__mcls, __name, __bases, __namespace, **kwargs)
        if not hasattr(cls, 'command'):
            setattr(cls, 'command', staticmethod(null_command))
        if not hasattr(cls, 'identity'):
            setattr(cls, 'identity', (-hash(cls), cls.__qualname__))
        return cls

    def __int__(self) -> int:
        return self.identity[0]

    def __str__(self) -> str:
        return self.identity[1]

    def __repr__(self) -> str:
        return f"<class {self.__qualname__!r}>"

    def register(self, cls: type[_T]) -> type[_T]:
        # This should only be used internally, and only a couple of
        # times (max).
        assert isinstance(cls, ItemInterface)
        return super().register(cls)


@runtime_checkable
class ItemInterface(Protocol, metaclass=ItemInterfaceMeta):
    """Minimal item API for non-item types."""
    __slots__ = ()

    def __repr__(self):
        config = ', '.join(f"{k}={str(v)!r}" for k, v in self.configuration().items())
        return f"{type(self).__qualname__}({config})"

    @property
    def tag(self) -> ItemUUID:
        return -hash(self)  # signed -- avoids DPG uuid conflicts

    @property
    def alias(self) -> ItemAlias:
        return str(self.tag)

    parent: Item | None = None

    @abc.abstractmethod
    def configure(self, **kwargs) -> None: ...

    @abc.abstractmethod
    def configuration(self) -> Mapping[str, Any]: ...

    def information(self) -> Mapping[str, Any]:
        info = dict(ITEM_INFO_TEMPLATE)
        info['type'] = self.identity[1]  # type:ignore
        return info

    def state(self) -> Mapping[str, Any]:
        return dict(ITEM_STATE_TEMPLATE)

# Only virtual subclasses (`AppItemType`) need to define these, as
# the metaclass ensures that subclasses have these attributes. I
# don't want pyright complaining about it all the friggin' time.
ItemInterface.__annotations__.update(
    identity=tuple[int, str],
    command=ItemCommand,
)



class ItemInfoDict(TypedDict):
    children                        : Mapping[Literal[0, 1, 2, 3], list[Item]]
    type                            : str
    target                          : int
    parent                          : Item | None
    theme                           : Item | None
    handlers                        : Item | None
    font                            : Item | None
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

ITEM_INFO_TEMPLATE: ItemInfoDict = MappingProxyType(
    ItemInfoDict(
        children=MappingProxyType(dict.fromkeys(range(4), ())),  # type:ignore
        type="",
        target=1,
        parent=None,
        theme=None,
        handlers=None,
        font=None,
        container=False,
        hover_handler_applicable=False,
        active_handler_applicable=False,
        focus_handler_applicable=False,
        clicked_handler_applicable=False,
        visible_handler_applicable=False,
        edited_handler_applicable=False,
        activated_handler_applicable=False,
        deactivated_handler_applicable=False,
        deactivatedae_handler_applicable=False,
        toggled_open_handler_applicable=False,
        resized_handler_applicable=False,
    )
)


class ItemStateDict(TypedDict):
    ok                   : Required[bool]
    pos                  : Vec2[int] | None
    hovered              : bool | None
    active               : bool | None
    focused              : bool | None
    clicked              : bool | None
    left_clicked         : bool | None
    right_clicked        : bool | None
    middle_clicked       : bool | None
    visible              : bool | None
    edited               : bool | None
    activated            : bool | None
    deactivated          : bool | None
    resized              : bool | None
    rect_min             : Vec2[int] | None
    rect_max             : Vec2[int] | None
    rect_size            : Vec2[int] | None
    content_region_avail : Vec2[int] | None

ITEM_STATE_TEMPLATE: ItemStateDict = MappingProxyType(  # type:ignore
    ItemStateDict(
        ok=True,
        pos=None,
        hovered=None,
        active=None,
        focused=None,
        clicked=None,
        left_clicked=None,
        right_clicked=None,
        middle_clicked=None,
        visible=None,
        edited=None,
        activated=None,
        deactivated=None,
        resized=None,
        rect_min=None,
        rect_max=None,
        rect_size=None,
        content_region_avail=None,
    )
)






# Dear PyGui buffer types

# NOTE: The proper *index* argument type of the below `__get/setitem__`
# methods is `SupportsIndex`. Normal Python arrays will throw
# `IndexError` when out-of-range, however, DPG's buffers will NOT.
# Since `mvVec4` and `mvMat4` are s

class mvBuffer(Protocol):
    """Protocol for Dear PyGui's `mvBuffer` type."""
    def __init__(self, length: int = 0) -> None: ...
    def __str__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, __i: SupportsIndex, /) -> float: ...
    def __setitem__(self, __i: SupportsIndex, __value: float, /) -> None: ...
    def get_width(self) -> int: ...
    def get_height(self) -> int: ...
    def clear_value(self, __initial_value: float, /) -> None: ...


class mvVec4(Protocol):
    """Protocol for Dear PyGui's 4-dimensional vector type `mvVec4`.

    >NOTE: `IndexError` is NOT thrown when the index is out-of-range.
    """
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0) -> None: ...
    def __str__(self) -> str: ...
    def __len__(self) -> Literal[4]: ...
    def __getitem__(self, __i: SupportsIndex, /) -> float: ...
    def __setitem__(self, __i: SupportsIndex, __value: float, /) -> None: ...
    def __add__(self, __other: Self, /) -> Self: ...
    def __radd__(self, __other: Self, /) -> Self: ...
    def __sub__(self, __other: Self, /) -> Self: ...
    def __rsub__(self, __other: Self, /) -> Self: ...
    def __mul__(self, __other: Self | float, /) -> Self: ...
    def __rmul__(self, __other: Self | float, /) -> Self: ...


class mvMat4(Protocol):
    """Protocol for Dear PyGui's 4x4 matrix type `mvMat4`.

    >NOTE: `IndexError` is NOT thrown when the index is out-of-range.
    """
    def __init__(self, m00: float = 0.0, m01: float = 0.0, m02: float = 0.0, m03: float = 0.0, m10: float = 0.0, m11: float = 0.0, m12: float = 0.0, m13: float = 0.0, m20: float = 0.0, m21: float = 0.0, m22: float = 0.0, m23: float = 0.0, m30: float = 0.0, m31: float = 0.0, m32: float = 0.0, m33: float = 0.0) -> None: ...
    def __str__(self) -> str: ...
    def __len__(self) -> Literal[16]: ...
    def __getitem__(self, __i: SupportsIndex, /) -> float: ...
    def __setitem__(self, __i: SupportsIndex, __value: float, /) -> None: ...
    def __add__(self, __other: Self, /) -> Self: ...
    def __radd__(self, __other: Self, /) -> Self: ...
    def __sub__(self, __other: Self, /) -> Self: ...
    def __rsub__(self, __other: Self, /) -> Self: ...
    def __mul__(self, __other: Self | float, /) -> Self: ...
    def __rmul__(self, __other: Self | float, /) -> Self: ...
