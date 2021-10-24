from __future__ import annotations
from collections.abc import Mapping
from typing import Callable, Union, Sequence, Any
from functools import singledispatchmethod, wraps
import enum
from dearpygui import _dearpygui
from dearpygui.dearpygui import (
    # theme
    add_theme,
    add_theme_component,
    add_theme_color,
    add_theme_style,
    bind_theme,
    bind_item_theme,
    # font
    bind_font,
    bind_item_font,
    add_font,
    add_font_chars,
    add_font_range,
    add_font_range_hint,
    # misc
    configure_item
)
from dearpypixl.item import Item, configuration_override
from dearpypixl.errors import ItemBindingError
from dearpypixl.constants import (
    CoreThemeElement,
    PlotThemeElement,
    NodeThemeElement,
    ItemCategory,
    FontRangeHint,
    _ThemeElementT,
    ThemeElementTData,
)


__all__ = [
    "Theme",
    "ThemeComponent",
    "ColorComponent",
    "StyleComponent",

    "Font",

    "ItemCategory",
    "CoreThemeElement",
    "PlotThemeElement",
    "NodeThemeElement",
    "FontRangeHint",
]


# Type hints
Numeric: Union[int, float]
ThemeElement = Union[
    "_ThemeElementT",
    "CoreThemeElement",
    "NodeThemeElement",
    "PlotThemeElement",
]





###################################
############## Theme ##############
###################################
class Theme(Mapping, Item):
    """A configurable mapping-like item that stores color and style
    values. Items will reflect the theme that they are bound to. Items can
    only be bound to 1 Theme item at a time -- creating a new bind safely
    destroys the previous one. However, an error will occur when trying to
    manually unbind an item from a Theme that isn't bound.
    """
    def __init__(
        self,
        label: str = None,
        font: Union[str, Font] = None,
        font_size: float = 12.0, 
        *,
        include_presets: bool = True,
    ):
        self.__keys: set[str] = {"label", "font", "font_size"}
        self.__preset = include_presets
        self.__target_uuids: set[int] = set()
        self.__font: Font = font
        self.__font_uuid: int = 0
        self.__font_size_value: float = font_size

        super().__init__(label=label)

        if include_presets:
            self.color = ColorComponent(ItemCategory.ALL, enabled_state=True, parent=self.tag)
            self.style = StyleComponent(ItemCategory.ALL, enabled_state=True, parent=self.tag)

    def __setattr__(self, attr, value):  # Overloaded
        if isinstance(value, ThemeComponent):
            self.__keys.add(attr)
        elif attr in self.__keys:
            # attr formerly was a ThemeComponent
            self.__keys.remove(attr)
        object.__setattr__(self, attr, value)

    def __getattr__(self, attr):  # Overloaded
        raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(self, item, value)

    def __len__(self):
        return len(self.__keys)

    def __iter__(self):
        yield from self.__keys

    def __str__(self):
        mapping = {k: str(v) for k, v in dict(self).items()}
        return f"{mapping}"

    def __enter__(self):
        _dearpygui.push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        _dearpygui.pop_container_stack()


    @property
    def label(self) -> str:
        return _dearpygui.get_item_configuration(self._tag)["label"]
    @label.setter
    def label(self, value: str):
        configure_item(self._tag, label=value)


    @property
    def targets(self) -> list[Item]:
        """Items currently bound to this theme.
        """
        target_uuids = self.__target_uuids
        appitems = type(self)._appitems
        return [target_item for targets in target_uuids
                for target in targets if
                (target_item := appitems.get(target, None))]


    @property
    def font(self) -> Union[Font, None]:
        """Font item used by this theme. If set as a `str` (filepath),
        will try to load the font.
        """
        return self.__font
    @font.setter
    def font(self, value: Union[str, Font, None]):
        # While changes to the theme (color and style) are automatically
        # reflected on any item using it, the font is not and must be
        # manually applied with each change.
        if not value:
            self.__font = None
        elif isinstance(value, str):
            # Get a suitable Font object from `value` (should be a filepath)
            self.__font = Font.get_font_tag(value)
        else:  # assumed `Font` type
            self.__font = value
        # Having font_size.setter update bound items with the font, if needed.
        self.font_size = self.__font_size_value


    @property
    def font_size(self) -> float:
        return self.__font_size_value
    @font_size.setter
    def font_size(self, value: float):
        if value < 0:
            raise ValueError(f"`font_size` cannot be less than zero (got {value!r}).")
        font = self.__font
        self.__font_size_value = value
        # This means that the font doesn't need to be applied to anything.
        if not font and self.__font_uuid == 0:
            return None
        # If __font_id is not 0, that means self.font was set to
        # None in the prior frame via font property (NOTE: See font setter comment).
        self.__font_uuid = font.get_size(value) if font else 0
        self.__update_targets_font()

    def configure(
            self,
            label: str = ...,
            color: dict = ...,
            style: dict = ...,
            font: Union[str, Font] = ...,
            font_size: float = ...,
    ) -> Theme:
        """Customize and return the theme. Useful for creating themes from
        mappings (presets only).
        """
        if label != ...:
            self.label = label
        if color != ...:
            self.color.configure(**color)
        if style != ...:
            self.style.configure(**style)
        # Setting this first because the font property will
        # call the font_size property if it needs to.
        if font_size != ...:
            self.__font_size_value = font_size
        if font != ...:
            self.font = font

        return self

    def configuration(self) -> dict:
        """Returns the theme's configuration.

        NOTE: The return value of this method contains all of the
        input parameters for `configure` method.
        """
        return {attr: getattr(self, attr) for attr in self.__keys}

    def renew(self) -> None:
        """Deletes all of the theme's children, including theme components.
        Any presets will be re-created if `include_presets` was True on
        instantiation.
        """
        super().renew()
        if self.__preset:
            self.color = ColorComponent(ItemCategory.ALL, enabled_state=True, parent=self.tag)
            self.style = StyleComponent(ItemCategory.ALL, enabled_state=True, parent=self.tag)

    def bind(self, *item: Item) -> None:
        """Link item(s) to the theme. If no item is passed, the theme will
        be set as the new default theme.

        Args:
            * item(Item, optional): instances of `Item` to bind to the theme.
            Binding an item will break an existing bind to a Theme (if it exists).
        """
        self_uuid = self._tag
        self_target_uuids = self.__target_uuids
        for i in item:
            bind_item_theme(i._tag, self_uuid)
            bind_item_font(i._tag, self.__font_uuid)
            self_target_uuids.add(i._tag)
        
        # Sets as default
        if not item:
            bind_theme(self_uuid)
            bind_font(self.__font_uuid)
            type(self).__default_theme_uuid = self_uuid
   
    def unbind(self, *item: Item) -> None:
        """Unlink item(s) from the theme. If no item is passed and the theme
        is the default theme, it will no longer be the default theme.

        Args:
            * item(Item, optional): instances of `Item` to unbind from the theme. If an
            item is not bound to this Theme, `BindItemError` will be raised. 
        """
        self_target_uuids = self.__target_uuids
        for i in item:
            if i._tag not in self_target_uuids:
                raise ItemBindingError(f"Cannot unbind `item`: it is not bound to this item.")
            bind_item_theme(i._tag, 0)  # 0 is system default theme
            bind_item_font(i._tag, 0)  # 0 is system default theme
        
        # If default, unset
        if not item and self._tag == type(self).__default_theme_uuid:
            bind_theme(0)
            bind_font(0)
            type(self).__default_theme_uuid = 0

    ################################
    ####### Private/Internal #######
    ################################
    _command = add_theme
    __default_theme_uuid = 0  # no way to fetch via DPG API
    __keys = {}

    def __update_targets_font(self):
        # font.setter uses this to bind a new font (size) to all bound items.
        font_uuid = self.__font_uuid
        target_uuids = self.__target_uuids
        # Since theme and font are seperate internally we need to rebind
        # all targets to the new font item.
        for item_uuid in target_uuids:
            bind_item_font(item_uuid, font_uuid)

        # If this theme is also the default theme:
        if self._tag == type(self).__default_theme_uuid:
            bind_font(font_uuid)
            

class ThemeComponent(Mapping, Item):
    def __init__(
        self,
        item_type: ItemCategory = ItemCategory.ALL,
        enabled_state: bool = True,
        parent: Theme = None,
        label: str = None,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
            item_type=int(item_type),
            enabled_state=enabled_state,
            parent=parent or 0,
            label=label,
            user_data=user_data,
            **kwargs
        )
        # Importing class element data. The data needs to be kept per-instance
        # because it may change via `bind`.
        cls = type(self)
        self.__element_aliases: dict[str, ThemeElement] = {**cls.__element_aliases}
        self.__element_uuids: dict[ThemeElement, int] = {element: None for element in
                                                         self.__element_aliases.values()}
        self.__item_type = item_type
        self.label = label
        self.enabled_state = enabled_state
        self.parent = parent

    def __init_subclass__(cls):
        # NOTE: Subclassing `ThemeComponent` allows elements to be pre-bound
        # to their instances by defining class attributes of type `ThemeElement`.
        super().__init_subclass__()
        element_aliases = cls.__element_aliases = {}
        for attr in dir(cls):
            if attr.startswith("_") or not isinstance((enum_member := getattr(cls, attr)), _ThemeElementT):
                continue
            # Applicable class attributes are bound as elements (equivelent to calling
            # `bind` but stored on the class).
            element_aliases[attr] = enum_member
            # Attribute needs to be deleted, or else __getattribute__ won't call
            # __getattr__ for instances.
            type.__delattr__(cls, attr)

    def __enter__(self):
        _dearpygui.push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        _dearpygui.pop_container_stack()

    def __setattr__(self, attr, value):
        if attr in self.__element_aliases:
            try:
                return self.add_element(attr, *value)
            except TypeError:
                return self.add_element(attr, value)
        super().__setattr__(attr, value)

    def __getattr__(self, attr):
        if element := self.__element_aliases.get(attr, None):
            try:
                return _dearpygui.get_value(self.__element_uuids[element])
            except SystemError:
                return None
        super().__getattr__(attr)

    def __delattr__(self, attr):
        # Need to unbind if the attribute is bound to an element.
        element = self.__element_aliases.pop(attr, None)
        if element and (element_uuid := self.__element_uuids.get(element, None)):
            _dearpygui.delete_item(element_uuid)
            self.__element_uuids[element] = None
        if element:
            return None
        super().__delattr__(attr)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(self, item, value)

    def __len__(self):
        return len(self.__element_aliases)

    def __iter__(self):
        yield from self.__element_aliases

    def __str__(self):
        mapping = {k: str(v) for k, v in dict(self).items()}
        return f"{mapping}"

    def __manage_target_param(method: Callable = None):
        @wraps(method)
        def wrapper(self, target: Union[str, ThemeElement], *value: Numeric):
            aliases = getattr(self, "_ThemeComponent__element_aliases")
            target = aliases.get(target, target)
            try:
                target.value
            except AttributeError:
                raise TypeError(f"`target` parameter {target!r} is not of type `ThemeElement`, or is not a bound theme attribute.")
            return method(self, target, *value)
        return wrapper

    @property
    def item_type(self) -> ItemCategory:
        """Elements items parented by this component will only affect this
        type of appitem, and all children parented by that appitem type.
        """
        return self.__item_type

    @__manage_target_param
    def add_element(self, target: Union[ThemeElement, str], *value: Numeric) -> int:
        """Update an existing theme element, or create a new one if one doesn't exist,
        for `target` with `value`. The `target` must be of type `ThemeElement`, or a
        `ThemeElement`-bound instance attribute name.

        Color elements have 4 parameters (in order: r=0, g=0, b=0, a=255) with applicable values
        ranging from 0 to 255, while style elements can have UP to 2 parameters (in order:
        x=1, y=-1) with values varying ranges. Default values will be used for any missing
        positional parameters if the value is being set for the first time. Otherwise,
        remaining existing values will not be changed. `-1` can be used as placeholder 
        values -- For example, passing the value [-1, -1, 150, -1] to an existing color
        element will set `b` to 150, while `r`, `g`, and `a` remain unchainged. If setting
        the value for the first time, `r`, `g`, and `a` will use default values of 0, 0, and
        255, respectively.

        See the `constants` module for more information.

        Args:
            * target (Union[ThemeElement, str]): The element to affect.
            * value (Union[int, float]): Positional parameters for the `target` element value.
        """
        element_data: ThemeElementTData = target.value
        value = list(value)

        number_of_vals = element_data.values
        new_vals_len = len(value)
        try:
            assert new_vals_len <= number_of_vals
        except AssertionError:
            raise TypeError(f"`ThemeElement` {target!r} takes up to {number_of_vals!r} argument(s) ({new_vals_len!r} given).")

        # Adding placeholder values so `value` matches the number of values necessary.
        for _ in range(number_of_vals - new_vals_len):
            value.append(None)

        value_ceil = element_data.value_max

        # Update value of an existing item...
        if element_uuid := self.__element_uuids.get(target, None):
            current_value = _dearpygui.get_value(element_uuid)
            new_value = self.__build_new_value(value, current_value, value_ceil)
            return _dearpygui.set_value(element_uuid, new_value)

        element_type = element_data.element_type
        default_values = self.__element_defaults[element_type]
        new_value = self.__build_new_value(value, default_values, value_ceil)
        
        # New color item
        if element_type == 0:
            element_uuid = add_theme_color(
                element_data.target,
                new_value,
                category=element_data.category,
                parent=self._tag)
        # New style item
        else:  # element_type == 1
            if number_of_vals == 1:
                x = new_value[0]
                y = -1.0
            else:
                x, y = new_value
            element_uuid = add_theme_style(
                element_data.target,
                element_data.value_type(x),
                element_data.value_type(y),
                category=element_data.category,
                parent=self._tag)

        self.__element_uuids[target] = element_uuid
        return element_uuid

    @__manage_target_param
    def get_element_tag(self, target: Union[ThemeElement, str]) -> int:
        """Returns the unique identifier in use for `target`.
        """
        return self.__element_uuids[target]

    def bind(self, attribute: str = None, element: ThemeElement = None, **kwargs: ThemeElement) -> None:
        """Sets new instance attributes and links them to theme elements. Multiple
        attributes can be bound to the same element. If an attribute is already
        bound to an element, an `AttributeError` will be raised. Attributes can be
        unbound from their element with `delattr`.

        Args:
            * attribute (str): the name of the new instance attribute.
            * element (ThemeElement): the element that will be registered.
            * kwargs (keyword-only, optional): attribute:element pairs.
        """
        # `attribute` and `element` must both be truthy or both `None`
        if attribute and not element:
            raise TypeError("Missing `element` parameter.")
        elif not attribute and element:
            raise TypeError("Missing `attribute` parameter.")
        # both `attribute` and `element` exist
        elif attribute:
            kwargs[attribute] = element

        element_aliases = self.__element_aliases
        element_uuids = self.__element_uuids
        for attribute, element in kwargs.items():
            if attribute in element_aliases:
                raise AttributeError(
                    f"{attribute!r} is already bound to an element and can't be set.")
            elif not isinstance(attribute, str):
                raise TypeError(f"`str` expected for `attribute` parameter, got {type(attribute)!r}.")
            elif not isinstance(element, _ThemeElementT):
                raise TypeError(f"`ThemeElement` expected for `element` parameter, got {type(attribute)!r}.")
            element_aliases[attribute] = element
            element_uuids.setdefault(element, None)

    ################################
    ####### Private/Internal #######
    ################################
    _command = add_theme_component
    __element_defaults = {
        0: [0, 0, 0, 255],
        1: [-1.0, -1.0],
    }
    __element_aliases: dict[str, ThemeElement] = {}
   
    @staticmethod
    def __build_new_value(new: Sequence, current: Sequence, value_ceiling):
        def val_map_func(val):
            x, y = val
            if all(x != cond for cond in (None, -1)):
                return x
            return y
        try:
            return [val if val < value_ceiling else value_ceiling
                    for val in map(val_map_func, zip(new, current))]
        except TypeError:  # occurs if value_ceiling is `...` or `None` (no max)
            return [val for val in map(val_map_func, zip(new, current))]

    


class ColorComponent(ThemeComponent):
    """A theme component with pre-bound elements that affect
    color for all theme categories.
    """
    border = CoreThemeElement.Border
    border_shadow = CoreThemeElement.BorderShadow
    button = CoreThemeElement.Button
    button_active = CoreThemeElement.ButtonActive
    button_hovered = CoreThemeElement.ButtonHovered
    check_mark = CoreThemeElement.CheckMark
    child_bg = CoreThemeElement.ChildBg
    docking_empty_bg = CoreThemeElement.DockingEmptyBg
    docking_preview = CoreThemeElement.DockingPreview
    drag_drop_target = CoreThemeElement.DragDropTarget
    frame_bg = CoreThemeElement.FrameBg
    frame_bg_active = CoreThemeElement.FrameBgActive
    frame_bg_hovered = CoreThemeElement.FrameBgHovered
    header = CoreThemeElement.Header
    header_active = CoreThemeElement.HeaderActive
    header_hovered = CoreThemeElement.HeaderHovered
    menu_bar_bg = CoreThemeElement.MenuBarBg
    modal_window_dim_bg = CoreThemeElement.ModalWindowDimBg
    nav_highlight = CoreThemeElement.NavHighlight
    nav_windowing_dim_bg = CoreThemeElement.NavWindowingDimBg
    nav_windowing_highlight = CoreThemeElement.NavWindowingHighlight
    plot_histogram = CoreThemeElement.PlotHistogram
    plot_histogram_hovered = CoreThemeElement.PlotHistogramHovered
    plot_lines = CoreThemeElement.PlotLines
    plot_lines_hovered = CoreThemeElement.PlotLinesHovered
    popup_bg = CoreThemeElement.PopupBg
    resize_grip = CoreThemeElement.ResizeGrip
    resize_grip_active = CoreThemeElement.ResizeGripActive
    resize_grip_hovered = CoreThemeElement.ResizeGripHovered
    scrollbar_bg = CoreThemeElement.ScrollbarBg
    scrollbar_grab = CoreThemeElement.ScrollbarGrab
    scrollbar_grab_active = CoreThemeElement.ScrollbarGrabActive
    scrollbar_grab_hovered = CoreThemeElement.ScrollbarGrabHovered
    separator = CoreThemeElement.Separator
    separator_active = CoreThemeElement.SeparatorActive
    separator_hovered = CoreThemeElement.SeparatorHovered
    slider_grab = CoreThemeElement.SliderGrab
    slider_grab_active = CoreThemeElement.SliderGrabActive
    tab = CoreThemeElement.Tab
    tab_active = CoreThemeElement.TabActive
    tab_hovered = CoreThemeElement.TabHovered
    tab_unfocused = CoreThemeElement.TabUnfocused
    tab_unfocused_active = CoreThemeElement.TabUnfocusedActive
    table_border_light = CoreThemeElement.TableBorderLight
    table_border_strong = CoreThemeElement.TableBorderStrong
    table_header_bg = CoreThemeElement.TableHeaderBg
    table_row_bg = CoreThemeElement.TableRowBg
    table_row_bg_alt = CoreThemeElement.TableRowBgAlt
    text = CoreThemeElement.Text
    text_disabled = CoreThemeElement.TextDisabled
    text_selected_bg = CoreThemeElement.TextSelectedBg
    title_bg = CoreThemeElement.TitleBg
    title_bg_active = CoreThemeElement.TitleBgActive
    title_bg_collapsed = CoreThemeElement.TitleBgCollapsed
    window_bg = CoreThemeElement.WindowBg

    node_bg = NodeThemeElement.NodeBackground
    node_bg_hovered = NodeThemeElement.NodeBackgroundHovered
    node_bg_selected = NodeThemeElement.NodeBackgroundSelected
    node_box_selector = NodeThemeElement.BoxSelector
    node_box_selector_outline = NodeThemeElement.BoxSelectorOutline
    node_grid_bg = NodeThemeElement.GridBackground
    node_grid_line = NodeThemeElement.GridLine
    node_link = NodeThemeElement.Link
    node_link_hovered = NodeThemeElement.LinkHovered
    node_link_selected = NodeThemeElement.LinkSelected
    node_outline = NodeThemeElement.NodeOutline
    node_pin = NodeThemeElement.Pin
    node_pin_hovered = NodeThemeElement.PinHovered
    node_title_bar = NodeThemeElement.TitleBar
    node_title_bar_hovered = NodeThemeElement.TitleBarHovered
    node_title_bar_selected = NodeThemeElement.TitleBarSelected

    plot_bg = PlotThemeElement.PlotBg
    plot_border = PlotThemeElement.PlotBorder
    plot_crosshairs = PlotThemeElement.Crosshairs
    plot_error_bar = PlotThemeElement.ErrorBar
    plot_fill = PlotThemeElement.Fill
    plot_frame_bg = PlotThemeElement.FrameBg
    plot_inlay_text = PlotThemeElement.InlayText
    plot_legend_bg = PlotThemeElement.LegendBg
    plot_legend_border = PlotThemeElement.LegendBorder
    plot_legend_text = PlotThemeElement.LegendText
    plot_line = PlotThemeElement.Line
    plot_marker_fill = PlotThemeElement.MarkerFill
    plot_marker_outline = PlotThemeElement.MarkerOutline
    plot_query = PlotThemeElement.Query
    plot_selection = PlotThemeElement.Selection
    plot_title_text = PlotThemeElement.TitleText
    plot_x_axis = PlotThemeElement.XAxis
    plot_x_axis_grid = PlotThemeElement.XAxisGrid
    plot_y_axis = PlotThemeElement.YAxis
    plot_y_axis2 = PlotThemeElement.YAxis2
    plot_y_axis3 = PlotThemeElement.YAxis3
    plot_y_axis_grid = PlotThemeElement.YAxisGrid
    plot_y_axis_grid2 = PlotThemeElement.YAxisGrid2
    plot_y_axis_grid3 = PlotThemeElement.YAxisGrid3


class StyleComponent(ThemeComponent):
    """A theme component with pre-bound elements that affect
    styling for all theme categories.
    """
    alpha = CoreThemeElement.Alpha
    button_text_align = CoreThemeElement.ButtonTextAlign
    cell_padding = CoreThemeElement.CellPadding
    child_border_size = CoreThemeElement.ChildBorderSize
    child_rounding = CoreThemeElement.ChildRounding
    frame_border_size = CoreThemeElement.FrameBorderSize
    frame_padding = CoreThemeElement.FramePadding
    frame_rounding = CoreThemeElement.FrameRounding
    grab_min_size = CoreThemeElement.GrabMinSize
    grab_rounding = CoreThemeElement.GrabRounding
    indent_spacing = CoreThemeElement.IndentSpacing
    item_inner_spacing = CoreThemeElement.ItemInnerSpacing
    item_spacing = CoreThemeElement.ItemSpacing
    popup_border_size = CoreThemeElement.PopupBorderSize
    popup_rounding = CoreThemeElement.PopupRounding
    scrollbar_rounding = CoreThemeElement.ScrollbarRounding
    scrollbar_size = CoreThemeElement.ScrollbarSize
    selectable_text_align = CoreThemeElement.SelectableTextAlign
    tab_rounding = CoreThemeElement.TabRounding
    window_border_size = CoreThemeElement.WindowBorderSize
    window_min_size = CoreThemeElement.WindowMinSize
    window_padding = CoreThemeElement.WindowPadding
    window_rounding = CoreThemeElement.WindowRounding
    window_title_align = CoreThemeElement.WindowTitleAlign

    node_border_thickness = NodeThemeElement.NodeBorderThickness
    node_corner_rounding = NodeThemeElement.NodeCornerRounding
    node_grid_spacing = NodeThemeElement.GridSpacing
    node_link_hover_distance = NodeThemeElement.LinkHoverDistance
    node_link_line_segments_per_length = NodeThemeElement.LinkLineSegmentsPerLength
    node_link_thickness = NodeThemeElement.LinkThickness
    node_padding_horizontal = NodeThemeElement.NodePaddingHorizontal
    node_padding_vertical = NodeThemeElement.NodePaddingVertical
    node_pin_circle_radius = NodeThemeElement.PinCircleRadius
    node_pin_hover_radius = NodeThemeElement.PinHoverRadius
    node_pin_line_thickness = NodeThemeElement.LinkThickness
    node_pin_offset = NodeThemeElement.PinOffset
    node_pin_quad_side_length = NodeThemeElement.PinQuadSideLength
    node_pin_triangle_side_length = NodeThemeElement.PinTriangleSideLength

    plot_annotation_padding = PlotThemeElement.AnnotationPadding
    plot_border_size = PlotThemeElement.PlotBorderSize
    plot_default_size = PlotThemeElement.PlotDefaultSize
    plot_digital_bit_gap = PlotThemeElement.DigitalBitGap
    plot_digital_bit_height = PlotThemeElement.DigitalBitHeight
    plot_error_bar_size = PlotThemeElement.ErrorBarSize
    plot_error_bar_weight = PlotThemeElement.ErrorBarWeight
    plot_fill_alpha = PlotThemeElement.FillAlpha
    plot_fit_padding = PlotThemeElement.FitPadding
    plot_label_padding = PlotThemeElement.LabelPadding
    plot_legend_inner_padding = PlotThemeElement.LegendInnerPadding
    plot_legend_padding = PlotThemeElement.LegendPadding
    plot_legend_spacing = PlotThemeElement.LegendSpacing
    plot_line_weight = PlotThemeElement.LineWeight
    plot_major_grid_size = PlotThemeElement.MajorGridSize
    plot_major_tick_len = PlotThemeElement.MajorTickLen
    plot_major_tick_size = PlotThemeElement.MajorTickSize
    plot_marker = PlotThemeElement.Marker
    plot_marker_size = PlotThemeElement.MarkerSize
    plot_marker_weight = PlotThemeElement.MarkerWeight
    plot_min_size = PlotThemeElement.PlotMinSize
    plot_minor_alpha = PlotThemeElement.MinorAlpha
    plot_minor_grid_size = PlotThemeElement.MinorGridSize
    plot_minor_tick_len = PlotThemeElement.MinorTickLen
    plot_minor_tick_size = PlotThemeElement.MinorTickSize
    plot_mouse_pos_padding = PlotThemeElement.MousePosPadding
    plot_padding = PlotThemeElement.PlotPadding



###################################
############## Font ###############
###################################
class Font:
    """Global font manager and registry system.
    """
    __fonts: dict = {}
    # Loading font files is expensive. Each font is rendered as a bitmap, so
    # the size can't be changed easily while maintaining a quality render.
    # Changing the font size means creating a new internal font item. To streamline
    # the end-user API and avoid needlessly creating new font items, this class
    # (and instances) tracks all font files and sizes passed -- caching them for
    # reuse when possible.

    def __new__(cls, file: str, size: Numeric = 12.0, label: str = None) -> "Font":
        if font := cls.__fonts.get(file, None):
            return font(size)
        instance = object.__new__(cls)
        return instance

    def __init__(self, file: str, size: Numeric = 12.0, label: str = None) -> None:
        self.__sizes: dict[Numeric, int] = {}
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

    def __call__(self, size: Numeric = 12.0, **kwargs) -> "Font":
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

    def __manage_range_hint(method=None):
        @wraps(method)
        def wrapper(self, range_hint: FontRangeHint, *args, **kwargs):
            try:
                range_hint.value
            except AttributeError:
                raise TypeError(f"type `FontRangeHint` expected for `range_hint`, got {type(range_hint)!r}.")
            return method(self, range_hint, *args, **kwargs)
        return wrapper

    @property
    def file(self):
        return self.__file

    @property
    def fonts(self) -> dict[str, "Font"]:
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
    def range_hints(self) -> list[FontRangeHint]:
        """Returns a list copy of the range hints used by the font.
        """
        return self.__range_hints.copy()

    @classmethod
    def get_font_tag(cls, file: str, size: Numeric = 12.0, label: str = None) -> "Font":
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

    @__manage_range_hint
    def add_range_hint(self, range_hint: FontRangeHint) -> None:
        """Adds a font range hint to the font.
        """
        self.__range_hints.append(range_hint)
        # Every existing font item needs to have the new hint
        # applied.
        range_hint = int(range_hint)
        [add_font_range_hint(range_hint, parent=font_id)
         for font_id in self.__sizes.values()]

    #### Misc. ####

    def bind(self, item: Item, size: Numeric = 12.0) -> None:
        """Links the font of *size* to *item*. 

        Args:
            item (Item): the Item that will reflect the font.
        """
        # This will create a new font item if it doesn't exist, then
        # apply it.
        return bind_item_font(item._tag, self(size).__sizes[size])

    def unbind(self, item: Item, size: Numeric = 12.0) -> None:
        """[summary]

        Args:
            item (Item): the Item that will be unbound.
            size (Numeric, optional): [description]. Defaults to 12.0.
        """
        return bind_item_font(item._tag, 0)

    def delete(self) -> None:
        """Deletes the font object.
        """
        # Removing from cache.
        type(self).__fonts.pop(self.__file)
        # Deleting all individual font items.
        for font_id in self.__sizes.values():
            try:
                _dearpygui.delete_item(font_id)
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



