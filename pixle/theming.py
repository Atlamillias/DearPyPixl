
from __future__ import annotations
from collections.abc import Mapping
from typing import Callable, Union, Optional
from functools import singledispatchmethod
import enum
from dearpygui.dearpygui import (
    # theme
    add_theme,
    add_theme_color,
    add_theme_style,
    set_item_theme,
    set_item_disabled_theme,
    # font
    set_item_font,
    add_font,
    add_font_chars,
    add_font_range,
    add_font_range_hint,
    # misc
    delete_item,
    configure_item
)
from pixle.itemtypes import Item
from pixle.errors import FontSizeError


__all__ = [
    "Theme",
    "Font",
    "FontRangeHint",
]


# Type hints
Numeric: Union[int, float]
ColorValue: tuple[Numeric, Numeric, Numeric, Optional[Numeric]]
StyleValue: tuple[Numeric, Numeric]
ElementValue: Union[ColorValue, StyleValue, None]
FtRangeHint: Union[FontRangeHint, int, str]


# NOTE: The internal library seperates "theme"s and "font"s, while the
# end-user API for this library unifies the two into "theme". Outside of
# docstrings they will both be referenced as seperate entities.



###################################
############## Theme ##############
###################################
class Theme(Item, Mapping):
    """A theme that can be applied to items. The same theme can be applied
    to several items. Themes are dynamic -- any changes made to the theme
    will be reflected to all items using it. An item can be affected by a
    theme (prioritized, from top to bottom):
        * by directly applying the theme to an item
        * if the item is a child of a parent item with an applied theme
        * if an application default theme is set
        * by the system (internal) default theme


    Properties
    ----------
    * targets (read-only)
    * color (read-only)
    * style (read-only)
    * font
    * font_size


    Methods
    -------
    * configure
    * configuration
    * apply
    * apply_as_disabled
    * unapply
    * unapply_disabled
    * renew


    Returns:
        *Theme*
    """
    _command = add_theme
    __gl_font_id = 0
    __gl_theme_id = 0

    def __init__(self, label: str = None, **kwargs):
        super().__init__(
            label=label,
            **kwargs
        )
        self._color = Color(self)
        self._style = Style(self)
        self._font: Font = None

        self.__keys = {"color", "style", "font", "font_size"}
        self.__font_id = 0
        self.__font_size_value = 12.0
        self.__item_ids: set[int] = set()

        self.label = label

    def __getitem__(self, item):
        if item in self.__keys:
            return getattr(self, item)
        raise KeyError

    def __setitem__(self, item, value):
        if item in self.__keys:
            return setattr(self, item, value)
        raise KeyError

    def __len__(self):
        return len(self.__keys)

    def __iter__(self):
        yield from self.__keys

    @property
    def color(self) -> Color:
        return self._color

    @property
    def style(self) -> Style:
        return self._style

    @property
    def font(self) -> Union[Font, None]:
        return self._font
    @font.setter
    def font(self, value: Union[str, Font]):
        # While changes to the theme (color and style) are automatically
        # reflected on any item using it, the font is not and must be
        # manually applied with each change.
        if not value:
            self._font = None
        elif isinstance(value, str):
            self._font = Font.get_font(value)
        else:  # assumed Font type
            self._font = value
        # This will properly set the font and apply the current size
        # to items.
        self.font_size = self.__font_size_value
        
    @property
    def font_size(self) -> float:
        return self.__font_size_value
    @font_size.setter
    def font_size(self, value: float):
        # See font setter comment.
        if value < 0:
            raise FontSizeError("`font_size` cannot be less than zero.")
        
        font = self._font
        self.__font_size_value = value
        # This means that the font doesn't need to be applied to
        # anything.
        if not font and self.__font_id == 0:
            return None
        # If __font_id is not 0, that means self.font was changed to 
        # None in the prior frame (which should have been font.setter).
        self.__font_id = font.get_size(value) if font else 0
        self._set_font()

    @property
    def targets(self) -> list[Item]:
        """Returns a list of items that the theme is directly applied to. 
        """
        appitems = self.APPITEMS
        return [item for item_id in self.__item_ids if
                (item := appitems.get(item_id, None))]

    ### Misc. methods ####
    def configure(
        self,
        color: dict = None,
        style: dict = None,
        font: Union[str, Font] = None,
        font_size: float = None) -> Theme:
        """Customize and return the theme.
        """
        self._color.configure(**color)
        self._style.configure(**style)

        # Setting this first so the font property will
        # call the font_size property if it needs to.
        if font_size:
            self.__font_size_value = font_size
        if font:
            self.font = font

        return self

    def configuration(self) -> dict:
        """Returns the theme's configuration.

        NOTE: The return value of this method contains all of the
        input parameters for `configure` method.
        """
        return {
            "color": self.color.configuration(),
            "style": self.style.configuration(),
            "font": self.font,
            "font_size": self.font_size,
        }

    def renew(self) -> None:
        """Resets all theme elements to their default values.
        """
        delete_item(self._tag, children_only=True)
        self._color._element_ids.clear()
        self._style._element_ids.clear()

    
    #### Applying/Removing ####
    def apply(self, item: Item):
        """Applies the theme to *item*. The theme will be shown only if
        the item **is not** disabled. If an item is in a disabled state,
        the item's "disabled theme" will be used. An item can only have
        1 "enabled" theme and 1 "disabled" theme set at a time -- an
        existing set theme will be unset. Cannot be applied to staged
        items.
        """
        item_id = item._tag
        # Since font is tied to the main enabled theme we need to
        # track items so we can manually apply the font as it changes.
        self.__item_ids.add(item_id)
        set_item_theme(item_id, self._tag)
        set_item_font(item_id, self.__font_id)

    def apply_as_disabled(self, item: Item):
        """Applies the theme to *item*. The theme will be shown only if
        the item **is** disabled. If an item is not in a disabled state,
        the item's "enabled theme" will be used. An item can only have
        1 "enabled" theme and 1 "disabled" theme set at a time -- an
        existing set theme will be unset. Cannot be applied to staged
        items.

        NOTE: the theme's *font* and *font_size* cannot be applied to an
        item's disabled theme.
        """
        set_item_disabled_theme(item._tag, self._tag)

    def unapply(self, item: Item):
        """Applies the current enabled default theme to the item,
        or the system default is no default theme is set.
        """
        item_id = item._tag
        self.__item_ids.remove(item_id)
        # 0 is the system default font/theme id.
        set_item_theme(item_id, 0)
        set_item_font(item_id, 0)

    def unapply_disabled(self, item: Item):
        """Applies the current disabled default theme to the item,
        or the system default is no default theme is set.
        """
        # 0 is the system default font/theme id.
        set_item_disabled_theme(item._tag, 0)

    #### Internal-use ####
    def _set_font(self):
        font_id = self.__font_id
        item_ids = self.__item_ids
        # Since theme and font are seperate internally, all of the
        # items passed through "apply" need to be tracked so we can
        # set the "new" font per item.
        for _, item_id in enumerate(item_ids):
            if item_id not in self.APPITEMS:
                item_ids.remove(item_id)
                continue
            set_item_font(item_id, font_id)

        cls = type(self)
        # If this theme is also the default theme:
        if self._tag == cls.__gl_theme_id:
            configure_item(font_id, default_font=True)
            cls.__gl_font_id = font_id
        
    def _set_as_default(self):
        cls = type(self)
        theme_id = self._tag
        font_id = self.__font_id
        gl_theme_id = cls.__gl_theme_id
        gl_font_id = cls.__gl_font_id

        if gl_theme_id:
            configure_item(gl_theme_id, default_theme=False)
        if gl_font_id:
            configure_item(gl_font_id, default_font=False)

        configure_item(theme_id, default_theme=True)
        if font_id:
            configure_item(font_id, default_font=True)

        # Can't fetch the current default font or theme with
        # the current API so it needs to be tracked.
        cls.__gl_theme_id = theme_id
        cls.__gl_font_id = font_id




#### Theme helper classes ####
class ThemeProperty(Mapping):
    """A dictionary-like object for setting and removing theme
    elements. Values of each element are saved on the instance.

    NOTE: Attributes not defined on the class itself cannot be
    set as instance attributes.
    """
    _elements: set = {}
    _command: Callable = ...

    def __init__(self, parent: Item):
        self._parent = parent
        self._parent_id = parent._tag
        self._element_ids = {}

        set_attr = object.__setattr__
        # Setting all elements as attributes on the instance.
        [set_attr(self, elem, None) for elem in self._elements]

    def __init_subclass__(cls):
        func_map = {
            "color": "_ThemeProperty__set_color",
            "style": "_ThemeProperty__set_style",
        }
        super().__init_subclass__()
        # Could have been in __init__, but this way it's only populated once.
        cls._elements = cls._elements = {k for k in cls.__dict__ if not k.startswith("_")}
        # Using the subclass name to determine which setter to use.
        cls._command = getattr(cls, func_map[cls.__qualname__.lower()])

    def __repr__(self):
        return f"{self.configuration()}"

    def __getitem__(self, item) -> ElementValue:
        return getattr(self, item)

    def __setitem__(self, item, value: ElementValue):
        setattr(self, item, value)

    def __delitem__(self, item):
        delattr(self, item)

    def __setattr__(self, attr, value: ElementValue):
        # This class only allows setting private or element attributes
        # ("element" as in a theming element -- defined on a subclass).
        if attr in self._elements:
            old_element_id = self._element_ids.pop(attr, None)
            if old_element_id:
                delete_item(old_element_id)
            if value is None:
                self.__dict__[attr] = value
            else:
                self.__dict__[attr] = self._command(attr, value)
            return None
        # "Private" attribute.
        elif attr.startswith("_"):
            return object.__setattr__(self, attr, value)
        raise AttributeError(f"{attr!r} cannot be set.")

    def __delattr__(self, item):
        # Not actually deleting the attribute from the instance, but setting
        # the value to None and deleting the registered element item.
        delete_item(self._element_ids.pop(item))
        self.__dict__[item] = None  # bypassing __setattr__
        
    def __iter__(self):
        yield from self._elements

    def __len__(self):
        return len(self._elements)

    def configure(self, **config) -> None:
        """Configure several elements.
        """
        [setattr(elem, value) for elem, value in config.items()]

    def configuration(self) -> dict[str, ElementValue]:
        """Returns the theme attribute's configuration.
        """
        return dict(self.items())

    @property
    def elements(self):
        return self._elements

    def __set_color(self, element: str, value):
        # Called if cls._command == __set_color (i.e. `Color` subclass)
        default_alpha = 255
        try:
            r, g, b, *a = value
        except TypeError:
            raise TypeError(
                f"minimum 3 values expected, but got {len(value)}.")
        a = a[0] if a else default_alpha
        element_uuid, category = getattr(type(self), element)
        ele_id = add_theme_color(element_uuid, [r, g, b, a],
                        category=category, parent=self._parent_id)
        self._element_ids[element] = ele_id
        
        return r, g, b, a

    def __set_style(self, element, value):
        # Called if cls._command == __set_color (i.e. `Style` subclass)
        # TypeError could be raised.
        x, y = value
        element_uuid, category = getattr(type(self), element)
        ele_id = add_theme_style(element_uuid, x, y, category=category,
                        parent=self._parent_id)
        self._element_ids[element] = ele_id
        return x, y


# NOTE: Elements (attributes) defined on the class contain a tuple: the 
# value of the element constant that the attribute represents (like
# "mvStyleVar") as the first value, and the category that the constant
# belongs to ("mvThemeCol_") for the second. They are the parameters used
# for setter functions to set an actual value. The real values are stored
# on the instance. So, `cls.border = (5, 0)`, while `self.border` is the
# actual value.
#
# `mvThemeCat_` values (tuple[1]):
#    0 == `mvThemeCat_Core`
#    1 == `mvThemeCat_Plot`
#    2 == `mvThemeCat_Nodes`
class Color(ThemeProperty):
    border = 5, 0
    border_shadow = 6, 0
    button = 21, 0
    button_active = 23, 0
    button_hovered = 22, 0
    check_mark = 18, 0
    child_bg = 3, 0
    docking_empty_bg = 39, 0
    docking_preview = 38, 0
    drag_drop_target = 50, 0
    frame_bg = 7, 0
    frame_bg_active = 9, 0
    frame_bg_hovered = 8, 0
    header = 24, 0
    header_active = 26, 0
    header_hovered = 25, 0
    menu_bar_bg = 13, 0
    modal_window_dim_bg = 54, 0
    nav_highlight = 51, 0
    nav_windowing_dim_bg = 53, 0
    nav_windowing_highlight = 52, 0
    node_background = 0, 2
    node_background_hovered = 1, 2
    node_background_selected = 2, 2
    node_box_selector = 12, 2
    node_box_selector_outline = 13, 2
    node_grid_background = 14, 2
    node_grid_line = 15, 2
    node_link = 7, 2
    node_link_hovered = 8, 2
    node_link_selected = 9, 2
    node_outline = 3, 2
    node_pin = 10, 2
    node_pin_hovered = 11, 2
    node_title_bar = 4, 2
    node_title_bar_hovered = 5, 2
    node_title_bar_selected = 6, 2
    plot_bg = 6, 1
    plot_border = 7, 1
    plot_crosshairs = 23, 1
    plot_error_bar = 4, 1
    plot_fill = 1, 1
    plot_frame_bg = 5, 1
    plot_histogram = 42, 0
    plot_histogram_hovered = 43, 0
    plot_inlay_text = 12, 1
    plot_legend_bg = 8, 1
    plot_legend_border = 9, 1
    plot_legend_text = 10, 1
    plot_line = 0, 1
    plot_lines = 40, 0
    plot_lines_hovered = 41, 0
    plot_marker_fill = 3, 1
    plot_marker_outline = 2, 1
    plot_query = 22, 1
    plot_selection = 21, 1
    plot_title_text = 11, 1
    plot_x_axis = 13, 1
    plot_x_axis_grid = 14, 1
    plot_y_axis = 15, 1
    plot_y_axis2 = 17, 1
    plot_y_axis3 = 19, 1
    plot_y_axis_grid = 16, 1
    plot_y_axis_grid2 = 18, 1
    plot_y_axis_grid3 = 20, 1
    popup_bg = 4, 0
    resize_grip = 30, 0
    resize_grip_active = 32, 0
    resize_grip_hovered = 31, 0
    scrollbar_bg = 14, 0
    scrollbar_grab = 15, 0
    scrollbar_grab_active = 17, 0
    scrollbar_grab_hovered = 16, 0
    separator = 27, 0
    separator_active = 29, 0
    separator_hovered = 28, 0
    slider_grab = 19, 0
    slider_grab_active = 20, 0
    tab = 33, 0
    tab_active = 35, 0
    tab_hovered = 34, 0
    tab_unfocused = 36, 0
    tab_unfocused_active = 37, 0
    table_border_light = 46, 0
    table_border_strong = 45, 0
    table_header_bg = 44, 0
    table_row_bg = 47, 0
    table_row_bg_alt = 48, 0
    text = 0, 0
    text_disabled = 1, 0
    text_selected_bg = 49, 0
    title_bg = 10, 0
    title_bg_active = 11, 0
    title_bg_collapsed = 12, 0
    window_bg = 2, 0


class Style(ThemeProperty):
    alpha = 0, 0
    button_text_align = 22, 0
    cell_padding = 16, 0
    child_border_size = 7, 0
    child_rounding = 6, 0
    frame_border_size = 12, 0
    frame_padding = 10, 0
    frame_rounding = 11, 0
    grab_min_size = 19, 0
    grab_rounding = 20, 0
    indent_spacing = 15, 0
    item_inner_spacing = 14, 0
    item_spacing = 13, 0
    node_border_thickness = 4, 2
    node_corner_rounding = 1, 2
    node_grid_spacing = 0, 2
    node_link_hover_distance = 7, 2
    node_link_line_segments_per_length = 6, 2
    node_link_thickness = 5, 2
    node_padding_horizontal = 2, 2
    node_padding_vertical = 3, 2
    node_pin_circle_radius = 8, 2
    node_pin_hover_radius = 12, 2
    node_pin_line_thickness = 11, 2
    node_pin_offset = 13, 2
    node_pin_quad_side_length = 9, 2
    node_pin_triangle_side_length = 10, 2
    plot_annotation_padding = 23, 1
    plot_border_size = 9, 1
    plot_default_size = 25, 1
    plot_digital_bit_gap = 8, 1
    plot_digital_bit_height = 7, 1
    plot_error_bar_size = 5, 1
    plot_error_bar_weight = 6, 1
    plot_fill_alpha = 4, 1
    plot_fit_padding = 24, 1
    plot_label_padding = 18, 1
    plot_legend_inner_padding = 20, 1
    plot_legend_padding = 19, 1
    plot_legend_spacing = 21, 1
    plot_line_weight = 0, 1
    plot_major_grid_size = 15, 1
    plot_major_tick_len = 11, 1
    plot_major_tick_size = 13, 1
    plot_marker = 1, 1
    plot_marker_size = 2, 1
    plot_marker_weight = 3, 1
    plot_min_size = 26, 1
    plot_minor_alpha = 10, 1
    plot_minor_grid_size = 16, 1
    plot_minor_tick_len = 12, 1
    plot_minor_tick_size = 14, 1
    plot_mouse_pos_padding = 22, 1
    plot_padding = 17, 1
    popup_border_size = 9, 0
    popup_rounding = 8, 0
    scrollbar_rounding = 18, 0
    scrollbar_size = 17, 0
    selectable_text_align = 23, 0
    tab_rounding = 21, 0
    window_border_size = 3, 0
    window_min_size = 4, 0
    window_padding = 1, 0
    window_rounding = 2, 0
    window_title_align = 5, 0




###################################
############## Font ###############
###################################
class FontRangeHint(enum.Enum):
    Chinese_Full = 3
    Chinese_Simplified_Common = 4
    Cyrillic = 5
    Default = 0
    Japanese = 1
    Korean = 2
    Thai = 6
    Vietnamese = 7


class Font:
    """Global font manager and registry system.
    """
    __fonts: dict = {}
    # Loading font files is expensive. Each font is rendered as a bitmap, so
    # the size can't be changed easily while maintaining a quality render. 
    # Changing the font size means creating a new internal font item. To streamline
    # the end-user API and avoid needlessly creating new font items, this class
    # (and instances) track all font files and sizes passed -- caching them for
    # reuse when possible.
    def __new__(cls, file: str, size: Numeric = 12.0, label: str = None) -> Font:
        if font := cls.__fonts.get(file, None):
            return font(size)
        instance = object.__new__(cls)
        return instance
    
    def __init__(self, file: str, size: Numeric = 12.0, label: str = None) -> None:
        self.__sizes: dict[Numeric,int] = {}
        self.__file = file
        self.__characters: list = []
        self.__ranges: list[tuple] = []
        self.__range_hints: list[FontRangeHint] = []

        self.label = label or file
        # Registering new font object
        type(self).__fonts[file] = self
        # Creates a font item of *size*.
        self(size)

    def __repr__(self):
        config = ("label", "file", "sizes", "range_hints", "characters")
        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={getattr(self, attr)!r}' for attr in config))
            + f")"
        )
 
    def __call__(self, size: Numeric = 12.0, **kwargs) -> Font:
        """Creates a font item of *size*, then returns the instance.

        Args:
            size (Numeric, optional): Size of the (new) font item.
        """
        # If a font item (id) of that size exists already, there's no need 
        # to create a new one.
        if size in self.__sizes:
            return self

        font_id = add_font(self.__file, size)
        # Addl. characters
        add_font_chars(self.__characters, parent=font_id)
        # Character ranges
        [add_font_range(start, stop, parent=font_id)
         for start, stop in self.__ranges]
        # Range hints
        [add_font_range_hint(hint.value, parent=font_id)
         for hint in self.__range_hints]

        self.__sizes[float(size)] = font_id
        return self

    @property
    def file(self):
        return self.__file
        
    @property
    def fonts(self) -> dict[str,Font]:
        """A mapping of all loaded font files.
        """
        return type(self).__fonts

    @property
    def sizes(self) -> list[float]:
        """Returns a list copy of loaded font sizes.
        """
        return [size for size in self.__sizes.keys()]
    
    @property
    def characters(self) -> list[int]:
        """Returns a list copy of additional characters registered to the font.
        """
        return self.__characters.copy()

    @property
    def range_hints(self) -> list[FtRangeHint]:
        """Returns a list copy of the range hints used by the font.
        """
        return self.__range_hints.copy()

    @classmethod
    def get_range_hints(cls) -> list:
        """Returns a list of all available font range hints.
        """
        return [hint for hint in FontRangeHint.__members__]

    @classmethod
    def get_font(cls, file: str, size: Numeric = 12.0, label: str = None) -> Font:
        """Returns a font instance that manages *file*.

        Args:
            file (str): File path of the file to load.
            size (Numeric, optional): Size of the font. Only used if a new instance
            would be created. Defaults to 12.0.
            label (str, optional): A name for the font. Only used if a new
            instance would be created. Defaults to None.
        """
        # This may or may not create a new instance. See `__new__`.
        return cls(file, size, label)

    def get_size(self, size: Numeric = 12.0) -> int:
        """Returns the font id of the given *size*.

        Args:
            size (Numeric, optional): Size of the requested font item. Defaults
            to 12.0.
        """
        # This is very similar to just calling the font instance, but a font id
        # of the size is returned instead of the instance itself.
        return self(size).__sizes[size]


    #### Configuration methods ####
    def add_characters(self, *chars: Numeric) -> None:
        """Adds additional characters to the font
        """
        self.__characters += chars
        # Applying characters to all font items.
        [add_font_chars(chars, parent=font_id)
         for font_id in self.__sizes.values()]

    def add_character_range(self, first_char: Numeric, last_char: Numeric) -> None:
        """Adds a range of characters to the font.
        """
        # NOTE: Need to find out how to generate these myself
        # so they can be added to *self.__characters*. Meanwhile
        # the range managed as-is.
        self.__ranges.append((first_char, last_char))
        # Applying new range to all font items.
        [add_font_range(first_char, last_char, parent=font_id)
         for font_id in self.__sizes.values()]

    def add_range_hint(self, range_hint: FtRangeHint) -> None:
        """Adds a font range hint to the font.
        """
        range_hint = self.__manage_range_hint(range_hint)
        # Every existing font item needs to have the new hint
        # applied.
        [add_font_range_hint(range_hint, parent=font_id)
         for font_id in self.__sizes.values()]


    #### Misc. ####
    def apply(self, item: Item, size: Numeric = 12.0) -> None:
        """Applies the font of *size* to *item*. 

        Args:
            item (Item): Item that you want to use the font.
        """
        # This will create a new font item if it doesn't exist, then
        # apply it.
        return set_item_font(item._tag, self(size).__sizes[size])

    def delete(self) -> None:
        """Deletes the font object.
        """
        # Removing from cache.
        type(self).__fonts.pop(self.__file)
        # Deleting all individual font items.
        for font_id in self.__sizes.values():
            try:
                delete_item(font_id)
            except SystemError:
                continue
        del self

    def load_sizes(self, *sizes: Numeric):
        """Creates a font item for each numeric in *sizes*.

        NOTE: Loading several sizes at once may cause hanging in your
        application. 
        """
        font_sizes = self.__sizes
        file = self.__file
        [font_sizes.update({font_size: add_font(file, font_size)})
         for font_size in sizes]


    #### Internal-use ####
    @singledispatchmethod
    def __manage_range_hint(self, range_hint) -> None:
        raise TypeError(f"{range_hint} is not a valid font range hint.")

    @__manage_range_hint.register
    def _(self, range_hint: FontRangeHint):
        self.__range_hints.append(range_hint)
        return range_hint.value
    @__manage_range_hint.register
    def _(self, range_hint: str):
        hint_member = FontRangeHint[range_hint]
        self.__range_hints.append(hint_member)
        return hint_member.value
    @__manage_range_hint.register
    def _(self, range_hint: int):
        hint_member = FontRangeHint(range_hint)
        self.__range_hints.append(hint_member)
        return hint_member.value
