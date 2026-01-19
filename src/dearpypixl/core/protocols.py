import typing
from typing import Never

from dearpygui import dearpygui as _dearpygui

if typing.TYPE_CHECKING:
    from types import CodeType as Code




# [ primitive types ]

type Item = int | str


class ItemCommand[**P](typing.Protocol):
    __name__: str
    __defaults__: tuple
    __kwdefaults__: dict[str, typing.Any] | None
    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> Item: ...




class _FunctionLike(typing.Protocol):
    __name__: str
    __code__: Code

class ItemCallback0(_FunctionLike, typing.Protocol):
    def __call__(self, /) -> typing.Any: ...

class ItemCallback1[T: Item](_FunctionLike, typing.Protocol):
    def __call__(self, sender: T, /) -> typing.Any: ...

class ItemCallback2[T1: Item, T2](_FunctionLike, typing.Protocol):
    def __call__(self, sender: T1, app_data: T2, /) -> typing.Any: ...

class ItemCallback3[T1: Item, T2, T3](_FunctionLike, typing.Protocol):
    def __call__(self, sender: T1, app_data: T2, user_data: T3, /) -> typing.Any: ...

type ItemCallback[T1: Item = Item, T2 = typing.Any, T3 = typing.Any] = (
    ItemCallback0 | ItemCallback1[T1] | ItemCallback2[T1, T2] | ItemCallback3[T1, T2, T3]
)




# [ Dear PyGui buffers ]

class mvBuffer:
    """Protocol for Dear PyGui's `mvBuffer`."""
    __name__: typing.ClassVar[str]
    def __new__(cls, length: int = 0) -> mvBuffer: ...
    def __str__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> float: ...
    def __setitem__(self, index: typing.SupportsIndex, value: float, /) -> None: ...
    def get_width(self) -> int: ...
    def get_height(self) -> int: ...
    def clear_value(self, initial_value: float, /) -> None: ...

mvBuffer = typing.cast(type[mvBuffer], _dearpygui.mvBuffer)


class mvVec4:
    """Protocol for Dear PyGui's `mvVec4`."""
    __name__: typing.ClassVar[str]
    def __new__(cls, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0) -> mvVec4: ...
    def __str__(self) -> str: ...
    def __len__(self) -> typing.Literal[4]: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> float: ...
    def __setitem__(self, index: typing.SupportsIndex, value: float, /) -> None: ...
    def __add__(self, other: typing.Self, /) -> mvVec4: ...
    def __radd__(self, other: typing.Self, /) -> mvVec4: ...
    def __sub__(self, other: typing.Self, /) -> mvVec4: ...
    def __rsub__(self, other: typing.Self, /) -> mvVec4: ...
    def __mul__(self, other: typing.Self | float, /) -> mvVec4: ...
    def __rmul__(self, other: typing.Self | float, /) -> mvVec4: ...

mvVec4 = typing.cast(type[mvVec4], _dearpygui.mvVec4)


class mvMat4:
    """Protocol for Dear PyGui's `mvMat4`."""
    __name__: typing.ClassVar[str]
    def __new__(cls, m00: float = 0.0, m01: float = 0.0, m02: float = 0.0, m03: float = 0.0, m10: float = 0.0, m11: float = 0.0, m12: float = 0.0, m13: float = 0.0, m20: float = 0.0, m21: float = 0.0, m22: float = 0.0, m23: float = 0.0, m30: float = 0.0, m31: float = 0.0, m32: float = 0.0, m33: float = 0.0) -> mvMat4: ...
    def __str__(self) -> str: ...
    def __len__(self) -> typing.Literal[16]: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> float: ...
    def __setitem__(self, index: typing.SupportsIndex, value: float, /) -> None: ...
    def __add__(self, other: typing.Self, /) -> mvMat4: ...
    def __radd__(self, other: typing.Self, /) -> mvMat4: ...
    def __sub__(self, other: typing.Self, /) -> mvMat4: ...
    def __rsub__(self, other: typing.Self, /) -> mvMat4: ...
    def __mul__(self, other: typing.Self | float, /) -> mvMat4: ...
    def __rmul__(self, other: typing.Self | float, /) -> mvMat4: ...

mvMat4 = typing.cast(type[mvMat4], _dearpygui.mvMat4)




# [ other types ]

type true = typing.Literal[True]
type false = typing.Literal[False]


class SupportsKeysAndGetItem[KT, VT](typing.Protocol):
    __slots__ = ()
    def __getitem__(self, key: KT, /) -> VT: ...
    def keys(self) -> typing.Iterable[VT]: ...


class SupportsRichComparison(typing.Protocol):
    __slots__ = ()
    def __lt__(self, other: typing.Any, /) -> typing.Any: ...
    def __le__(self, other: typing.Any, /) -> typing.Any: ...
    def __ge__(self, other: typing.Any, /) -> typing.Any: ...
    def __gt__(self, other: typing.Any, /) -> typing.Any: ...


type _FGet[GT] = typing.Callable[[typing.Any], GT]
type _FSet[ST] = typing.Callable[[typing.Any, ST], None]
type _FDel = typing.Callable[[typing.Any], None]

type _NoDeleter = typing.Literal[False] | None | Never

# XXX: As a protocol, type checkers flag this as incompatible with
# `property()` due to the overloads for `__new__()`. Since type checkers
# handle `property()` uniquely anyway, it's better to just inherit from
# `property()`
class PropertyType(type):
    def __instancecheck__(self, instance: typing.Any, /) -> bool:
        return property.__instancecheck__(instance)

    def __subclasscheck__(self, subclass: type, /) -> bool:
        return property.__subclasscheck__(subclass)

class Property[GT: typing.Any = Never, ST: typing.Any = Never, D: bool = false](property, metaclass=PropertyType):
    __slots__ = ("__doc__",)

    fget: _FGet[GT] | None
    fset: _FSet[ST] | None
    fdel: _FDel | None

    @typing.overload
    def __new__(cls, /, fget: _FGet[GT] | None = None, fset: _FSet[ST] | None = None, fdel: None = None, doc: str | None = None) -> Property[GT, ST, false]: ...
    @typing.overload
    def __new__(cls, /, fget: _FGet[GT] | None, fset: _FSet[ST] | None, fdel: _FDel, doc: str | None = None) -> Property[GT, ST, true]: ...
    @typing.overload
    def __new__(cls, /, fget: _FGet[GT] | None = None, fset: _FSet[ST] | None = None, fdel: _FDel | None = None, doc: str | None = None) -> Property[GT, ST, bool]: ...
    def __new__(cls, *args, **kwargs) -> typing.Any: ...
    @typing.overload
    def __get__(self, instance: None, owner: type, /) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: typing.Any, owner: type | None = None, /) -> GT: ...
    @typing.overload
    def __get__(self: Property[Never, typing.Any, typing.Any], instance: typing.Any, owner: type | None = None, /) -> typing.NoReturn: ...
    def __get__(self, *args) -> typing.Any: ...
    @typing.overload
    def __set__(self, instance: typing.Any, value: ST, /) -> None: ...
    @typing.overload
    def __set__(self: Property[typing.Any, Never, typing.Any], instance: typing.Any, value: Never, /) -> typing.NoReturn: ...
    def __set__(self, *args) -> typing.Any: ...
    @typing.overload
    def __delete__(self: Property[typing.Any, typing.Any, true], instance: typing.Any, /) -> None: ...
    @typing.overload
    def __delete__(self: Property[typing.Any, typing.Any, false], instance: typing.Any, /) -> typing.NoReturn: ...
    def __delete__(self, instance) -> typing.Any: ...
    del __new__, __get__, __set__, __delete__

    def getter[_GT](self: Property[typing.Any, ST, D], getter: _FGet[_GT], /) -> Property[_GT, ST, D]:
        return __class__(getter, self.fset, self.fdel, self.__doc__)

    def setter[_ST](self: Property[GT, typing.Any, D], setter: _FSet[_ST], /) -> Property[GT, _ST, D]:
        return __class__(self.fget, setter, self.fdel, self.__doc__)

    def deleter(self: Property[GT, ST, typing.Any], deleter: _FDel, /) -> Property[GT, ST, true]:
        return __class__(self.fget, self.fset, deleter, self.__doc__)

property = Property


class Descriptor[T](typing.Protocol):
    __slots__ = ()
    @typing.overload
    def __get__(self, instance: None, owner: type, /) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: typing.Any, owner: type | None = None, /) -> T: ...


type Mappable[KT: typing.Hashable, VT] = SupportsKeysAndGetItem[KT, VT] | typing.Iterable[tuple[KT, VT]]


class Array[T](typing.Protocol):
    def __len__(self) -> int: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> T: ...
    def __iter__(self) -> typing.Iterator[T]: ...


# XXX: use for inputs, not outputs
type Array1D[S: int, T: int | float] = typing.Annotated[Array[T], S]
type Point[T: int | float] = Array1D[typing.Literal[2], T]
type Vec3[T: int | float] = Array1D[typing.Literal[3], T]
type Vec4[T: int | float] = Array1D[typing.Literal[4], T]
type Matrix[S1: int, S2: int, T: int | float] = typing.Annotated[Array[Array[T]], tuple[S1, S2]]
type Mat4[T: int | float] = Matrix[typing.Literal[4], typing.Any, T]

type SizedList[N: int, T] = typing.Annotated[list[T], N]

# these can be any sequence, but DPG types them as `list | tuple` only
type RGB[T: int | float] = tuple[T, T, T] | list[T]
type RGBA[T: int | float] = tuple[T, T, T] | tuple[T, T, T, T] | list[T]
