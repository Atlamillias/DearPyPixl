"""Base interface implementations for DearPyGui items."""

from dearpygui import dearpygui
from .px_typing import (
    ItemId,
    Array,
    DPGCallback,
    Callable,
    Sequence,
    Any,
    typing_overload
)
from .px_items import (
    AppItemType,
    CallableItem,
    ContainerItem,
    HandlerItem,
    PositionedItem,
    RegistryItem,
    RootItem,
    SizedItem,
    ValueAbleItem,
    ValueArrayItem,
    WindowItem
)


__all__ = [
    'mv2dHistogramSeries',
    'mvActivatedHandler',
    'mvActiveHandler',
    'mvAnnotation',
    'mvAreaSeries',
    'mvBarSeries',
    'mvBoolValue',
    'mvButton',
    'mvCandleSeries',
    'mvCharRemap',
    'mvCheckbox',
    'mvChildWindow',
    'mvClickedHandler',
    'mvClipper',
    'mvCollapsingHeader',
    'mvColorButton',
    'mvColorEdit',
    'mvColorMap',
    'mvColorMapButton',
    'mvColorMapRegistry',
    'mvColorMapScale',
    'mvColorMapSlider',
    'mvColorPicker',
    'mvColorValue',
    'mvCombo',
    'mvCustomSeries',
    'mvDatePicker',
    'mvDeactivatedAfterEditHandler',
    'mvDeactivatedHandler',
    'mvDouble4Value',
    'mvDoubleClickedHandler',
    'mvDoubleValue',
    'mvDragDouble',
    'mvDragDoubleMulti',
    'mvDragFloat',
    'mvDragFloatMulti',
    'mvDragInt',
    'mvDragIntMulti',
    'mvDragLine',
    'mvDragPayload',
    'mvDragPoint',
    'mvDrawArrow',
    'mvDrawBezierCubic',
    'mvDrawBezierQuadratic',
    'mvDrawCircle',
    'mvDrawEllipse',
    'mvDrawImage',
    'mvDrawImageQuad',
    'mvDrawLayer',
    'mvDrawLine',
    'mvDrawNode',
    'mvDrawPolygon',
    'mvDrawPolyline',
    'mvDrawQuad',
    'mvDrawRect',
    'mvDrawText',
    'mvDrawTriangle',
    'mvDrawlist',
    'mvDynamicTexture',
    'mvEditedHandler',
    'mvErrorSeries',
    'mvFileDialog',
    'mvFileExtension',
    'mvFilterSet',
    'mvFloat4Value',
    'mvFloatValue',
    'mvFloatVectValue',
    'mvFocusHandler',
    'mvFont',
    'mvFontChars',
    'mvFontRange',
    'mvFontRangeHint',
    'mvFontRegistry',
    'mvGroup',
    'mvHLineSeries',
    'mvHandlerRegistry',
    'mvHeatSeries',
    'mvHistogramSeries',
    'mvHoverHandler',
    'mvImage',
    'mvImageButton',
    'mvImageSeries',
    'mvInputDouble',
    'mvInputDoubleMulti',
    'mvInputFloat',
    'mvInputFloatMulti',
    'mvInputInt',
    'mvInputIntMulti',
    'mvInputText',
    'mvInt4Value',
    'mvIntValue',
    'mvItemHandlerRegistry',
    'mvKeyDownHandler',
    'mvKeyPressHandler',
    'mvKeyReleaseHandler',
    'mvKnobFloat',
    'mvLabelSeries',
    'mvLineSeries',
    'mvListbox',
    'mvLoadingIndicator',
    'mvMenu',
    'mvMenuBar',
    'mvMenuItem',
    'mvMouseClickHandler',
    'mvMouseDoubleClickHandler',
    'mvMouseDownHandler',
    'mvMouseDragHandler',
    'mvMouseMoveHandler',
    'mvMouseReleaseHandler',
    'mvMouseWheelHandler',
    'mvNode',
    'mvNodeAttribute',
    'mvNodeEditor',
    'mvNodeLink',
    'mvPieSeries',
    'mvPlot',
    'mvPlotAxis',
    'mvPlotLegend',
    'mvProgressBar',
    'mvRadioButton',
    'mvRawTexture',
    'mvResizeHandler',
    'mvScatterSeries',
    'mvSelectable',
    'mvSeparator',
    'mvSeriesValue',
    'mvShadeSeries',
    'mvSimplePlot',
    'mvSlider3D',
    'mvSliderDouble',
    'mvSliderDoubleMulti',
    'mvSliderFloat',
    'mvSliderFloatMulti',
    'mvSliderInt',
    'mvSliderIntMulti',
    'mvSpacer',
    'mvStage',
    'mvStairSeries',
    'mvStaticTexture',
    'mvStemSeries',
    'mvStringValue',
    'mvSubPlots',
    'mvTab',
    'mvTabBar',
    'mvTabButton',
    'mvTable',
    'mvTableCell',
    'mvTableColumn',
    'mvTableRow',
    'mvTemplateRegistry',
    'mvText',
    'mvTextureRegistry',
    'mvTheme',
    'mvThemeColor',
    'mvThemeComponent',
    'mvThemeStyle',
    'mvTimePicker',
    'mvToggledOpenHandler',
    'mvTooltip',
    'mvTreeNode',
    'mvVLineSeries',
    'mvValueRegistry',
    'mvViewportDrawlist',
    'mvViewportMenuBar',
    'mvVisibleHandler',
    'mvWindowAppItem'
]




class mv2dHistogramSeries(ValueArrayItem, AppItemType):
    """Adds a 2d histogram series.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * xbins (int, optional):

        * ybins (int, optional):

        * xmin_range (float, optional):

        * xmax_range (float, optional):

        * ymin_range (float, optional):

        * ymax_range (float, optional):

        * density (bool, optional):

        * outliers (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_2d_histogram_series
    identity = dearpygui.mv2dHistogramSeries, 'mvAppItemType::mv2dHistogramSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    xbins             : int
    ybins             : int
    xmin_range        : float
    xmax_range        : float
    ymin_range        : float
    ymax_range        : float
    density           : bool
    outliers          : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., xbins: int = ..., ybins: int = ..., xmin_range: float = ..., xmax_range: float = ..., ymin_range: float = ..., ymax_range: float = ..., density: bool = ..., outliers: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., xbins: int = ..., ybins: int = ..., xmin_range: float = ..., xmax_range: float = ..., ymin_range: float = ..., ymax_range: float = ..., density: bool = ..., outliers: bool = ..., **kwargs) -> None: ...


class mvActivatedHandler(HandlerItem, AppItemType):
    """Adds a activated handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_activated_handler
    identity = dearpygui.mvActivatedHandler, 'mvAppItemType::mvActivatedHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvActiveHandler(HandlerItem, AppItemType):
    """Adds a active handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_active_handler
    identity = dearpygui.mvActiveHandler, 'mvAppItemType::mvActiveHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvAnnotation(ValueAbleItem, AppItemType):
    """Adds an annotation to a plot.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * default_value (Any, optional):

        * offset (Sequence[float], optional):

        * color (Sequence[int], optional):

        * clamped (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_plot_annotation
    identity = dearpygui.mvAnnotation, 'mvAppItemType::mvAnnotation'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    offset            : Sequence[float]
    color             : Array[int, int, int, int | None]
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., default_value: Any = ..., offset: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., offset: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvAreaSeries(ValueArrayItem, AppItemType):
    """Adds an area series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * fill (Sequence[int], optional):

        * contribute_to_bounds (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_area_series
    identity = dearpygui.mvAreaSeries, 'mvAppItemType::mvAreaSeries'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    before              : ItemId
    source              : ItemId
    show                : bool
    fill                : Array[int, int, int, int | None]
    contribute_to_bounds: bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., fill: Array[int, int, int, int | None] = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., fill: Array[int, int, int, int | None] = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...


class mvBarSeries(ValueArrayItem, AppItemType):
    """Adds a bar series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * weight (float, optional):

        * horizontal (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_bar_series
    identity = dearpygui.mvBarSeries, 'mvAppItemType::mvBarSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    weight            : float
    horizontal        : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., weight: float = ..., horizontal: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., weight: float = ..., horizontal: bool = ..., **kwargs) -> None: ...


class mvBoolValue(ValueAbleItem, AppItemType):
    """Adds a bool value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (bool, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_bool_value
    identity = dearpygui.mvBoolValue, 'mvAppItemType::mvBoolValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvButton(SizedItem, CallableItem, AppItemType):
    """Adds a button.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * small (bool, optional): Shrinks the size of the button to the text of the label
        it contains. Useful for embedding in text.

        * arrow (bool, optional): Displays an arrow in place of the text string. This
        requires the direction keyword.

        * direction (int, optional): Sets the cardinal direction for the arrow by using
        constants mvDir_Left, mvDir_Up, mvDir_Down, mvDir_Right, mvDir_None. Arrow keyword
        must be set to True.

    Returns:
        *Self*
    """
    command  = dearpygui.add_button
    identity = dearpygui.mvButton, 'mvAppItemType::mvButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    small             : bool
    arrow             : bool
    direction         : int
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., small: bool = ..., arrow: bool = ..., direction: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., small: bool = ..., arrow: bool = ..., direction: int = ..., **kwargs) -> None: ...


class mvCandleSeries(ValueArrayItem, AppItemType):
    """Adds a candle series to a plot.

    Args:
        * dates (Any):

        * opens (Any):

        * closes (Any):

        * lows (Any):

        * highs (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * bull_color (Sequence[int], optional):

        * bear_color (Sequence[int], optional):

        * weight (float, optional):

        * tooltip (bool, optional):

        * time_unit (int, optional): mvTimeUnit_* constants. Default mvTimeUnit_Day.

    Returns:
        *Self*
    """
    command  = dearpygui.add_candle_series
    identity = dearpygui.mvCandleSeries, 'mvAppItemType::mvCandleSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    bull_color        : Array[int, int, int, int | None]
    bear_color        : Array[int, int, int, int | None]
    weight            : float
    tooltip           : bool
    time_unit         : int
    
    @typing_overload
    def __init__(self, dates: Sequence[float] = ..., opens: Sequence[float] = ..., closes: Sequence[float] = ..., lows: Sequence[float] = ..., highs: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., bull_color: Array[int, int, int, int | None] = ..., bear_color: Array[int, int, int, int | None] = ..., weight: float = ..., tooltip: bool = ..., time_unit: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., bull_color: Array[int, int, int, int | None] = ..., bear_color: Array[int, int, int, int | None] = ..., weight: float = ..., tooltip: bool = ..., time_unit: int = ..., **kwargs) -> None: ...


class mvCharRemap(AppItemType):
    """Remaps a character.

    Args:
        * source (int):

        * target (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_char_remap
    identity = dearpygui.mvCharRemap, 'mvAppItemType::mvCharRemap'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, source: int = ..., target: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvCheckbox(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a checkbox.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (bool, optional): Sets the default value of the checkmark

    Returns:
        *Self*
    """
    command  = dearpygui.add_checkbox
    identity = dearpygui.mvCheckbox, 'mvAppItemType::mvCheckbox'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...


class mvChildWindow(WindowItem, SizedItem, AppItemType):
    """Adds an embedded child window. Will show scrollbars when items do not fit.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * border (bool, optional): Shows/Hides the border around the sides.

        * autosize_x (bool, optional): Autosize the window to its parents size in x.

        * autosize_y (bool, optional): Autosize the window to its parents size in y.

        * no_scrollbar (bool, optional): Disable scrollbars (window can still scroll with
        mouse or programmatically).

        * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear (off
        by default).

        * menubar (bool, optional): Shows/Hides the menubar at the top.

    Returns:
        *Self*
    """
    command  = dearpygui.add_child_window
    identity = dearpygui.mvChildWindow, 'mvAppItemType::mvChildWindow'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    width               : int
    height              : int
    indent              : int
    before              : ItemId
    payload_type        : str
    drop_callback       : DPGCallback
    show                : bool
    pos                 : Array[int, int]
    filter_key          : str
    delay_search        : bool
    tracked             : bool
    track_offset        : float
    border              : bool
    autosize_x          : bool
    autosize_y          : bool
    no_scrollbar        : bool
    horizontal_scrollbar: bool
    menubar             : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ..., **kwargs) -> None: ...


class mvClickedHandler(HandlerItem, AppItemType):
    """Adds a clicked handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_clicked_handler
    identity = dearpygui.mvClickedHandler, 'mvAppItemType::mvClickedHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvClipper(ContainerItem, AppItemType):
    """Helper to manually clip large list of items. Increases performance by not searching or
    drawing widgets outside of the clipped region.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Returns:
        *Self*
    """
    command  = dearpygui.add_clipper
    identity = dearpygui.mvClipper, 'mvAppItemType::mvClipper'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    show              : bool
    delay_search      : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...


class mvCollapsingHeader(ContainerItem, PositionedItem, AppItemType):
    """Adds a collapsing header to add items to. Must be closed with the end command.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * closable (bool, optional): Adds the ability to hide this widget by pressing the
        (x) in the top right of widget.

        * default_open (bool, optional): Sets the collapseable header open by default.

        * open_on_double_click (bool, optional): Need double-click to open node.

        * open_on_arrow (bool, optional): Only open when clicking on the arrow part.

        * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf
        nodes).

        * bullet (bool, optional): Display a bullet instead of arrow.

    Returns:
        *Self*
    """
    command  = dearpygui.add_collapsing_header
    identity = dearpygui.mvCollapsingHeader, 'mvAppItemType::mvCollapsingHeader'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    indent              : int
    before              : ItemId
    payload_type        : str
    drag_callback       : DPGCallback
    drop_callback       : DPGCallback
    show                : bool
    pos                 : Array[int, int]
    filter_key          : str
    delay_search        : bool
    tracked             : bool
    track_offset        : float
    closable            : bool
    open_on_double_click: bool
    open_on_arrow       : bool
    leaf                : bool
    bullet              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., **kwargs) -> None: ...


class mvColorButton(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a color button.

    Args:
        * default_value (Sequence[int], optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_border (bool, optional): Disable border around the image.

        * no_drag_drop (bool, optional): Disable ability to drag and drop small preview
        (color square) to apply colors to other items.

    Returns:
        *Self*
    """
    command  = dearpygui.add_color_button
    identity = dearpygui.mvColorButton, 'mvAppItemType::mvColorButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    no_alpha          : bool
    no_border         : bool
    no_drag_drop      : bool
    
    @typing_overload
    def __init__(self, default_value: Array[int, int, int, int | None] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_border: bool = ..., no_drag_drop: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_border: bool = ..., no_drag_drop: bool = ..., **kwargs) -> None: ...


class mvColorEdit(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds an RGBA color editor. Left clicking the small color preview will provide a color
    picker. Click and draging the small color preview will copy the color to be applied on
    any other color widget.

    Args:
        * default_value (Sequence[int], optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_picker (bool, optional): Disable picker popup when color square is clicked.

        * no_options (bool, optional): Disable toggling options menu when right-clicking
        on inputs/small preview.

        * no_small_preview (bool, optional): Disable colored square preview next to the
        inputs. (e. g. to show only the inputs). This only displays if the side preview is
        not shown.

        * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e. g. to show
        only the small preview colored square)

        * no_tooltip (bool, optional): Disable tooltip when hovering the preview.

        * no_label (bool, optional): Disable display of inline text label.

        * no_drag_drop (bool, optional): Disable ability to drag and drop small preview
        (color square) to apply colors to other items.

        * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.

        * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone,
        mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf

        * display_mode (int, optional): mvColorEdit_rgb, mvColorEdit_hsv, or
        mvColorEdit_hex

        * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float

        * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv

    Returns:
        *Self*
    """
    command  = dearpygui.add_color_edit
    identity = dearpygui.mvColorEdit, 'mvAppItemType::mvColorEdit'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    no_alpha          : bool
    no_picker         : bool
    no_options        : bool
    no_small_preview  : bool
    no_inputs         : bool
    no_tooltip        : bool
    no_label          : bool
    no_drag_drop      : bool
    alpha_bar         : bool
    alpha_preview     : int
    display_mode      : int
    display_type      : int
    input_mode        : int
    
    @typing_overload
    def __init__(self, default_value: Array[int, int, int, int | None] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_picker: bool = ..., no_options: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., no_drag_drop: bool = ..., alpha_bar: bool = ..., alpha_preview: int = ..., display_mode: int = ..., display_type: int = ..., input_mode: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_picker: bool = ..., no_options: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., no_drag_drop: bool = ..., alpha_bar: bool = ..., alpha_preview: int = ..., display_mode: int = ..., display_type: int = ..., input_mode: int = ..., **kwargs) -> None: ...


class mvColorMap(AppItemType):
    """Adds a legend that pairs colors with normalized value 0. 0->1. 0. Each color will be This is
    typically used with a heat series. (ex. [[0, 0, 0, 255], [255, 255, 255, 255]] will be
    mapped to a soft transition from 0. 0-1. 0)

    Args:
        * colors (Any): colors that will be mapped to the normalized value 0. 0->1. 0

        * qualitative (bool): Qualitative will create hard transitions for color boundries
        across the value range when enabled.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_colormap
    identity = dearpygui.mvColorMap, 'mvAppItemType::mvColorMap'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, colors: Array[int, int, int, int | None] = ..., qualitative: bool = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvColorMapButton(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a button that a color map can be bound to.

    Args:
        * default_value (Sequence[int], optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

    Returns:
        *Self*
    """
    command  = dearpygui.add_colormap_button
    identity = dearpygui.mvColorMapButton, 'mvAppItemType::mvColorMapButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    
    @typing_overload
    def __init__(self, default_value: Array[int, int, int, int | None] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...


class mvColorMapRegistry(RegistryItem, AppItemType):
    """Adds a colormap registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_colormap_registry
    identity = dearpygui.mvColorMapRegistry, 'mvAppItemType::mvColorMapRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvColorMapScale(SizedItem, AppItemType):
    """Adds a legend that pairs values with colors. This is typically used with a heat series.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * colormap (int | str, optional): mvPlotColormap_* constants or mvColorMap uuid
        from a color map registry

        * min_scale (float, optional): Sets the min number of the color scale. Typically
        is the same as the min scale from the heat series.

        * max_scale (float, optional): Sets the max number of the color scale. Typically
        is the same as the max scale from the heat series.

    Returns:
        *Self*
    """
    command  = dearpygui.add_colormap_scale
    identity = dearpygui.mvColorMapScale, 'mvAppItemType::mvColorMapScale'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    colormap          : ItemId
    min_scale         : float
    max_scale         : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., colormap: ItemId = ..., min_scale: float = ..., max_scale: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., colormap: ItemId = ..., min_scale: float = ..., max_scale: float = ..., **kwargs) -> None: ...


class mvColorMapSlider(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a color slider that a color map can be bound to.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_colormap_slider
    identity = dearpygui.mvColorMapSlider, 'mvAppItemType::mvColorMapSlider'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...


class mvColorPicker(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds an RGB color picker. Right click the color picker for options. Click and drag the color
    preview to copy the color and drop on any other color widget to apply. Right Click
    allows the style of the color picker to be changed.

    Args:
        * default_value (Sequence[int], optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_side_preview (bool, optional): Disable bigger color preview on right side of
        the picker, use small colored square preview instead , unless small preview is also
        hidden.

        * no_small_preview (bool, optional): Disable colored square preview next to the
        inputs. (e. g. to show only the inputs). This only displays if the side preview is
        not shown.

        * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e. g. to show
        only the small preview colored square)

        * no_tooltip (bool, optional): Disable tooltip when hovering the preview.

        * no_label (bool, optional): Disable display of inline text label.

        * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.

        * display_rgb (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * display_hsv (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * display_hex (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * picker_mode (int, optional): mvColorPicker_bar or mvColorPicker_wheel

        * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone,
        mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf

        * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float

        * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv

    Returns:
        *Self*
    """
    command  = dearpygui.add_color_picker
    identity = dearpygui.mvColorPicker, 'mvAppItemType::mvColorPicker'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    no_alpha          : bool
    no_side_preview   : bool
    no_small_preview  : bool
    no_inputs         : bool
    no_tooltip        : bool
    no_label          : bool
    alpha_bar         : bool
    display_rgb       : bool
    display_hsv       : bool
    display_hex       : bool
    picker_mode       : int
    alpha_preview     : int
    display_type      : int
    input_mode        : int
    
    @typing_overload
    def __init__(self, default_value: Array[int, int, int, int | None] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_side_preview: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., alpha_bar: bool = ..., display_rgb: bool = ..., display_hsv: bool = ..., display_hex: bool = ..., picker_mode: int = ..., alpha_preview: int = ..., display_type: int = ..., input_mode: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_side_preview: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., alpha_bar: bool = ..., display_rgb: bool = ..., display_hsv: bool = ..., display_hex: bool = ..., picker_mode: int = ..., alpha_preview: int = ..., display_type: int = ..., input_mode: int = ..., **kwargs) -> None: ...


class mvColorValue(ValueAbleItem, AppItemType):
    """Adds a color value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Sequence[float], optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_color_value
    identity = dearpygui.mvColorValue, 'mvAppItemType::mvColorValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Sequence[float] = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvCombo(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window.
    All items will be shown as selectables on the dropdown.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown in the drop down
        window. Can consist of any combination of types but will convert all items to
        strings to be shown.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (str, optional): Sets a selected item from the drop down by
        specifying the string value.

        * popup_align_left (bool, optional): Align the contents on the popup toward the
        left.

        * no_arrow_button (bool, optional): Display the preview box without the square
        arrow button indicating dropdown activity.

        * no_preview (bool, optional): Display only the square arrow button and not the
        selected value.

        * height_mode (int, optional): Controlls the number of items shown in the dropdown
        by the constants mvComboHeight_Small, mvComboHeight_Regular, mvComboHeight_Large,
        mvComboHeight_Largest

    Returns:
        *Self*
    """
    command  = dearpygui.add_combo
    identity = dearpygui.mvCombo, 'mvAppItemType::mvCombo'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    popup_align_left  : bool
    no_arrow_button   : bool
    no_preview        : bool
    height_mode       : int
    
    @typing_overload
    def __init__(self, items: Sequence[str] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., popup_align_left: bool = ..., no_arrow_button: bool = ..., no_preview: bool = ..., height_mode: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., popup_align_left: bool = ..., no_arrow_button: bool = ..., no_preview: bool = ..., height_mode: int = ..., **kwargs) -> None: ...


class mvCustomSeries(ContainerItem, ValueArrayItem, CallableItem, AppItemType):
    """Adds a custom series to a plot. New in 1. 6.

    Args:
        * x (Any):

        * y (Any):

        * channel_count (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * y1 (Any, optional):

        * y2 (Any, optional):

        * y3 (Any, optional):

        * tooltip (bool, optional): Show tooltip when plot is hovered.

    Returns:
        *Self*
    """
    command  = dearpygui.add_custom_series
    identity = dearpygui.mvCustomSeries, 'mvAppItemType::mvCustomSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    callback          : DPGCallback
    show              : bool
    y1                : Any
    y2                : Any
    y3                : Any
    tooltip           : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., channel_count: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., y1: Any = ..., y2: Any = ..., y3: Any = ..., tooltip: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., y1: Any = ..., y2: Any = ..., y3: Any = ..., tooltip: bool = ..., **kwargs) -> None: ...


class mvDatePicker(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a data picker.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (dict, optional):

        * level (int, optional): Use avaliable constants. mvDatePickerLevel_Day,
        mvDatePickerLevel_Month, mvDatePickerLevel_Year

    Returns:
        *Self*
    """
    command  = dearpygui.add_date_picker
    identity = dearpygui.mvDatePicker, 'mvAppItemType::mvDatePicker'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    level             : int
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., level: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., level: int = ..., **kwargs) -> None: ...


class mvDeactivatedAfterEditHandler(HandlerItem, AppItemType):
    """Adds a deactivated after edit handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_deactivated_after_edit_handler
    identity = dearpygui.mvDeactivatedAfterEditHandler, 'mvAppItemType::mvDeactivatedAfterEditHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvDeactivatedHandler(HandlerItem, AppItemType):
    """Adds a deactivated handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_deactivated_handler
    identity = dearpygui.mvDeactivatedHandler, 'mvAppItemType::mvDeactivatedHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvDouble4Value(ValueAbleItem, AppItemType):
    """Adds a double value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Any, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_double4_value
    identity = dearpygui.mvDouble4Value, 'mvAppItemType::mvDouble4Value'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Any = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvDoubleClickedHandler(HandlerItem, AppItemType):
    """Adds a double click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_double_clicked_handler
    identity = dearpygui.mvDoubleClickedHandler, 'mvAppItemType::mvDoubleClickedHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvDoubleValue(ValueAbleItem, AppItemType):
    """Adds a double value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (float, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_double_value
    identity = dearpygui.mvDoubleValue, 'mvAppItemType::mvDoubleValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: float = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvDragDouble(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag for a single double value. Useful when drag float is not accurate enough. Directly
    entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit
    for the drag. Use clamped keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_double
    identity = dearpygui.mvDragDouble, 'mvAppItemType::mvDragDouble'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    speed             : float
    min_value         : float
    max_value         : float
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragDoubleMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag input for a set of double values up to 4. Useful when drag float is not accurate
    enough. Directly entry can be done with double click or CTRL+Click. Min and Max alone
    are a soft limit for the drag. Use clamped keyword to also apply limits to the direct
    entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Any, optional):

        * size (int, optional): Number of doubles to be displayed.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_doublex
    identity = dearpygui.mvDragDoubleMulti, 'mvAppItemType::mvDragDoubleMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    format            : str
    speed             : float
    min_value         : float
    max_value         : float
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragFloat(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag for a single float value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also
    apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_float
    identity = dearpygui.mvDragFloat, 'mvAppItemType::mvDragFloat'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    speed             : float
    min_value         : float
    max_value         : float
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragFloatMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag input for a set of float values up to 4. Directly entry can be done with double
    click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped
    keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[float], optional):

        * size (int, optional): Number of floats to be displayed.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_floatx
    identity = dearpygui.mvDragFloatMulti, 'mvAppItemType::mvDragFloatMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    format            : str
    speed             : float
    min_value         : float
    max_value         : float
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragInt(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag for a single int value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also
    apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (int, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (int, optional): Applies a limit only to draging entry only.

        * max_value (int, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_int
    identity = dearpygui.mvDragInt, 'mvAppItemType::mvDragInt'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    speed             : float
    min_value         : int
    max_value         : int
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragIntMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds drag input for a set of int values up to 4. Directly entry can be done with double
    click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped
    keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[int], optional):

        * size (int, optional): Number of ints to be displayed.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (int, optional): Applies a limit only to draging entry only.

        * max_value (int, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_intx
    identity = dearpygui.mvDragIntMulti, 'mvAppItemType::mvDragIntMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    format            : str
    speed             : float
    min_value         : int
    max_value         : int
    no_input          : bool
    clamped           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Array[int, int, int, int | None] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ..., **kwargs) -> None: ...


class mvDragLine(ValueAbleItem, CallableItem, AppItemType):
    """Adds a drag line to a plot.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * default_value (Any, optional):

        * color (Sequence[int], optional):

        * thickness (float, optional):

        * show_label (bool, optional):

        * vertical (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_line
    identity = dearpygui.mvDragLine, 'mvAppItemType::mvDragLine'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    callback          : DPGCallback
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    show_label        : bool
    vertical          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., default_value: Any = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., show_label: bool = ..., vertical: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., show_label: bool = ..., vertical: bool = ..., **kwargs) -> None: ...


class mvDragPayload(ContainerItem, AppItemType):
    """User data payload for drag and drop operations.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * show (bool, optional): Attempt to render widget.

        * drag_data (Any, optional): Drag data

        * drop_data (Any, optional): Drop data

        * payload_type (str, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_payload
    identity = dearpygui.mvDragPayload, 'mvAppItemType::mvDragPayload'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    drag_data         : Any
    drop_data         : Any
    payload_type      : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., show: bool = ..., drag_data: Any = ..., drop_data: Any = ..., payload_type: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., drag_data: Any = ..., drop_data: Any = ..., payload_type: str = ..., **kwargs) -> None: ...


class mvDragPoint(ValueAbleItem, CallableItem, AppItemType):
    """Adds a drag point to a plot.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * default_value (Any, optional):

        * color (Sequence[int], optional):

        * thickness (float, optional):

        * show_label (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_drag_point
    identity = dearpygui.mvDragPoint, 'mvAppItemType::mvDragPoint'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    callback          : DPGCallback
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    show_label        : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., default_value: Any = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., show_label: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., show_label: bool = ..., **kwargs) -> None: ...


class mvDrawArrow(AppItemType):
    """Adds an arrow.

    Args:
        * p1 (Sequence[float]): Arrow tip.

        * p2 (Sequence[float]): Arrow tail.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * thickness (float, optional):

        * size (int, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_arrow
    identity = dearpygui.mvDrawArrow, 'mvAppItemType::mvDrawArrow'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    size              : int
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., size: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., size: int = ..., **kwargs) -> None: ...


class mvDrawBezierCubic(AppItemType):
    """Adds a cubic bezier curve.

    Args:
        * p1 (Sequence[float]): First point in curve.

        * p2 (Sequence[float]): Second point in curve.

        * p3 (Sequence[float]): Third point in curve.

        * p4 (Sequence[float]): Fourth point in curve.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * thickness (float, optional):

        * segments (int, optional): Number of segments to approximate bezier curve.

    Returns:
        *Self*
    """
    command  = dearpygui.draw_bezier_cubic
    identity = dearpygui.mvDrawBezierCubic, 'mvAppItemType::mvDrawBezierCubic'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    segments          : int
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., p3: Sequence[float] = ..., p4: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...


class mvDrawBezierQuadratic(AppItemType):
    """Adds a quadratic bezier curve.

    Args:
        * p1 (Sequence[float]): First point in curve.

        * p2 (Sequence[float]): Second point in curve.

        * p3 (Sequence[float]): Third point in curve.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * thickness (float, optional):

        * segments (int, optional): Number of segments to approximate bezier curve.

    Returns:
        *Self*
    """
    command  = dearpygui.draw_bezier_quadratic
    identity = dearpygui.mvDrawBezierQuadratic, 'mvAppItemType::mvDrawBezierQuadratic'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    segments          : int
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., p3: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...


class mvDrawCircle(AppItemType):
    """Adds a circle

    Args:
        * center (Sequence[float]):

        * radius (float):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * fill (Sequence[int], optional):

        * thickness (float, optional):

        * segments (int, optional): Number of segments to approximate circle.

    Returns:
        *Self*
    """
    command  = dearpygui.draw_circle
    identity = dearpygui.mvDrawCircle, 'mvAppItemType::mvDrawCircle'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    thickness         : float
    segments          : int
    
    @typing_overload
    def __init__(self, center: Sequence[float] = ..., radius: float = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...


class mvDrawEllipse(AppItemType):
    """Adds an ellipse.

    Args:
        * pmin (Sequence[float]): Min point of bounding rectangle.

        * pmax (Sequence[float]): Max point of bounding rectangle.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * fill (Sequence[int], optional):

        * thickness (float, optional):

        * segments (int, optional): Number of segments to approximate bezier curve.

    Returns:
        *Self*
    """
    command  = dearpygui.draw_ellipse
    identity = dearpygui.mvDrawEllipse, 'mvAppItemType::mvDrawEllipse'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    thickness         : float
    segments          : int
    
    @typing_overload
    def __init__(self, pmin: Sequence[float] = ..., pmax: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., segments: int = ..., **kwargs) -> None: ...


class mvDrawImage(AppItemType):
    """Adds an image (for a drawing).

    Args:
        * texture_tag (int | str):

        * pmin (Sequence[float]): Point of to start drawing texture.

        * pmax (Sequence[float]): Point to complete drawing texture.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * uv_min (Sequence[float], optional): Normalized coordinates on texture that will
        be drawn.

        * uv_max (Sequence[float], optional): Normalized coordinates on texture that will
        be drawn.

        * color (Sequence[int], optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_image
    identity = dearpygui.mvDrawImage, 'mvAppItemType::mvDrawImage'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    uv_min            : Sequence[float]
    uv_max            : Sequence[float]
    color             : Array[int, int, int, int | None]
    
    @typing_overload
    def __init__(self, texture_tag: ItemId = ..., pmin: Sequence[float] = ..., pmax: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...


class mvDrawImageQuad(AppItemType):
    """Adds an image (for a drawing).

    Args:
        * texture_tag (int | str):

        * p1 (Sequence[float]):

        * p2 (Sequence[float]):

        * p3 (Sequence[float]):

        * p4 (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * uv1 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv2 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv3 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv4 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * color (Sequence[int], optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_image_quad
    identity = dearpygui.mvDrawImageQuad, 'mvAppItemType::mvDrawImageQuad'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    uv1               : Sequence[float]
    uv2               : Sequence[float]
    uv3               : Sequence[float]
    uv4               : Sequence[float]
    color             : Array[int, int, int, int | None]
    
    @typing_overload
    def __init__(self, texture_tag: ItemId = ..., p1: Sequence[float] = ..., p2: Sequence[float] = ..., p3: Sequence[float] = ..., p4: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., uv1: Sequence[float] = ..., uv2: Sequence[float] = ..., uv3: Sequence[float] = ..., uv4: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., uv1: Sequence[float] = ..., uv2: Sequence[float] = ..., uv3: Sequence[float] = ..., uv4: Sequence[float] = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...


class mvDrawLayer(ContainerItem, AppItemType):
    """New in 1. 1. Creates a layer useful for grouping drawlist items.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * perspective_divide (bool, optional): New in 1. 1. apply perspective divide

        * depth_clipping (bool, optional): New in 1. 1. apply depth clipping

        * cull_mode (int, optional): New in 1. 1. culling mode, mvCullMode_* constants.
        Only works with triangles currently.

    Returns:
        *Self*
    """
    command  = dearpygui.add_draw_layer
    identity = dearpygui.mvDrawLayer, 'mvAppItemType::mvDrawLayer'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    perspective_divide: bool
    depth_clipping    : bool
    cull_mode         : int
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., perspective_divide: bool = ..., depth_clipping: bool = ..., cull_mode: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., perspective_divide: bool = ..., depth_clipping: bool = ..., cull_mode: int = ..., **kwargs) -> None: ...


class mvDrawLine(AppItemType):
    """Adds a line.

    Args:
        * p1 (Sequence[float]): Start of line.

        * p2 (Sequence[float]): End of line.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_line
    identity = dearpygui.mvDrawLine, 'mvAppItemType::mvDrawLine'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawNode(ContainerItem, AppItemType):
    """New in 1. 1. Creates a drawing node to associate a transformation matrix. Child node
    matricies will concatenate.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_draw_node
    identity = dearpygui.mvDrawNode, 'mvAppItemType::mvDrawNode'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvDrawPolygon(AppItemType):
    """Adds a polygon.

    Args:
        * points (List[List[float]]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * fill (Sequence[int], optional):

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_polygon
    identity = dearpygui.mvDrawPolygon, 'mvAppItemType::mvDrawPolygon'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    thickness         : float
    
    @typing_overload
    def __init__(self, points: list[list[float]] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawPolyline(AppItemType):
    """Adds a polyline.

    Args:
        * points (List[List[float]]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * closed (bool, optional): Will close the polyline by returning to the first
        point.

        * color (Sequence[int], optional):

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_polyline
    identity = dearpygui.mvDrawPolyline, 'mvAppItemType::mvDrawPolyline'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    closed            : bool
    color             : Array[int, int, int, int | None]
    thickness         : float
    
    @typing_overload
    def __init__(self, points: list[list[float]] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., closed: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., closed: bool = ..., color: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawQuad(AppItemType):
    """Adds a quad.

    Args:
        * p1 (Sequence[float]):

        * p2 (Sequence[float]):

        * p3 (Sequence[float]):

        * p4 (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * fill (Sequence[int], optional):

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_quad
    identity = dearpygui.mvDrawQuad, 'mvAppItemType::mvDrawQuad'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    thickness         : float
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., p3: Sequence[float] = ..., p4: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawRect(AppItemType):
    """Adds a rectangle.

    Args:
        * pmin (Sequence[float]): Min point of bounding rectangle.

        * pmax (Sequence[float]): Max point of bounding rectangle.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * color_upper_left (Sequence[int], optional): 'multicolor' must be set to 'True'

        * color_upper_right (Sequence[int], optional): 'multicolor' must be set to 'True'

        * color_bottom_right (Sequence[int], optional): 'multicolor' must be set to 'True'

        * color_bottom_left (Sequence[int], optional): 'multicolor' must be set to 'True'

        * fill (Sequence[int], optional):

        * multicolor (bool, optional):

        * rounding (float, optional): Number of pixels of the radius that will round the
        corners of the rectangle. Note: doesn't work with multicolor

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_rectangle
    identity = dearpygui.mvDrawRect, 'mvAppItemType::mvDrawRect'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    color_upper_left  : Array[int, int, int, int | None]
    color_upper_right : Array[int, int, int, int | None]
    color_bottom_right: Array[int, int, int, int | None]
    color_bottom_left : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    multicolor        : Array[int, int, int, int | None]
    rounding          : float
    thickness         : float
    
    @typing_overload
    def __init__(self, pmin: Sequence[float] = ..., pmax: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., color_upper_left: Array[int, int, int, int | None] = ..., color_upper_right: Array[int, int, int, int | None] = ..., color_bottom_right: Array[int, int, int, int | None] = ..., color_bottom_left: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., multicolor: Array[int, int, int, int | None] = ..., rounding: float = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., color_upper_left: Array[int, int, int, int | None] = ..., color_upper_right: Array[int, int, int, int | None] = ..., color_bottom_right: Array[int, int, int, int | None] = ..., color_bottom_left: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., multicolor: Array[int, int, int, int | None] = ..., rounding: float = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawText(PositionedItem, AppItemType):
    """Adds text (drawlist).

    Args:
        * pos (Sequence[float]): Top left point of bounding text rectangle.

        * text (str): Text to draw.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * size (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_text
    identity = dearpygui.mvDrawText, 'mvAppItemType::mvDrawText'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    size              : float
    
    @typing_overload
    def __init__(self, pos: Array[int, int] = ..., text: str = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., size: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., size: float = ..., **kwargs) -> None: ...


class mvDrawTriangle(AppItemType):
    """Adds a triangle.

    Args:
        * p1 (Sequence[float]):

        * p2 (Sequence[float]):

        * p3 (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * color (Sequence[int], optional):

        * fill (Sequence[int], optional):

        * thickness (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.draw_triangle
    identity = dearpygui.mvDrawTriangle, 'mvAppItemType::mvDrawTriangle'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    show              : bool
    color             : Array[int, int, int, int | None]
    fill              : Array[int, int, int, int | None]
    thickness         : float
    
    @typing_overload
    def __init__(self, p1: Sequence[float] = ..., p2: Sequence[float] = ..., p3: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., show: bool = ..., color: Array[int, int, int, int | None] = ..., fill: Array[int, int, int, int | None] = ..., thickness: float = ..., **kwargs) -> None: ...


class mvDrawlist(ContainerItem, SizedItem, CallableItem, AppItemType):
    """Adds a drawing canvas.

    Args:
        * width (int):

        * height (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

    Returns:
        *Self*
    """
    command  = dearpygui.add_drawlist
    identity = dearpygui.mvDrawlist, 'mvAppItemType::mvDrawlist'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    callback          : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    
    @typing_overload
    def __init__(self, width: int = ..., height: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...


class mvDynamicTexture(ValueAbleItem, AppItemType):
    """Adds a dynamic texture.

    Args:
        * width (int):

        * height (int):

        * default_value (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_dynamic_texture
    identity = dearpygui.mvDynamicTexture, 'mvAppItemType::mvDynamicTexture'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, width: int = ..., height: int = ..., default_value: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvEditedHandler(HandlerItem, AppItemType):
    """Adds an edited handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_edited_handler
    identity = dearpygui.mvEditedHandler, 'mvAppItemType::mvEditedHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvErrorSeries(ValueArrayItem, AppItemType):
    """Adds an error series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * negative (Any):

        * positive (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * contribute_to_bounds (bool, optional):

        * horizontal (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_error_series
    identity = dearpygui.mvErrorSeries, 'mvAppItemType::mvErrorSeries'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    before              : ItemId
    source              : ItemId
    show                : bool
    contribute_to_bounds: bool
    horizontal          : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., negative: Sequence[float] = ..., positive: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., contribute_to_bounds: bool = ..., horizontal: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., contribute_to_bounds: bool = ..., horizontal: bool = ..., **kwargs) -> None: ...


class mvFileDialog(RootItem, CallableItem, AppItemType):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by
    default. Callback will be ran when the file or directory picker is closed. The app_data
    arguemnt will be populated with information related to the file and directory as a
    dictionary.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * default_path (str, optional): Path that the file dialog will default to when
        opened.

        * default_filename (str, optional): Default name that will show in the file name
        input.

        * file_count (int, optional): Number of visible files in the dialog.

        * modal (bool, optional): Forces user interaction with the file selector.

        * directory_selector (bool, optional): Shows only directory/paths as options.
        Allows selection of directory/paths only.

        * min_size (Sequence[int], optional): Minimum window size.

        * max_size (Sequence[int], optional): Maximum window size.

        * cancel_callback (Callable, optional): Callback called when cancel button is
        clicked.

    Returns:
        *Self*
    """
    command  = dearpygui.add_file_dialog
    identity = dearpygui.mvFileDialog, 'mvAppItemType::mvFileDialog'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    callback          : DPGCallback
    show              : bool
    file_count        : int
    modal             : bool
    directory_selector: bool
    min_size          : Sequence[int]
    max_size          : Sequence[int]
    cancel_callback   : DPGCallback
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., callback: DPGCallback = ..., show: bool = ..., default_path: str = ..., default_filename: str = ..., file_count: int = ..., modal: bool = ..., directory_selector: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., cancel_callback: DPGCallback = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., callback: DPGCallback = ..., show: bool = ..., file_count: int = ..., modal: bool = ..., directory_selector: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., cancel_callback: DPGCallback = ..., **kwargs) -> None: ...


class mvFileExtension(AppItemType):
    """Creates a file extension filter option in the file dialog.

    Args:
        * extension (str): Extension that will show as an when the parent is a file
        dialog.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * custom_text (str, optional): Replaces the displayed text in the drop down for
        this extension.

        * color (Sequence[int], optional): Color for the text that will be shown with
        specified extensions.

    Returns:
        *Self*
    """
    command  = dearpygui.add_file_extension
    identity = dearpygui.mvFileExtension, 'mvAppItemType::mvFileExtension'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    before            : ItemId
    custom_text       : str
    color             : Array[int, int, int, int | None]
    
    @typing_overload
    def __init__(self, extension: str = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., parent: ItemId = ..., before: ItemId = ..., custom_text: str = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., before: ItemId = ..., custom_text: str = ..., color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...


class mvFilterSet(ContainerItem, AppItemType):
    """Helper to parse and apply text filters (e. g. aaaaa[, bbbbb][, ccccc])

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Returns:
        *Self*
    """
    command  = dearpygui.add_filter_set
    identity = dearpygui.mvFilterSet, 'mvAppItemType::mvFilterSet'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    show              : bool
    delay_search      : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...


class mvFloat4Value(ValueAbleItem, AppItemType):
    """Adds a float4 value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Sequence[float], optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_float4_value
    identity = dearpygui.mvFloat4Value, 'mvAppItemType::mvFloat4Value'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Sequence[float] = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvFloatValue(ValueAbleItem, AppItemType):
    """Adds a float value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (float, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_float_value
    identity = dearpygui.mvFloatValue, 'mvAppItemType::mvFloatValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: float = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvFloatVectValue(ValueAbleItem, AppItemType):
    """Adds a float vect value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Sequence[float], optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_float_vect_value
    identity = dearpygui.mvFloatVectValue, 'mvAppItemType::mvFloatVectValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Sequence[float] = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvFocusHandler(HandlerItem, AppItemType):
    """Adds a focus handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_focus_handler
    identity = dearpygui.mvFocusHandler, 'mvAppItemType::mvFocusHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvFont(ContainerItem, AppItemType):
    """Adds font to a font registry.

    Args:
        * file (str):

        * size (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_font
    identity = dearpygui.mvFont, 'mvAppItemType::mvFont'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, file: str = ..., size: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvFontChars(AppItemType):
    """Adds specific font characters to a font.

    Args:
        * chars (Sequence[int]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_font_chars
    identity = dearpygui.mvFontChars, 'mvAppItemType::mvFontChars'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, chars: Sequence[int] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvFontRange(AppItemType):
    """Adds a range of font characters to a font.

    Args:
        * first_char (int):

        * last_char (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_font_range
    identity = dearpygui.mvFontRange, 'mvAppItemType::mvFontRange'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, first_char: int = ..., last_char: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvFontRangeHint(AppItemType):
    """Adds a range of font characters (mvFontRangeHint_ constants).

    Args:
        * hint (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_font_range_hint
    identity = dearpygui.mvFontRangeHint, 'mvAppItemType::mvFontRangeHint'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, hint: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvFontRegistry(RegistryItem, AppItemType):
    """Adds a font registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_font_registry
    identity = dearpygui.mvFontRegistry, 'mvAppItemType::mvFontRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvGroup(ContainerItem, PositionedItem, AppItemType):
    """Creates a group that other widgets can belong to. The group allows item commands to be
    issued for all of its members.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * horizontal (bool, optional): Forces child widgets to be added in a horizontal
        layout.

        * horizontal_spacing (float, optional): Spacing for the horizontal layout.

        * xoffset (float, optional): Offset from containing window x item location within
        group.

    Returns:
        *Self*
    """
    command  = dearpygui.add_group
    identity = dearpygui.mvGroup, 'mvAppItemType::mvGroup'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    horizontal        : bool
    horizontal_spacing: float
    xoffset           : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., horizontal: bool = ..., horizontal_spacing: float = ..., xoffset: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., horizontal: bool = ..., horizontal_spacing: float = ..., xoffset: float = ..., **kwargs) -> None: ...


class mvHLineSeries(ValueArrayItem, AppItemType):
    """Adds an infinite horizontal line series to a plot.

    Args:
        * x (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_hline_series
    identity = dearpygui.mvHLineSeries, 'mvAppItemType::mvHLineSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvHandlerRegistry(RegistryItem, AppItemType):
    """Adds a handler registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_handler_registry
    identity = dearpygui.mvHandlerRegistry, 'mvAppItemType::mvHandlerRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvHeatSeries(ValueArrayItem, AppItemType):
    """Adds a heat series to a plot.

    Args:
        * x (Any):

        * rows (int):

        * cols (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * scale_min (float, optional): Sets the color scale min. Typically paired with the
        color scale widget scale_min.

        * scale_max (float, optional): Sets the color scale max. Typically paired with the
        color scale widget scale_max.

        * bounds_min (Any, optional):

        * bounds_max (Any, optional):

        * format (str, optional):

        * contribute_to_bounds (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_heat_series
    identity = dearpygui.mvHeatSeries, 'mvAppItemType::mvHeatSeries'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    before              : ItemId
    source              : ItemId
    show                : bool
    scale_min           : float
    scale_max           : float
    bounds_min          : Any
    bounds_max          : Any
    format              : str
    contribute_to_bounds: bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., rows: int = ..., cols: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., scale_min: float = ..., scale_max: float = ..., bounds_min: Any = ..., bounds_max: Any = ..., format: str = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., scale_min: float = ..., scale_max: float = ..., bounds_min: Any = ..., bounds_max: Any = ..., format: str = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...


class mvHistogramSeries(ValueArrayItem, AppItemType):
    """Adds a histogram series to a plot.

    Args:
        * x (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * bins (int, optional):

        * bar_scale (float, optional):

        * min_range (float, optional):

        * max_range (float, optional):

        * cumlative (bool, optional):

        * density (bool, optional):

        * outliers (bool, optional):

        * contribute_to_bounds (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_histogram_series
    identity = dearpygui.mvHistogramSeries, 'mvAppItemType::mvHistogramSeries'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    before              : ItemId
    source              : ItemId
    show                : bool
    bins                : int
    bar_scale           : float
    min_range           : float
    max_range           : float
    cumlative           : bool
    density             : bool
    outliers            : bool
    contribute_to_bounds: bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., bins: int = ..., bar_scale: float = ..., min_range: float = ..., max_range: float = ..., cumlative: bool = ..., density: bool = ..., outliers: bool = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., bins: int = ..., bar_scale: float = ..., min_range: float = ..., max_range: float = ..., cumlative: bool = ..., density: bool = ..., outliers: bool = ..., contribute_to_bounds: bool = ..., **kwargs) -> None: ...


class mvHoverHandler(HandlerItem, AppItemType):
    """Adds a hover handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_hover_handler
    identity = dearpygui.mvHoverHandler, 'mvAppItemType::mvHoverHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvImage(SizedItem, AppItemType):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture
    coordinates of the original image that will be shown. Using range (0. 0,0. 0)->(1. 0,1.
    0) for texture coordinates will generally display the entire texture.

    Args:
        * texture_tag (int | str): The texture_tag should come from a texture that was
        added to a texture registry.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * tint_color (Sequence[float], optional): Applies a color tint to the entire
        texture.

        * border_color (Sequence[float], optional): Displays a border of the specified
        color around the texture. If the theme style has turned off the border it will not
        be shown.

        * uv_min (Sequence[float], optional): Normalized texture coordinates min point.

        * uv_max (Sequence[float], optional): Normalized texture coordinates max point.

    Returns:
        *Self*
    """
    command  = dearpygui.add_image
    identity = dearpygui.mvImage, 'mvAppItemType::mvImage'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    tint_color        : Array[int, int, int, int | None]
    border_color      : Array[int, int, int, int | None]
    uv_min            : Sequence[float]
    uv_max            : Sequence[float]
    
    @typing_overload
    def __init__(self, texture_tag: ItemId = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., tint_color: Array[int, int, int, int | None] = ..., border_color: Array[int, int, int, int | None] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., tint_color: Array[int, int, int, int | None] = ..., border_color: Array[int, int, int, int | None] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., **kwargs) -> None: ...


class mvImageButton(SizedItem, CallableItem, AppItemType):
    """Adds an button with a texture. uv_min and uv_max represent the normalized texture
    coordinates of the original image that will be shown. Using range (0. 0,0. 0)->(1. 0,1.
    0) texture coordinates will generally display the entire texture

    Args:
        * texture_tag (int | str): The texture_tag should come from a texture that was
        added to a texture registry.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * frame_padding (int, optional): Empty space around the outside of the texture.
        Button will show around the texture.

        * tint_color (Sequence[float], optional): Applies a color tint to the entire
        texture.

        * background_color (Sequence[float], optional): Displays a border of the specified
        color around the texture.

        * uv_min (Sequence[float], optional): Normalized texture coordinates min point.

        * uv_max (Sequence[float], optional): Normalized texture coordinates max point.

    Returns:
        *Self*
    """
    command  = dearpygui.add_image_button
    identity = dearpygui.mvImageButton, 'mvAppItemType::mvImageButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    frame_padding     : int
    tint_color        : Array[int, int, int, int | None]
    background_color  : Array[int, int, int, int | None]
    uv_min            : Sequence[float]
    uv_max            : Sequence[float]
    
    @typing_overload
    def __init__(self, texture_tag: ItemId = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., frame_padding: int = ..., tint_color: Array[int, int, int, int | None] = ..., background_color: Array[int, int, int, int | None] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., frame_padding: int = ..., tint_color: Array[int, int, int, int | None] = ..., background_color: Array[int, int, int, int | None] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., **kwargs) -> None: ...


class mvImageSeries(ValueArrayItem, AppItemType):
    """Adds an image series to a plot.

    Args:
        * texture_tag (int | str):

        * bounds_min (Any):

        * bounds_max (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * uv_min (Sequence[float], optional): normalized texture coordinates

        * uv_max (Sequence[float], optional): normalized texture coordinates

        * tint_color (Sequence[int], optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_image_series
    identity = dearpygui.mvImageSeries, 'mvAppItemType::mvImageSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    uv_min            : Sequence[float]
    uv_max            : Sequence[float]
    tint_color        : Array[int, int, int, int | None]
    
    @typing_overload
    def __init__(self, texture_tag: ItemId = ..., bounds_min: Sequence[float] = ..., bounds_max: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., tint_color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., tint_color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...


class mvInputDouble(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds input for an double. Useful when input float is not accurate enough. +/- buttons can be
    activated by setting the value of step.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * min_value (float, optional): Value for lower limit of input. By default this
        limits the step buttons. Use min_clamped to limit manual input.

        * max_value (float, optional): Value for upper limit of input. By default this
        limits the step buttons. Use max_clamped to limit manual input.

        * step (float, optional): Increment to change value by when the step buttons are
        pressed. Setting this and step_fast to a value of 0 or less will turn off step
        buttons.

        * step_fast (float, optional): Increment to change value by when ctrl + step
        buttons are pressed. Setting this and step to a value of 0 or less will turn off
        step buttons.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_double
    identity = dearpygui.mvInputDouble, 'mvAppItemType::mvInputDouble'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    min_value         : float
    max_value         : float
    step              : float
    step_fast         : float
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputDoubleMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi double input for up to 4 double values. Useful when input float mulit is not
    accurate enough.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Any, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * min_value (float, optional): Value for lower limit of input for each cell. Use
        min_clamped to turn on.

        * max_value (float, optional): Value for upper limit of input for each cell. Use
        max_clamped to turn on.

        * size (int, optional): Number of components displayed for input.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_doublex
    identity = dearpygui.mvInputDoubleMulti, 'mvAppItemType::mvInputDoubleMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    min_value         : float
    max_value         : float
    size              : int
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputFloat(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds input for an float. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * min_value (float, optional): Value for lower limit of input. By default this
        limits the step buttons. Use min_clamped to limit manual input.

        * max_value (float, optional): Value for upper limit of input. By default this
        limits the step buttons. Use max_clamped to limit manual input.

        * step (float, optional): Increment to change value by when the step buttons are
        pressed. Setting this and step_fast to a value of 0 or less will turn off step
        buttons.

        * step_fast (float, optional): Increment to change value by when ctrl + step
        buttons are pressed. Setting this and step to a value of 0 or less will turn off
        step buttons.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_float
    identity = dearpygui.mvInputFloat, 'mvAppItemType::mvInputFloat'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    min_value         : float
    max_value         : float
    step              : float
    step_fast         : float
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputFloatMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi float input for up to 4 float values.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[float], optional):

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

        * min_value (float, optional): Value for lower limit of input for each cell. Use
        min_clamped to turn on.

        * max_value (float, optional): Value for upper limit of input for each cell. Use
        max_clamped to turn on.

        * size (int, optional): Number of components displayed for input.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_floatx
    identity = dearpygui.mvInputFloatMulti, 'mvAppItemType::mvInputFloatMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    format            : str
    min_value         : float
    max_value         : float
    size              : int
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputInt(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds input for an int. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (int, optional):

        * min_value (int, optional): Value for lower limit of input. By default this
        limits the step buttons. Use min_clamped to limit manual input.

        * max_value (int, optional): Value for upper limit of input. By default this
        limits the step buttons. Use max_clamped to limit manual input.

        * step (int, optional): Increment to change value by when the step buttons are
        pressed. Setting this and step_fast to a value of 0 or less will turn off step
        buttons.

        * step_fast (int, optional): Increment to change value by when ctrl + step buttons
        are pressed. Setting this and step to a value of 0 or less will turn off step
        buttons.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_int
    identity = dearpygui.mvInputInt, 'mvAppItemType::mvInputInt'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    min_value         : int
    max_value         : int
    step              : int
    step_fast         : int
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., min_value: int = ..., max_value: int = ..., step: int = ..., step_fast: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., min_value: int = ..., max_value: int = ..., step: int = ..., step_fast: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputIntMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi int input for up to 4 integer values.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[int], optional):

        * min_value (int, optional): Value for lower limit of input for each cell. Use
        min_clamped to turn on.

        * max_value (int, optional): Value for upper limit of input for each cell. Use
        max_clamped to turn on.

        * size (int, optional): Number of components displayed for input.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter.

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_intx
    identity = dearpygui.mvInputIntMulti, 'mvAppItemType::mvInputIntMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    min_value         : int
    max_value         : int
    size              : int
    min_clamped       : bool
    max_clamped       : bool
    on_enter          : bool
    readonly          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Array[int, int, int, int | None] = ..., min_value: int = ..., max_value: int = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., min_value: int = ..., max_value: int = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ..., **kwargs) -> None: ...


class mvInputText(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds input for text.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (str, optional):

        * hint (str, optional): Displayed only when value is an empty string. Will
        reappear if input value is set to empty string. Will not show if default value is
        anything other than default empty string.

        * multiline (bool, optional): Allows for multiline text input.

        * no_spaces (bool, optional): Filter out spaces and tabs.

        * uppercase (bool, optional): Automatically make all inputs uppercase.

        * tab_input (bool, optional): Allows tabs to be input into the string value
        instead of changing item focus.

        * decimal (bool, optional): Only allow characters 0123456789. +-*/

        * hexadecimal (bool, optional): Only allow characters 0123456789ABCDEFabcdef

        * readonly (bool, optional): Activates read only mode where no text can be input
        but text can still be highlighted.

        * password (bool, optional): Display all input characters as '*'.

        * scientific (bool, optional): Only allow characters 0123456789. +-*/eE
        (Scientific notation input)

        * on_enter (bool, optional): Only runs callback on enter key press.

    Returns:
        *Self*
    """
    command  = dearpygui.add_input_text
    identity = dearpygui.mvInputText, 'mvAppItemType::mvInputText'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    hint              : str
    multiline         : bool
    no_spaces         : bool
    uppercase         : bool
    tab_input         : bool
    decimal           : bool
    hexadecimal       : bool
    readonly          : bool
    password          : bool
    scientific        : bool
    on_enter          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., hint: str = ..., multiline: bool = ..., no_spaces: bool = ..., uppercase: bool = ..., tab_input: bool = ..., decimal: bool = ..., hexadecimal: bool = ..., readonly: bool = ..., password: bool = ..., scientific: bool = ..., on_enter: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., hint: str = ..., multiline: bool = ..., no_spaces: bool = ..., uppercase: bool = ..., tab_input: bool = ..., decimal: bool = ..., hexadecimal: bool = ..., readonly: bool = ..., password: bool = ..., scientific: bool = ..., on_enter: bool = ..., **kwargs) -> None: ...


class mvInt4Value(ValueAbleItem, AppItemType):
    """Adds a int4 value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Sequence[int], optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_int4_value
    identity = dearpygui.mvInt4Value, 'mvAppItemType::mvInt4Value'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Array[int, int, int, int | None] = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvIntValue(ValueAbleItem, AppItemType):
    """Adds a int value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (int, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_int_value
    identity = dearpygui.mvIntValue, 'mvAppItemType::mvIntValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: int = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvItemHandlerRegistry(RegistryItem, AppItemType):
    """Adds an item handler registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_handler_registry
    identity = dearpygui.mvItemHandlerRegistry, 'mvAppItemType::mvItemHandlerRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvKeyDownHandler(HandlerItem, AppItemType):
    """Adds a key down handler.

    Args:
        * key (int, optional): Submits callback for all keys

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_key_down_handler
    identity = dearpygui.mvKeyDownHandler, 'mvAppItemType::mvKeyDownHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, key: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvKeyPressHandler(HandlerItem, AppItemType):
    """Adds a key press handler.

    Args:
        * key (int, optional): Submits callback for all keys

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_key_press_handler
    identity = dearpygui.mvKeyPressHandler, 'mvAppItemType::mvKeyPressHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, key: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvKeyReleaseHandler(HandlerItem, AppItemType):
    """Adds a key release handler.

    Args:
        * key (int, optional): Submits callback for all keys

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_key_release_handler
    identity = dearpygui.mvKeyReleaseHandler, 'mvAppItemType::mvKeyReleaseHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, key: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvKnobFloat(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a knob that rotates based on change in x mouse position.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * min_value (float, optional): Applies lower limit to value.

        * max_value (float, optional): Applies upper limit to value.

    Returns:
        *Self*
    """
    command  = dearpygui.add_knob_float
    identity = dearpygui.mvKnobFloat, 'mvAppItemType::mvKnobFloat'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    min_value         : float
    max_value         : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., min_value: float = ..., max_value: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., min_value: float = ..., max_value: float = ..., **kwargs) -> None: ...


class mvLabelSeries(AppItemType):
    """Adds a label series to a plot.

    Args:
        * x (float):

        * y (float):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * x_offset (int, optional):

        * y_offset (int, optional):

        * vertical (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_text_point
    identity = dearpygui.mvLabelSeries, 'mvAppItemType::mvLabelSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    x_offset          : int
    y_offset          : int
    vertical          : bool
    
    @typing_overload
    def __init__(self, x: float = ..., y: float = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., x_offset: int = ..., y_offset: int = ..., vertical: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., x_offset: int = ..., y_offset: int = ..., vertical: bool = ..., **kwargs) -> None: ...


class mvLineSeries(ValueArrayItem, AppItemType):
    """Adds a line series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_line_series
    identity = dearpygui.mvLineSeries, 'mvAppItemType::mvLineSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvListbox(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a listbox. If height is not large enough to show all items a scroll bar will appear.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown in the listbox.
        Can consist of any combination of types. All items will be displayed as strings.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (str, optional): String value of the item that will be selected by
        default.

        * num_items (int, optional): Expands the height of the listbox to show specified
        number of items.

    Returns:
        *Self*
    """
    command  = dearpygui.add_listbox
    identity = dearpygui.mvListbox, 'mvAppItemType::mvListbox'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    num_items         : int
    
    @typing_overload
    def __init__(self, items: Sequence[str] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., num_items: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., num_items: int = ..., **kwargs) -> None: ...


class mvLoadingIndicator(SizedItem, AppItemType):
    """Adds a rotating animated loading symbol.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * style (int, optional): 0 is rotating dots style, 1 is rotating bar style.

        * circle_count (int, optional): Number of dots show if dots or size of circle if
        circle.

        * speed (float, optional): Speed the anamation will rotate.

        * radius (float, optional): Radius size of the loading indicator.

        * thickness (float, optional): Thickness of the circles or line.

        * color (Sequence[int], optional): Color of the growing center circle.

        * secondary_color (Sequence[int], optional): Background of the dots in dot mode.

    Returns:
        *Self*
    """
    command  = dearpygui.add_loading_indicator
    identity = dearpygui.mvLoadingIndicator, 'mvAppItemType::mvLoadingIndicator'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    style             : int
    circle_count      : int
    speed             : float
    radius            : float
    thickness         : float
    color             : Array[int, int, int, int | None]
    secondary_color   : Array[int, int, int, int | None]
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., style: int = ..., circle_count: int = ..., speed: float = ..., radius: float = ..., thickness: float = ..., color: Array[int, int, int, int | None] = ..., secondary_color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., style: int = ..., circle_count: int = ..., speed: float = ..., radius: float = ..., thickness: float = ..., color: Array[int, int, int, int | None] = ..., secondary_color: Array[int, int, int, int | None] = ..., **kwargs) -> None: ...


class mvMenu(ContainerItem, AppItemType):
    """Adds a menu to an existing menu bar.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

    Returns:
        *Self*
    """
    command  = dearpygui.add_menu
    identity = dearpygui.mvMenu, 'mvAppItemType::mvMenu'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., **kwargs) -> None: ...


class mvMenuBar(ContainerItem, AppItemType):
    """Adds a menu bar to a window.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * show (bool, optional): Attempt to render widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Returns:
        *Self*
    """
    command  = dearpygui.add_menu_bar
    identity = dearpygui.mvMenuBar, 'mvAppItemType::mvMenuBar'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    show              : bool
    delay_search      : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...


class mvMenuItem(ValueAbleItem, CallableItem, AppItemType):
    """Adds a menu item to an existing menu. Menu items act similar to selectables and has a bool
    value. When placed in a menu the checkmark will reflect its value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (bool, optional): This value also controls the checkmark when
        shown.

        * shortcut (str, optional): Displays text on the menu item. Typically used to show
        a shortcut key command.

        * check (bool, optional): Displays a checkmark on the menu item when it is
        selected and placed in a menu.

    Returns:
        *Self*
    """
    command  = dearpygui.add_menu_item
    identity = dearpygui.mvMenuItem, 'mvAppItemType::mvMenuItem'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    filter_key        : str
    tracked           : bool
    track_offset      : float
    shortcut          : str
    check             : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., shortcut: str = ..., check: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., shortcut: str = ..., check: bool = ..., **kwargs) -> None: ...


class mvMouseClickHandler(HandlerItem, AppItemType):
    """Adds a mouse click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_click_handler
    identity = dearpygui.mvMouseClickHandler, 'mvAppItemType::mvMouseClickHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseDoubleClickHandler(HandlerItem, AppItemType):
    """Adds a mouse double click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_double_click_handler
    identity = dearpygui.mvMouseDoubleClickHandler, 'mvAppItemType::mvMouseDoubleClickHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseDownHandler(HandlerItem, AppItemType):
    """Adds a mouse down handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_down_handler
    identity = dearpygui.mvMouseDownHandler, 'mvAppItemType::mvMouseDownHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseDragHandler(HandlerItem, AppItemType):
    """Adds a mouse drag handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * threshold (float, optional): The threshold the mouse must be dragged before the
        callback is ran

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_drag_handler
    identity = dearpygui.mvMouseDragHandler, 'mvAppItemType::mvMouseDragHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., threshold: float = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseMoveHandler(HandlerItem, AppItemType):
    """Adds a mouse move handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_move_handler
    identity = dearpygui.mvMouseMoveHandler, 'mvAppItemType::mvMouseMoveHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseReleaseHandler(HandlerItem, AppItemType):
    """Adds a mouse release handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_release_handler
    identity = dearpygui.mvMouseReleaseHandler, 'mvAppItemType::mvMouseReleaseHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, button: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvMouseWheelHandler(HandlerItem, AppItemType):
    """Adds a mouse wheel handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_mouse_wheel_handler
    identity = dearpygui.mvMouseWheelHandler, 'mvAppItemType::mvMouseWheelHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvNode(ContainerItem, PositionedItem, AppItemType):
    """Adds a node to a node editor.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * draggable (bool, optional): Allow node to be draggable.

    Returns:
        *Self*
    """
    command  = dearpygui.add_node
    identity = dearpygui.mvNode, 'mvAppItemType::mvNode'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    draggable         : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., draggable: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., draggable: bool = ..., **kwargs) -> None: ...


class mvNodeAttribute(ContainerItem, AppItemType):
    """Adds a node attribute to a node.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * attribute_type (int, optional): mvNode_Attr_Input, mvNode_Attr_Output, or
        mvNode_Attr_Static.

        * shape (int, optional): Pin shape.

        * category (str, optional): Category

    Returns:
        *Self*
    """
    command  = dearpygui.add_node_attribute
    identity = dearpygui.mvNodeAttribute, 'mvAppItemType::mvNodeAttribute'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    show              : bool
    filter_key        : str
    tracked           : bool
    track_offset      : float
    attribute_type    : int
    shape             : int
    category          : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., attribute_type: int = ..., shape: int = ..., category: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., attribute_type: int = ..., shape: int = ..., category: str = ..., **kwargs) -> None: ...


class mvNodeEditor(ContainerItem, CallableItem, AppItemType):
    """Adds a node editor.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * delink_callback (Callable, optional): Callback ran when a link is detached.

        * menubar (bool, optional): Shows or hides the menubar.

        * minimap (bool, optional): Shows or hides the Minimap. New in 1. 6.

        * minimap_location (int, optional): mvNodeMiniMap_Location_* constants. New in 1.
        6.

    Returns:
        *Self*
    """
    command  = dearpygui.add_node_editor
    identity = dearpygui.mvNodeEditor, 'mvAppItemType::mvNodeEditor'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    before            : ItemId
    callback          : DPGCallback
    show              : bool
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    delink_callback   : DPGCallback
    menubar           : bool
    minimap           : bool
    minimap_location  : int
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., parent: ItemId = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., delink_callback: DPGCallback = ..., menubar: bool = ..., minimap: bool = ..., minimap_location: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., delink_callback: DPGCallback = ..., menubar: bool = ..., minimap: bool = ..., minimap_location: int = ..., **kwargs) -> None: ...


class mvNodeLink(AppItemType):
    """Adds a node link between 2 node attributes.

    Args:
        * attr_1 (int | str):

        * attr_2 (int | str):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_node_link
    identity = dearpygui.mvNodeLink, 'mvAppItemType::mvNodeLink'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, attr_1: ItemId = ..., attr_2: ItemId = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvPieSeries(ValueArrayItem, AppItemType):
    """Adds an pie series to a plot.

    Args:
        * x (float):

        * y (float):

        * radius (float):

        * values (Any):

        * labels (Sequence[str]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * format (str, optional):

        * angle (float, optional):

        * normalize (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_pie_series
    identity = dearpygui.mvPieSeries, 'mvAppItemType::mvPieSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    format            : str
    angle             : float
    normalize         : bool
    
    @typing_overload
    def __init__(self, x: float = ..., y: float = ..., radius: float = ..., values: Sequence[float] = ..., labels: Sequence[str] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., format: str = ..., angle: float = ..., normalize: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., format: str = ..., angle: float = ..., normalize: bool = ..., **kwargs) -> None: ...


class mvPlot(ContainerItem, SizedItem, CallableItem, AppItemType):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * no_title (bool, optional): the plot title will not be displayed

        * no_menus (bool, optional): the user will not be able to open context menus with
        right-click

        * no_box_select (bool, optional): the user will not be able to box-select with
        right-click drag

        * no_mouse_pos (bool, optional): the mouse position, in plot coordinates, will not
        be displayed inside of the plot

        * no_highlight (bool, optional): plot items will not be highlighted when their
        legend entry is hovered

        * no_child (bool, optional): a child window region will not be used to capture
        mouse scroll (can boost performance for single ImGui window applications)

        * query (bool, optional): the user will be able to draw query rects with middle -
        mouse or CTRL + right - click drag

        * crosshairs (bool, optional): the default mouse cursor will be replaced with a
        crosshair when hovered

        * anti_aliased (bool, optional): plot lines will be software anti-aliased (not
        recommended for high density plots, prefer MSAA)

        * equal_aspects (bool, optional): primary x and y axes will be constrained to have
        the same units/pixel (does not apply to auxiliary y-axes)

        * use_local_time (bool, optional): axis labels will be formatted for your timezone
        when

        * use_ISO8601 (bool, optional): dates will be formatted according to ISO 8601
        where applicable (e. g. YYYY-MM-DD, YYYY-MM, --MM-DD, etc. )

        * use_24hour_clock (bool, optional): times will be formatted using a 24 hour clock

        * pan_button (int, optional): enables panning when held

        * pan_mod (int, optional): optional modifier that must be held for panning

        * fit_button (int, optional): fits visible data when double clicked

        * context_menu_button (int, optional): opens plot context menu (if enabled) when
        clicked

        * box_select_button (int, optional): begins box selection when pressed and
        confirms selection when released

        * box_select_mod (int, optional): begins box selection when pressed and confirms
        selection when released

        * box_select_cancel_button (int, optional): cancels active box selection when
        pressed

        * query_button (int, optional): begins query selection when pressed and end query
        selection when released

        * query_mod (int, optional): optional modifier that must be held for query
        selection

        * query_toggle_mod (int, optional): when held, active box selections turn into
        queries

        * horizontal_mod (int, optional): expands active box selection/query horizontally
        to plot edge when held

        * vertical_mod (int, optional): expands active box selection/query vertically to
        plot edge when held

    Returns:
        *Self*
    """
    command  = dearpygui.add_plot
    identity = dearpygui.mvPlot, 'mvAppItemType::mvPlot'
    
    label                   : str
    user_data               : Any
    use_internal_label      : bool
    width                   : int
    height                  : int
    indent                  : int
    before                  : ItemId
    payload_type            : str
    callback                : DPGCallback
    drag_callback           : DPGCallback
    drop_callback           : DPGCallback
    show                    : bool
    pos                     : Array[int, int]
    filter_key              : str
    delay_search            : bool
    tracked                 : bool
    track_offset            : float
    no_title                : bool
    no_menus                : bool
    no_box_select           : bool
    no_mouse_pos            : bool
    no_highlight            : bool
    no_child                : bool
    query                   : bool
    crosshairs              : bool
    anti_aliased            : bool
    equal_aspects           : bool
    use_local_time          : bool
    use_ISO8601             : bool
    use_24hour_clock        : bool
    pan_button              : int
    pan_mod                 : int
    fit_button              : int
    context_menu_button     : int
    box_select_button       : int
    box_select_mod          : int
    box_select_cancel_button: int
    query_button            : int
    query_mod               : int
    query_toggle_mod        : int
    horizontal_mod          : int
    vertical_mod            : int
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., no_title: bool = ..., no_menus: bool = ..., no_box_select: bool = ..., no_mouse_pos: bool = ..., no_highlight: bool = ..., no_child: bool = ..., query: bool = ..., crosshairs: bool = ..., anti_aliased: bool = ..., equal_aspects: bool = ..., use_local_time: bool = ..., use_ISO8601: bool = ..., use_24hour_clock: bool = ..., pan_button: int = ..., pan_mod: int = ..., fit_button: int = ..., context_menu_button: int = ..., box_select_button: int = ..., box_select_mod: int = ..., box_select_cancel_button: int = ..., query_button: int = ..., query_mod: int = ..., query_toggle_mod: int = ..., horizontal_mod: int = ..., vertical_mod: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., no_title: bool = ..., no_menus: bool = ..., no_box_select: bool = ..., no_mouse_pos: bool = ..., no_highlight: bool = ..., no_child: bool = ..., query: bool = ..., crosshairs: bool = ..., anti_aliased: bool = ..., equal_aspects: bool = ..., use_local_time: bool = ..., use_ISO8601: bool = ..., use_24hour_clock: bool = ..., pan_button: int = ..., pan_mod: int = ..., fit_button: int = ..., context_menu_button: int = ..., box_select_button: int = ..., box_select_mod: int = ..., box_select_cancel_button: int = ..., query_button: int = ..., query_mod: int = ..., query_toggle_mod: int = ..., horizontal_mod: int = ..., vertical_mod: int = ..., **kwargs) -> None: ...


class mvPlotAxis(ContainerItem, AppItemType):
    """Adds an axis to a plot.

    Args:
        * axis (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * no_gridlines (bool, optional):

        * no_tick_marks (bool, optional):

        * no_tick_labels (bool, optional):

        * log_scale (bool, optional):

        * invert (bool, optional):

        * lock_min (bool, optional):

        * lock_max (bool, optional):

        * time (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_plot_axis
    identity = dearpygui.mvPlotAxis, 'mvAppItemType::mvPlotAxis'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    no_gridlines      : bool
    no_tick_marks     : bool
    no_tick_labels    : bool
    log_scale         : bool
    invert            : bool
    lock_min          : bool
    lock_max          : bool
    time              : bool
    
    @typing_overload
    def __init__(self, axis: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., no_gridlines: bool = ..., no_tick_marks: bool = ..., no_tick_labels: bool = ..., log_scale: bool = ..., invert: bool = ..., lock_min: bool = ..., lock_max: bool = ..., time: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., no_gridlines: bool = ..., no_tick_marks: bool = ..., no_tick_labels: bool = ..., log_scale: bool = ..., invert: bool = ..., lock_min: bool = ..., lock_max: bool = ..., time: bool = ..., **kwargs) -> None: ...


class mvPlotLegend(AppItemType):
    """Adds a plot legend to a plot.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * location (int, optional): location, mvPlot_Location_*

        * horizontal (bool, optional):

        * outside (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_plot_legend
    identity = dearpygui.mvPlotLegend, 'mvAppItemType::mvPlotLegend'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    location          : int
    horizontal        : bool
    outside           : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., location: int = ..., horizontal: bool = ..., outside: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., location: int = ..., horizontal: bool = ..., outside: bool = ..., **kwargs) -> None: ...


class mvProgressBar(SizedItem, ValueAbleItem, AppItemType):
    """Adds a progress bar.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * overlay (str, optional): Overlayed text onto the bar that typically used to
        display the value of the progress.

        * default_value (float, optional): Normalized value to fill the bar from 0. 0 to
        1. 0.

    Returns:
        *Self*
    """
    command  = dearpygui.add_progress_bar
    identity = dearpygui.mvProgressBar, 'mvAppItemType::mvProgressBar'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    overlay           : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., overlay: str = ..., default_value: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., overlay: str = ..., **kwargs) -> None: ...


class mvRadioButton(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown as radio options.
        Can consist of any combination of types. All types will be shown as strings.

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (str, optional): Default selected radio option. Set by using the
        string value of the item.

        * horizontal (bool, optional): Displays the radio options horizontally.

    Returns:
        *Self*
    """
    command  = dearpygui.add_radio_button
    identity = dearpygui.mvRadioButton, 'mvAppItemType::mvRadioButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    horizontal        : bool
    
    @typing_overload
    def __init__(self, items: Sequence[str] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., horizontal: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., horizontal: bool = ..., **kwargs) -> None: ...


class mvRawTexture(ValueAbleItem, AppItemType):
    """Adds a raw texture.

    Args:
        * width (int):

        * height (int):

        * default_value (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * format (int, optional): Data format.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_raw_texture
    identity = dearpygui.mvRawTexture, 'mvAppItemType::mvRawTexture'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    format            : int
    
    @typing_overload
    def __init__(self, width: int = ..., height: int = ..., default_value: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., format: int = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., format: int = ..., **kwargs) -> None: ...


class mvResizeHandler(HandlerItem, AppItemType):
    """Adds a resize handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_resize_handler
    identity = dearpygui.mvResizeHandler, 'mvAppItemType::mvResizeHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvScatterSeries(ValueArrayItem, AppItemType):
    """Adds a scatter series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_scatter_series
    identity = dearpygui.mvScatterSeries, 'mvAppItemType::mvScatterSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvSelectable(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a selectable. Similar to a button but can indicate its selected state.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (bool, optional):

        * span_columns (bool, optional): Forces the selectable to span the width of all
        columns if placed in a table.

        * disable_popup_close (bool, optional): Disable closing a modal or popup window.

    Returns:
        *Self*
    """
    command  = dearpygui.add_selectable
    identity = dearpygui.mvSelectable, 'mvAppItemType::mvSelectable'
    
    label              : str
    user_data          : Any
    use_internal_label : bool
    width              : int
    height             : int
    indent             : int
    before             : ItemId
    source             : ItemId
    payload_type       : str
    callback           : DPGCallback
    drag_callback      : DPGCallback
    drop_callback      : DPGCallback
    show               : bool
    enabled            : bool
    pos                : Array[int, int]
    filter_key         : str
    tracked            : bool
    track_offset       : float
    span_columns       : bool
    disable_popup_close: bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., span_columns: bool = ..., disable_popup_close: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., span_columns: bool = ..., disable_popup_close: bool = ..., **kwargs) -> None: ...


class mvSeparator(PositionedItem, AppItemType):
    """Adds a horizontal line separator.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

    Returns:
        *Self*
    """
    command  = dearpygui.add_separator
    identity = dearpygui.mvSeparator, 'mvAppItemType::mvSeparator'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    show              : bool
    pos               : Array[int, int]
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., pos: Array[int, int] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., show: bool = ..., pos: Array[int, int] = ..., **kwargs) -> None: ...


class mvSeriesValue(ValueArrayItem, AppItemType):
    """Adds a plot series value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (Any, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_series_value
    identity = dearpygui.mvSeriesValue, 'mvAppItemType::mvSeriesValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: Any = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvShadeSeries(ValueArrayItem, AppItemType):
    """Adds a shade series to a plot.

    Args:
        * x (Any):

        * y1 (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

        * y2 (Any, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_shade_series
    identity = dearpygui.mvShadeSeries, 'mvAppItemType::mvShadeSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    y2                : Any
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y1: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., y2: Any = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., y2: Any = ..., **kwargs) -> None: ...


class mvSimplePlot(ValueAbleItem, AppItemType):
    """Adds a simple plot for visualization of a 1 dimensional set of values.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[float], optional):

        * overlay (str, optional): overlays text (similar to a plot title)

        * histogram (bool, optional):

        * autosize (bool, optional):

        * min_scale (float, optional):

        * max_scale (float, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_simple_plot
    identity = dearpygui.mvSimplePlot, 'mvAppItemType::mvSimplePlot'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    filter_key        : str
    tracked           : bool
    track_offset      : float
    overlay           : str
    histogram         : bool
    autosize          : bool
    min_scale         : float
    max_scale         : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., overlay: str = ..., histogram: bool = ..., autosize: bool = ..., min_scale: float = ..., max_scale: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., overlay: str = ..., histogram: bool = ..., autosize: bool = ..., min_scale: float = ..., max_scale: float = ..., **kwargs) -> None: ...


class mvSlider3D(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a 3D box slider.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[float], optional):

        * max_x (float, optional): Applies upper limit to slider.

        * max_y (float, optional): Applies upper limit to slider.

        * max_z (float, optional): Applies upper limit to slider.

        * min_x (float, optional): Applies lower limit to slider.

        * min_y (float, optional): Applies lower limit to slider.

        * min_z (float, optional): Applies lower limit to slider.

        * scale (float, optional): Size of the widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_3d_slider
    identity = dearpygui.mvSlider3D, 'mvAppItemType::mvSlider3D'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    max_x             : float
    max_y             : float
    max_z             : float
    min_x             : float
    min_y             : float
    min_z             : float
    scale             : float
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., max_x: float = ..., max_y: float = ..., max_z: float = ..., min_x: float = ..., min_y: float = ..., min_z: float = ..., scale: float = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., max_x: float = ..., max_y: float = ..., max_z: float = ..., min_x: float = ..., min_y: float = ..., min_z: float = ..., scale: float = ..., **kwargs) -> None: ...


class mvSliderDouble(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds slider for a single double value. Useful when slider float is not accurate enough.
    Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft
    limit for the slider. Use clamped keyword to also apply limits to the direct entry
    modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * vertical (bool, optional): Sets orientation of the slidebar and slider to
        vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_double
    identity = dearpygui.mvSliderDouble, 'mvAppItemType::mvSliderDouble'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    vertical          : bool
    no_input          : bool
    clamped           : bool
    min_value         : float
    max_value         : float
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...


class mvSliderDoubleMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi slider for up to 4 double values. Usueful for when multi slide float is not
    accurate enough. Directly entry can be done with double click or CTRL+Click. Min and Max
    alone are a soft limit for the slider. Use clamped keyword to also apply limits to the
    direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Any, optional):

        * size (int, optional): Number of doubles to be displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_doublex
    identity = dearpygui.mvSliderDoubleMulti, 'mvAppItemType::mvSliderDoubleMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    no_input          : bool
    clamped           : bool
    min_value         : float
    max_value         : float
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...


class mvSliderFloat(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds slider for a single float value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (float, optional):

        * vertical (bool, optional): Sets orientation of the slidebar and slider to
        vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_float
    identity = dearpygui.mvSliderFloat, 'mvAppItemType::mvSliderFloat'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    vertical          : bool
    no_input          : bool
    clamped           : bool
    min_value         : float
    max_value         : float
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...


class mvSliderFloatMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi slider for up to 4 float values. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[float], optional):

        * size (int, optional): Number of floats to be displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_floatx
    identity = dearpygui.mvSliderFloatMulti, 'mvAppItemType::mvSliderFloatMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    no_input          : bool
    clamped           : bool
    min_value         : float
    max_value         : float
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ..., **kwargs) -> None: ...


class mvSliderInt(SizedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds slider for a single int value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (int, optional):

        * vertical (bool, optional): Sets orientation of the slidebar and slider to
        vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (int, optional): Applies a limit only to sliding entry only.

        * max_value (int, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_int
    identity = dearpygui.mvSliderInt, 'mvAppItemType::mvSliderInt'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    vertical          : bool
    no_input          : bool
    clamped           : bool
    min_value         : int
    max_value         : int
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ..., **kwargs) -> None: ...


class mvSliderIntMulti(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds multi slider for up to 4 int values. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (Sequence[int], optional):

        * size (int, optional): Number of ints to be displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or
        ctrl+click or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (int, optional): Applies a limit only to sliding entry only.

        * max_value (int, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Returns:
        *Self*
    """
    command  = dearpygui.add_slider_intx
    identity = dearpygui.mvSliderIntMulti, 'mvAppItemType::mvSliderIntMulti'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    enabled           : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    size              : int
    no_input          : bool
    clamped           : bool
    min_value         : int
    max_value         : int
    format            : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Array[int, int, int, int | None] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., enabled: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ..., **kwargs) -> None: ...


class mvSpacer(SizedItem, AppItemType):
    """Adds a spacer item that can be used to help with layouts or can be used as a placeholder
    item.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

    Returns:
        *Self*
    """
    command  = dearpygui.add_spacer
    identity = dearpygui.mvSpacer, 'mvAppItemType::mvSpacer'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    show              : bool
    pos               : Array[int, int]
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., pos: Array[int, int] = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., show: bool = ..., pos: Array[int, int] = ..., **kwargs) -> None: ...


class mvStage(RootItem, AppItemType):
    """Adds a stage.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

    Returns:
        *Self*
    """
    command  = dearpygui.add_stage
    identity = dearpygui.mvStage, 'mvAppItemType::mvStage'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvStairSeries(ValueArrayItem, AppItemType):
    """Adds a stair series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_stair_series
    identity = dearpygui.mvStairSeries, 'mvAppItemType::mvStairSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvStaticTexture(ValueAbleItem, AppItemType):
    """Adds a static texture.

    Args:
        * width (int):

        * height (int):

        * default_value (Sequence[float]):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_static_texture
    identity = dearpygui.mvStaticTexture, 'mvAppItemType::mvStaticTexture'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, width: int = ..., height: int = ..., default_value: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvStemSeries(ValueArrayItem, AppItemType):
    """Adds a stem series to a plot.

    Args:
        * x (Any):

        * y (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_stem_series
    identity = dearpygui.mvStemSeries, 'mvAppItemType::mvStemSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., y: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvStringValue(ValueAbleItem, AppItemType):
    """Adds a string value.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * default_value (str, optional):

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

    Returns:
        *Self*
    """
    command  = dearpygui.add_string_value
    identity = dearpygui.mvStringValue, 'mvAppItemType::mvStringValue'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    source            : ItemId
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., source: ItemId = ..., default_value: str = ..., parent: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., source: ItemId = ..., **kwargs) -> None: ...


class mvSubPlots(ContainerItem, SizedItem, CallableItem, AppItemType):
    """Adds a collection of plots.

    Args:
        * rows (int):

        * columns (int):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * row_ratios (Sequence[float], optional):

        * column_ratios (Sequence[float], optional):

        * no_title (bool, optional):

        * no_menus (bool, optional): the user will not be able to open context menus with
        right-click

        * no_resize (bool, optional): resize splitters between subplot cells will be not
        be provided

        * no_align (bool, optional): subplot edges will not be aligned vertically or
        horizontally

        * link_rows (bool, optional): link the y-axis limits of all plots in each row
        (does not apply auxiliary y-axes)

        * link_columns (bool, optional): link the x-axis limits of all plots in each
        column

        * link_all_x (bool, optional): link the x-axis limits in every plot in the subplot

        * link_all_y (bool, optional): link the y-axis limits in every plot in the subplot
        (does not apply to auxiliary y-axes)

        * column_major (bool, optional): subplots are added in column major order instead
        of the default row major order

    Returns:
        *Self*
    """
    command  = dearpygui.add_subplots
    identity = dearpygui.mvSubPlots, 'mvAppItemType::mvSubPlots'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    width             : int
    height            : int
    indent            : int
    before            : ItemId
    callback          : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    row_ratios        : Sequence[float]
    column_ratios     : Sequence[float]
    no_title          : bool
    no_menus          : bool
    no_resize         : bool
    no_align          : bool
    link_rows         : bool
    link_columns      : bool
    link_all_x        : bool
    link_all_y        : bool
    column_major      : bool
    
    @typing_overload
    def __init__(self, rows: int = ..., columns: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., row_ratios: Sequence[float] = ..., column_ratios: Sequence[float] = ..., no_title: bool = ..., no_menus: bool = ..., no_resize: bool = ..., no_align: bool = ..., link_rows: bool = ..., link_columns: bool = ..., link_all_x: bool = ..., link_all_y: bool = ..., column_major: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., row_ratios: Sequence[float] = ..., column_ratios: Sequence[float] = ..., no_title: bool = ..., no_menus: bool = ..., no_resize: bool = ..., no_align: bool = ..., link_rows: bool = ..., link_columns: bool = ..., link_all_x: bool = ..., link_all_y: bool = ..., column_major: bool = ..., **kwargs) -> None: ...


class mvTab(ContainerItem, AppItemType):
    """Adds a tab to a tab bar.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * closable (bool, optional): Creates a button on the tab that can hide the tab.

        * no_tooltip (bool, optional): Disable tooltip for the given tab.

        * order_mode (bool, optional): set using a constant: mvTabOrder_Reorderable:
        allows reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to
        front, mvTabOrder_Trailing: adds tab to back

    Returns:
        *Self*
    """
    command  = dearpygui.add_tab
    identity = dearpygui.mvTab, 'mvAppItemType::mvTab'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    drop_callback     : DPGCallback
    show              : bool
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    closable          : bool
    no_tooltip        : bool
    order_mode        : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., no_tooltip: bool = ..., order_mode: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., no_tooltip: bool = ..., order_mode: bool = ..., **kwargs) -> None: ...


class mvTabBar(ContainerItem, PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a tab bar.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * reorderable (bool, optional): Allows for the user to change the order of the
        tabs.

    Returns:
        *Self*
    """
    command  = dearpygui.add_tab_bar
    identity = dearpygui.mvTabBar, 'mvAppItemType::mvTabBar'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    callback          : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    delay_search      : bool
    tracked           : bool
    track_offset      : float
    reorderable       : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., reorderable: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., reorderable: bool = ..., **kwargs) -> None: ...


class mvTabButton(CallableItem, AppItemType):
    """Adds a tab button to a tab bar.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * no_reorder (bool, optional): Disable reordering this tab or having another tab
        cross over this tab. Fixes the position of this tab in relation to the order of
        neighboring tabs at start.

        * leading (bool, optional): Enforce the tab position to the left of the tab bar
        (after the tab list popup button).

        * trailing (bool, optional): Enforce the tab position to the right of the tab bar
        (before the scrolling buttons).

        * no_tooltip (bool, optional): Disable tooltip for the given tab.

    Returns:
        *Self*
    """
    command  = dearpygui.add_tab_button
    identity = dearpygui.mvTabButton, 'mvAppItemType::mvTabButton'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    filter_key        : str
    tracked           : bool
    track_offset      : float
    no_reorder        : bool
    leading           : bool
    trailing          : bool
    no_tooltip        : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_reorder: bool = ..., leading: bool = ..., trailing: bool = ..., no_tooltip: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_reorder: bool = ..., leading: bool = ..., trailing: bool = ..., no_tooltip: bool = ..., **kwargs) -> None: ...


class mvTable(ContainerItem, SizedItem, CallableItem, AppItemType):
    """Adds a table.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * header_row (bool, optional): show headers at the top of the columns

        * clipper (bool, optional): Use clipper (rows must be same height).

        * inner_width (int, optional):

        * policy (int, optional):

        * freeze_rows (int, optional):

        * freeze_columns (int, optional):

        * sort_multi (bool, optional): Hold shift when clicking headers to sort on
        multiple column.

        * sort_tristate (bool, optional): Allow no sorting, disable default sorting.

        * resizable (bool, optional): Enable resizing columns

        * reorderable (bool, optional): Enable reordering columns in header row (need
        calling TableSetupColumn() + TableHeadersRow() to display headers)

        * hideable (bool, optional): Enable hiding/disabling columns in context menu.

        * sortable (bool, optional): Enable sorting. Call TableGetSortSpecs() to obtain
        sort specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.

        * context_menu_in_body (bool, optional): Right-click on columns body/contents will
        display table context menu. By default it is available in TableHeadersRow().

        * row_background (bool, optional): Set each RowBg color with ImGuiCol_TableRowBg
        or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with
        ImGuiTableBgFlags_RowBg0 on each row manually)

        * borders_innerH (bool, optional): Draw horizontal borders between rows.

        * borders_outerH (bool, optional): Draw horizontal borders at the top and bottom.

        * borders_innerV (bool, optional): Draw vertical borders between columns.

        * borders_outerV (bool, optional): Draw vertical borders on the left and right
        sides.

        * no_host_extendX (bool, optional): Make outer width auto-fit to columns,
        overriding outer_size. x value. Only available when ScrollX/ScrollY are disabled and
        Stretch columns are not used.

        * no_host_extendY (bool, optional): Make outer height stop exactly at outer_size.
        y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY
        are disabled. Data below the limit will be clipped and not visible.

        * no_keep_columns_visible (bool, optional): Disable keeping column always
        minimally visible when ScrollX is off and table gets too small. Not recommended if
        columns are resizable.

        * precise_widths (bool, optional): Disable distributing remainder width to
        stretched columns (width allocation on a 100-wide table with 3 columns: Without this
        flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing
        will appear to be less smooth.

        * no_clip (bool, optional): Disable clipping rectangle for every individual
        columns.

        * pad_outerX (bool, optional): Default if BordersOuterV is on. Enable outer-most
        padding. Generally desirable if you have headers.

        * no_pad_outerX (bool, optional): Default if BordersOuterV is off. Disable outer-
        most padding.

        * no_pad_innerX (bool, optional): Disable inner padding between columns (double
        inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).

        * scrollX (bool, optional): Enable horizontal scrolling. Require 'outer_size'
        parameter of BeginTable() to specify the container size. Changes default sizing
        policy. Because this create a child window, ScrollY is currently generally
        recommended when using ScrollX.

        * scrollY (bool, optional): Enable vertical scrolling.

        * no_saved_settings (bool, optional): Never load/save settings in . ini file.

    Returns:
        *Self*
    """
    command  = dearpygui.add_table
    identity = dearpygui.mvTable, 'mvAppItemType::mvTable'
    
    label                  : str
    user_data              : Any
    use_internal_label     : bool
    width                  : int
    height                 : int
    indent                 : int
    before                 : ItemId
    source                 : ItemId
    callback               : DPGCallback
    show                   : bool
    pos                    : Array[int, int]
    filter_key             : str
    delay_search           : bool
    header_row             : bool
    clipper                : bool
    inner_width            : int
    policy                 : int
    freeze_rows            : int
    freeze_columns         : int
    sort_multi             : bool
    sort_tristate          : bool
    resizable              : bool
    reorderable            : bool
    hideable               : bool
    sortable               : bool
    context_menu_in_body   : bool
    row_background         : bool
    borders_innerH         : bool
    borders_outerH         : bool
    borders_innerV         : bool
    borders_outerV         : bool
    no_host_extendX        : bool
    no_host_extendY        : bool
    no_keep_columns_visible: bool
    precise_widths         : bool
    no_clip                : bool
    pad_outerX             : bool
    no_pad_outerX          : bool
    no_pad_innerX          : bool
    scrollX                : bool
    scrollY                : bool
    no_saved_settings      : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., header_row: bool = ..., clipper: bool = ..., inner_width: int = ..., policy: int = ..., freeze_rows: int = ..., freeze_columns: int = ..., sort_multi: bool = ..., sort_tristate: bool = ..., resizable: bool = ..., reorderable: bool = ..., hideable: bool = ..., sortable: bool = ..., context_menu_in_body: bool = ..., row_background: bool = ..., borders_innerH: bool = ..., borders_outerH: bool = ..., borders_innerV: bool = ..., borders_outerV: bool = ..., no_host_extendX: bool = ..., no_host_extendY: bool = ..., no_keep_columns_visible: bool = ..., precise_widths: bool = ..., no_clip: bool = ..., pad_outerX: bool = ..., no_pad_outerX: bool = ..., no_pad_innerX: bool = ..., scrollX: bool = ..., scrollY: bool = ..., no_saved_settings: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., header_row: bool = ..., clipper: bool = ..., inner_width: int = ..., policy: int = ..., freeze_rows: int = ..., freeze_columns: int = ..., sort_multi: bool = ..., sort_tristate: bool = ..., resizable: bool = ..., reorderable: bool = ..., hideable: bool = ..., sortable: bool = ..., context_menu_in_body: bool = ..., row_background: bool = ..., borders_innerH: bool = ..., borders_outerH: bool = ..., borders_innerV: bool = ..., borders_outerV: bool = ..., no_host_extendX: bool = ..., no_host_extendY: bool = ..., no_keep_columns_visible: bool = ..., precise_widths: bool = ..., no_clip: bool = ..., pad_outerX: bool = ..., no_pad_outerX: bool = ..., no_pad_innerX: bool = ..., scrollX: bool = ..., scrollY: bool = ..., no_saved_settings: bool = ..., **kwargs) -> None: ...


class mvTableCell(ContainerItem, AppItemType):
    """Adds a table.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * height (int, optional): Height of the item.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_table_cell
    identity = dearpygui.mvTableCell, 'mvAppItemType::mvTableCell'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    height            : int
    before            : ItemId
    show              : bool
    filter_key        : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., height: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., height: int = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., **kwargs) -> None: ...


class mvTableColumn(AppItemType):
    """Adds a table column.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * enabled (bool, optional): Turns off functionality of widget and applies the
        disabled theme.

        * init_width_or_weight (float, optional):

        * default_hide (bool, optional): Default as a hidden/disabled column.

        * default_sort (bool, optional): Default as a sorting column.

        * width_stretch (bool, optional): Column will stretch. Preferable with horizontal
        scrolling disabled (default if table sizing policy is _SizingStretchSame or
        _SizingStretchProp).

        * width_fixed (bool, optional): Column will not stretch. Preferable with
        horizontal scrolling enabled (default if table sizing policy is _SizingFixedFit and
        table is resizable).

        * no_resize (bool, optional): Disable manual resizing.

        * no_reorder (bool, optional): Disable manual reordering this column, this will
        also prevent other columns from crossing over this column.

        * no_hide (bool, optional): Disable ability to hide/disable this column.

        * no_clip (bool, optional): Disable clipping for this column (all NoClip columns
        will render in a same draw command).

        * no_sort (bool, optional): Disable ability to sort on this field (even if
        ImGuiTableFlags_Sortable is set on the table).

        * no_sort_ascending (bool, optional): Disable ability to sort in the ascending
        direction.

        * no_sort_descending (bool, optional): Disable ability to sort in the descending
        direction.

        * no_header_width (bool, optional): Disable header text width contribution to
        automatic column width.

        * prefer_sort_ascending (bool, optional): Make the initial sort direction
        Ascending when first sorting on this column (default).

        * prefer_sort_descending (bool, optional): Make the initial sort direction
        Descending when first sorting on this column.

        * indent_enable (bool, optional): Use current Indent value when entering cell
        (default for column 0).

        * indent_disable (bool, optional): Ignore current Indent value when entering cell
        (default for columns > 0). Indentation changes _within_ the cell will still be
        honored.

    Returns:
        *Self*
    """
    command  = dearpygui.add_table_column
    identity = dearpygui.mvTableColumn, 'mvAppItemType::mvTableColumn'
    
    label                 : str
    user_data             : Any
    use_internal_label    : bool
    width                 : int
    before                : ItemId
    show                  : bool
    enabled               : bool
    init_width_or_weight  : float
    width_stretch         : bool
    width_fixed           : bool
    no_resize             : bool
    no_reorder            : bool
    no_hide               : bool
    no_clip               : bool
    no_sort               : bool
    no_sort_ascending     : bool
    no_sort_descending    : bool
    no_header_width       : bool
    prefer_sort_ascending : bool
    prefer_sort_descending: bool
    indent_enable         : bool
    indent_disable        : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., enabled: bool = ..., init_width_or_weight: float = ..., default_hide: bool = ..., default_sort: bool = ..., width_stretch: bool = ..., width_fixed: bool = ..., no_resize: bool = ..., no_reorder: bool = ..., no_hide: bool = ..., no_clip: bool = ..., no_sort: bool = ..., no_sort_ascending: bool = ..., no_sort_descending: bool = ..., no_header_width: bool = ..., prefer_sort_ascending: bool = ..., prefer_sort_descending: bool = ..., indent_enable: bool = ..., indent_disable: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., before: ItemId = ..., show: bool = ..., enabled: bool = ..., init_width_or_weight: float = ..., width_stretch: bool = ..., width_fixed: bool = ..., no_resize: bool = ..., no_reorder: bool = ..., no_hide: bool = ..., no_clip: bool = ..., no_sort: bool = ..., no_sort_ascending: bool = ..., no_sort_descending: bool = ..., no_header_width: bool = ..., prefer_sort_ascending: bool = ..., prefer_sort_descending: bool = ..., indent_enable: bool = ..., indent_disable: bool = ..., **kwargs) -> None: ...


class mvTableRow(ContainerItem, AppItemType):
    """Adds a table row.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * height (int, optional): Height of the item.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_table_row
    identity = dearpygui.mvTableRow, 'mvAppItemType::mvTableRow'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    height            : int
    before            : ItemId
    show              : bool
    filter_key        : str
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., height: int = ..., parent: ItemId = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., height: int = ..., before: ItemId = ..., show: bool = ..., filter_key: str = ..., **kwargs) -> None: ...


class mvTemplateRegistry(RegistryItem, AppItemType):
    """Adds a template registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

    Returns:
        *Self*
    """
    command  = dearpygui.add_template_registry
    identity = dearpygui.mvTemplateRegistry, 'mvAppItemType::mvTemplateRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvText(PositionedItem, ValueAbleItem, AppItemType):
    """Adds text. Text can have an optional label that will display to the right of the text.

    Args:
        * default_value (str, optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * wrap (int, optional): Number of pixels from the start of the item until wrapping
        starts.

        * bullet (bool, optional): Places a bullet to the left of the text.

        * color (Sequence[int], optional): Color of the text (rgba).

        * show_label (bool, optional): Displays the label to the right of the text.

    Returns:
        *Self*
    """
    command  = dearpygui.add_text
    identity = dearpygui.mvText, 'mvAppItemType::mvText'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    source            : ItemId
    payload_type      : str
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    wrap              : int
    bullet            : bool
    color             : Array[int, int, int, int | None]
    show_label        : bool
    
    @typing_overload
    def __init__(self, default_value: str = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., wrap: int = ..., bullet: bool = ..., color: Array[int, int, int, int | None] = ..., show_label: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., source: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., wrap: int = ..., bullet: bool = ..., color: Array[int, int, int, int | None] = ..., show_label: bool = ..., **kwargs) -> None: ...


class mvTextureRegistry(RegistryItem, AppItemType):
    """Adds a dynamic texture.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_texture_registry
    identity = dearpygui.mvTextureRegistry, 'mvAppItemType::mvTextureRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvTheme(RegistryItem, AppItemType):
    """Adds a theme.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

    Returns:
        *Self*
    """
    command  = dearpygui.add_theme
    identity = dearpygui.mvTheme, 'mvAppItemType::mvTheme'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvThemeColor(ValueArrayItem, AppItemType):
    """Adds a theme color.

    Args:
        * target (int, optional):

        * value (Sequence[int], optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots,
        mvThemeCat_Nodes.

    Returns:
        *Self*
    """
    command  = dearpygui.add_theme_color
    identity = dearpygui.mvThemeColor, 'mvAppItemType::mvThemeColor'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    category          : int
    
    @typing_overload
    def __init__(self, target: int = ..., value: Array[int, int, int, int | None] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., category: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., category: int = ..., **kwargs) -> None: ...


class mvThemeComponent(ContainerItem, AppItemType):
    """Adds a theme component.

    Args:
        * item_type (int, optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * enabled_state (bool, optional):

    Returns:
        *Self*
    """
    command  = dearpygui.add_theme_component
    identity = dearpygui.mvThemeComponent, 'mvAppItemType::mvThemeComponent'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    enabled_state     : bool
    
    @typing_overload
    def __init__(self, item_type: int = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., enabled_state: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., enabled_state: bool = ..., **kwargs) -> None: ...


class mvThemeStyle(ValueArrayItem, AppItemType):
    """Adds a theme style.

    Args:
        * target (int, optional):

        * x (float, optional):

        * y (float, optional):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots,
        mvThemeCat_Nodes.

    Returns:
        *Self*
    """
    command  = dearpygui.add_theme_style
    identity = dearpygui.mvThemeStyle, 'mvAppItemType::mvThemeStyle'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    category          : int
    
    @typing_overload
    def __init__(self, target: int = ..., x: float = ..., y: float = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., category: int = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., category: int = ..., **kwargs) -> None: ...


class mvTimePicker(PositionedItem, ValueAbleItem, CallableItem, AppItemType):
    """Adds a time picker.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Registers a callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_value (dict, optional):

        * hour24 (bool, optional): Show 24 hour clock instead of 12 hour.

    Returns:
        *Self*
    """
    command  = dearpygui.add_time_picker
    identity = dearpygui.mvTimePicker, 'mvAppItemType::mvTimePicker'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    before            : ItemId
    payload_type      : str
    callback          : DPGCallback
    drag_callback     : DPGCallback
    drop_callback     : DPGCallback
    show              : bool
    pos               : Array[int, int]
    filter_key        : str
    tracked           : bool
    track_offset      : float
    hour24            : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., hour24: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., callback: DPGCallback = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., hour24: bool = ..., **kwargs) -> None: ...


class mvToggledOpenHandler(HandlerItem, AppItemType):
    """Adds a togged open handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_toggled_open_handler
    identity = dearpygui.mvToggledOpenHandler, 'mvAppItemType::mvToggledOpenHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvTooltip(ContainerItem, AppItemType):
    """Adds a tooltip window.

    Args:
        * parent (int | str):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_tooltip
    identity = dearpygui.mvTooltip, 'mvAppItemType::mvTooltip'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    
    @typing_overload
    def __init__(self, parent: ItemId = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., **kwargs) -> None: ...


class mvTreeNode(ContainerItem, PositionedItem, AppItemType):
    """Adds a tree node to add items to.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Scroll tracking

        * track_offset (float, optional): 0. 0f:top, 0. 5f:center, 1. 0f:bottom

        * default_open (bool, optional): Sets the tree node open by default.

        * open_on_double_click (bool, optional): Need double-click to open node.

        * open_on_arrow (bool, optional): Only open when clicking on the arrow part.

        * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf
        nodes).

        * bullet (bool, optional): Display a bullet instead of arrow.

        * selectable (bool, optional): Makes the tree selectable.

    Returns:
        *Self*
    """
    command  = dearpygui.add_tree_node
    identity = dearpygui.mvTreeNode, 'mvAppItemType::mvTreeNode'
    
    label               : str
    user_data           : Any
    use_internal_label  : bool
    indent              : int
    before              : ItemId
    payload_type        : str
    drag_callback       : DPGCallback
    drop_callback       : DPGCallback
    show                : bool
    pos                 : Array[int, int]
    filter_key          : str
    delay_search        : bool
    tracked             : bool
    track_offset        : float
    open_on_double_click: bool
    open_on_arrow       : bool
    leaf                : bool
    bullet              : bool
    selectable          : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., selectable: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., before: ItemId = ..., payload_type: str = ..., drag_callback: DPGCallback = ..., drop_callback: DPGCallback = ..., show: bool = ..., pos: Array[int, int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., selectable: bool = ..., **kwargs) -> None: ...


class mvVLineSeries(ValueArrayItem, AppItemType):
    """Adds an infinite vertical line series to a plot.

    Args:
        * x (Any):

        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * before (int | str, optional): This item will be displayed before the specified
        item in the parent.

        * source (int | str, optional): Overrides 'id' as value storage key.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_vline_series
    identity = dearpygui.mvVLineSeries, 'mvAppItemType::mvVLineSeries'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    before            : ItemId
    source            : ItemId
    show              : bool
    
    @typing_overload
    def __init__(self, x: Sequence[float] = ..., *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., before: ItemId = ..., source: ItemId = ..., show: bool = ..., **kwargs) -> None: ...


class mvValueRegistry(RegistryItem, AppItemType):
    """Adds a value registry.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

    Returns:
        *Self*
    """
    command  = dearpygui.add_value_registry
    identity = dearpygui.mvValueRegistry, 'mvAppItemType::mvValueRegistry'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...


class mvViewportDrawlist(RootItem, AppItemType):
    """A container that is used to present draw items or layers directly to the viewport. By
    default this will draw to the back of the viewport. Layers and draw items should be
    added to this widget as children.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * show (bool, optional): Attempt to render widget.

        * filter_key (str, optional): Used by filter widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * front (bool, optional): Draws to the front of the view port instead of the back.

    Returns:
        *Self*
    """
    command  = dearpygui.add_viewport_drawlist
    identity = dearpygui.mvViewportDrawlist, 'mvAppItemType::mvViewportDrawlist'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    show              : bool
    filter_key        : str
    delay_search      : bool
    front             : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., front: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., front: bool = ..., **kwargs) -> None: ...


class mvViewportMenuBar(ContainerItem, AppItemType):
    """Adds a menubar to the viewport.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * show (bool, optional): Attempt to render widget.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Returns:
        *Self*
    """
    command  = dearpygui.add_viewport_menu_bar
    identity = dearpygui.mvViewportMenuBar, 'mvAppItemType::mvViewportMenuBar'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    indent            : int
    show              : bool
    delay_search      : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., indent: int = ..., parent: ItemId = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., indent: int = ..., show: bool = ..., delay_search: bool = ..., **kwargs) -> None: ...


class mvVisibleHandler(HandlerItem, AppItemType):
    """Adds a visible handler.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * parent (int | str, optional): Parent to add this item to. (runtime adding)

        * callback (Callable, optional): Registers a callback.

        * show (bool, optional): Attempt to render widget.

    Returns:
        *Self*
    """
    command  = dearpygui.add_item_visible_handler
    identity = dearpygui.mvVisibleHandler, 'mvAppItemType::mvVisibleHandler'
    
    label             : str
    user_data         : Any
    use_internal_label: bool
    callback          : DPGCallback
    show              : bool
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., parent: ItemId = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., callback: DPGCallback = ..., show: bool = ..., **kwargs) -> None: ...


class mvWindowAppItem(WindowItem, RootItem, SizedItem, AppItemType):
    """Creates a new window for following items to be added to.

    Args:
        * label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): User data for callbacks

        * use_internal_label (bool, optional): Use generated internal label instead of
        user specified (appends ### uuid).

        * tag (int | str, optional): Unique id used to programmatically refer to the item.
        If label is unused this will be the label.

        * width (int, optional): Width of the item.

        * height (int, optional): Height of the item.

        * indent (int, optional): Offsets the widget to the right the specified number
        multiplied by the indent style.

        * show (bool, optional): Attempt to render widget.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * min_size (Sequence[int], optional): Minimum window size.

        * max_size (Sequence[int], optional): Maximum window size.

        * menubar (bool, optional): Shows or hides the menubar.

        * collapsed (bool, optional): Collapse the window.

        * autosize (bool, optional): Autosized the window to fit it's items.

        * no_resize (bool, optional): Allows for the window size to be changed or fixed.

        * no_title_bar (bool, optional): Title name for the title bar of the window.

        * no_move (bool, optional): Allows for the window's position to be changed or
        fixed.

        * no_scrollbar (bool, optional): Disable scrollbars. (window can still scroll with
        mouse or programmatically)

        * no_collapse (bool, optional): Disable user collapsing window by double-clicking
        on it.

        * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear.
        (off by default)

        * no_focus_on_appearing (bool, optional): Disable taking focus when transitioning
        from hidden to visible state.

        * no_bring_to_front_on_focus (bool, optional): Disable bringing window to front
        when taking focus. (e. g. clicking on it or programmatically giving it focus)

        * no_close (bool, optional): Disable user closing the window by removing the close
        button.

        * no_background (bool, optional): Sets Background and border alpha to transparent.

        * modal (bool, optional): Fills area behind window according to the theme and
        disables user ability to interact with anything except the window.

        * popup (bool, optional): Fills area behind window according to the theme, removes
        title bar, collapse and close. Window can be closed by selecting area in the
        background behind the window.

        * no_saved_settings (bool, optional): Never load/save settings in . ini file.

        * no_open_over_existing_popup (bool, optional): Don't open if there's already a
        popup

        * on_close (Callable, optional): Callback ran when window is closed.

    Returns:
        *Self*
    """
    command  = dearpygui.add_window
    identity = dearpygui.mvWindowAppItem, 'mvAppItemType::mvWindowAppItem'
    
    label                      : str
    user_data                  : Any
    use_internal_label         : bool
    width                      : int
    height                     : int
    indent                     : int
    show                       : bool
    pos                        : Array[int, int]
    delay_search               : bool
    min_size                   : Sequence[int]
    max_size                   : Sequence[int]
    menubar                    : bool
    collapsed                  : bool
    autosize                   : bool
    no_resize                  : bool
    no_title_bar               : bool
    no_move                    : bool
    no_scrollbar               : bool
    no_collapse                : bool
    horizontal_scrollbar       : bool
    no_focus_on_appearing      : bool
    no_bring_to_front_on_focus : bool
    no_close                   : bool
    no_background              : bool
    modal                      : bool
    popup                      : bool
    no_saved_settings          : bool
    no_open_over_existing_popup: bool
    on_close                   : Callable
    
    @typing_overload
    def __init__(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: ItemId = ..., width: int = ..., height: int = ..., indent: int = ..., show: bool = ..., pos: Array[int, int] = ..., delay_search: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., menubar: bool = ..., collapsed: bool = ..., autosize: bool = ..., no_resize: bool = ..., no_title_bar: bool = ..., no_move: bool = ..., no_scrollbar: bool = ..., no_collapse: bool = ..., horizontal_scrollbar: bool = ..., no_focus_on_appearing: bool = ..., no_bring_to_front_on_focus: bool = ..., no_close: bool = ..., no_background: bool = ..., modal: bool = ..., popup: bool = ..., no_saved_settings: bool = ..., no_open_over_existing_popup: bool = ..., on_close: Callable = ..., **kwargs) -> None: ...
    @typing_overload
    def configure(self, *, label: str = ..., user_data: Any = ..., use_internal_label: bool = ..., width: int = ..., height: int = ..., indent: int = ..., show: bool = ..., pos: Array[int, int] = ..., delay_search: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., menubar: bool = ..., collapsed: bool = ..., autosize: bool = ..., no_resize: bool = ..., no_title_bar: bool = ..., no_move: bool = ..., no_scrollbar: bool = ..., no_collapse: bool = ..., horizontal_scrollbar: bool = ..., no_focus_on_appearing: bool = ..., no_bring_to_front_on_focus: bool = ..., no_close: bool = ..., no_background: bool = ..., modal: bool = ..., popup: bool = ..., no_saved_settings: bool = ..., no_open_over_existing_popup: bool = ..., on_close: Callable = ..., **kwargs) -> None: ...


