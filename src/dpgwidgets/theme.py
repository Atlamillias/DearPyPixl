from __future__ import annotations
from typing import Sequence
from pathlib import Path

from dpgwidgets import dpg, _Registry
from dpgwidgets.constants import COLOR_OPTN, STYLE_OPTN


# NOTE: DearPyGui seperates "Theme" and "Font". The process
# of marrying the two (below) is not straight-forward and have
# different implementations. Where the Theme class (below) has
# helper classes for color and styles (which are basically
# dictionaries) the Font class (even further below) manages itself
# and is not made nor does it work in the same way. The
# ThemeSupport mixin class serves as the middle-man for making the
# API more streamlined for the end-user.
#
# TL/DR: Managing this in the future might *suck* depending how DPG
# manages fonts/themes going forward.

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
    """Mixin class for Item subclasses supporting functionality 
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
    def theme_color(self):
        return self.theme.color

    @property
    def theme_style(self):
        return self.theme.style

    # NOTE: See the Font class for comments regarding how this works.
    @property
    def theme_font(self):
        return self.theme.font

    @theme_font.setter
    def theme_font(self, value: Font):
        # All that is needed to be done by the end-user is
        # instantiate an instance (binding it to a variable), and setting
        # an item's theme_font to that variable (item.theme_font = Font(...)).
        # See the Font class comments for more context.
        if isinstance(self.id, int):
            self.theme.font = value
            dpg.set_item_font(self.id, self.theme._font_id)
        # If unsetting the default font (i.e. value is None), *when* self.theme.font
        # is set matters since the original references are needed to configure it.
        elif value is not None:
            self.theme.font = value
            dpg.configure_item(self.theme._font_id, default_font=True)
        elif value is None and self.theme.font is None:
            return
        else:
            dpg.configure_item(self.theme._font_id, default_font=False)
            self.theme.font = value

    @property
    def theme_ft_size(self):
        return self.theme.font_size

    @theme_ft_size.setter
    def theme_ft_size(self, value: float):
        # The current DPG API disallows getting/setting
        # the font size from an existing font item.
        # Since fonts are rendered as bitmaps, they wouldn't
        # scale well even if they could be directly resized.
        self.theme.font_size = value
        if value is None:
            raise ValueError(f"value must be <float>.")

        if isinstance(self.id, int):
            dpg.set_item_font(self.id, self.theme._font_id)
        else:
            dpg.configure_item(self.theme._font_id, default_font=True)



class Theme:
    # Note: DPG seperates font and "theme" (color and style).
    # The idea here is to unify them.
    _color_ids = None
    _style_ids = None
    _font_id = None  # id of the font item that matches the set size
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

    # NOTE: See the Font class for comments regarding how this works.
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value: Font):
        self.__font = value
        if value is None:
            self._font_id = 0
        else:
            self.__font_size = self.__font_size or value.default_size
            self._font_id = value(self.__font_size)

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, value: float):
        self.__font_size = value
        if value is None:
            self._font_id = None
        elif font_obj := self.__font:
            # Calling the set Font instance returns a font item
            # with the matching size.
            # See the Font class for more context.
            self._font_id = font_obj(self.__font_size)

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
        self.__font = None
        self.__font_size = None
        self._font_id = None
  

    def _clean(self):
        dpg.delete_item(self.__id, children_only=True)




########## Theme helpers ##########
class THelper:
    # NOTE: There's definitely a better way of handling this.
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
        # name collisions because there are SO MANY OPTIONS.
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
    alpha = None
    button_text_align = None  # centered is 0.5, 0.5
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
    selectable_text_align = None  # centered is 0.5, 0.5
    tab_rounding = None
    window_border_size = None
    window_min_size = None
    window_padding = None
    window_rounding = None
    window_title_align = None  # centered is 0.5, 0.5
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
    """Returns a callable Font object and adds the font to the 
    global font registry.
    """
    # NOTE: When DPG creates a font, they are rendered as bitmaps.
    # This means they don't scale very well when resized. At this
    # time, an existing font item cannot have its size fetched or
    # changed through the DPG API. This class solves both of these
    # problems. 
    registered_fonts = []

    def __init__(
        self,
        label: str,
        file: str,
        size: float = 13.0,

        font_range: tuple[int, int] = None,
        font_range_hint: int = None,
        addl_chars: Sequence = None,

        **kwargs
    ):
        # When instantiated, a font item is created, the size id are 
        # added to self._fonts as {size: font_id} via _get_font_item,
        # and the instance is appended to Font.registered_fonts.

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

        self.__class__.registered_fonts.append(self)
        self._get_font_item()

    def __str__(self):
        return self.__label

    def __repr__(self):
        return (f"{self.__class__.__name__}" +
               f"(label={self.__label}, " +
               f"file={self.__file}, " +
               f"default_size={self.__default_size})")

    def __call__(self, size: float = None) -> int:
        return self._get_font_item(size)

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

    def _get_font_item(self, size: float = None):
        size = size or self.__default_size
        # Creating font items internally stalls the running thread
        # (this is quite severe when creating many font items).
        # To avoid re-creating the same item for different widgets,
        # any font id created is cached in self._fonts as {size: id}.
        # The cache is checked first for an item with the requested
        # size and returns it if it exists.
        if font := self._fonts.get(size, None):
            return int(font)
        
        # If a font with that size doesn't exist, then we create one
        # and add it to the cache using the parameters passed when 
        # the Font instance was created.
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

    @classmethod
    def fonts(cls):
        """Returns a list of registered fonts."""
        return cls.registered_fonts

    @classmethod
    def load_fonts(cls, dir_path: str):
        """Attempts to load and register all .otf and .ttf files
        in <dir_path>, and return a list of all font objects created.

        Note: You will notice a sizable lag when loading several at once.
        """
        # NOTE: This is something you would want to do early on,
        # before even calling a Viewport instance. Definitely one
        # of those "Loading, please wait..." moments.
        fonts = []
        for ffile in Path(dir_path).iterdir():
            if ffile.suffix in (".ttf", ".otf"):
                try:
                    fonts.append(cls(ffile.stem, str(ffile)))
                except Exception as e:
                    pass

        return fonts

