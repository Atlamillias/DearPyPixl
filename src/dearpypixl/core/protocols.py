""":meta private:"""
import sys
import typing
from typing import Never

from dearpygui import dearpygui as _dearpygui

if typing.TYPE_CHECKING:
    from types import CodeType as Code




# [ sentinel type ]

if typing.TYPE_CHECKING:

    @typing.final
    class sentinel[T: typing.LiteralString](type):
        @property
        def __name__(self, /) -> str: ...  # type: ignore
        @property
        def __qualname__(self, /) -> str: ...  # type: ignore
        @property
        def __module__(self, /) -> str: ...  # type: ignore
        @property
        def __doc__(self, /) -> str | None: ...  # type: ignore
        @__doc__.setter
        def __doc__(self, value: str | None, /) -> None: ...  # type: ignore
        def __new__(cls, name: T, module: str | None = None, /, doc: str | None = None) -> sentinel[T]: ...
        def __call__(self, /) -> typing.Never: ...
        def __bool__(self, /) -> typing.Never: ...
        def __delattr__(self, name: str, /) -> typing.Never: ...
else:
    def _sentinel__new__(*args):
        raise TypeError("sentinel cannot be instantiated")

    _sentinel__new__.__name__ = "__new__"
    _sentinel__new__.__qualname__ = "sentinel.__new__"

    _ALLOWED_SENTINEL_BASES = (object, type, typing.Generic)

    class sentinel[T: typing.LiteralString](type):  # type: ignore
        __slots__ = ()

        __final__ = True

        def __new__(cls, name: str, module = None, /, doc: str | None = None):
            if module is None:
                module = sys._getframemodulename(1) or __name__

            namespace = {
                "__slots__": (),
                "__module__": module,
                "__doc__": doc,
                "__new__": _sentinel__new__,  # mostly irrelevent due to `__call__()`
            }

            return type.__new__(cls, name, (), namespace)

        def __call__(self, /) -> typing.Never:
            raise TypeError("sentinel cannot be instantiated")

        def __repr__(self, /) -> str:
            return f"<sentinel '{self.__name__}'>"

        def __bool__(self, /):
            return False
            #raise TypeError("sentinel does not support boolean operations")

        def __setattr__(self, name: str, value: typing.Any, /):
            # Sentinels should be frozen (immutable), but the behavior is difficult
            # to emulate for classes created via Python code since we can't wrap
            # `__dict__` in a `mappingproxy()` like a built-in. Additionally, the
            # interpreter may need to set something post-creation like `__parameters__`.
            # Instead, allow non-callable dunders to be set and block everything else.
            if name.startswith("__") and name.endswith("__") and not callable(value):
                return type.__setattr__(self, name, value)
            raise AttributeError("sentinel type is immutable")

        def __delattr__(self, name: str, /) -> typing.Never:
            if hasattr(self, name):
                raise AttributeError("sentinel type is immutable")
            raise AttributeError(f"sentinel has no attribute {name!r}")

        def __instancecheck__(self, instance: typing.Any, /) -> bool:
            return self is instance



# [ primitives ]

MISSING = sentinel("MISSING")


class Array[T, S: int = typing.Any](typing.Protocol):
    __slots__ = ()
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> T: ...
    def __iter__(self, /) -> typing.Iterator[T]: ...

class Function[**P, T](typing.Protocol):
    __slots__ = ()
    __name__: str
    __code__: Code
    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> T: ...

class Descriptor[GT](typing.Protocol):
    __slots__ = ()
    @typing.overload
    def __get__(self, instance: None, owner: type, /) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: typing.Any, owner: typing.Any = ..., /) -> GT: ...

class DataDescriptor[GT, ST = sentinel](Descriptor[GT], typing.Protocol):
    __slots__ = ()
    @typing.overload
    def __set__(self, instance: typing.Any, value: ST, /) -> None: ...
    @typing.overload
    def __set__(self: DataDescriptor[GT, sentinel], instance: typing.Any, value: GT, /) -> None: ...

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


type Mappable[KT: typing.Hashable, VT] = SupportsKeysAndGetItem[KT, VT] | typing.Iterable[tuple[KT, VT]]




# [ item-related ]

type Item = int | str


class ItemCommand[**P](typing.Protocol):
    __name__: str
    __defaults__: tuple
    __kwdefaults__: dict[str, typing.Any] | None
    def __call__(self, /, *args: P.args, **kwargs: P.kwargs) -> Item: ...


class ItemCallback0(Function, typing.Protocol):
    def __call__(self, /) -> typing.Any: ...

class ItemCallback1[T: Item](Function, typing.Protocol):
    def __call__(self, sender: T, /) -> typing.Any: ...

class ItemCallback2[T1: Item, T2](Function, typing.Protocol):
    def __call__(self, sender: T1, app_data: T2, /) -> typing.Any: ...

class ItemCallback3[T1: Item, T2, T3](Function, typing.Protocol):
    def __call__(self, sender: T1, app_data: T2, user_data: T3, /) -> typing.Any: ...

type ItemCallback[T1: Item = Item, T2 = typing.Any, T3 = typing.Any] = (
    ItemCallback0 | ItemCallback1[T1] | ItemCallback2[T1, T2] | ItemCallback3[T1, T2, T3]
)




# [ DearPyGui buffers ]

class mvBuffer:
    """Protocol for DearPyGui's `mvBuffer`."""
    __name__: typing.ClassVar[str]
    def __new__(cls, length: int = 0) -> mvBuffer: ...
    def __str__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> float: ...
    def __setitem__(self, index: typing.SupportsIndex, value: float, /) -> None: ...
    def get_width(self) -> int: ...
    def get_height(self) -> int: ...
    def clear_value(self, initial_value: float, /) -> None: ...

mvBuffer = typing.cast(type[mvBuffer], _dearpygui.mvBuffer)  # ty:ignore[invalid-assignment]


class mvVec4:
    """Protocol for DearPyGui's `mvVec4`."""
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

mvVec4 = typing.cast(type[mvVec4], _dearpygui.mvVec4)  # ty:ignore[invalid-assignment]


class mvMat4:
    """Protocol for DearPyGui's `mvMat4`."""
    __name__: typing.ClassVar[str]
    def __new__(cls, m00: float = 0.0, m01: float = 0.0, m02: float = 0.0, m03: float = 0.0, m10: float = 0.0, m11: float = 0.0, m12: float = 0.0, m13: float = 0.0, m20: float = 0.0, m21: float = 0.0, m22: float = 0.0, m23: float = 0.0, m30: float = 0.0, m31: float = 0.0, m32: float = 0.0, m33: float = 0.0) -> mvMat4: ...
    def __str__(self, /) -> str: ...
    def __len__(self, /) -> typing.Literal[16]: ...
    def __getitem__(self, index: typing.SupportsIndex, /) -> float: ...
    def __setitem__(self, index: typing.SupportsIndex, value: float, /) -> None: ...
    def __add__(self, other: typing.Self, /) -> mvMat4: ...
    def __radd__(self, other: typing.Self, /) -> mvMat4: ...
    def __sub__(self, other: typing.Self, /) -> mvMat4: ...
    def __rsub__(self, other: typing.Self, /) -> mvMat4: ...
    def __mul__(self, other: typing.Self | float, /) -> mvMat4: ...
    def __rmul__(self, other: typing.Self | float, /) -> mvMat4: ...

mvMat4 = typing.cast(type[mvMat4], _dearpygui.mvMat4)  # ty:ignore[invalid-assignment]




# [ other types ]

type true = typing.Literal[True]
type false = typing.Literal[False]


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
    def __delete__(self, instance, /) -> typing.Any: ...  # type: ignore
    del __new__, __get__, __set__, __delete__

    def getter[_GT](self: Property[typing.Any, ST, D], getter: _FGet[_GT], /) -> Property[_GT, ST, D]:
        return __class__(getter, self.fset, self.fdel, self.__doc__)

    def setter[_ST](self: Property[GT, typing.Any, D], setter: _FSet[_ST], /) -> Property[GT, _ST, D]:
        return __class__(self.fget, setter, self.fdel, self.__doc__)

    def deleter(self: Property[GT, ST, typing.Any], deleter: _FDel, /) -> Property[GT, ST, true]:
        return __class__(self.fget, self.fset, deleter, self.__doc__)
