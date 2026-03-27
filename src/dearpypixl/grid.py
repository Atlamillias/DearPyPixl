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

from dearpypixl.core import management
from dearpypixl.core.protocols import Item, DataDescriptor
from dearpypixl.core import codegen


__all__ = ("ItemData", "Slot", "Axis", "Grid")




NaN = float("nan")

_MISSING = object()




# [ HELPER FUNCTIONS ]

def _is_nan(v: typing.Any) -> bool:
    return v != v

def _to_value(value: typing.Any, default: typing.Any):
    if value is None or _is_nan(value):
        return default
    return value

def _to_float_arr(value: typing.Sequence[float] | float | None, length: int, default: float = NaN) -> typing.Any:
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
        return array('f', (default,) * length)  # pyright: ignore
    if isinstance(value, (float, int)):
        return array('f', (value,) * length)  # pyright: ignore

    arr = array('f', (default,) * length)
    try:
        for i in range(length):
            arr[i] = _to_value(value[i], default)
    except IndexError:
        pass
    return arr  # pyright: ignore

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
    def __call__(self, item: Item, /) -> tuple[int, int, int, int, bool]: ...

def _default_rect_getter(item: Item, /, *, _config_getter=_dearpygui.get_item_configuration, _state_getter=_dearpygui.get_item_state) -> tuple[int, int, int, int, bool]:
    state = _state_getter(item)

    visible = state.get("visible")
    if visible is None:
        visible = _config_getter(item)["show"]

    return *state['rect_size'], *state['pos'], visible


class _RectSetter(typing.Protocol):
    def __call__(self, item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool, /) -> typing.Any: ...

def _default_rect_setter(item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool, /, *, _config_setter=_dearpygui.configure_item):
    _config_setter(item, width=width, height=height, pos=(x_pos, y_pos), show=show)




@dataclasses.dataclass(slots=True)
class ItemData:
    item       : int
    cellspan   : tuple[int, int, int, int]
    max_size   : tuple[float, float]
    padding    : tuple[float, float, float, float,]
    pos_coef   : tuple[float, float]
    rect_setter: _RectSetter

    _out_of_bounds: bool = dataclasses.field(default=False, init=False, repr=False)

    def __hash__(self) -> int:
        return hash(self.item)

    def __eq__(self, other, /) -> bool:
        if isinstance(other, str):
            other = _dearpygui.get_alias_id(other)
        try:
            h = hash(other)
        except:
            return False
        return self.item == h




# [ major components ]

@dataclasses.dataclass(init=False)
class _GridComponent:
    __slots__ = ('label', '_spacing', '_padding')

    label: str
    spacing: float = _min_number_property(0.0)
    padding: typing.MutableSequence[float] = _float_arr_property(2)

    def __init__(self, *, label: str = '', spacing: float = NaN, padding: typing.Sequence[float] | float | None = None, **kwargs):
        self.configure(label=label, spacing=spacing, padding=padding, **kwargs)

    def configure(self, **kwargs) -> None:
        fields = self.__dataclass_fields__
        for k, v in kwargs.items():
            if k in fields:
                self.__setattr__(k, v)

    def configuration(self) -> dict[str, typing.Any]:
        return {f:getattr(self, f) for f in self.__dataclass_fields__}


@dataclasses.dataclass(slots=True)
class _GridSlotState:
    pos    : float = 0
    size   : float = 0
    spacing: float = 0
    padding: tuple[float, float] = (0, 0)

@dataclasses.dataclass(init=False)
class Slot(_GridComponent):
    __slots__ = ('_state', '_size', '_weight')

    weight: DataDescriptor[float, float | None] = _min_number_property(0.1, 1.0)
    size: DataDescriptor[int, int | None] = _min_number_property(0, 0)

    @typing.overload
    def __init__(self, *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., weight: float | None = ..., size: int | None = ...) -> None: ...  # type: ignore
    def __init__(self, *, weight: typing.Any = 1.0, size: typing.Any = 0, **kwargs) -> None:
        self._state = _GridSlotState()  # managed by the parenting `Grid` during a draw event
        super().__init__(weight=weight, size=size, **kwargs)

    def configure(self, *, label: str = ..., spacing: float | None = ..., padding: typing.Sequence[float] | float | None = ..., weight: float | None = ..., size: int | None = ...) -> None: ... # type: ignore
    del locals()["configure"]

    def configuration(self) -> dict[typing.Literal['label', 'spacing', 'padding', 'weight', 'size'], typing.Any]: ...  # type: ignore
    del locals()["configuration"]


@dataclasses.dataclass(init=False)
class Axis(_GridComponent, typing.Iterable[Slot], typing.Sized):
    __slots__ = ('_slots', '_lock')

    length: DataDescriptor[int, int] = property(lambda self: self.__len__(), lambda self, value: self.resize(value))

    def __init__(self, length: int = 0, *, _lock=None, **kwargs) -> None:
        self._slots = list[Slot]()
        self._lock  = _lock or threading.Lock()
        super().__init__(length=length, **kwargs)

    @property
    def weight(self, /) -> float:
        with self._lock:
            return sum(s._weight for s in self._slots if not s._size)  # ty:ignore[unresolved-attribute]

    @property
    def size(self, /) -> int:
        with self._lock:
            return sum(s._size for s in self._slots)  # ty:ignore[unresolved-attribute]

    def _get_sizeweight_tuple(self, /, *, sum=sum) -> tuple[int, float]:
        # used by `Grid`
        slots = self._slots
        return sum(s._size for s in slots), sum(s._weight for s in slots if not s._size)  # ty:ignore[unresolved-attribute]

    def __str__(self, /) -> str:
        return str(self._slots)

    def __bool__(self, /) -> bool:
        return bool(self._slots)

    def __getitem__(self, index: typing.SupportsIndex, /) -> Slot:
        return self._slots[index]

    def __iter__(self, /) -> typing.Iterator[Slot]:
        yield from self._slots

    def __len__(self, /, *, _len=len) -> int:
        return _len(self._slots)

    __int__ = __index__ = __trunc__ = __floor__ = __ceil__ = __abs__ = __len__

    def __iadd__(self, n: int, /) -> typing.Self:
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
        if not n:
            return self
        if n > 0:
            with self._lock:
                self._slots.extend(Slot() for _ in range(n))
                return self
        return self.__isub__(abs(n))

    def __isub__(self, n: int, /) -> typing.Self:
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
        if not n:
            return self
        if n > 0:
            with self._lock:
                del self._slots[-n:]
                return self
        return self.__iadd__(abs(n))

    def resize(self, length: int, /):
        """
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

    def __imul__(self, n: int, /):  # NOTE: ROUNDS DOWN
        """
        >>> x = Axis(4)
        >>> x *= 4
        >>> len(x)
        16
        """
        if n % 1:
            raise TypeError("operand must be an integral — floating-point not supported")
        if n < 0:
            raise ValueError(f'cannot multiply slots by a negative number (got {n!r}).')
        return self.resize(int(len(self) * n))

    def __ifloordiv__(self, x: float, /):
        """
        >>> x = Axis(16)
        >>> x /= 2
        >>> len(x)
        8
        >>> x /= 3  # floor div
        >>> len(x)
        2
        """
        if x < 0:
            raise ValueError(f"cannot divide slots by a negative number (got {x!r}).")
        return self.resize(self.__len__() // x)  # type: ignore

    __itruediv__ = __ifloordiv__

    def insert(self, index: typing.SupportsIndex, /):
        with self._lock:
            self._slots.insert(index, Slot())

    def remove(self, index: typing.SupportsIndex = -1):
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

    @management.initializer
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
        self._lock        = threading.Lock()
        self._drawlayer   = 0
        self._item_data   = set[ItemData]()
        self._data_to_del = set[int | ItemData]()
        self._overlay     = Overlay(self)
        # the setters invoke `draw()`, so set the private vars here instead
        self._show         = show
        self._show_overlay = overlay
        self._overlay.show = show and overlay

        self.cols        = Axis(cols, label='x', _lock=self._lock)
        self.rows        = Axis(rows, label='y', _lock=self._lock)
        self.label       = label
        self.padding     = padding
        self.spacing     = spacing
        self.width       = width
        self.height      = height
        self.offsets     = offsets
        self.parent      = parent
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

    cols: DataDescriptor[Axis, Axis | int] = cols  # pyright: ignore

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

    rows: DataDescriptor[Axis, Axis | int] = rows  # pyright: ignore

    label: str = ''
    parent: Item | None = None
    rect_getter: _RectGetter | None = None
    width: DataDescriptor[int, int | None] = _min_number_property(0, 0)
    height: DataDescriptor[int, int | None] = _min_number_property(0, 0)
    offsets: DataDescriptor[typing.Sequence[float], typing.Sequence[float] | float | None] = _float_arr_property(4, 0.0)
    padding: DataDescriptor[typing.Sequence[float], typing.Sequence[float] | float | None] = _float_arr_property(4, 0.0)
    spacing: DataDescriptor[typing.Sequence[float], typing.Sequence[float] | float | None] = _float_arr_property(2, 0.0)

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
                        self._data_to_del.add(item_data)
                    else:
                        raise

        self.draw()

    show: DataDescriptor[bool, bool] = show  # pyright: ignore

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

    overlay: DataDescriptor[bool, bool] = overlay  # pyright: ignore

    @typing.overload
    def configure(self, *, cols: int = ..., rows: int = ..., parent: Item | None = ..., label: str | None = ..., padding: typing.Sequence[float] | float | None = ..., spacing: typing.Sequence[float] | float | None = ..., width: float | None = ..., height: float | None = ..., offsets: typing.Sequence[float] | float | None = ..., rect_getter: _RectGetter | None = ..., overlay: bool = ..., show: bool = ..., **kwargs) -> None:  ...  # type: ignore
    def configure(self, **kwargs):
        missing = _MISSING
        super().configure(**{k:v for k,v in kwargs.items() if v is not missing})
        self._gc_item_data()

    def configuration(self):
        with self._lock:
            config = super().configuration()
        return config

    def pop(self, item: Item):
        if isinstance(item, str):
            item = dearpygui.get_alias_id(item)

        with self._lock:
            self._data_to_del.discard(item)  # type: ignore
            self._item_data.discard(item)  # type: ignore

    def clear(self):
        with self._lock:
            for item_data in self._item_data:
                try:
                    _item_set_config(item_data.item, pos=())
                except SystemError:
                    pass
            self._data_to_del.update(self._item_data)
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

    def push(self, item, cell_start: typing.Any, cell_stop: typing.Any = None, /, *, anchor='c', rect_setter=_default_rect_setter, max_size=None, padding=None):
        # item
        if isinstance(item, str):
            uuid = dearpygui.get_alias_id(item)
            if not uuid:
                raise ValueError(f"item {item!r} does not exist")
            item = uuid
        assert isinstance(item, int)

        # cellspan
        if hasattr(cell_start, '__iter__'):  # cell range?
            try:
                x1, y1 = cell_start
            except ValueError:
                raise ValueError(f'expected a 2-item sequence of cell coordinates for `cell_start`, got {len(cell_start)!r}.') from None
            try:
                x2, y2 = cell_stop
            except TypeError:
                if cell_stop is None:  # single cell
                    x2 = x1
                    y2 = y1
                else:
                    raise ValueError(f'expected a 2-item sequence of cell coordinates for `cell_stop`, got {cell_stop!r}.') from None
        else:  # single cell
            x1 = x2 = cell_start
            try:
                y1 = y2 = int(cell_stop)
            except TypeError:
                if cell_stop is not None:
                    raise TypeError(f'expected int for `row`, got {type(cell_stop)!r}.') from None
                raise TypeError(f"expected 3 positional arguments for '{self.push.__qualname__}()' got 2.") from None

        cellspan = (x1, y1, x2, y2)

        # max_size
        if isinstance(max_size, (int, float)):
            max_wt = max_ht = max_size
        elif max_size is None:
            max_wt = max_ht = 0.0
        else:
            max_wt, max_ht = max_size

        max_size = (
            0.0 if max_wt is None or max_wt < 0 else float(max_wt),
            0.0 if max_ht is None or max_ht < 0 else float(max_ht),
        )

        # padding
        if isinstance(padding, (int, float)):
            pad_x1 = pad_y1 = pad_x2 = pad_y2 = padding
        elif padding is None:
            pad_x1 = pad_y1 = pad_x2 = pad_y2 = NaN
        else:
            pad_x1, pad_y1, pad_x2, pad_y2 = padding

        padding = (
            NaN if pad_x1 is None or pad_x1 < 0 else float(pad_x1),
            NaN if pad_y1 is None or pad_y1 < 0 else float(pad_y1),
            NaN if pad_x2 is None or pad_x2 < 0 else float(pad_x2),
            NaN if pad_y2 is None or pad_y2 < 0 else float(pad_y2),
        )

        # anchor coefficients
        try:
            pos_coef = __class__.ANCHORS[anchor.casefold()]
        except Exception as error:
            anchors = tuple(__class__.ANCHORS)
            choices = ", ".join(repr(s) for s in anchors[:-1]) + f"or {anchors[-1]!r}"
            message = f"expected case-insensitive string literal {choices} — got {anchor!r}"
            if isinstance(error, AttributeError):
                error = AttributeError(message)
            elif isinstance(error, KeyError):
                error = ValueError(message)
            raise error from None

        item_data = ItemData(
            item=item,
            cellspan=cellspan,
            max_size=max_size,
            padding=padding,
            pos_coef=pos_coef,
            rect_setter=rect_setter or _default_rect_setter,
        )

        with self._lock:
            self._data_to_del.discard(item)
            self._item_data.discard(item)  # type: ignore
            self._item_data.add(item_data)

        return item

    def _get_parent_rect_info(self, default=_default_rect_getter):
        return (self.rect_getter or default)(self.parent or 0)

    def _gc_item_data(self):
        # currently called before or after:
        #   * updating the grid's settings
        #   * updating `self._item_data`
        #   * drawing the grid
        self._item_data.difference_update(self._data_to_del)
        self._data_to_del.clear()

    def draw(self, /):
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

        axis_c1_pad, axis_c2_pad = axis._padding  # ty:ignore[unresolved-attribute]
        if axis_c1_pad != axis_c1_pad:  # NaN
            axis_c1_pad = padding[xy1_index]
        if axis_c2_pad != axis_c2_pad:  # NaN
            axis_c2_pad = padding[xy2_index]

        spacing = self.spacing

        axis_spacing = axis._spacing  # ty:ignore[unresolved-attribute]
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

            slot_spacing = slot._spacing  # ty:ignore[unresolved-attribute]
            if slot_spacing != slot_spacing:  # NaN
                slot_spacing = axis_spacing
            state.spacing = slot_spacing

            # centerline, offset by half the slot spacing
            state.pos = alloc_size + area_c1_pad + (slot_spacing * 0.5)  # XXX: allows negative spacing

            xy1_pad, xy2_pad = slot._padding  # ty:ignore[unresolved-attribute]
            if xy1_pad != xy1_pad:   # NaN
                xy1_pad = axis_c1_pad
            if xy2_pad != xy2_pad:   # NaN
                xy2_pad = axis_c2_pad
            state.padding = (xy1_pad, xy2_pad)

            # non-zero size == "fixed fit" policy, otherwise it scales
            slot_size = slot._size or (size_unit * slot._weight)  # ty:ignore[unresolved-attribute]

            slot_content_size = slot_size - slot_spacing
            if slot_content_size < 0.0:
                slot_content_size = 0.0
            state.size = slot_content_size

            alloc_size += slot_size

    def _upd_item_states(self, *, int=int, does_item_exist=dearpygui.does_item_exist, get_item_state=dearpygui.get_item_state):
        rows = self._rows._slots
        cols = self._cols._slots

        dirty_refs = self._data_to_del

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
