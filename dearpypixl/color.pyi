from ._dearpypixl.common import (
    Item,
    ItemAlias,
    ItemUUID,
    ItemCommand,
    Array,
    Literal,
    Sequence,
    Callable,
    Unpack,
    Property,
    Any,
    Color,
    Point,
    overload,
)
from ._dearpypixl.interface import (
    BasicType,
    ContainerType,
    DrawNodeType,
    DrawingType,
    FontType,
    HandlerType,
    NodeEditorType,
    NodeType,
    PlotAxisType,
    PlotType,
    PlottingType,
    RegistryType,
    RootType,
    SupportsCallback,
    SupportsSized,
    SupportsValueArray,
    TableItemType,
    TableType,
    ThemeType,
    WindowType,
    mvAll,
)
from .items import (
    ThemeColor as ThemeColor,
    ThemeStyle as ThemeStyle,
    mvThemeColor as mvThemeColor,
    mvThemeStyle as mvThemeStyle,
)


@overload
def border(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def border_shadow(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def border_shadow(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def button(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def button(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def button_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def button_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def button_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def button_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def check_mark(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def check_mark(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def child_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def child_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def docking_empty_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def docking_empty_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def docking_preview(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def docking_preview(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def drag_drop_target(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def drag_drop_target(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def frame_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def frame_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def frame_bg_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def frame_bg_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def frame_bg_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def frame_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def header(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def header(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def header_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def header_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def header_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def header_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def menu_bar_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def menu_bar_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def modal_window_dim_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def modal_window_dim_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def nav_highlight(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def nav_highlight(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def nav_windowing_dim_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def nav_windowing_dim_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def nav_windowing_highlight(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def nav_windowing_highlight(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_histogram(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_histogram(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_histogram_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_histogram_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_lines(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_lines(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_lines_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_lines_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def popup_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def popup_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def resize_grip(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def resize_grip(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def resize_grip_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def resize_grip_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def resize_grip_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def resize_grip_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def scrollbar_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def scrollbar_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def scrollbar_grab(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def scrollbar_grab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def scrollbar_grab_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def scrollbar_grab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def scrollbar_grab_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def scrollbar_grab_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def separator(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def separator(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def separator_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def separator_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def separator_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def separator_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def slider_grab(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def slider_grab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def slider_grab_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def slider_grab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def tab(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def tab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def tab_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def tab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def tab_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def tab_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def tab_unfocused(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def tab_unfocused(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def tab_unfocused_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def tab_unfocused_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def table_border_light(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def table_border_light(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def table_border_strong(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def table_border_strong(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def table_header_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def table_header_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def table_row_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def table_row_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def table_row_bg_alt(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def table_row_bg_alt(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def text(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def text_disabled(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def text_disabled(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def text_selected_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def text_selected_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bg_active(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bg_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bg_collapsed(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bg_collapsed(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def window_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def window_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def crosshairs(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def crosshairs(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def error_bar(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def error_bar(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def fill(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def fill(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def inlay_text(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def inlay_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def legend_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def legend_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def legend_border(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def legend_border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def legend_text(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def legend_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def line(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def line(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def marker_fill(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def marker_fill(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def marker_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def marker_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_border(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def plot_frame_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def plot_frame_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def query(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def query(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def selection(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def selection(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_text(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def x_axis(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def x_axis(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def x_axis_grid(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def x_axis_grid(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis2(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis2(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis3(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis3(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis_grid(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis_grid(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis_grid2(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis_grid2(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def y_axis_grid3(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def y_axis_grid3(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def box_selector(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def box_selector(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def box_selector_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def box_selector_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def grid_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def grid_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def grid_line(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def grid_line(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def grid_line_primary(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def grid_line_primary(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def link(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def link(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def link_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def link_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def link_selected(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def link_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_bg_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_canvas(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_canvas(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_canvas_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_canvas_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_link(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_link(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_link_selected(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_link_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_node_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_node_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_node_bg_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_node_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_node_bg_selected(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_node_bg_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_node_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_node_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def mini_map_outline_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def mini_map_outline_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def node_bg(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def node_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def node_bg_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def node_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def node_bg_selected(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def node_bg_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def node_outline(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def node_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def pin(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def pin(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def pin_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def pin_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bar(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bar(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bar_hovered(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bar_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


@overload
def title_bar_selected(value: Array[int, int, int, int | None], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...
@overload
def title_bar_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeColor: ...


Border = border
BorderShadow = border_shadow
Button = button
ButtonActive = button_active
ButtonHovered = button_hovered
CheckMark = check_mark
ChildBg = child_bg
DockingEmptyBg = docking_empty_bg
DockingPreview = docking_preview
DragDropTarget = drag_drop_target
FrameBg = frame_bg
FrameBgActive = frame_bg_active
FrameBgHovered = frame_bg_hovered
Header = header
HeaderActive = header_active
HeaderHovered = header_hovered
MenuBarBg = menu_bar_bg
ModalWindowDimBg = modal_window_dim_bg
NavHighlight = nav_highlight
NavWindowingDimBg = nav_windowing_dim_bg
NavWindowingHighlight = nav_windowing_highlight
PlotHistogram = plot_histogram
PlotHistogramHovered = plot_histogram_hovered
PlotLines = plot_lines
PlotLinesHovered = plot_lines_hovered
PopupBg = popup_bg
ResizeGrip = resize_grip
ResizeGripActive = resize_grip_active
ResizeGripHovered = resize_grip_hovered
ScrollbarBg = scrollbar_bg
ScrollbarGrab = scrollbar_grab
ScrollbarGrabActive = scrollbar_grab_active
ScrollbarGrabHovered = scrollbar_grab_hovered
Separator = separator
SeparatorActive = separator_active
SeparatorHovered = separator_hovered
SliderGrab = slider_grab
SliderGrabActive = slider_grab_active
Tab = tab
TabActive = tab_active
TabHovered = tab_hovered
TabUnfocused = tab_unfocused
TabUnfocusedActive = tab_unfocused_active
TableBorderLight = table_border_light
TableBorderStrong = table_border_strong
TableHeaderBg = table_header_bg
TableRowBg = table_row_bg
TableRowBgAlt = table_row_bg_alt
Text = text
TextDisabled = text_disabled
TextSelectedBg = text_selected_bg
TitleBg = title_bg
TitleBgActive = title_bg_active
TitleBgCollapsed = title_bg_collapsed
WindowBg = window_bg
Crosshairs = crosshairs
ErrorBar = error_bar
Fill = fill
InlayText = inlay_text
LegendBg = legend_bg
LegendBorder = legend_border
LegendText = legend_text
Line = line
MarkerFill = marker_fill
MarkerOutline = marker_outline
PlotBg = plot_bg
PlotBorder = plot_border
PlotFrameBg = plot_frame_bg
Query = query
Selection = selection
TitleText = title_text
XAxis = x_axis
XAxisGrid = x_axis_grid
YAxis = y_axis
YAxis2 = y_axis2
YAxis3 = y_axis3
YAxisGrid = y_axis_grid
YAxisGrid2 = y_axis_grid2
YAxisGrid3 = y_axis_grid3
BoxSelector = box_selector
BoxSelectorOutline = box_selector_outline
GridBg = grid_bg
GridLine = grid_line
GridLinePrimary = grid_line_primary
Link = link
LinkHovered = link_hovered
LinkSelected = link_selected
MiniMapBg = mini_map_bg
MiniMapBgHovered = mini_map_bg_hovered
MiniMapCanvas = mini_map_canvas
MiniMapCanvasOutline = mini_map_canvas_outline
MiniMapLink = mini_map_link
MiniMapLinkSelected = mini_map_link_selected
MiniMapNodeBg = mini_map_node_bg
MiniMapNodeBgHovered = mini_map_node_bg_hovered
MiniMapNodeBgSelected = mini_map_node_bg_selected
MiniMapNodeOutline = mini_map_node_outline
MiniMapOutline = mini_map_outline
MiniMapOutlineHovered = mini_map_outline_hovered
NodeBg = node_bg
NodeBgHovered = node_bg_hovered
NodeBgSelected = node_bg_selected
NodeOutline = node_outline
Pin = pin
PinHovered = pin_hovered
TitleBar = title_bar
TitleBarHovered = title_bar_hovered
TitleBarSelected = title_bar_selected