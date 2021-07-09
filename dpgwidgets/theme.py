from typing import Union, Sequence

from . import dpg, Item
from .dpgwrap.stylize import Theme as _Theme
from .constants import THEMECOLOR, THEMESTYLE


class Theme(_Theme):
    def __init__(
        self,
        parent: Union[int,Item] = None,
        is_disabled_theme: bool = False,
        **kwargs
    ):
        # self.__set_theme_cmd doesn't need to exist in this case
        if parent is None:
            super().__init__(default_theme=True,**kwargs)
            self.__set_theme_cmd = lambda *x, **y: None
            self.__parent = 0
        # there aren't "default disabled themes" (to my knowledge)
        elif is_disabled_theme:
            super().__init__(**kwargs)
            self.__set_theme_cmd = dpg.set_item_disabled_theme
            self.__parent = int(parent)
        else:
            super().__init__(**kwargs)
            self.__set_theme_cmd = dpg.set_item_theme
            self.__parent = int(parent)

        # {option: theme_item_id, ...}
        self.__color_ids = {attr: None for attr in THEMECOLOR}
        self.__style_ids = {attr: None for attr in THEMESTYLE}
        
        # helpers store the actual current value of theme items
        # because they can't be fetched after creation
        self.__color = ColorHelper(self, self.__color_ids, "apply_color")
        self.__style = StyleHelper(self, self.__style_ids, "apply_style")
            
    @property
    def color(self):
        return self.__color

    @property
    def style(self):
        return self.__style

    def apply_color(self, option: str, rgba: Sequence = (0,0,0,255)):
        target, category = THEMECOLOR[option]
        old_theme_item = self.__color_ids.pop(option)
        new_theme_item = dpg.add_theme_color(
            target, 
            rgba, 
            category=category,
            parent=self.id
        )
        # need to update helper first because its __setattr__
        # will bork the process if <option> is in _color_ids
        setattr(self.__style, option, rgba)
        # applying new item/color
        self.__color_ids[option] = new_theme_item
        self.__set_theme_cmd(self.__parent, self.id)
        # cleanup
        if old_theme_item:
            dpg.delete_item(old_theme_item)

    def apply_style(self, option: str, xy: Sequence = (1.0, -1.0)):
        x, y = xy
        target, category = THEMESTYLE[option]
        old_theme_item = self.__style_ids.pop(option)
        new_theme_item = dpg.add_theme_style(
            target,
            x,
            y,
            category=category,
            parent=self.id
        )
        # need to update helper first because its __setattr__
        # will bork the process if <option> is in _style_ids
        setattr(self.__style, option, (x, y))
        # applying new item/style
        self.__style_ids[option] = new_theme_item
        self.__set_theme_cmd(self.__parent, self.id)
        # cleanup
        if old_theme_item:
            dpg.delete_item(old_theme_item)

    def refresh(self):
        self.__color_ids = {attr: None for attr in THEMECOLOR}
        self.__style_ids = {attr: None for attr in THEMESTYLE}
        super().refresh()




class TItemBase:
    __item_ids = {}

    def __init__(self, parent: Theme, item_ids: dict, theme_type: str):
        self.__parent = parent
        self.__theme_type = theme_type

        if "_color" in theme_type:
            self.__value_setter = self.__set_color_value
        elif "_style" in theme_type:
            self.__value_setter = self.__set_style_value

        self.__item_ids = item_ids

    def __setattr__(self, attr, value):
        if attr in self.__item_ids:
            self.__value_setter(attr, value)
    
        super().__setattr__(attr, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        setattr(self, item, value)

    def __set_color_value(self, attr, value):
        self.__parent.apply_color(attr, value)

    def __set_style_value(self, attr, value):
        if isinstance(value, (int, float)):
            value = value, -1.0
        self.__parent.apply_style(attr, value)


class ColorHelper(TItemBase):
    border = None
    border_shadow = None
    button = None
    button_active = None
    button_hovered = None
    check_mark = None
    child_bg = None
    docking_empty_bg = None
    docking_preview = None
    drag_drop_target = None
    frame_bg = None
    frame_bg_active = None
    frame_bg_hovered = None
    header = None
    header_active = None
    header_hovered = None
    menu_bar_bg = None
    modal_window_dim_bg = None
    nav_highlight = None
    nav_windowing_dim_bg = None
    nav_windowing_highlight = None
    plot_histogram = None
    plot_histogram_hovered = None
    plot_lines = None
    plot_lines_hovered = None
    popup_bg = None
    resize_grip = None
    resize_grip_active = None
    resize_grip_hovered = None
    scrollbar_bg = None
    scrollbar_grab = None
    scrollbar_grab_active = None
    scrollbar_grab_hovered = None
    separator = None
    separator_active = None
    separator_hovered = None
    slider_grab = None
    slider_grab_active = None
    tab = None
    tab_active = None
    tab_hovered = None
    tab_unfocused = None
    tab_unfocused_active = None
    table_border_light = None
    table_border_strong = None
    table_header_bg = None
    table_row_bg = None
    table_row_bg_alt = None
    text = None
    text_disabled = None
    text_selected_bg = None
    title_bg = None
    title_bg_active = None
    title_bg_collapsed = None
    window_bg = None
    plot_crosshairs = None
    plot_error_bar = None
    plot_fill = None
    plot_frame_bg = None
    plot_inlay_text = None
    plot_legend_bg = None
    plot_legend_border = None
    plot_legend_text = None
    plot_line = None
    plot_marker_fill = None
    plot_marker_outline = None
    plot_bg = None
    plot_border = None
    plot_query = None
    plot_selection = None
    plot_title_text = None
    plot_x_axis = None
    plot_x_axis_grid = None
    plot_y_axis = None
    plot_y_axis2 = None
    plot_y_axis3 = None
    plot_y_axis_grid = None
    plot_y_axis_grid2 = None
    plot_y_axis_grid3 = None
    node_box_selector = None
    node_box_selector_outline = None
    node_grid_background = None
    node_grid_line = None
    node_link = None
    node_link_hovered = None
    node_link_selected = None
    node_background = None
    node_background_hovered = None
    node_background_selected = None
    node_outline = None
    node_pin = None
    node_pin_hovered = None
    node_title_bar = None
    node_title_bar_hovered = None
    node_title_bar_selected = None


class StyleHelper(TItemBase):
    # Notes: 
    #     "*text_align": centered is 0.5, 0.5
    alpha = None
    button_text_align = None
    cell_padding = None
    child_border_size = None
    child_rounding = None
    frame_border_size = None
    frame_padding = None
    frame_rounding = None
    grab_min_size = None
    grab_rounding = None
    indent_spacing = None
    item_inner_spacing = None
    item_spacing = None
    popup_border_size = None
    popup_rounding = None
    scrollbar_rounding = None
    scrollbar_size = None
    selectable_text_align = None
    tab_rounding = None
    window_border_size = None
    window_min_size = None
    window_padding = None
    window_rounding = None
    window_title_align = None
    plot_annotation_padding = None
    plot_digital_bit_gap = None
    plot_digital_bit_height = None
    plot_error_bar_size = None
    plot_error_bar_weight = None
    plot_fill_alpha = None
    plot_fit_padding = None
    plot_label_padding = None
    plot_legend_inner_padding = None
    plot_legend_padding = None
    plot_legend_spacing = None
    plot_line_weight = None
    plot_major_grid_size = None
    plot_major_tick_len = None
    plot_major_tick_size = None
    plot_marker = None
    plot_marker_size = None
    plot_marker_weight = None
    plot_minor_alpha = None
    plot_minor_grid_size = None
    plot_minor_tick_len = None
    plot_minor_tick_size = None
    plot_mouse_pos_padding = None
    plot_border_size = None
    plot_default_size = None
    plot_min_size = None
    plot_padding = None
    node_grid_spacing = None
    node_link_hover_distance = None
    node_link_line_segments_per_length = None
    node_link_thickness = None
    node_border_thickness = None
    node_corner_rounding = None
    node_padding_horizontal = None
    node_padding_vertical = None
    node_pin_circle_radius = None
    node_pin_hover_radius = None
    node_pin_line_thickness = None
    node_pin_offset = None
    node_pin_quad_side_length = None
    node_pin_triangle_side_length = None
