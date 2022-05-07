from __future__ import annotations
from collections.abc import Mapping
from typing import Callable, Union, Sequence, Any, Optional, TypeAlias
import decimal
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
)
from dearpypixl.components.configuration import item_attribute, ItemAttribute
from dearpypixl.components.item import Item
from dearpypixl.constants import (
    ThemeCategoryCore,
    ThemeCategoryPlot,
    ThemeCategoryNode,
    ItemIndex,
    FontRangeHint,
    _ThemeCategoryT,
    ThemeElementTData,
)


__all__ = [
    "Theme",
    "ThemeComponent",
    "ThemeColorComponent",
    "ThemeStyleComponent",
    "Font",
]


# Type aliases
Numeric               : TypeAlias = int | float
ThemeElementColorValue: TypeAlias = tuple[Numeric, Optional[Numeric], Optional[Numeric], Optional[Numeric]] | None
ThemeElementStyleValue: TypeAlias = tuple[Numeric, Optional[Numeric]] | None
ThemeElement          : TypeAlias = ThemeCategoryCore | ThemeCategoryNode | ThemeCategoryPlot





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
    __is_container__ : bool     = True                                                                                            
    __is_root_item__ : bool     = True                                                                                            
    __is_value_able__: bool     = False                                                                                           
    __able_parents__ : tuple    = ()                                                                                              
    __able_children__: tuple    = ('ThemeComponent',)                                                                             
    __commands__     : tuple    = ('bind_theme',)                                                                                 
    __constants__    : tuple    = ('mvTheme', 'mvThemeCat_Core', 'mvThemeCat_Plots', 'mvThemeCat_Nodes')                          
    __command__      : Callable = add_theme      

    def __init__(
        self,
        label: str = None,
        font: Union[str, Font] = None,
        font_size: float = 12.0, 
    ):
        self.__target_uuids: set[int] = set()
        self.__font: Font = font
        self.__font_uuid: int = 0
        self.__font_size_value: float = font_size

        super().__init__(label=label)

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
            Theme._default_theme_uuid = self_uuid
   
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
        if not item and self._tag == Theme._default_theme_uuid:
            bind_theme(0)
            bind_font(0)
            Theme._default_theme_uuid = 0

    def __update_targets_font(self):
        # font.setter uses this to bind a new font (size) to all bound items.
        font_uuid = self.__font_uuid
        target_uuids = self.__target_uuids
        # Since theme and font are seperate internally we need to rebind
        # all targets to the new font item.
        for item_uuid in target_uuids:
            bind_item_font(item_uuid, font_uuid)

        # If this theme is also the default theme:
        if self._tag == Theme._default_theme_uuid:
            bind_font(font_uuid)

    _default_theme_uuid = 0  # no way to fetch via DPG API
            

class ThemeComponent(Item):
    item_type         : Union[int, ItemIndex]    =  ItemAttribute("configuration", "get_item_cached", None)
    enabled_state     : bool                     =  ItemAttribute("configuration", "get_item_config", "set_item_config")     

    __is_container__ : bool                     =  True                                                                                            
    __is_root_item__ : bool                     =  False                                                                                           
    __is_value_able__: bool                     =  False                                                                                           
    __able_parents__ : tuple                    =  ('Theme',)                                                                                      
    __able_children__: tuple                    =  ('ThemeColor', 'ThemeStyle')                                                                    
    __commands__     : tuple                    =  ()                                                                                              
    __constants__    : tuple                    =  ('mvThemeComponent',)                                                                           
    __command__      : Callable                 =  add_theme_component  

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
            if attr.startswith("_") or not isinstance((enum_member := getattr(cls, attr)), _ThemeCategoryT):
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

        number_of_vals = element_data.components
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
            elif not isinstance(element, _ThemeCategoryT):
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
    border                       : ThemeElementColorValue = ThemeCategoryCore.Border                
    border_shadow                : ThemeElementColorValue = ThemeCategoryCore.BorderShadow          
    button                       : ThemeElementColorValue = ThemeCategoryCore.Button                
    button_active                : ThemeElementColorValue = ThemeCategoryCore.ButtonActive          
    button_hovered               : ThemeElementColorValue = ThemeCategoryCore.ButtonHovered         
    check_mark                   : ThemeElementColorValue = ThemeCategoryCore.CheckMark             
    child_bg                     : ThemeElementColorValue = ThemeCategoryCore.ChildBg               
    docking_empty_bg             : ThemeElementColorValue = ThemeCategoryCore.DockingEmptyBg        
    docking_preview              : ThemeElementColorValue = ThemeCategoryCore.DockingPreview        
    drag_drop_target             : ThemeElementColorValue = ThemeCategoryCore.DragDropTarget        
    frame_bg                     : ThemeElementColorValue = ThemeCategoryCore.FrameBg               
    frame_bg_active              : ThemeElementColorValue = ThemeCategoryCore.FrameBgActive         
    frame_bg_hovered             : ThemeElementColorValue = ThemeCategoryCore.FrameBgHovered        
    header                       : ThemeElementColorValue = ThemeCategoryCore.Header                
    header_active                : ThemeElementColorValue = ThemeCategoryCore.HeaderActive          
    header_hovered               : ThemeElementColorValue = ThemeCategoryCore.HeaderHovered         
    menu_bar_bg                  : ThemeElementColorValue = ThemeCategoryCore.MenuBarBg             
    modal_window_dim_bg          : ThemeElementColorValue = ThemeCategoryCore.ModalWindowDimBg      
    nav_highlight                : ThemeElementColorValue = ThemeCategoryCore.NavHighlight          
    nav_windowing_dim_bg         : ThemeElementColorValue = ThemeCategoryCore.NavWindowingDimBg     
    nav_windowing_highlight      : ThemeElementColorValue = ThemeCategoryCore.NavWindowingHighlight 
    plot_histogram               : ThemeElementColorValue = ThemeCategoryCore.PlotHistogram         
    plot_histogram_hovered       : ThemeElementColorValue = ThemeCategoryCore.PlotHistogramHovered  
    plot_lines                   : ThemeElementColorValue = ThemeCategoryCore.PlotLines             
    plot_lines_hovered           : ThemeElementColorValue = ThemeCategoryCore.PlotLinesHovered      
    popup_bg                     : ThemeElementColorValue = ThemeCategoryCore.PopupBg               
    resize_grip                  : ThemeElementColorValue = ThemeCategoryCore.ResizeGrip            
    resize_grip_active           : ThemeElementColorValue = ThemeCategoryCore.ResizeGripActive      
    resize_grip_hovered          : ThemeElementColorValue = ThemeCategoryCore.ResizeGripHovered     
    scrollbar_bg                 : ThemeElementColorValue = ThemeCategoryCore.ScrollbarBg           
    scrollbar_grab               : ThemeElementColorValue = ThemeCategoryCore.ScrollbarGrab         
    scrollbar_grab_active        : ThemeElementColorValue = ThemeCategoryCore.ScrollbarGrabActive   
    scrollbar_grab_hovered       : ThemeElementColorValue = ThemeCategoryCore.ScrollbarGrabHovered  
    separator                    : ThemeElementColorValue = ThemeCategoryCore.Separator             
    separator_active             : ThemeElementColorValue = ThemeCategoryCore.SeparatorActive       
    separator_hovered            : ThemeElementColorValue = ThemeCategoryCore.SeparatorHovered      
    slider_grab                  : ThemeElementColorValue = ThemeCategoryCore.SliderGrab            
    slider_grab_active           : ThemeElementColorValue = ThemeCategoryCore.SliderGrabActive      
    tab                          : ThemeElementColorValue = ThemeCategoryCore.Tab                   
    tab_active                   : ThemeElementColorValue = ThemeCategoryCore.TabActive             
    tab_hovered                  : ThemeElementColorValue = ThemeCategoryCore.TabHovered            
    tab_unfocused                : ThemeElementColorValue = ThemeCategoryCore.TabUnfocused          
    tab_unfocused_active         : ThemeElementColorValue = ThemeCategoryCore.TabUnfocusedActive    
    table_border_light           : ThemeElementColorValue = ThemeCategoryCore.TableBorderLight      
    table_border_strong          : ThemeElementColorValue = ThemeCategoryCore.TableBorderStrong     
    table_header_bg              : ThemeElementColorValue = ThemeCategoryCore.TableHeaderBg         
    table_row_bg                 : ThemeElementColorValue = ThemeCategoryCore.TableRowBg            
    table_row_bg_alt             : ThemeElementColorValue = ThemeCategoryCore.TableRowBgAlt         
    text                         : ThemeElementColorValue = ThemeCategoryCore.Text                  
    text_disabled                : ThemeElementColorValue = ThemeCategoryCore.TextDisabled          
    text_selected_bg             : ThemeElementColorValue = ThemeCategoryCore.TextSelectedBg        
    title_bg                     : ThemeElementColorValue = ThemeCategoryCore.TitleBg               
    title_bg_active              : ThemeElementColorValue = ThemeCategoryCore.TitleBgActive         
    title_bg_collapsed           : ThemeElementColorValue = ThemeCategoryCore.TitleBgCollapsed      
    window_bg                    : ThemeElementColorValue = ThemeCategoryCore.WindowBg           

    node_bg                      : ThemeElementColorValue = ThemeCategoryNode.NodeBackground        
    node_bg_hovered              : ThemeElementColorValue = ThemeCategoryNode.NodeBackgroundHovered 
    node_bg_selected             : ThemeElementColorValue = ThemeCategoryNode.NodeBackgroundSelected
    node_box_selector            : ThemeElementColorValue = ThemeCategoryNode.BoxSelector           
    node_box_selector_outline    : ThemeElementColorValue = ThemeCategoryNode.BoxSelectorOutline    
    node_grid_bg                 : ThemeElementColorValue = ThemeCategoryNode.GridBackground        
    node_grid_line               : ThemeElementColorValue = ThemeCategoryNode.GridLine   
    node_grid_line_primary       : ThemeElementColorValue = ThemeCategoryNode.GridLinePrimary        
    node_link                    : ThemeElementColorValue = ThemeCategoryNode.Link                  
    node_link_hovered            : ThemeElementColorValue = ThemeCategoryNode.LinkHovered           
    node_link_selected           : ThemeElementColorValue = ThemeCategoryNode.LinkSelected          
    node_outline                 : ThemeElementColorValue = ThemeCategoryNode.NodeOutline 
    node_minimap_bg              : ThemeElementColorValue = ThemeCategoryNode.MiniMapBackground
    node_minimap_bg_hovered      : ThemeElementColorValue = ThemeCategoryNode.MiniMapBackgroundHovered
    node_minimap_outline         : ThemeElementColorValue = ThemeCategoryNode.MiniMapOutline
    node_minimap_outline_hovered : ThemeElementColorValue = ThemeCategoryNode.MiniMapOutlineHovered
    node_minimap_node_bg         : ThemeElementColorValue = ThemeCategoryNode.MiniMapNodeBackground
    node_minimap_node_bg_hovered : ThemeElementColorValue = ThemeCategoryNode.MiniMapNodeBackgroundHovered
    node_minimap_node_bg_selected: ThemeElementColorValue = ThemeCategoryNode.MiniMapNodeBackgroundSelected
    node_minimap_node_outline    : ThemeElementColorValue = ThemeCategoryNode.MiniMapNodeOutline
    node_minimap_link            : ThemeElementColorValue = ThemeCategoryNode.MiniMapLink
    node_minimap_link_selected   : ThemeElementColorValue = ThemeCategoryNode.MiniMapLinkSelected
    node_minimap_canvas          : ThemeElementColorValue = ThemeCategoryNode.MiniMapCanvas
    node_minimap_canvas_outline  : ThemeElementColorValue = ThemeCategoryNode.MiniMapCanvasOutline
    node_pin                     : ThemeElementColorValue = ThemeCategoryNode.Pin                   
    node_pin_hovered             : ThemeElementColorValue = ThemeCategoryNode.PinHovered            
    node_title_bar               : ThemeElementColorValue = ThemeCategoryNode.TitleBar              
    node_title_bar_hovered       : ThemeElementColorValue = ThemeCategoryNode.TitleBarHovered       
    node_title_bar_selected      : ThemeElementColorValue = ThemeCategoryNode.TitleBarSelected      
    
    plot_bg                      : ThemeElementColorValue = ThemeCategoryPlot.PlotBg                
    plot_border                  : ThemeElementColorValue = ThemeCategoryPlot.PlotBorder            
    plot_crosshairs              : ThemeElementColorValue = ThemeCategoryPlot.Crosshairs            
    plot_error_bar               : ThemeElementColorValue = ThemeCategoryPlot.ErrorBar              
    plot_fill                    : ThemeElementColorValue = ThemeCategoryPlot.Fill                  
    plot_frame_bg                : ThemeElementColorValue = ThemeCategoryPlot.FrameBg               
    plot_inlay_text              : ThemeElementColorValue = ThemeCategoryPlot.InlayText             
    plot_legend_bg               : ThemeElementColorValue = ThemeCategoryPlot.LegendBg              
    plot_legend_border           : ThemeElementColorValue = ThemeCategoryPlot.LegendBorder          
    plot_legend_text             : ThemeElementColorValue = ThemeCategoryPlot.LegendText            
    plot_line                    : ThemeElementColorValue = ThemeCategoryPlot.Line                  
    plot_marker_fill             : ThemeElementColorValue = ThemeCategoryPlot.MarkerFill            
    plot_marker_outline          : ThemeElementColorValue = ThemeCategoryPlot.MarkerOutline         
    plot_query                   : ThemeElementColorValue = ThemeCategoryPlot.Query                 
    plot_selection               : ThemeElementColorValue = ThemeCategoryPlot.Selection             
    plot_title_text              : ThemeElementColorValue = ThemeCategoryPlot.TitleText             
    plot_x_axis                  : ThemeElementColorValue = ThemeCategoryPlot.XAxis                 
    plot_x_axis_grid             : ThemeElementColorValue = ThemeCategoryPlot.XAxisGrid             
    plot_y_axis                  : ThemeElementColorValue = ThemeCategoryPlot.YAxis                 
    plot_y_axis2                 : ThemeElementColorValue = ThemeCategoryPlot.YAxis2                
    plot_y_axis3                 : ThemeElementColorValue = ThemeCategoryPlot.YAxis3                
    plot_y_axis_grid             : ThemeElementColorValue = ThemeCategoryPlot.YAxisGrid             
    plot_y_axis_grid2            : ThemeElementColorValue = ThemeCategoryPlot.YAxisGrid2            
    plot_y_axis_grid3            : ThemeElementColorValue = ThemeCategoryPlot.YAxisGrid3 


class ThemeStyleComponent(ThemeComponent):
    """A theme component with pre-bound elements that affect
    styling for all theme categories.
    """
    alpha                             : ThemeElementStyleValue = ThemeCategoryCore.Alpha                    
    button_text_align                 : ThemeElementStyleValue = ThemeCategoryCore.ButtonTextAlign          
    cell_padding                      : ThemeElementStyleValue = ThemeCategoryCore.CellPadding              
    child_border_size                 : ThemeElementStyleValue = ThemeCategoryCore.ChildBorderSize          
    child_rounding                    : ThemeElementStyleValue = ThemeCategoryCore.ChildRounding            
    frame_border_size                 : ThemeElementStyleValue = ThemeCategoryCore.FrameBorderSize          
    frame_padding                     : ThemeElementStyleValue = ThemeCategoryCore.FramePadding             
    frame_rounding                    : ThemeElementStyleValue = ThemeCategoryCore.FrameRounding            
    grab_min_size                     : ThemeElementStyleValue = ThemeCategoryCore.GrabMinSize              
    grab_rounding                     : ThemeElementStyleValue = ThemeCategoryCore.GrabRounding             
    indent_spacing                    : ThemeElementStyleValue = ThemeCategoryCore.IndentSpacing            
    item_inner_spacing                : ThemeElementStyleValue = ThemeCategoryCore.ItemInnerSpacing         
    item_spacing                      : ThemeElementStyleValue = ThemeCategoryCore.ItemSpacing              
    popup_border_size                 : ThemeElementStyleValue = ThemeCategoryCore.PopupBorderSize          
    popup_rounding                    : ThemeElementStyleValue = ThemeCategoryCore.PopupRounding            
    scrollbar_rounding                : ThemeElementStyleValue = ThemeCategoryCore.ScrollbarRounding        
    scrollbar_size                    : ThemeElementStyleValue = ThemeCategoryCore.ScrollbarSize            
    selectable_text_align             : ThemeElementStyleValue = ThemeCategoryCore.SelectableTextAlign      
    tab_rounding                      : ThemeElementStyleValue = ThemeCategoryCore.TabRounding              
    window_border_size                : ThemeElementStyleValue = ThemeCategoryCore.WindowBorderSize         
    window_min_size                   : ThemeElementStyleValue = ThemeCategoryCore.WindowMinSize            
    window_padding                    : ThemeElementStyleValue = ThemeCategoryCore.WindowPadding            
    window_rounding                   : ThemeElementStyleValue = ThemeCategoryCore.WindowRounding           
    window_title_align                : ThemeElementStyleValue = ThemeCategoryCore.WindowTitleAlign  

    node_border_thickness             : ThemeElementStyleValue = ThemeCategoryNode.NodeBorderThickness      
    node_corner_rounding              : ThemeElementStyleValue = ThemeCategoryNode.NodeCornerRounding       
    node_grid_spacing                 : ThemeElementStyleValue = ThemeCategoryNode.GridSpacing              
    node_link_hover_distance          : ThemeElementStyleValue = ThemeCategoryNode.LinkHoverDistance        
    node_link_line_segments_per_length: ThemeElementStyleValue = ThemeCategoryNode.LinkLineSegmentsPerLength
    node_link_thickness               : ThemeElementStyleValue = ThemeCategoryNode.LinkThickness            
    node_padding                      : ThemeElementStyleValue = ThemeCategoryNode.NodePadding   
    node_minimap_padding              : ThemeElementStyleValue = ThemeCategoryNode.MiniMapPadding
    node_minimap_offset               : ThemeElementStyleValue = ThemeCategoryNode.MiniMapOffset
    node_pin_circle_radius            : ThemeElementStyleValue = ThemeCategoryNode.PinCircleRadius          
    node_pin_hover_radius             : ThemeElementStyleValue = ThemeCategoryNode.PinHoverRadius           
    node_pin_line_thickness           : ThemeElementStyleValue = ThemeCategoryNode.LinkThickness            
    node_pin_offset                   : ThemeElementStyleValue = ThemeCategoryNode.PinOffset                
    node_pin_quad_side_length         : ThemeElementStyleValue = ThemeCategoryNode.PinQuadSideLength        
    node_pin_triangle_side_length     : ThemeElementStyleValue = ThemeCategoryNode.PinTriangleSideLength

    plot_annotation_padding           : ThemeElementStyleValue = ThemeCategoryPlot.AnnotationPadding        
    plot_border_size                  : ThemeElementStyleValue = ThemeCategoryPlot.PlotBorderSize           
    plot_default_size                 : ThemeElementStyleValue = ThemeCategoryPlot.PlotDefaultSize          
    plot_digital_bit_gap              : ThemeElementStyleValue = ThemeCategoryPlot.DigitalBitGap            
    plot_digital_bit_height           : ThemeElementStyleValue = ThemeCategoryPlot.DigitalBitHeight         
    plot_error_bar_size               : ThemeElementStyleValue = ThemeCategoryPlot.ErrorBarSize             
    plot_error_bar_weight             : ThemeElementStyleValue = ThemeCategoryPlot.ErrorBarWeight           
    plot_fill_alpha                   : ThemeElementStyleValue = ThemeCategoryPlot.FillAlpha                
    plot_fit_padding                  : ThemeElementStyleValue = ThemeCategoryPlot.FitPadding               
    plot_label_padding                : ThemeElementStyleValue = ThemeCategoryPlot.LabelPadding             
    plot_legend_inner_padding         : ThemeElementStyleValue = ThemeCategoryPlot.LegendInnerPadding       
    plot_legend_padding               : ThemeElementStyleValue = ThemeCategoryPlot.LegendPadding            
    plot_legend_spacing               : ThemeElementStyleValue = ThemeCategoryPlot.LegendSpacing            
    plot_line_weight                  : ThemeElementStyleValue = ThemeCategoryPlot.LineWeight               
    plot_major_grid_size              : ThemeElementStyleValue = ThemeCategoryPlot.MajorGridSize            
    plot_major_tick_len               : ThemeElementStyleValue = ThemeCategoryPlot.MajorTickLen             
    plot_major_tick_size              : ThemeElementStyleValue = ThemeCategoryPlot.MajorTickSize            
    plot_marker                       : ThemeElementStyleValue = ThemeCategoryPlot.Marker                   
    plot_marker_size                  : ThemeElementStyleValue = ThemeCategoryPlot.MarkerSize               
    plot_marker_weight                : ThemeElementStyleValue = ThemeCategoryPlot.MarkerWeight             
    plot_min_size                     : ThemeElementStyleValue = ThemeCategoryPlot.PlotMinSize              
    plot_minor_alpha                  : ThemeElementStyleValue = ThemeCategoryPlot.MinorAlpha               
    plot_minor_grid_size              : ThemeElementStyleValue = ThemeCategoryPlot.MinorGridSize            
    plot_minor_tick_len               : ThemeElementStyleValue = ThemeCategoryPlot.MinorTickLen             
    plot_minor_tick_size              : ThemeElementStyleValue = ThemeCategoryPlot.MinorTickSize            
    plot_mouse_pos_padding            : ThemeElementStyleValue = ThemeCategoryPlot.MousePosPadding          
    plot_padding                      : ThemeElementStyleValue = ThemeCategoryPlot.PlotPadding  



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

