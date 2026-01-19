import typing
import threading
import dataclasses
from array import array

from dearpygui import dearpygui, _dearpygui
from dearpygui._dearpygui import (
    get_item_configuration as _item_get_config,
    get_item_state as _item_get_state,
    configure_item as _item_set_config,
)

from dearpypixl.core.protocols import Item, property
from dearpypixl.core import codegen



NaN = float("nan")

_MISSING = object()


class _Array[L: int, T](typing.Protocol):
    def __len__(self, /) -> L: ...
    def __iter__(self, /) -> typing.Iterator[T]: ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex, /) -> T: ...
    @typing.overload
    def __getitem__[C: _ArrayLike](self: C, slice: slice, /) -> C: ...
    @typing.overload
    def __setitem__(self, index: typing.SupportsIndex, value: T, /) -> None: ...
    @typing.overload
    def __setitem__(self, slice: slice, value: _ArrayLike[L, T], /) -> None: ...

type _ArrayLike[L: int, T] = typing.Annotated[typing.Sequence[T], L]

type _2 = typing.Literal[2]
type _4 = typing.Literal[4]

type _True = typing.Literal[True]
type _False = typing.Literal[False]




# [ HELPER FUNCTIONS ]

def _create_context():
    global _create_context
    # runs once, then no-op
    dearpygui.create_context()
    def _create_context():
        pass

def _is_nan(v: typing.Any) -> bool:
    return v != v

def _is_nanlike(v: typing.Any) -> bool:
    return v is None or v != v

def _to_value(value: typing.Any, default: typing.Any):
    if value is None or _is_nan(value):
        return default
    return value

def _to_float_arr(value: _ArrayLike[_2, float] | float | None, length: int, default: float = NaN) -> typing.Any:
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

    # typing.Sequence[float | nan | None], len(value) >= 4
    >>> arr = _to_float_array([20, None, float("nan"), 10, 0, 0], 4, -5.0)  # 6-len input
    >>> tuple(arr) == (20, -5.0, -5.0, 10)
    True

    # typing.Sequence[float | float('nan') | None], len(value) < 4
    >>> arr = _to_float_array([20, None], 4, -5.0)
    >>> tuple(arr) == (20, -5.0, -5.0, -5.0)
    True

    """
    if value is None or _is_nan(value):
        return array('f', (default,) * length)  # type: ignore
    if isinstance(value, (float, int)):
        return array('f', (value,) * length)  # type: ignore

    arr = array('f', (default,) * length)
    try:
        for i in range(length):
            arr[i] = _to_value(value[i], default)
    except IndexError:
        pass
    return arr  # type: ignore

def _float_arr_property(length: int, default: float | None = None) -> typing.Any:
    def _create_property(name):
        return codegen.create_property(
            (
                f"try:",
                f"  return self._{name}",
                f"except AttributeError:",
                f"  {name} = self._{name} = _to_float_arr(None, {length}, {default})",
                f"  return {name}",
            ),
            (
                f"{name} = self.{name}",
                f"if _is_nan(value) or value is None:",
                f"  {' = '.join(f'{name}[{i}]' for i in range(length))} = {default}",
                f"else:",
                f"  {name}[:] = _to_float_arr(value, {length}, {default})",
            ),
            (
                f"{' = '.join(f'{name}[{i}]' for i in range(length))} = {default}",
            ),
            module=__name__,
            globals=globals(),
        )

    if default is None:
        default = "NaN"  # type: ignore

    return codegen.DescriptorDelegate(_create_property)

def _min_number_property(floor: int | float = 0.0, default = None) -> typing.Any:
    def _create_property(name):
        return codegen.create_property(
            (
                f"return self._{name}",
            ),
            (
                f"if _is_nan(value) or value is None:",
                f"  self._{name} = {default}",
                f"else:",
                f"  self._{name} = max({floor}, type_(value))",
            ),
            (
                f"self._{name} = {default}",
            ),
            module=__name__,
            globals=globals(),
            locals={"type_": type_}
        )

    type_ = type(floor)

    if default is None:
        if issubclass(type_, float):
            default = "NaN"
        else:
            default = 0

    return codegen.DescriptorDelegate(_create_property)



# [ minor components ]

class _RectGetter(typing.Protocol):
    """A function that returns an item's size, position, and visibility
    state as a 5-tuple `(width, height, x_pos, y_pos, is_visible)`.
    """
    def __call__(self, item: Item, /) -> tuple[int, int, int, int, bool]: ...

def _default_rect_getter(item: Item, /, *, _config_getter=_dearpygui.get_item_configuration, _state_getter=_dearpygui.get_item_state) -> tuple[int, int, int, int, bool]:
    state = _state_getter(item)

    visible = state.get("visible")
    if visible is None:
        visible = _config_getter(item)["show"]

    return *state['rect_size'], *state['pos'], visible


class _RectSetter(typing.Protocol):
    """A function that updates an item's size and position via
    `dearpygui.configure_item`.
    """
    def __call__(self, item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool, /) -> typing.Any: ...

def _default_rect_setter(item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool, /, *, _config_setter=_dearpygui.configure_item):
    _config_setter(item, width=width, height=height, pos=(x_pos, y_pos), show=show)

def _set_text_rect(item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool):
    _item_set_config(
        item,
        pos=(int(x_pos), int(y_pos)),
        show=show,
    )




@dataclasses.dataclass(slots=True)
class ItemData:
    """Contains the size and placement information of an item attached
    to a `Grid` object.

    :vartype item: `int | str`
    :var item: The target item's integer uuid or string alias.

    :vartype cellspan: `tuple[int, int, int, int]`
    :var cellspan: Contains coordinates for
        the target cell range, as `(col_start, row_start, col_end, row_end)`.

    :vartype max_size: `tuple[int, int]`
    :var max_size: Indicates the item's maximum width
        and height (min 0 per value).

    :vartype padding: `tuple[float, float, float, float]`
    :var padding: Top-level padding
        override values.

    :vartype positioner: `_Positioner`
    :var positioner: Function used to calculate the item's
        final position.

    :vartype rect_setter: `_RectSetter`
    :var rect_setter: typing.Callable used to update the item's size,
        position, and visibility status.

    :vartype is_text: `bool`
    :var is_text: If True, the target item an `mvText` object.
    """
    item       : Item
    cellspan   : tuple[int, int, int, int]
    max_size   : typing.Sequence[float]
    padding    : typing.Sequence[float]
    pos_coef   : tuple[float, float]
    rect_setter: _RectSetter
    is_text    : bool

    _out_of_bounds: bool = dataclasses.field(default=False, init=False, repr=False)

    def __hash__(self) -> int:
        return hash(self.item)

    def __eq__(self, other, /) -> bool:
        try:
            h = hash(other)
        except:
            return False
        return self.__hash__() == h




# [ major components ]

@dataclasses.dataclass(init=False)
class _GridComponent:
    __slots__ = ('label', '_spacing', '_padding')

    label: str
    spacing: property[float, None, _True] = _min_number_property(0.0)
    padding: property[_Array[_2, float], _ArrayLike[typing.Any, float] | float | None, _True] = _float_arr_property(2)

    def __init__(self, *, label: str = '', spacing: float = NaN, padding: typing.Sequence[float] | float | None = None, **kwargs):
        self.configure(label=label, spacing=spacing, padding=padding, **kwargs)

    def configure(self, **kwargs) -> None:
        """Update the object's high-level settings.

        Accepts all arguments accepted by the object's constructor
        as keyword arguments.
        """
        fields = self.__dataclass_fields__
        for k, v in kwargs.items():
            if k in fields:
                self.__setattr__(k, v)

    def configuration(self) -> dict[str, typing.Any]:
        """Return a mapping of the object's settings and their current values."""
        return {f:getattr(self, f) for f in self.__dataclass_fields__}


@dataclasses.dataclass(slots=True)
class _GridSlotState:
    pos    : float = 0
    size   : float = 0
    spacing: float = 0
    padding: tuple[float, float] = (0, 0)

@dataclasses.dataclass(init=False)
class Slot(_GridComponent):
    """A grid row or column.

    :vartype label: ``
    :var label: Informal name for the slot.

    :vartype spacing: `float`
    :var spacing: Used to offset the slot's position during a draw
        event. Is ignored for calculations when NaN.

    :vartype padding: `array[float, float]`
    :var padding: Used as the left/upper and right/lower padding values
        (columns and rows respectively) for cells in the slot during a
        draw event. Inner NaN values are ignored for calculations.

    :vartype weight: `float`
    :var weight: During a draw event and when the slot's policy is
        evaluated as "sized", this affects how much the slot is scaled
        in proportion to the size of the grid and the total weight of all
        other slots in the axis.

    :vartype size: `int`
    :var size: The width/height (for columns and rows respectively) of
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

    weight: property[float, float | None, _True] = _min_number_property(0.1, 1.0)
    size: property[int, int | None, _True] = _min_number_property(0, 0)

    @typing.overload
    def __init__(self, *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., weight: float | None = ..., size: int | None = ...) -> None: ...  # type: ignore
    def __init__(self, *, weight: typing.Any = 1.0, size: typing.Any = 0, **kwargs) -> None:
        self._state = _GridSlotState()  # managed by the parenting `Grid` during a draw event
        super().__init__(weight=weight, size=size, **kwargs)

    def configure(self, *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., weight: FloatV = ..., size: FloatV = ...) -> None: ... # type: ignore
    del locals()["configure"]

    def configuration(self) -> dict[typing.Literal['label', 'spacing', 'padding', 'weight', 'size'], typing.Any]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    del locals()["configuration"]


@dataclasses.dataclass(init=False)
class Axis(_GridComponent, typing.Iterable[Slot], typing.Sized):
    """A collection of rows or columns.

    :vartype label: `str`
    :var label: Informal name for the axis.

    :vartype spacing: `float`
    :var spacing: Used as a fallback value to offset the slot's
        position during a draw event. Is ignored for calculations when NaN.

    :vartype padding: `array[float, float]`
    :var padding: Fallback values used during a draw
        event when a slot contained in the axis does not specify a padding
        value. Inner NaN values are ignored for calculations.

    :vartype length: `int`
    :var length: Evaluates to `len(self)`. Setting a value resizes
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

    @property
    def length(self, /) -> int:  # pyright: ignore[reportRedeclaration]
        return self.__len__()
    @length.setter
    def length(self, value: int, /) -> None:  # pyright: ignore[reportRedeclaration]
        self.resize(value)

    length: property[int, int] = length  # type: ignore

    @typing.overload
    def __init__(self, length: int = ..., *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., **kwargs) -> None: ...  # type: ignore
    def __init__(self, length: int = 0, *, _lock=None, **kwargs) -> None:
        self._slots = list[Slot]()
        self._lock  = _lock or threading.Lock()
        super().__init__(length=length, **kwargs)

    def configure(self, *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., length: int = ..., **kwargs): ...  # type: ignore
    del locals()["configure"]

    def configuration(self) -> dict[typing.Literal['label', 'spacing', 'padding', 'length'], typing.Any]: ... # pyright: ignore[reportIncompatibleMethodOverride]
    del locals()["configuration"]

    @property
    def weight(self, /) -> float:
        """[get] the total weight of all "sized" slots in the axis."""
        with self._lock:
            return sum(s._weight for s in self._slots if not s._size)

    @property
    def size(self, /) -> int:
        """[get] the total size of all "fixed" slots in the axis."""
        with self._lock:
            return sum(s._size for s in self._slots)

    def _get_sizeweight_tuple(self, /, *, sum=sum) -> tuple[int, float]:
        # used by `Grid`
        slots = self._slots
        return sum(s._size for s in slots), sum(s._weight for s in slots if not s._size)

    def __str__(self, /) -> str:
        return str(self._slots)

    def __bool__(self, /) -> bool:
        return bool(self._slots)

    def __getitem__(self, index: typing.SupportsIndex, /) -> Slot:
        return self._slots[index]

    def __iter__(self, /) -> typing.Iterator[Slot]:
        yield from self._slots

    def __len__(self, _: typing.Any = None, /, *, _len=len) -> int:
        return _len(self._slots)

    __int__ = __index__ = __round__ = __trunc__ = __floor__ = __ceil__ = __abs__ = __len__

    def __iadd__(self, x: int, /) -> typing.Self:
        """Adds an additional *x* slots to the end of the axis.

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

    def __isub__(self, x: int, /) -> typing.Self:
        """Removes the last *x* slots from the end of the axis.
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

    def resize(self, length: int, /):
        """Add/remove slots from the axis so that it contains the number
        of slots specified.

        :type length: `int`
        :param length: A positive number indicating the target length of
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

    def __imul__(self, x: int, /):  # NOTE: ROUNDS DOWN
        """
        >>> x = Axis(4)
        >>> x *= 4
        >>> len(x)
        16
        """
        if x % 1:
            raise TypeError("operand must be an integral — floating-point not supported")
        if x < 0:
            raise ValueError(f'cannot multiply slots by a negative number (got {x!r}).')
        return self.resize(int(len(self) * x))

    def __ifloordiv__(self, x: float, /):  # NOTE: ROUNDS DOWN (floor division)
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
        return self.resize(self.__len__() // x)  # type: ignore

    __itruediv__ = __ifloordiv__

    def insert(self, index: typing.SupportsIndex, /):
        """Adds a new row/column at the specified index.

        :type index: `SupportsIndex`
        :param index: Target slot index.
        """
        with self._lock:
            self._slots.insert(index, Slot())

    def remove(self, index: typing.SupportsIndex = -1):
        """Delete the row/column at the specified index, or the last
        row/column if not specified.

        :type index: `SupportsIndex`
        :param index: Target slot index.
        """
        with self._lock:
            self._slots.pop(index)

    def __float__(self, /) -> float:
        return float(self.__len__())

    def __lt__(self, other: typing.Any, /) -> bool:
        return self.__len__() < other

    def __le__(self, other: typing.Any, /) -> bool:
        return self.__len__() <= other

    def __eq__(self, other: typing.Any, /) -> bool:  # pyright: ignore[reportIncompatibleMethodOverride]
        return self.__len__() == other

    def __ne__(self, other: typing.Any, /) -> bool:
        return self.__len__() != other

    def __gt__(self, other: typing.Any, /) -> bool:
        return self.__len__() > other

    def __ge__(self, other: typing.Any, /) -> bool:
        return self.__len__() >= other

    def __pos__(self) -> int:
        return +self.__len__()

    def __neg__(self) -> int:
        return -self.__len__()

    def __add__(self, i: int, /) -> int:
        return self.__len__() + i

    def __sub__(self, i: int, /) -> int:
        return self.__len__() - i

    def __mul__(self, i: int, /) -> int:
        return self.__len__() * i

    def __floordiv__(self, i: int, /) -> int:
        return self.__len__() // i

    __truediv__ = __floordiv__

    def __mod__(self, i: int, /) -> int:
        return self.__len__() % i

    def __divmod__(self, i: typing.Any, /) -> tuple[int, int]:
        length = self.__len__()
        return (length // i, length % i)

    def __pow__(self, i: int, /, mod: int | None = None) -> int:
        return pow(self.__len__(), i, mod)


@dataclasses.dataclass(init=False)
class Grid(_GridComponent):
    """Layout manager for Dear PyGui, emulating a table-like structure.

    :vartype cols: `Axis`
    :var cols: Living representation of the grid's columns (x-axis).
            See the `Axis` class for more information.

    :vartype rows: `Axis`
    :var rows: Living representation of the grid's rows (y-axis).
        See the `Axis` class for more information.

    :vartype target: `int | str`
    :var target: The integer identifier or string alias of the
        item used as the grid's positional reference. Additionally, it's
        visibility state is used to determine whether or not to display (draw)
        the grid. The size of the target item is also used as fallback values
        as necessary when `self.width` and/or `self.height` are not applicable.

    :vartype label: `str`
    :var label: An informal name for the grid.

    :vartype spacing: `array[float, float]`
    :var spacing: Values used to offset a slot's (columns
        and rows, respectively) position during a draw event when both
        `slot.spacing` and `axis.spacing` are not applicable (min. 0 per value).

    :vartype padding: `array[float, float, float, float]`
    :var padding: Used as the left, upper,
        right, and lower padding values during a draw event when item-level
        padding override values were not provided and both `slot.spacing` and
        `axis.spacing` are not applicable. The first and third values are used
        for column padding, while the second and fourth values are used for rows
        (min. 0 per value).

    :vartype width: `int`
    :var width: The horizontal size of the grid. Can be used to extend
        the grid beyond the default view of the target item, allowing for items
        to be positioned in their parent's scroll area. If 0, the width of the
        target item is used instead (min. 0).

    :vartype height: `int`
    :var height: The vertical size of the grid. Can be used to extend
        the grid beyond the default view of the target item, allowing for items
        to be positioned in their parent's scroll area. If 0, the height of the
        target item is used instead (min. 0).

    :vartype offsets: `array[float, float, float, float]`
    :var offsets: Similar to padding, but
        targets the left, upper, right, and lower edges of the grid itself and
        not its' slots. Can be used to expand or shrink the size of the grid's
        content region (min. 0 per value).

    :vartype rect_getter: `_RectGetter`
    :var rect_getter: Called before attempting to draw the grid
        to fetch the target item's size, position, and visibility status. The
        default implementation is a light wrapper around
        `dearpygui.get_item_state`. It may also call
        `dearpygui.get_item_configuration` if one or more details cannot be
        accessed by reading the item's state.

    :vartype overlay: `bool`
    :var overlay: If True, a visual representation of the grid will be
        displayed over it.

    :vartype show: `bool`
    :var show: If True, the grid and its' content will be visible.


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
    def __init__(
        self,
        cols: int = 1,
        rows: int = 1,
        parent: Item | None = 0,
        *,
        label: str = "",
        padding: typing.Sequence[float] | float | None = None,
        spacing: typing.Sequence[float] | float | None = None,
        width: int | None = None,
        height: int | None = None,
        offsets: typing.Sequence[float] | float | None = None,
        rect_getter: _RectGetter | None = None,
        overlay: bool = False,
        show: bool = True,
    ) -> None:
        _create_context()

        self._lock      = threading.Lock()
        self._drawlayer = 0
        self._item_data = set[ItemData]()
        self._dirty_refs  = set[Item | ItemData]()
        self._overlay   = Overlay(self)
        # the setters invoke `draw()`, so set the private vars here instead
        self._show = show
        self._show_overlay = overlay
        self._overlay.show = show and overlay

        self.cols = Axis(cols, label='x', _lock=self._lock)
        self.rows = Axis(rows, label='y', _lock=self._lock)
        self.label = label
        self.padding = padding
        self.spacing = spacing
        self.width = width
        self.height = height
        self.offsets = offsets
        self.parent = parent
        self.rect_getter = rect_getter

    @property
    def cols(self, /) -> Axis:  # pyright: ignore[reportRedeclaration]
        try:
            return self._cols
        except AttributeError:
            cols = self._cols = Axis(0, label="x", _lock=self._lock)
            return cols
    @cols.setter
    def cols(self, value: Axis | int, /) -> None:  # pyright: ignore[reportRedeclaration]
        if isinstance(value, Axis):
            self._cols = value
            value._lock = self._lock
        else:
            with self._lock:
                self._cols.resize(value)

    cols: property[Axis, Axis | int] = cols  # type: ignore

    @property
    def rows(self, /) -> Axis:  # pyright: ignore[reportRedeclaration]
        try:
            return self._rows
        except AttributeError:
            rows = self._rows = Axis(0, label="y", _lock=self._lock)
            return rows
    @rows.setter
    def rows(self, value: Axis | int, /) -> None:  # pyright: ignore[reportRedeclaration]
        if isinstance(value, Axis):
            self._rows = value
            value._lock = self._lock
        else:
            with self._lock:
                self._rows.resize(value)

    rows: property[Axis, Axis | int] = rows  # type: ignore

    label: str = ''
    parent: Item | None = None
    rect_getter: _RectGetter | None = None
    width: property[int, int | None, _True] = _min_number_property(0, 0)
    height: property[int, int | None, _True] = _min_number_property(0, 0)
    offsets: property[_Array[_4, float], _ArrayLike[typing.Any, float] | float | None, _True] = _float_arr_property(4, 0.0)
    padding: property[_Array[_4, float], _ArrayLike[typing.Any, float] | float | None, _True] = _float_arr_property(4, 0.0)
    spacing: property[_Array[_2, float], _ArrayLike[typing.Any, float] | float | None, _True] = _float_arr_property(2, 0.0)

    @property
    def show(self, /) -> bool:  # pyright: ignore[reportRedeclaration]
        try:
            return self._show
        except AttributeError:
            show = self._show = True
            return show
    @show.setter
    def show(self, value: bool, /) -> None:  # pyright: ignore[reportRedeclaration]
        with self._lock:
            show = self._show = value
            self._overlay.show = show and self.overlay

            for item_data in self._item_data:
                try:
                    _item_set_config(item_data.item, show=show)
                except SystemError:
                    if not dearpygui.does_item_exist(item_data.item):
                        self._dirty_refs.add(item_data)
                    else:
                        raise

        self.draw()

    show: property[bool, bool] = show  # type: ignore

    @property
    def overlay(self, /) -> bool:  # pyright: ignore[reportRedeclaration]
        try:
            return self._show_overlay
        except AttributeError:
            overlay = self._show_overlay = True
            return overlay
    @overlay.setter
    def overlay(self, value: bool, /) -> None:  # pyright: ignore[reportRedeclaration]
        with self._lock:
            self._show_overlay = value
            self._overlay.show = self.show and value

        self.draw()

    overlay: property[bool, bool] = overlay  # type: ignore

    @typing.overload
    def configure(self, *, cols: int = ..., rows: int = ..., parent: Item | None = ..., label: str | None = ..., padding: typing.Sequence[float] | float | None = ..., spacing: typing.Sequence[float] | float | None = ..., width: float | None = ..., height: float | None = ..., offsets: typing.Sequence[float] | float | None = ..., rect_getter: _RectGetter | None = ..., overlay: bool = ..., show: bool = ..., **kwargs) -> None:  ...  # pyright: ignore[reportInconsistentOverload]
    def configure(self, **kwargs):
        """Update the grid's settings."""
        missing = _MISSING
        super().configure(**{k:v for k,v in kwargs.items() if v is not missing})
        self._gc_item_data()

    def configuration(self):
        """Return the grid's various settings and values."""
        with self._lock:
            config = super().configuration()
        return config

    def _pop(self, item: Item):
        # Two instances of `ItemData` can potentially exist for the same item
        # since refs can be integers or strings. Try to remove all of them just
        # in case.
        if not dearpygui.does_item_exist(item):
            self._dirty_refs.add(item)
        else:
            if isinstance(item, str):
                refs = (item, dearpygui.get_alias_id(item), dearpygui.get_item_alias(item))
            else:
                refs = (item, dearpygui.get_item_alias(item))
            self._dirty_refs.update(refs)
            _item_set_config(item, pos=())
        self._gc_item_data()

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
            self._dirty_refs.update(self._item_data)
            self._gc_item_data()

    ANCHORS = {}
    ANCHORS["c"]  = ANCHORS["center"]    = (0.5, 0.5)
    ANCHORS["n"]  = ANCHORS["north"]     = (0.5, 0.0)
    ANCHORS["ne"] = ANCHORS["northeast"] = (1.0, 0.0)
    ANCHORS["e"]  = ANCHORS["east"]      = (1.0, 0.5)
    ANCHORS["se"] = ANCHORS["southeast"] = (1.0, 1.0)
    ANCHORS["s"]  = ANCHORS["south"]     = (0.5, 1.0)
    ANCHORS["sw"] = ANCHORS["southwest"] = (0.0, 1.0)
    ANCHORS["w"]  = ANCHORS["west"]      = (0.0, 0.5)
    ANCHORS["nw"] = ANCHORS["northwest"] = (0.0, 0.0)

    @typing.overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., max_size: typing.Sequence[float] | float | None = ..., max_width: int = ..., max_height: int = ..., padding: typing.Sequence[float] | float | None = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ..., rect_setter: _RectSetter = ...): ...
    @typing.overload
    def push(self, item: Item, cell: tuple[int, int], /, *, anchor: str = ..., max_size: typing.Sequence[float] | float | None = ..., max_width: int = ..., max_height: int = ..., padding: typing.Sequence[float] | float | None = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ..., rect_setter: _RectSetter = ...): ...
    @typing.overload
    def push(self, item: Item, cell_start: tuple[int, int], cell_stop: tuple[int, int], /, *, anchor: str = ..., max_size: typing.Sequence[float] | float | None = ..., max_width: int = ..., max_height: int = ..., padding: typing.Sequence[float] | float | None = ..., x1_pad: int = ..., y1_pad: int = ..., x2_pad: int = ..., y2_pad: int = ..., rect_setter: _RectSetter = ...): ...
    def push(self, item: Item, cell_start: typing.Any, cell_stop: typing.Any = None, /, *, anchor: str = 'c', rect_setter: _RectSetter = _default_rect_setter, max_size: typing.Any = None, max_width: typing.Any = None, max_height: typing.Any = None, padding: typing.Any = None, x1_pad: typing.Any = None, y1_pad: typing.Any = None, x2_pad: typing.Any = None, y2_pad: typing.Any = None):
        """Attach an item to the grid.

        Awaits internal lock release.

        :vartype item: `int | str`
        :var item: Item identifier to push.

        :vartype positional_arg2: `int | tuple[int, int]`
        :var col, cell_start: Index of the column that will contain the
            item, OR a 2-tuple containing the column and row indices
            of the first or only cell the item will occupy. If provided as a
            single integer, the next positional argument is non-optional and
            must be an integer indicating the row index.

        :vartype positional_arg3: `int | tuple[int, int]`
        :var row, cell_stop: Index of the row that will contain the
            item, OR a 2-tuple containing the column and row indices of the
            last cell this item will occupy. If provided as a 2-tuple, the
            prior positional argument must also be the first cell in the
            span/range as a 2-tuple.

        :vartype anchor: `str`
        :var anchor: A case-insensitive compass direction name or abbreviation
            indicating which side(s) of the cell the item will "stick" to e.g.
            `"north"`, `"ne"` (northeast), "southwest", etc. The default value
            `"center"` (or `"c"`) centers the item horizontally and vertically
            within its cellspan.

        :vartype rect_setter: `Callable[[int | str, int, int, int, int, bool]]`
        :var rect_setter: A callable accepting *item*, x-position, y-position,
            width, height, and visible state as positional arguments that updates
            the item's size, position, and visibility. The default implementation
            is a simple wrapper around `dearpygui.configure_item`.

        :vartype max_size: `float | tuple[float, float] | None`
        :var max_size: As a 2-tuple, this is used as the item's maximum width and
            height. When provided as a single numeric value, that value will be
            used as both the maxmimum width and height.

        :vartype max_width: `float | None`
        :var max_width: Individual width component (first value) of *max_size*.
            Ignored when *max_size* is specified.

        :vartype max_height: `float | None`
        :var max_height: Individual height component (second value) of *max_size*.
            Ignored when *max_size* is specified.

        :vartype padding: `float | tuple[float, float]`
        :var padding: A 4-item sequence whose values will be used to override the
            left, upper, right, and/or lower-padding values of the first/last slots
            in the target cell range, OR, a non-sequence value that will be used
            as the override value for all padding components. Inner NaN-like values
            are not applied as an overriding value.

        :vartype x1_pad: ``
        :var x1_pad: Overrides the left padding value of the first column
            in the target cell range. Ignored when *padding* is specified.

        :vartype y1_pad: ``
        :var y1_pad: Overrides the upper padding value of the first row
            in the target cell range. Ignored when *padding* is specified.

        :vartype x2_pad: ``
        :var x2_pad: Overrides the right padding value of the first column
            in the target cell range. Ignored when *padding* is specified.

        :vartype y2_pad: ``
        :var y2_pad: Overrides the lower padding value of the first row
            in the target cell range. Ignored when *padding* is specified.


        In order for an item to be managed by the grid, it must support sizing
        via `width` and `height` configurations, positioning via `pos`, and
        visibility updates via `show`. Otherwise, consider "wrapping" the item
        in a capatible parent such as a group or child window first.

        This method accepts three positional arguments — the item to push,
        and column and row indices. Single-cell coordinates can be passed as a
        2-tuple or two individual arguments (column and row indices, respectively).
        When it is desired to have the item occupy a range of cells, second
        and third positional arguments must be 2-tuples containing the column and
        row indices of the first and last cell in the range.

        Final cell coordinates are not determined when pushing the item to the grid.
        Instead, they are evaluated each time the grid is drawn. This is
        negligible performance-wise, and allows the grid to have some beneficial
        (but sometimes suprising) behaviors:
        - cell indices can be negative
        - grid's dimensions can be freely updated even after adding items
        - coordinates/indices can be "out-of-range"
        Like Python sequences, negative indices start from the end of the axis.
        Since coordinates are determined when drawing the grid, items can be
        "pinned" to a specific side of an axis depending on whether the index
        used is positive or negative. For example, using the coordinates `(1, -1)`
        will ensure an item is **always** positioned in the second column of the
        last row that exists during that draw event. However, if one or more
        cells do not exist when attempting to position the item, the item is
        hidden from view until additional columns/rows are added to the grid.

        An item's size is affected by the size of the columns and rows they
        occupy. *max_size* (OR individual *max_width/height* values) can be
        provided to limit the item's size as cells expand. However, the grid
        will shrink or hide items as needed to conform to slot constraints.
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
                    if rect_setter == _default_rect_setter:
                        rect_setter = _set_text_rect
                elif item_type == 'mvAppItemType::mvTable':
                    # BUG: Table items accept a `pos` keyword, but DPG doesn't
                    # do anything with it.
                    raise ValueError("`mvTable` items cannot be explicitly positioned")

            item_data = ItemData(
                item=item,
                cellspan=cellspan,
                max_size=max_size,
                padding=padding,
                pos_coef=self.ANCHORS[anchor.casefold()],
                rect_setter=rect_setter,
                is_text=is_text,
            )
            self._item_data.add(item_data)
            return item_data

    def _get_parent_rect_info(self, default=_default_rect_getter):
        return (self.rect_getter or default)(self.parent or 0)

    def _gc_item_data(self):
        # currently called before or after:
        #   * updating the grid's settings
        #   * updating `self._item_data`
        #   * drawing the grid
        self._item_data.difference_update(self._dirty_refs)
        self._dirty_refs.clear()

    def draw(self, /):
        """Draw the grid, updating the size and position of any item
        attached.

        Awaits internal lock release.
        """
        with self._lock:
            self._gc_item_data()

            _area_width, _area_height, area_x_pos, area_y_pos, area_visible = self._get_parent_rect_info()

            if self._show and area_visible:
                area_width = self.width or _area_width
                self._upd_slot_states(self.cols, area_width, 0)

                area_height = self.height or _area_height
                self._upd_slot_states(self.rows, area_height, 1)

                self._upd_item_states()

                area_x_max = area_x_pos + area_width
                area_y_max = area_y_pos + area_height
            else:
                area_x_pos = area_y_pos = area_x_max = area_y_max = 0

            self._overlay.draw(area_x_pos, area_y_pos, area_x_max, area_y_max)

    __call__ = draw
    __code__ = (lambda: ...).__code__  # tell DPG we accept no arguments

    def _upd_slot_states(self, axis: Axis, area_size: float, index_offset: typing.Literal[0, 1], /):
        xy1_index = index_offset
        xy2_index = index_offset + 2

        offsets = self.offsets

        area_c1_pad = offsets[xy1_index]
        area_c2_pad = offsets[xy2_index]
        content_size = area_size - area_c1_pad - area_c2_pad

        padding = self.padding

        axis_c1_pad, axis_c2_pad = axis._padding
        if axis_c1_pad != axis_c1_pad:  # NaN
            axis_c1_pad = padding[xy1_index]
        if axis_c2_pad != axis_c2_pad:  # NaN
            axis_c2_pad = padding[xy2_index]

        spacing = self.spacing

        axis_spacing = axis._spacing
        if axis_spacing != axis_spacing:  # NaN
            axis_spacing = spacing[xy1_index]

        # axis must be at least `total_size` pixels wide/long
        total_size, total_weight = axis._get_sizeweight_tuple()

        remaining_space = content_size - total_size
        if remaining_space < 0.0:
            remaining_space = 0.0

        size_unit = (remaining_space / total_weight)

        alloc_size = 0.0
        for slot in axis._slots:
            state = slot._state

            slot_spacing = slot._spacing
            if slot_spacing != slot_spacing:  # NaN
                slot_spacing = axis_spacing
            state.spacing = slot_spacing

            # centerline, offset by half the slot spacing
            state.pos = alloc_size + area_c1_pad + (slot_spacing * 0.5)  # XXX: allows negative spacing

            xy1_pad, xy2_pad = slot._padding
            if xy1_pad != xy1_pad:   # NaN
                xy1_pad = axis_c1_pad
            if xy2_pad != xy2_pad:   # NaN
                xy2_pad = axis_c2_pad
            state.padding = (xy1_pad, xy2_pad)

            # non-zero size == "fixed fit" policy, otherwise it scales
            slot_size = slot._size or (size_unit * slot._weight)

            slot_content_size = slot_size - slot_spacing
            if slot_content_size < 0.0:
                slot_content_size = 0.0
            state.size = slot_content_size

            alloc_size += slot_size

    def _upd_item_states(self, *, int=int, does_item_exist=dearpygui.does_item_exist, get_item_state=dearpygui.get_item_state):
        rows = self._rows._slots
        cols = self._cols._slots

        dirty_refs = self._dirty_refs

        n_cols = len(cols)
        n_rows = len(rows)

        if n_cols == 0 or n_rows == 0:
            for item_data in self._item_data:
                try:
                    item_data.rect_setter(item_data.item, 0, 0, 0, 0, False)
                except SystemError:
                    if not does_item_exist(item_data.item):
                        dirty_refs.add(item_data.item)
                        continue
                    raise

            self._gc_item_data()
            return

        for item_data in self._item_data:
            x1, y1, x2, y2 = item_data.cellspan

            if item_data._out_of_bounds:
                if x1 >= n_cols or x2 >= n_cols or y1 >= n_rows or y2 >= n_rows:
                    continue
                item_data._out_of_bounds = False
            elif x1 >= n_cols or x2 >= n_cols or y1 >= n_rows or y2 >= n_rows:
                item_data._out_of_bounds = True
                try:
                    item_data.rect_setter(item_data.item, 0, 0, 0, 0, False)
                except SystemError:
                    if not does_item_exist(item_data.item):
                        dirty_refs.add(item_data.item)
                        continue
                    raise
                continue

            # convert negative indexes
            if x1 < 0: x1 %= n_cols
            if y1 < 0: y1 %= n_rows
            if x2 < 0: x2 %= n_cols
            if y2 < 0: y2 %= n_rows
            # fix inverted cellspan
            if y1 > y2: (y1, y2) = (y2, y1)
            if x1 > x2: (x1, x2) = (x2, x1)

            col1_state = cols[x1]._state
            row1_state = rows[y1]._state
            col2_state = cols[x2]._state
            row2_state = rows[y2]._state

            x1_pad, y1_pad, x2_pad, y2_pad = item_data.padding

            # cell x-axis
            if x1_pad != x1_pad:  # is NaN?
                x1_pad = col1_state.padding[0]
            cell_x_pos = col1_state.pos + x1_pad

            if x2_pad != x2_pad:  # is NaN?
                x2_pad = col2_state.padding[1]
            cell_width = col2_state.pos + col2_state.size - cell_x_pos - x2_pad  # col2_end = col2_state.pos + col2_state.size

            if cell_width < 1:  # hide item (no real estate)
                try:
                    item_data.rect_setter(item_data.item, 0, 0, 0, 0, False)
                except SystemError:
                    if not does_item_exist(item_data.item):
                        dirty_refs.add(item_data.item)
                        continue
                    raise
                continue

            # cell y-axis
            if y1_pad != y1_pad:  # is NaN?
                y1_pad = row1_state.padding[0]
            cell_y_pos = row1_state.pos + y1_pad

            if y2_pad != y2_pad:  # is NaN?
                y2_pad = row2_state.padding[1]
            cell_height = row2_state.pos + row2_state.size - cell_y_pos - y2_pad

            if cell_height < 1:  # hide item (no real estate)
                try:
                    item_data.rect_setter(item_data.item, 0, 0, 0, 0, False)
                except SystemError:
                    if not does_item_exist(item_data.item):
                        dirty_refs.add(item_data.item)
                        continue
                    raise
                continue

            ## item size
            #if item_data.is_text:
            #    # We can't resize text items, so they either fit the
            #    # space we have available, or don't. Ideally, the user
            #    # should push a child window parenting the desired text
            #    # item instead. We can resize that, and has the added
            #    # benefit of wrapping the text (if enabled) when we do.
            #    try:
            #        item_width, item_height = get_item_state(item_data.item)['rect_size']
            #    except SystemError:
            #        if not does_item_exist(item_data.item):
            #            dirty_refs.add(item_data.item)
            #            continue
            #        raise
            #else:
            item_width, item_height = item_data.max_size
            if not item_width or item_width > cell_width:
                item_width = cell_width

            if not item_height or item_height > cell_height:
                item_height = cell_height

            if item_width < 1 or item_height < 1:  # hide item (too small)
                item_width = item_height = item_x_pos = item_y_pos = 0
                item_show = False
            else:
                x_coef, y_coef = item_data.pos_coef
                item_x_pos = int(cell_x_pos + (cell_width - item_width) * x_coef)
                item_y_pos = int(cell_y_pos + (cell_height - item_height) * y_coef)
                item_width = int(item_width)
                item_height = int(item_height)
                item_show = True

            try:
                item_data.rect_setter(
                    item_data.item, item_x_pos, item_y_pos, item_width, item_height, item_show,
                )
            except SystemError:
                if not does_item_exist(item_data.item):
                    dirty_refs.add(item_data.item)
                    continue
                raise

        self._gc_item_data()


class Overlay:
    """Visual representation of a :py:class:`Grid`s boundaries."""

    @property
    def border_color(self) -> tuple:
        return self._border_line_color[:3]
    @border_color.setter
    def border_color(self, value, /) -> None:
        self._border_line_color = (*value, 255)
        self._border_pad_color = (*value, 80)

    @property
    def slots_color(self) -> tuple:
        return self._slots_line_color[:3]
    @slots_color.setter
    def slots_color(self, value, /) -> None:
        self._slots_line_color = (*value, 120)
        self._slots_void_color = (*value, 255)
        self._slots_pad_color = (*value, 80)

    def __init__(
        self,
        grid: Grid,
        /, *,
        show: bool = False,
        border_color: tuple[int, int, int] = (150, 255, 255),
        slots_color: tuple[int, int, int] = (150, 255, 255),
    ) -> None:
        self.grid = grid
        self.show = show
        self.border_color = border_color
        self.slots_color = slots_color

    __VIEWPORT_DRAWLIST = f"{__name__}.Overlay"

    _drawlayer = 0

    @typing.overload
    def draw(self, /) -> None: ...
    @typing.overload
    def draw(self, x_min: int, y_min: int, x_max: int, y_max: int, /) -> None: ...
    def draw(self, /, *args) -> None:
        if args:
            x_min, y_min, x_max, y_max = args
        else:
            width, height, x_min, y_min, *_ = self.grid._get_parent_rect_info()
            x_max = (self.grid.width or width) + x_min
            y_max = (self.grid.height or height) + y_min

            args = (x_min, y_min, x_max, y_max)

        layer = self._drawlayer

        show = self.show
        if not (show and any(args)):
            layer = self._drawlayer
            if layer:
                try:
                    _item_set_config(layer, show=False)
                except SystemError:
                    if dearpygui.does_item_exist(layer):
                        raise
                    else:
                        self._drawlayer = 0
            return

        try:
            if not (layer and dearpygui.does_item_exist(layer)):
                layer = self._drawlayer = dearpygui.add_draw_layer(show=True, parent=__class__.__VIEWPORT_DRAWLIST)
            else:
                dearpygui.delete_item(layer, children_only=True)
        except SystemError:
            if not dearpygui.does_item_exist(__class__.__VIEWPORT_DRAWLIST):
                dearpygui.add_viewport_drawlist(tag=__class__.__VIEWPORT_DRAWLIST)
            if not (layer and dearpygui.does_item_exist(layer)):
                layer = self._drawlayer = dearpygui.add_draw_layer(show=True, parent=__class__.__VIEWPORT_DRAWLIST)
            else:
                raise

        self._draw_outline(x_min, y_min, x_max, y_max)
        self._draw_slots(x_min, y_min, x_max, y_max)

    __call__ = draw
    __code__ = (lambda: ...).__code__  # tell DPG we accept no arguments

    _EMPTY_COLOR = (0, 0, 0, 0)

    def _draw_outline(self, x_min: int, y_min: int, x_max: int, y_max: int):
        layer = self._drawlayer

        no_color = __class__._EMPTY_COLOR
        line_color = self._border_line_color
        pad_color = self._border_pad_color

        x1_pad, y1_pad, x2_pad, y2_pad = self.grid.offsets

        # padding
        if x1_pad:
            dearpygui.draw_rectangle(
                (x_min, y_max), (x_min + x1_pad, y_min + y1_pad),
                color=no_color, fill=pad_color, parent=layer,
            )
        if y1_pad:
            dearpygui.draw_rectangle(
                (x_min, y_min), (x_max - x2_pad, y_min + y1_pad),
                color=no_color, fill=pad_color, parent=layer,
            )
        if x2_pad:
            dearpygui.draw_rectangle(
                (x_max, y_min), (x_max - x2_pad, y_max - y2_pad),
                color=no_color, fill=pad_color, parent=layer,
            )
        if y2_pad:
            dearpygui.draw_rectangle(
                (x_max, y_max), (x_min + x1_pad, y_max - y2_pad),
                color=no_color, fill=pad_color, parent=layer,
            )

        # outline
        dearpygui.draw_rectangle(
            (x_min, y_min), (x_max, y_max),
            fill=no_color, color=line_color, parent=layer,
        )

    def _draw_slots(self, x_min: int, y_min: int, x_max: int, y_max: int, /):
        layer = self._drawlayer

        no_color = __class__._EMPTY_COLOR
        line_color = self._slots_line_color
        space_color = self._slots_void_color
        pad_color = self._slots_pad_color

        cols = self.grid.cols
        rows = self.grid.rows

        x1_pad, y1_pad, x2_pad, y2_pad = self.grid.offsets
        x_space = cols.spacing / 2
        y_space = rows.spacing / 2
        cont_x_min = x_min + x1_pad
        cont_y_min = y_min + y1_pad
        cont_x_max = x_max - x2_pad
        cont_y_max = y_max - y2_pad

        for col in cols:
            col_state = col._state
            cell_x_min  = x_min + col_state.pos
            cell_x_max  = cell_x_min + col_state.size
            cell_x1_pad, cell_x2_pad = col_state.padding

            for row in rows:
                row_state = row._state
                cell_y_min  = y_min + row_state.pos
                cell_y_max  = cell_y_min + row_state.size
                cell_y1_pad, cell_y2_pad = row_state.padding

                if cell_x1_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_min, cell_y_max), (cell_x_min + cell_x1_pad, cell_y_min + cell_y1_pad),
                        color=no_color, fill=pad_color, parent=layer,
                    )
                if cell_y1_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_min, cell_y_min), (cell_x_max - cell_x2_pad, cell_y_min + cell_y1_pad),
                        color=no_color, fill=pad_color, parent=layer,
                    )
                if cell_x2_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_max, cell_y_min), (cell_x_max - cell_x2_pad, cell_y_max - cell_y2_pad),
                        color=no_color, fill=pad_color, parent=layer,
                    )
                if cell_y2_pad:
                    dearpygui.draw_rectangle(
                        (cell_x_max, cell_y_max), (cell_x_min + cell_x1_pad, cell_y_max - cell_y2_pad),
                        color=no_color, fill=pad_color, parent=layer,
                    )

                dearpygui.draw_rectangle(
                    (cont_x_min, cell_y_min), (cont_x_max, cell_y_min - y_space),
                    color=no_color, fill=space_color, parent=layer,
                )
                dearpygui.draw_rectangle(
                    (cont_x_min, cell_y_max), (cont_x_max, cell_y_max + y_space),
                    color=no_color, fill=space_color, parent=layer,
                )
                # lines
                dearpygui.draw_line(
                    (cont_x_min, cell_y_min), (cont_x_max, cell_y_min),
                    color=line_color, parent=layer,
                )
                dearpygui.draw_line(
                    (cont_x_min, cell_y_max), (cont_x_max, cell_y_max),
                    color=line_color, parent=layer,
                )

            # outer spacing
            dearpygui.draw_rectangle(
                (cell_x_min, cont_y_min), (cell_x_min - x_space, cont_y_max),
                color=no_color, fill=space_color, parent=layer,
            )
            dearpygui.draw_rectangle(
                (cell_x_max, cont_y_min), (cell_x_max + x_space, cont_y_max),
                color=no_color, fill=space_color, parent=layer,
            )
            # lines
            dearpygui.draw_line(
                (cell_x_min, cont_y_min), (cell_x_min, cont_y_max),
                color=line_color, parent=layer,
            )
            dearpygui.draw_line(
                (cell_x_max, cont_y_min), (cell_x_max, cont_y_max),
                color=line_color, parent=layer,
            )




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
