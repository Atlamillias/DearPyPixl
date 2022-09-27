"""Contains commonly-used type aliases and markers."""
import os
import types
from typing import TypeAlias, TypeVar, Generic, Protocol, final
from typing_extensions import TypeVarTuple, Unpack


_S = TypeVarTuple("_S")

class _TypeRepr(type):
    def __repr__(cls):
        return f"<class {cls.__qualname__!r}>"


@final
class Null(metaclass=_TypeRepr):
    """Sentinel value used by DearPyPixl."""

class ItemRef(Protocol):
    def __int__(self) -> int | str: ...

class NullRef(int):
    """Type marker for an item identifier not bound to an Item instance."""


class SizedSequence(Generic[Unpack[_S]]):
    """A list or tuple-like sequence of a fixed size."""


ItemTMember = TypeVar("ItemTMember", str, types.GetSetDescriptorType)

Filepath: TypeAlias = str | os.PathLike

R   : TypeAlias = float
G   : TypeAlias = float
B   : TypeAlias = float
A   : TypeAlias = float
RGBA: TypeAlias = SizedSequence[R, G, B, A] | SizedSequence[R, G, B]

X : TypeAlias = float
Y : TypeAlias = float
XY: TypeAlias = SizedSequence[X, Y] | SizedSequence[X]
