from typing import *
from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.core.itemtype import *
from dearpypixl.items import mvTheme as mvTheme
from dearpypixl.items import mvThemeComponent as mvThemeComponent
from dearpypixl.items import mvThemeColor as mvThemeColor
from dearpypixl.items import mvThemeStyle as mvThemeStyle

__all__ = (
    "alpha",
    "button_text_align",
    "cell_padding",
    "child_border_size",
    "child_rounding",
    "disabled_alpha",
    "docking_separator_size",
    "frame_border_size",
    "frame_padding",
    "frame_rounding",
    "grab_min_size",
    "grab_rounding",
    "indent_spacing",
    "item_inner_spacing",
    "item_spacing",
    "popup_border_size",
    "popup_rounding",
    "scrollbar_rounding",
    "scrollbar_size",
    "selectable_text_align",
    "separator_text_align",
    "separator_text_border_size",
    "separator_text_padding",
    "tab_bar_border_size",
    "tab_border_size",
    "tab_rounding",
    "table_angled_headers_angle",
    "table_angled_headers_text_align",
    "window_border_size",
    "window_min_size",
    "window_padding",
    "window_rounding",
    "window_title_align",
    "plot_annotation_padding",
    "plot_border_size",
    "plot_default_size",
    "plot_digital_bit_gap",
    "plot_digital_bit_height",
    "plot_error_bar_size",
    "plot_error_bar_weight",
    "plot_fill_alpha",
    "plot_fit_padding",
    "plot_label_padding",
    "plot_legend_inner_padding",
    "plot_legend_padding",
    "plot_legend_spacing",
    "plot_line_weight",
    "plot_major_grid_size",
    "plot_major_tick_len",
    "plot_major_tick_size",
    "plot_marker",
    "plot_marker_size",
    "plot_marker_weight",
    "plot_min_size",
    "plot_minor_alpha",
    "plot_minor_grid_size",
    "plot_minor_tick_len",
    "plot_minor_tick_size",
    "plot_mouse_pos_padding",
    "plot_padding",
    "node_border_thickness",
    "node_corner_rounding",
    "node_grid_spacing",
    "node_link_hover_distance",
    "node_link_line_segments_per_length",
    "node_link_thickness",
    "node_mini_map_offset",
    "node_mini_map_padding",
    "node_padding",
    "node_pin_circle_radius",
    "node_pin_hover_radius",
    "node_pin_line_thickness",
    "node_pin_offset",
    "node_pin_quad_side_length",
    "node_pin_triangle_side_length"
)


@overload
@staticmethod
def alpha[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def alpha[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def button_text_align[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def button_text_align[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def cell_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def cell_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def child_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def child_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def child_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def child_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def disabled_alpha[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def disabled_alpha[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def docking_separator_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def docking_separator_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def frame_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def frame_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def frame_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def frame_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def frame_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def frame_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def grab_min_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def grab_min_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def grab_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def grab_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def indent_spacing[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def indent_spacing[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def item_inner_spacing[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def item_inner_spacing[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def item_spacing[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def item_spacing[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def popup_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def popup_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def popup_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def popup_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def scrollbar_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def scrollbar_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def scrollbar_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def scrollbar_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def selectable_text_align[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def selectable_text_align[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def separator_text_align[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def separator_text_align[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def separator_text_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def separator_text_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def separator_text_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def separator_text_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def tab_bar_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def tab_bar_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def tab_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def tab_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def tab_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def tab_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def table_angled_headers_angle[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def table_angled_headers_angle[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def table_angled_headers_text_align[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def table_angled_headers_text_align[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def window_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def window_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def window_min_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def window_min_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def window_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def window_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def window_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def window_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def window_title_align[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def window_title_align[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_annotation_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_annotation_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_border_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_border_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_default_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_default_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_digital_bit_gap[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_digital_bit_gap[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_digital_bit_height[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_digital_bit_height[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_error_bar_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_error_bar_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_error_bar_weight[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_error_bar_weight[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_fill_alpha[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_fill_alpha[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_fit_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_fit_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_label_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_label_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_legend_inner_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_legend_inner_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_legend_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_legend_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_legend_spacing[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_legend_spacing[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_line_weight[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_line_weight[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_major_grid_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_major_grid_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_major_tick_len[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_major_tick_len[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_major_tick_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_major_tick_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_marker[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_marker[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_marker_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_marker_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_marker_weight[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_marker_weight[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_min_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_min_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_minor_alpha[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_minor_alpha[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_minor_grid_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_minor_grid_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_minor_tick_len[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_minor_tick_len[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_minor_tick_size[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_minor_tick_size[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_mouse_pos_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_mouse_pos_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def plot_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def plot_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_border_thickness[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_border_thickness[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_corner_rounding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_corner_rounding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_grid_spacing[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_grid_spacing[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_link_hover_distance[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_link_hover_distance[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_link_line_segments_per_length[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_link_line_segments_per_length[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_link_thickness[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_link_thickness[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_mini_map_offset[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_mini_map_offset[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_mini_map_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_mini_map_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_padding[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_padding[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_circle_radius[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_circle_radius[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_hover_radius[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_hover_radius[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_line_thickness[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_line_thickness[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_offset[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_offset[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_quad_side_length[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_quad_side_length[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...

@overload
@staticmethod
def node_pin_triangle_side_length[T = Any](value: tuple[int, int] | Sequence[int], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
@overload
@staticmethod
def node_pin_triangle_side_length[T = Any](x: float = 1.0, y: float = -1.0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True) -> mvThemeStyle[T, float]: ...
