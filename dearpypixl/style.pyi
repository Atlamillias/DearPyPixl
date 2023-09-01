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
def annotation_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def annotation_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def digital_bit_gap(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def digital_bit_gap(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def digital_bit_height(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def digital_bit_height(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def error_bar_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def error_bar_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def error_bar_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def error_bar_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def fill_alpha(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def fill_alpha(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def fit_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def fit_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def label_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def label_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def legend_inner_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def legend_inner_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def legend_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def legend_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def legend_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def legend_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def line_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def line_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def major_grid_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def major_grid_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def major_tick_len(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def major_tick_len(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def major_tick_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def major_tick_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def marker(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def marker(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def marker_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def marker_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def marker_weight(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def marker_weight(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def minor_alpha(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def minor_alpha(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def minor_grid_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def minor_grid_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def minor_tick_len(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def minor_tick_len(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def minor_tick_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def minor_tick_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def mouse_pos_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def mouse_pos_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_border_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_border_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_default_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_default_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_min_size(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_min_size(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def plot_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def plot_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def grid_spacing(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def grid_spacing(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def link_hover_distance(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def link_hover_distance(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def link_line_segments_per_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def link_line_segments_per_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def link_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def link_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def mini_map_offset(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def mini_map_offset(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def mini_map_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def mini_map_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_border_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_border_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_corner_rounding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_corner_rounding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def node_padding(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def node_padding(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_circle_radius(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_circle_radius(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_hover_radius(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_hover_radius(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_line_thickness(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_line_thickness(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_offset(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_offset(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_quad_side_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_quad_side_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


@overload
def pin_triangle_side_length(value: Array[float, float] = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...
@overload
def pin_triangle_side_length(x: float = ..., y: float = ..., /, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ...) -> mvThemeStyle: ...


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
AnnotationPadding = annotation_padding
DigitalBitGap = digital_bit_gap
DigitalBitHeight = digital_bit_height
ErrorBarSize = error_bar_size
ErrorBarWeight = error_bar_weight
FillAlpha = fill_alpha
FitPadding = fit_padding
LabelPadding = label_padding
LegendInnerPadding = legend_inner_padding
LegendPadding = legend_padding
LegendSpacing = legend_spacing
LineWeight = line_weight
MajorGridSize = major_grid_size
MajorTickLen = major_tick_len
MajorTickSize = major_tick_size
Marker = marker
MarkerSize = marker_size
MarkerWeight = marker_weight
MinorAlpha = minor_alpha
MinorGridSize = minor_grid_size
MinorTickLen = minor_tick_len
MinorTickSize = minor_tick_size
MousePosPadding = mouse_pos_padding
PlotBorderSize = plot_border_size
PlotDefaultSize = plot_default_size
PlotMinSize = plot_min_size
PlotPadding = plot_padding
GridSpacing = grid_spacing
LinkHoverDistance = link_hover_distance
LinkLineSegmentsPerLength = link_line_segments_per_length
LinkThickness = link_thickness
MiniMapOffset = mini_map_offset
MiniMapPadding = mini_map_padding
NodeBorderThickness = node_border_thickness
NodeCornerRounding = node_corner_rounding
NodePadding = node_padding
PinCircleRadius = pin_circle_radius
PinHoverRadius = pin_hover_radius
PinLineThickness = pin_line_thickness
PinOffset = pin_offset
PinQuadSideLength = pin_quad_side_length
PinTriangleSideLength = pin_triangle_side_length