from ._typing import (
    Item,
    ItemAlias,
    ItemUUID,
    ItemCommand,
    Literal,
    Sequence,
    Callable,
    Unpack,
    Property,
    Any,
    overload,
)
from ._interface import (
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
    ThemeElementType,
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
def border(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def border_shadow(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def border_shadow(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def button(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def button(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def button_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def button_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def button_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def button_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def check_mark(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def check_mark(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def child_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def child_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def docking_empty_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def docking_empty_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def docking_preview(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def docking_preview(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def drag_drop_target(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def drag_drop_target(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def frame_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def frame_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def frame_bg_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def frame_bg_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def frame_bg_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def frame_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def header(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def header(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def header_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def header_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def header_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def header_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def menu_bar_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def menu_bar_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def modal_window_dim_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def modal_window_dim_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def nav_highlight(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def nav_highlight(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def nav_windowing_dim_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def nav_windowing_dim_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def nav_windowing_highlight(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def nav_windowing_highlight(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_histogram(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_histogram(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_histogram_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_histogram_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_lines(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_lines(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_lines_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_lines_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def popup_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def popup_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def resize_grip(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def resize_grip(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def resize_grip_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def resize_grip_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def resize_grip_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def resize_grip_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def scrollbar_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def scrollbar_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def scrollbar_grab(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def scrollbar_grab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def scrollbar_grab_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def scrollbar_grab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def scrollbar_grab_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def scrollbar_grab_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def separator(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def separator(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def separator_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def separator_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def separator_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def separator_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def slider_grab(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def slider_grab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def slider_grab_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def slider_grab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def tab(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def tab(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def tab_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def tab_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def tab_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def tab_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def tab_unfocused(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def tab_unfocused(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def tab_unfocused_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def tab_unfocused_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def table_border_light(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def table_border_light(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def table_border_strong(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def table_border_strong(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def table_header_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def table_header_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def table_row_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def table_row_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def table_row_bg_alt(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def table_row_bg_alt(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def text(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def text_disabled(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def text_disabled(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def text_selected_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def text_selected_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def title_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def title_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def title_bg_active(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def title_bg_active(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def title_bg_collapsed(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def title_bg_collapsed(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def window_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def window_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_border(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_crosshairs(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_crosshairs(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_error_bar(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_error_bar(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_fill(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_fill(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_frame_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_frame_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_inlay_text(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_inlay_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_legend_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_legend_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_legend_border(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_legend_border(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_legend_text(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_legend_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_line(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_line(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_marker_fill(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_marker_fill(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_marker_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_marker_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_query(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_query(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_selection(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_selection(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_title_text(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_title_text(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_x_axis(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_x_axis(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_x_axis_grid(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_x_axis_grid(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis2(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis2(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis3(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis3(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis_grid(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis_grid(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis_grid2(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis_grid2(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def plot_y_axis_grid3(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def plot_y_axis_grid3(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_bg_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_bg_selected(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_bg_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_box_selector(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_box_selector(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_box_selector_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_box_selector_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_grid_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_grid_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_grid_line(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_grid_line(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_grid_line_primary(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_grid_line_primary(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_link(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_link(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_link_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_link_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_link_selected(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_link_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_bg_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_canvas(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_canvas(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_canvas_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_canvas_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_link(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_link(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_link_selected(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_link_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_node_bg(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_node_bg(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_node_bg_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_node_bg_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_node_bg_selected(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_node_bg_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_node_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_node_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_mini_map_outline_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_mini_map_outline_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_outline(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_outline(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_pin(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_pin(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_pin_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_pin_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_title_bar(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_title_bar(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_title_bar_hovered(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_title_bar_hovered(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


@overload
def node_title_bar_selected(value: tuple[int, int, int] | Sequence[int] | tuple[int, int, int, int], /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...
@overload
def node_title_bar_selected(r: float, g: float, b: float, a: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> mvThemeColor: ...


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
PlotBg = plot_bg
PlotBorder = plot_border
PlotCrosshairs = plot_crosshairs
PlotErrorBar = plot_error_bar
PlotFill = plot_fill
PlotFrameBg = plot_frame_bg
PlotInlayText = plot_inlay_text
PlotLegendBg = plot_legend_bg
PlotLegendBorder = plot_legend_border
PlotLegendText = plot_legend_text
PlotLine = plot_line
PlotMarkerFill = plot_marker_fill
PlotMarkerOutline = plot_marker_outline
PlotQuery = plot_query
PlotSelection = plot_selection
PlotTitleText = plot_title_text
PlotXAxis = plot_x_axis
PlotXAxisGrid = plot_x_axis_grid
PlotYAxis = plot_y_axis
PlotYAxis2 = plot_y_axis2
PlotYAxis3 = plot_y_axis3
PlotYAxisGrid = plot_y_axis_grid
PlotYAxisGrid2 = plot_y_axis_grid2
PlotYAxisGrid3 = plot_y_axis_grid3
NodeBg = node_bg
NodeBgHovered = node_bg_hovered
NodeBgSelected = node_bg_selected
NodeBoxSelector = node_box_selector
NodeBoxSelectorOutline = node_box_selector_outline
NodeGridBg = node_grid_bg
NodeGridLine = node_grid_line
NodeGridLinePrimary = node_grid_line_primary
NodeLink = node_link
NodeLinkHovered = node_link_hovered
NodeLinkSelected = node_link_selected
NodeMiniMapBg = node_mini_map_bg
NodeMiniMapBgHovered = node_mini_map_bg_hovered
NodeMiniMapCanvas = node_mini_map_canvas
NodeMiniMapCanvasOutline = node_mini_map_canvas_outline
NodeMiniMapLink = node_mini_map_link
NodeMiniMapLinkSelected = node_mini_map_link_selected
NodeMiniMapNodeBg = node_mini_map_node_bg
NodeMiniMapNodeBgHovered = node_mini_map_node_bg_hovered
NodeMiniMapNodeBgSelected = node_mini_map_node_bg_selected
NodeMiniMapNodeOutline = node_mini_map_node_outline
NodeMiniMapOutline = node_mini_map_outline
NodeMiniMapOutlineHovered = node_mini_map_outline_hovered
NodeOutline = node_outline
NodePin = node_pin
NodePinHovered = node_pin_hovered
NodeTitleBar = node_title_bar
NodeTitleBarHovered = node_title_bar_hovered
NodeTitleBarSelected = node_title_bar_selected