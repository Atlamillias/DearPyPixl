from ._typing import (
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
def alpha(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def alpha(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def button_text_align(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def button_text_align(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def cell_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def cell_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def child_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def child_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def child_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def child_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def frame_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def frame_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def frame_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def frame_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def frame_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def frame_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def grab_min_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def grab_min_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def grab_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def grab_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def indent_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def indent_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def item_inner_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def item_inner_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def item_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def item_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def popup_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def popup_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def popup_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def popup_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def scrollbar_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def scrollbar_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def scrollbar_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def scrollbar_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def selectable_text_align(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def selectable_text_align(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def tab_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def tab_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def window_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def window_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def window_min_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def window_min_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def window_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def window_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def window_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def window_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def window_title_align(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def window_title_align(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_annotation_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_annotation_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_default_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_default_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_digital_bit_gap(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_digital_bit_gap(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_digital_bit_height(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_digital_bit_height(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_error_bar_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_error_bar_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_error_bar_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_error_bar_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_fill_alpha(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_fill_alpha(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_fit_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_fit_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_label_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_label_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_legend_inner_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_legend_inner_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_legend_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_legend_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_legend_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_legend_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_line_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_line_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_major_grid_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_major_grid_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_major_tick_len(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_major_tick_len(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_major_tick_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_major_tick_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_marker(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_marker(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_marker_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_marker_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_marker_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_marker_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_min_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_min_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_minor_alpha(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_minor_alpha(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_minor_grid_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_minor_grid_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_minor_tick_len(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_minor_tick_len(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_minor_tick_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_minor_tick_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_mouse_pos_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_mouse_pos_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_border_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_border_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_corner_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_corner_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_grid_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_grid_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_link_hover_distance(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_link_hover_distance(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_link_line_segments_per_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_link_line_segments_per_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_link_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_link_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_mini_map_offset(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_mini_map_offset(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_mini_map_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_mini_map_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_circle_radius(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_circle_radius(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_hover_radius(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_hover_radius(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_line_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_line_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_offset(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_offset(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_quad_side_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_quad_side_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_pin_triangle_side_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_pin_triangle_side_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


Alpha = alpha
ButtonTextAlign = button_text_align
CellPadding = cell_padding
ChildBorderSize = child_border_size
ChildRounding = child_rounding
FrameBorderSize = frame_border_size
FramePadding = frame_padding
FrameRounding = frame_rounding
GrabMinSize = grab_min_size
GrabRounding = grab_rounding
IndentSpacing = indent_spacing
ItemInnerSpacing = item_inner_spacing
ItemSpacing = item_spacing
PopupBorderSize = popup_border_size
PopupRounding = popup_rounding
ScrollbarRounding = scrollbar_rounding
ScrollbarSize = scrollbar_size
SelectableTextAlign = selectable_text_align
TabRounding = tab_rounding
WindowBorderSize = window_border_size
WindowMinSize = window_min_size
WindowPadding = window_padding
WindowRounding = window_rounding
WindowTitleAlign = window_title_align
PlotAnnotationPadding = plot_annotation_padding
PlotBorderSize = plot_border_size
PlotDefaultSize = plot_default_size
PlotDigitalBitGap = plot_digital_bit_gap
PlotDigitalBitHeight = plot_digital_bit_height
PlotErrorBarSize = plot_error_bar_size
PlotErrorBarWeight = plot_error_bar_weight
PlotFillAlpha = plot_fill_alpha
PlotFitPadding = plot_fit_padding
PlotLabelPadding = plot_label_padding
PlotLegendInnerPadding = plot_legend_inner_padding
PlotLegendPadding = plot_legend_padding
PlotLegendSpacing = plot_legend_spacing
PlotLineWeight = plot_line_weight
PlotMajorGridSize = plot_major_grid_size
PlotMajorTickLen = plot_major_tick_len
PlotMajorTickSize = plot_major_tick_size
PlotMarker = plot_marker
PlotMarkerSize = plot_marker_size
PlotMarkerWeight = plot_marker_weight
PlotMinSize = plot_min_size
PlotMinorAlpha = plot_minor_alpha
PlotMinorGridSize = plot_minor_grid_size
PlotMinorTickLen = plot_minor_tick_len
PlotMinorTickSize = plot_minor_tick_size
PlotMousePosPadding = plot_mouse_pos_padding
PlotPadding = plot_padding
NodeBorderThickness = node_border_thickness
NodeCornerRounding = node_corner_rounding
NodeGridSpacing = node_grid_spacing
NodeLinkHoverDistance = node_link_hover_distance
NodeLinkLineSegmentsPerLength = node_link_line_segments_per_length
NodeLinkThickness = node_link_thickness
NodeMiniMapOffset = node_mini_map_offset
NodeMiniMapPadding = node_mini_map_padding
NodePadding = node_padding
NodePinCircleRadius = node_pin_circle_radius
NodePinHoverRadius = node_pin_hover_radius
NodePinLineThickness = node_pin_line_thickness
NodePinOffset = node_pin_offset
NodePinQuadSideLength = node_pin_quad_side_length
NodePinTriangleSideLength = node_pin_triangle_side_length