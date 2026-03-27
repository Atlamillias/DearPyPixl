from typing import *

from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.lib.items import mvTheme as mvTheme
from dearpypixl.lib.items import mvThemeComponent as mvThemeComponent
from dearpypixl.lib.items import mvThemeColor as mvThemeColor
from dearpypixl.lib.items import mvThemeStyle as mvThemeStyle


__all__ = (
    "text",
    "text_disabled",
    "window_bg",
    "child_bg",
    "border",
    "popup_bg",
    "border_shadow",
    "frame_bg",
    "frame_bg_hovered",
    "frame_bg_active",
    "title_bg",
    "title_bg_active",
    "title_bg_collapsed",
    "menu_bar_bg",
    "scrollbar_bg",
    "scrollbar_grab",
    "scrollbar_grab_hovered",
    "scrollbar_grab_active",
    "check_mark",
    "slider_grab",
    "slider_grab_active",
    "button",
    "button_hovered",
    "button_active",
    "header",
    "header_hovered",
    "header_active",
    "separator",
    "separator_hovered",
    "separator_active",
    "resize_grip",
    "resize_grip_hovered",
    "resize_grip_active",
    "tab",
    "tab_hovered",
    "tab_active",
    "tab_unfocused",
    "tab_unfocused_active",
    "docking_preview",
    "docking_empty_bg",
    "plot_lines",
    "plot_lines_hovered",
    "plot_histogram",
    "plot_histogram_hovered",
    "table_header_bg",
    "table_border_strong",
    "table_border_light",
    "table_row_bg",
    "table_row_bg_alt",
    "text_selected_bg",
    "drag_drop_target",
    "nav_highlight",
    "nav_windowing_highlight",
    "nav_windowing_dim_bg",
    "modal_window_dim_bg",
    "plot_line",
    "plot_fill",
    "plot_marker_outline",
    "plot_marker_fill",
    "plot_error_bar",
    "plot_frame_bg",
    "plot_bg",
    "plot_border",
    "plot_legend_bg",
    "plot_legend_border",
    "plot_legend_text",
    "plot_title_text",
    "plot_inlay_text",
    "plot_axis_bg",
    "plot_axis_bg_active",
    "plot_axis_bg_hovered",
    "plot_axis_grid",
    "plot_axis_text",
    "plot_selection",
    "plot_crosshairs",
    "node_bg",
    "node_bg_hovered",
    "node_bg_selected",
    "node_outline",
    "node_title_bar",
    "node_title_bar_hovered",
    "node_title_bar_selected",
    "node_link",
    "node_link_hovered",
    "node_link_selected",
    "node_pin",
    "node_pin_hovered",
    "node_box_selector",
    "node_box_selector_outline",
    "node_grid_bg",
    "node_grid_line",
    "node_grid_line_primary",
    "node_mini_map_bg",
    "node_mini_map_bg_hovered",
    "node_mini_map_outline",
    "node_mini_map_outline_hovered",
    "node_mini_map_bg",
    "node_mini_map_bg_hovered",
    "node_mini_map_bg_selected",
    "node_mini_map_outline",
    "node_mini_map_link",
    "node_mini_map_link_selected",
    "node_mini_map_canvas",
    "node_mini_map_canvas_outline",
)




@overload
def text[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def text[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def text_disabled[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def text_disabled[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def window_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def window_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def child_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def child_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def border[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def border[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def popup_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def popup_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def border_shadow[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def border_shadow[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def frame_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def frame_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def frame_bg_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def frame_bg_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def frame_bg_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def frame_bg_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def title_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def title_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def title_bg_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def title_bg_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def title_bg_collapsed[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def title_bg_collapsed[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def menu_bar_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def menu_bar_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def scrollbar_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def scrollbar_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def scrollbar_grab[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def scrollbar_grab[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def scrollbar_grab_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def scrollbar_grab_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def scrollbar_grab_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def scrollbar_grab_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def check_mark[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def check_mark[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def slider_grab[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def slider_grab[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def slider_grab_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def slider_grab_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def button[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def button[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def button_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def button_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def button_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def button_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def header[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def header[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def header_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def header_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def header_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def header_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def separator[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def separator[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def separator_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def separator_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def separator_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def separator_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def resize_grip[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def resize_grip[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def resize_grip_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def resize_grip_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def resize_grip_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def resize_grip_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def tab[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def tab[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def tab_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def tab_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def tab_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def tab_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def tab_unfocused[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def tab_unfocused[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def tab_unfocused_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def tab_unfocused_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def docking_preview[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def docking_preview[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def docking_empty_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def docking_empty_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_lines[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_lines[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_lines_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_lines_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_histogram[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_histogram[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_histogram_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_histogram_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def table_header_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def table_header_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def table_border_strong[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def table_border_strong[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def table_border_light[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def table_border_light[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def table_row_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def table_row_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def table_row_bg_alt[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def table_row_bg_alt[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def text_selected_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def text_selected_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def drag_drop_target[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def drag_drop_target[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def nav_highlight[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def nav_highlight[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def nav_windowing_highlight[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def nav_windowing_highlight[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def nav_windowing_dim_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def nav_windowing_dim_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def modal_window_dim_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def modal_window_dim_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_line[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_line[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_fill[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_fill[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_marker_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_marker_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_marker_fill[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_marker_fill[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_error_bar[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_error_bar[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_frame_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_frame_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_border[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_border[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_legend_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_legend_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_legend_border[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_legend_border[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_legend_text[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_legend_text[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_title_text[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_title_text[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_inlay_text[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_inlay_text[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_axis_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_axis_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_axis_bg_active[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_axis_bg_active[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_axis_bg_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_axis_bg_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_axis_grid[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_axis_grid[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_axis_text[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_axis_text[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_selection[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_selection[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def plot_crosshairs[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def plot_crosshairs[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_bg_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_bg_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_bg_selected[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_bg_selected[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_title_bar[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_title_bar[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_title_bar_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_title_bar_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_title_bar_selected[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_title_bar_selected[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_link[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_link[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_link_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_link_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_link_selected[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_link_selected[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_pin[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_pin[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_pin_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_pin_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_box_selector[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_box_selector[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_box_selector_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_box_selector_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_grid_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_grid_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_grid_line[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_grid_line[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_grid_line_primary[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_grid_line_primary[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_bg_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_bg_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_outline_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_outline_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_bg[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_bg[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_bg_hovered[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_bg_hovered[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_bg_selected[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_bg_selected[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_link[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_link[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_link_selected[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_link_selected[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_canvas[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_canvas[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


@overload
def node_mini_map_canvas_outline[T = Any](value: Array[int, Literal[3, 4]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...
@overload
def node_mini_map_canvas_outline[T = Any](r: int, g: int, b: int, a: int = 255, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeColor[T]: ...


