import types
from typing import Self, TypeVar, NamedTuple, Protocol, Callable, Literal, Generic, overload, Iterator, Any, Collection
from dearpygui import dearpygui, _dearpygui
from dearpygui._dearpygui import (
    get_item_state as _get_item_state,
    get_item_configuration as _get_item_size,
    configure_item as _set_item_size,
)


dearpygui.create_context()



ItemId = int | str



####################################################
########### ITEMSIZE GET/SET FUNCTIONS #############
####################################################

class SizerT(Protocol):
    def __call__(self, item: ItemId) -> tuple[int, int]: ...

def size_from_size(item: ItemId) -> tuple[int, int]:
    cfg = _get_item_size(item)
    return cfg["width"], cfg["height"]

def size_from_rect(item: ItemId) -> tuple[int, int]:
    return _get_item_state(item)["rect_size"]




####################################################
###### ANCHORS & ANCHOR SIZE/POS CALCULATORS #######
####################################################

_ANCHOR_MAP: dict[str, '_AnchorCalcT'] = {}


class _AnchorCalcT(Protocol):
    def __call__(self, item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]: ...


def _new_anchor(*anchor: str) -> Callable[[_AnchorCalcT], _AnchorCalcT]:
    def register_anchor_fn(fn: _AnchorCalcT) -> _AnchorCalcT:
        for s in anchor:
            _ANCHOR_MAP[s.lower()] = fn
        return fn
    return register_anchor_fn


@_new_anchor("n", "north")
def _calc_anchor_N(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int(cell_y)  # center x

@_new_anchor("ne", "northeast")
def _calc_anchor_NE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) + cell_x), int(cell_y)

@_new_anchor("e", "east")
def _calc_anchor_E(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) + cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center y

@_new_anchor("se", "southeast")
def _calc_anchor_SE(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt)     + cell_x), int((cell_ht - item_ht)     + cell_y)

@_new_anchor("s", "south")
def _calc_anchor_S(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int((cell_ht - item_ht)     + cell_y)  # center x

@_new_anchor("sw", "southwest")
def _calc_anchor_SW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int((cell_ht - item_ht) + cell_y)

@_new_anchor("w", "west")
def _calc_anchor_W(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center y

@_new_anchor("nw", "northwest")
def _calc_anchor_NW(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int(cell_x), int(cell_y)

@_new_anchor("c", "center")
def _calc_anchor_C(item_wt: float, item_ht: float, cell_x: float, cell_y: float, cell_wt: float, cell_ht: float) -> tuple[int, int]:
    return int((cell_wt - item_wt) / 2 + cell_x), int((cell_ht - item_ht) / 2 + cell_y)  # center x & y




####################################################
########### MISC TYPES/HELPER FUNCTIONS ############
####################################################

class Rect(NamedTuple):
    """Contains bounding box information of a DearPyGui item."""
    x : float
    y : float
    wt: float
    ht: float


def _normalize_cellspan(r1, c1, r2, c2, rows, cols):
    r1 %= rows
    c1 %= cols
    r2 %= rows
    c2 %= cols
    if r1 > r2:
        r1, r2 = r2, r1
    if c1 > c2:
        c1, c2 = c2, c1
    return r1, c1, r2, c2


def _draw_cells(
    rect_size : tuple[int, int],
    rect_pad  : tuple[float, ...],
    cell_pad  : tuple[float, ...],
    x_axis    : 'GridAxis',
    y_axis    : 'GridAxis',
) -> dict[tuple[int, int], tuple[float, ...]]:
    bbox_x1_pad = rect_pad[0]
    bbox_y1_pad = rect_pad[2]
    bbox_ht = rect_size[1] - bbox_y1_pad - rect_pad[3]
    bbox_wt = rect_size[0] - bbox_x1_pad - rect_pad[1]

    weighted_ht = max(0, (bbox_ht - x_axis.min_size)) / max(1, x_axis.weight)
    weighted_wt = max(0, (bbox_wt - y_axis.min_size)) / max(1, y_axis.weight)

    cell_x1_pad = cell_pad[0] / 2
    cell_y1_pad = cell_pad[2] / 2
    cell_x_pad = cell_x1_pad + (cell_pad[1] / 2.0)
    cell_y_pad = cell_y1_pad + (cell_pad[3] / 2.0)

    rows = x_axis._members
    cols = [*enumerate(y_axis._members)]
    cell_map = {}

    alloc_ht = 0.0
    for row, row_cfg in enumerate(rows):
        row_height = row_cfg.size or weighted_ht * row_cfg.weight  # FIXED or SIZED policy
        # cell rect (vertical)
        cell_y_pos   = bbox_y1_pad + alloc_ht + cell_y1_pad
        cell_height  = row_height - cell_y_pad
        alloc_wt = 0.0
        for col, col_cfg in cols:
            col_width = col_cfg.size or weighted_wt * col_cfg.weight  # FIXED or SIZED policy
            # cell rect (horizontal)
            cell_x_pos    = bbox_x1_pad + alloc_wt + cell_x1_pad
            cell_width    = col_width - cell_x_pad
            alloc_wt += col_width
            cell_map[(row, col)] = (
                cell_x_pos,
                cell_y_pos,
                cell_width,
                cell_height,
            )
        alloc_ht += row_height
    return cell_map




####################################################
############# GRID & GRID DEPENDENCIES #############
####################################################

_GT = TypeVar("_GT")
_ST = TypeVar("_ST")

class GridConfigure(Generic[_GT, _ST], property):  # inherit property's "special-casing" (pyright)
    __slots__ = ("_get_eval", "_set_eval")

    def __init__(self, *args):
        ...

    def __set_name__(self, cls, name: str):
        self._get_eval = compile(f"instance._{name}", __name__, mode="eval")
        self._set_eval = compile(f"instance.configure({name}=value)", __name__, mode="exec")

    def __get__(self, instance, cls) -> _GT:
        try:
            return eval(self._get_eval)
        except (TypeError, AttributeError):
            if not instance:
                return self
            raise

    def __set__(self, instance, value: _ST) -> None:
        exec(self._set_eval)


class GridMember(NamedTuple):
    item   : ItemId
    cell1  : tuple[int, int]
    cell2  : tuple[int, int]
    max_wt : int
    max_ht : int
    calc_fn: _AnchorCalcT
    size_fn: Callable     = _set_item_size


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

    __slots__ = ("_weight", "_size",)

    FIXED = "fixed"
    SIZED = "sized"

    def __init__(self):
        self._weight = 1.0
        self._size   = 0

    def __repr__(self):
        return f"{type(self).__qualname__}(weight={self.weight}, size={self.size})"

    weight: GridConfigure[float, float] = GridConfigure()
    size  : GridConfigure[int, int]     = GridConfigure()

    @property
    def policy(self) -> Literal["fixed", "sized"]:
        return self.FIXED if self.size else self.SIZED

    @overload
    def configure(self, *, weight: float = ..., size: int = ...) -> None: ...
    def configure(self, *, weight: float = None, size: int | None = None) -> None:
        if weight is not None:
            self._weight = max(0, weight)
        if size is not None:
            self._size = max(0, size)


class GridAxis(Collection[GridSlot]):
    """A collection of Grid slots of a single axis."""

    __slots__ = ("_members",)

    def __init__(self, length : int = 0) -> None:
        self._members: list[GridSlot] = []
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
        self._members.extend(GridSlot() for _ in range(value))
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
        self._members.insert(index, GridSlot())

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
            self._members.extend(GridSlot() for _ in range(amount))
        else:
            del self._members[-amount:]


class Grid:
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
        parent : ItemId                                              =      0,
        sizer  : SizerT                                              = size_from_rect,
    ):
        self._rows = GridAxis(rows)
        self._cols = GridAxis(cols)
        self._members: dict[ItemId, GridMember] = {}
        self.members = types.MappingProxyType(self._members)
        self.configure(spacing=spacing, padding=padding, parent=parent, sizer=sizer)

    def __call__(self, *args) -> None:
        """Update the position and size of items managed by the grid."""
        # TODO: implement in rust
        # TODO: catch sizer_fn err
        cells   = _draw_cells(
            tuple(self._sizer(self._parent)),  # `_grid_draw_cells` expects PyTuple
            self._padding,
            self._spacing,
            self._rows,
            self._cols,
        )
        row_len = len(self._rows)
        col_len = len(self._cols)
        for item, coords1, coords2, item_width, item_height, calc_fn, sizer_fn, in self._members.values():
            r1, c1, r2, c2 = _normalize_cellspan(*coords1, *coords2, row_len, col_len)
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
            sizer_fn(
                item,
                pos=calc_fn(item_width, item_height, x_pos, y_pos, cell_width, cell_height),
                # XXX Due to how DPG interprets size values, the width/height cannot be
                # lower than 1 as it would actually make the item larger...
                width=max(int(item_width), 1),
                height=max(int(item_height), 1),
            )

    __code__ = __call__.__code__  # enables use as a direct DPG callback

    def __setitem__(self, coords: tuple[int, int] | tuple[int, int, int, int], item: ItemId, *, _anchor: str = "c"):
        """Pack and center an item into a grid cell or cell range."""
        self.push(item, *coords, anchor=_anchor)

    @property
    def rows(self) -> GridAxis:
        return self._rows
    @rows.setter
    def rows(self, value: int | GridAxis) -> None:
        if self._rows != value:  # self.rows += 1 -> self.rows.__set__(self, (self._rows + 1))
            self.configure(rows=value)

    @property
    def cols(self) -> GridAxis:
        return self._cols
    @cols.setter
    def cols(self, value: int | GridAxis) -> None:
        if self._cols != value:  # self.cols += 1 -> self.cols.__set__(self, (self._cols + 1))
            self.configure(cols=value)

    padding: GridConfigure[GridOffset, tuple[int | tuple[int, int], int | tuple[int, int]]] = GridConfigure()
    spacing: GridConfigure[GridOffset, tuple[int | tuple[int, int], int | tuple[int, int]]] = GridConfigure()

    parent : GridConfigure[ItemId, ItemId] = GridConfigure()
    sizer  : GridConfigure[SizerT, SizerT] = GridConfigure()

    ANCHORS = tuple(a.lower() for a in _ANCHOR_MAP)

    def configure(
        self,
        *,
        rows   : int = 0,
        cols   : int = 0,
        spacing: tuple[int | tuple[int, int], int | tuple[int, int]] | None = None,
        padding: tuple[int | tuple[int, int], int | tuple[int, int]] | None = None,
        parent : ItemId | None = None,
        sizer  : SizerT | None = None,
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
            if not parent and not (parent:=_dearpygui.top_container_stack()):
                raise ValueError("requires parent (container stack is empty).")
            self._parent = parent
        if sizer:
            self._sizer = sizer

    @overload
    def push(self, row: int, col: int, /, *, max_width: int = ..., max_height: int = ..., anchor: str = ...) -> None: ...
    @overload
    def push(self, r1: int, c1: int, r2: int, c2: int, /, *, max_width: int = ..., max_height: int = ..., anchor: str = ...) -> None: ...
    def push(self, item: ItemId, r1: int, c1: int, r2: int = None, c2: int = None, *, max_width : int = 0, max_height: int = 0, anchor: str = "c") -> None:
        # ensure item is currently valid
        if not (
        (isinstance(item, int) and dearpygui.does_item_exist(item)) or
        (isinstance(item, str) and dearpygui.does_alias_exist(item))):
            raise TypeError(f"`item` expected as int or str (got {item!r}).")
        # ensure coords are currently valid (XXX coords can become invalid as the number of slots change)
        try:
            self._rows[r1]
            self._rows[c1]
            self._cols[r2 or 0]
            self._cols[c2 or 0]
        except IndexError:
            raise IndexError("index(s) outside of grid range.") from None
        # pushing to single cell
        if r2 is None or c2 is None:
            r2, c2 = r1, c1
        # get anchor calculator
        try:
            anchor_fn = _ANCHOR_MAP[anchor.lower()]
        except TypeError:
            raise TypeError(f"`anchor` should be a string (got {type(anchor)}).") from None
        except KeyError:
            raise ValueError(f"Accepted `anchor` values; {', '.join(f'{a!r}' for a in self.ANCHORS)} (got {anchor!r}).") from None
        self._members[item] = GridMember(item, (r1, c1), (r2, c2), max(max_width, 0), max(max_height, 0), anchor_fn)

    @overload
    def pop(self, item: ItemId, /) -> None: ...
    @overload
    def pop(self, *, all_items: bool = ...) -> None: ...
    def pop(self, item: ItemId = None, *, unpack_all: bool = False) -> None:
        self._members.pop(item, None)
        if unpack_all:
            self._members.clear()




if __name__ == '__main__':
    from random import randint
    from dearpygui import dearpygui as dpg

    def bind_button_theme():
        while True:
            item = yield
            rgb  = randint(0, 255), randint(0, 255), randint(0, 255)
            with dpg.theme() as theme:
                with dpg.theme_component(0):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, [*rgb, 80])
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [*rgb, 255])
            dpg.bind_item_theme(item, theme)

    def create_button():
        themes = bind_button_theme().send
        themes(None)
        while True:
            tag = dpg.generate_uuid()
            item = dpg.add_button(label=tag, tag=tag)
            themes(item)
            yield item


    create_button = create_button().__next__


    dpg.create_context()
    dpg.create_viewport(title="Grid Demo (NEW)", width=1000, height=1000, min_height=10, min_width=10)
    dpg.setup_dearpygui()


    with dpg.window(no_scrollbar=True, no_background=True) as win:
        grid = Grid(6, 6, padding=((10, 30), 8), spacing=(0, 0))

        ...

        # Without additional arguments, items will expand and shrink to the cell's size.
        grid.push(create_button(),  0,  2)  # first row
        grid.push(create_button(), -1,  3)  # last row

        # You can clamp an item's width/height and include an alignment option. Valid
        # options are 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', and 'c'.
        grid.push(create_button(), 1, 1, max_height=25, anchor="w")  # west (centered)
        grid.push(create_button(), 1, 1, max_width=25, anchor="n")   # north (centered)
        grid.push(create_button(), 4, 4, max_height=25, anchor="w")

        # These items will occupy a range of cells.
        grid.push(create_button(),  3,  1,  4,  2)
        grid.push(create_button(),  1,  3,  2,  4)
        grid.push(create_button(),  4,  0, -1,  1)
        grid.push(create_button(),  0,  4,  1, -1)

        for anchor in grid.ANCHORS:  # '
            kwargs = dict(max_width=50, max_height=50, anchor=anchor)
            # pack to individual cells (cont.)
            grid.push(create_button(),  0,  0, **kwargs)  # first row & column
            grid.push(create_button(), -1, -1, **kwargs)  # last row & column
            # pack to a "merged cell" (cont.)
            grid.push(create_button(),  2,  2,  3,  3, **kwargs)

        # You can change the weight or set a fixed size for a row/column.

        grid.cols[2].weight = 0.5
        grid.cols[3].weight = 0.5
        grid.rows[2].weight = 0.5
        grid.rows[3].weight = 0.5

    print(grid.ANCHORS)


    dpg.set_primary_window(win, True)
    dpg.show_viewport()
    dpg.set_viewport_resize_callback(grid)


    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()