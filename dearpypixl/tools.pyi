from typing import TypeVar, Generic, Sized, Hashable, Container


_T = TypeVar("_T", int, float)

class mvBuffer(Generic[_T], Sized, Hashable, Container):
    """Type inferrence for DearPyGui's mvBuffer type."""
    def __init__(self, length: int = 0): ...
    def __str__(self) -> str: ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def get_width(self) -> int:
        """Return the width of the buffer."""
    def get_height(self) -> int:
        """Return the height of the buffer."""
    def clear_value(self, value) -> None:
        """Sets all values in the buffer to <value>."""


class mvVec4(Generic[_T], Sized, Hashable, Container):
    """Type inferrence for DearPyGui's mvVec4 type."""


class mvMat4(Generic[_T], Sized, Hashable, Container):
    """Type inferrence for DearPyGui's mvMat4 type."""