import enum
import numbers
import threading
import dataclasses
from dearpygui._dearpygui import (
    get_viewport_configuration as _viewport_get_config,
    get_item_configuration as _item_get_config,
    get_item_state as _item_get_state,
    configure_item as _item_set_config,

)
from typing import (

    Any,

    Self,
    NamedTuple,
    Protocol,
    Callable,
    Literal,
    Sequence,
    Mapping,
    Generic,
    Iterator,
    SupportsIndex,
    Sized,
    Iterable,
    TypeVar,
    overload,
)




# [ GENERAL TYPING ]

_T = TypeVar('_T')
_N = TypeVar('_N', bound=numbers.Real)



Point = tuple[int, int]
Rect  = tuple[int, int, int, int]  # x1, y1, x2, y2 / left, top, right, bottom
Item  = int | str




# [ RECT GETTERS/SETTERS ]

class _RectGetter(Protocol):
    """A function that returns the width and height of an item."""
    def __call__(self, item: Item) -> tuple[int, int]: ...

class _RectSetter(Protocol):
    """A function that updates an item's size and position."""
    def __call__(self, item: Item, width: float, height: float, x_pos: float, y_pos: float) -> Any: ...


def get_item_size_from_config(item: Item) -> tuple[int, int]:
    config = _item_get_config(item)
    return config['width'], config['height']

def get_item_size_from_state(item: Item) -> tuple[int, int]:
    return _item_get_state(item)['rect_size']

def set_item_size(item: Item, width: float, height: float, x_pos: float, y_pos: float):
    if not width and not height:
        _item_set_config(item, pos=(int(x_pos), int(y_pos)), show=False)
    else:
        _item_set_config(
            item,
            width=int(width),
            height=int(height),
            pos=(int(x_pos), int(y_pos)),
            show=True,
        )


def get_viewport_size(viewport: str = "DPG NOT USED YET") -> tuple[int, int]:
    config = _viewport_get_config(viewport)
    return config['client_width'], config['client_height']




# [ ITEM POSITION CALCULATORS ]

class _PositionCalc(Protocol):
    def __call__(self, item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float, /) -> tuple[float, float]: ...


_ANCHOR_MAP: dict[str, _PositionCalc] = {}

def _get_positioner(key: str):
    try:
        return _ANCHOR_MAP[key.casefold()]
    except AttributeError:
        return _ANCHOR_MAP[key]  # raise `KeyError`

def _anchor_position(*anchors: str) -> Callable[[_PositionCalc], _PositionCalc]:
    def register_anchor_fn(fn: _PositionCalc) -> _PositionCalc:
        for s in anchors:
            _ANCHOR_MAP[s.lower()] = fn  # type: ignore
        return fn
    return register_anchor_fn


@_anchor_position("n", "north")
def _anchor_position_N(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) / 2 + cell_x, cell_y  # center x

@_anchor_position("ne", "northeast")
def _anchor_position_NE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) + cell_x, cell_y

@_anchor_position("e", "east")
def _anchor_position_E(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) + cell_x, (cell_ht - item_ht) / 2 + cell_y  # center y

@_anchor_position("se", "southeast")
def _anchor_position_SE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) + cell_x, (cell_ht - item_ht) + cell_y

@_anchor_position("s", "south")
def _anchor_position_S(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) / 2 + cell_x, (cell_ht - item_ht) + cell_y  # center x

@_anchor_position("sw", "southwest")
def _anchor_position_SW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return cell_x, (cell_ht - item_ht) + cell_y

@_anchor_position("w", "west")
def _anchor_position_W(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return cell_x, (cell_ht - item_ht) / 2 + cell_y  # center y

@_anchor_position("nw", "northwest")
def _anchor_position_NW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return cell_x, cell_y

@_anchor_position("c", "center", "centered")
def _anchor_position_C(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[float, float]:
    return (cell_wt - item_wt) / 2 + cell_x, (cell_ht - item_ht) / 2 + cell_y  # center x & y



# [ HELPER FUNCTIONS ]

_PointV = int | tuple[int, int] | Sequence[int]

def _to_4point(x: _PointV, y: _PointV) -> tuple[int, int, int, int]:
    if isinstance(x, (int, float)):
        x1 = x2 = x
    else:
        x1, x2 = x
    if isinstance(y, (int, float)):
        y1 = y2 = y
    else:
        y1, y2 = y
    return x1, y1, x2, y2


def _normalize_cellspan(r1: int, c1: int, r2: int, c2: int, rows: int, cols: int):
    r1 %= rows
    c1 %= cols
    r2 %= rows
    c2 %= cols
    if r1 > r2:
        r1, r2 = r2, r1
    if c1 > c2:
        c1, c2 = c2, c1
    return r1, c1, r2, c2


def _not_implemented(*args, **kwargs):
    raise NotImplementedError()




# [ GRID COMPONENTS ]

class _Configure(Generic[_T]):
    __slots__ = ("_key",)

    def __init__(self, key: str = '', /):
        self._key = key

    def __set_name__(self, cls: type, name: str):
        self._key = self._key or name

    @overload
    def __get__(self, inst: Any, cls: type | None = ...) -> _T: ...
    @overload
    def __get__(self, inst: None, cls: type | None = None) -> Self: ...
    def __get__(self, inst: Any, cls: Any = None):
        if inst is None:
            return self
        return inst.configuration()[self._key]

    def __set__(self, inst: Any, value: Any):
        inst.configure(**{self._key: value})


@dataclasses.dataclass(slots=True)
class ItemData:
    item      : Item
    cellspan  : tuple[int, int, int, int]
    positioner: _PositionCalc             = _get_positioner('centered')
    max_size  : tuple[int, int]           = (0, 0)
    padding   : tuple[int, int, int, int] = (0, 0, 0, 0)

    def __hash__(self):
        return hash(self.item)




@dataclasses.dataclass(init=False)
class Slot:
    """Contains size settings for a `Grid` row or column."""
    __slots__ = ( '_label', '_size', '_weight')

    def __init__(self, label: str = '', *, weight: float = 1.0, size: int = 0):
        self.configure(label=label, size=size, weight=weight)

    label : _Configure[str]   = dataclasses.field(default=_Configure('label'))
    weight: _Configure[float] = dataclasses.field(default=_Configure('weight'))
    size  : _Configure[int]   = dataclasses.field(default=_Configure('size'))

    @overload
    def configure(self, *, label: str = ..., weight: float = ..., size: int = ...): ...  # type: ignore
    def configure(self, **kwargs):
        if 'label' in kwargs:
            self._label = kwargs['label']
        if 'weight' in kwargs:
            self._weight = max(0.0, kwargs['weight'] or 0.0)
        if 'size' in kwargs:
            self._size = max(0, int(kwargs['size'] or 0))

    def configuration(self) -> dict[Literal['label', 'weight', 'size'], str | float]:
        return {
            'label' : self._label,
            'weight': self._weight,
            'size'  : self._size,
        }

    @property
    def policy(self) -> Literal['FIXED', 'SIZED']:
        return 'FIXED' if self._size else 'SIZED'


class Axis(Iterable[Slot], Sized):
    """Container object for a `Grid`s rows/columns.

    Row/columns are identified by their positions (index) in the
    axis. Indexing the `Axis` instance returns a `Slot` object
    containing the size settings for that row or column.

    Instances are treated as immutable, unsigned pseudo-integrals
    for most operations; the value of which is a representation
    of the number of slots in the axis. However, in-place
    operations directly affect the number of slots they contain.
    Whenever a slot is added or removed, it is done to/from the
    end of the axis.
    """

    # Slot members are identified only by their positions (index)
    # in the axis. In-place ops directly modify the number of
    # slots. Otherwise, treat the object as an immutable, unsigned
    # pseudo-integral representing the number of contained slots.

    __slots__ = ('_label', '_slots', '_lock')

    _slots: list[Slot]

    def __init__(self, length: int = 0, *, label: str = '') -> None:
        self._slots = []
        self._lock  = threading.Lock()
        self.configure(label=label, length=length)

    label : _Configure[str] = _Configure()
    length: _Configure[int] = _Configure()

    @overload
    def configure(self, *, label: str = ..., length: int = ...): ...  # type: ignore
    def configure(self, **kwargs):
        if 'label' in kwargs:
            self._label = kwargs['label']
        if 'length' in kwargs:
            self.resize(kwargs['length'])

    def configuration(self) -> dict[Literal['label', 'length'], str | int]:
        with self._lock:
            return {'label': self._label, 'length': len(self)}

    def __repr__(self):
        return f"{type(self).__qualname__}(label={self._label}, length={len(self)!r})"

    def __str__(self):
        return str(self._slots)

    def __bool__(self):
        return bool(self._slots)

    def __len__(self) -> int:
        # TODO: check for concurrency issues
        return len(self._slots)

    __int__ = __index__ = __len__

    def __float__(self):
        return float(len(self))

    def __complex__(self):
        return complex(len(self))

    def __lt__(self, other: Any) -> bool:
        return len(self) < other

    def __le__(self, other: Any) -> bool:
        return len(self) <= other

    def __eq__(self, other: Any) -> bool:  # XXX: `__hash__ == None`
        return len(self) == other

    def __ne__(self, other: Any) -> bool:
        return len(self) != other

    def __gt__(self, other: Any) -> bool:
        return len(self) > other

    def __ge__(self, other: Any) -> bool:
        return len(self) >= other

    @property
    def weight(self) -> float:
        return sum(s._weight for s in self._slots if not s._size)

    @property
    def min_size(self) -> int:
        return sum(s._size for s in self._slots)


    # Number Behaviors (no bitwise)

    def __pos__(self):
        return +len(self)

    def __neg__(self):
        return -len(self)

    def __add__(self, x: _N) -> _N:
        return len(self) + x

    def __sub__(self, x: _N) -> _N:
        return len(self) - x

    def __mul__(self, x: _N) -> _N:
        return len(self) * x

    def __truediv__(self, x: _N) -> _N:
        return len(self) * x

    def __floordiv__(self, x: _N) -> _N | float:
        return len(self) // x

    def __mod__(self, x: _N) -> _N:
        return len(self) % x

    def __divmod__(self, x: Any) -> tuple[float, float]:
        length = len(self)
        return (length // x, length % x)

    def __pow__(self, x: int, mod: int | None = None) -> int:
        return pow(len(self), x, mod)

    def __round__(self, ndigits: int = 0):
        return round(len(self), ndigits)

    __trunc__ = __floor__ = __ceil__ = __abs__ = __int__


    # Sequence Methods

    def __getitem__(self, index: SupportsIndex) -> Slot:
        with self._lock:
            return self._slots[index]

    def __iter__(self) -> Iterator[Slot]:
        with self._lock:
            yield from self._slots

    def __iadd__(self, x: int) -> Self:
        """
        >>> x = Axis(4)
        >>> x += 8
        >>> len(x)
        12
        >>> x += 0
        >>> len(x)
        12
        >>> x += -10  # __isub__
        >>> len(x)
        2
        """
        if not x:
            return self
        if x > 0:
            with self._lock:
                self._slots.extend(Slot(self._label) for _ in range(x))
                return self
        return self.__isub__(abs(x))

    def __isub__(self, x: int) -> Self:
        """
        >>> x = Axis(12)
        >>> x -= 8
        >>> len(x)
        4
        >>> x -= 0
        >>> len(x)
        4
        >>> x -= -10  # __iadd__
        >>> len(x)
        12
        """
        if not x:
            return self
        if x > 0:
            with self._lock:
                del self._slots[-x:]
                return self
        return self.__iadd__(abs(x))

    def resize(self, length: int):
        """Add/remove slots from the axis so that it contains the number
        of slots specified.

        Args:
            * length: A positive number indicating the target length of
            the axis.


        Slots are always added to, and removed from, the end of the axis.


        >>> x = Axis(8)
        >>> x.resize(2)  # trim
        >>> len(x)
        2
        >>> x.resize(12)  # extend
        >>> len(x)
        12
        """
        if length < 0:
            raise ValueError(f'`length` cannot be less than zero (got {length!r}).')
        return self.__iadd__(length-len(self))

    def __imul__(self, x: int):  # NOTE: ROUNDS DOWN
        """
        >>> x = Axis(4)
        >>> x *= 4
        >>> len(x)
        16
        >>> x *= 0.73  # trunc 11.68
        >>> len(x)
        11
        """
        if x < 0:
            raise ValueError(f'cannot multiply slots by a negative number (got {x!r}).')
        return self.resize(int(len(self) * x))

    def __itruediv__(self, x: float):  # NOTE: ROUNDS DOWN (floor division)
        """
        >>> x = Axis(16)
        >>> x /= 2
        >>> len(x)
        8
        >>> x /= 3  # floor div
        2
        """
        if x < 0:
            raise ValueError(f"cannot divide slots by a negative number (got {x!r}).")
        return self.resize(len(self) // x)  # type: ignore

    __ifloordiv__ = __itruediv__

    def insert(self, index: SupportsIndex):
        """Adds a new row/column at the specified index.

        Args:
            * index: Position of the new slot.
        """
        with self._lock:
            self._slots.insert(index, Slot(self._label))

    def remove(self, index: SupportsIndex = -1):
        """Delete the row/column at the specified index, or the last
        row/column if not specified.

        Args:
            * index: Target slot index.
        """
        with self._lock:
            self._slots.pop(index)



class Grid:
    # __slots__ = ()

    def __init_subclass__(cls) -> None:
        # ensure that DearPyGui can always call subclass instances
        if "__call__" in cls.__dict__ and "__code__" not in cls.__dict__:
            cls.__dict__["__code__"] = cls.__call__.__code__

    def __init__(
        self,
        rows: int = 1,
        cols: int = 1,
        *,
        label     : str  = '',
        width     : int  = 0,
        height    : int  = 0,
        padding   : tuple[_PointV, _PointV] | Sequence[_PointV] = (0, 0),
        spacing   : tuple[_PointV, _PointV] | Sequence[_PointV] = (0, 0),
        parent    : Item = 0,
    ):
        """Args:
            * rows: Number of initial rows.

            * cols: Number of initial columns.

            * label: An informal display name for the grid.

            * parent: The unique identifier of an existing item whose size
            will be used as the grid's "frame-of-reference".

            * width: Overrides the *parent* width when sizing the grid.

            * height: Overrides the *parent* height when sizing the grid.

            * padding: The number of pixels between cells and the inner walls
            of the grid.

            * spacing: The number of pixels between cell walls.


        Unlike Dear PyGui, *parent* is not limited to container items. However,
        the item must support explicit positioning (`pos`). In addition, the
        item must have a calculated rect size, or be sizable using the `width`
        and `height` configuration.

        When *parent* is unspecified, the grid will try to use the item
        atop the container stack instead.

        Both *padding* and *spacing* must be a 2-item sequence where each
        value is an integer or 2-item sequence of integers. The first item
        in the outer sequence refers to the left and upper padding/spacing
        values as `[x1, y1]`, while the second item contains the right and
        lower values as `[x2, y2]`. If either value in the outer sequence
        is an integer, its' value will be used for both *x* and *y*. For
        example, `([2, 4], 4)` expands to `([2, 4], [4, 4])`.

        When *width* or *height* is 0, auto-sizing is disabled for 
        The grid's size will be equal to *width* and/or *height*, falling
        back to the size of *parent* for each unspecified component.
        The grid will scale to the size of *parent*, but will use *width*
        and/or *height* if set.
        """
        self.cols = Axis(cols, label='x')
        self.rows = Axis(rows, label='y')


g = Grid(3, 2)

g.cols += 4