import sys
import numbers
import functools
import threading
import dataclasses
import math
from array import array
import dearpygui.dearpygui as dearpygui
from dearpygui._dearpygui import (
    get_item_configuration as _item_get_config,
    get_item_state as _item_get_state,
    configure_item as _item_set_config,
)
from typing import (
    Any,

    Self,
    Protocol,
    Callable,
    ClassVar,
    Literal,
    Sequence,
    Generic,
    Iterator,
    SupportsIndex,
    Sized,
    Iterable,
    Annotated,
    TypeVar,
    Union,

    overload,
    cast,
)




_T  = TypeVar('_T')
_N  = TypeVar('_N', bound=numbers.Real)

Item   = int | str
FloatV = float | None
Vec2   = Annotated[tuple[FloatV, FloatV]                 | Sequence[FloatV], Literal[2]]
Vec4   = Annotated[tuple[FloatV, FloatV, FloatV, FloatV] | Sequence[FloatV], Literal[4]]

NaN  = math.nan




# [ HELPER FUNCTIONS ]

def _create_context():
    # runs once, then no-op
    dearpygui.create_context()
    @functools.wraps(_create_context)
    def create_context(): ...
    setattr(sys.modules[__name__], _create_context.__name__, create_context)


def _is_nan(v: Any) -> bool:
    return v != v

def _is_nanlike(v: Any) -> bool:
    return v is None or v != v

def _to_value(value: Any, default: Any):
    if value is None or _is_nan(value):
        return default
    return value

def _to_float_arr(value: Sequence[float | None] | float | None, length: int, default: float = NaN) -> 'array[float]':
    """
    # Non-Sequence value (None | float('nan'))
    >>> arr = _to_float_array(None, 2)
    >>> len(arr) == 2 and all(_is_nan(v) for v in arr)
    True
    >>> arr = _to_float_array(float("nan"), 2)
    >>> len(arr) == 2 and all(_is_nan(v) for v in arr)
    True

    # Non-Sequence value (number)
    >>> arr = _to_float_array(20, 4)
    >>> len(arr) == 4 and all(v == 20 for v in arr)
    True

    # Sequence[float | nan | None], len(value) >= 4
    >>> arr = _to_float_array([20, None, float("nan"), 10, 0, 0], 4, -5.0)  # 6-len input
    >>> tuple(arr) == (20, -5.0, -5.0, 10)
    True

    # Sequence[float | float('nan') | None], len(value) < 4
    >>> arr = _to_float_array([20, None], 4, -5.0)
    >>> tuple(arr) == (20, -5.0, -5.0, -5.0)
    True

    """
    if value is None or _is_nan(value):
        return array('f', (default,) * length)
    if isinstance(value, (float, int)):
        return array('f', (value,) * length)

    arr = array('f', (default,) * length)
    try:
        for i in range(length):
            arr[i] = _to_value(value[i], default)
    except IndexError:
        pass
    return arr




# [ MINOR COMPONENTS ]  (major components/helpers of minor ones)

class _RectGetter(Protocol):
    """A function that returns an item's size and position; as
    `(width, height, x_pos, y_pos, is_visible)`.
    """
    def __call__(self, item: Item) -> tuple[int, int, int, int, bool]: ...


def _get_item_rect(item: Item) -> tuple[int, int, int, int, bool]:
    d  = _item_get_state(item)
    if 'visible' in d:
        return *d['rect_size'], *d['pos'], d['visible']  # type: ignore
    return *d['rect_size'], *d['pos'], _item_get_config(item)['show']  # type: ignore




class _RectSetter(Protocol):
    """A function that updates an item's size and position via
    `dearpygui.configure_item`.
    """
    def __call__(self, item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool) -> Any: ...


def _set_item_rect(item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool):
    _item_set_config(
        item,
        width=int(width),
        height=int(height),
        pos=(int(x_pos), int(y_pos)),
        show=show,
    )

def _set_text_rect(item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool):
    _item_set_config(
        item,
        pos=(int(x_pos), int(y_pos)),
        show=show,
    )




class _Positioner(Protocol):
    """Calculates the final position of an item in the occupying cell
    or cellspan.
    """
    def __call__(self, item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float, /) -> tuple[float, float]: ...


_ANCHOR_MAP: dict[str, _Positioner] = {}

def _get_positioner(key: str):
    try:
        return _ANCHOR_MAP[key.casefold()]
    except AttributeError:
        return _ANCHOR_MAP[key]  # raise `KeyError`

def _anchor_position(*anchors: str) -> Callable[[_Positioner], _Positioner]:
    def register_anchor_fn(fn: _Positioner) -> _Positioner:
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




@dataclasses.dataclass(slots=True)
class ItemData:
    """Contains the size and placement information of an item attached
    to a `Grid` object.

    Attributes:
        * item (int | str): The target item's integer uuid or string alias.

        * cellspan (tuple[int, int, int, int]): Contains coordinates for
        the target cell range, as `(col_start, row_start, col_end, row_end)`.

        * max_size (tuple[int, int]): Indicates the item's maximum width
        and height (min 0 per value).

        * padding (tuple[float, float, float, float]): Top-level padding
        override values.

        * positioner (_Positioner): Function used to calculate the item's
        final position.

        * rect_setter (_RectSetter): Callable used to update the item's size,
        position, and visibility status.

        * is_text (bool): If True, the target item an `mvText` object.
    """
    item       : Item
    cellspan   : tuple[int, int, int, int]
    max_size   : Sequence[float]
    padding    : Sequence[float]
    positioner : _Positioner
    rect_setter: _RectSetter
    is_text    : bool

    def __hash__(self):
        return hash(self.item)





# [ MAJOR COMPONENTS ]

class _GridSetting(Generic[_T]):
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


@dataclasses.dataclass(init=False)
class _GridComponent:
    __slots__ = ('_label', '_spacing', '_padding')

    label  : _GridSetting[str]            = dataclasses.field(default=_GridSetting('label'))
    spacing: _GridSetting['array[float]'] = dataclasses.field(default=_GridSetting('spacing'))
    padding: _GridSetting['array[float]'] = dataclasses.field(default=_GridSetting('padding'))

    def __init__(self, *, label: str | None = None, spacing: FloatV = None, padding: Vec2 | FloatV = None, **kwargs):
        self.configure(label=label, spacing=spacing, padding=padding, **kwargs)

    def configure(self, **kwargs) -> None:
        """Update the object's high-level settings.

        Accepts all arguments accepted by the object's constructor
        as keyword arguments.
        """
        if 'label' in kwargs:
            self._label = kwargs['label'] or ''
        if 'padding' in kwargs:
            self._padding = _to_float_arr(kwargs['padding'], 2, NaN)
        if 'spacing' in kwargs:
            spacing = _to_value(kwargs['spacing'], None)
            if spacing is None:
                spacing = NaN
            else:
                spacing = max(0.0, spacing)
            self._spacing = spacing

    def configuration(self) -> dict[str, Any]:
        """Return a mapping of the object's settings and their current values."""
        return {f:getattr(self, f'_{f}') for f in self.__dataclass_fields__}


@dataclasses.dataclass(init=False)
class Slot(_GridComponent):
    """A row or column in a table-like structure.

    Attributes:
        * label: Informal name for the slot.

        * spacing (float): Used to offset the slot's position during a draw
        event. Is ignored for calculations when NaN.

        * padding (array[float, float]): Used as the left/upper and right/lower
        (for columns and rows respectively) padding values for cells in the slot
        during a draw event. Inner NaN values are ignored for calculations.

        * weight (float): During a draw event and when the slot's policy is
        evaluated as "sized", this affects how much the slot is scaled
        in proportion to the size of the grid and the total weight of all
        other slots in the axis.

        * size (int): The width/height (for columns and rows respectively) of
        the slot. When this value is not 0, a "fixed" sizing policy is enforced
        upon the slot, disabling dynamic resizing.


    A slot's sizing policy is not set, but determined during a draw event
    based on the slot's state. A "fixed" policy is enforced whenever a slot's
    `.size` attribute is greater than 0, and uses a "sized" policy otherwise.
    When "fixed", a slot is ensured to always be drawn to it's `.size`.

    A slot is unaware of its' role in the grid (column vs row). A higher-level
    object may indicate this through its' `.label` attribute.
    """
    __slots__ = ('_state', '_size', '_weight')

    weight: _GridSetting[float] = dataclasses.field(default=_GridSetting('weight'))
    size  : _GridSetting[int]   = dataclasses.field(default=_GridSetting('size'))

    @overload
    def __init__(self, *, label: str = ..., spacing: FloatV = ..., padding: Vec2 | FloatV = ..., weight: FloatV = ..., size: FloatV = ...) -> None: ...  # type: ignore
    def __init__(self, *, weight: Any = 1.0, size: Any = 0, **kwargs) -> None:
        """Args:
            * label: Used to update `self.label`. None is treated as ''.

            * spacing: Used to update `self.spacing`. A minimum 0 is used
            for non-NaN values. None is treated as NaN.

            * padding: Used to update `self.padding`. When the value is a
            sequence, the first two items of the sequence are used as the
            left/upper and right/lower (for columns and rows respectively)
            padding values, where inner None values are treated as NaN.
            Otherwise, the value is applied to all padding values while
            treating NaN and None as `(NaN, NaN)`.

            * weight: Used to update `self.weight`. A minimum of 0 is used
            for non-NaN values. None is treated as NaN.

            * size: Used to update `self.size`. A minimum of 0 is used for
            non-NaN values. None is treated as NaN.
        """
        # managed by the parenting `Grid` during a draw event
        self._state = cast(
            dict[Literal['pos' ,'size', 'spacing', 'padding'], Any],
            {
                'pos'    : 0,
                'size'   : 0,
                'spacing': 0,
                'padding': (0, 0),
            }
        )
        super().__init__(weight=weight, size=size, **kwargs)

    @overload
    def configure(self, *, label: str = ..., spacing: FloatV = ..., padding: Vec2 | FloatV = ..., weight: FloatV = ..., size: FloatV = ...) -> None: ... # type: ignore
    def configure(self, **kwargs) -> None:
        if 'weight' in kwargs:
            self._weight = max(0.0, _to_value(kwargs['weight'], 0.0))
        if 'size' in kwargs:
            self._size = max(0, int(_to_value(kwargs['size'], 0)))
        super().configure(**kwargs)

    def configuration(self) -> dict[Literal['label', 'spacing', 'padding', 'weight', 'size'], Any]: ...
    del configuration


@dataclasses.dataclass(init=False)
class Axis(_GridComponent, Iterable[Slot], Sized):
    """A collection of rows or columns.

    Attributes:
        * label (str): Informal name for the axis.

        * spacing (float): Used as a fallback value to offset the slot's
        position during a draw event. Is ignored for calculations when NaN.

        * padding (array[float, float]): Fallback values used during a draw
        event when a slot contained in the axis does not specify a padding
        value. Inner NaN values are ignored for calculations.

        * length (int): Evaluates to `len(self)`. Setting a value resizes
        the length of the axis; adding or removing slots as necessary.


    Instances are treated as immutable, unsigned pseudo-integrals
    for most operations; the value of which is a representation
    of the number of slots in the axis. However, in-place operations
    directly affect the number of slots contained.

    Axes objects behave similar to lists. Slots are identified by their
    positions (index) in the axis. Indexing the axis returns the `Slot`
    object for that row or column.

    When the axis' number of slots is changed, slots are always appended
    to, or are removed from, the end of the axis.

    Operations that update the number of slots in the axis are
    thread-safe.

    An axis object is unaware of its' role in the grid i.e. x
    (columns) vs y (rows). A higher-level object may indicate this
    through its' `.label` attribute.
    """
    __slots__ = ('_slots', '_lock')

    length: _GridSetting[int] = dataclasses.field(default=_GridSetting('length'))

    @overload
    def __init__(self, length: int = ..., *, label: str = ..., spacing: FloatV = ..., padding: Vec2 | FloatV = ...) -> None: ...  # type: ignore
    def __init__(self, length: int = 0, **kwargs) -> None:
        """Args:
            * length: Integer value used to update `self.length`.

            * label: Used to update `self.label`. None is treated as ''.

            * spacing: Used to update `self.spacing`. A minimum 0 is used
            for non-NaN values. None is treated as NaN.

            * padding: Used to update `self.padding`. When the value is a
            sequence, the first two items of the sequence are used as the
            left/upper and right/lower (for columns and rows respectively)
            padding values, where inner None values are treated as NaN.
            Otherwise, the value is applied to all padding values while
            treating NaN and None as `(NaN, NaN)`.
        """
        self._slots = cast(list[Slot], [])
        self._lock  = threading.Lock()
        super().__init__(length=length, **kwargs)

    @overload
    def configure(self, *, label: str = ..., spacing: FloatV = ..., padding: Vec2 | FloatV = ..., length: int = ...): ...  # type: ignore
    def configure(self, **kwargs):
        if 'length' in kwargs:
            self.resize(kwargs['length'])
        super().configure(**kwargs)

    def configuration(self) -> dict[Literal['label', 'spacing', 'padding', 'length'], Any]: ...
    del configuration

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

    def slot_weight(self) -> float:
        """Return the weight sum of all "sized" slots in the axis."""
        with self._lock:
            return sum(s._weight for s in self._slots if not s._size)

    def slot_size(self) -> int:
        """Return the size sum of all "fixed" slots in the axis."""
        with self._lock:
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


    # Sequence Behaviors/Methods

    def __getitem__(self, index: SupportsIndex) -> Slot:
        return self._slots[index]

    def __iter__(self) -> Iterator[Slot]:
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
                self._slots.extend(Slot() for _ in range(x))
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

        Awaits internal lock release.

        Args:
            * length: A positive number indicating the target length of
            the axis.


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

        Awaits internal lock release.

        Args:
            * index: Position of the new slot.
        """
        with self._lock:
            self._slots.insert(index, Slot())

    def remove(self, index: SupportsIndex = -1):
        """Delete the row/column at the specified index, or the last
        row/column if not specified.

        Awaits internal lock release.

        Args:
            * index: Target slot index.
        """
        with self._lock:
            self._slots.pop(index)


@dataclasses.dataclass(init=False)
class Grid(_GridComponent):
    """Layout manager for Dear PyGui, emulating a table-like structure.

    Attributes:
        * cols (Axis): Living representation of the grid's columns (x-axis).
        See the `Axis` class for more information.

        * rows (Axis): Living representation of the grid's rows (y-axis).
        See the `Axis` class for more information.

        * target (int | str): The integer identifier or string alias of the
        item used as the grid's positional reference. Additionally, it's
        visibility state is used to determine whether or not to display (draw)
        the grid. The size of the target item is also used as fallback values
        as necessary when `self.width` and/or `self.height` are not applicable.

        * label (str): An informal name for the grid.

        * spacing (array[float, float]): Values used to offset a slot's (columns
        and rows, respectively) position during a draw event when both
        `slot.spacing` and `axis.spacing` are not applicable (min. 0 per value).

        * padding (array[float, float, float, float]): Used as the left, upper,
        right, and lower padding values during a draw event when item-level
        padding override values were not provided and both `slot.spacing` and
        `axis.spacing` are not applicable. The first and third values are used
        for column padding, while the second and fourth values are used for rows
        (min. 0 per value).

        * width (int): The horizontal size of the grid. Can be used to extend
        the grid beyond the default view of the target item, allowing for items
        to be positioned in their parent's scroll area. If 0, the width of the
        target item is used instead (min. 0).

        * height (int): The vertical size of the grid. Can be used to extend
        the grid beyond the default view of the target item, allowing for items
        to be positioned in their parent's scroll area. If 0, the height of the
        target item is used instead (min. 0).

        * offsets (array[float, float, float, float]): Similar to padding, but
        targets the left, upper, right, and lower edges of the grid itself and
        not its' slots. Can be used to expand or shrink the size of the grid's
        content region (min. 0 per value).

        * rect_getter (_RectGetter): Called before attempting to draw the grid
        to fetch the target item's size, position, and visibility status. The
        default implementation is a light wrapper around
        `dearpygui.get_item_state`. It may also call
        `dearpygui.get_item_configuration` if one or more details cannot be
        accessed by reading the item's state.

        * overlay (bool): If True, a visual representation of the grid will be
        displayed over it.

        * show (bool): If True, the grid and its' content will be visible.


    The grid calculates the positions, sizes, and visibility states of
    itself and attached items during a draw event; triggered by calling the
    grid. The grid must be frequently drawn in order for it to operate as
    expected, performing best when registered as the resize callback for its'
    target item or the parenting root-level window. However, the grid can
    registered as any Dear PyGui callback or even called directly.

    The grid does not use or create items to assist with the layout. Any item
    generated by the grid is used for its' overlay, enabled when `self.overlay`
    is True. A class-level `mvViewportDrawlist` item is created when the first
    instance of `Grid` is created, while a `mvDrawLayer` item is created per
    `Grid` instance. When `self.overlay` is False, no additional items are
    created.

    When a draw event occurs, the "draw" step is skipped when the grid is
    not visible. Additionally, the grid, its content, and overlay are drawn
    and displayed only if the visibility value returned from `self.rect_getter`
    is True, regardless of the value of `self.show` and `self.overlay`.

    Items can be attached to the grid via the `.push` method. When sizing and
    positioning an item during a draw event, settings provided when attatching
    the item (padding, spacing, etc.) are used over slot, axis and grid settings.
    If setting(s) are unspecified (usually indicated by None or NaN), the grid
    falls back to using settings found on the slot, then axis, etc.

    There are situations where an item may be hidden when drawing
    the grid:
        * the item's cellspan is outside of the grid's current
        range
        * given the constraints of the slots in the target cellspan,
        the size of the item is calculated to be less than 1 pixel

    Any item attached to the grid that does not exist at the time
    of a draw event is silently dropped from the grid, and will not
    be managed further.

    For more information, see `Grid.__init__`, `Grid.__call__` and `Grid.push`.

    """
    __slots__ = (
        # internal
        '_lock',
        '_item_data',
        '_trashbin',
        '_drawlayer',
        # configuration
        'rows',
        'cols',
        '_width',
        '_height',
        '_offsets',
        '_target',
        '_rect_getter',
        '_overlay',
        '_show',
        # other
        '__weakref__',
    )

    target     : _GridSetting[Item]           = dataclasses.field(default=_GridSetting("target"))
    spacing    : _GridSetting['array[float]'] = dataclasses.field(default=_GridSetting("spacing"))  # float -> array[float]
    width      : _GridSetting[int]            = dataclasses.field(default=_GridSetting("width"))
    height     : _GridSetting[int]            = dataclasses.field(default=_GridSetting("height"))
    offsets    : _GridSetting['array[float]'] = dataclasses.field(default=_GridSetting("offsets"))
    rect_getter: _GridSetting[_RectGetter]    = dataclasses.field(default=_GridSetting("rect_getter"))
    overlay    : _GridSetting[bool]           = dataclasses.field(default=_GridSetting("overlay"))
    show       : _GridSetting[bool]           = dataclasses.field(default=_GridSetting("show"))

    __drawlist = '[mvViewportDrawlist] Grid'

    @overload
    def __init__(self, cols: int = ..., rows: int = ..., target: Item = ..., *, label: str | None = ..., padding: Vec4 | FloatV = ..., spacing: Vec2 | FloatV = ..., width: FloatV = ..., height: FloatV = ..., offsets: Vec4 | FloatV = ..., rect_getter: _RectGetter = ..., overlay: bool = ..., show: bool = ...) -> None: ...  # type: ignore
    def __init__(
        self,
        cols       : int  = 1,
        rows       : int  = 1,
        target     : Item = 0,
        *,
        width      : Any  = None,
        height     : Any  = None,
        offsets    : Any  = None,
        rect_getter: Any  = None,
        overlay    : bool = False,
        show       : bool = True,
        **kwargs,
    ) -> None:
        """Args:
            * cols: Integer value used to update `self.cols` via `self.cols.resize`.
            Sets the number of slots in the x-axis.

            * rows: Integer value used to update `self.rows` via `self.rows.resize`.
            Sets the number of slots in the y-axis.

            * target: Integer or string value used to update `self.target`. Non-
            optional in most cases.

            * label: Used to update `self.label`. None is treated as ''.

            * rect_getter: Used to update `self.rect_getter`. Should be None, or a
            callable accepting `self.target` as a positional argument and returns a
            5-tuple containing a related width, height, x-position, y-position, and
            visibility status. None is treated as the internal default value.

            * width: Used to update `self.width`. Sets a minimum value of 0.
            None is treated as 0.

            * height: Used to update `self.height`. Sets a minimum value of 0.
            None is treated as 0.

            * offsets: Used to update `self.offsets`. When the value is a
            sequence, the first four items are used as the grid's left, upper,
            right, and lower inner padding values, where inner None values are
            treated as 0. Otherwise, the value is applied to all padding values
            while treating NaN and None as `(0, 0, 0, 0)`.

            * padding: Used to update `self.padding`. When the value is a
            sequence, the first four items are used as the left, upper,
            right, and lower padding values for slots, where inner None values
            are treated as 0. Otherwise, the value is applied to all padding values
            while treating NaN and None as `(0, 0, 0, 0)`.

            * spacing: Used to update `self.spacing`. When the value is a
            sequence, the first two items are used as column and row spacing values,
            where inner None values are treated as 0. Otherwise, the value is applied
            to all spacing values while treating NaN and None as `(0, 0)`.

            * overlay: Used to update `self.overlay`. Evaluated as a boolean, True
            will cause the overlay to be displayed once a draw event has been
            triggered.

            * show: Used to update `self.show`. Evaluated as a boolean,
            False will hide the grid, its' overlay, and all attached items (and
            vice-versa).
        """
        _create_context()
        if not dearpygui.does_item_exist(self.__drawlist):
            type(self).__drawlist = dearpygui.add_viewport_drawlist()
        self._drawlayer = dearpygui.add_draw_layer(parent=self.__drawlist)
        self._item_data = cast(set[ItemData], set())
        self._trashbin  = set()
        self._lock      = threading.Lock() if not sys.gettrace() else threading.RLock()

        self.cols = Axis(0, label='x')
        self.rows = Axis(0, label='y')

        super().__init__(
            rows=rows,
            cols=cols,
            width=width,
            height=height,
            offsets=offsets,
            target=target,
            rect_getter=rect_getter,
            overlay=overlay,
            show=show,
            **kwargs,
        )

    def _clean_cache(self):
        # currently called before or after:
        #   * updating the grid's settings
        #   * updating `self._item_data`
        #   * drawing the grid
        self._item_data.difference_update(self._trashbin)
        self._trashbin.clear()

    @overload
    def configure(self, *, cols: int = ..., rows: int = ..., target: Item = ..., label: str | None = ..., padding: Vec4 | FloatV = ..., spacing: Vec2 | FloatV = ..., offsets: Vec4 | FloatV = ..., width: FloatV = ..., height: FloatV = ..., rect_getter: _RectGetter = ..., overlay: bool = ..., show: bool = ...): ...  # type: ignore
    def configure(self, **kwargs):
        """Update the grid's settings.

        Awaits internal lock release.
        """
        with self._lock:
            # slots
            if 'cols' in kwargs:
                cols = kwargs['cols']
                if not isinstance(cols, int):
                    raise TypeError(f'expected int for `cols` (got {type(cols)!r}).')
                self.cols.resize(kwargs['cols'])
            if 'rows' in kwargs:
                rows = kwargs['rows']
                if not isinstance(rows, int):
                    raise TypeError(f'expected int for `rows` (got {type(rows)!r}).')
                self.rows.resize(kwargs['rows'])

            if 'target' in kwargs or 'rect_getter' in kwargs:
                target      = kwargs.get('target', getattr(self, '_target', 0)) or 0
                rect_getter = kwargs.get('rect_getter', getattr(self, '_rect_getter', _get_item_rect)) or _get_item_rect
                if not target and rect_getter is _get_item_rect:
                    raise ValueError(f'`target` required when using the default rect-getter.')
                try:
                    _, _, _, _, _ = rect_getter(target)
                except ValueError:
                    raise TypeError(f'expected `rect_getter` to return a 5-tuple, got {type(rect_getter)!r}.')
                except TypeError:
                    if not callable(rect_getter):
                        raise TypeError(f'expected callable for `rect_getter`, got {type(rect_getter)!r}.') from None
                    raise
                except SystemError:
                    if target and dearpygui.does_item_exist(target):
                        raise

                self._target      = target
                self._rect_getter = rect_getter

            # sizing
            if 'width' in kwargs:
                self._width = int(max(0, _to_value(kwargs['width'], 0)))
            if 'height' in kwargs:
                self._height = int(max(0, _to_value(kwargs['height'], 0)))

            # offsets
            if 'offsets' in kwargs:
                self._offsets = _to_float_arr(kwargs['offsets'], 4, 0.0)
            if 'padding' in kwargs:
                self._padding = _to_float_arr(kwargs.pop('padding'), 4, 0.0)  # override
            if 'spacing' in kwargs:
                self._spacing = _to_float_arr(kwargs.pop('spacing'), 2, 0.0)  # override

            # visibility
            if 'overlay' in kwargs:
                overlay = bool(kwargs['overlay'])
                _item_set_config(self._drawlayer, show=overlay)
                self._overlay = overlay
            if 'show' in kwargs:
                show = bool(kwargs['show'])
                if not show:
                    _item_set_config(self._drawlayer, show=False)
                for item_data in self._item_data:
                    try:
                        _item_set_config(item_data.item, show=show)
                    except SystemError:
                        if not dearpygui.does_item_exist(item_data.item):
                            self._trashbin.add(item_data)
                        else:
                            raise
                self._show = show

            super().configure(**kwargs)
            self._clean_cache()

    def configuration(self):
        """Return the grid's various settings and values."""
        cfg = {'cols': len(self.cols), 'rows': len(self.rows)}
        cfg.update({f:getattr(self, f'_{f}') for f in self.__dataclass_fields__})
        return cfg

    def _pop(self, item: Item):
        # Two instances of `ItemData` can potentially exist for the same item
        # since refs can be integers or strings. Try to remove all of them just
        # in case.
        if not dearpygui.does_item_exist(item):
            self._trashbin.add(item)
        else:
            if isinstance(item, str):
                refs = (item, dearpygui.get_alias_id(item), dearpygui.get_item_alias(item))
            else:
                refs = (item, dearpygui.get_item_alias(item))
            self._trashbin.update(refs)
            _item_set_config(item, pos=())
        self._clean_cache()

    def pop(self, item: Item):
        """Release an item from the grid.

        Awaits internal lock release.
        """
        with self._lock:
            self._pop(item)

    def clear(self):
        """Release all items from the grid.

        Awaits internal lock release.
        """
        with self._lock:
            for item_data in self._item_data:
                try:
                    _item_set_config(item_data.item, pos=())
                except SystemError:
                    pass
            self._trashbin.update(self._item_data)
            self._clean_cache()

    ANCHORS = tuple(s.lower() for s in _ANCHOR_MAP)

    @overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_size: Vec2 | FloatV = ..., padding: Vec4 | FloatV = ...): ...
    @overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_width: int = ..., max_height: int = ..., padding: Vec4 | FloatV = ...): ...
    @overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_size: Vec2 | FloatV = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ...): ...
    @overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_width: int = ..., max_height: int = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ...): ...
    @overload
    def push(self, item: Item, cell_start: tuple[int, int] | Sequence[int], cell_stop: tuple[int, int] | Sequence[int] | None = ..., /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_size: Vec2 | FloatV = ..., padding: Vec4 | FloatV = ...): ...
    @overload
    def push(self, item: Item, cell_start: tuple[int, int] | Sequence[int], cell_stop: tuple[int, int] | Sequence[int] | None = ..., /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_width: int = ..., max_height: int = ..., padding: Vec4 | FloatV = ...): ...
    @overload
    def push(self, item: Item, cell_start: tuple[int, int] | Sequence[int], cell_stop: tuple[int, int] | Sequence[int] | None = ..., /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_size: Vec2 | FloatV = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ...): ...
    @overload
    def push(self, item: Item, cell_start: tuple[int, int] | Sequence[int], cell_stop: tuple[int, int] | Sequence[int] | None = ..., /, *, anchor: str = ..., rect_setter: _RectSetter = ..., max_width: int = ..., max_height: int = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ...): ...
    def push(self, item: Item, cell_start: Any, cell_stop: Any = None, /, *, anchor: str = 'c', rect_setter: _RectSetter = _set_item_rect, max_size: Any = None, max_width: Any = None, max_height: Any = None, padding: Any = None, x1_pad: Any = None, y1_pad: Any = None, x2_pad: Any = None, y2_pad: Any = None):
        """Attach an item to the grid.

        Awaits internal lock release.

        Args:
            * item: Integer uuid or string alias of an item.

            * col, cell_start: Index of the cell's column that will contain the
            item, OR a 2-item sequence containing both the column and row indices
            of the initial cell of the cell range the item will occupy.

            * row, cell_stop: Index of the cell's row that will contain the item,
            OR a 2-item sequence containing both the column and row indices of the
            last cell of the cell range the item will occupy.

            * anchor: A (inter)cardinal direction name (e.g. "north", "southwest")
            or abbreviation (e.g. "n", "sw") indicating the area of the cell the
            item will "stick" to. "center", "centered", or "c" will result in the
            item being centered in the specified cell or cellspan (default). Value
            is case-insensitive.

            * rect_setter: A callable accepting *item*, x-position, y-position,
            width, height, and visible state as positional arguments that updates
            the item's size, position, and visibility. By default, it is a
            simple wrapper around `dearpygui.configure_item`.

            * max_size: The maximum width and height the item will scale to. Inner
            NaN-like values are not applied.

            * max_width: Individual width component (first value) of *max_size*.
            Ignored when *max_size* is specified.

            * max_height: Individual height component (second value) of *max_size*.
            Ignored when *max_size* is specified.

            * padding: A 4-item sequence whose values will be used to override the
            left, upper, right, and/or lower-padding values of the first/last slots
            in the target cell range, OR, a non-sequence value that will be used
            as the override value for all padding components. Inner NaN-like values
            are not applied as an overriding value.

            * x1_pad: Overrides the first `.padding` value of the first column
            (left-padding) in the target cell range. Ignored when *padding* is
            specified.

            * y1_pad: Overrides the first `.padding` value of the first row
            (upper-padding) in the target cell range. Ignored when *padding* is
            specified.

            * x2_pad: Overrides the first `.padding` value of the last column
            (right-padding) in the target cell range. Ignored when *padding* is
            specified.

            * y2_pad: Overrides the first `.padding` value of the last row
            (lower-padding) in the target cell range. Ignored when *padding* is
            specified.


        An item attached to the grid must support sizing via `width` and `height`
        configurations, positioning via `pos`, and visibility updates via `show`.
        Otherwise, consider attaching a compatible parenting, container item
        instead. Alternatively, a custom *rect_setter* can be passed to enforce
        item compatibility.

        When it is desired for the item to occupy a single cell, the second and
        third positional arguments are the target cell's column and row indices,
        respectively. Alternatively, a 2-item sequence can be passed as the
        second positional argument containing both indices while leaving the
        third positional argument unspecified. To push an item onto a range of
        cells, the second and third positional arguments must both be 2-item
        sequences containing indices of the endpoint cells in the range. During
        a draw event, the cell whose indices are nearest to `(0, 0)` is
        considered the "starting" cell in the range for that event.

        Column/row indices can be positive or negative integers. The "indexing"
        behavior mirrors typical Python subscript behavior; cell coordinates
        `(-1, 0)` would specify the cell at the last column and first row.

        The exact cell(s) used are evaluated during draw events; deterministic
        of the grid's state at the time of the event and *not* when the item is
        attached. A side effect of this is that column and row indices can be
        outside the grid's range when items are attached. If the target cell or
        cellspan is out-of-range during a draw event, the item is simply hidden.
        Additionally, passing a row index of 4 is not the same as -1 even if the
        grid only has 5 rows at the time of attachment since the exact row is
        not determined until a draw event occurs.

        During a draw event, *rect_setter* is called to update the item using
        the finalized size, position, and visibility values. This means that items
        attached to the grid must support sizing via `width` and `height`
        configurations, positioning via `pos`, and visibility updates via `show`.
        If an item does not support one of more of the mentioned configuration
        options, consider parenting it within a more compatible item and attaching
        that item instead. Otherwise, a custom *rect_setter* can be used force
        compatibility of otherwise incompatible items by choosing which settings
        are updated in their call to `dearpygui.configure_item` or, alternatively,
        update a different item entirely.

        An item's size is usually dependant on the size of the row(s) and column(s)
        they occupy. *max_size* (OR individual *max_width/height*) values can be
        passed to clamp the item's size as the cell or cellspan expands. Setting a
        minimum size per item is not supported, since having the content of a
        cell(span) extend beyond its' borders is not typical of a grid system.
        When desired, it is recommended to set the `size` attribute of the entire
        row or column. This sets a "fixed" sizing policy on the slot, preventing it
        from being dynamically sized. If an item *must* have a unique minimum size,
        a custom *rect_setter* can be set that sends other width/height values to
        `dearpygui.configure_item`.

        > NOTE: A grid object that calls *rect_setter* will be holding its' internal
        mutex. Under normal operation, a *rect_setter* that calls a grid's methods or
        invokes behavior documented to "await internal lock release" will result in
        a deadlock.
        """
        if hasattr(cell_start, '__iter__'):  # possible cell range
            try:
                x1, y1 = cell_start
            except ValueError:
                raise ValueError(
                    f'expected a 2-item sequence of cell coordinates for `cell_start`, got {len(cell_start)!r}.'
                ) from None

            try:
                x2, y2 = cell_stop
            except TypeError:
                if cell_stop is None:  # single cell
                    x2 = x1
                    y2 = y1
                else:
                    raise ValueError(
                        f'expected a 2-item sequence of cell coordinates for `cell_stop`, got {cell_stop!r}.'
                    ) from None
        else:  # single cell
            x1 = x2 = cell_start

            try:
                y1 = y2 = int(cell_stop)
            except TypeError:
                if cell_stop is not None:
                    raise TypeError(
                        f'expected int for `row`, got {type(cell_stop)!r}.'
                    ) from None
                raise TypeError(
                    f"expected 3 positional arguments for '{self.push.__qualname__}()' got 2."
                ) from None
        cellspan = int(x1), int(y1), int(x2), int(y2),

        if max_size is _is_nanlike(max_size):
            max_size = (max_width, max_height)
        max_size = _to_float_arr(max_size, 2, 0.0)
        for i in range(len(max_size)):
            max_size[i] = max(0.0, max_size[i])

        if padding is _is_nanlike(padding):
            padding = (x1_pad, y1_pad, x2_pad, y2_pad)
        padding = _to_float_arr(padding, 4, NaN)

        with self._lock:
            self._pop(item)

            # unique handling per item type
            is_text = False
            try:
                item_type = dearpygui.get_item_info(item)['type']
            except SystemError:
                # XXX: The item may not exist yet. It is very rare that this is
                # purposeful, but it happens? Allowing this can create gachas.
                pass
            else:
                if item_type == 'mvAppItemType::mvText':
                    is_text = True
                    if rect_setter == _set_item_rect:
                        rect_setter = _set_text_rect
                elif item_type == 'mvAppItemType::mvTable':
                    # BUG: Table items accept a `pos` keyword, but DPG doesn't
                    # do anything with it.
                    raise ValueError("`mvTable` items cannot be explicitly positioned.")

            item_data = ItemData(
                item=item,
                cellspan=cellspan,
                max_size=max_size,
                padding=padding,
                positioner=_get_positioner(anchor),
                rect_setter=rect_setter,
                is_text=is_text,
            )
            self._item_data.add(item_data)
            return item_data

    def _upd_slot_states(self, axis: Axis, area_size: float, index_offset: Literal[0, 1]):  # XXX: performance-sensitive
        area_c1_pad  = self._offsets[0 + index_offset]
        area_c2_pad  = self._offsets[2 + index_offset]
        content_size = area_size - area_c1_pad - area_c2_pad

        _slot_c1_pad, _slot_c2_pad = axis._padding
        if _slot_c1_pad != _slot_c1_pad:  # is NaN?
            _slot_c1_pad = self._padding[0 + index_offset]
        if _slot_c2_pad != _slot_c2_pad:  # is NaN?
            _slot_c2_pad = self._padding[2 + index_offset]

        _slot_size_offset = axis._spacing
        if _slot_size_offset != _slot_size_offset:  # is NaN?
            _slot_size_offset = self._spacing[0 + index_offset]

        slot_pos_offset = _slot_size_offset / 2.0

        slot_weight_size = (
            max(0, (content_size - axis.slot_size())) / max(1, axis.slot_weight())
        )

        alloc_size = 0.0
        for slot in axis:
            slot_state = slot._state

            slot_size_offset = slot._spacing
            if slot_size_offset != slot_size_offset:  # is NaN?
                slot_size_offset = _slot_size_offset
            slot_state['spacing'] = slot_size_offset

            slot_state['pos'] = alloc_size + area_c1_pad + slot_pos_offset

            slot_c1_pad, slot_c2_pad = slot._padding
            if slot_c1_pad != slot_c1_pad:  # is NaN?
                slot_c1_pad = _slot_c1_pad
            if slot_c2_pad != slot_c2_pad:  # is NaN?
                slot_c2_pad = _slot_c2_pad
            slot_state['padding'] = slot_c1_pad, slot_c2_pad

            slot_size = slot._size or slot_weight_size * slot._weight  # FIXED or SIZED
            slot_state['size'] = slot_size - _slot_size_offset
            alloc_size += slot_size

    def _upd_item_states(self):  # XXX: performance-sensitive
        rows = self.rows._slots
        cols = self.cols._slots

        n_cols = len(cols)
        n_rows = len(rows)

        for item_data in self._item_data:
            x1, y1, x2, y2 = item_data.cellspan
            # convert negative indexes
            x1 %= n_cols
            y1 %= n_rows
            x2 %= n_cols
            y2 %= n_rows
            # fix inversed cellspan
            if y1 > y2:
                y1, y2 = y2, y1
            if x1 > x2:
                x1, x2 = x2, x1

            try:
                col1_state = cols[x1]._state
                row1_state = rows[y1]._state
                col2_state = cols[x2]._state
                row2_state = rows[y2]._state
            except KeyError:  # hide the item - cellspan is out-of-range
                item_x_pos  = 0
                item_y_pos  = 0
                item_width  = 0
                item_height = 0
                item_show   = False
            else:
                x1_pad, y1_pad, x2_pad, y2_pad = item_data.padding

                if x1_pad != x1_pad:  # is NaN?
                    x1_pad = col1_state['padding'][0]
                cell_x_pos = col1_state['pos'] + x1_pad

                if y1_pad != y1_pad:  # is NaN?
                    y1_pad = row1_state['padding'][0]
                cell_y_pos  = row1_state['pos'] + y1_pad

                if x2_pad != x2_pad:  # is NaN?
                    x2_pad = col2_state['padding'][1]
                cell_width = col2_state['pos'] + col2_state['size'] - cell_x_pos - x2_pad

                if y2_pad != y2_pad:  # is NaN?
                    y2_pad = row1_state['padding'][1]
                cell_height = row2_state['pos'] + row2_state['size'] - cell_y_pos - y2_pad

                # XXX: It's really common for users to want to align text items.
                # Unfortunately, they must be handled differently since their size
                # is determined by their value and font used.
                if item_data.is_text:
                    try:
                        item_width, item_height = _item_get_state(item_data.item)['rect_size']
                        # if item_width > cell_width or item_height > cell_height:
                        #     item_width = item_height = 0
                    except SystemError:  # does not exist - dealt with below
                        item_width = item_height = 0
                else:
                    item_width, item_height = item_data.max_size
                    if not item_width or item_width > cell_width:
                        item_width = cell_width
                    if not item_height or item_height > cell_height:
                        item_height = cell_height

                if item_width < 1 or item_height < 1:  # hide the item - size too small
                    item_x_pos = 0
                    item_y_pos = 0
                    item_show  = False
                else:
                    item_x_pos, item_y_pos = item_data.positioner(
                        item_width,
                        item_height,
                        cell_x_pos,
                        cell_y_pos,
                        cell_width,
                        cell_height,
                    )
                    item_show = True

            try:
                item_data.rect_setter(
                    item_data.item,
                    int(item_x_pos),
                    int(item_y_pos),
                    int(item_width),
                    int(item_height),
                    item_show,
                )
            except SystemError:
                if not dearpygui.does_item_exist(item_data.item):
                    self._trashbin.add(item_data.item)
                else:
                    raise

    def _draw_outline(self, x_min: int, y_min: int, x_max: int, y_max: int, line_color: Sequence[int], pad_color: Sequence[int]):
        layer = self._drawlayer
        x1_pad, y1_pad, x2_pad, y2_pad = self._offsets

        # padding
        if x1_pad:
            dearpygui.draw_rectangle(
                (x_min, y_max),
                (x_min + x1_pad, y_min + y1_pad),
                color=(0, 0, 0, 0),
                fill=pad_color,  # type: ignore
                parent=layer,
            )
        if y1_pad:
            dearpygui.draw_rectangle(
                (x_min, y_min),
                (x_max - x2_pad, y_min + y1_pad),
                color=(0, 0, 0, 0),
                fill=pad_color,  # type: ignore
                parent=layer,
            )
        if x2_pad:
            dearpygui.draw_rectangle(
                (x_max, y_min),
                (x_max - x2_pad, y_max - y2_pad),
                color=(0, 0, 0, 0),
                fill=pad_color,  # type: ignore
                parent=layer,
            )
        if y2_pad:
            dearpygui.draw_rectangle(
                (x_max, y_max),
                (x_min + x1_pad, y_max - y2_pad),
                color=(0, 0, 0, 0),
                fill=pad_color,  # type: ignore
                parent=layer,
            )

        # outline
        dearpygui.draw_rectangle(
            (x_min, y_min), (x_max, y_max),
            fill=(0, 0, 0, 0),
            color=line_color,  # type: ignore
            parent=layer,
        )

    def _draw_slots(self, x_min: int, y_min: int, x_max: int, y_max: int, line_color: Sequence[int], space_color: Sequence[int], pad_color: Sequence[int], ):
        layer = self._drawlayer
        x1_pad, y1_pad, x2_pad, y2_pad = self._offsets
        x_space = self.cols._spacing / 2
        y_space = self.rows._spacing / 2
        cont_x_min = x_min + x1_pad
        cont_y_min = y_min + y1_pad
        cont_x_max = x_max - x2_pad
        cont_y_max = y_max - y2_pad

        for col in self.cols:
            col_state = col._state
            cell_x_min  = x_min + col_state['pos']
            cell_x_max  = cell_x_min + col_state['size']
            cell_x1_pad, cell_x2_pad = col_state['padding']

            for row in self.rows:
                row_state = row._state
                cell_y_min  = y_min + row_state['pos']
                cell_y_max  = cell_y_min + row_state['size']
                cell_y1_pad, cell_y2_pad = row_state['padding']

                if cell_x1_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_min              , cell_y_max              ),
                        (cell_x_min + cell_x1_pad, cell_y_min + cell_y1_pad),
                        color=(0, 0, 0, 0),
                        fill=pad_color,  # type: ignore
                        parent=layer,
                    )
                if cell_y1_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_min              , cell_y_min              ),
                        (cell_x_max - cell_x2_pad, cell_y_min + cell_y1_pad),
                        color=(0, 0, 0, 0),
                        fill=pad_color,  # type: ignore
                        parent=layer,
                    )
                if cell_x2_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_max              , cell_y_min              ),
                        (cell_x_max - cell_x2_pad, cell_y_max - cell_y2_pad),
                        color=(0, 0, 0, 0),
                        fill=pad_color,  # type: ignore
                        parent=layer,
                    )
                if cell_y2_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_max              , cell_y_max              ),
                        (cell_x_min + cell_x1_pad, cell_y_max - cell_y2_pad),
                        color=(0, 0, 0, 0),
                        fill=pad_color,  # type: ignore
                        parent=layer,
                    )

                dearpygui.draw_rectangle(
                    (cont_x_min, cell_y_min          ),
                    (cont_x_max, cell_y_min - y_space),
                    color=(0, 0, 0, 0),
                    fill=space_color,  # type: ignore
                    parent=layer,
                )
                dearpygui.draw_rectangle(
                    (cont_x_min, cell_y_max          ),
                    (cont_x_max, cell_y_max + y_space),
                    color=(0, 0, 0, 0),
                    fill=space_color,  # type: ignore
                    parent=layer,
                )
                # lines
                dearpygui.draw_line(
                    (cont_x_min, cell_y_min),
                    (cont_x_max, cell_y_min),
                    color=line_color,  # type: ignore
                    parent=layer,
                )
                dearpygui.draw_line(
                    (cont_x_min, cell_y_max),
                    (cont_x_max, cell_y_max),
                    color=line_color,  # type: ignore
                    parent=layer,
                )

            # outer spacing
            dearpygui.draw_rectangle(
                (cell_x_min          , cont_y_min),
                (cell_x_min - x_space, cont_y_max),
                color=(0, 0, 0, 0),
                fill=space_color,  # type: ignore
                parent=layer,
            )
            dearpygui.draw_rectangle(
                (cell_x_max          , cont_y_min),
                (cell_x_max + x_space, cont_y_max),
                color=(0, 0, 0, 0),
                fill=space_color,  # type: ignore
                parent=layer,
            )
            # lines
            dearpygui.draw_line(
                (cell_x_min, cont_y_min),
                (cell_x_min, cont_y_max),
                color=line_color,  # type: ignore
                parent=layer,
            )
            dearpygui.draw_line(
                (cell_x_max, cont_y_min),
                (cell_x_max, cont_y_max),
                color=line_color,  # type: ignore
                parent=layer,
            )

    @property
    def __code__(self):
        """[get] Return `self.__call__.__code__`.

        Enables `Grid` objects to registered as Dear PyGui callbacks.
        """
        return self.__call__.__code__

    def __call__(self, *args):
        """Draw the grid, updating the size and position of any item
        attached.

        Awaits internal lock release.


        > NOTE: When overriding, redefining, or reassigning this method,
        the new method must accept variadic positional arguments for
        `Grid` objects to be callable by Dear PyGui.
        """
        with self._lock:
            self._clean_cache()

            _area_width, _area_height, area_x_pos, area_y_pos, area_visible = self._rect_getter(
                self._target
            )

            if self._show and area_visible:
                area_width = self._width or _area_width
                self._upd_slot_states(self.cols, area_width, 0)
                area_height = self._height or _area_height
                self._upd_slot_states(self.rows, area_height, 1)

                self._upd_item_states()

                if self._overlay:
                    dearpygui.delete_item(self._drawlayer, children_only=True)
                    _item_set_config(self._drawlayer, show=True)

                    area_x_max = area_x_pos + area_width
                    area_y_max = area_y_pos + area_height
                    self._draw_outline(
                        area_x_pos,
                        area_y_pos,
                        area_x_max,
                        area_y_max,
                        (150, 255, 255),
                        (150, 255, 255, 80),
                    )
                    self._draw_slots(
                        area_x_pos,
                        area_y_pos,
                        area_x_max,
                        area_y_max,
                        (150, 255, 255, 120),
                        (150, 255, 255, 255),
                        (150, 255, 255, 80),
                    )
            else:
                _item_set_config(self._drawlayer, show=False)




if __name__ == '__main__':
    dpg = dearpygui


    dpg.create_context()
    dpg.setup_dearpygui()
    dpg.create_viewport()
    dpg.show_viewport()

    main_window = dpg.add_window()
    dpg.set_primary_window(main_window, True)
    dpg.configure_item(main_window, no_scroll_with_mouse=True, no_scrollbar=True)


    grid = Grid(2, 4, main_window, overlay=True)

    with dpg.item_handler_registry() as window_hr:
        dpg.add_item_resize_handler(callback=grid)
    dpg.bind_item_handler_registry(main_window, window_hr)




    grid.rows[0].size = 28
    with dpg.child_window(border=True, parent=main_window) as menu_bar:
        ...
    grid.push(menu_bar, (0, 0), (-1, 0))


    grid.rows[1].size = 100
    with dpg.child_window(border=True, parent=main_window) as ribbon:
        ...
    grid.push(ribbon, (0, 1), (-1, 1))


    grid.cols[0].size = 300
    with dpg.window(no_title_bar=True, no_collapse=True, no_move=True) as left_view:
        for i in range(10):
            dpg.add_button(label=f"button {i}",width=-1, height=80)

        def cb_left_view_resize(sender, app_data, user_data):
            grid.cols[0].size = dpg.get_item_width(user_data)
            grid()

        with dpg.item_handler_registry() as left_view_hr:
            dpg.add_item_resize_handler(callback=cb_left_view_resize, user_data=left_view)
        dpg.bind_item_handler_registry(left_view, left_view_hr)
    grid.push(left_view, 0, 2)


    with dpg.child_window(border=True, parent=main_window, horizontal_scrollbar=True) as right_view:
        rv_grid = Grid(10, 4, right_view, width=2000, offsets=(2, 12, 2, 12), padding=(8, 8, 8, 8), overlay=True)
        dpg.add_item_resize_handler(callback=rv_grid, parent=window_hr)
        dpg.add_item_resize_handler(callback=rv_grid, parent=left_view_hr)

        rv_grid.push(dpg.add_button(label=f"content"), (0, 0), (2, 0))
        rv_grid.push(dpg.add_button(label=f"content"), (1, 1), (3, 1))
        rv_grid.push(dpg.add_button(label=f"content"), (2, 2), (4, 2))
        rv_grid.push(dpg.add_button(label=f"content"), (3, 3), (5, 3))
        rv_grid.push(dpg.add_button(label=f"content"), (4, 0), (6, 0))
        rv_grid.push(dpg.add_button(label=f"content"), (5, 1), (7, 1))
        rv_grid.push(dpg.add_button(label=f"content"), (6, 2), (8, 2))
        rv_grid.push(dpg.add_button(label=f"content"), (7, 3), (9, 3))
    grid.push(right_view, (1, 2), (1, 2))


    grid.rows[-1].size = 24
    with dpg.child_window(border=True, parent=main_window) as footer:
        t = dpg.add_text("hello_world")
    grid.push(footer, (0, -1), (-1, -1))


    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        grid()
