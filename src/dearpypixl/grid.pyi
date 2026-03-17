from typing import *
import types

if TYPE_CHECKING:
    from dearpypixl.core.protocols import Item


__all__ = ("ItemData", "Slot", "Axis", "Grid")




class _Array[T, L: int = int](Protocol):
    def __len__(self, /) -> L: ...
    def __iter__(self, /) -> Iterator[T]: ...
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> T: ...
    @overload
    def __getitem__(self, slice: slice, /) -> _Array[T, int]: ...

class _MutArray[T, L: int = int](_Array[T, L], Protocol):
    @overload
    def __setitem__(self, index: SupportsIndex, value: T, /) -> None: ...
    @overload
    def __setitem__(self, slice: slice, value: _Array[T, L], /) -> None: ...


class _RectGetter(Protocol):
    """A function that returns an item's size, position, and visibility
    state as a 5-tuple `(width, height, x_pos, y_pos, is_visible)`.
    """
    def __call__(self, item: Item, /) -> tuple[int, int, int, int, bool]: ...

class _RectSetter(Protocol):
    """A function that updates an item's size and position via
    `dearpygui.configure_item()`.
    """
    def __call__(self, item: Item, x_pos: int, y_pos: int, width: int, height: int, show: bool, /) -> Any: ...


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
    max_size   : tuple[float, float]
    padding    : tuple[float, float, float, float]
    pos_coef   : tuple[float, float]
    rect_setter: _RectSetter
    def __hash__(self, /) -> int: ...
    def __eq__(self, other: Any, /) -> bool: ...


class _GridComponent(Protocol):
    @property
    def label(self, /) -> str: ...
    @label.setter
    def label(self, value: str, /) -> None: ...
    @property
    def spacing(self, /) -> float: ...
    @spacing.setter
    def spacing(self, value: float | None, /) -> None: ...
    @spacing.deleter
    def spacing(self, /) -> None: ...
    @property
    def padding(self, /) -> float: ...
    @padding.setter
    def padding(self, value: float | None, /) -> None: ...
    @padding.deleter
    def padding(self, /) -> None: ...
    def configure(self, /) -> None: ...
    def configuration(self, /) -> Any: ...

class Slot(_GridComponent):
    """A grid row or column.

    :vartype label: `str`
    :var label: Informal name for the slot.

    :vartype spacing: `float`
    :var spacing: Used to offset the slot's position during a draw
        event. Is ignored for calculations when NaN.

    :vartype padding: `_MutArray[float, Literal[2]]`
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
    object may indicate this through its' `label` attribute.
    """
    @property
    def weight(self, /) -> float: ...
    @weight.setter
    def weight(self, value: float | None, /) -> None: ...
    @weight.deleter
    def weight(self, /) -> None: ...
    @property
    def size(self, /) -> int: ...
    @size.setter
    def size(self, value: int | None, /) -> None: ...
    @size.deleter
    def size(self, /) -> None: ...
    def __init__(self, /, *, label: str = ..., spacing: float | None = ..., padding: Sequence[float] | float | None = ..., weight: float | None = ..., size: int | None = ...) -> None: ...
    def configure(self, /, *, label: str = ..., spacing: float | None = ..., padding: Sequence[float] | float | None = ..., weight: float | None = ..., size: int | None = ...) -> None: ...
    def configuration(self, /) -> dict[Literal['label', 'spacing', 'padding', 'weight', 'size'], Any]: ...

class Axis(_GridComponent, Iterable[Slot], Sized):
    """A collection of rows or columns.

    :vartype label: `str`
    :var label: Informal name for the axis.

    :vartype spacing: `float`
    :var spacing: Used as a fallback value to offset the slot's
        position during a draw event. Is ignored for calculations when NaN.

    :vartype padding: `_MutArray[float, Literal[2]]`
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
    @property
    def length(self, /) -> int: ...
    @length.setter
    def length(self, value: int, /) -> None: ...
    @property
    def weight(self, /) -> float:
        """[**get**] the total weight of all slots in the axis that are
        dynamically-size.
        """
    @property
    def size(self, /) -> int:
        """[**get**] the total size of all slots in the axis with a static
        size.
        """
    def __init__(self, /, length: int = ..., *, label: str = ..., spacing: float | None = ..., padding: Sequence[float] | float | None = ..., **kwargs) -> None: ...
    def configure(self, /, *, label: str = ..., spacing: float | None = ..., padding: Sequence[float] | float | None = ..., length: int = ..., **kwargs): ...
    def configuration(self, /) -> dict[Literal['label', 'spacing', 'padding', 'length'], Any]: ...
    def insert(self, index: SupportsIndex, /):
        """Adds a new slot (row/column) at the specified index.

        :type index: `SupportsIndex`
        :param index: Target slot index.
        """
    def remove(self, index: SupportsIndex = -1, /):
        """Delete the slot (row/column) at the specified index, or the last
        slot if not specified.

        :type index: `SupportsIndex`
        :param index: Target slot index.
        """
    def resize(self, length: int, /) -> Self:
        """Add/remove slots from the axis so that it contains the number
        of slots specified.

        :type length: `int`
        :param length: A positive number indicating the target length of
            the axis.
        """
    def __iadd__(self, n: int, /) -> Self:
        """Adds an additional *n* slots to the end of the axis."""
    def __isub__(self, n: int, /) -> Self:
        """Removes the last *n* slots from the end of the axis."""
    def __imul__(self, n: int, /) -> Self:
        """Multiply the number of slots in the axis by *n* (min. 1)."""
    def __ifloordiv__(self, n: int, /) -> Self:
        """Divide the number of slots in the axis by *n* (rounded down, min. 1).

        ***NOTE**: In-place division on :py:class:`Axis` objects is always floor
        division, regardless of the operator.*
        """
    __itruediv__ = __ifloordiv__
    def __str__(self, /) -> str: ...
    def __bool__(self, /) -> bool: ...
    def __getitem__(self, index: SupportsIndex, /) -> Slot: ...
    def __iter__(self, /) -> Iterator[Slot]: ...
    def __len__(self, /) -> int: ...
    def __int__(self, /) -> int: ...
    def __index__(self, /) -> int: ...
    def __trunc__(self, /) -> int: ...
    def __floor__(self, /) -> int: ...
    def __ceil__(self, /) -> int: ...
    def __abs__(self, /) -> int: ...
    def __float__(self, /) -> float: ...
    def __lt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: Any, /) -> bool: ...
    def __ne__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...
    def __pos__(self, /) -> int: ...
    def __neg__(self, /) -> int: ...
    def __add__(self, i: int, /) -> int: ...
    def __sub__(self, i: int, /) -> int: ...
    def __mul__(self, i: int, /) -> int: ...
    def __floordiv__(self, i: int, /) -> int: ...
    def __truediv__(self, i: int, /) -> int: ...
    def __mod__(self, i: int, /) -> int: ...
    def __divmod__(self, i: Any, /) -> tuple[int, int]: ...
    def __pow__(self, i: int, /, mod: int | None = None) -> int: ...

class Grid(_GridComponent):
    """Layout manager for DearPyGui, emulating a table-like structure.
    Calling the grid object or its :py:meth:`draw()` method calculates
    the geometry of items within the it (added via :py:meth:`push()`)
    and updates their sizes and positions based on the constraints of
    the slots (columns and rows) they occupy. The grid can be freely
    reshaped after creation.

    Grids have two dependencies: it needs a geometry reference, and must
    be told to update. The former is provided indirectly by the item set
    on :py:property:`parent`, or directly via the :py:property:`rect_getter`
    callable. When set, :py:property:`width` and/or :py:property:`height`
    override the respective values in the reference. The second requirement
    is best fulfilled by calling the grid object or :py:meth:`draw()` in the
    render loop, or by setting it as a "while visible" or "on resize"
    callback of the grid's geometry reference.
    ```python
    from dearpypixl.grid import Grid
    from dearpygui import dearpygui as dpg

    # initialize DearPyGui
    dpg.create_context()
    dpg.setup_dearpygui()
    dpg.create_viewport()


    with dpg.window() as window:
        button1 = dpg.add_button(label="Button 1")
        button2 = dpg.add_button(label="Button 1")

        # initializes the grid with 3 columns and 4 rows
        grid = Grid(3, 4, parent=window)

        # pack the item within a single cell (the first one)
        grid.push(button1, 0, 0)

        # pack the item within a range of cells — from the cell x1, y1 to
        # the last cell in the grid
        grid.push(button2, (1, 1), (-1, -1))

        # ensure the grid updates frequently
        with dpg.item_handler_registry() as handlers:
            dpg.add_item_resize_handler(callback=grid)

        dpg.bind_item_handler_registry(window, handlers)

    # the grid's dimensions can be updated at any time, even after adding items
    grid.cols = 5  # set the number of columns to 5 (adds 2 additional columns)
    assert len(grid.cols) == 5
    grid.rows -= 1  # reduce the number of rows by 1 (removes the last row)
    assert len(grid.rows) == 3

    # run the app
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    ```

    Grids are primarily composed of two other objects: :py:class:`Slot`s
    and :py:class:`Axis` objects. A :py:class:`Slot` represents an entire
    column or row, while :py:class:`Axis` objects are collections of
    :py:class:`Slot`s for a specific axis. A grid's x and y axes are
    exposed via :py:property:`cols` and :py:property:`rows`. :py:class:`Grid`,
    :py:class:`Axis`, and :py:class:`Slot` have a parent-child relationship
    — common settings are propegated down (this is element-wise for array-like
    settings) to their children, but the child setting is prioritized. For
    example, cell padding is composed of four values: left (`x1`), upper (`y1`),
    right (`x2`), and lower (`x2`). To determine the horizontal padding of
    cell `(0, 0)` given the code below:
    ```python

    grid = Grid(3, 4)

    # grid.padding == `[x1, y1, x2, y2]`
    grid.padding[0] = grid.padding[2] = 4

    # grid.cols.padding == `[x1, x2]`
    grid.cols.padding[0] = 8

    # grid.cols[0].padding == `[x1, x2]`
    grid.cols[0].padding[0] = 2
    ```
    ...`2` as the left value and `4` for the right. The slot containing the
    cell's horizontal padding only includes the left padding (while the right
    padding is NaN). Moving up to the axis, a left padding value is set but is
    ignored because the grid prioritized the child's value. Still without a
    value for the right padding, the grid falls back to using its own value of
    `4`.
    """
    ANCHORS: ClassVar[Collection[Literal[
        "c" "center",
        "n", "north",
        "ne", "northeast",
        "e",  "east",
        "se", "southeast",
        "s", "south",
        "sw", "southwest",
        "w",  "west",
        "nw", "northwest"
    ]]]
    def __init__(self, /, cols: int = 1, rows: int = 1, parent: Item | None = 0, *, label: str = "", padding: Sequence[float] | float | None = None, spacing: Sequence[float] | float | None = None, width: int | None = None, height: int | None = None, offsets: Sequence[float] | float | None = None, rect_getter: _RectGetter | None = None, overlay: bool = False, show: bool = True) -> None: ...
    @property
    def cols(self, /) -> Axis:
        """The :py:class:`Axis` object representing the grid's columns (x-axis)."""
    @cols.setter
    def cols(self, value: Axis | int, /) -> None: ...
    @property
    def rows(self, /) -> Axis:
        """The :py:class:`Axis` object representing the grid's rows (y-axis)."""
    @rows.setter
    def rows(self, value: Axis | int, /) -> None: ...
    @property
    def width(self, /) -> int:
        """[**get**, **set**] the horizontal size of the grid in pixels (min. 0).

        By default, the grid's size is determined based on the size of its
        :py:attr:`parent`. Setting a static height or width can be used to expand
        or shrink the size of the grid beyond or within the parent item's clipping
        area.
        """
    @width.setter
    def width(self, value: int | None, /) -> None: ...
    @property
    def height(self, /) -> int:
        """[**get**, **set**] the vertical size of the grid in pixels (min. 0).

        By default, the grid's size is determined based on the size of its
        :py:attr:`parent`. Setting a static height or width can be used to expand
        or shrink the size of the grid beyond or within the parent item's clipping
        area.
        """
    @height.setter
    def height(self, value: int | None, /) -> None: ...
    @property
    def show(self, /) -> bool:
        """[**get**, **set**] the grid's visibility state. Also affects the visibility
        of items managed by the grid.
        """
    @show.setter
    def show(self, value: bool, /) -> None: ...
    @property
    def overlay(self, /) -> bool:
        """[**get**, **set**] the visibility state of the grid's overlay. The overlay
        is a visual representation of the grid's "outline".
        """
    @overlay.setter
    def overlay(self, value: bool, /) -> None: ...
    @property
    def offsets(self, /) -> _MutArray[float, Literal[4]]:
        """[**get**, **set**, **del**] values used as the left, upper, right, and lower
        edges of the grid (similar to :py:property:`padding`, affects the grid itself
        and not its slots). Expands or shrinks the size of the grid's content region
        (min. 0 per value).
        """
    @offsets.setter
    def offsets(self, value: _Array[float, Literal[4]] | float | None, /) -> None: ...
    @offsets.deleter
    def offsets(self, /) -> None: ...
    @property
    def padding(self, /) -> _MutArray[float, Literal[4]]:
        """[**get**, **set**, **del**] values used as the left, upper, right, and lower
        padding values during a draw event when item-level padding override values were
        not provided and both `slot.spacing` and `axis.spacing` are not applicable. The
        first and third values are used for column padding, while the second and fourth
        values are used for rows (min. 0 per value).
        """
    @padding.setter
    def padding(self, value: _Array[float, Literal[4]] | float | None, /) -> None: ...
    @padding.deleter
    def padding(self, /) -> None: ...
    @property
    def spacing(self, /) -> _MutArray[float, Literal[2]]:
        """[**get**, **set**, **del**] values used to offset a slot's (columns and
        rows, respectively) position during a draw event when both `slot.spacing`
        and `axis.spacing` are not applicable (min. 0 per value).
        """
    @spacing.setter
    def spacing(self, value: _Array[float, Literal[2]] | float | None, /) -> None: ...
    @spacing.deleter
    def spacing(self, /) -> None: ...
    @property
    def parent(self, /) -> Item | None:
        """[**get**, **set**] the grid's reference item. The position, size, and
        visibility state of the grid reflects the position, size, and visibility of
        this item.

        If :py:property:`parent` is `None`, :py:property:`rect_getter` **cannot**
        be `None`.
        """
    @parent.setter
    def parent(self, value: Item | None, /) -> None: ...
    @property
    def rect_getter(self, /) -> _RectGetter | None:
        """[**get**, **set**] the callable used to query the geometry and visibility
        status of :py:property:`parent`.

        When `None`, a light wrapper around `dearpygui.get_item_state()` is used to
        fetch the geometry and visibility of :py:property:`parent`. Otherwise, the
        set callable must accept :py:property:`parent` and return a 5-tuple containing
        the width, height, x-position, y-position, and visibility state to use for the
        grid. Depending on the implementation of the callable, :py:property:`parent`
        may not be necessary and can be set to `None`.
        """
    @rect_getter.setter
    def rect_getter(self, value: _RectGetter | None, /) -> None: ...
    @overload
    def configure(self, /, *, cols: int = ..., rows: int = ..., parent: Item | None = ..., label: str | None = ..., padding: Sequence[float] | float | None = ..., spacing: Sequence[float] | float | None = ..., width: float | None = ..., height: float | None = ..., offsets: Sequence[float] | float | None = ..., rect_getter: _RectGetter | None = ..., overlay: bool = ..., show: bool = ..., **kwargs) -> None: ...
    @overload
    def configure(self, **kwargs): ...
    def configuration(self, /): ...
    @overload
    def push(self, item: Item, col: int, row: int, /, *, anchor: str = ..., max_size: _Array[float, Literal[2]] | float | None = ..., padding: _Array[float, Literal[4]] | float | None = ..., rect_setter: _RectSetter | None = ...):
        """Attach an item to the grid, positioning it within a specific cell.

        Awaits internal lock release.

        :type item: `int | str`
        :param item: Item identifier to push. The item must have geometry
            (*width*, *height*, and *pos*) and support the *show* configuration
            option.

        :type col: `int`
        :param col: The column which *item* will occupy as a zero-index.

        :type row: `int`
        :param row: The row which *item* will occupy as a zero-index.

        :type anchor: `str`
        :param anchor: A case-insensitive compass direction name or abbreviation
            indicating which side(s) of the cell the item will "stick" to e.g.
            `"north"`, `"ne"` (northeast), "southwest", etc. The default value
            `"center"` (or `"c"`) centers the item horizontally and vertically
            within its cellspan. Defaults to `"center"`.

        :type max_size: `Array[int, Literal[2]] | int | None`
        :param max_size: The upper limits for the item's width and height in pixels.
            The actual size limits used is determined using *max_size* or the cell(span)'s
            maximum content region (whichever is smaller). Value(s) less than `1` are
            treated as `None`. Single, non-iterable values are used for both width
            and height e.g. `4 -> [4, 4]`, `None -> [None, None]`, etc. Defaults to
            `None`.

        :type padding: `Array[float, Literal[4]] | float | None`
        :param padding: Left, upper, right, and lower padding values in fractional
            pixels, overriding :py:class:`Slot` and :py:class:`Axis` padding when
            sizing and positioning the item. `None` and NaN value(s) indicate "no
            overriding value". Single, non-iterable values are used for all padding
            values e.g. `None | NaN -> [NaN, NaN, NaN, NaN]`, `2.5 -> [2.5, 2.5,
            2.5, 2.5]`, etc. Defaults to `None`.

        :type rect_setter: `Callable[[int | str, int, int, int, int, bool]] | None`
        :param rect_setter: A callable responsible for applying the final geometry
            values and visibility status for *item* in DearPyGui when drawing the
            grid. It must accept five positional arguments: *item*, x-position,
            y-position, width, height, and visible state. The default implementation
            is a simple wrapper around `dearpygui.configure_item()`. Defaults to
            `None`.

        The item's cell coordinates are not made "final" when pushing the item, but
        are re-calculated whenever the grid is drawn. Since the grid's dimensions
        can can be freely updated between draws, this leads to some beneficial
        (but possibly surprising) runtime behavior. Final cell coordinates are
        determined using the provided indices on Python sequences. This means the
        exact slot(s) used may not always be the same between draws e.g. `(-1, -1)`
        resolves to the last column and row at the time the grid is drawn. This
        also means it's possible for a cellspan to become "out-of-range" when the
        number of slots in the grid is reduced. The item is hidden if one or more
        cells in the cellspan are missing or hidden, or if the content region of
        the cell or cellspan is too small when drawing the grid.
        """
    @overload
    def push(self, item: Item, cell: tuple[int, int], /, *, anchor: str = ..., max_size: _Array[float, Literal[2]] | float | None = ..., padding: _Array[float, Literal[4]] | float | None = ..., rect_setter: _RectSetter | None = ...):
        """Attach an item to the grid, positioning it within a specific cell.

        :type item: `int | str`
        :param item: Item identifier to push. The item must have geometry
            (*width*, *height*, and *pos*) and support the *show* configuration
            option.

        :type cell: `tuple[int, int]`
        :param cell: The cell which *item* will occupy as zero-index coordinates
            `(row, column)`.

        :type anchor: `str`
        :param anchor: A case-insensitive compass direction name or abbreviation
            indicating which side(s) of the cell the item will "stick" to e.g.
            `"north"`, `"ne"` (northeast), "southwest", etc. The default value
            `"center"` (or `"c"`) centers the item horizontally and vertically
            within its cellspan. Defaults to `"center"`.

        :type max_size: `Array[int, Literal[2]] | int | None`
        :param max_size: The upper limits for the item's width and height in pixels.
            The actual size limits used is determined using *max_size* or the cell(span)'s
            maximum content region (whichever is smaller). Value(s) less than `1` are
            treated as `None`. Single, non-iterable values are used for both width
            and height e.g. `4 -> [4, 4]`, `None -> [None, None]`, etc. Defaults to
            `None`.

        :type padding: `Array[float, Literal[4]] | float | None`
        :param padding: Left, upper, right, and lower padding values in fractional
            pixels, overriding :py:class:`Slot` and :py:class:`Axis` padding when
            sizing and positioning the item. `None` and NaN value(s) indicate "no
            overriding value". Single, non-iterable values are used for all padding
            values e.g. `None | NaN -> [NaN, NaN, NaN, NaN]`, `2.5 -> [2.5, 2.5,
            2.5, 2.5]`, etc. Defaults to `None`.

        :type rect_setter: `Callable[[int | str, int, int, int, int, bool]] | None`
        :param rect_setter: A callable responsible for applying the final geometry
            values and visibility status for *item* in DearPyGui when drawing the
            grid. It must accept five positional arguments: *item*, x-position,
            y-position, width, height, and visible state. The default implementation
            is a simple wrapper around `dearpygui.configure_item()`. Defaults to
            `None`.

        The item's cell coordinates are not made "final" when pushing the item, but
        are re-calculated whenever the grid is drawn. Since the grid's dimensions
        can can be freely updated between draws, this leads to some beneficial
        (but possibly surprising) runtime behavior. Final cell coordinates are
        determined using the provided indices on Python sequences. This means the
        exact slot(s) used may not always be the same between draws e.g. `(-1, -1)`
        resolves to the last column and row at the time the grid is drawn. This
        also means it's possible for a cellspan to become "out-of-range" when the
        number of slots in the grid is reduced. The item is hidden if one or more
        cells in the cellspan are missing or hidden, or if the content region of
        the cell or cellspan is too small when drawing the grid.
        """
    @overload
    def push(self, item: Item, cell_start: tuple[int, int], cell_stop: tuple[int, int], /, *, anchor: str = ..., max_size: _Array[float, Literal[2]] | float | None = ..., padding: _Array[float, Literal[4]] | float | None = ..., rect_setter: _RectSetter | None = ...):
        """Attach an item to the grid, positioning it within a range of cells.

        :type item: `int | str`
        :param item: Item identifier to push. The item must have geometry
            (*width*, *height*, and *pos*) and support the *show* configuration
            option.

        :type cell_start: `tuple[int, int]`
        :param cell_start: The first cell in a range of cells which *item* will occupy
            as zero-index coordinates `(row, column)`.

        :type cell_stop: `tuple[int, int]`
        :param cell_stop: The last cell in a range of cells which *item* will occupy
            as zero-index coordinates `(row, column)`.

        :type anchor: `str`
        :param anchor: A case-insensitive compass direction name or abbreviation
            indicating which side(s) of the cell the item will "stick" to e.g.
            `"north"`, `"ne"` (northeast), "southwest", etc. The default value
            `"center"` (or `"c"`) centers the item horizontally and vertically
            within its cellspan. Defaults to `"center"`.

        :type max_size: `Array[int, Literal[2]] | int | None`
        :param max_size: The upper limits for the item's width and height in pixels.
            The actual size limits used is determined using *max_size* or the cell(span)'s
            maximum content region (whichever is smaller). Value(s) less than `1` are
            treated as `None`. Single, non-iterable values are used for both width
            and height e.g. `4 -> [4, 4]`, `None -> [None, None]`, etc. Defaults to
            `None`.

        :type padding: `Array[float, Literal[4]] | float | None`
        :param padding: Left, upper, right, and lower padding values in fractional
            pixels, overriding :py:class:`Slot` and :py:class:`Axis` padding when
            sizing and positioning the item. `None` and NaN value(s) indicate "no
            overriding value". Single, non-iterable values are used for all padding
            values e.g. `None | NaN -> [NaN, NaN, NaN, NaN]`, `2.5 -> [2.5, 2.5,
            2.5, 2.5]`, etc. Defaults to `None`.

        :type rect_setter: `Callable[[int | str, int, int, int, int, bool]] | None`
        :param rect_setter: A callable responsible for applying the final geometry
            values and visibility status for *item* in DearPyGui when drawing the
            grid. It must accept five positional arguments: *item*, x-position,
            y-position, width, height, and visible state. The default implementation
            is a simple wrapper around `dearpygui.configure_item()`. Defaults to
            `None`.

        The item's cell coordinates are not made "final" when pushing the item, but
        are re-calculated whenever the grid is drawn. Since the grid's dimensions
        can can be freely updated between draws, this leads to some beneficial
        (but possibly surprising) runtime behavior. Final cell coordinates are
        determined using the provided indices on Python sequences. This means the
        exact slot(s) used may not always be the same between draws e.g. `(-1, -1)`
        resolves to the last column and row at the time the grid is drawn. This
        also means it's possible for a cellspan to become "out-of-range" when the
        number of slots in the grid is reduced. The item is hidden if one or more
        cells in the cellspan are missing or hidden, or if the content region of
        the cell or cellspan is too small when drawing the grid.
        """
    def pop(self, item: Item, /) -> None:
        """Releases an item from the grid. Does not raise an error if the item
        is missing or does not exist.

        Awaits internal lock release.

        :type item: `Item`
        :param item: Item to remove from the grid.
        """
    def clear(self, /) -> None:
        """Release all items from the grid.

        Awaits internal lock release.
        """
    def draw(self, /) -> None:
        """Draw the grid, updating the size and position of any item attached.

        Awaits internal lock release.
        """
    __call__ = draw
    __code__: types.CodeType


class Overlay:
    @overload
    def draw(self, /) -> None: ...
    @overload
    def draw(self, x_min: int, y_min: int, x_max: int, y_max: int, /) -> None: ...
