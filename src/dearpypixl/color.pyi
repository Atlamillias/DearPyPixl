from typing import *
from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.core.itemtype import *
from dearpypixl.items import mvTheme as mvTheme
from dearpypixl.items import mvThemeComponent as mvThemeComponent
from dearpypixl.items import mvThemeColor as mvThemeColor
from dearpypixl.items import mvThemeStyle as mvThemeStyle

__all__ = (
    "border",
    "border_shadow",
    "button",
    "button_active",
    "button_hovered",
    "check_mark",
    "child_bg",
    "docking_empty_bg",
    "docking_preview",
    "drag_drop_target",
    "frame_bg",
    "frame_bg_active",
    "frame_bg_hovered",
    "header",
    "header_active",
    "header_hovered",
    "menu_bar_bg",
    "modal_window_dim_bg",
    "nav_highlight",
    "nav_windowing_dim_bg",
    "nav_windowing_highlight",
    "plot_histogram",
    "plot_histogram_hovered",
    "plot_lines",
    "plot_lines_hovered",
    "popup_bg",
    "resize_grip",
    "resize_grip_active",
    "resize_grip_hovered",
    "scrollbar_bg",
    "scrollbar_grab",
    "scrollbar_grab_active",
    "scrollbar_grab_hovered",
    "separator",
    "separator_active",
    "separator_hovered",
    "slider_grab",
    "slider_grab_active",
    "tab",
    "tab_active",
    "tab_hovered",
    "tab_unfocused",
    "tab_unfocused_active",
    "table_border_light",
    "table_border_strong",
    "table_header_bg",
    "table_row_bg",
    "table_row_bg_alt",
    "text",
    "text_disabled",
    "text_selected_bg",
    "title_bg",
    "title_bg_active",
    "title_bg_collapsed",
    "window_bg",
    "plot_axis_bg",
    "plot_axis_bg_active",
    "plot_axis_bg_hovered",
    "plot_axis_grid",
    "plot_axis_text",
    "plot_bg",
    "plot_border",
    "plot_crosshairs",
    "plot_error_bar",
    "plot_fill",
    "plot_frame_bg",
    "plot_inlay_text",
    "plot_legend_bg",
    "plot_legend_border",
    "plot_legend_text",
    "plot_line",
    "plot_marker_fill",
    "plot_marker_outline",
    "plot_selection",
    "plot_title_text",
    "node_bg",
    "node_bg_hovered",
    "node_bg_selected",
    "node_box_selector",
    "node_box_selector_outline",
    "node_grid_bg",
    "node_grid_line",
    "node_grid_line_primary",
    "node_link",
    "node_link_hovered",
    "node_link_selected",
    "node_mini_map_bg",
    "node_mini_map_bg_hovered",
    "node_mini_map_canvas",
    "node_mini_map_canvas_outline",
    "node_mini_map_link",
    "node_mini_map_link_selected",
    "node_mini_map_node_bg",
    "node_mini_map_node_bg_hovered",
    "node_mini_map_node_bg_selected",
    "node_mini_map_node_outline",
    "node_mini_map_outline",
    "node_mini_map_outline_hovered",
    "node_outline",
    "node_pin",
    "node_pin_hovered",
    "node_title_bar",
    "node_title_bar_hovered",
    "node_title_bar_selected"
)


@overload
@staticmethod
def border[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def border[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def border_shadow[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def border_shadow[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def button[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def button[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def button_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def button_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def button_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def button_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def check_mark[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def check_mark[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def child_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def child_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def docking_empty_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def docking_empty_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def docking_preview[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def docking_preview[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def drag_drop_target[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def drag_drop_target[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def frame_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def frame_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def frame_bg_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def frame_bg_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def frame_bg_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def frame_bg_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def header[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def header[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def header_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def header_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def header_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def header_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def menu_bar_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def menu_bar_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def modal_window_dim_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def modal_window_dim_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def nav_highlight[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def nav_highlight[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def nav_windowing_dim_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def nav_windowing_dim_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def nav_windowing_highlight[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def nav_windowing_highlight[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_histogram[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_histogram[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_histogram_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_histogram_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_lines[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_lines[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_lines_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_lines_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def popup_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def popup_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def resize_grip[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def resize_grip[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def resize_grip_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def resize_grip_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def resize_grip_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def resize_grip_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def scrollbar_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def scrollbar_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def scrollbar_grab[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def scrollbar_grab[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def scrollbar_grab_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def scrollbar_grab_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def scrollbar_grab_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def scrollbar_grab_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def separator[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def separator[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def separator_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def separator_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def separator_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def separator_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def slider_grab[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def slider_grab[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def slider_grab_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def slider_grab_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def tab[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def tab[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def tab_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def tab_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def tab_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def tab_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def tab_unfocused[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def tab_unfocused[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def tab_unfocused_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def tab_unfocused_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def table_border_light[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def table_border_light[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def table_border_strong[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def table_border_strong[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def table_header_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def table_header_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def table_row_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def table_row_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def table_row_bg_alt[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def table_row_bg_alt[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def text[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def text[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def text_disabled[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def text_disabled[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def text_selected_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def text_selected_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def title_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def title_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def title_bg_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def title_bg_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def title_bg_collapsed[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def title_bg_collapsed[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def window_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def window_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_axis_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_axis_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_axis_bg_active[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_axis_bg_active[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_axis_bg_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_axis_bg_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_axis_grid[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_axis_grid[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_axis_text[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_axis_text[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_border[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_border[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_crosshairs[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_crosshairs[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_error_bar[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_error_bar[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_fill[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_fill[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_frame_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_frame_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_inlay_text[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_inlay_text[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_legend_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_legend_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_legend_border[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_legend_border[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_legend_text[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_legend_text[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_line[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_line[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_marker_fill[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_marker_fill[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_marker_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_marker_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_selection[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_selection[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def plot_title_text[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def plot_title_text[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_bg_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_bg_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_bg_selected[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_bg_selected[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_box_selector[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_box_selector[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_box_selector_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_box_selector_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_grid_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_grid_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_grid_line[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_grid_line[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_grid_line_primary[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_grid_line_primary[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_link[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_link[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_link_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_link_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_link_selected[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_link_selected[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_bg_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_bg_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_canvas[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_canvas[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_canvas_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_canvas_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_link[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_link[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_link_selected[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_link_selected[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_node_bg[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_node_bg[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_node_bg_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_node_bg_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_node_bg_selected[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_node_bg_selected[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_node_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_node_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_mini_map_outline_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_mini_map_outline_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_outline[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_outline[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_pin[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_pin[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_pin_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_pin_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_title_bar[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_title_bar[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_title_bar_hovered[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_title_bar_hovered[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...

@overload
@staticmethod
def node_title_bar_selected[T = Any](value: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
@overload
@staticmethod
def node_title_bar_selected[T = Any](r: float, g: float, b: float, a: float = 255.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeColor[T, float]: ...
