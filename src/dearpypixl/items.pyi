from typing import *
from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import *
from dearpypixl.core.itemtype import *
from dearpypixl.core.parsing import ThemeElementInfo

__all__ = (
    'mvStage', 'stage', 'add_stage',
    'mvWindowAppItem', 'window', 'add_window',
    'mvChildWindow', 'child_window', 'add_child_window',
    'mvTableColumn', 'add_table_column',
    'mvTableRow', 'table_row', 'add_table_row',
    'mvTableCell', 'table_cell', 'add_table_cell',
    'mvTable', 'table', 'add_table',
    'mvThemeComponent', 'theme_component', 'add_theme_component',
    'mvTheme', 'theme', 'add_theme',
    'mvThemeColor', 'add_theme_color',
    'mvThemeStyle', 'add_theme_style',
    'mvFont', 'font', 'add_font',
    'mvFontRegistry', 'font_registry', 'add_font_registry',
    'mvFontChars', 'add_font_chars',
    'mvFontRange', 'add_font_range',
    'mvFontRangeHint', 'add_font_range_hint',
    'mvKeyDownHandler', 'add_key_down_handler',
    'mvKeyPressHandler', 'add_key_press_handler',
    'mvKeyReleaseHandler', 'add_key_release_handler',
    'mvMouseClickHandler', 'add_mouse_click_handler',
    'mvMouseDoubleClickHandler', 'add_mouse_double_click_handler',
    'mvMouseDownHandler', 'add_mouse_down_handler',
    'mvMouseDragHandler', 'add_mouse_drag_handler',
    'mvMouseMoveHandler', 'add_mouse_move_handler',
    'mvMouseReleaseHandler', 'add_mouse_release_handler',
    'mvMouseWheelHandler', 'add_mouse_wheel_handler',
    'mvHandlerRegistry', 'handler_registry', 'add_handler_registry',
    'mvActivatedHandler', 'add_item_activated_handler',
    'mvActiveHandler', 'add_item_active_handler',
    'mvClickedHandler', 'add_item_clicked_handler',
    'mvDeactivatedAfterEditHandler', 'add_item_deactivated_after_edit_handler',
    'mvDeactivatedHandler', 'add_item_deactivated_handler',
    'mvDoubleClickedHandler', 'add_item_double_clicked_handler',
    'mvEditedHandler', 'add_item_edited_handler',
    'mvFocusHandler', 'add_item_focus_handler',
    'mvHoverHandler', 'add_item_hover_handler',
    'mvResizeHandler', 'add_item_resize_handler',
    'mvToggledOpenHandler', 'add_item_toggled_open_handler',
    'mvVisibleHandler', 'add_item_visible_handler',
    'mvItemHandlerRegistry', 'item_handler_registry', 'add_item_handler_registry',
    'mvColorMapRegistry', 'colormap_registry', 'add_colormap_registry',
    'mvColorButton', 'add_color_button',
    'mvColorEdit', 'add_color_edit',
    'mvColorMap', 'add_colormap',
    'mvColorMapButton', 'add_colormap_button',
    'mvColorMapScale', 'add_colormap_scale',
    'mvColorMapSlider', 'add_colormap_slider',
    'mvColorPicker', 'add_color_picker',
    'mvValueRegistry', 'value_registry', 'add_value_registry',
    'mvFloat4Value', 'add_float4_value',
    'mvFloatValue', 'add_float_value',
    'mvFloatVectValue', 'add_float_vect_value',
    'mvInt4Value', 'add_int4_value',
    'mvIntValue', 'add_int_value',
    'mvDouble4Value', 'add_double4_value',
    'mvDoubleValue', 'add_double_value',
    'mvColorValue', 'add_color_value',
    'mvBoolValue', 'add_bool_value',
    'mvTemplateRegistry', 'template_registry', 'add_template_registry',
    'mvTextureRegistry', 'texture_registry', 'add_texture_registry',
    'mvNodeEditor', 'node_editor', 'add_node_editor',
    'mvNode', 'node', 'add_node',
    'mvNodeLink', 'add_node_link',
    'mvNodeAttribute', 'node_attribute', 'add_node_attribute',
    'mvPlotAxis', 'plot_axis', 'add_plot_axis',
    'mvPlot', 'plot', 'add_plot',
    'mvAreaSeries', 'add_area_series',
    'mvBarGroupSeries', 'add_bar_group_series',
    'mvBarSeries', 'add_bar_series',
    'mvCandleSeries', 'add_candle_series',
    'mvCustomSeries', 'custom_series', 'add_custom_series',
    'mvDigitalSeries', 'add_digital_series',
    'mvErrorSeries', 'add_error_series',
    'mvHeatSeries', 'add_heat_series',
    'mvHistogramSeries', 'add_histogram_series',
    'mv2dHistogramSeries', 'add_2d_histogram_series',
    'mvImageSeries', 'add_image_series',
    'mvInfLineSeries', 'add_inf_line_series',
    'mvLabelSeries', 'add_text_point',
    'mvLineSeries', 'add_line_series',
    'mvPieSeries', 'add_pie_series',
    'mvScatterSeries', 'add_scatter_series',
    'mvShadeSeries', 'add_shade_series',
    'mvStairSeries', 'add_stair_series',
    'mvStemSeries', 'add_stem_series',
    'mvAnnotation', 'add_plot_annotation',
    'mvPlotLegend', 'add_plot_legend',
    'mvViewportDrawlist', 'viewport_drawlist', 'add_viewport_drawlist',
    'mvDrawlist', 'drawlist', 'add_drawlist',
    'mvDrawLayer', 'draw_layer', 'add_draw_layer',
    'mvDrawNode', 'draw_node', 'add_draw_node',
    'mvDrawArrow', 'draw_arrow',
    'mvDrawBezierCubic', 'draw_bezier_cubic',
    'mvDrawBezierQuadratic', 'draw_bezier_quadratic',
    'mvDrawCircle', 'draw_circle',
    'mvDrawEllipse', 'draw_ellipse',
    'mvDrawImage', 'draw_image',
    'mvDrawImageQuad', 'draw_image_quad',
    'mvDrawLine', 'draw_line',
    'mvDrawPolygon', 'draw_polygon',
    'mvDrawPolyline', 'draw_polyline',
    'mvDrawQuad', 'draw_quad',
    'mvDrawRect', 'draw_rectangle',
    'mvDrawText', 'draw_text',
    'mvDrawTriangle', 'draw_triangle',
    'mvDatePicker', 'add_date_picker',
    'mvAxisTag', 'add_axis_tag',
    'mvButton', 'add_button',
    'mvCharRemap', 'add_char_remap',
    'mvCheckbox', 'add_checkbox',
    'mvClipper', 'clipper', 'add_clipper',
    'mvCollapsingHeader', 'collapsing_header', 'add_collapsing_header',
    'mvCombo', 'add_combo',
    'mvDragDouble', 'add_drag_double',
    'mvDragDoubleMulti', 'add_drag_doublex',
    'mvDragFloat', 'add_drag_float',
    'mvDragFloatMulti', 'add_drag_floatx',
    'mvDragInt', 'add_drag_int',
    'mvDragIntMulti', 'add_drag_intx',
    'mvDragLine', 'add_drag_line',
    'mvDragPayload', 'drag_payload', 'add_drag_payload',
    'mvDragPoint', 'add_drag_point',
    'mvDragRect', 'add_drag_rect',
    'mvDynamicTexture', 'add_dynamic_texture',
    'mvFileDialog', 'file_dialog', 'add_file_dialog',
    'mvFileExtension', 'add_file_extension',
    'mvFilterSet', 'filter_set', 'add_filter_set',
    'mvGroup', 'group', 'add_group',
    'mvImage', 'add_image',
    'mvImageButton', 'add_image_button',
    'mvInputDouble', 'add_input_double',
    'mvInputDoubleMulti', 'add_input_doublex',
    'mvInputFloat', 'add_input_float',
    'mvInputFloatMulti', 'add_input_floatx',
    'mvInputInt', 'add_input_int',
    'mvInputIntMulti', 'add_input_intx',
    'mvInputText', 'add_input_text',
    'mvKnobFloat', 'add_knob_float',
    'mvListbox', 'add_listbox',
    'mvLoadingIndicator', 'add_loading_indicator',
    'mvMenu', 'menu', 'add_menu',
    'mvMenuBar', 'menu_bar', 'add_menu_bar',
    'mvMenuItem', 'add_menu_item',
    'mvProgressBar', 'add_progress_bar',
    'mvRadioButton', 'add_radio_button',
    'mvRawTexture', 'add_raw_texture',
    'mvSelectable', 'add_selectable',
    'mvSeparator', 'add_separator',
    'mvSeriesValue', 'add_series_value',
    'mvSimplePlot', 'add_simple_plot',
    'mvSlider3D', 'add_3d_slider',
    'mvSliderDouble', 'add_slider_double',
    'mvSliderDoubleMulti', 'add_slider_doublex',
    'mvSliderFloat', 'add_slider_float',
    'mvSliderFloatMulti', 'add_slider_floatx',
    'mvSliderInt', 'add_slider_int',
    'mvSliderIntMulti', 'add_slider_intx',
    'mvSpacer', 'add_spacer',
    'mvStaticTexture', 'add_static_texture',
    'mvStringValue', 'add_string_value',
    'mvSubPlots', 'subplots', 'add_subplots',
    'mvTabBar', 'tab_bar', 'add_tab_bar',
    'mvTab', 'tab', 'add_tab',
    'mvTabButton', 'add_tab_button',
    'mvText', 'add_text',
    'mvTimePicker', 'add_time_picker',
    'mvTooltip', 'tooltip', 'add_tooltip',
    'mvTreeNode', 'tree_node', 'add_tree_node',
    'mvViewportMenuBar', 'viewport_menu_bar', 'add_viewport_menu_bar'
)


class mvStage[U = Any, C: ChildItemT = Any](RootItem[U, C, None]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def stage[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvStage[U]: ...
def add_stage[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvStage[U]: ...


class mvWindowAppItem[U = Any, C: ChildItemT = Any](SupportsRect, RootItem[U, C, None]):
    __slots__ = ()
    x_scroll_max: Property[float, Never, false]
    x_scroll_pos: Property[float, float, false]
    y_scroll_max: Property[float, Never, false]
    y_scroll_pos: Property[float, float, false]
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    min_size: Property[Sequence[int], Sequence[int], false]
    max_size: Property[Sequence[int], Sequence[int], false]
    menubar: Property[bool, bool, false]
    collapsed: Property[bool, bool, false]
    autosize: Property[bool, bool, false]
    no_resize: Property[bool, bool, false]
    unsaved_document: Property[bool, bool, false]
    no_title_bar: Property[bool, bool, false]
    no_move: Property[bool, bool, false]
    no_scrollbar: Property[bool, bool, false]
    no_collapse: Property[bool, bool, false]
    horizontal_scrollbar: Property[bool, bool, false]
    no_focus_on_appearing: Property[bool, bool, false]
    no_bring_to_front_on_focus: Property[bool, bool, false]
    no_close: Property[bool, bool, false]
    no_background: Property[bool, bool, false]
    modal: Property[bool, bool, false]
    popup: Property[bool, bool, false]
    no_saved_settings: Property[bool, bool, false]
    no_open_over_existing_popup: Property[bool, bool, false]
    no_scroll_with_mouse: Property[bool, bool, false]
    on_close: Property[ItemCallback | None, ItemCallback | None, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = (), delay_search: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), menubar: bool = False, collapsed: bool = False, autosize: bool = False, no_resize: bool = False, unsaved_document: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, no_close: bool = False, no_background: bool = False, modal: bool = False, popup: bool = False, no_saved_settings: bool = False, no_open_over_existing_popup: bool = True, no_scroll_with_mouse: bool = False, on_close: ItemCallback | None = None, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = (), delay_search: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), menubar: bool = False, collapsed: bool = False, autosize: bool = False, no_resize: bool = False, unsaved_document: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, no_close: bool = False, no_background: bool = False, modal: bool = False, popup: bool = False, no_saved_settings: bool = False, no_open_over_existing_popup: bool = True, no_scroll_with_mouse: bool = False, on_close: ItemCallback | None = None, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = (), min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), menubar: bool = False, collapsed: bool = False, autosize: bool = False, no_resize: bool = False, unsaved_document: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, no_close: bool = False, no_background: bool = False, modal: bool = False, popup: bool = False, no_saved_settings: bool = False, no_open_over_existing_popup: bool = True, no_scroll_with_mouse: bool = False, on_close: ItemCallback | None = None) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "show", "min_size", "max_size", "menubar", "collapsed", "autosize", "no_resize", "unsaved_document", "no_title_bar", "no_move", "no_scrollbar", "no_collapse", "horizontal_scrollbar", "no_focus_on_appearing", "no_bring_to_front_on_focus", "no_close", "no_background", "modal", "popup", "no_saved_settings", "no_open_over_existing_popup", "no_scroll_with_mouse", "on_close"], Any]: ...

def window[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = (), delay_search: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), menubar: bool = False, collapsed: bool = False, autosize: bool = False, no_resize: bool = False, unsaved_document: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, no_close: bool = False, no_background: bool = False, modal: bool = False, popup: bool = False, no_saved_settings: bool = False, no_open_over_existing_popup: bool = True, no_scroll_with_mouse: bool = False, on_close: ItemCallback | None = None, **kwargs) -> mvWindowAppItem[U]: ...
def add_window[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = (), delay_search: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), menubar: bool = False, collapsed: bool = False, autosize: bool = False, no_resize: bool = False, unsaved_document: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, no_close: bool = False, no_background: bool = False, modal: bool = False, popup: bool = False, no_saved_settings: bool = False, no_open_over_existing_popup: bool = True, no_scroll_with_mouse: bool = False, on_close: ItemCallback | None = None, **kwargs) -> mvWindowAppItem[U]: ...


class mvChildWindow[U = Any, P: ContainerItemT = Any](SupportsRect, ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    x_scroll_max: Property[float, Never, false]
    x_scroll_pos: Property[float, float, false]
    y_scroll_max: Property[float, Never, false]
    y_scroll_pos: Property[float, float, false]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    border: Property[bool, bool, false]
    autosize_x: Property[bool, bool, false]
    autosize_y: Property[bool, bool, false]
    no_scrollbar: Property[bool, bool, false]
    horizontal_scrollbar: Property[bool, bool, false]
    menubar: Property[bool, bool, false]
    no_scroll_with_mouse: Property[bool, bool, false]
    flattened_navigation: Property[bool, bool, false]
    always_use_window_padding: Property[bool, bool, false]
    resizable_x: Property[bool, bool, false]
    resizable_y: Property[bool, bool, false]
    always_auto_resize: Property[bool, bool, false]
    frame_style: Property[bool, bool, false]
    auto_resize_x: Property[bool, bool, false]
    auto_resize_y: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, no_scroll_with_mouse: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, no_scroll_with_mouse: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, no_scroll_with_mouse: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "drop_callback", "show", "filter_key", "tracked", "track_offset", "border", "autosize_x", "autosize_y", "no_scrollbar", "horizontal_scrollbar", "menubar", "no_scroll_with_mouse", "flattened_navigation", "always_use_window_padding", "resizable_x", "resizable_y", "always_auto_resize", "frame_style", "auto_resize_x", "auto_resize_y"], Any]: ...

def child_window[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, no_scroll_with_mouse: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False, **kwargs) -> mvChildWindow[U]: ...
def add_child_window[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, no_scroll_with_mouse: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False, **kwargs) -> mvChildWindow[U]: ...


class mvTableColumn[U = Any](ChildItem[U, None, mvTable]):
    __slots__ = ()
    width: Property[int, int, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    init_width_or_weight: Property[float, float, false]
    width_stretch: Property[bool, bool, false]
    width_fixed: Property[bool, bool, false]
    no_resize: Property[bool, bool, false]
    no_reorder: Property[bool, bool, false]
    no_hide: Property[bool, bool, false]
    no_clip: Property[bool, bool, false]
    no_sort: Property[bool, bool, false]
    no_sort_ascending: Property[bool, bool, false]
    no_sort_descending: Property[bool, bool, false]
    no_header_width: Property[bool, bool, false]
    prefer_sort_ascending: Property[bool, bool, false]
    prefer_sort_descending: Property[bool, bool, false]
    indent_enable: Property[bool, bool, false]
    indent_disable: Property[bool, bool, false]
    angled_header: Property[bool, bool, false]
    no_header_label: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, enabled: bool = True, init_width_or_weight: float = 0.0, default_hide: bool = False, default_sort: bool = False, width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False, no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False, no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False, no_header_width: bool = False, prefer_sort_ascending: bool = True, prefer_sort_descending: bool = False, indent_enable: bool = False, indent_disable: bool = False, angled_header: bool = False, no_header_label: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, enabled: bool = True, init_width_or_weight: float = 0.0, default_hide: bool = False, default_sort: bool = False, width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False, no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False, no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False, no_header_width: bool = False, prefer_sort_ascending: bool = True, prefer_sort_descending: bool = False, indent_enable: bool = False, indent_disable: bool = False, angled_header: bool = False, no_header_label: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, show: bool = True, enabled: bool = True, init_width_or_weight: float = 0.0, width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False, no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False, no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False, no_header_width: bool = False, prefer_sort_ascending: bool = True, prefer_sort_descending: bool = False, indent_enable: bool = False, indent_disable: bool = False, angled_header: bool = False, no_header_label: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "show", "enabled", "init_width_or_weight", "width_stretch", "width_fixed", "no_resize", "no_reorder", "no_hide", "no_clip", "no_sort", "no_sort_ascending", "no_sort_descending", "no_header_width", "prefer_sort_ascending", "prefer_sort_descending", "indent_enable", "indent_disable", "angled_header", "no_header_label"], Any]: ...

def add_table_column[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, enabled: bool = True, init_width_or_weight: float = 0.0, default_hide: bool = False, default_sort: bool = False, width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False, no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False, no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False, no_header_width: bool = False, prefer_sort_ascending: bool = True, prefer_sort_descending: bool = False, indent_enable: bool = False, indent_disable: bool = False, angled_header: bool = False, no_header_label: bool = False, **kwargs) -> mvTableColumn[U]: ...


class mvTableRow[U = Any](ChildContainerItem[U, None, mvTable, Any]):
    __slots__ = ()
    height: Property[int, int, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, height: int = 0, show: bool = True, filter_key: str = '') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "height", "show", "filter_key"], Any]: ...

def table_row[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> mvTableRow[U]: ...
def add_table_row[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> mvTableRow[U]: ...


class mvTableCell[U = Any](ChildContainerItem[U, None, mvTableRow, Any]):
    __slots__ = ()
    height: Property[int, int, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, height: int = 0, show: bool = True, filter_key: str = '') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "height", "show", "filter_key"], Any]: ...

def table_cell[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> mvTableCell[U]: ...
def add_table_cell[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, height: int = 0, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', **kwargs) -> mvTableCell[U]: ...


class mvTable[U = Any, P: ContainerItemT = Any](SupportsRect, SupportsCallback[ItemCallback2], ChildContainerItem[U, str | None, P, mvTableRow]):
    __slots__ = ()
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    header_row: Property[bool, bool, false]
    clipper: Property[bool, bool, false]
    inner_width: Property[int, int, false]
    policy: Property[int, int, false]
    freeze_rows: Property[int, int, false]
    freeze_columns: Property[int, int, false]
    sort_multi: Property[bool, bool, false]
    sort_tristate: Property[bool, bool, false]
    resizable: Property[bool, bool, false]
    reorderable: Property[bool, bool, false]
    hideable: Property[bool, bool, false]
    sortable: Property[bool, bool, false]
    context_menu_in_body: Property[bool, bool, false]
    row_background: Property[bool, bool, false]
    borders_innerH: Property[bool, bool, false]
    borders_outerH: Property[bool, bool, false]
    borders_innerV: Property[bool, bool, false]
    borders_outerV: Property[bool, bool, false]
    no_host_extendX: Property[bool, bool, false]
    no_host_extendY: Property[bool, bool, false]
    no_keep_columns_visible: Property[bool, bool, false]
    precise_widths: Property[bool, bool, false]
    no_clip: Property[bool, bool, false]
    pad_outerX: Property[bool, bool, false]
    no_pad_outerX: Property[bool, bool, false]
    no_pad_innerX: Property[bool, bool, false]
    scrollX: Property[bool, bool, false]
    scrollY: Property[bool, bool, false]
    no_saved_settings: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0, freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False, sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False, borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False, no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False, no_saved_settings: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0, freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False, sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False, borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False, no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False, no_saved_settings: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0, freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False, sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False, borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False, no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False, no_saved_settings: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "callback", "show", "filter_key", "header_row", "clipper", "inner_width", "policy", "freeze_rows", "freeze_columns", "sort_multi", "sort_tristate", "resizable", "reorderable", "hideable", "sortable", "context_menu_in_body", "row_background", "borders_innerH", "borders_outerH", "borders_innerV", "borders_outerV", "no_host_extendX", "no_host_extendY", "no_keep_columns_visible", "precise_widths", "no_clip", "pad_outerX", "no_pad_outerX", "no_pad_innerX", "scrollX", "scrollY", "no_saved_settings"], Any]: ...
    def index(self, item: Item, /) -> int: ...
    def is_cell_highlighted(self, irow: int, icol: int, /) -> bool: ...
    def is_column_highlighted(self, icol: int, /) -> bool: ...
    def is_row_highlighted(self, irow: int, /) -> bool: ...
    def set_cell_highlight(self, irow: int, icol: int, color: RGBA | None, /): ...
    def set_column_highlight(self, icol: int, color: RGBA | None, /): ...
    def set_row_highlight(self, irow: int, color: RGBA | None, /): ...
    def set_row_color(self, irow: int, color: RGBA | None, /): ...

def table[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0, freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False, sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False, borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False, no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False, no_saved_settings: bool = False, **kwargs) -> mvTable[U]: ...
def add_table[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0, freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False, sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False, borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False, no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False, no_saved_settings: bool = False, **kwargs) -> mvTable[U]: ...


class mvThemeComponent[U = Any](ThemeAPI, ChildContainerItem[U, None, mvTheme, ElementItem]):
    __slots__ = ()
    enabled_state: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(item_type: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, item_type: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, enabled_state: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "enabled_state"], Any]: ...

def theme_component[U: Any](item_type: int = 0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> mvThemeComponent[U]: ...
def add_theme_component[U: Any](item_type: int = 0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> mvThemeComponent[U]: ...


class mvTheme[U = Any, C: mvThemeComponent = mvThemeComponent](ThemeAPI, RootItem[U, C, None]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def theme[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvTheme[U]: ...
def add_theme[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvTheme[U]: ...


class mvThemeColor[U = Any, V: int | float = float](ThemeAPI, ChildValueArrayItem[U, V, mvThemeComponent]):
    __slots__ = ()
    category: Property[int, Never, false]
    target: Property[int, Never, false]
    @staticmethod
    def __itemtype_command__(target: int = 0, value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, target: int = 0, value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "category", "target"], Any]: ...
    def identity(self, /) -> ThemeElementInfo: ...

def add_theme_color[U: Any](target: int = 0, value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> mvThemeColor[U]: ...


class mvThemeStyle[U = Any, V: int | float = float](ThemeAPI, ChildValueArrayItem[U, V, mvThemeComponent]):
    __slots__ = ()
    category: Property[int, Never, false]
    target: Property[int, Never, false]
    @staticmethod
    def __itemtype_command__(target: int = 0, x: float = 1.0, y: float = -1.0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, target: int = 0, x: float = 1.0, y: float = -1.0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "category", "target"], Any]: ...
    def identity(self, /) -> ThemeElementInfo: ...

def add_theme_style[U: Any](target: int = 0, x: float = 1.0, y: float = -1.0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, category: int = 0, **kwargs) -> mvThemeStyle[U]: ...


class mvFont[U = Any](FontAPI, ChildContainerItem[U, None, mvFontRegistry, Any]):
    __slots__ = ()
    pixel_snapH: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(file: str, size: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, pixel_snapH: bool = False, parent: Item = 10, **kwargs) -> Item: ...
    @classmethod
    def create(cls, file: str, size: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, pixel_snapH: bool = False, parent: Item = 10, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, pixel_snapH: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "pixel_snapH"], Any]: ...

def font[U: Any](file: str, size: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, pixel_snapH: bool = False, parent: Item = 10, **kwargs) -> mvFont[U]: ...
def add_font[U: Any](file: str, size: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, pixel_snapH: bool = False, parent: Item = 10, **kwargs) -> mvFont[U]: ...


class mvFontRegistry[U = Any, C: mvFont = mvFont](FontAPI, RootItem[U, C, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...

def font_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvFontRegistry[U]: ...
def add_font_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvFontRegistry[U]: ...


class mvFontChars[U = Any](FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(chars: Sequence[int], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, chars: Sequence[int], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_font_chars[U: Any](chars: Sequence[int], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> mvFontChars[U]: ...


class mvFontRange[U = Any](FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(first_char: int, last_char: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, first_char: int, last_char: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_font_range[U: Any](first_char: int, last_char: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> mvFontRange[U]: ...


class mvFontRangeHint[U = Any](FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(hint: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, hint: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_font_range_hint[U: Any](hint: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> mvFontRangeHint[U]: ...


class mvKeyDownHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    key: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, key: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "key"], Any]: ...

def add_key_down_handler[U: Any](key: int = 0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvKeyDownHandler[U]: ...


class mvKeyPressHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    key: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, key: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "key"], Any]: ...

def add_key_press_handler[U: Any](key: int = 0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvKeyPressHandler[U]: ...


class mvKeyReleaseHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    key: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, key: int = 0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, key: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "key"], Any]: ...

def add_key_release_handler[U: Any](key: int = 0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvKeyReleaseHandler[U]: ...


class mvMouseClickHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_mouse_click_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseClickHandler[U]: ...


class mvMouseDoubleClickHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_mouse_double_click_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseDoubleClickHandler[U]: ...


class mvMouseDownHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_mouse_down_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseDownHandler[U]: ...


class mvMouseDragHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, threshold: float = 10.0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, threshold: float = 10.0, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_mouse_drag_handler[U: Any](button: int = -1, threshold: float = 10.0, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseDragHandler[U]: ...


class mvMouseMoveHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_mouse_move_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseMoveHandler[U]: ...


class mvMouseReleaseHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_mouse_release_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseReleaseHandler[U]: ...


class mvMouseWheelHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_mouse_wheel_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, callback: ItemCallback | None = None, show: bool = True, parent: Item = 11, **kwargs) -> mvMouseWheelHandler[U]: ...


class mvHandlerRegistry[U = Any, C: ChildItemT = HandlerItem](RootItem[U, C, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...
    @overload
    def on_mouse_click(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseClickHandler]: ...
    @overload
    def on_mouse_click(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseClickHandler: ...
    @overload
    def on_mouse_click_down(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseDownHandler]: ...
    @overload
    def on_mouse_click_down(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseDownHandler: ...
    @overload
    def on_mouse_click_up(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseReleaseHandler]: ...
    @overload
    def on_mouse_click_up(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseReleaseHandler: ...
    @overload
    def on_mouse_double_click(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseDoubleClickHandler]: ...
    @overload
    def on_mouse_double_click(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseDoubleClickHandler: ...
    @overload
    def on_mouse_wheel(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseWheelHandler]: ...
    @overload
    def on_mouse_wheel(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseWheelHandler: ...
    @overload
    def on_mouse_move(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseMoveHandler]: ...
    @overload
    def on_mouse_move(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseMoveHandler: ...
    @overload
    def on_mouse_drag(self, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvMouseDragHandler]: ...
    @overload
    def on_mouse_drag(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvMouseDragHandler: ...
    @overload
    def on_key_down(self, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvKeyDownHandler]: ...
    @overload
    def on_key_down(self, callback: ItemCallback, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvKeyDownHandler: ...
    @overload
    def on_key_press(self, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvKeyPressHandler]: ...
    @overload
    def on_key_press(self, callback: ItemCallback, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvKeyPressHandler: ...
    @overload
    def on_key_up(self, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvKeyReleaseHandler]: ...
    @overload
    def on_key_up(self, callback: ItemCallback, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvKeyReleaseHandler: ...

def handler_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvHandlerRegistry[U]: ...
def add_handler_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvHandlerRegistry[U]: ...


class mvActivatedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_activated_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvActivatedHandler[U]: ...


class mvActiveHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_active_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvActiveHandler[U]: ...


class mvClickedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_item_clicked_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvClickedHandler[U]: ...


class mvDeactivatedAfterEditHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_deactivated_after_edit_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvDeactivatedAfterEditHandler[U]: ...


class mvDeactivatedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_deactivated_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvDeactivatedHandler[U]: ...


class mvDoubleClickedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    button: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, button: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, button: int = -1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "button"], Any]: ...

def add_item_double_clicked_handler[U: Any](button: int = -1, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvDoubleClickedHandler[U]: ...


class mvEditedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_edited_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvEditedHandler[U]: ...


class mvFocusHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_focus_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvFocusHandler[U]: ...


class mvHoverHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_hover_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvHoverHandler[U]: ...


class mvResizeHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_resize_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvResizeHandler[U]: ...


class mvToggledOpenHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_toggled_open_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvToggledOpenHandler[U]: ...


class mvVisibleHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, mvItemHandlerRegistry, CB]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show"], Any]: ...

def add_item_visible_handler[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, callback: ItemCallback | None = None, show: bool = True, **kwargs) -> mvVisibleHandler[U]: ...


class mvItemHandlerRegistry[U = Any, C: ChildItemT = HandlerItem](RootItem[U, C, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...
    @overload
    def on_resize(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvResizeHandler]: ...
    @overload
    def on_resize(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvResizeHandler: ...
    @overload
    def on_click(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvClickedHandler]: ...
    @overload
    def on_click(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvClickedHandler: ...
    @overload
    def on_toggle_open(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvToggledOpenHandler]: ...
    @overload
    def on_toggle_open(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvToggledOpenHandler: ...
    @overload
    def on_edit(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvEditedHandler]: ...
    @overload
    def on_edit(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvEditedHandler: ...
    @overload
    def on_deactivation_after_edit(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvDeactivatedAfterEditHandler]: ...
    @overload
    def on_deactivation_after_edit(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvDeactivatedAfterEditHandler: ...
    @overload
    def on_activation(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvActivatedHandler]: ...
    @overload
    def on_activation(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvActivatedHandler: ...
    @overload
    def on_deactivation(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvDeactivatedHandler]: ...
    @overload
    def on_deactivation(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvDeactivatedHandler: ...
    @overload
    def while_active(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvActiveHandler]: ...
    @overload
    def while_active(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvActiveHandler: ...
    @overload
    def while_visible(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvVisibleHandler]: ...
    @overload
    def while_visible(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvVisibleHandler: ...
    @overload
    def while_focused(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvFocusHandler]: ...
    @overload
    def while_focused(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvFocusHandler: ...
    @overload
    def while_hovered(self, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Callable[[ItemCallback], mvHoverHandler]: ...
    @overload
    def while_hovered(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvHoverHandler: ...

def item_handler_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvItemHandlerRegistry[U]: ...
def add_item_handler_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, **kwargs) -> mvItemHandlerRegistry[U]: ...


class mvColorMapRegistry[U = Any](RootItem[U, Any, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...

def colormap_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> mvColorMapRegistry[U]: ...
def add_colormap_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> mvColorMapRegistry[U]: ...


class mvColorButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    no_alpha: Property[bool, bool, false]
    no_border: Property[bool, bool, false]
    no_drag_drop: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_border: bool = False, no_drag_drop: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_border: bool = False, no_drag_drop: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_border: bool = False, no_drag_drop: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "no_alpha", "no_border", "no_drag_drop"], Any]: ...

def add_color_button[U: Any](default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_border: bool = False, no_drag_drop: bool = False, **kwargs) -> mvColorButton[U]: ...


class mvColorEdit[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    no_alpha: Property[bool, bool, false]
    no_picker: Property[bool, bool, false]
    no_options: Property[bool, bool, false]
    no_small_preview: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    no_tooltip: Property[bool, bool, false]
    no_label: Property[bool, bool, false]
    no_drag_drop: Property[bool, bool, false]
    alpha_bar: Property[bool, bool, false]
    alpha_preview: Property[int, int, false]
    display_mode: Property[int, int, false]
    display_type: Property[int, int, false]
    input_mode: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_picker: bool = False, no_options: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, no_drag_drop: bool = False, alpha_bar: bool = False, alpha_preview: int = 0, display_mode: int = 1048576, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> Item: ...
    @classmethod
    def create(cls, default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_picker: bool = False, no_options: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, no_drag_drop: bool = False, alpha_bar: bool = False, alpha_preview: int = 0, display_mode: int = 1048576, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_picker: bool = False, no_options: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, no_drag_drop: bool = False, alpha_bar: bool = False, alpha_preview: int = 0, display_mode: int = 1048576, display_type: int = 8388608, input_mode: int = 134217728) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "no_alpha", "no_picker", "no_options", "no_small_preview", "no_inputs", "no_tooltip", "no_label", "no_drag_drop", "alpha_bar", "alpha_preview", "display_mode", "display_type", "input_mode"], Any]: ...

def add_color_edit[U: Any](default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_picker: bool = False, no_options: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, no_drag_drop: bool = False, alpha_bar: bool = False, alpha_preview: int = 0, display_mode: int = 1048576, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> mvColorEdit[U]: ...


class mvColorMap[U = Any](ChildItem[U, None, mvColorMapRegistry]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(colors: list[list[int] | tuple[int, ...]], qualitative: bool, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, parent: Item = 14, **kwargs) -> Item: ...
    @classmethod
    def create(cls, colors: list[list[int] | tuple[int, ...]], qualitative: bool, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, parent: Item = 14, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...

def add_colormap[U: Any](colors: list[list[int] | tuple[int, ...]], qualitative: bool, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, parent: Item = 14, **kwargs) -> mvColorMap[U]: ...


class mvColorMapButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Item: ...
    @classmethod
    def create(cls, default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset"], Any]: ...

def add_colormap_button[U: Any](default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, **kwargs) -> mvColorMapButton[U]: ...


class mvColorMapScale[U = Any, P: ContainerItemT = Any](SupportsRect, ChildItem[U, None, P]):
    __slots__ = ()
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    colormap: Property[int | str, int | str, false]
    min_scale: Property[float, float, false]
    max_scale: Property[float, float, false]
    format: Property[str, str, false]
    reverse_dir: Property[bool, bool, false]
    mirror: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), colormap: int | str = 0, min_scale: float = 0.0, max_scale: float = 1.0, format: str = '%g', reverse_dir: bool = False, mirror: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), colormap: int | str = 0, min_scale: float = 0.0, max_scale: float = 1.0, format: str = '%g', reverse_dir: bool = False, mirror: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), colormap: int | str = 0, min_scale: float = 0.0, max_scale: float = 1.0, format: str = '%g', reverse_dir: bool = False, mirror: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "drop_callback", "show", "colormap", "min_scale", "max_scale", "format", "reverse_dir", "mirror"], Any]: ...

def add_colormap_scale[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), colormap: int | str = 0, min_scale: float = 0.0, max_scale: float = 1.0, format: str = '%g', reverse_dir: bool = False, mirror: bool = False, **kwargs) -> mvColorMapScale[U]: ...


class mvColorMapSlider[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsCallback[CB], ChildItem[U, float, P]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "callback", "drop_callback", "show", "filter_key", "tracked", "track_offset"], Any]: ...

def add_colormap_slider[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, **kwargs) -> mvColorMapSlider[U]: ...


class mvColorPicker[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    no_alpha: Property[bool, bool, false]
    no_side_preview: Property[bool, bool, false]
    no_small_preview: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    no_tooltip: Property[bool, bool, false]
    no_label: Property[bool, bool, false]
    alpha_bar: Property[bool, bool, false]
    display_rgb: Property[bool, bool, false]
    display_hsv: Property[bool, bool, false]
    display_hex: Property[bool, bool, false]
    picker_mode: Property[int, int, false]
    alpha_preview: Property[int, int, false]
    display_type: Property[int, int, false]
    input_mode: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_side_preview: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, alpha_bar: bool = False, display_rgb: bool = False, display_hsv: bool = False, display_hex: bool = False, picker_mode: int = 33554432, alpha_preview: int = 0, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> Item: ...
    @classmethod
    def create(cls, default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_side_preview: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, alpha_bar: bool = False, display_rgb: bool = False, display_hsv: bool = False, display_hex: bool = False, picker_mode: int = 33554432, alpha_preview: int = 0, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_side_preview: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, alpha_bar: bool = False, display_rgb: bool = False, display_hsv: bool = False, display_hex: bool = False, picker_mode: int = 33554432, alpha_preview: int = 0, display_type: int = 8388608, input_mode: int = 134217728) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "no_alpha", "no_side_preview", "no_small_preview", "no_inputs", "no_tooltip", "no_label", "alpha_bar", "display_rgb", "display_hsv", "display_hex", "picker_mode", "alpha_preview", "display_type", "input_mode"], Any]: ...

def add_color_picker[U: Any](default_value: Sequence[int] = (0, 0, 0, 255), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_alpha: bool = False, no_side_preview: bool = False, no_small_preview: bool = False, no_inputs: bool = False, no_tooltip: bool = False, no_label: bool = False, alpha_bar: bool = False, display_rgb: bool = False, display_hsv: bool = False, display_hex: bool = False, picker_mode: int = 33554432, alpha_preview: int = 0, display_type: int = 8388608, input_mode: int = 134217728, **kwargs) -> mvColorPicker[U]: ...


class mvValueRegistry[U = Any, C: ChildItemT = ChildItem](RootItem[U, C, None]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def value_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvValueRegistry[U]: ...
def add_value_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvValueRegistry[U]: ...


class mvFloat4Value[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_float4_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> mvFloat4Value[U]: ...


class mvFloatValue[U = Any](ChildItem[U, float, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_float_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> mvFloatValue[U]: ...


class mvFloatVectValue[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_float_vect_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (), parent: Item = 13, **kwargs) -> mvFloatVectValue[U]: ...


class mvInt4Value[U = Any](ChildValueArrayItem[U, int, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[int] = (0, 0, 0, 0), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[int] = (0, 0, 0, 0), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_int4_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[int] = (0, 0, 0, 0), parent: Item = 13, **kwargs) -> mvInt4Value[U]: ...


class mvIntValue[U = Any](ChildItem[U, int, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: int = 0, parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: int = 0, parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_int_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: int = 0, parent: Item = 13, **kwargs) -> mvIntValue[U]: ...


class mvDouble4Value[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_double4_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> mvDouble4Value[U]: ...


class mvDoubleValue[U = Any](ChildItem[U, float, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_double_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: float = 0.0, parent: Item = 13, **kwargs) -> mvDoubleValue[U]: ...


class mvColorValue[U = Any, V: int | float = float](ChildValueArrayItem[U, V, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_color_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), parent: Item = 13, **kwargs) -> mvColorValue[U]: ...


class mvBoolValue[U = Any, V: bool = bool](ChildItem[U, V, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: bool = False, parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: bool = False, parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_bool_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: bool = False, parent: Item = 13, **kwargs) -> mvBoolValue[U]: ...


class mvTemplateRegistry[U = Any, C: ChildItemT = Any](RootItem[U, C, None]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def template_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvTemplateRegistry[U]: ...
def add_template_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvTemplateRegistry[U]: ...


class mvTextureRegistry[U = Any, C: ChildItemT = Any](RootItem[U, C, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...

def texture_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> mvTextureRegistry[U]: ...
def add_texture_registry[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = False, **kwargs) -> mvTextureRegistry[U]: ...


class mvNodeEditor[U = Any, P: ContainerItemT = Any](SupportsCallback[ItemCallback2 | ItemCallback3], ChildContainerItem[U, None, P, mvNode]):
    __slots__ = ()
    width: Property[int, int, false]
    height: Property[int, int, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    delink_callback: Property[ItemCallback | None, ItemCallback | None, false]
    menubar: Property[bool, bool, false]
    minimap: Property[bool, bool, false]
    minimap_location: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, delink_callback: ItemCallback | None = None, menubar: bool = False, minimap: bool = False, minimap_location: int = 2, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, delink_callback: ItemCallback | None = None, menubar: bool = False, minimap: bool = False, minimap_location: int = 2, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, delink_callback: ItemCallback | None = None, menubar: bool = False, minimap: bool = False, minimap_location: int = 2) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "callback", "show", "filter_key", "tracked", "track_offset", "delink_callback", "menubar", "minimap", "minimap_location"], Any]: ...
    def selected_nodes(self, /) -> list[Item]: ...
    def selected_links(self, /) -> list[Item]: ...
    def clear_selected_nodes(self, /) -> None: ...
    def clear_selected_links(self, /) -> None: ...

def node_editor[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, delink_callback: ItemCallback | None = None, menubar: bool = False, minimap: bool = False, minimap_location: int = 2, **kwargs) -> mvNodeEditor[U]: ...
def add_node_editor[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, delink_callback: ItemCallback | None = None, menubar: bool = False, minimap: bool = False, minimap_location: int = 2, **kwargs) -> mvNodeEditor[U]: ...


class mvNode[U = Any](ChildContainerItem[U, None, mvNodeEditor, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    draggable: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, draggable: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, draggable: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, draggable: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "draggable"], Any]: ...

def node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, draggable: bool = True, **kwargs) -> mvNode[U]: ...
def add_node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, draggable: bool = True, **kwargs) -> mvNode[U]: ...


class mvNodeLink[U = Any](ChildItem[U, None, mvNodeEditor]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(attr_1: int | str, attr_2: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, attr_1: int | str, attr_2: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...

def add_node_link[U: Any](attr_1: int | str, attr_2: int | str, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> mvNodeLink[U]: ...


class mvNodeAttribute[U = Any](ChildContainerItem[U, None, mvNode, Any]):
    __slots__ = ()
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    attribute_type: Property[int, int, false]
    shape: Property[int, int, false]
    category: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, attribute_type: int = 0, shape: int = 1, category: str = 'general', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, attribute_type: int = 0, shape: int = 1, category: str = 'general', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, attribute_type: int = 0, shape: int = 1, category: str = 'general') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "show", "filter_key", "tracked", "track_offset", "attribute_type", "shape", "category"], Any]: ...

def node_attribute[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, attribute_type: int = 0, shape: int = 1, category: str = 'general', **kwargs) -> mvNodeAttribute[U]: ...
def add_node_attribute[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, attribute_type: int = 0, shape: int = 1, category: str = 'general', **kwargs) -> mvNodeAttribute[U]: ...


class mvPlotAxis[U = Any](ChildContainerItem[U, None, mvPlot, Any]):
    __slots__ = ()
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    no_label: Property[bool, bool, false]
    no_gridlines: Property[bool, bool, false]
    no_tick_marks: Property[bool, bool, false]
    no_tick_labels: Property[bool, bool, false]
    no_initial_fit: Property[bool, bool, false]
    no_menus: Property[bool, bool, false]
    no_side_switch: Property[bool, bool, false]
    no_highlight: Property[bool, bool, false]
    opposite: Property[bool, bool, false]
    foreground_grid: Property[bool, bool, false]
    tick_format: Property[str, str, false]
    scale: Property[int, int, false]
    invert: Property[bool, bool, false]
    auto_fit: Property[bool, bool, false]
    range_fit: Property[bool, bool, false]
    pan_stretch: Property[bool, bool, false]
    lock_min: Property[bool, bool, false]
    lock_max: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(axis: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = 0, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, axis: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = 0, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = 0, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "payload_type", "drop_callback", "show", "no_label", "no_gridlines", "no_tick_marks", "no_tick_labels", "no_initial_fit", "no_menus", "no_side_switch", "no_highlight", "opposite", "foreground_grid", "tick_format", "scale", "invert", "auto_fit", "range_fit", "pan_stretch", "lock_min", "lock_max"], Any]: ...
    def set_pan_limits(self, /, vmin: float, vmax: float) -> None: ...
    def reset_pan_limits(self) -> None: ...
    def set_zoom_limits(self, /, vmin: float, vmax: float) -> None: ...
    def reset_zoom_limits(self) -> None: ...
    def set_ticks(self, label_pairs: Sequence[tuple[str, int | str] | Sequence[str | int]]): ...
    def reset_ticks(self): ...
    def auto_fit_data(self): ...

def plot_axis[U: Any](axis: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = 0, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False, **kwargs) -> mvPlotAxis[U]: ...
def add_plot_axis[U: Any](axis: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = 0, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False, **kwargs) -> mvPlotAxis[U]: ...


class mvPlot[U = Any, P: ContainerItemT = Any](SupportsRect, SupportsCallback, ChildContainerItem[U, None, P, mvPlotAxis]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    no_title: Property[bool, bool, false]
    no_menus: Property[bool, bool, false]
    no_box_select: Property[bool, bool, false]
    no_mouse_pos: Property[bool, bool, false]
    query: Property[bool, bool, false]
    query_color: Property[Sequence[float], Sequence[float], false]
    min_query_rects: Property[int, int, false]
    max_query_rects: Property[int, int, false]
    crosshairs: Property[bool, bool, false]
    equal_aspects: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    no_frame: Property[bool, bool, false]
    use_local_time: Property[bool, bool, false]
    use_ISO8601: Property[bool, bool, false]
    use_24hour_clock: Property[bool, bool, false]
    pan_button: Property[int, int, false]
    pan_mod: Property[int, int, false]
    context_menu_button: Property[int, int, false]
    fit_button: Property[int, int, false]
    box_select_button: Property[int, int, false]
    box_select_mod: Property[int, int, false]
    box_select_cancel_button: Property[int, int, false]
    query_toggle_mod: Property[int, int, false]
    horizontal_mod: Property[int, int, false]
    vertical_mod: Property[int, int, false]
    override_mod: Property[int, int, false]
    zoom_mod: Property[int, int, false]
    zoom_rate: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, no_title: bool = False, no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, query: bool = False, query_color: Sequence[float] = (0, 255, 0, 255), min_query_rects: int = 1, max_query_rects: int = 1, crosshairs: bool = False, equal_aspects: bool = False, no_inputs: bool = False, no_frame: bool = False, use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False, pan_button: int = 0, pan_mod: int = 0, context_menu_button: int = 1, fit_button: int = 0, box_select_button: int = 1, box_select_mod: int = 0, box_select_cancel_button: int = 0, query_toggle_mod: int = 4096, horizontal_mod: int = 16384, vertical_mod: int = 8192, override_mod: int = 4096, zoom_mod: int = 0, zoom_rate: float = 0.1, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, no_title: bool = False, no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, query: bool = False, query_color: Sequence[float] = (0, 255, 0, 255), min_query_rects: int = 1, max_query_rects: int = 1, crosshairs: bool = False, equal_aspects: bool = False, no_inputs: bool = False, no_frame: bool = False, use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False, pan_button: int = 0, pan_mod: int = 0, context_menu_button: int = 1, fit_button: int = 0, box_select_button: int = 1, box_select_mod: int = 0, box_select_cancel_button: int = 0, query_toggle_mod: int = 4096, horizontal_mod: int = 16384, vertical_mod: int = 8192, override_mod: int = 4096, zoom_mod: int = 0, zoom_rate: float = 0.1, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_title: bool = False, no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, query: bool = False, query_color: Sequence[float] = (0, 255, 0, 255), min_query_rects: int = 1, max_query_rects: int = 1, crosshairs: bool = False, equal_aspects: bool = False, no_inputs: bool = False, no_frame: bool = False, use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False, pan_button: int = 0, pan_mod: int = 0, context_menu_button: int = 1, fit_button: int = 0, box_select_button: int = 1, box_select_mod: int = 0, box_select_cancel_button: int = 0, query_toggle_mod: int = 4096, horizontal_mod: int = 16384, vertical_mod: int = 8192, override_mod: int = 4096, zoom_mod: int = 0, zoom_rate: float = 0.1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "no_title", "no_menus", "no_box_select", "no_mouse_pos", "query", "query_color", "min_query_rects", "max_query_rects", "crosshairs", "equal_aspects", "no_inputs", "no_frame", "use_local_time", "use_ISO8601", "use_24hour_clock", "pan_button", "pan_mod", "context_menu_button", "fit_button", "box_select_button", "box_select_mod", "box_select_cancel_button", "query_toggle_mod", "horizontal_mod", "vertical_mod", "override_mod", "zoom_mod", "zoom_rate"], Any]: ...
    def index(self, axis: Item, /) -> int: ...
    def auto_fit_data(self, iaxis: SupportsIndex) -> None: ...
    def get_axis_limits(self, iaxis: SupportsIndex) -> list[float]: ...
    def set_axis_limits(self, iaxis: SupportsIndex, ymin: float, ymax: float): ...
    def reset_axis_limits(self, iaxis: SupportsIndex): ...
    def set_axis_ticks(self, iaxis: SupportsIndex, label_pairs: Sequence[tuple[str, int | str] | Sequence[str | int]]): ...
    def reset_axis_ticks(self, iaxis: SupportsIndex): ...

def plot[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, no_title: bool = False, no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, query: bool = False, query_color: Sequence[float] = (0, 255, 0, 255), min_query_rects: int = 1, max_query_rects: int = 1, crosshairs: bool = False, equal_aspects: bool = False, no_inputs: bool = False, no_frame: bool = False, use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False, pan_button: int = 0, pan_mod: int = 0, context_menu_button: int = 1, fit_button: int = 0, box_select_button: int = 1, box_select_mod: int = 0, box_select_cancel_button: int = 0, query_toggle_mod: int = 4096, horizontal_mod: int = 16384, vertical_mod: int = 8192, override_mod: int = 4096, zoom_mod: int = 0, zoom_rate: float = 0.1, **kwargs) -> mvPlot[U]: ...
def add_plot[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, no_title: bool = False, no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, query: bool = False, query_color: Sequence[float] = (0, 255, 0, 255), min_query_rects: int = 1, max_query_rects: int = 1, crosshairs: bool = False, equal_aspects: bool = False, no_inputs: bool = False, no_frame: bool = False, use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False, pan_button: int = 0, pan_mod: int = 0, context_menu_button: int = 1, fit_button: int = 0, box_select_button: int = 1, box_select_mod: int = 0, box_select_cancel_button: int = 0, query_toggle_mod: int = 4096, horizontal_mod: int = 16384, vertical_mod: int = 8192, override_mod: int = 4096, zoom_mod: int = 0, zoom_rate: float = 0.1, **kwargs) -> mvPlot[U]: ...


class mvAreaSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    fill: Property[Sequence[int], Sequence[int], false]
    contribute_to_bounds: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, fill: Sequence[int] = (0, 0, 0, -255), contribute_to_bounds: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, fill: Sequence[int] = (0, 0, 0, -255), contribute_to_bounds: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, fill: Sequence[int] = (0, 0, 0, -255), contribute_to_bounds: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "fill", "contribute_to_bounds"], Any]: ...

def add_area_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, fill: Sequence[int] = (0, 0, 0, -255), contribute_to_bounds: bool = True, **kwargs) -> mvAreaSeries[U]: ...


class mvBarGroupSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    group_width: Property[float, float, false]
    shift: Property[int, int, false]
    horizontal: Property[bool, bool, false]
    stacked: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(values: Sequence[float], label_ids: Sequence[str], group_size: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, group_width: float = 0.67, shift: int = 0, horizontal: bool = False, stacked: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, values: Sequence[float], label_ids: Sequence[str], group_size: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, group_width: float = 0.67, shift: int = 0, horizontal: bool = False, stacked: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, group_width: float = 0.67, shift: int = 0, horizontal: bool = False, stacked: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "group_width", "shift", "horizontal", "stacked"], Any]: ...

def add_bar_group_series[U: Any](values: Sequence[float], label_ids: Sequence[str], group_size: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, group_width: float = 0.67, shift: int = 0, horizontal: bool = False, stacked: bool = False, **kwargs) -> mvBarGroupSeries[U]: ...


class mvBarSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    weight: Property[float, float, false]
    horizontal: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, weight: float = 1.0, horizontal: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, weight: float = 1.0, horizontal: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, weight: float = 1.0, horizontal: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "weight", "horizontal"], Any]: ...

def add_bar_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, weight: float = 1.0, horizontal: bool = False, **kwargs) -> mvBarSeries[U]: ...


class mvCandleSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    bull_color: Property[Sequence[int], Sequence[int], false]
    bear_color: Property[Sequence[int], Sequence[int], false]
    weight: Property[float, float, false]
    tooltip: Property[bool, bool, false]
    time_unit: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(dates: Sequence[float], opens: Sequence[float], closes: Sequence[float], lows: Sequence[float], highs: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bull_color: Sequence[int] = (0, 255, 113, 255), bear_color: Sequence[int] = (218, 13, 79, 255), weight: float = 0.25, tooltip: bool = True, time_unit: int = 5, **kwargs) -> Item: ...
    @classmethod
    def create(cls, dates: Sequence[float], opens: Sequence[float], closes: Sequence[float], lows: Sequence[float], highs: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bull_color: Sequence[int] = (0, 255, 113, 255), bear_color: Sequence[int] = (218, 13, 79, 255), weight: float = 0.25, tooltip: bool = True, time_unit: int = 5, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, bull_color: Sequence[int] = (0, 255, 113, 255), bear_color: Sequence[int] = (218, 13, 79, 255), weight: float = 0.25, tooltip: bool = True, time_unit: int = 5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "bull_color", "bear_color", "weight", "tooltip", "time_unit"], Any]: ...

def add_candle_series[U: Any](dates: Sequence[float], opens: Sequence[float], closes: Sequence[float], lows: Sequence[float], highs: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bull_color: Sequence[int] = (0, 255, 113, 255), bear_color: Sequence[int] = (218, 13, 79, 255), weight: float = 0.25, tooltip: bool = True, time_unit: int = 5, **kwargs) -> mvCandleSeries[U]: ...


class mvCustomSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildContainerItem[U, list[V], mvPlotAxis, Any]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    y1: Property[Any, Any, false]
    y2: Property[Any, Any, false]
    y3: Property[Any, Any, false]
    tooltip: Property[bool, bool, false]
    no_fit: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, y1: Any = (), y2: Any = (), y3: Any = (), tooltip: bool = True, no_fit: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, y1: Any = (), y2: Any = (), y3: Any = (), tooltip: bool = True, no_fit: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, y1: Any = (), y2: Any = (), y3: Any = (), tooltip: bool = True, no_fit: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "callback", "show", "y1", "y2", "y3", "tooltip", "no_fit"], Any]: ...

def custom_series[U: Any](x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, y1: Any = (), y2: Any = (), y3: Any = (), tooltip: bool = True, no_fit: bool = False, **kwargs) -> mvCustomSeries[U]: ...
def add_custom_series[U: Any](x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, y1: Any = (), y2: Any = (), y3: Any = (), tooltip: bool = True, no_fit: bool = False, **kwargs) -> mvCustomSeries[U]: ...


class mvDigitalSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show"], Any]: ...

def add_digital_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, **kwargs) -> mvDigitalSeries[U]: ...


class mvErrorSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    contribute_to_bounds: Property[bool, bool, false]
    horizontal: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], negative: Sequence[float], positive: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, contribute_to_bounds: bool = True, horizontal: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], negative: Sequence[float], positive: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, contribute_to_bounds: bool = True, horizontal: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, contribute_to_bounds: bool = True, horizontal: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "contribute_to_bounds", "horizontal"], Any]: ...

def add_error_series[U: Any](x: Sequence[float], y: Sequence[float], negative: Sequence[float], positive: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, contribute_to_bounds: bool = True, horizontal: bool = False, **kwargs) -> mvErrorSeries[U]: ...


class mvHeatSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    scale_min: Property[float, float, false]
    scale_max: Property[float, float, false]
    bounds_min: Property[Any, Any, false]
    bounds_max: Property[Any, Any, false]
    format: Property[str, str, false]
    contribute_to_bounds: Property[bool, bool, false]
    col_major: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], rows: int, cols: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, scale_min: float = 0.0, scale_max: float = 1.0, bounds_min: Any = (0.0, 0.0), bounds_max: Any = (1.0, 1.0), format: str = '%0.1f', contribute_to_bounds: bool = True, col_major: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], rows: int, cols: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, scale_min: float = 0.0, scale_max: float = 1.0, bounds_min: Any = (0.0, 0.0), bounds_max: Any = (1.0, 1.0), format: str = '%0.1f', contribute_to_bounds: bool = True, col_major: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, scale_min: float = 0.0, scale_max: float = 1.0, bounds_min: Any = (0.0, 0.0), bounds_max: Any = (1.0, 1.0), format: str = '%0.1f', contribute_to_bounds: bool = True, col_major: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "scale_min", "scale_max", "bounds_min", "bounds_max", "format", "contribute_to_bounds", "col_major"], Any]: ...

def add_heat_series[U: Any](x: Sequence[float], rows: int, cols: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, scale_min: float = 0.0, scale_max: float = 1.0, bounds_min: Any = (0.0, 0.0), bounds_max: Any = (1.0, 1.0), format: str = '%0.1f', contribute_to_bounds: bool = True, col_major: bool = False, **kwargs) -> mvHeatSeries[U]: ...


class mvHistogramSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    bins: Property[int, int, false]
    bar_scale: Property[float, float, false]
    min_range: Property[float, float, false]
    max_range: Property[float, float, false]
    cumulative: Property[bool, bool, false]
    density: Property[bool, bool, false]
    outliers: Property[bool, bool, false]
    horizontal: Property[bool, bool, false]
    contribute_to_bounds: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bins: int = -1, bar_scale: float = 1.0, min_range: float = 0.0, max_range: float = 0.0, cumulative: bool = False, density: bool = False, outliers: bool = True, horizontal: bool = False, contribute_to_bounds: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bins: int = -1, bar_scale: float = 1.0, min_range: float = 0.0, max_range: float = 0.0, cumulative: bool = False, density: bool = False, outliers: bool = True, horizontal: bool = False, contribute_to_bounds: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, bins: int = -1, bar_scale: float = 1.0, min_range: float = 0.0, max_range: float = 0.0, cumulative: bool = False, density: bool = False, outliers: bool = True, horizontal: bool = False, contribute_to_bounds: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "bins", "bar_scale", "min_range", "max_range", "cumulative", "density", "outliers", "horizontal", "contribute_to_bounds"], Any]: ...

def add_histogram_series[U: Any](x: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, bins: int = -1, bar_scale: float = 1.0, min_range: float = 0.0, max_range: float = 0.0, cumulative: bool = False, density: bool = False, outliers: bool = True, horizontal: bool = False, contribute_to_bounds: bool = True, **kwargs) -> mvHistogramSeries[U]: ...


class mv2dHistogramSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    xbins: Property[int, int, false]
    ybins: Property[int, int, false]
    xmin_range: Property[float, float, false]
    xmax_range: Property[float, float, false]
    ymin_range: Property[float, float, false]
    ymax_range: Property[float, float, false]
    density: Property[bool, bool, false]
    outliers: Property[bool, bool, false]
    col_major: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, xbins: int = -1, ybins: int = -1, xmin_range: float = 0.0, xmax_range: float = 0.0, ymin_range: float = 0.0, ymax_range: float = 0.0, density: bool = False, outliers: bool = False, col_major: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, xbins: int = -1, ybins: int = -1, xmin_range: float = 0.0, xmax_range: float = 0.0, ymin_range: float = 0.0, ymax_range: float = 0.0, density: bool = False, outliers: bool = False, col_major: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, xbins: int = -1, ybins: int = -1, xmin_range: float = 0.0, xmax_range: float = 0.0, ymin_range: float = 0.0, ymax_range: float = 0.0, density: bool = False, outliers: bool = False, col_major: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "xbins", "ybins", "xmin_range", "xmax_range", "ymin_range", "ymax_range", "density", "outliers", "col_major"], Any]: ...

def add_2d_histogram_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, xbins: int = -1, ybins: int = -1, xmin_range: float = 0.0, xmax_range: float = 0.0, ymin_range: float = 0.0, ymax_range: float = 0.0, density: bool = False, outliers: bool = False, col_major: bool = False, **kwargs) -> mv2dHistogramSeries[U]: ...


class mvImageSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    uv_min: Property[Sequence[float], Sequence[float], false]
    uv_max: Property[Sequence[float], Sequence[float], false]
    tint_color: Property[Sequence[int], Sequence[int], false]
    @staticmethod
    def __itemtype_command__(texture_tag: int | str, bounds_min: Sequence[float], bounds_max: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), tint_color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Item: ...
    @classmethod
    def create(cls, texture_tag: int | str, bounds_min: Sequence[float], bounds_max: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), tint_color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), tint_color: Sequence[int] = (255, 255, 255, 255)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "uv_min", "uv_max", "tint_color"], Any]: ...

def add_image_series[U: Any](texture_tag: int | str, bounds_min: Sequence[float], bounds_max: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), tint_color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> mvImageSeries[U]: ...


class mvInfLineSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    horizontal: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, horizontal: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "horizontal"], Any]: ...

def add_inf_line_series[U: Any](x: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> mvInfLineSeries[U]: ...


class mvLabelSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    offset: Property[Sequence[float], Sequence[float], false]
    vertical: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: float, y: float, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, offset: Sequence[float] = (0.0, 0.0), vertical: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: float, y: float, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, offset: Sequence[float] = (0.0, 0.0), vertical: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, offset: Sequence[float] = (0.0, 0.0), vertical: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "offset", "vertical"], Any]: ...

def add_text_point[U: Any](x: float, y: float, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, offset: Sequence[float] = (0.0, 0.0), vertical: bool = False, **kwargs) -> mvLabelSeries[U]: ...


class mvLineSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    segments: Property[bool, bool, false]
    loop: Property[bool, bool, false]
    skip_nan: Property[bool, bool, false]
    no_clip: Property[bool, bool, false]
    shaded: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, segments: bool = False, loop: bool = False, skip_nan: bool = False, no_clip: bool = False, shaded: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, segments: bool = False, loop: bool = False, skip_nan: bool = False, no_clip: bool = False, shaded: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, segments: bool = False, loop: bool = False, skip_nan: bool = False, no_clip: bool = False, shaded: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "segments", "loop", "skip_nan", "no_clip", "shaded"], Any]: ...

def add_line_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, segments: bool = False, loop: bool = False, skip_nan: bool = False, no_clip: bool = False, shaded: bool = False, **kwargs) -> mvLineSeries[U]: ...


class mvPieSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    format: Property[str, str, false]
    angle: Property[float, float, false]
    normalize: Property[bool, bool, false]
    ignore_hidden: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: float, y: float, radius: float, values: Sequence[float], labels: Sequence[str], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, format: str = '%0.2f', angle: float = 90.0, normalize: bool = False, ignore_hidden: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: float, y: float, radius: float, values: Sequence[float], labels: Sequence[str], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, format: str = '%0.2f', angle: float = 90.0, normalize: bool = False, ignore_hidden: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, format: str = '%0.2f', angle: float = 90.0, normalize: bool = False, ignore_hidden: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "format", "angle", "normalize", "ignore_hidden"], Any]: ...

def add_pie_series[U: Any](x: float, y: float, radius: float, values: Sequence[float], labels: Sequence[str], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, format: str = '%0.2f', angle: float = 90.0, normalize: bool = False, ignore_hidden: bool = False, **kwargs) -> mvPieSeries[U]: ...


class mvScatterSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    no_clip: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, no_clip: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, no_clip: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, no_clip: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "no_clip"], Any]: ...

def add_scatter_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, no_clip: bool = False, **kwargs) -> mvScatterSeries[U]: ...


class mvShadeSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    y2: Property[Any, Any, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y1: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, y2: Any = (), **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y1: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, y2: Any = (), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, y2: Any = ()) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "y2"], Any]: ...

def add_shade_series[U: Any](x: Sequence[float], y1: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, y2: Any = (), **kwargs) -> mvShadeSeries[U]: ...


class mvStairSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    pre_step: Property[bool, bool, false]
    shaded: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, pre_step: bool = False, shaded: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, pre_step: bool = False, shaded: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, pre_step: bool = False, shaded: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "pre_step", "shaded"], Any]: ...

def add_stair_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, pre_step: bool = False, shaded: bool = False, **kwargs) -> mvStairSeries[U]: ...


class mvStemSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    horizontal: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, source: int | str = 0, show: bool = True, horizontal: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "source", "show", "horizontal"], Any]: ...

def add_stem_series[U: Any](x: Sequence[float], y: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, horizontal: bool = False, **kwargs) -> mvStemSeries[U]: ...


class mvAnnotation[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    offset: Property[Sequence[float], Sequence[float], false]
    color: Property[Sequence[int], Sequence[int], false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: Any = (0.0, 0.0), offset: Sequence[float] = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), clamped: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: Any = (0.0, 0.0), offset: Sequence[float] = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), clamped: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, offset: Sequence[float] = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), clamped: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "offset", "color", "clamped"], Any]: ...

def add_plot_annotation[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: Any = (0.0, 0.0), offset: Sequence[float] = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), clamped: bool = True, **kwargs) -> mvAnnotation[U]: ...


class mvPlotLegend[U = Any](ChildItem[U, None, mvPlot]):
    __slots__ = ()
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    location: Property[int, int, false]
    horizontal: Property[bool, bool, false]
    sort: Property[bool, bool, false]
    outside: Property[bool, bool, false]
    no_highlight_item: Property[bool, bool, false]
    no_highlight_axis: Property[bool, bool, false]
    no_menus: Property[bool, bool, false]
    no_buttons: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, location: int = 5, horizontal: bool = False, sort: bool = False, outside: bool = False, no_highlight_item: bool = False, no_highlight_axis: bool = False, no_menus: bool = False, no_buttons: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, location: int = 5, horizontal: bool = False, sort: bool = False, outside: bool = False, no_highlight_item: bool = False, no_highlight_axis: bool = False, no_menus: bool = False, no_buttons: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, location: int = 5, horizontal: bool = False, sort: bool = False, outside: bool = False, no_highlight_item: bool = False, no_highlight_axis: bool = False, no_menus: bool = False, no_buttons: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "payload_type", "drop_callback", "show", "location", "horizontal", "sort", "outside", "no_highlight_item", "no_highlight_axis", "no_menus", "no_buttons"], Any]: ...

def add_plot_legend[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, location: int = 5, horizontal: bool = False, sort: bool = False, outside: bool = False, no_highlight_item: bool = False, no_highlight_axis: bool = False, no_menus: bool = False, no_buttons: bool = False, **kwargs) -> mvPlotLegend[U]: ...


class mvViewportDrawlist[U = Any, C: ChildItemT = Any](DrawingAPI, RootItem[U, C, None]):
    __slots__ = ()
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    front: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, filter_key: str = '', delay_search: bool = False, front: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, filter_key: str = '', delay_search: bool = False, front: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, filter_key: str = '', front: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "filter_key", "front"], Any]: ...

def viewport_drawlist[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, filter_key: str = '', delay_search: bool = False, front: bool = True, **kwargs) -> mvViewportDrawlist[U]: ...
def add_viewport_drawlist[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, filter_key: str = '', delay_search: bool = False, front: bool = True, **kwargs) -> mvViewportDrawlist[U]: ...


class mvDrawlist[U = Any, P: ContainerItemT = Any](SupportsRect, SupportsCallback, DrawingAPI, ChildContainerItem[U, P, Any, Any]):
    __slots__ = ()
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(width: int, height: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Item: ...
    @classmethod
    def create(cls, width: int, height: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "callback", "show", "filter_key", "tracked", "track_offset"], Any]: ...

def drawlist[U: Any](width: int, height: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> mvDrawlist[U]: ...
def add_drawlist[U: Any](width: int, height: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> mvDrawlist[U]: ...


class mvDrawLayer[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] = Any](DrawingAPI, ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    show: Property[bool, bool, false]
    perspective_divide: Property[bool, bool, false]
    depth_clipping: Property[bool, bool, false]
    cull_mode: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "perspective_divide", "depth_clipping", "cull_mode"], Any]: ...
    def set_clip_space(self, top_left_x: float, top_left_y: float, width: float, height: float, min_depth: float, max_depth: float) -> None: ...

def draw_layer[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0, **kwargs) -> mvDrawLayer[U]: ...
def add_draw_layer[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0, **kwargs) -> mvDrawLayer[U]: ...


class mvDrawNode[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show"], Any]: ...
    def apply_transform(self, transform: Vec4[float]) -> None: ...

def draw_node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawNode[U]: ...
def add_draw_node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawNode[U]: ...


class mvDrawArrow[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    size: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, size: int = 4, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, size: int = 4, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, size: int = 4) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "thickness", "size"], Any]: ...

def draw_arrow[U: Any](p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, size: int = 4, **kwargs) -> mvDrawArrow[U]: ...


class mvDrawBezierCubic[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    segments: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "thickness", "segments"], Any]: ...

def draw_bezier_cubic[U: Any](p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> mvDrawBezierCubic[U]: ...


class mvDrawBezierQuadratic[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    segments: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "thickness", "segments"], Any]: ...

def draw_bezier_quadratic[U: Any](p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, **kwargs) -> mvDrawBezierQuadratic[U]: ...


class mvDrawCircle[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    segments: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(center: Sequence[float], radius: float, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, center: Sequence[float], radius: float, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "thickness", "segments"], Any]: ...

def draw_circle[U: Any](center: Sequence[float], radius: float, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 0, **kwargs) -> mvDrawCircle[U]: ...


class mvDrawEllipse[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    segments: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 32, **kwargs) -> Item: ...
    @classmethod
    def create(cls, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 32, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 32) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "thickness", "segments"], Any]: ...

def draw_ellipse[U: Any](pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 32, **kwargs) -> mvDrawEllipse[U]: ...


class mvDrawImage[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    uv_min: Property[Sequence[float], Sequence[float], false]
    uv_max: Property[Sequence[float], Sequence[float], false]
    color: Property[Sequence[int], Sequence[int], false]
    @staticmethod
    def __itemtype_command__(texture_tag: int | str, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Item: ...
    @classmethod
    def create(cls, texture_tag: int | str, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), color: Sequence[int] = (255, 255, 255, 255)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "uv_min", "uv_max", "color"], Any]: ...

def draw_image[U: Any](texture_tag: int | str, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> mvDrawImage[U]: ...


class mvDrawImageQuad[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    uv1: Property[Sequence[float], Sequence[float], false]
    uv2: Property[Sequence[float], Sequence[float], false]
    uv3: Property[Sequence[float], Sequence[float], false]
    uv4: Property[Sequence[float], Sequence[float], false]
    color: Property[Sequence[int], Sequence[int], false]
    @staticmethod
    def __itemtype_command__(texture_tag: int | str, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv1: Sequence[float] = (0.0, 0.0), uv2: Sequence[float] = (1.0, 0.0), uv3: Sequence[float] = (1.0, 1.0), uv4: Sequence[float] = (0.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Item: ...
    @classmethod
    def create(cls, texture_tag: int | str, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv1: Sequence[float] = (0.0, 0.0), uv2: Sequence[float] = (1.0, 0.0), uv3: Sequence[float] = (1.0, 1.0), uv4: Sequence[float] = (0.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, uv1: Sequence[float] = (0.0, 0.0), uv2: Sequence[float] = (1.0, 0.0), uv3: Sequence[float] = (1.0, 1.0), uv4: Sequence[float] = (0.0, 1.0), color: Sequence[int] = (255, 255, 255, 255)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "uv1", "uv2", "uv3", "uv4", "color"], Any]: ...

def draw_image_quad[U: Any](texture_tag: int | str, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, uv1: Sequence[float] = (0.0, 0.0), uv2: Sequence[float] = (1.0, 0.0), uv3: Sequence[float] = (1.0, 1.0), uv4: Sequence[float] = (0.0, 1.0), color: Sequence[int] = (255, 255, 255, 255), **kwargs) -> mvDrawImageQuad[U]: ...


class mvDrawLine[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "thickness"], Any]: ...

def draw_line[U: Any](p1: Sequence[float], p2: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> mvDrawLine[U]: ...


class mvDrawPolygon[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(points: list[list[float]], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, points: list[list[float]], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "thickness"], Any]: ...

def draw_polygon[U: Any](points: list[list[float]], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> mvDrawPolygon[U]: ...


class mvDrawPolyline[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    closed: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(points: list[list[float]], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, closed: bool = False, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, points: list[list[float]], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, closed: bool = False, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, closed: bool = False, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "closed", "color", "thickness"], Any]: ...

def draw_polyline[U: Any](points: list[list[float]], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, closed: bool = False, color: Sequence[int] = (255, 255, 255, 255), thickness: float = 1.0, **kwargs) -> mvDrawPolyline[U]: ...


class mvDrawQuad[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "thickness"], Any]: ...

def draw_quad[U: Any](p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> mvDrawQuad[U]: ...


class mvDrawRect[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    multicolor: Property[bool, bool, false]
    rounding: Property[float, float, false]
    thickness: Property[float, float, false]
    corner_colors: Property[Any, Any, false]
    @staticmethod
    def __itemtype_command__(pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), multicolor: bool = False, rounding: float = 0.0, thickness: float = 1.0, corner_colors: Any = None, **kwargs) -> Item: ...
    @classmethod
    def create(cls, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), multicolor: bool = False, rounding: float = 0.0, thickness: float = 1.0, corner_colors: Any = None, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), multicolor: bool = False, rounding: float = 0.0, thickness: float = 1.0, corner_colors: Any = None) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "multicolor", "rounding", "thickness", "corner_colors"], Any]: ...

def draw_rectangle[U: Any](pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), multicolor: bool = False, rounding: float = 0.0, thickness: float = 1.0, corner_colors: Any = None, **kwargs) -> mvDrawRect[U]: ...


class mvDrawText[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    size: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(pos: Sequence[float], text: str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), size: float = 10.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, pos: Sequence[float], text: str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), size: float = 10.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), size: float = 10.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "size"], Any]: ...

def draw_text[U: Any](pos: Sequence[float], text: str, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), size: float = 10.0, **kwargs) -> mvDrawText[U]: ...


class mvDrawTriangle[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any, Any] | mvWindowAppItem[Any, Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any] = Any](DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    fill: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "color", "fill", "thickness"], Any]: ...

def draw_triangle[U: Any](p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, show: bool = True, color: Sequence[int] = (255, 255, 255, 255), fill: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, **kwargs) -> mvDrawTriangle[U]: ...


class mvDatePicker[U = Any, P: ContainerItemT = Any](ChildItem[U, dict[Literal['sec', 'min', 'hour', 'month_day', 'month', 'year', 'week_day', 'year_day', 'daylight_savings'], int], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    level: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'month_day': 14, 'year': 20, 'month': 5}, level: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'month_day': 14, 'year': 20, 'month': 5}, level: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, level: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "level"], Any]: ...

def add_date_picker[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'month_day': 14, 'year': 20, 'month': 5}, level: int = 0, **kwargs) -> mvDatePicker[U]: ...


class mvAxisTag[U = Any](ChildItem[U, float, mvPlotAxis]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    auto_rounding: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), auto_rounding: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), auto_rounding: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, show: bool = True, color: Sequence[int] = (0, 0, 0, -255), auto_rounding: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "show", "color", "auto_rounding"], Any]: ...

def add_axis_tag[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), auto_rounding: bool = False, **kwargs) -> mvAxisTag[U]: ...


class mvButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsCallback[CB], ChildItem[U, bool, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    small: Property[bool, bool, false]
    arrow: Property[bool, bool, false]
    direction: Property[int, int, false]
    repeat: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, small: bool = False, arrow: bool = False, direction: int = 0, repeat: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, small: bool = False, arrow: bool = False, direction: int = 0, repeat: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, small: bool = False, arrow: bool = False, direction: int = 0, repeat: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "small", "arrow", "direction", "repeat"], Any]: ...

def add_button[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, small: bool = False, arrow: bool = False, direction: int = 0, repeat: bool = False, **kwargs) -> mvButton[U]: ...


class mvCharRemap[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(source: int, target: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, source: int, target: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_char_remap[U: Any](source: int, target: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, **kwargs) -> mvCharRemap[U]: ...


class mvCheckbox[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset"], Any]: ...

def add_checkbox[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, **kwargs) -> mvCheckbox[U]: ...


class mvClipper[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    width: Property[int, int, false]
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "show"], Any]: ...

def clipper[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvClipper[U]: ...
def add_clipper[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvClipper[U]: ...


class mvCollapsingHeader[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool, Any, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    closable: Property[bool, bool, false]
    open_on_double_click: Property[bool, bool, false]
    open_on_arrow: Property[bool, bool, false]
    leaf: Property[bool, bool, false]
    bullet: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, closable: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "closable", "open_on_double_click", "open_on_arrow", "leaf", "bullet"], Any]: ...

def collapsing_header[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, **kwargs) -> mvCollapsingHeader[U]: ...
def add_collapsing_header[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, **kwargs) -> mvCollapsingHeader[U]: ...


class mvCombo[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, str, P, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    popup_align_left: Property[bool, bool, false]
    no_arrow_button: Property[bool, bool, false]
    no_preview: Property[bool, bool, false]
    fit_width: Property[bool, bool, false]
    height_mode: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', popup_align_left: bool = False, no_arrow_button: bool = False, no_preview: bool = False, fit_width: bool = False, height_mode: int = 1, **kwargs) -> Item: ...
    @classmethod
    def create(cls, items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', popup_align_left: bool = False, no_arrow_button: bool = False, no_preview: bool = False, fit_width: bool = False, height_mode: int = 1, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, popup_align_left: bool = False, no_arrow_button: bool = False, no_preview: bool = False, fit_width: bool = False, height_mode: int = 1) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "popup_align_left", "no_arrow_button", "no_preview", "fit_width", "height_mode"], Any]: ...

def add_combo[U: Any](items: Sequence[str] = (), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', popup_align_left: bool = False, no_arrow_button: bool = False, no_preview: bool = False, fit_width: bool = False, height_mode: int = 1, **kwargs) -> mvCombo[U]: ...


class mvDragDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_double[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragDouble[U]: ...


class mvDragDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_doublex[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragDoubleMulti[U]: ...


class mvDragFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_float[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragFloat[U]: ...


class mvDragFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_floatx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, format: str = '%0.3f', speed: float = 1.0, min_value: float = 0.0, max_value: float = 100.0, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragFloatMulti[U]: ...


class mvDragInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_int[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragInt[U]: ...


class mvDragIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    format: Property[str, str, false]
    speed: Property[float, float, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "format", "speed", "min_value", "max_value", "no_input", "clamped"], Any]: ...

def add_drag_intx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, format: str = '%d', speed: float = 1.0, min_value: int = 0, max_value: int = 100, no_input: bool = False, clamped: bool = False, **kwargs) -> mvDragIntMulti[U]: ...


class mvDragLine[U = Any](ChildItem[U, float, mvPlot]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    show_label: Property[bool, bool, false]
    vertical: Property[bool, bool, false]
    delayed: Property[bool, bool, false]
    no_cursor: Property[bool, bool, false]
    no_fit: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, vertical: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, vertical: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, vertical: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "callback", "show", "color", "thickness", "show_label", "vertical", "delayed", "no_cursor", "no_fit", "no_inputs"], Any]: ...

def add_drag_line[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: float = 0.0, color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, vertical: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> mvDragLine[U]: ...


class mvDragPayload[U = Any, P: AppItem[Any, Any, Any] = Any](ChildContainerItem[U, None, P, Any]):  # type: ignore
    __slots__ = ()
    show: Property[bool, bool, false]
    drag_data: Property[Any, Any, false]
    drop_data: Property[Any, Any, false]
    payload_type: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, drag_data: Any = None, drop_data: Any = None, payload_type: str = '$$DPG_PAYLOAD', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, drag_data: Any = None, drop_data: Any = None, payload_type: str = '$$DPG_PAYLOAD', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, drag_data: Any = None, drop_data: Any = None, payload_type: str = '$$DPG_PAYLOAD') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "drag_data", "drop_data", "payload_type"], Any]: ...

def drag_payload[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, drag_data: Any = None, drop_data: Any = None, payload_type: str = '$$DPG_PAYLOAD', **kwargs) -> mvDragPayload[U]: ...
def add_drag_payload[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, drag_data: Any = None, drop_data: Any = None, payload_type: str = '$$DPG_PAYLOAD', **kwargs) -> mvDragPayload[U]: ...


class mvDragPoint[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    thickness: Property[float, float, false]
    show_label: Property[bool, bool, false]
    offset: Property[Sequence[float], Sequence[float], false]
    clamped: Property[bool, bool, false]
    delayed: Property[bool, bool, false]
    no_cursor: Property[bool, bool, false]
    no_fit: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, offset: Sequence[float] = (16.0, 8.0), clamped: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, offset: Sequence[float] = (16.0, 8.0), clamped: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, offset: Sequence[float] = (16.0, 8.0), clamped: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "callback", "show", "color", "thickness", "show_label", "offset", "clamped", "delayed", "no_cursor", "no_fit", "no_inputs"], Any]: ...

def add_drag_point[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), thickness: float = 1.0, show_label: bool = True, offset: Sequence[float] = (16.0, 8.0), clamped: bool = True, delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> mvDragPoint[U]: ...


class mvDragRect[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    delayed: Property[bool, bool, false]
    no_cursor: Property[bool, bool, false]
    no_fit: Property[bool, bool, false]
    no_inputs: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0, 0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0, 0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, color: Sequence[int] = (0, 0, 0, -255), delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source", "callback", "show", "color", "delayed", "no_cursor", "no_fit", "no_inputs"], Any]: ...

def add_drag_rect[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, before: Item = 0, source: int | str = 0, callback: ItemCallback | None = None, show: bool = True, default_value: Any = (0.0, 0.0, 0.0, 0.0), color: Sequence[int] = (0, 0, 0, -255), delayed: bool = False, no_cursor: bool = False, no_fit: bool = False, no_inputs: bool = False, **kwargs) -> mvDragRect[U]: ...


class mvDynamicTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> Item: ...
    @classmethod
    def create(cls, width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_dynamic_texture[U: Any](width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> mvDynamicTexture[U]: ...


class mvFileDialog[U = Any, C: ChildItemT = Any](RootItem[U, C, bool]):
    __slots__ = ()
    width: Property[int, int, false]
    height: Property[int, int, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    file_count: Property[int, int, false]
    modal: Property[bool, bool, false]
    directory_selector: Property[bool, bool, false]
    min_size: Property[Sequence[int], Sequence[int], false]
    max_size: Property[Sequence[int], Sequence[int], false]
    cancel_callback: Property[ItemCallback | None, ItemCallback | None, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, default_path: str = '', default_filename: str = '.', file_count: int = 0, modal: bool = False, directory_selector: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), cancel_callback: ItemCallback | None = None, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, default_path: str = '', default_filename: str = '.', file_count: int = 0, modal: bool = False, directory_selector: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), cancel_callback: ItemCallback | None = None, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, file_count: int = 0, modal: bool = False, directory_selector: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), cancel_callback: ItemCallback | None = None) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "callback", "show", "file_count", "modal", "directory_selector", "min_size", "max_size", "cancel_callback"], Any]: ...

def file_dialog[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, default_path: str = '', default_filename: str = '.', file_count: int = 0, modal: bool = False, directory_selector: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), cancel_callback: ItemCallback | None = None, **kwargs) -> mvFileDialog[U]: ...
def add_file_dialog[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, callback: ItemCallback | None = None, show: bool = True, default_path: str = '', default_filename: str = '.', file_count: int = 0, modal: bool = False, directory_selector: bool = False, min_size: Sequence[int] = (100, 100), max_size: Sequence[int] = (30000, 30000), cancel_callback: ItemCallback | None = None, **kwargs) -> mvFileDialog[U]: ...


class mvFileExtension[U = Any](ChildItem[U, None, mvFileDialog]):
    __slots__ = ()
    width: Property[int, int, false]
    height: Property[int, int, false]
    custom_text: Property[str, str, false]
    color: Property[Sequence[int], Sequence[int], false]
    @staticmethod
    def __itemtype_command__(extension: str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, custom_text: str = '', color: Sequence[int] = (-255, 0, 0, 255), **kwargs) -> Item: ...
    @classmethod
    def create(cls, extension: str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, custom_text: str = '', color: Sequence[int] = (-255, 0, 0, 255), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, custom_text: str = '', color: Sequence[int] = (-255, 0, 0, 255)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "custom_text", "color"], Any]: ...

def add_file_extension[U: Any](extension: str, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, parent: Item = 0, before: Item = 0, custom_text: str = '', color: Sequence[int] = (-255, 0, 0, 255), **kwargs) -> mvFileExtension[U]: ...


class mvFilterSet[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, str, P, Any]):
    __slots__ = ()
    width: Property[int, int, false]
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "show"], Any]: ...

def filter_set[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvFilterSet[U]: ...
def add_filter_set[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvFilterSet[U]: ...


class mvGroup[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    horizontal: Property[bool, bool, false]
    horizontal_spacing: Property[float, float, false]
    xoffset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "horizontal", "horizontal_spacing", "xoffset"], Any]: ...

def group[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0.0, **kwargs) -> mvGroup[U]: ...
def add_group[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0.0, **kwargs) -> mvGroup[U]: ...


class mvImage[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    tint_color: Property[Sequence[float], Sequence[float], false]
    border_color: Property[Sequence[float], Sequence[float], false]
    uv_min: Property[Sequence[float], Sequence[float], false]
    uv_max: Property[Sequence[float], Sequence[float], false]
    @staticmethod
    def __itemtype_command__(texture_tag: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), border_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> Item: ...
    @classmethod
    def create(cls, texture_tag: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), border_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), border_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "tint_color", "border_color", "uv_min", "uv_max"], Any]: ...

def add_image[U: Any](texture_tag: int | str, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), border_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> mvImage[U]: ...


class mvImageButton[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    tint_color: Property[Sequence[float], Sequence[float], false]
    background_color: Property[Sequence[float], Sequence[float], false]
    uv_min: Property[Sequence[float], Sequence[float], false]
    uv_max: Property[Sequence[float], Sequence[float], false]
    @staticmethod
    def __itemtype_command__(texture_tag: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), background_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> Item: ...
    @classmethod
    def create(cls, texture_tag: int | str, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), background_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), background_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "tint_color", "background_color", "uv_min", "uv_max"], Any]: ...

def add_image_button[U: Any](texture_tag: int | str, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, tint_color: Sequence[float] = (255, 255, 255, 255), background_color: Sequence[float] = (0, 0, 0, 0), uv_min: Sequence[float] = (0.0, 0.0), uv_max: Sequence[float] = (1.0, 1.0), **kwargs) -> mvImageButton[U]: ...


class mvInputDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    step: Property[float, float, false]
    step_fast: Property[float, float, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "min_value", "max_value", "step", "step_fast", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_double[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputDouble[U]: ...


class mvInputDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    size: Property[int, int, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "min_value", "max_value", "size", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_doublex[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputDoubleMulti[U]: ...


class mvInputFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    step: Property[float, float, false]
    step_fast: Property[float, float, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "min_value", "max_value", "step", "step_fast", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_float[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, step: float = 0.1, step_fast: float = 1.0, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputFloat[U]: ...


class mvInputFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    format: Property[str, str, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    size: Property[int, int, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "format", "min_value", "max_value", "size", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_floatx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), format: str = '%.3f', min_value: float = 0.0, max_value: float = 100.0, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputFloatMulti[U]: ...


class mvInputInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    step: Property[int, int, false]
    step_fast: Property[int, int, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, min_value: int = 0, max_value: int = 100, step: int = 1, step_fast: int = 100, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, min_value: int = 0, max_value: int = 100, step: int = 1, step_fast: int = 100, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, min_value: int = 0, max_value: int = 100, step: int = 1, step_fast: int = 100, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "min_value", "max_value", "step", "step_fast", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_int[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, min_value: int = 0, max_value: int = 100, step: int = 1, step_fast: int = 100, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputInt[U]: ...


class mvInputIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    size: Property[int, int, false]
    min_clamped: Property[bool, bool, false]
    max_clamped: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), min_value: int = 0, max_value: int = 100, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), min_value: int = 0, max_value: int = 100, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, min_value: int = 0, max_value: int = 100, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "min_value", "max_value", "size", "min_clamped", "max_clamped", "on_enter", "readonly"], Any]: ...

def add_input_intx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), min_value: int = 0, max_value: int = 100, size: int = 4, min_clamped: bool = False, max_clamped: bool = False, on_enter: bool = False, readonly: bool = False, **kwargs) -> mvInputIntMulti[U]: ...


class mvInputText[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    hint: Property[str, str, false]
    multiline: Property[bool, bool, false]
    no_spaces: Property[bool, bool, false]
    uppercase: Property[bool, bool, false]
    tab_input: Property[bool, bool, false]
    decimal: Property[bool, bool, false]
    hexadecimal: Property[bool, bool, false]
    readonly: Property[bool, bool, false]
    password: Property[bool, bool, false]
    scientific: Property[bool, bool, false]
    on_enter: Property[bool, bool, false]
    auto_select_all: Property[bool, bool, false]
    ctrl_enter_for_new_line: Property[bool, bool, false]
    no_horizontal_scroll: Property[bool, bool, false]
    always_overwrite: Property[bool, bool, false]
    no_undo_redo: Property[bool, bool, false]
    escape_clears_all: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', hint: str = '', multiline: bool = False, no_spaces: bool = False, uppercase: bool = False, tab_input: bool = False, decimal: bool = False, hexadecimal: bool = False, readonly: bool = False, password: bool = False, scientific: bool = False, on_enter: bool = False, auto_select_all: bool = False, ctrl_enter_for_new_line: bool = False, no_horizontal_scroll: bool = False, always_overwrite: bool = False, no_undo_redo: bool = False, escape_clears_all: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', hint: str = '', multiline: bool = False, no_spaces: bool = False, uppercase: bool = False, tab_input: bool = False, decimal: bool = False, hexadecimal: bool = False, readonly: bool = False, password: bool = False, scientific: bool = False, on_enter: bool = False, auto_select_all: bool = False, ctrl_enter_for_new_line: bool = False, no_horizontal_scroll: bool = False, always_overwrite: bool = False, no_undo_redo: bool = False, escape_clears_all: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, hint: str = '', multiline: bool = False, no_spaces: bool = False, uppercase: bool = False, tab_input: bool = False, decimal: bool = False, hexadecimal: bool = False, readonly: bool = False, password: bool = False, scientific: bool = False, on_enter: bool = False, auto_select_all: bool = False, ctrl_enter_for_new_line: bool = False, no_horizontal_scroll: bool = False, always_overwrite: bool = False, no_undo_redo: bool = False, escape_clears_all: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "hint", "multiline", "no_spaces", "uppercase", "tab_input", "decimal", "hexadecimal", "readonly", "password", "scientific", "on_enter", "auto_select_all", "ctrl_enter_for_new_line", "no_horizontal_scroll", "always_overwrite", "no_undo_redo", "escape_clears_all"], Any]: ...

def add_input_text[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', hint: str = '', multiline: bool = False, no_spaces: bool = False, uppercase: bool = False, tab_input: bool = False, decimal: bool = False, hexadecimal: bool = False, readonly: bool = False, password: bool = False, scientific: bool = False, on_enter: bool = False, auto_select_all: bool = False, ctrl_enter_for_new_line: bool = False, no_horizontal_scroll: bool = False, always_overwrite: bool = False, no_undo_redo: bool = False, escape_clears_all: bool = False, **kwargs) -> mvInputText[U]: ...


class mvKnobFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, min_value: float = 0.0, max_value: float = 100.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, min_value: float = 0.0, max_value: float = 100.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, min_value: float = 0.0, max_value: float = 100.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "min_value", "max_value"], Any]: ...

def add_knob_float[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, min_value: float = 0.0, max_value: float = 100.0, **kwargs) -> mvKnobFloat[U]: ...


class mvListbox[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    num_items: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', num_items: int = 3, **kwargs) -> Item: ...
    @classmethod
    def create(cls, items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', num_items: int = 3, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, num_items: int = 3) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "num_items"], Any]: ...

def add_listbox[U: Any](items: Sequence[str] = (), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', num_items: int = 3, **kwargs) -> mvListbox[U]: ...


class mvLoadingIndicator[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    style: Property[int, int, false]
    circle_count: Property[int, int, false]
    speed: Property[float, float, false]
    radius: Property[float, float, false]
    thickness: Property[float, float, false]
    color: Property[Sequence[int], Sequence[int], false]
    secondary_color: Property[Sequence[int], Sequence[int], false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), style: int = 0, circle_count: int = 8, speed: float = 1.0, radius: float = 3.0, thickness: float = 1.0, color: Sequence[int] = (51, 51, 55, 255), secondary_color: Sequence[int] = (29, 151, 236, 103), **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), style: int = 0, circle_count: int = 8, speed: float = 1.0, radius: float = 3.0, thickness: float = 1.0, color: Sequence[int] = (51, 51, 55, 255), secondary_color: Sequence[int] = (29, 151, 236, 103), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), style: int = 0, circle_count: int = 8, speed: float = 1.0, radius: float = 3.0, thickness: float = 1.0, color: Sequence[int] = (51, 51, 55, 255), secondary_color: Sequence[int] = (29, 151, 236, 103)) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "payload_type", "drop_callback", "show", "style", "circle_count", "speed", "radius", "thickness", "color", "secondary_color"], Any]: ...

def add_loading_indicator[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), style: int = 0, circle_count: int = 8, speed: float = 1.0, radius: float = 3.0, thickness: float = 1.0, color: Sequence[int] = (51, 51, 55, 255), secondary_color: Sequence[int] = (29, 151, 236, 103), **kwargs) -> mvLoadingIndicator[U]: ...


class mvMenu[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset"], Any]: ...

def menu[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> mvMenu[U]: ...
def add_menu[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, **kwargs) -> mvMenu[U]: ...


class mvMenuBar[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool, P, Any]):
    __slots__ = ()
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "show"], Any]: ...

def menu_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvMenuBar[U]: ...
def add_menu_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvMenuBar[U]: ...


class mvMenuItem[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    shortcut: Property[str, str, false]
    check: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, shortcut: str = '', check: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, shortcut: str = '', check: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, shortcut: str = '', check: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "shortcut", "check"], Any]: ...

def add_menu_item[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, shortcut: str = '', check: bool = False, **kwargs) -> mvMenuItem[U]: ...


class mvProgressBar[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    overlay: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, overlay: str = '', default_value: float = 0.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, overlay: str = '', default_value: float = 0.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, overlay: str = '') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "overlay"], Any]: ...

def add_progress_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, overlay: str = '', default_value: float = 0.0, **kwargs) -> mvProgressBar[U]: ...


class mvRadioButton[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    horizontal: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', horizontal: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, items: Sequence[str] = (), *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', horizontal: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "horizontal"], Any]: ...

def add_radio_button[U: Any](items: Sequence[str] = (), *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: str = '', horizontal: bool = False, **kwargs) -> mvRadioButton[U]: ...


class mvRawTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
    format: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, format: int = 0, parent: Item = 12, **kwargs) -> Item: ...
    @classmethod
    def create(cls, width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, format: int = 0, parent: Item = 12, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, format: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "format"], Any]: ...

def add_raw_texture[U: Any](width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, format: int = 0, parent: Item = 12, **kwargs) -> mvRawTexture[U]: ...


class mvSelectable[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    span_columns: Property[bool, bool, false]
    disable_popup_close: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, span_columns: bool = False, disable_popup_close: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, span_columns: bool = False, disable_popup_close: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, span_columns: bool = False, disable_popup_close: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "span_columns", "disable_popup_close"], Any]: ...

def add_selectable[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: bool = False, span_columns: bool = False, disable_popup_close: bool = False, **kwargs) -> mvSelectable[U]: ...


class mvSeparator[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, show: bool = True, pos: Sequence[int] = ()) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "show"], Any]: ...

def add_separator[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> mvSeparator[U]: ...


class mvSeriesValue[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (), parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (), parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_series_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: Any = (), parent: Item = 13, **kwargs) -> mvSeriesValue[U]: ...


class mvSimplePlot[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    overlay: Property[str, str, false]
    histogram: Property[bool, bool, false]
    autosize: Property[bool, bool, false]
    min_scale: Property[float, float, false]
    max_scale: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (), overlay: str = '', histogram: bool = False, autosize: bool = True, min_scale: float = 0.0, max_scale: float = 0.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (), overlay: str = '', histogram: bool = False, autosize: bool = True, min_scale: float = 0.0, max_scale: float = 0.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, overlay: str = '', histogram: bool = False, autosize: bool = True, min_scale: float = 0.0, max_scale: float = 0.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "overlay", "histogram", "autosize", "min_scale", "max_scale"], Any]: ...

def add_simple_plot[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (), overlay: str = '', histogram: bool = False, autosize: bool = True, min_scale: float = 0.0, max_scale: float = 0.0, **kwargs) -> mvSimplePlot[U]: ...


class mvSlider3D[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    max_x: Property[float, float, false]
    max_y: Property[float, float, false]
    max_z: Property[float, float, false]
    min_x: Property[float, float, false]
    min_y: Property[float, float, false]
    min_z: Property[float, float, false]
    scale: Property[float, float, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), max_x: float = 100.0, max_y: float = 100.0, max_z: float = 100.0, min_x: float = 0.0, min_y: float = 0.0, min_z: float = 0.0, scale: float = 1.0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), max_x: float = 100.0, max_y: float = 100.0, max_z: float = 100.0, min_x: float = 0.0, min_y: float = 0.0, min_z: float = 0.0, scale: float = 1.0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, max_x: float = 100.0, max_y: float = 100.0, max_z: float = 100.0, min_x: float = 0.0, min_y: float = 0.0, min_z: float = 0.0, scale: float = 1.0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "max_x", "max_y", "max_z", "min_x", "min_y", "min_z", "scale"], Any]: ...

def add_3d_slider[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), max_x: float = 100.0, max_y: float = 100.0, max_z: float = 100.0, min_x: float = 0.0, min_y: float = 0.0, min_z: float = 0.0, scale: float = 1.0, **kwargs) -> mvSlider3D[U]: ...


class mvSliderDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    vertical: Property[bool, bool, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "vertical", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_double[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> mvSliderDouble[U]: ...


class mvSliderDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_doublex[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Any = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> mvSliderDoubleMulti[U]: ...


class mvSliderFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    vertical: Property[bool, bool, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "vertical", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_float[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: float = 0.0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> mvSliderFloat[U]: ...


class mvSliderFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[float, float, false]
    max_value: Property[float, float, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_floatx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[float] = (0.0, 0.0, 0.0, 0.0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: float = 0.0, max_value: float = 100.0, format: str = '%.3f', **kwargs) -> mvSliderFloatMulti[U]: ...


class mvSliderInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    vertical: Property[bool, bool, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "vertical", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_int[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: int = 0, vertical: bool = False, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> mvSliderInt[U]: ...


class mvSliderIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    enabled: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    size: Property[int, int, false]
    no_input: Property[bool, bool, false]
    clamped: Property[bool, bool, false]
    min_value: Property[int, int, false]
    max_value: Property[int, int, false]
    format: Property[str, str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, size: int = 4, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d') -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "indent", "source", "payload_type", "callback", "drag_callback", "drop_callback", "show", "enabled", "filter_key", "tracked", "track_offset", "size", "no_input", "clamped", "min_value", "max_value", "format"], Any]: ...

def add_slider_intx[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, enabled: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: Sequence[int] = (0, 0, 0, 0), size: int = 4, no_input: bool = False, clamped: bool = False, min_value: int = 0, max_value: int = 100, format: str = '%d', **kwargs) -> mvSliderIntMulti[U]: ...


class mvSpacer[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, show: bool = True, pos: Sequence[int] = ()) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "show"], Any]: ...

def add_spacer[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, show: bool = True, pos: Sequence[int] = (), **kwargs) -> mvSpacer[U]: ...


class mvStaticTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
    @staticmethod
    def __itemtype_command__(width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> Item: ...
    @classmethod
    def create(cls, width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label"], Any]: ...

def add_static_texture[U: Any](width: int, height: int, default_value: Sequence[float], *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 12, **kwargs) -> mvStaticTexture[U]: ...


class mvStringValue[U = Any](ChildItem[U, str, mvValueRegistry]):
    __slots__ = ()
    source: Property[int | str, int | str, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: str = '', parent: Item = 13, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: str = '', parent: Item = 13, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, source: int | str = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "source"], Any]: ...

def add_string_value[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, source: int | str = 0, default_value: str = '', parent: Item = 13, **kwargs) -> mvStringValue[U]: ...


class mvSubPlots[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    width: Property[int, int, false]
    height: Property[int, int, false]
    indent: Property[int, int, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    row_ratios: Property[Sequence[float], Sequence[float], false]
    column_ratios: Property[Sequence[float], Sequence[float], false]
    no_title: Property[bool, bool, false]
    no_menus: Property[bool, bool, false]
    no_resize: Property[bool, bool, false]
    no_align: Property[bool, bool, false]
    share_series: Property[bool, bool, false]
    link_rows: Property[bool, bool, false]
    link_columns: Property[bool, bool, false]
    link_all_x: Property[bool, bool, false]
    link_all_y: Property[bool, bool, false]
    column_major: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(rows: int, columns: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, row_ratios: Sequence[float] = (), column_ratios: Sequence[float] = (), no_title: bool = False, no_menus: bool = False, no_resize: bool = False, no_align: bool = False, share_series: bool = False, link_rows: bool = False, link_columns: bool = False, link_all_x: bool = False, link_all_y: bool = False, column_major: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, rows: int, columns: int, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, row_ratios: Sequence[float] = (), column_ratios: Sequence[float] = (), no_title: bool = False, no_menus: bool = False, no_resize: bool = False, no_align: bool = False, share_series: bool = False, link_rows: bool = False, link_columns: bool = False, link_all_x: bool = False, link_all_y: bool = False, column_major: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, row_ratios: Sequence[float] = (), column_ratios: Sequence[float] = (), no_title: bool = False, no_menus: bool = False, no_resize: bool = False, no_align: bool = False, share_series: bool = False, link_rows: bool = False, link_columns: bool = False, link_all_x: bool = False, link_all_y: bool = False, column_major: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "width", "height", "indent", "callback", "show", "filter_key", "tracked", "track_offset", "row_ratios", "column_ratios", "no_title", "no_menus", "no_resize", "no_align", "share_series", "link_rows", "link_columns", "link_all_x", "link_all_y", "column_major"], Any]: ...

def subplots[U: Any](rows: int, columns: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, row_ratios: Sequence[float] = (), column_ratios: Sequence[float] = (), no_title: bool = False, no_menus: bool = False, no_resize: bool = False, no_align: bool = False, share_series: bool = False, link_rows: bool = False, link_columns: bool = False, link_all_x: bool = False, link_all_y: bool = False, column_major: bool = False, **kwargs) -> mvSubPlots[U]: ...
def add_subplots[U: Any](rows: int, columns: int, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, width: int = 0, height: int = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, row_ratios: Sequence[float] = (), column_ratios: Sequence[float] = (), no_title: bool = False, no_menus: bool = False, no_resize: bool = False, no_align: bool = False, share_series: bool = False, link_rows: bool = False, link_columns: bool = False, link_all_x: bool = False, link_all_y: bool = False, column_major: bool = False, **kwargs) -> mvSubPlots[U]: ...


class mvTabBar[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, int, P, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    reorderable: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, reorderable: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, reorderable: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, reorderable: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "callback", "show", "filter_key", "tracked", "track_offset", "reorderable"], Any]: ...

def tab_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, reorderable: bool = False, **kwargs) -> mvTabBar[U]: ...
def add_tab_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, reorderable: bool = False, **kwargs) -> mvTabBar[U]: ...


class mvTab[U = Any](ChildContainerItem[U, bool, mvTabBar, Any]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    closable: Property[bool, bool, false]
    no_tooltip: Property[bool, bool, false]
    order_mode: Property[int, int, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, no_tooltip: bool = False, order_mode: int = 0, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, no_tooltip: bool = False, order_mode: int = 0, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, closable: bool = False, no_tooltip: bool = False, order_mode: int = 0) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "drop_callback", "show", "filter_key", "tracked", "track_offset", "closable", "no_tooltip", "order_mode"], Any]: ...

def tab[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, no_tooltip: bool = False, order_mode: int = 0, **kwargs) -> mvTab[U]: ...
def add_tab[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, closable: bool = False, no_tooltip: bool = False, order_mode: int = 0, **kwargs) -> mvTab[U]: ...


class mvTabButton[U = Any](ChildItem[U, None, mvTabBar]):
    __slots__ = ()
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    callback: Property[ItemCallback | None, ItemCallback | None, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    no_reorder: Property[bool, bool, false]
    leading: Property[bool, bool, false]
    trailing: Property[bool, bool, false]
    no_tooltip: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_reorder: bool = False, leading: bool = False, trailing: bool = False, no_tooltip: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_reorder: bool = False, leading: bool = False, trailing: bool = False, no_tooltip: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_reorder: bool = False, leading: bool = False, trailing: bool = False, no_tooltip: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "no_reorder", "leading", "trailing", "no_tooltip"], Any]: ...

def add_tab_button[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, no_reorder: bool = False, leading: bool = False, trailing: bool = False, no_tooltip: bool = False, **kwargs) -> mvTabButton[U]: ...


class mvText[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    source: Property[int | str, int | str, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    wrap: Property[int, int, false]
    bullet: Property[bool, bool, false]
    color: Property[Sequence[int], Sequence[int], false]
    show_label: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(default_value: str = '', *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, wrap: int = -1, bullet: bool = False, color: Sequence[int] = (-255, 0, 0, 255), show_label: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, default_value: str = '', *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, wrap: int = -1, bullet: bool = False, color: Sequence[int] = (-255, 0, 0, 255), show_label: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, wrap: int = -1, bullet: bool = False, color: Sequence[int] = (-255, 0, 0, 255), show_label: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "source", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "wrap", "bullet", "color", "show_label"], Any]: ...

def add_text[U: Any](default_value: str = '', *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, source: int | str = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, wrap: int = -1, bullet: bool = False, color: Sequence[int] = (-255, 0, 0, 255), show_label: bool = False, **kwargs) -> mvText[U]: ...


class mvTimePicker[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsCallback[CB], ChildItem[U, None, P]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    hour24: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'hour': 14, 'min': 32, 'sec': 23}, hour24: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'hour': 14, 'min': 32, 'sec': 23}, hour24: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, hour24: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "callback", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "hour24"], Any]: ...

def add_time_picker[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', callback: ItemCallback | None = None, drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, default_value: dict = {'hour': 14, 'min': 32, 'sec': 23}, hour24: bool = False, **kwargs) -> mvTimePicker[U]: ...


class mvTooltip[U = Any, P: AppItem[Any, Any, Any] = Any](ChildContainerItem[U, None, P, Any]):  # type: ignore
    __slots__ = ()
    show: Property[bool, bool, false]
    delay: Property[float, float, false]
    hide_on_activity: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(parent: Item, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, delay: float = 0.0, hide_on_activity: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, parent: Item, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, delay: float = 0.0, hide_on_activity: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, show: bool = True, delay: float = 0.0, hide_on_activity: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "show", "delay", "hide_on_activity"], Any]: ...

def tooltip[U: Any](parent: Item, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, delay: float = 0.0, hide_on_activity: bool = False, **kwargs) -> mvTooltip[U]: ...
def add_tooltip[U: Any](parent: Item, *, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, show: bool = True, delay: float = 0.0, hide_on_activity: bool = False, **kwargs) -> mvTooltip[U]: ...


class mvTreeNode[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool, P, Any]):
    __slots__ = ()
    pos: Property[list[int], Sequence[int], Literal[True]]
    indent: Property[int, int, false]
    payload_type: Property[str, str, false]
    drag_callback: Property[ItemCallback | None, ItemCallback | None, false]
    drop_callback: Property[ItemCallback | None, ItemCallback | None, false]
    show: Property[bool, bool, false]
    filter_key: Property[str, str, false]
    tracked: Property[bool, bool, false]
    track_offset: Property[float, float, false]
    open_on_double_click: Property[bool, bool, false]
    open_on_arrow: Property[bool, bool, false]
    leaf: Property[bool, bool, false]
    bullet: Property[bool, bool, false]
    selectable: Property[bool, bool, false]
    span_text_width: Property[bool, bool, false]
    span_full_width: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, selectable: bool = False, span_text_width: bool = False, span_full_width: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, selectable: bool = False, span_text_width: bool = False, span_full_width: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, selectable: bool = False, span_text_width: bool = False, span_full_width: bool = False) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "payload_type", "drag_callback", "drop_callback", "show", "filter_key", "tracked", "track_offset", "open_on_double_click", "open_on_arrow", "leaf", "bullet", "selectable", "span_text_width", "span_full_width"], Any]: ...

def tree_node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, selectable: bool = False, span_text_width: bool = False, span_full_width: bool = False, **kwargs) -> mvTreeNode[U]: ...
def add_tree_node[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, before: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drag_callback: ItemCallback | None = None, drop_callback: ItemCallback | None = None, show: bool = True, pos: Sequence[int] = (), filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, selectable: bool = False, span_text_width: bool = False, span_full_width: bool = False, **kwargs) -> mvTreeNode[U]: ...


class mvViewportMenuBar[U = Any, C: ChildItemT = Any](RootItem[U, C, None]):
    __slots__ = ()
    indent: Property[int, int, false]
    show: Property[bool, bool, false]
    @staticmethod
    def __itemtype_command__(*, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Item: ...
    @classmethod
    def create(cls, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> Self: ...
    def configure(self, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, indent: int = -1, show: bool = True) -> None: ...  # type: ignore[override]
    def configuration(self) -> dict[Literal["label", "user_data", "use_internal_label", "indent", "show"], Any]: ...

def viewport_menu_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvViewportMenuBar[U]: ...
def add_viewport_menu_bar[U: Any](*, label: str | None = None, user_data: U = None, use_internal_label: bool = True, tag: Item = 0, indent: int = -1, parent: Item = 0, show: bool = True, delay_search: bool = False, **kwargs) -> mvViewportMenuBar[U]: ...

