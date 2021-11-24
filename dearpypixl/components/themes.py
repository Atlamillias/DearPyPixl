from __future__ import annotations
from collections.abc import Mapping
from typing import Callable, Union, Sequence, Any, Optional
import functools
from warnings import warn
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
    pop_container_stack,
    push_container_stack,
    get_text_size,
)
from dearpypixl.item.configuration import item_attribute, ItemAttribute
from dearpypixl.item.item import Item
from dearpypixl.constants import (
    CoreThemeElement,
    PlotThemeElement,
    NodeThemeElement,
    ItemIndex,
    FontRangeHint,
    _ThemeElementT,
    ThemeElementTData,
)


__all__ = [
    "Theme",
    "ThemeComponent",
    "ThemeColorComponent",
    "ThemeStyleComponent",
    "Font",
]


# Type hints
Numeric: Union[int, float]
ThemeElementColorValue: Union[tuple[Numeric, Optional[Numeric], Optional[Numeric], Optional[Numeric]], None]
ThemeElementStyleValue: Union[tuple[Numeric, Optional[Numeric]], None]
ThemeElement: Union[
    "_ThemeElementT",
    "CoreThemeElement",
    "NodeThemeElement",
    "PlotThemeElement",
]




###################################
############## Theme ##############
###################################
class Theme(Item):
    """A configurable item that stores color and style
    values. Items will reflect the theme that they are bound to. Items can
    only be bound to 1 Theme item at a time -- creating a new bind safely
    destroys the previous one. However, an error will occur when trying to
    manually unbind an item from a Theme that isn't bound.
    """
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ('ThemeComponent',)                                                                             
    _unique_commands  : tuple    = ('bind_theme',)                                                                                 
    _unique_constants : tuple    = ('mvTheme', 'mvThemeCat_Core', 'mvThemeCat_Plots', 'mvThemeCat_Nodes')                          
    _command          : Callable = add_theme      

    def __init__(
        self,
        label: str = None,
        font: Union[str, Font] = None,
        font_size: float = 12.0, 
        *,
        incl_theme_presets: bool = True,
    ):
        self.__target_uuids: set[int] = set()
        self.__preset = incl_theme_presets
        self.__font: Font = font
        self.__font_uuid: int = 0
        self.__font_size_value: float = font_size

        super().__init__(label=label)

        if incl_theme_presets:
            self.color = ThemeColorComponent(ItemIndex.ALL, enabled_state=True, parent=self.tag)
            self.style = ThemeStyleComponent(ItemIndex.ALL, enabled_state=True, parent=self.tag)

    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        pop_container_stack()

    @property
    @item_attribute(category="configuration")
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
    @item_attribute(category="configuration")
    def font_size(self) -> float:
        return self.__font_size_value
    @font_size.setter
    def font_size(self, value: float):
        if value < 0:
            raise ValueError(f"`font_size` cannot be less than zero (got {value!r}).")
        elif value > 350:
            warn(f"Rendering some fonts at such sizes ({value!r}) can cause a segmentation fault.")
        font = self.__font
        self.__font_size_value = value
        # This means that the font doesn't need to be applied to anything.
        if not font and self.__font_uuid == 0:
            return None
        # If __font_id is not 0, that means self.font was set to
        # None in the prior frame via font property (NOTE: See font setter comment).
        self.__font_uuid = font.get_font_size(value) if font else 0
        self.__update_targets_font()

    @property
    @item_attribute(category="information")
    def targets(self) -> list[Item]:
        """Return a list of items that are bound to this item.
        """
        target_uuids = self.__target_uuids
        appitems = type(self)._AppItemsRegistry
        return [target_item for targets in target_uuids
                for target in targets if
                (target_item := appitems.get(target, None))]

    def renew(self) -> None:
        """Deletes all of the theme's children, including theme components.
        Any presets will be re-created if `include_presets` was True on
        instantiation.
        """
        super().delete(children_only=True)
        if self.__preset:
            self.color = ThemeColorComponent(ItemIndex.ALL, enabled_state=True, parent=self.tag)
            self.style = ThemeStyleComponent(ItemIndex.ALL, enabled_state=True, parent=self.tag)

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
                raise ValueError(f"Cannot unbind {item.__qualname__!r} as it is not bound to this item.")
            bind_item_theme(i._tag, 0)  # 0 is system default theme
            bind_item_font(i._tag, 0)  # 0 is system default theme
        
        # If default, unset
        if not item and self._tag == type(self).__default_theme_uuid:
            bind_theme(0)
            bind_font(0)
            type(self).__default_theme_uuid = 0

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

    __default_theme_uuid = 0  # no way to fetch via DPG API
            

class ThemeComponent(Item):
    item_type         : Union[int, ItemIndex]    =  ItemAttribute("configuration", "get_unmanagable", None, "item_type")
    label             : str                      =  ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any                      =  ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool                     =  ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    enabled_state     : bool                     =  ItemAttribute("configuration", "get_item_configuration", "configure_item", "enabled_state")     

    _is_container     : bool                     =  True                                                                                            
    _is_root_item     : bool                     =  False                                                                                           
    _is_value_able    : bool                     =  False                                                                                           
    _unique_parents   : tuple                    =  ('Theme',)                                                                                      
    _unique_children  : tuple                    =  ('ThemeColor', 'ThemeStyle')                                                                    
    _unique_commands  : tuple                    =  ()                                                                                              
    _unique_constants : tuple                    =  ('mvThemeComponent',)                                                                           
    _command          : Callable                 =  add_theme_component  

    def __init__(
        self                                               ,
        item_type         : Union[int, ItemIndex]    = ItemIndex.ALL,
        label             : str                      = None         ,
        user_data         : Any                      = None         ,
        use_internal_label: bool                     = True         ,
        parent            : Union[int, str]          = 0            ,
        before            : Union[int, str]          = 0            ,
        enabled_state     : bool                     = True         ,
        **kwargs                                                    ,
    ) -> None:
        super().__init__(
            item_type=item_type,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            enabled_state=enabled_state,
            **kwargs,
        )
        # Importing class element data. The data needs to be kept per-instance
        # because it may change via `bind`.
        cls = type(self)
        self.__element_aliases: dict[str, ThemeElement] = {**cls.__element_aliases}
        self.__element_uuids: dict[ThemeElement, int] = {element: None for element in
                                                         self.__element_aliases.values()}

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
        raise AttributeError(f"{type(self).__qualname__!r} has no attribute {attr!r}.")

    def __delattr__(self, attr):
        # Need to unbind if the attribute is bound to an element.
        element = self.__element_aliases.pop(attr, None)
        if element and (element_uuid := self.__element_uuids.get(element, None)):
            _dearpygui.delete_item(element_uuid)
            self.__element_uuids[element] = None
        if element:
            return None
        super().__delattr__(attr)

    def __manage_target_param(method: Callable = None):
        @functools.wraps(method)
        def wrapper(self, target: Union[str, ThemeElement], *value: Numeric):
            aliases = getattr(self, "_ThemeComponent__element_aliases")
            target = aliases.get(target, target)
            try:
                target.value
            except AttributeError:
                raise TypeError(f"`target` parameter {target!r} is not of type `ThemeElement`, or is not a bound theme attribute.")
            return method(self, target, *value)
        return wrapper

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
            * target (ThemeElement | str): The element to affect.
            * value (int | float): Positional parameters for the `target` element value.
        """
        element_data: ThemeElementTData = target.value
        value = list(value)

        number_of_vals = element_data.values
        new_vals_len = len(value)

        if new_vals_len > number_of_vals:
            raise ValueError(f"`ThemeElement` {target!r} takes up to {number_of_vals!r} argument(s) ({new_vals_len!r} given).")

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

    __element_defaults = {
        0: [0, 0, 0, 255],
        1: [-1.0, -1.0],
    }
    __element_aliases: dict[str, ThemeElement] = {}

    
class ThemeColorComponent(ThemeComponent):
    """A theme component with pre-bound elements that affect
    color for all theme categories.
    """
    border                   : ThemeElementColorValue = CoreThemeElement.Border                
    border_shadow            : ThemeElementColorValue = CoreThemeElement.BorderShadow          
    button                   : ThemeElementColorValue = CoreThemeElement.Button                
    button_active            : ThemeElementColorValue = CoreThemeElement.ButtonActive          
    button_hovered           : ThemeElementColorValue = CoreThemeElement.ButtonHovered         
    check_mark               : ThemeElementColorValue = CoreThemeElement.CheckMark             
    child_bg                 : ThemeElementColorValue = CoreThemeElement.ChildBg               
    docking_empty_bg         : ThemeElementColorValue = CoreThemeElement.DockingEmptyBg        
    docking_preview          : ThemeElementColorValue = CoreThemeElement.DockingPreview        
    drag_drop_target         : ThemeElementColorValue = CoreThemeElement.DragDropTarget        
    frame_bg                 : ThemeElementColorValue = CoreThemeElement.FrameBg               
    frame_bg_active          : ThemeElementColorValue = CoreThemeElement.FrameBgActive         
    frame_bg_hovered         : ThemeElementColorValue = CoreThemeElement.FrameBgHovered        
    header                   : ThemeElementColorValue = CoreThemeElement.Header                
    header_active            : ThemeElementColorValue = CoreThemeElement.HeaderActive          
    header_hovered           : ThemeElementColorValue = CoreThemeElement.HeaderHovered         
    menu_bar_bg              : ThemeElementColorValue = CoreThemeElement.MenuBarBg             
    modal_window_dim_bg      : ThemeElementColorValue = CoreThemeElement.ModalWindowDimBg      
    nav_highlight            : ThemeElementColorValue = CoreThemeElement.NavHighlight          
    nav_windowing_dim_bg     : ThemeElementColorValue = CoreThemeElement.NavWindowingDimBg     
    nav_windowing_highlight  : ThemeElementColorValue = CoreThemeElement.NavWindowingHighlight 
    plot_histogram           : ThemeElementColorValue = CoreThemeElement.PlotHistogram         
    plot_histogram_hovered   : ThemeElementColorValue = CoreThemeElement.PlotHistogramHovered  
    plot_lines               : ThemeElementColorValue = CoreThemeElement.PlotLines             
    plot_lines_hovered       : ThemeElementColorValue = CoreThemeElement.PlotLinesHovered      
    popup_bg                 : ThemeElementColorValue = CoreThemeElement.PopupBg               
    resize_grip              : ThemeElementColorValue = CoreThemeElement.ResizeGrip            
    resize_grip_active       : ThemeElementColorValue = CoreThemeElement.ResizeGripActive      
    resize_grip_hovered      : ThemeElementColorValue = CoreThemeElement.ResizeGripHovered     
    scrollbar_bg             : ThemeElementColorValue = CoreThemeElement.ScrollbarBg           
    scrollbar_grab           : ThemeElementColorValue = CoreThemeElement.ScrollbarGrab         
    scrollbar_grab_active    : ThemeElementColorValue = CoreThemeElement.ScrollbarGrabActive   
    scrollbar_grab_hovered   : ThemeElementColorValue = CoreThemeElement.ScrollbarGrabHovered  
    separator                : ThemeElementColorValue = CoreThemeElement.Separator             
    separator_active         : ThemeElementColorValue = CoreThemeElement.SeparatorActive       
    separator_hovered        : ThemeElementColorValue = CoreThemeElement.SeparatorHovered      
    slider_grab              : ThemeElementColorValue = CoreThemeElement.SliderGrab            
    slider_grab_active       : ThemeElementColorValue = CoreThemeElement.SliderGrabActive      
    tab                      : ThemeElementColorValue = CoreThemeElement.Tab                   
    tab_active               : ThemeElementColorValue = CoreThemeElement.TabActive             
    tab_hovered              : ThemeElementColorValue = CoreThemeElement.TabHovered            
    tab_unfocused            : ThemeElementColorValue = CoreThemeElement.TabUnfocused          
    tab_unfocused_active     : ThemeElementColorValue = CoreThemeElement.TabUnfocusedActive    
    table_border_light       : ThemeElementColorValue = CoreThemeElement.TableBorderLight      
    table_border_strong      : ThemeElementColorValue = CoreThemeElement.TableBorderStrong     
    table_header_bg          : ThemeElementColorValue = CoreThemeElement.TableHeaderBg         
    table_row_bg             : ThemeElementColorValue = CoreThemeElement.TableRowBg            
    table_row_bg_alt         : ThemeElementColorValue = CoreThemeElement.TableRowBgAlt         
    text                     : ThemeElementColorValue = CoreThemeElement.Text                  
    text_disabled            : ThemeElementColorValue = CoreThemeElement.TextDisabled          
    text_selected_bg         : ThemeElementColorValue = CoreThemeElement.TextSelectedBg        
    title_bg                 : ThemeElementColorValue = CoreThemeElement.TitleBg               
    title_bg_active          : ThemeElementColorValue = CoreThemeElement.TitleBgActive         
    title_bg_collapsed       : ThemeElementColorValue = CoreThemeElement.TitleBgCollapsed      
    window_bg                : ThemeElementColorValue = CoreThemeElement.WindowBg           

    node_bg                  : ThemeElementColorValue = NodeThemeElement.NodeBackground        
    node_bg_hovered          : ThemeElementColorValue = NodeThemeElement.NodeBackgroundHovered 
    node_bg_selected         : ThemeElementColorValue = NodeThemeElement.NodeBackgroundSelected
    node_box_selector        : ThemeElementColorValue = NodeThemeElement.BoxSelector           
    node_box_selector_outline: ThemeElementColorValue = NodeThemeElement.BoxSelectorOutline    
    node_grid_bg             : ThemeElementColorValue = NodeThemeElement.GridBackground        
    node_grid_line           : ThemeElementColorValue = NodeThemeElement.GridLine              
    node_link                : ThemeElementColorValue = NodeThemeElement.Link                  
    node_link_hovered        : ThemeElementColorValue = NodeThemeElement.LinkHovered           
    node_link_selected       : ThemeElementColorValue = NodeThemeElement.LinkSelected          
    node_outline             : ThemeElementColorValue = NodeThemeElement.NodeOutline           
    node_pin                 : ThemeElementColorValue = NodeThemeElement.Pin                   
    node_pin_hovered         : ThemeElementColorValue = NodeThemeElement.PinHovered            
    node_title_bar           : ThemeElementColorValue = NodeThemeElement.TitleBar              
    node_title_bar_hovered   : ThemeElementColorValue = NodeThemeElement.TitleBarHovered       
    node_title_bar_selected  : ThemeElementColorValue = NodeThemeElement.TitleBarSelected      
    
    plot_bg                  : ThemeElementColorValue = PlotThemeElement.PlotBg                
    plot_border              : ThemeElementColorValue = PlotThemeElement.PlotBorder            
    plot_crosshairs          : ThemeElementColorValue = PlotThemeElement.Crosshairs            
    plot_error_bar           : ThemeElementColorValue = PlotThemeElement.ErrorBar              
    plot_fill                : ThemeElementColorValue = PlotThemeElement.Fill                  
    plot_frame_bg            : ThemeElementColorValue = PlotThemeElement.FrameBg               
    plot_inlay_text          : ThemeElementColorValue = PlotThemeElement.InlayText             
    plot_legend_bg           : ThemeElementColorValue = PlotThemeElement.LegendBg              
    plot_legend_border       : ThemeElementColorValue = PlotThemeElement.LegendBorder          
    plot_legend_text         : ThemeElementColorValue = PlotThemeElement.LegendText            
    plot_line                : ThemeElementColorValue = PlotThemeElement.Line                  
    plot_marker_fill         : ThemeElementColorValue = PlotThemeElement.MarkerFill            
    plot_marker_outline      : ThemeElementColorValue = PlotThemeElement.MarkerOutline         
    plot_query               : ThemeElementColorValue = PlotThemeElement.Query                 
    plot_selection           : ThemeElementColorValue = PlotThemeElement.Selection             
    plot_title_text          : ThemeElementColorValue = PlotThemeElement.TitleText             
    plot_x_axis              : ThemeElementColorValue = PlotThemeElement.XAxis                 
    plot_x_axis_grid         : ThemeElementColorValue = PlotThemeElement.XAxisGrid             
    plot_y_axis              : ThemeElementColorValue = PlotThemeElement.YAxis                 
    plot_y_axis2             : ThemeElementColorValue = PlotThemeElement.YAxis2                
    plot_y_axis3             : ThemeElementColorValue = PlotThemeElement.YAxis3                
    plot_y_axis_grid         : ThemeElementColorValue = PlotThemeElement.YAxisGrid             
    plot_y_axis_grid2        : ThemeElementColorValue = PlotThemeElement.YAxisGrid2            
    plot_y_axis_grid3        : ThemeElementColorValue = PlotThemeElement.YAxisGrid3 


class ThemeStyleComponent(ThemeComponent):
    """A theme component with pre-bound elements that affect
    styling for all theme categories.
    """
    alpha                             : ThemeElementStyleValue = CoreThemeElement.Alpha                    
    button_text_align                 : ThemeElementStyleValue = CoreThemeElement.ButtonTextAlign          
    cell_padding                      : ThemeElementStyleValue = CoreThemeElement.CellPadding              
    child_border_size                 : ThemeElementStyleValue = CoreThemeElement.ChildBorderSize          
    child_rounding                    : ThemeElementStyleValue = CoreThemeElement.ChildRounding            
    frame_border_size                 : ThemeElementStyleValue = CoreThemeElement.FrameBorderSize          
    frame_padding                     : ThemeElementStyleValue = CoreThemeElement.FramePadding             
    frame_rounding                    : ThemeElementStyleValue = CoreThemeElement.FrameRounding            
    grab_min_size                     : ThemeElementStyleValue = CoreThemeElement.GrabMinSize              
    grab_rounding                     : ThemeElementStyleValue = CoreThemeElement.GrabRounding             
    indent_spacing                    : ThemeElementStyleValue = CoreThemeElement.IndentSpacing            
    item_inner_spacing                : ThemeElementStyleValue = CoreThemeElement.ItemInnerSpacing         
    item_spacing                      : ThemeElementStyleValue = CoreThemeElement.ItemSpacing              
    popup_border_size                 : ThemeElementStyleValue = CoreThemeElement.PopupBorderSize          
    popup_rounding                    : ThemeElementStyleValue = CoreThemeElement.PopupRounding            
    scrollbar_rounding                : ThemeElementStyleValue = CoreThemeElement.ScrollbarRounding        
    scrollbar_size                    : ThemeElementStyleValue = CoreThemeElement.ScrollbarSize            
    selectable_text_align             : ThemeElementStyleValue = CoreThemeElement.SelectableTextAlign      
    tab_rounding                      : ThemeElementStyleValue = CoreThemeElement.TabRounding              
    window_border_size                : ThemeElementStyleValue = CoreThemeElement.WindowBorderSize         
    window_min_size                   : ThemeElementStyleValue = CoreThemeElement.WindowMinSize            
    window_padding                    : ThemeElementStyleValue = CoreThemeElement.WindowPadding            
    window_rounding                   : ThemeElementStyleValue = CoreThemeElement.WindowRounding           
    window_title_align                : ThemeElementStyleValue = CoreThemeElement.WindowTitleAlign  

    node_border_thickness             : ThemeElementStyleValue = NodeThemeElement.NodeBorderThickness      
    node_corner_rounding              : ThemeElementStyleValue = NodeThemeElement.NodeCornerRounding       
    node_grid_spacing                 : ThemeElementStyleValue = NodeThemeElement.GridSpacing              
    node_link_hover_distance          : ThemeElementStyleValue = NodeThemeElement.LinkHoverDistance        
    node_link_line_segments_per_length: ThemeElementStyleValue = NodeThemeElement.LinkLineSegmentsPerLength
    node_link_thickness               : ThemeElementStyleValue = NodeThemeElement.LinkThickness            
    node_padding_horizontal           : ThemeElementStyleValue = NodeThemeElement.NodePaddingHorizontal    
    node_padding_vertical             : ThemeElementStyleValue = NodeThemeElement.NodePaddingVertical      
    node_pin_circle_radius            : ThemeElementStyleValue = NodeThemeElement.PinCircleRadius          
    node_pin_hover_radius             : ThemeElementStyleValue = NodeThemeElement.PinHoverRadius           
    node_pin_line_thickness           : ThemeElementStyleValue = NodeThemeElement.LinkThickness            
    node_pin_offset                   : ThemeElementStyleValue = NodeThemeElement.PinOffset                
    node_pin_quad_side_length         : ThemeElementStyleValue = NodeThemeElement.PinQuadSideLength        
    node_pin_triangle_side_length     : ThemeElementStyleValue = NodeThemeElement.PinTriangleSideLength

    plot_annotation_padding           : ThemeElementStyleValue = PlotThemeElement.AnnotationPadding        
    plot_border_size                  : ThemeElementStyleValue = PlotThemeElement.PlotBorderSize           
    plot_default_size                 : ThemeElementStyleValue = PlotThemeElement.PlotDefaultSize          
    plot_digital_bit_gap              : ThemeElementStyleValue = PlotThemeElement.DigitalBitGap            
    plot_digital_bit_height           : ThemeElementStyleValue = PlotThemeElement.DigitalBitHeight         
    plot_error_bar_size               : ThemeElementStyleValue = PlotThemeElement.ErrorBarSize             
    plot_error_bar_weight             : ThemeElementStyleValue = PlotThemeElement.ErrorBarWeight           
    plot_fill_alpha                   : ThemeElementStyleValue = PlotThemeElement.FillAlpha                
    plot_fit_padding                  : ThemeElementStyleValue = PlotThemeElement.FitPadding               
    plot_label_padding                : ThemeElementStyleValue = PlotThemeElement.LabelPadding             
    plot_legend_inner_padding         : ThemeElementStyleValue = PlotThemeElement.LegendInnerPadding       
    plot_legend_padding               : ThemeElementStyleValue = PlotThemeElement.LegendPadding            
    plot_legend_spacing               : ThemeElementStyleValue = PlotThemeElement.LegendSpacing            
    plot_line_weight                  : ThemeElementStyleValue = PlotThemeElement.LineWeight               
    plot_major_grid_size              : ThemeElementStyleValue = PlotThemeElement.MajorGridSize            
    plot_major_tick_len               : ThemeElementStyleValue = PlotThemeElement.MajorTickLen             
    plot_major_tick_size              : ThemeElementStyleValue = PlotThemeElement.MajorTickSize            
    plot_marker                       : ThemeElementStyleValue = PlotThemeElement.Marker                   
    plot_marker_size                  : ThemeElementStyleValue = PlotThemeElement.MarkerSize               
    plot_marker_weight                : ThemeElementStyleValue = PlotThemeElement.MarkerWeight             
    plot_min_size                     : ThemeElementStyleValue = PlotThemeElement.PlotMinSize              
    plot_minor_alpha                  : ThemeElementStyleValue = PlotThemeElement.MinorAlpha               
    plot_minor_grid_size              : ThemeElementStyleValue = PlotThemeElement.MinorGridSize            
    plot_minor_tick_len               : ThemeElementStyleValue = PlotThemeElement.MinorTickLen             
    plot_minor_tick_size              : ThemeElementStyleValue = PlotThemeElement.MinorTickSize            
    plot_mouse_pos_padding            : ThemeElementStyleValue = PlotThemeElement.MousePosPadding          
    plot_padding                      : ThemeElementStyleValue = PlotThemeElement.PlotPadding  



###################################
############## Font ###############
###################################
class Font:
    """Global font manager and registry system.
    """
    __fonts: dict = {}
    # This is the "default" registry for the entire framework. DearPyPixl does
    # NOT expose font registries like DearPyGui does.

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
        @functools.wraps(method)
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

    def get_font_size(self, size: Numeric = 12.0) -> int:
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
