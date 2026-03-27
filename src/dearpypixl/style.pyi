from typing import *

from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.lib.items import mvTheme as mvTheme
from dearpypixl.lib.items import mvThemeComponent as mvThemeComponent
from dearpypixl.lib.items import mvThemeColor as mvThemeColor
from dearpypixl.lib.items import mvThemeStyle as mvThemeStyle


__all__ = (
    "alpha",
    "disabled_alpha",
    "window_padding",
    "window_rounding",
    "window_border_size",
    "window_min_size",
    "window_title_align",
    "child_rounding",
    "child_border_size",
    "popup_rounding",
    "popup_border_size",
    "frame_padding",
    "frame_rounding",
    "frame_border_size",
    "item_spacing",
    "item_inner_spacing",
    "indent_spacing",
    "cell_padding",
    "scrollbar_size",
    "scrollbar_rounding",
    "grab_min_size",
    "grab_rounding",
    "tab_rounding",
    "tab_border_size",
    "tab_bar_border_size",
    "table_angled_headers_angle",
    "table_angled_headers_text_align",
    "button_text_align",
    "selectable_text_align",
    "separator_text_border_size",
    "separator_text_align",
    "separator_text_padding",
    "docking_separator_size",
    "plot_line_weight",
    "plot_marker",
    "plot_marker_size",
    "plot_marker_weight",
    "plot_fill_alpha",
    "plot_error_bar_size",
    "plot_error_bar_weight",
    "plot_digital_bit_height",
    "plot_digital_bit_gap",
    "plot_border_size",
    "plot_minor_alpha",
    "plot_major_tick_len",
    "plot_minor_tick_len",
    "plot_major_tick_size",
    "plot_minor_tick_size",
    "plot_major_grid_size",
    "plot_minor_grid_size",
    "plot_padding",
    "plot_label_padding",
    "plot_legend_padding",
    "plot_legend_inner_padding",
    "plot_legend_spacing",
    "plot_mouse_pos_padding",
    "plot_annotation_padding",
    "plot_fit_padding",
    "plot_default_size",
    "plot_min_size",
    "node_grid_spacing",
    "node_corner_rounding",
    "node_padding",
    "node_border_thickness",
    "node_link_thickness",
    "node_link_line_segments_per_length",
    "node_link_hover_distance",
    "node_pin_circle_radius",
    "node_pin_quad_side_length",
    "node_pin_triangle_side_length",
    "node_pin_line_thickness",
    "node_pin_hover_radius",
    "node_pin_offset",
    "node_mini_map_padding",
    "node_mini_map_offset",
)




@overload
def alpha[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def alpha[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def disabled_alpha[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def disabled_alpha[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def window_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def window_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def window_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def window_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def window_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def window_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def window_min_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def window_min_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def window_title_align[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def window_title_align[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def child_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def child_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def child_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def child_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def popup_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def popup_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def popup_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def popup_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def frame_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def frame_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def frame_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def frame_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def frame_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def frame_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def item_spacing[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def item_spacing[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def item_inner_spacing[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def item_inner_spacing[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def indent_spacing[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def indent_spacing[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def cell_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def cell_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def scrollbar_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def scrollbar_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def scrollbar_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def scrollbar_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def grab_min_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def grab_min_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def grab_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def grab_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def tab_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def tab_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def tab_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def tab_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def tab_bar_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def tab_bar_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def table_angled_headers_angle[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def table_angled_headers_angle[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def table_angled_headers_text_align[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def table_angled_headers_text_align[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def button_text_align[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def button_text_align[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def selectable_text_align[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def selectable_text_align[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def separator_text_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def separator_text_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def separator_text_align[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def separator_text_align[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def separator_text_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def separator_text_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def docking_separator_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def docking_separator_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_line_weight[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_line_weight[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_marker[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_marker[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_marker_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_marker_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_marker_weight[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_marker_weight[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_fill_alpha[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_fill_alpha[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_error_bar_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_error_bar_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_error_bar_weight[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_error_bar_weight[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_digital_bit_height[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_digital_bit_height[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_digital_bit_gap[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_digital_bit_gap[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_border_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_border_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_minor_alpha[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_minor_alpha[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_major_tick_len[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_major_tick_len[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_minor_tick_len[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_minor_tick_len[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_major_tick_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_major_tick_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_minor_tick_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_minor_tick_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_major_grid_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_major_grid_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_minor_grid_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_minor_grid_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_label_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_label_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_legend_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_legend_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_legend_inner_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_legend_inner_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_legend_spacing[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_legend_spacing[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_mouse_pos_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_mouse_pos_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_annotation_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_annotation_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_fit_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_fit_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_default_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_default_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def plot_min_size[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def plot_min_size[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_grid_spacing[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_grid_spacing[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_corner_rounding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_corner_rounding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_border_thickness[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_border_thickness[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_link_thickness[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_link_thickness[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_link_line_segments_per_length[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_link_line_segments_per_length[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_link_hover_distance[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_link_hover_distance[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_circle_radius[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_circle_radius[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_quad_side_length[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_quad_side_length[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_triangle_side_length[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_triangle_side_length[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_line_thickness[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_line_thickness[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_hover_radius[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_hover_radius[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_pin_offset[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_pin_offset[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_mini_map_padding[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_mini_map_padding[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


@overload
def node_mini_map_offset[T = Any](value: Array[int | float, Literal[2]], /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...
@overload
def node_mini_map_offset[T = Any](x: int | float = 1.0, y: int | float = -1.0, /, *, label: str | None = None, user_data: T = ..., use_internal_label: bool = True, tag: Item = 0, parent: Item = 0) -> mvThemeStyle[T]: ...


