"""Grid-layout manager for Dear PyPixl and Dear PyGui."""
import types
from dearpygui._dearpygui import (  # using the "raw" API to help w/performance in some places
    get_item_state as _get_item_state,
    get_item_configuration as _get_item_size,
    get_viewport_configuration as _get_viewport_size,
    configure_item as _set_item_size,
)
from ._typing import (
    Item,

    Any,
    Array,
    Self,
    NamedTuple,
    Protocol,
    Callable,
    Literal,
    Mapping,
    Generic,
    Iterator,
    Collection,
    overload,

    TypeVar,
)
from .api import Registry as RegistryAPI


# TODO: add thread lock


Rect = Array[float, float, float, float]  # width, height, x_pos, y_pos




####################################################
########### ITEMSIZE GET/SET FUNCTIONS #############
####################################################

class FGetSize(Protocol):
    """A function that returns the size of an item."""
    def __call__(self, item: Item) -> tuple[int, int]: ...

def size_from_size(item: Item) -> tuple[int, int]:
    cfg = _get_item_size(item)
    return cfg["width"], cfg["height"]

def size_from_rect(item: Item) -> tuple[int, int]:
    return _get_item_state(item)["rect_size"]

def size_from_viewport(item: Any = None) -> tuple[int, int]:
    cfg = _get_viewport_size("DPG NOT USED YET")
    return cfg['width'], cfg['height']


class FSetSize(Protocol):
    """A function that sets the size and position of an item."""
    def __call__(self, item: Item, *, width: int, height: int, pos: Array[int, int]) -> Any: ...




####################################################
###### ANCHORS & ANCHOR SIZE/POS CALCULATORS #######
####################################################

_ANCHOR_MAP = {}


class FAnchor(Protocol):
    def __call__(self, item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float, /) -> tuple[int, int]: ...


def _register_anchors(*anchor: str) -> Callable[[FAnchor], FAnchor]:
    def register_anchor_fn(fn: FAnchor) -> FAnchor:
        for s in anchor:
            _ANCHOR_MAP[s.lower()] = fn  # type: ignore
        return fn
    return register_anchor_fn


@_register_anchors("n", "north")
def _calc_anchor_N(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int(cell_y)  # center x

@_register_anchors("ne", "northeast")
def _calc_anchor_NE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) + cell_x), int(cell_y)

@_register_anchors("e", "east")
def _calc_anchor_E(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) + cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center y

@_register_anchors("se", "southeast")
def _calc_anchor_SE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt)     + cell_x), int((cell_ht - item_ht)     + cell_y)

@_register_anchors("s", "south")
def _calc_anchor_S(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int((cell_ht - item_ht)     + cell_y)  # center x

@_register_anchors("sw", "southwest")
def _calc_anchor_SW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int((cell_ht - item_ht) + cell_y)

@_register_anchors("w", "west")
def _calc_anchor_W(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center y

@_register_anchors("nw", "northwest")
def _calc_anchor_NW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int(cell_y)

@_register_anchors("c", "center")
def _calc_anchor_C(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center x & y



_ANCHOR_MAP: Mapping[str, FAnchor] = types.MappingProxyType(_ANCHOR_MAP)




####################################################
########### MISC TYPES/HELPER FUNCTIONS ############
####################################################

# These are decoupled from `Grid` to make it easier to monkeypatch
# in more performant alternatives later.

def normalize_cellspan(r1: int, c1: int, r2: int, c2: int, rows: int, cols: int):
    """Corrects backwards/reversed start-stop slot ranges and returns the positive
    indexes of a cellspan.

    Args:
        * r1: A positive or negative integer representing the index of the starting
        row of the cellspan. Its' absolute value should be within `range(rows)`.

        * c1: A positive or negative integer representing the index of the starting
        column of the cellspan. Its' absolute value should be within `range(cols)`.

        * r2: A positive or negative integer representing the index of the ending
        row of the cellspan. Its' absolute value should be within `range(rows)`.

        * c2: A positive or negative integer representing the index of the ending
        column of the cellspan. Its' absolute value should be within `range(cols)`.

        * rows: The total number of rows.

        * cols: The total number of columns.
    """
    r1 %= rows
    c1 %= cols
    r2 %= rows
    c2 %= cols
    if r1 > r2:
        r1, r2 = r2, r1
    if c1 > c2:
        c1, c2 = c2, c1
    return r1, c1, r2, c2


def draw_cells(
    rect_size: tuple[int, int],
    rect_pad : tuple[float, float, float, float],
    cell_pad : tuple[float, float, float, float],
    x_axis   : 'GridAxis',
    y_axis   : 'GridAxis',
) -> dict[tuple[int, int], tuple[float, ...]]:
    """Args:
        * rect_size: Width and height of the grid's parent/target.

        * rect_pad: The amount of whitespace (in pixels) between the grid's
        parent/target and the outer-most cells, as `(left, right, upper, lower)`.

        * cell_pad: The amount of whitespace (in pixels) between cells, as
        `(left, right, upper, lower)`.

        * x_axis: `GridAxis` object containing horizontal slot settings.

        * y_axis: `GridAxis` object containing vertical slot settings.
    """
    rect_x1_pad = rect_pad[0]
    rect_y1_pad = rect_pad[2]
    rect_wt     = rect_size[1] - rect_y1_pad - rect_pad[3]
    rect_ht     = rect_size[0] - rect_x1_pad - rect_pad[1]

    weight_wt = max(0, (rect_ht - y_axis.min_size)) / max(1, y_axis.weight)  # `max(1, ...)` prevents `ZeroDivisionError`
    weight_ht = max(0, (rect_wt - x_axis.min_size)) / max(1, x_axis.weight)

    # The size of each cell is calculated using half of each padding
    # value; two cells side-by-side have the "full" amount of padding
    # between them.
    cell_x1_pad = cell_pad[0] / 2
    cell_y1_pad = cell_pad[2] / 2
    cell_x_pad  = cell_x1_pad + (cell_pad[1] / 2.0)
    cell_y_pad  = cell_y1_pad + (cell_pad[3] / 2.0)

    cell_map = {}
    alloc_ht = 0.0

    rows = x_axis._members
    cols = [*enumerate(y_axis._members)]  # iterated over many times, unlike `rows`
    for row, row_cfg in enumerate(rows):
        # calculate each cell's vertical rect
        row_ht     = row_cfg.size or weight_ht * row_cfg.weight  # FIXED or SIZED policy
        cell_y_pos = rect_y1_pad + alloc_ht + cell_y1_pad
        cell_ht    = row_ht - cell_y_pad
        alloc_wt   = 0.0
        for col, col_cfg in cols:
            # calculate each cell's horizontal rect
            col_wt     = col_cfg.size or weight_wt * col_cfg.weight  # FIXED or SIZED policy
            cell_x_pos = rect_x1_pad + alloc_wt + cell_x1_pad
            cell_wt   = col_wt - cell_x_pad
            alloc_wt += col_wt
            cell_map[(row, col)] = (
                cell_x_pos,
                cell_y_pos,
                cell_wt,
                cell_ht,
            )
        alloc_ht += row_ht
    return cell_map


def redraw_grid(grid: 'Grid', *args):
    """Update the position and size of items managed by the grid."""
    cells = draw_cells(
        grid._sizer(grid._parent),
        grid._padding,
        grid._spacing,
        grid._rows,
        grid._cols,
    )
    row_len = len(grid._rows)
    col_len = len(grid._cols)
    del_items = None
    for item, coords1, coords2, item_width, item_height, anchor, size_setter, in grid._members.values():
        r1, c1, r2, c2 = normalize_cellspan(*coords1, *coords2, row_len, col_len)
        x_pos , y_pos , width1, height1 = cells[(r1, c1)]
        x_offs, y_offs, width2, height2 = cells[(r2, c2)]
        # fix offset when drawing over a cell range
        cell_width  = x_offs + width2  - x_pos
        cell_height = y_offs + height2 - y_pos
        # itemsize must conform to the cell space
        if not item_width or item_width > cell_width:
            item_width = cell_width
        if not item_height or item_height > cell_height:
            item_height = cell_height
        try:
            size_setter(
                item,
                pos=anchor(item_width, item_height, x_pos, y_pos, cell_width, cell_height),
                # BUG: DPG parses integers as unsigned longs, so a
                # negative value would actually make the item larger.
                width=max(int(item_width), 1),
                height=max(int(item_height), 1),
            )
        except SystemError:
            if not RegistryAPI.item_exists(item):
                if not del_items:
                    del_items = []
                del_items.append(item)
            else:
                raise
    if del_items:
        for item in del_items:
            grid.pop(item)




####################################################
############# GRID & GRID DEPENDENCIES #############
####################################################

_GT = TypeVar("_GT")
_ST = TypeVar("_ST")

class GridConfigure(Generic[_GT, _ST]):
    __slots__ = ("_get_eval", "_set_eval")

    def __set_name__(self, cls, name: str):
        self._get_eval = compile(f"instance._{name}", __name__, mode="eval")
        self._set_eval = compile(f"instance.configure({name}=value)", __name__, mode="exec")

    def __get__(self, instance, cls) -> _GT:
        if instance is None:
            return self  # type: ignore
        return eval(self._get_eval)

    def __set__(self, instance, value: _ST) -> None:
        exec(self._set_eval)


class GridMember(NamedTuple):
    item     : Item
    cell1    : tuple[int, int]
    cell2    : tuple[int, int]
    max_wt   : int
    max_ht   : int
    anchor   : FAnchor
    fset_size: Callable = _set_item_size


class GridOffset(NamedTuple):
    """Contains Grid padding or spacing values.

    Args:
        * x1: Horizontal offset from the left. Default is 0.

        * x1: Horizontal offset from the right. Default is 0.

        * y1: Vertical offset from the top. Default is 0.

        * y2: Vertical offset from the bottom. Default is 0.
    """
    x1: int = 0
    x2: int = 0
    y1: int = 0
    y2: int = 0

    @classmethod
    def new(cls, x: int | tuple[int, int], y: int | tuple[int, int], /) -> Self:
        """
        Args:
            * x: A single value to use as both x1 and x2 values, or a 2-tuple containing
            individual values for x1 and x2 respectively.

            * y: A single value to use as both y1 and y2 values, or a 2-tuple containing
            individual values for y1 and y2 respectively.
        """
        if isinstance(x, (int, float)):
            x = x, x
        if isinstance(y, (int, float)):
            y = y, y
        return cls(*x, *y)

    @property
    def x(self):
        return self[:2]

    @property
    def y(self):
        return self[2:]


class GridSlot:
    """A Grid row or column."""

    __slots__ = ("_weight", "_size", "label")

    FIXED = "fixed"
    SIZED = "sized"

    def __init__(self, label: str = ''):
        self.label   = label
        self._weight = 1.0
        self._size   = 0

    def __repr__(self):
        return f"{type(self).__qualname__}(label={self.label!r}, weight={self.weight}, size={self.size})"

    weight: GridConfigure[float, float] = GridConfigure()
    size  : GridConfigure[int, int]     = GridConfigure()

    @property
    def policy(self) -> Literal["fixed", "sized"]:
        return self.FIXED if self.size else self.SIZED

    @overload
    def configure(self, *, weight: float = ..., size: int = ...) -> None: ...  # type: ignore
    def configure(self, *, weight: Any = None, size: int | None = None) -> None:
        if weight is not None:
            self._weight = max(0, weight)
        if size is not None:
            self._size = max(0, size)


class GridAxis(Collection[GridSlot]):
    """A collection of Grid slots of a single axis."""

    __slots__ = ("_members", 'label',)

    _members: list[GridSlot]

    def __init__(self, length : int = 0, label: str = '') -> None:
        self.label    = label
        self._members = []
        self.resize(length)

    def __str__(self):
        return str(self._members)

    def __repr__(self):
        return f"{type(self).__qualname__}({str(self).strip('[]')})"

    def __len__(self):
        return len(self._members)

    def __int__(self):
        return len(self._members)

    def __iter__(self) -> Iterator[GridSlot]:
        yield from self._members

    def __getitem__(self, index: int) -> GridSlot:
        return self._members[index]

    def __contains__(self, other: Any) -> bool:
        return other in self._members

    def __add__(self, value: int) -> Self:
        self._members.extend(GridSlot(self.label) for _ in range(value))
        return self

    def __sub__(self, value: int) -> Self:
        if value > 0:
            del self._members[-value:]
        return self

    @property
    def weight(self) -> float:
        # ignore weight of fixed-size slots
        return sum(slot._weight for slot in self._members if not slot._size)

    @property
    def min_size(self) -> int:
        return sum(slot._size for slot in self._members)

    def insert(self, index: int, *args) -> None:
        """Insert a new row/column somewhere in the axis. The indexes of rows/columns
        trailing the point of insertion will be offset by 1.

        Args:
            * index: Specifies the position to insert the new row or column.
        """
        self._members.insert(index, GridSlot(self.label))

    def delete(self, index: int) -> None:
        self._members.pop(index)

    def resize(self, amount: int) -> None:
        """Update the size of the axis.

        Args:
            * amount: Integer specifying the amount of rows/columns to add or remove. A
            positive value will add that many additional rows/columns, while a negative
            value will remove that many from the end of the axis.
        """
        if amount >= 0:
            self._members.extend(GridSlot(self.label) for _ in range(amount))
        else:
            del self._members[-amount:]


class Grid:
    """A grid-layout manager for items.
        >>> import random
        >>> import dearpygui.dearpygui as dpg
        >>>
        >>>
        >>> def bind_button_theme(item: int | str):
        ...     rgb  = random.randint(0, 255), randint(0, 255), randint(0, 255)
        ...     with dpg.theme() as theme:
        ...         with dpg.theme_component(0):
        ...             dpg.add_theme_color(dpg.mvThemeCol_Button, [*rgb, 80])
        ...             dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [*rgb, 255])
        ...     dpg.bind_item_theme(item, theme)
        >>>
        >>> def create_button() -> int | str:
        ...     item = dpg.add_button(label=tag, tag=tag)
        ...     bind_button_theme(item)
        ...     return item
        >>>
        >>>
        >>>    dpg.create_context()
        >>>    dpg.create_viewport(title="Grid Demo", width=1000, height=1000, min_height=10, min_width=10)
        >>>    dpg.setup_dearpygui()
        >>>
        >>>    with dpg.window(no_scrollbar=True, no_background=True) as win:
        ...        grid = Grid(6, 6, padding=((10, 30), 8), spacing=(0, 0))
        ...
        ...        # Without additional arguments, items will expand and shrink to the cell's size.
        ...        grid.push(create_button(),  0,  2)  # first row
        ...        grid.push(create_button(), -1,  3)  # last row
        ...
        ...        # You can clamp an item's width/height and include an alignment option. A few
        ...        # valid anchor options are 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', and 'c'.
        ...        grid.push(create_button(), 1, 1, max_height=25, anchor="w")      # west anchor
        ...        grid.push(create_button(), 1, 1, max_width=25, anchor="north")   # north anchor
        ...        grid.push(create_button(), 4, 4, max_height=25, anchor="w")
        ...
        ...        # These items will occupy a range of cells.
        ...        grid.push(create_button(),  3,  1,  4,  2)
        ...        grid.push(create_button(),  1,  3,  2,  4)
        ...        grid.push(create_button(),  4,  0, -1,  1)
        ...        grid.push(create_button(),  0,  4,  1, -1)
        ...
        ...        for anchor in grid.ANCHORS:
        ...            kwargs = dict(max_width=50, max_height=50, anchor=anchor)
        ...            # pack to individual cells (cont.)
        ...            grid.push(create_button(),  0,  0, **kwargs)  # first row & column
        ...            grid.push(create_button(), -1, -1, **kwargs)  # last row & column
        ...            # pack to a "merged cell" (cont.)
        ...            grid.push(create_button(),  2,  2,  3,  3, **kwargs)
        ...
        ...        # You can change the weight or set a fixed size for a row/column.
        ...        grid.cols[2].weight = 0.5
        ...        grid.cols[3].weight = 0.5
        ...        grid.rows[2].weight = 0.5
        ...        grid.rows[3].weight = 0.5
        >>>
        >>> dpg.set_primary_window(win, True)
        >>> dpg.show_viewport()
        >>> dpg.set_viewport_resize_callback(grid)
        >>>
        >>> while dpg.is_dearpygui_running():
        ...     dpg.render_dearpygui_frame()
    """
    __slots__ = (
        "_rows",
        "_cols",
        "_padding",
        "_spacing",
        "_parent",
        "_sizer",
        "_members",
        "members",
    )

    def __init_subclass__(cls) -> None:
        # if __call__ is redefined, ensure that DearPyGui can still call it
        if "__call__" in cls.__dict__ and "__code__" not in cls.__dict__:
            cls.__dict__["__code__"] = cls.__call__.__code__

    def __init__(
        self,
        rows: int = 1,
        cols: int = 1,
        *,
        spacing: tuple[int | tuple[int, int], int | tuple[int, int]] = (0, 0),
        padding: tuple[int | tuple[int, int], int | tuple[int, int]] = (0, 0),
        parent : Item                                                =      0,
        sizer  : FGetSize                                            = size_from_rect,
    ):
        """Args:
            * rows: The initial number of virtual rows in the grid (min. 1).

            * cols: The initial number of virtual columns in the grid (min. 1).

            * spacing: Horizontal and vertical padding between cells.

            * padding: Horizontal and vertical padding between outer cells and the
            parent/target item's walls.

            * parent: Reference to an existing item or viewport. The width and
            height of the grid will scale to the parent's size.

            * sizer: A function that accepts *parent* as a positional argument
            and returns a 2-item sequence containing its' width and height.

        The first value of the *spacing* and *padding* arguments horizontal
        spacing/padding, while the second affects vertical spacing/padding. When
        the value is a number, it is used for both the left/upper-most and
        right/lower-most spacing (for horizontal and vertical respectively).
        Alternatively, the value can be a 2-item sequence of integers; the first
        integer will be used for the left/upper-most spacing while the second is
        used for the right/lower-most. For example, `spacing=(4, (2, 6))` will
        expand to `spacing=((4, 4), (2, 6))` automatically.

        If specified, the *parent* argument must be a reference to an existing
        item. Otherwise, it will automatically use the item on top of the
        container stack as the parent. You can also pass the viewport identifier,
        "DPG NOT USED YET", to specify the viewport. However, you must specify
        the correct sizer for it (i.e. *sizer=size_from_viewport*).

        """
        self._rows = GridAxis(rows, 'y')
        self._cols = GridAxis(cols, 'x')
        self._members: dict[Item, GridMember] = {}
        self.members = types.MappingProxyType(self._members)
        self.configure(spacing=spacing, padding=padding, parent=parent, sizer=sizer)

    __call__ = redraw_grid
    __code__ = __call__.__code__  # enables use as a direct DPG callback

    def __setitem__(self, coords: tuple[int, int] | tuple[int, int, int, int], item: Item, *, _anchor: str = "c"):
        """Pack and center an item into a grid cell or cell range."""
        self.push(item, *coords, anchor=_anchor)

    @property
    def rows(self) -> GridAxis:
        return self._rows
    @rows.setter
    def rows(self, value: int | GridAxis) -> None:
        if self._rows != value:  # self.rows += 1 -> self.rows.__set__(self, (self._rows + 1))
            self.configure(rows=value)  # type: ignore

    @property
    def cols(self) -> GridAxis:
        return self._cols
    @cols.setter
    def cols(self, value: int | GridAxis) -> None:
        if self._cols != value:  # self.cols += 1 -> self.cols.__set__(self, (self._cols + 1))
            self.configure(cols=value)  # type: ignore

    padding: GridConfigure[GridOffset, tuple[int | tuple[int, int], int | tuple[int, int]]] = GridConfigure()
    spacing: GridConfigure[GridOffset, tuple[int | tuple[int, int], int | tuple[int, int]]] = GridConfigure()

    parent : GridConfigure[Item  , Item  ]     = GridConfigure()
    sizer  : GridConfigure[FGetSize, FGetSize] = GridConfigure()

    ANCHORS = tuple(a.lower() for a in _ANCHOR_MAP)

    def configure(
        self,
        *,
        rows   : int = 0,
        cols   : int = 0,
        spacing: tuple[int | tuple[int, int], int | tuple[int, int]] | None = None,
        padding: tuple[int | tuple[int, int], int | tuple[int, int]] | None = None,
        parent : Item | None = None,
        sizer  : FGetSize | None = None,
    ):
        if rows > 0:
            self._rows.resize(rows - len(self.rows))
        if cols > 0:
            self._cols.resize(cols - len(self.cols))
        if spacing:
            self._spacing = GridOffset.new(*spacing)
        if padding:
            self._padding = GridOffset.new(*padding)
        if parent is not None:
            # emulate auto-parenting similar to DearPyGui
            if not parent and not (parent:=RegistryAPI.top_stack_item()):
                raise ValueError("requires parent (container stack is empty).")
            self._parent = parent
        if sizer:
            self._sizer = sizer

    @overload
    def push(self, item: Item, row: int, col: int, /, *, max_width: int = ..., max_height: int = ..., anchor: str = ..., normalize_indexes: bool = ...) -> None: ...
    @overload
    def push(self, item: Item, row_start: int, col_start: int, row_stop: int, col_stop: int, /, *, max_width: int = ..., max_height: int = ..., anchor: str = ..., normalize_indexes: bool = ...) -> None: ...
    def push(self, item: Item, r1: int, c1: int, r2: Any = None, c2: Any = None, /, *, max_width : int = 0, max_height: int = 0, anchor: str = "c", normalize_indexes: bool = False) -> None:
        """Attach an item to the grid. It will be managed until the item is deleted or
        is released from the grid via the `.pop` or `.clear` methods.

        Args:
            * item: Reference to an existing item.

            * row, row_start: The index of the row to place the item into. If *row_stop*
            is specified, this is the starting row index.

            * col, col_start: The index of the column to place the item into. If *col_stop*
            is specified, this is the starting column index.

            * row_stop: The index of the last row to place the item into.

            * col_stop: The index of the last column to place the item into.

            * max_width: Clamps the horizontal size (in pixels) of the item.

            * max_height: Clamps the vertical size (in pixels) of the item.

            * anchor: A case-insensitive string value specifying the cell wall(s) that
            will anchor the item in place. Appropriate values consist of any cardinal
            direction name or abbreviation ("north", "n", "southeast", "se", etc)
            and "center" (abbrv. as "c").

            * normalize_indexes: If True, converts any negative indexes to positive.
            False (default) preserves the original indexes.

        """
        # ensure item is currently valid
        if not RegistryAPI.item_exists(item):
            raise TypeError(f"`item` {item!r} does not exist.")
        # ensure coords are currently valid (XXX coords can become invalid as the number of slots change)
        try:
            self._rows[r1]
            self._rows[c1]
            self._cols[r2 or 0]
            self._cols[c2 or 0]
        except IndexError:
            raise IndexError("index(s) outside of grid range.") from None
        if r2 is None or c2 is None:
            # pushing to single cell
            r2, c2 = r1, c1
        if normalize_indexes:
            r1, c1, r2, c2 = normalize_cellspan(r1, c1, r2, c2, len(self._rows), len(self._cols))
        # get anchor calculator
        try:
            anchor_fn = _ANCHOR_MAP[anchor.lower()]
        except TypeError:
            raise TypeError(
                f"`anchor` expected as a str, (got {type(anchor)})."
            ) from None
        except KeyError:
            raise ValueError(
                f"invalid `anchor` argument {anchor!r}, try {', '.join(f'{a!r}' for a in self.ANCHORS)}."
            ) from None
        self._members[item] = GridMember(item, (r1, c1), (r2, c2), max(max_width, 0), max(max_height, 0), anchor_fn)

    def pop(self, item: Any):
        """Release an item from the grid."""
        return self._members.pop(item, None)

    def clear(self):
        """Release all items from the grid."""
        self._members.clear()

