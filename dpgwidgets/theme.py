from __future__ import annotations
from typing import Sequence

from dpgwidgets import dpg, _Registry
from dpgwidgets.constants import COLOR_OPTN, STYLE_OPTN


_FONT_RANGE_HINT = {}


def _get_font_range_hints():
    range_hints = (attr for attr in dir(
        dpg) if attr.startswith("mvFontRangeHint_"))
    for var in range_hints:
        key = var.replace("mvFontRangeHint_", "").lower()
        _FONT_RANGE_HINT[key] = var


_get_font_range_hints()



##############################
###  Theme support mixins ####
##############################
class ThemeSupport:
    """Mixin class for the Item subclasses supporting functionality 
    for the modification of colors, styles, and fonts.
    """
    def __init__(self):
        super().__init__()
        self.theme = Theme()
        
    # active theme
    @property
    def theme(self):
        return self.__theme

    @theme.setter
    def theme(self, value: Theme):
        self.__theme = value
 
        if isinstance(self.id, int):  # <class "Item">
            dpg.set_item_theme(self.id, int(value))
            if value.font:
                dpg.set_item_font(self.id, value._font_id)
        elif isinstance(self.id, str):  # <class "Viewport">
            dpg.configure_item(int(value), default_theme=True)
            if value.font:
                dpg.configure_item(value._font_id, default_font=True)
        else:
            raise Exception(f"{repr(super().__class__)} does not support this mixin.")

    @property
    def tcolor(self):
        return self.theme.color

    @property
    def tstyle(self):
        return self.theme.style

    @property
    def tfont(self):
        return self.theme.font

    @tfont.setter
    def tfont(self, value: Font):
        self.theme.font = value

        if self.id:
            dpg.set_item_font(self.id, self.theme._font_id)
        else:
            dpg.configure_item(self.theme._font_id, default_font=True)

    @property
    def tfont_size(self):
        return self.theme.font_size

    @tfont_size.setter
    def tfont_size(self, value: float):
        self.theme.font_size = value

        if self.id:
            dpg.set_item_font(self.id, self.theme._font_id)
        else:
            dpg.configure_item(self.theme._font_id, default_font=True)



class Theme:
    # Note: DPG seperates font and "theme" (color and style).
    # The idea here is to unify them.
    _color_ids = None
    _style_ids = None
    _font_id = None
    __id = None

    __color = None
    __style = None
    __font = None
    __font_size = None



    def __init__(self, label: str = None, **kwargs):
        self.__kwargs = kwargs
        self.__label = label

        self._setup()

    def __int__(self):
        return int(self.__id)

    def __str__(self):
        return str(self.label)

    # DPG theme stuff
    @property
    def id(self):
        return self.__id

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value: str):
        self.__label = value
        dpg.configure_item(self.__id, label=value)

    # Theme attributes
    @property
    def color(self):
        return self.__color

    @property
    def style(self):
        return self.__style

    # Font doesn't have a helper class
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value: Font):
        self.__font = value
        self.__font_size = self.__font_size or value.default_size
        self._font_id = value(self.__font_size)

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, value: float):
        self.__font_size = value
        if font := self.__font:
            self._font_id = font(self.__font_size)

    def configure(
        self, 
        style: dict = None, 
        color: dict = None, 
        font: dict = None
    ):
        # **{category: {option: value}, ...}
        if color:
            [self.__color.set(optn, rgba) for optn, rgba in color.items()]
        if style:
            [self.__style.set(optn, xy) for optn, xy in style.items()]
        if font:  # font = {font: value, font_size: value}
            if font_obj := font.get("font", None):
                self.font = font_obj
            if ft_size := font.get("font_size", None):
                self.font_size = ft_size

        return self

    def refresh(self):
        self._setup()
        dpg.delete_item(self.__id, children_only=True)
    
    def _setup(self):
        # {option: theme_item_id, ...}
        self._color_ids = {attr: None for attr in COLOR_OPTN}
        self._style_ids = {attr: None for attr in STYLE_OPTN}

        if not self.__id:
            with dpg.theme(label=self.__label, **self.__kwargs) as self.__id:
                pass

        # theme "parts"
        # helpers store the actual current value of theme items
        # because the values can't be fetched after creation
        self.__color = ColorHelper(self, "color")
        self.__style = StyleHelper(self, "style")
        self.__font = _DEFAULT_FONT
        self.__font_size = _DEFAULT_FONT.default_size
        self._font_id = _DEFAULT_FONT()
  

    def _clean(self):
        dpg.delete_item(self.__id, children_only=True)




########## Theme helpers ##########
class THelper:
    # Note: There's definitely a better way of handling this.
    # The way this is currently set allows me to make subclasses
    # containing only the theme options and nothing else. All
    # functionality is below and doesn't need patching per subclass.
    # Downside is that its more error-prone and is kinda hell
    # to extend via subclasses.
    __theme_ids = {}

    def __init__(self, parent: Theme, theme_type: str):
        self.__id = int(parent)
        # The goal is to allow intellisense to help out with
        # the available colors/styles. These are mangled to avoid
        # name collisions and to keep intellisense from picking
        # at internal attributes.
        if "color" == theme_type:
            self.__optn_constants = COLOR_OPTN
            self.__theme_ids = parent._color_ids
            self.__setter = self.__set_color
            self.__dpg_cmd = dpg.add_theme_color
        elif "style" == theme_type:
            self.__optn_constants = STYLE_OPTN
            self.__theme_ids = parent._style_ids
            self.__setter = self.__set_style
            self.__dpg_cmd = dpg.add_theme_style

    def __setattr__(self, attr, value):
        if attr in self.__theme_ids:
            self.set(attr, value)

        super().__setattr__(attr, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        setattr(self, item, value)

    def set(self, option, value):
        old_item, new_item = self.__setter(option, value)
        # updating appropriate dicts
        self.__theme_ids[option] = new_item
        # cleanup
        if old_item:
            dpg.delete_item(old_item)

    def __set_color(self, option, value):
        target, category = self.__optn_constants[option]
        old_item = self.__theme_ids.pop(option)
        if value is None:
            # back to using the default theme
            # or inheriting a parent theme
            new_item = None
        else:
            new_item = self.__dpg_cmd(
                target,
                value,
                category=category,
                parent=int(self.__id)
            )
        return old_item, new_item

    def __set_style(self, option, xy):
        if xy is not None:
            if isinstance(xy, (int, float)):
                x, y = xy, -1.0
            else:
                x, y = xy
            target, category = self.__optn_constants[option]
            old_item = self.__theme_ids.pop(option)
            new_item = dpg.add_theme_style(
                target,
                x,
                y,
                category=category,
                parent=int(self.__id)
            )
        else:
            # back to using the default theme
            # or inheriting a parent theme
            old_item = self.__theme_ids.pop(option)
            new_item = None

        return old_item, new_item

class ColorHelper(THelper):
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

class StyleHelper(THelper):
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




##############################
######### Font stuff #########
##############################
class Font:
    """
    Returns a callable Font object.
    """
    _registered_fonts = []

    def __init__(
        self,
        label: str,
        file: str,
        size: float = 12.0,

        font_range: tuple[int, int] = None,
        font_range_hint: int = None,
        addl_chars: Sequence = None,

        **kwargs
    ):
        self.__default_size = size
        # future font item args
        self.__label = label
        self.__file = file
        self.__kwargs = kwargs
        # extras
        self.__font_range = font_range
        self.__font_range_hint = font_range_hint
        self.__addl_chars = addl_chars

        self._fonts = {}
        self.__class__._registered_fonts.append(self)

    def __str__(self):
        return self.__label

    def __repr__(self):
        return f"{self.__class__.__name__}(label={self.__label}, file={self.__file}, default_size={self.__default_size})"

    def __call__(self, size: float = None) -> int:
        # returns an existing font item of <size> or
        # creates a new one and caches it
        size = size or self.__default_size

        if font := self._fonts.get(size, None):
            return int(font)

        with dpg.font(self.__file, size, parent=_Registry.FONT.value, **self.__kwargs) as font:
            if self.__font_range:
                start, stop = self.__font_range
                dpg.add_font_range(start, stop)
            if hint := self.__font_range_hint:
                dpg.add_font_range_hint(hint)
            if self.__addl_chars:
                dpg.add_font_chars(self.__addl_chars)

        self._fonts[size] = font

        return font

    @property
    def label(self):
        return self.__label

    @property
    def default_size(self):
        return self.__default_size

    @default_size.setter
    def default_size(self, value: float):
        self(value)
        self.__default_size = value


_DEFAULT_FONT = Font("ProggyCleanSZ", "ProggyCleanSZ.ttf", 13.0)
