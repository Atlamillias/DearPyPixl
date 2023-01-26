from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from dearpypixl.grid import GridAxis


def draw_cells(
    rect_size : tuple[float, float],
    rect_pad  : tuple[float, float, float, float],
    cell_pad  : tuple[float, float, float, float],
    x_axis    : GridAxis,
    y_axis    : GridAxis,
) -> dict[tuple[int, int], tuple[float, float, float, float]]: ...
