from typing import Callable, Any
from dearpygui import dearpygui
from ..item import Item, ItemProperty, ItemIdType, CONFIG


__all__ = [
    "Theme",
    "ThemeComponent",
    "ThemeColor",
    "ThemeStyle",
]


class Theme(Item):
    """Adds a theme.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * default_theme (bool, optional): (deprecated)
    """
    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTheme, "mvTheme")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = True
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = (dearpygui.mvThemeComponent,)
    __commands__      : tuple      = ('bind_theme',)
    __constants__     : tuple      = ('mvTheme', 'mvThemeCat_Core', 'mvThemeCat_Plots', 'mvThemeCat_Nodes')
    __command__       : Callable   = dearpygui.add_theme

    def __init__(
        self,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class ThemeComponent(Item):
    """Adds a theme component.

        Args:
            * item_type (int, optional):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * enabled_state (bool, optional):
    """
    enabled_state     : bool       = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvThemeComponent, "mvThemeComponent")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvTheme,)
    __able_children__ : tuple      = (dearpygui.mvThemeColor, dearpygui.mvThemeStyle)
    __command__       : Callable   = dearpygui.add_theme_component

    def __init__(
        self,
        item_type          : int       = 0,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        parent             : int | str = 0,
        before             : int | str = 0,
        enabled_state      : bool      = True,
        **kwargs
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


class ThemeColor(Item):
    """Adds a theme color.

        Args:
            * target (int, optional):
            * value (list[int] | tuple[int, ...], optional):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    """
    target           : int                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value            : list[int] | tuple[int] = ItemProperty(CONFIG, 'get_item_value', 'set_item_value', 'default_value')
    category         : int                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvThemeColor, "mvThemeColor")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = True
    __able_parents__ : tuple      = (dearpygui.mvThemeComponent, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __constants__    : tuple      = ('mvThemeColor', 'mvThemeCol_Text', 'mvThemeCol_TextDisabled', 'mvThemeCol_WindowBg', 'mvThemeCol_ChildBg', 'mvThemeCol_Border', 'mvThemeCol_PopupBg', 'mvThemeCol_BorderShadow', 'mvThemeCol_FrameBg', 'mvThemeCol_FrameBgHovered', 'mvThemeCol_FrameBgActive', 'mvThemeCol_TitleBg', 'mvThemeCol_TitleBgActive', 'mvThemeCol_TitleBgCollapsed', 'mvThemeCol_MenuBarBg', 'mvThemeCol_ScrollbarBg', 'mvThemeCol_ScrollbarGrab', 'mvThemeCol_ScrollbarGrabHovered', 'mvThemeCol_ScrollbarGrabActive', 'mvThemeCol_CheckMark', 'mvThemeCol_SliderGrab', 'mvThemeCol_SliderGrabActive', 'mvThemeCol_Button', 'mvThemeCol_ButtonHovered', 'mvThemeCol_ButtonActive', 'mvThemeCol_Header', 'mvThemeCol_HeaderHovered', 'mvThemeCol_HeaderActive', 'mvThemeCol_Separator', 'mvThemeCol_SeparatorHovered', 'mvThemeCol_SeparatorActive', 'mvThemeCol_ResizeGrip', 'mvThemeCol_ResizeGripHovered', 'mvThemeCol_ResizeGripActive', 'mvThemeCol_Tab', 'mvThemeCol_TabHovered', 'mvThemeCol_TabActive', 'mvThemeCol_TabUnfocused', 'mvThemeCol_TabUnfocusedActive', 'mvThemeCol_DockingPreview', 'mvThemeCol_DockingEmptyBg', 'mvThemeCol_PlotLines', 'mvThemeCol_PlotLinesHovered', 'mvThemeCol_PlotHistogram', 'mvThemeCol_PlotHistogramHovered', 'mvThemeCol_TableHeaderBg', 'mvThemeCol_TableBorderStrong', 'mvThemeCol_TableBorderLight', 'mvThemeCol_TableRowBg', 'mvThemeCol_TableRowBgAlt', 'mvThemeCol_TextSelectedBg', 'mvThemeCol_DragDropTarget', 'mvThemeCol_NavHighlight', 'mvThemeCol_NavWindowingHighlight', 'mvThemeCol_NavWindowingDimBg', 'mvThemeCol_ModalWindowDimBg', 'mvPlotCol_Line', 'mvPlotCol_Fill', 'mvPlotCol_MarkerOutline', 'mvPlotCol_MarkerFill', 'mvPlotCol_ErrorBar', 'mvPlotCol_FrameBg', 'mvPlotCol_PlotBg', 'mvPlotCol_PlotBorder', 'mvPlotCol_LegendBg', 'mvPlotCol_LegendBorder', 'mvPlotCol_LegendText', 'mvPlotCol_TitleText', 'mvPlotCol_InlayText', 'mvPlotCol_XAxis', 'mvPlotCol_XAxisGrid', 'mvPlotCol_YAxis', 'mvPlotCol_YAxisGrid', 'mvPlotCol_YAxis2', 'mvPlotCol_YAxisGrid2', 'mvPlotCol_YAxis3', 'mvPlotCol_YAxisGrid3', 'mvPlotCol_Selection', 'mvPlotCol_Query', 'mvPlotCol_Crosshairs', 'mvNodeCol_NodeBackground', 'mvNodeCol_NodeBackgroundHovered', 'mvNodeCol_NodeBackgroundSelected', 'mvNodeCol_NodeOutline', 'mvNodeCol_TitleBar', 'mvNodeCol_TitleBarHovered', 'mvNodeCol_TitleBarSelected', 'mvNodeCol_Link', 'mvNodeCol_LinkHovered', 'mvNodeCol_LinkSelected', 'mvNodeCol_Pin', 'mvNodeCol_PinHovered', 'mvNodeCol_BoxSelector', 'mvNodeCol_BoxSelectorOutline', 'mvNodeCol_GridBackground', 'mvNodeCol_GridLine')
    __command__      : Callable   = dearpygui.add_theme_color

    def __init__(
        self,
        target             : int                         = 0,
        value              : list[int] | tuple[int, ...] = (0, 0, 0, 255),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        parent             : int | str                   = 0,
        category           : int                         = 0,
        **kwargs
    ) -> None:
        super().__init__(
            target=target,
            value=value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            category=category,
            **kwargs,
        )


class ThemeStyle(Item):
    """Adds a theme style.

        Args:
            * target (int, optional):
            * x (float, optional):
            * y (float, optional):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    """
    target  : int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    x       : float = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    y       : float = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    category: int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvThemeStyle, "mvThemeStyle")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = True
    __able_parents__ : tuple      = (dearpygui.mvThemeComponent, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __constants__    : tuple      = ('mvThemeStyle', 'mvStyleVar_Alpha', 'mvStyleVar_WindowPadding', 'mvStyleVar_WindowRounding', 'mvStyleVar_WindowBorderSize', 'mvStyleVar_WindowMinSize', 'mvStyleVar_WindowTitleAlign', 'mvStyleVar_ChildRounding', 'mvStyleVar_ChildBorderSize', 'mvStyleVar_PopupRounding', 'mvStyleVar_PopupBorderSize', 'mvStyleVar_FramePadding', 'mvStyleVar_FrameRounding', 'mvStyleVar_FrameBorderSize', 'mvStyleVar_ItemSpacing', 'mvStyleVar_ItemInnerSpacing', 'mvStyleVar_IndentSpacing', 'mvStyleVar_CellPadding', 'mvStyleVar_ScrollbarSize', 'mvStyleVar_ScrollbarRounding', 'mvStyleVar_GrabMinSize', 'mvStyleVar_GrabRounding', 'mvStyleVar_TabRounding', 'mvStyleVar_ButtonTextAlign', 'mvStyleVar_SelectableTextAlign', 'mvPlotStyleVar_LineWeight', 'mvPlotStyleVar_Marker', 'mvPlotStyleVar_MarkerSize', 'mvPlotStyleVar_MarkerWeight', 'mvPlotStyleVar_FillAlpha', 'mvPlotStyleVar_ErrorBarSize', 'mvPlotStyleVar_ErrorBarWeight', 'mvPlotStyleVar_DigitalBitHeight', 'mvPlotStyleVar_DigitalBitGap', 'mvPlotStyleVar_PlotBorderSize', 'mvPlotStyleVar_MinorAlpha', 'mvPlotStyleVar_MajorTickLen', 'mvPlotStyleVar_MinorTickLen', 'mvPlotStyleVar_MajorTickSize', 'mvPlotStyleVar_MinorTickSize', 'mvPlotStyleVar_MajorGridSize', 'mvPlotStyleVar_MinorGridSize', 'mvPlotStyleVar_PlotPadding', 'mvPlotStyleVar_LabelPadding', 'mvPlotStyleVar_LegendPadding', 'mvPlotStyleVar_LegendInnerPadding', 'mvPlotStyleVar_LegendSpacing', 'mvPlotStyleVar_MousePosPadding', 'mvPlotStyleVar_AnnotationPadding', 'mvPlotStyleVar_FitPadding', 'mvPlotStyleVar_PlotDefaultSize', 'mvPlotStyleVar_PlotMinSize', 'mvNodeStyleVar_GridSpacing', 'mvNodeStyleVar_NodeCornerRounding', 'mvNodeStyleVar_NodePaddingHorizontal', 'mvNodeStyleVar_NodePaddingVertical', 'mvNodeStyleVar_NodeBorderThickness', 'mvNodeStyleVar_LinkThickness', 'mvNodeStyleVar_LinkLineSegmentsPerLength', 'mvNodeStyleVar_LinkHoverDistance', 'mvNodeStyleVar_PinCircleRadius', 'mvNodeStyleVar_PinQuadSideLength', 'mvNodeStyleVar_PinTriangleSideLength', 'mvNodeStyleVar_PinLineThickness', 'mvNodeStyleVar_PinHoverRadius', 'mvNodeStyleVar_PinOffset')
    __command__      : Callable   = dearpygui.add_theme_style

    def __init__(
        self,
        target            : int             = 0   ,
        x                 : float           = 1.0 ,
        y                 : float           = -1.0,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str = 0   ,
        category          : int             = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            target=target,
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            category=category,
            **kwargs,
        )
