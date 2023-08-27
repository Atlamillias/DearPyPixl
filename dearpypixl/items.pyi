from ._dearpypixl.common import (
    Item,
    ItemAlias,
    ItemUUID,
    ItemCommand,
    Array,
    Literal,
    Sequence,
    Callable,
    Property,
    Any,
    Color,
    Point,
)
from ._dearpypixl.interface import (
    BasicType,
    ContainerType,
    DrawNodeType,
    DrawingType,
    FontType,
    HandlerType,
    NodeEditorType,
    NodeType,
    PlotAxisType,
    PlotType,
    PlottingType,
    RegistryType,
    RootType,
    SupportsCallback,
    SupportsSized,
    SupportsValueArray,
    TableItemType,
    TableType,
    ThemeType,
    WindowType,
    auto_parent as auto_parent,
    basic_types as basic_types,
    container_types as container_types,
    drawing_items as drawing_items,
    interface as interface,
    mvAll as mvAll,
    node_types as node_types,
    plotting_items as plotting_items,
    registry_types as registry_types,
    root_types as root_types,
    table_types as table_types,
    theme_types as theme_types,
)




class mv2dHistogramSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a 2d histogram series.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * xbins (int, optional): ybins (int, optional):.

        * xmin_range (float, optional): xmax_range (float, optional):.

        * ymin_range (float, optional): ymax_range (float, optional):.

        * density (bool, optional): outliers (bool, optional):.

    Command: `dearpygui.add_2d_histogram_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    xbins: Property[int] = ...
    ybins: Property[int] = ...
    xmin_range: Property[float] = ...
    xmax_range: Property[float] = ...
    ymin_range: Property[float] = ...
    ymax_range: Property[float] = ...
    density: Property[bool] = ...
    outliers: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., xbins: int = ..., ybins: int = ..., xmin_range: float = ..., xmax_range: float = ..., ymin_range: float = ..., ymax_range: float = ..., density: bool = ..., outliers: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., xbins: int = ..., ybins: int = ..., xmin_range: float = ..., xmax_range: float = ..., ymin_range: float = ..., ymax_range: float = ..., density: bool = ..., outliers: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'xbins', 'ybins', 'xmin_range', 'xmax_range', 'ymin_range', 'ymax_range', 'density', 'outliers'], Any]: ...


class mvActivatedHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a activated handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_activated_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvActiveHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a active handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_active_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvAnnotation(PlottingType, BasicType):
    """Adds an annotation to a plot.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * default_value (Any, optional): offset (Sequence[float], optional):.

        * color (Sequence[int], optional): clamped (bool, optional):.

    Command: `dearpygui.add_plot_annotation`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    offset: Property[Sequence[float]] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., default_value: Any = ..., offset: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., default_value: Any = ..., offset: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'offset', 'color', 'clamped'], Any]: ...


class mvAreaSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an area series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * fill (Sequence[int], optional): contribute_to_bounds (bool, optional):.

    Command: `dearpygui.add_area_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    contribute_to_bounds: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., contribute_to_bounds: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., contribute_to_bounds: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'fill', 'contribute_to_bounds'], Any]: ...


class mvBarSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a bar series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * weight (float, optional): horizontal (bool, optional):.

    Command: `dearpygui.add_bar_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    weight: Property[float] = ...
    horizontal: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., weight: float = ..., horizontal: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., weight: float = ..., horizontal: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'weight', 'horizontal'], Any]: ...


class mvBoolValue(BasicType):
    """Adds a bool value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (bool, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_bool_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvButton(SupportsSized, SupportsCallback, BasicType):
    """Adds a button.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * small (bool, optional): Shrinks the size of the button to the text of the label it
        contains. Useful for embedding in text.

        * arrow (bool, optional): Displays an arrow in place of the text string. This
        requires the direction keyword.

        * direction (int, optional): Sets the cardinal direction for the arrow by using
        constants mvDir_Left, mvDir_Up, mvDir_Down, mvDir_Right, mvDir_None. Arrow keyword
        must be set to True.

    Command: `dearpygui.add_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    small: Property[bool] = ...
    arrow: Property[bool] = ...
    direction: Property[int] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., small: bool = ..., arrow: bool = ..., direction: int = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., small: bool = ..., arrow: bool = ..., direction: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'small', 'arrow', 'direction'], Any]: ...


class mvCandleSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a candle series to a plot.

    Args:
        * dates (Any): opens (Any):.

        * closes (Any): lows (Any):.

        * highs (Any): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * bull_color (Sequence[int], optional): bear_color (Sequence[int], optional):.

        * weight (float, optional): tooltip (bool, optional):.

        * time_unit (int, optional): mvTimeUnit_* constants. Default mvTimeUnit_Day.

    Command: `dearpygui.add_candle_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    bull_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    bear_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    weight: Property[float] = ...
    tooltip: Property[bool] = ...
    time_unit: Property[int] = ...
    def __init__(self, dates: Sequence[float], opens: Sequence[float], closes: Sequence[float], lows: Sequence[float], highs: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., bull_color: tuple[int, int, int, int | None] | list[int] = ..., bear_color: tuple[int, int, int, int | None] | list[int] = ..., weight: float = ..., tooltip: bool = ..., time_unit: int = ...) -> None: ...
    @staticmethod
    def command(dates: Sequence[float], opens: Sequence[float], closes: Sequence[float], lows: Sequence[float], highs: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., bull_color: tuple[int, int, int, int | None] | list[int] = ..., bear_color: tuple[int, int, int, int | None] | list[int] = ..., weight: float = ..., tooltip: bool = ..., time_unit: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'bull_color', 'bear_color', 'weight', 'tooltip', 'time_unit'], Any]: ...


class mvCharRemap(BasicType):
    """Remaps a character.

    Args:
        * source (int): A reference to an existing item (as a `int` uuid, `str` alias, or
        `int` item interface). If specified, getting or setting this item's value will
        instead get or set the value of the referenced item. If the item normally displays
        its' value, it will instead display the referenced item's value.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_char_remap`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, source: int, target: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(source: int, target: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvCheckbox(SupportsCallback, BasicType):
    """Adds a checkbox.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (bool, optional): Sets the default value of the checkmark.

    Command: `dearpygui.add_checkbox`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset'], Any]: ...


class mvChildWindow(SupportsSized, WindowType, ContainerType, BasicType):
    """Adds an embedded child window. Will show scrollbars when items do not fit.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * border (bool, optional): Shows/Hides the border around the sides.

        * autosize_x (bool, optional): Autosize the window to its parents size in x.

        * autosize_y (bool, optional): Autosize the window to its parents size in y.

        * no_scrollbar (bool, optional): Disable scrollbars (window can still scroll with
        mouse or programmatically).

        * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear (off
        by default).

        * menubar (bool, optional): Shows/Hides the menubar at the top.

    Command: `dearpygui.add_child_window`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    border: Property[bool] = ...
    autosize_x: Property[bool] = ...
    autosize_y: Property[bool] = ...
    no_scrollbar: Property[bool] = ...
    horizontal_scrollbar: Property[bool] = ...
    menubar: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'border', 'autosize_x', 'autosize_y', 'no_scrollbar', 'horizontal_scrollbar', 'menubar'], Any]: ...


class mvClickedHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a clicked handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_clicked_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvClipper(ContainerType, BasicType):
    """Helper to manually clip large list of items. Increases performance by not searching or
    drawing widgets outside of the clipped region.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Command: `dearpygui.add_clipper`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    delay_search: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'show', 'delay_search'], Any]: ...


class mvCollapsingHeader(ContainerType, BasicType):
    """Adds a collapsing header to add items to. Must be closed with the end command.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * closable (bool, optional): Adds the ability to hide this widget by pressing the
        (x) in the top right of widget.

        * default_open (bool, optional): Sets the collapseable header open by default.

        * open_on_double_click (bool, optional): Need double-click to open node.

        * open_on_arrow (bool, optional): Only open when clicking on the arrow part.

        * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf
        nodes).

        * bullet (bool, optional): Display a bullet instead of arrow.

    Command: `dearpygui.add_collapsing_header`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    closable: Property[bool] = ...
    open_on_double_click: Property[bool] = ...
    open_on_arrow: Property[bool] = ...
    leaf: Property[bool] = ...
    bullet: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'closable', 'open_on_double_click', 'open_on_arrow', 'leaf', 'bullet'], Any]: ...


class mvColorButton(SupportsSized, SupportsCallback, BasicType):
    """Adds a color button.

    Args:
        * default_value (Sequence[int], optional): label (str, optional): Overrides 'name'
        as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_border (bool, optional): Disable border around the image.

        * no_drag_drop (bool, optional): Disable ability to drag and drop small preview
        (color square) to apply colors to other items.

    Command: `dearpygui.add_color_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    no_alpha: Property[bool] = ...
    no_border: Property[bool] = ...
    no_drag_drop: Property[bool] = ...
    def __init__(self, default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_border: bool = ..., no_drag_drop: bool = ...) -> None: ...
    @staticmethod
    def command(default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_border: bool = ..., no_drag_drop: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'no_alpha', 'no_border', 'no_drag_drop'], Any]: ...


class mvColorEdit(SupportsSized, SupportsCallback, BasicType):
    """Adds an RGBA color editor. Left clicking the small color preview will provide a color
    picker. Click and draging the small color preview will copy the color to be applied on
    any other color widget.

    Args:
        * default_value (Sequence[int], optional): label (str, optional): Overrides 'name'
        as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_picker (bool, optional): Disable picker popup when color square is clicked.

        * no_options (bool, optional): Disable toggling options menu when right-clicking on
        inputs/small preview.

        * no_small_preview (bool, optional): Disable colored square preview next to the
        inputs. (e.g. to show only the inputs). This only displays if the side preview is
        not shown.

        * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show
        only the small preview colored square).

        * no_tooltip (bool, optional): Disable tooltip when hovering the preview.

        * no_label (bool, optional): Disable display of inline text label.

        * no_drag_drop (bool, optional): Disable ability to drag and drop small preview
        (color square) to apply colors to other items.

        * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.

        * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone,
        mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf.

        * display_mode (int, optional): mvColorEdit_rgb, mvColorEdit_hsv, or
        mvColorEdit_hex.

        * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float.

        * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv.

    Command: `dearpygui.add_color_edit`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    no_alpha: Property[bool] = ...
    no_picker: Property[bool] = ...
    no_options: Property[bool] = ...
    no_small_preview: Property[bool] = ...
    no_inputs: Property[bool] = ...
    no_tooltip: Property[bool] = ...
    no_label: Property[bool] = ...
    no_drag_drop: Property[bool] = ...
    alpha_bar: Property[bool] = ...
    alpha_preview: Property[int] = ...
    display_mode: Property[int] = ...
    display_type: Property[int] = ...
    input_mode: Property[int] = ...
    def __init__(self, default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_picker: bool = ..., no_options: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., no_drag_drop: bool = ..., alpha_bar: bool = ..., alpha_preview: int = ..., display_mode: int = ..., display_type: int = ..., input_mode: int = ...) -> None: ...
    @staticmethod
    def command(default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_picker: bool = ..., no_options: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., no_drag_drop: bool = ..., alpha_bar: bool = ..., alpha_preview: int = ..., display_mode: int = ..., display_type: int = ..., input_mode: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'no_alpha', 'no_picker', 'no_options', 'no_small_preview', 'no_inputs', 'no_tooltip', 'no_label', 'no_drag_drop', 'alpha_bar', 'alpha_preview', 'display_mode', 'display_type', 'input_mode'], Any]: ...


class mvColorMap(BasicType):
    """Adds a legend that pairs colors with normalized value 0.0->1.0. Each color will be  This is
    typically used with a heat series. (ex. [[0, 0, 0, 255], [255, 255, 255, 255]] will be
    mapped to a soft transition from 0.0-1.0).

    Args:
        * colors (Any): colors that will be mapped to the normalized value 0.0->1.0.

        * qualitative (bool): Qualitative will create hard transitions for color boundries
        across the value range when enabled.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_colormap`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, colors: tuple[int, int, int, int | None] | list[int], qualitative: bool, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(colors: tuple[int, int, int, int | None] | list[int], qualitative: bool, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvColorMapButton(SupportsSized, SupportsCallback, BasicType):
    """Adds a button that a color map can be bound to.

    Args:
        * default_value (Sequence[int], optional): label (str, optional): Overrides 'name'
        as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

    Command: `dearpygui.add_colormap_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    def __init__(self, default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ...) -> None: ...
    @staticmethod
    def command(default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset'], Any]: ...


class mvColorMapRegistry(RegistryType):
    """Adds a colormap registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_colormap_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvColorMapScale(SupportsSized, BasicType):
    """Adds a legend that pairs values with colors. This is typically used with a heat series.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * colormap (int | str, optional): mvPlotColormap_* constants or mvColorMap uuid from
        a color map registry.

        * min_scale (float, optional): Sets the min number of the color scale. Typically is
        the same as the min scale from the heat series.

        * max_scale (float, optional): Sets the max number of the color scale. Typically is
        the same as the max scale from the heat series.

    Command: `dearpygui.add_colormap_scale`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    colormap: Property['Item'] = ...
    min_scale: Property[float] = ...
    max_scale: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., colormap: 'Item' = ..., min_scale: float = ..., max_scale: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., colormap: 'Item' = ..., min_scale: float = ..., max_scale: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'drop_callback', 'show', 'pos', 'colormap', 'min_scale', 'max_scale'], Any]: ...


class mvColorMapSlider(SupportsSized, SupportsCallback, BasicType):
    """Adds a color slider that a color map can be bound to.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

    Command: `dearpygui.add_colormap_slider`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset'], Any]: ...


class mvColorPicker(SupportsSized, SupportsCallback, BasicType):
    """Adds an RGB color picker. Right click the color picker for options. Click and drag the color
    preview to copy the color and drop on any other color widget to apply. Right Click
    allows the style of the color picker to be changed.

    Args:
        * default_value (Sequence[int], optional): label (str, optional): Overrides 'name'
        as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * no_alpha (bool, optional): Removes the displayed slider that can change alpha
        channel.

        * no_side_preview (bool, optional): Disable bigger color preview on right side of
        the picker, use small colored square preview instead , unless small preview is also
        hidden.

        * no_small_preview (bool, optional): Disable colored square preview next to the
        inputs. (e.g. to show only the inputs). This only displays if the side preview is
        not shown.

        * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show
        only the small preview colored square).

        * no_tooltip (bool, optional): Disable tooltip when hovering the preview.

        * no_label (bool, optional): Disable display of inline text label.

        * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.

        * display_rgb (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * display_hsv (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * display_hex (bool, optional): Override _display_ type among RGB/HSV/Hex.

        * picker_mode (int, optional): mvColorPicker_bar or mvColorPicker_wheel.

        * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone,
        mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf.

        * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float.

        * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv.

    Command: `dearpygui.add_color_picker`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    no_alpha: Property[bool] = ...
    no_side_preview: Property[bool] = ...
    no_small_preview: Property[bool] = ...
    no_inputs: Property[bool] = ...
    no_tooltip: Property[bool] = ...
    no_label: Property[bool] = ...
    alpha_bar: Property[bool] = ...
    display_rgb: Property[bool] = ...
    display_hsv: Property[bool] = ...
    display_hex: Property[bool] = ...
    picker_mode: Property[int] = ...
    alpha_preview: Property[int] = ...
    display_type: Property[int] = ...
    input_mode: Property[int] = ...
    def __init__(self, default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_side_preview: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., alpha_bar: bool = ..., display_rgb: bool = ..., display_hsv: bool = ..., display_hex: bool = ..., picker_mode: int = ..., alpha_preview: int = ..., display_type: int = ..., input_mode: int = ...) -> None: ...
    @staticmethod
    def command(default_value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_alpha: bool = ..., no_side_preview: bool = ..., no_small_preview: bool = ..., no_inputs: bool = ..., no_tooltip: bool = ..., no_label: bool = ..., alpha_bar: bool = ..., display_rgb: bool = ..., display_hsv: bool = ..., display_hex: bool = ..., picker_mode: int = ..., alpha_preview: int = ..., display_type: int = ..., input_mode: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'no_alpha', 'no_side_preview', 'no_small_preview', 'no_inputs', 'no_tooltip', 'no_label', 'alpha_bar', 'display_rgb', 'display_hsv', 'display_hex', 'picker_mode', 'alpha_preview', 'display_type', 'input_mode'], Any]: ...


class mvColorValue(BasicType):
    """Adds a color value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Sequence[float], optional): parent (int | str, optional): Parent to
        add this item to. (runtime adding).

    Command: `dearpygui.add_color_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvCombo(SupportsCallback, BasicType):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window.
    All items will be shown as selectables on the dropdown.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown in the drop down
        window. Can consist of any combination of types but will convert all items to
        strings to be shown.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (str, optional): Sets a selected item from the drop down by
        specifying the string value.

        * popup_align_left (bool, optional): Align the contents on the popup toward the
        left.

        * no_arrow_button (bool, optional): Display the preview box without the square arrow
        button indicating dropdown activity.

        * no_preview (bool, optional): Display only the square arrow button and not the
        selected value.

        * height_mode (int, optional): Controlls the number of items shown in the dropdown
        by the constants mvComboHeight_Small, mvComboHeight_Regular, mvComboHeight_Large,
        mvComboHeight_Largest.

    Command: `dearpygui.add_combo`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    popup_align_left: Property[bool] = ...
    no_arrow_button: Property[bool] = ...
    no_preview: Property[bool] = ...
    height_mode: Property[int] = ...
    def __init__(self, items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., popup_align_left: bool = ..., no_arrow_button: bool = ..., no_preview: bool = ..., height_mode: int = ...) -> None: ...
    @staticmethod
    def command(items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., popup_align_left: bool = ..., no_arrow_button: bool = ..., no_preview: bool = ..., height_mode: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'popup_align_left', 'no_arrow_button', 'no_preview', 'height_mode'], Any]: ...


class mvCustomSeries(SupportsValueArray, SupportsCallback, PlottingType, ContainerType, BasicType):
    """Adds a custom series to a plot. New in 1.6.

    Args:
        * x (Any): y (Any):.

        * channel_count (int): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * y1 (Any, optional): y2 (Any, optional):.

        * y3 (Any, optional): tooltip (bool, optional): Show tooltip when plot is hovered.

    Command: `dearpygui.add_custom_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    y1: Property[Any] = ...
    y2: Property[Any] = ...
    y3: Property[Any] = ...
    tooltip: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., y1: Any = ..., y2: Any = ..., y3: Any = ..., tooltip: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], channel_count: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., y1: Any = ..., y2: Any = ..., y3: Any = ..., tooltip: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'callback', 'show', 'y1', 'y2', 'y3', 'tooltip'], Any]: ...


class mvDatePicker(SupportsCallback, BasicType):
    """Adds a data picker.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (dict, optional): level (int, optional): Use avaliable constants.
        mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year.

    Command: `dearpygui.add_date_picker`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    level: Property[int] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., level: int = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., level: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'level'], Any]: ...


class mvDeactivatedAfterEditHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a deactivated after edit handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_deactivated_after_edit_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvDeactivatedHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a deactivated handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_deactivated_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvDouble4Value(BasicType):
    """Adds a double value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Any, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_double4_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Any = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Any = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvDoubleClickedHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a double click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_double_clicked_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvDoubleValue(BasicType):
    """Adds a double value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (float, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_double_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: float = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: float = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvDragDouble(SupportsCallback, BasicType):
    """Adds drag for a single double value. Useful when drag float is not accurate enough. Directly
    entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit
    for the drag. Use clamped keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Command: `dearpygui.add_drag_double`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragDoubleMulti(SupportsCallback, BasicType):
    """Adds drag input for a set of double values up to 4. Useful when drag float is not accurate
    enough. Directly entry can be done with double click or CTRL+Click. Min and Max alone
    are a soft limit for the drag. Use clamped keyword to also apply limits to the direct
    entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Any, optional): size (int, optional): Number of doubles to be
        displayed.

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

    Command: `dearpygui.add_drag_doublex`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragFloat(SupportsCallback, BasicType):
    """Adds drag for a single float value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also
    apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (float, optional): Applies a limit only to draging entry only.

        * max_value (float, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Command: `dearpygui.add_drag_float`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragFloatMulti(SupportsCallback, BasicType):
    """Adds drag input for a set of float values up to 4. Directly entry can be done with double
    click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped
    keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[float], optional): size (int, optional): Number of floats
        to be displayed.

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

    Command: `dearpygui.add_drag_floatx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: float = ..., max_value: float = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragInt(SupportsCallback, BasicType):
    """Adds drag for a single int value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also
    apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (int, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

        * speed (float, optional): Sets the sensitivity the float will be modified while
        dragging.

        * min_value (int, optional): Applies a limit only to draging entry only.

        * max_value (int, optional): Applies a limit only to draging entry only.

        * no_input (bool, optional): Disable direct entry methods or Enter key allowing to
        input text directly into the widget.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

    Command: `dearpygui.add_drag_int`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragIntMulti(SupportsCallback, BasicType):
    """Adds drag input for a set of int values up to 4. Directly entry can be done with double
    click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped
    keyword to also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[int], optional): size (int, optional): Number of ints to
        be displayed.

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

    Command: `dearpygui.add_drag_intx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    format: Property[str] = ...
    speed: Property[float] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., size: int = ..., format: str = ..., speed: float = ..., min_value: int = ..., max_value: int = ..., no_input: bool = ..., clamped: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'format', 'speed', 'min_value', 'max_value', 'no_input', 'clamped'], Any]: ...


class mvDragLine(SupportsCallback, BasicType):
    """Adds a drag line to a plot.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * default_value (Any, optional): color (Sequence[int], optional):.

        * thickness (float, optional): show_label (bool, optional):.

    Command: `dearpygui.add_drag_line`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    show_label: Property[bool] = ...
    vertical: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., default_value: Any = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., show_label: bool = ..., vertical: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., default_value: Any = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., show_label: bool = ..., vertical: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'callback', 'show', 'color', 'thickness', 'show_label', 'vertical'], Any]: ...


class mvDragPayload(ContainerType, BasicType):
    """User data payload for drag and drop operations.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * drag_data (Any, optional): Drag data.

        * drop_data (Any, optional): Drop data.

    Command: `dearpygui.add_drag_payload`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    drag_data: Property[Any] = ...
    drop_data: Property[Any] = ...
    payload_type: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., show: bool = ..., drag_data: Any = ..., drop_data: Any = ..., payload_type: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., show: bool = ..., drag_data: Any = ..., drop_data: Any = ..., payload_type: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show', 'drag_data', 'drop_data', 'payload_type'], Any]: ...


class mvDragPoint(SupportsCallback, BasicType):
    """Adds a drag point to a plot.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * default_value (Any, optional): color (Sequence[int], optional):.

        * thickness (float, optional): show_label (bool, optional):.

    Command: `dearpygui.add_drag_point`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    show_label: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., default_value: Any = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., show_label: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., default_value: Any = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., show_label: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'callback', 'show', 'color', 'thickness', 'show_label'], Any]: ...


class mvDrawArrow(DrawingType, BasicType):
    """Adds an arrow.

    Args:
        * p1 (Sequence[float]): Arrow tip.

        * p2 (Sequence[float]): Arrow tail.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): thickness (float, optional):.

    Command: `dearpygui.draw_arrow`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    size: Property[int] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., size: int = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., size: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'thickness', 'size'], Any]: ...


class mvDrawBezierCubic(DrawingType, BasicType):
    """Adds a cubic bezier curve.

    Args:
        * p1 (Sequence[float]): First point in curve.

        * p2 (Sequence[float]): Second point in curve.

        * p3 (Sequence[float]): Third point in curve.

        * p4 (Sequence[float]): Fourth point in curve.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): thickness (float, optional):.

        * segments (int, optional): Number of segments to approximate bezier curve.

    Command: `dearpygui.draw_bezier_cubic`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    segments: Property[int] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'thickness', 'segments'], Any]: ...


class mvDrawBezierQuadratic(DrawingType, BasicType):
    """Adds a quadratic bezier curve.

    Args:
        * p1 (Sequence[float]): First point in curve.

        * p2 (Sequence[float]): Second point in curve.

        * p3 (Sequence[float]): Third point in curve.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): thickness (float, optional):.

        * segments (int, optional): Number of segments to approximate bezier curve.

    Command: `dearpygui.draw_bezier_quadratic`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    segments: Property[int] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'thickness', 'segments'], Any]: ...


class mvDrawCircle(DrawingType, BasicType):
    """Adds a circle.

    Args:
        * center (Sequence[float]): radius (float):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): fill (Sequence[int], optional):.

        * thickness (float, optional): segments (int, optional): Number of segments to
        approximate circle.

    Command: `dearpygui.draw_circle`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    segments: Property[int] = ...
    def __init__(self, center: Sequence[float], radius: float, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> None: ...
    @staticmethod
    def command(center: Sequence[float], radius: float, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'fill', 'thickness', 'segments'], Any]: ...


class mvDrawEllipse(DrawingType, BasicType):
    """Adds an ellipse.

    Args:
        * pmin (Sequence[float]): Min point of bounding rectangle.

        * pmax (Sequence[float]): Max point of bounding rectangle.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): fill (Sequence[int], optional):.

        * thickness (float, optional): segments (int, optional): Number of segments to
        approximate bezier curve.

    Command: `dearpygui.draw_ellipse`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    segments: Property[int] = ...
    def __init__(self, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> None: ...
    @staticmethod
    def command(pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ..., segments: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'fill', 'thickness', 'segments'], Any]: ...


class mvDrawImage(DrawingType, BasicType):
    """Adds an image (for a drawing).

    Args:
        * texture_tag (int | str): pmin (Sequence[float]): Point of to start drawing
        texture.

        * pmax (Sequence[float]): Point to complete drawing texture.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * uv_min (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv_max (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

    Command: `dearpygui.draw_image`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    uv_min: Property[Sequence[float]] = ...
    uv_max: Property[Sequence[float]] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    def __init__(self, texture_tag: 'Item', pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> None: ...
    @staticmethod
    def command(texture_tag: 'Item', pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'uv_min', 'uv_max', 'color'], Any]: ...


class mvDrawImageQuad(DrawingType, BasicType):
    """Adds an image (for a drawing).

    Args:
        * texture_tag (int | str): p1 (Sequence[float]):.

        * p2 (Sequence[float]): p3 (Sequence[float]):.

        * p4 (Sequence[float]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * uv1 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv2 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv3 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

        * uv4 (Sequence[float], optional): Normalized coordinates on texture that will be
        drawn.

    Command: `dearpygui.draw_image_quad`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    uv1: Property[Sequence[float]] = ...
    uv2: Property[Sequence[float]] = ...
    uv3: Property[Sequence[float]] = ...
    uv4: Property[Sequence[float]] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    def __init__(self, texture_tag: 'Item', p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., uv1: Sequence[float] = ..., uv2: Sequence[float] = ..., uv3: Sequence[float] = ..., uv4: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> None: ...
    @staticmethod
    def command(texture_tag: 'Item', p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., uv1: Sequence[float] = ..., uv2: Sequence[float] = ..., uv3: Sequence[float] = ..., uv4: Sequence[float] = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'uv1', 'uv2', 'uv3', 'uv4', 'color'], Any]: ...


class mvDrawLayer(DrawingType, ContainerType, BasicType):
    """New in 1.1. Creates a layer useful for grouping drawlist items.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * perspective_divide (bool, optional): New in 1.1. apply perspective divide.

        * depth_clipping (bool, optional): New in 1.1. apply depth clipping.

        * cull_mode (int, optional): New in 1.1. culling mode, mvCullMode_* constants. Only
        works with triangles currently.

    Command: `dearpygui.add_draw_layer`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    perspective_divide: Property[bool] = ...
    depth_clipping: Property[bool] = ...
    cull_mode: Property[int] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., perspective_divide: bool = ..., depth_clipping: bool = ..., cull_mode: int = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., perspective_divide: bool = ..., depth_clipping: bool = ..., cull_mode: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'perspective_divide', 'depth_clipping', 'cull_mode'], Any]: ...


class mvDrawLine(DrawingType, BasicType):
    """Adds a line.

    Args:
        * p1 (Sequence[float]): Start of line.

        * p2 (Sequence[float]): End of line.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): thickness (float, optional):.

    Command: `dearpygui.draw_line`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'thickness'], Any]: ...


class mvDrawNode(DrawNodeType, ContainerType, BasicType):
    """New in 1.1. Creates a drawing node to associate a transformation matrix. Child node
    matricies will concatenate.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_draw_node`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show'], Any]: ...


class mvDrawPolygon(DrawingType, BasicType):
    """Adds a polygon.

    Args:
        * points (Sequence[Sequence[float]]): label (str, optional): Overrides 'name' as
        label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): fill (Sequence[int], optional):.

    Command: `dearpygui.draw_polygon`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    def __init__(self, points: Sequence[Sequence[float]], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(points: Sequence[Sequence[float]], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'fill', 'thickness'], Any]: ...


class mvDrawPolyline(DrawingType, BasicType):
    """Adds a polyline.

    Args:
        * points (Sequence[Sequence[float]]): label (str, optional): Overrides 'name' as
        label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * closed (bool, optional): Will close the polyline by returning to the first point.

        * color (Sequence[int], optional): thickness (float, optional):.

    Command: `dearpygui.draw_polyline`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    closed: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    def __init__(self, points: Sequence[Sequence[float]], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., closed: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(points: Sequence[Sequence[float]], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., closed: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'closed', 'color', 'thickness'], Any]: ...


class mvDrawQuad(DrawingType, BasicType):
    """Adds a quad.

    Args:
        * p1 (Sequence[float]): p2 (Sequence[float]):.

        * p3 (Sequence[float]): p4 (Sequence[float]):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): fill (Sequence[int], optional):.

    Command: `dearpygui.draw_quad`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], p4: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'fill', 'thickness'], Any]: ...


class mvDrawRect(DrawingType, BasicType):
    """Adds a rectangle.

    Args:
        * pmin (Sequence[float]): Min point of bounding rectangle.

        * pmax (Sequence[float]): Max point of bounding rectangle.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): color_upper_left (Sequence[int], optional):
        'multicolor' must be set to 'True'.

        * color_upper_right (Sequence[int], optional): 'multicolor' must be set to 'True'.

        * color_bottom_right (Sequence[int], optional): 'multicolor' must be set to 'True'.

        * color_bottom_left (Sequence[int], optional): 'multicolor' must be set to 'True'.

        * fill (Sequence[int], optional): multicolor (bool, optional):.

        * rounding (float, optional): Number of pixels of the radius that will round the
        corners of the rectangle. Note: doesn't work with multicolor.

    Command: `dearpygui.draw_rectangle`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    color_upper_left: Property[tuple[int, int, int, int | None] | list[int]] = ...
    color_upper_right: Property[tuple[int, int, int, int | None] | list[int]] = ...
    color_bottom_right: Property[tuple[int, int, int, int | None] | list[int]] = ...
    color_bottom_left: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    multicolor: Property[tuple[int, int, int, int | None] | list[int]] = ...
    rounding: Property[float] = ...
    thickness: Property[float] = ...
    def __init__(self, pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., color_upper_left: tuple[int, int, int, int | None] | list[int] = ..., color_upper_right: tuple[int, int, int, int | None] | list[int] = ..., color_bottom_right: tuple[int, int, int, int | None] | list[int] = ..., color_bottom_left: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., multicolor: tuple[int, int, int, int | None] | list[int] = ..., rounding: float = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(pmin: Sequence[float], pmax: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., color_upper_left: tuple[int, int, int, int | None] | list[int] = ..., color_upper_right: tuple[int, int, int, int | None] | list[int] = ..., color_bottom_right: tuple[int, int, int, int | None] | list[int] = ..., color_bottom_left: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., multicolor: tuple[int, int, int, int | None] | list[int] = ..., rounding: float = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'color_upper_left', 'color_upper_right', 'color_bottom_right', 'color_bottom_left', 'fill', 'multicolor', 'rounding', 'thickness'], Any]: ...


class mvDrawText(DrawingType, BasicType):
    """Adds text (drawlist).

    Args:
        * pos (Sequence[float]): Top left point of bounding text rectangle.

        * text (str): Text to draw.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): size (float, optional):.

    Command: `dearpygui.draw_text`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    size: Property[float] = ...
    def __init__(self, pos: tuple[int, int] | list[int], text: str, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., size: float = ...) -> None: ...
    @staticmethod
    def command(pos: tuple[int, int] | list[int], text: str, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., size: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'size'], Any]: ...


class mvDrawTriangle(DrawingType, BasicType):
    """Adds a triangle.

    Args:
        * p1 (Sequence[float]): p2 (Sequence[float]):.

        * p3 (Sequence[float]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * color (Sequence[int], optional): fill (Sequence[int], optional):.

    Command: `dearpygui.draw_triangle`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    fill: Property[tuple[int, int, int, int | None] | list[int]] = ...
    thickness: Property[float] = ...
    def __init__(self, p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> None: ...
    @staticmethod
    def command(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., fill: tuple[int, int, int, int | None] | list[int] = ..., thickness: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'show', 'color', 'fill', 'thickness'], Any]: ...


class mvDrawlist(SupportsSized, SupportsCallback, DrawingType, ContainerType, BasicType):
    """Adds a drawing canvas.

    Args:
        * width (int): Horizontal size of the item in pixels. Setting this value may
        override auto-scaling options for some items; this can be reversed by setting this
        back to 0. Note that the value is interpreted as unsigned.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

    Command: `dearpygui.add_drawlist`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    def __init__(self, width: int, height: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ...) -> None: ...
    @staticmethod
    def command(width: int, height: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset'], Any]: ...


class mvDynamicTexture(BasicType):
    """Adds a dynamic texture.

    Args:
        * width (int): Horizontal size of the item in pixels. Setting this value may
        override auto-scaling options for some items; this can be reversed by setting this
        back to 0. Note that the value is interpreted as unsigned.

        * default_value (Sequence[float]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_dynamic_texture`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvEditedHandler(SupportsCallback, HandlerType, BasicType):
    """Adds an edited handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_edited_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvErrorSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an error series to a plot.

    Args:
        * x (Any): y (Any):.

        * negative (Any): positive (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * contribute_to_bounds (bool, optional): horizontal (bool, optional):.

    Command: `dearpygui.add_error_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    contribute_to_bounds: Property[bool] = ...
    horizontal: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], negative: Sequence[float], positive: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., contribute_to_bounds: bool = ..., horizontal: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], negative: Sequence[float], positive: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., contribute_to_bounds: bool = ..., horizontal: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'contribute_to_bounds', 'horizontal'], Any]: ...


class mvFileDialog(SupportsCallback, RootType):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by
    default. Callback will be ran when the file or directory picker is closed. The app_data
    arguemnt will be populated with information related to the file and directory as a
    dictionary.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * default_path (str, optional): Path that the file dialog will default to when
        opened.

        * default_filename (str, optional): Default name that will show in the file name
        input.

        * file_count (int, optional): Number of visible files in the dialog.

        * modal (bool, optional): Forces user interaction with the file selector.

        * directory_selector (bool, optional): Shows only directory/paths as options. Allows
        selection of directory/paths only.

        * min_size (Sequence[int], optional): Minimum window size.

        * max_size (Sequence[int], optional): Maximum window size.

        * cancel_callback (Callable, optional): Callback called when cancel button is
        clicked.

    Command: `dearpygui.add_file_dialog`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    file_count: Property[int] = ...
    modal: Property[bool] = ...
    directory_selector: Property[bool] = ...
    min_size: Property[Sequence[int]] = ...
    max_size: Property[Sequence[int]] = ...
    cancel_callback: Property[Callable | None] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., callback: Callable | None = ..., show: bool = ..., default_path: str = ..., default_filename: str = ..., file_count: int = ..., modal: bool = ..., directory_selector: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., cancel_callback: Callable | None = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., callback: Callable | None = ..., show: bool = ..., default_path: str = ..., default_filename: str = ..., file_count: int = ..., modal: bool = ..., directory_selector: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., cancel_callback: Callable | None = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'callback', 'show', 'file_count', 'modal', 'directory_selector', 'min_size', 'max_size', 'cancel_callback'], Any]: ...


class mvFileExtension(BasicType):
    """Creates a file extension filter option in the file dialog.

    Args:
        * extension (str): Extension that will show as an when the parent is a file dialog.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * custom_text (str, optional): Replaces the displayed text in the drop down for this
        extension.

        * color (Sequence[int], optional): Color for the text that will be shown with
        specified extensions.

    Command: `dearpygui.add_file_extension`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    before: Property['Item'] = ...
    custom_text: Property[str] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    def __init__(self, extension: str, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., custom_text: str = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> None: ...
    @staticmethod
    def command(extension: str, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., custom_text: str = ..., color: tuple[int, int, int, int | None] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'before', 'custom_text', 'color'], Any]: ...


class mvFilterSet(ContainerType, BasicType):
    """Helper to parse and apply text filters (e.g. aaaaa[, bbbbb][, ccccc]).

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Command: `dearpygui.add_filter_set`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    delay_search: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'show', 'delay_search'], Any]: ...


class mvFloat4Value(BasicType):
    """Adds a float4 value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Sequence[float], optional): parent (int | str, optional): Parent to
        add this item to. (runtime adding).

    Command: `dearpygui.add_float4_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvFloatValue(BasicType):
    """Adds a float value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (float, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_float_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: float = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: float = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvFloatVectValue(BasicType):
    """Adds a float vect value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Sequence[float], optional): parent (int | str, optional): Parent to
        add this item to. (runtime adding).

    Command: `dearpygui.add_float_vect_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Sequence[float] = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvFocusHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a focus handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_focus_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvFont(FontType, ContainerType, BasicType):
    """Adds font to a font registry.

    Args:
        * file (str): size (int):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_font`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, file: str, size: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(file: str, size: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvFontChars(BasicType):
    """Adds specific font characters to a font.

    Args:
        * chars (Sequence[int]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_font_chars`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, chars: Sequence[int], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(chars: Sequence[int], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvFontRange(BasicType):
    """Adds a range of font characters to a font.

    Args:
        * first_char (int): last_char (int):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_font_range`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, first_char: int, last_char: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(first_char: int, last_char: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvFontRangeHint(BasicType):
    """Adds a range of font characters (mvFontRangeHint_ constants).

    Args:
        * hint (int): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_font_range_hint`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, hint: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(hint: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvFontRegistry(RegistryType):
    """Adds a font registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_font_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvGroup(SupportsSized, ContainerType, BasicType):
    """Creates a group that other widgets can belong to. The group allows item commands to be
    issued for all of its members.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * horizontal (bool, optional): Forces child widgets to be added in a horizontal
        layout.

        * horizontal_spacing (float, optional): Spacing for the horizontal layout.

        * xoffset (float, optional): Offset from containing window x item location within
        group.

    Command: `dearpygui.add_group`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    horizontal: Property[bool] = ...
    horizontal_spacing: Property[float] = ...
    xoffset: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., horizontal: bool = ..., horizontal_spacing: float = ..., xoffset: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., horizontal: bool = ..., horizontal_spacing: float = ..., xoffset: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'horizontal', 'horizontal_spacing', 'xoffset'], Any]: ...


class mvHLineSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an infinite horizontal line series to a plot.

    Args:
        * x (Any): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_hline_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show'], Any]: ...


class mvHandlerRegistry(RegistryType):
    """Adds a handler registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_handler_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvHeatSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a heat series to a plot.

    Args:
        * x (Any): rows (int):.

        * cols (int): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * scale_min (float, optional): Sets the color scale min. Typically paired with the
        color scale widget scale_min.

        * scale_max (float, optional): Sets the color scale max. Typically paired with the
        color scale widget scale_max.

        * bounds_min (Any, optional): bounds_max (Any, optional):.

        * format (str, optional): contribute_to_bounds (bool, optional):.

    Command: `dearpygui.add_heat_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    scale_min: Property[float] = ...
    scale_max: Property[float] = ...
    bounds_min: Property[Any] = ...
    bounds_max: Property[Any] = ...
    format: Property[str] = ...
    contribute_to_bounds: Property[bool] = ...
    def __init__(self, x: Sequence[float], rows: int, cols: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., scale_min: float = ..., scale_max: float = ..., bounds_min: Any = ..., bounds_max: Any = ..., format: str = ..., contribute_to_bounds: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], rows: int, cols: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., scale_min: float = ..., scale_max: float = ..., bounds_min: Any = ..., bounds_max: Any = ..., format: str = ..., contribute_to_bounds: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'scale_min', 'scale_max', 'bounds_min', 'bounds_max', 'format', 'contribute_to_bounds'], Any]: ...


class mvHistogramSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a histogram series to a plot.

    Args:
        * x (Any): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * bins (int, optional): bar_scale (float, optional):.

        * min_range (float, optional): max_range (float, optional):.

        * cumlative (bool, optional): density (bool, optional):.

        * outliers (bool, optional): contribute_to_bounds (bool, optional):.

    Command: `dearpygui.add_histogram_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    bins: Property[int] = ...
    bar_scale: Property[float] = ...
    min_range: Property[float] = ...
    max_range: Property[float] = ...
    cumlative: Property[bool] = ...
    density: Property[bool] = ...
    outliers: Property[bool] = ...
    contribute_to_bounds: Property[bool] = ...
    def __init__(self, x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., bins: int = ..., bar_scale: float = ..., min_range: float = ..., max_range: float = ..., cumlative: bool = ..., density: bool = ..., outliers: bool = ..., contribute_to_bounds: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., bins: int = ..., bar_scale: float = ..., min_range: float = ..., max_range: float = ..., cumlative: bool = ..., density: bool = ..., outliers: bool = ..., contribute_to_bounds: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'bins', 'bar_scale', 'min_range', 'max_range', 'cumlative', 'density', 'outliers', 'contribute_to_bounds'], Any]: ...


class mvHoverHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a hover handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_hover_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvImage(SupportsSized, BasicType):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture
    coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0)
    for texture coordinates will generally display the entire texture.

    Args:
        * texture_tag (int | str): The texture_tag should come from a texture that was added
        to a texture registry.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * tint_color (Sequence[float], optional): Applies a color tint to the entire
        texture.

        * border_color (Sequence[float], optional): Displays a border of the specified color
        around the texture. If the theme style has turned off the border it will not be
        shown.

        * uv_min (Sequence[float], optional): Normalized texture coordinates min point.

        * uv_max (Sequence[float], optional): Normalized texture coordinates max point.

    Command: `dearpygui.add_image`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    tint_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    border_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    uv_min: Property[Sequence[float]] = ...
    uv_max: Property[Sequence[float]] = ...
    def __init__(self, texture_tag: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ..., border_color: tuple[int, int, int, int | None] | list[int] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ...) -> None: ...
    @staticmethod
    def command(texture_tag: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ..., border_color: tuple[int, int, int, int | None] | list[int] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'tint_color', 'border_color', 'uv_min', 'uv_max'], Any]: ...


class mvImageButton(SupportsSized, SupportsCallback, BasicType):
    """Adds an button with a texture. uv_min and uv_max represent the normalized texture
    coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0)
    texture coordinates will generally display the entire texture.

    Args:
        * texture_tag (int | str): The texture_tag should come from a texture that was added
        to a texture registry.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * frame_padding (int, optional): Empty space around the outside of the texture.
        Button will show around the texture.

        * tint_color (Sequence[float], optional): Applies a color tint to the entire
        texture.

        * background_color (Sequence[float], optional): Displays a border of the specified
        color around the texture.

        * uv_min (Sequence[float], optional): Normalized texture coordinates min point.

        * uv_max (Sequence[float], optional): Normalized texture coordinates max point.

    Command: `dearpygui.add_image_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    frame_padding: Property[int] = ...
    tint_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    background_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    uv_min: Property[Sequence[float]] = ...
    uv_max: Property[Sequence[float]] = ...
    def __init__(self, texture_tag: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., frame_padding: int = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ..., background_color: tuple[int, int, int, int | None] | list[int] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ...) -> None: ...
    @staticmethod
    def command(texture_tag: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., frame_padding: int = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ..., background_color: tuple[int, int, int, int | None] | list[int] = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'frame_padding', 'tint_color', 'background_color', 'uv_min', 'uv_max'], Any]: ...


class mvImageSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an image series to a plot.

    Args:
        * texture_tag (int | str): bounds_min (Any):.

        * bounds_max (Any): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * uv_min (Sequence[float], optional): normalized texture coordinates.

        * uv_max (Sequence[float], optional): normalized texture coordinates.

    Command: `dearpygui.add_image_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    uv_min: Property[Sequence[float]] = ...
    uv_max: Property[Sequence[float]] = ...
    tint_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    def __init__(self, texture_tag: 'Item', bounds_min: Sequence[float], bounds_max: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ...) -> None: ...
    @staticmethod
    def command(texture_tag: 'Item', bounds_min: Sequence[float], bounds_max: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., uv_min: Sequence[float] = ..., uv_max: Sequence[float] = ..., tint_color: tuple[int, int, int, int | None] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'uv_min', 'uv_max', 'tint_color'], Any]: ...


class mvInputDouble(SupportsCallback, BasicType):
    """Adds input for an double. Useful when input float is not accurate enough. +/- buttons can be
    activated by setting the value of step.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

        * min_value (float, optional): Value for lower limit of input. By default this
        limits the step buttons. Use min_clamped to limit manual input.

        * max_value (float, optional): Value for upper limit of input. By default this
        limits the step buttons. Use max_clamped to limit manual input.

        * step (float, optional): Increment to change value by when the step buttons are
        pressed. Setting this and step_fast to a value of 0 or less will turn off step
        buttons.

        * step_fast (float, optional): Increment to change value by when ctrl + step buttons
        are pressed. Setting this and step to a value of 0 or less will turn off step
        buttons.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_double`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    step: Property[float] = ...
    step_fast: Property[float] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'min_value', 'max_value', 'step', 'step_fast', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputDoubleMulti(SupportsCallback, BasicType):
    """Adds multi double input for up to 4 double values. Useful when input float mulit is not
    accurate enough.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Any, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

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

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_doublex`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    size: Property[int] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'min_value', 'max_value', 'size', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputFloat(SupportsCallback, BasicType):
    """Adds input for an float. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): format (str, optional): Determines the format the
        float will be displayed as use python string formatting.

        * min_value (float, optional): Value for lower limit of input. By default this
        limits the step buttons. Use min_clamped to limit manual input.

        * max_value (float, optional): Value for upper limit of input. By default this
        limits the step buttons. Use max_clamped to limit manual input.

        * step (float, optional): Increment to change value by when the step buttons are
        pressed. Setting this and step_fast to a value of 0 or less will turn off step
        buttons.

        * step_fast (float, optional): Increment to change value by when ctrl + step buttons
        are pressed. Setting this and step to a value of 0 or less will turn off step
        buttons.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter key press.

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_float`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    step: Property[float] = ...
    step_fast: Property[float] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., format: str = ..., min_value: float = ..., max_value: float = ..., step: float = ..., step_fast: float = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'min_value', 'max_value', 'step', 'step_fast', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputFloatMulti(SupportsCallback, BasicType):
    """Adds multi float input for up to 4 float values.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[float], optional): format (str, optional): Determines the
        format the float will be displayed as use python string formatting.

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

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_floatx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    format: Property[str] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    size: Property[int] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., format: str = ..., min_value: float = ..., max_value: float = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'format', 'min_value', 'max_value', 'size', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputInt(SupportsCallback, BasicType):
    """Adds input for an int. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (int, optional): min_value (int, optional): Value for lower limit of
        input. By default this limits the step buttons. Use min_clamped to limit manual
        input.

        * max_value (int, optional): Value for upper limit of input. By default this limits
        the step buttons. Use max_clamped to limit manual input.

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

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_int`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    step: Property[int] = ...
    step_fast: Property[int] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., min_value: int = ..., max_value: int = ..., step: int = ..., step_fast: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., min_value: int = ..., max_value: int = ..., step: int = ..., step_fast: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'min_value', 'max_value', 'step', 'step_fast', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputIntMulti(SupportsCallback, BasicType):
    """Adds multi int input for up to 4 integer values.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[int], optional): min_value (int, optional): Value for
        lower limit of input for each cell. Use min_clamped to turn on.

        * max_value (int, optional): Value for upper limit of input for each cell. Use
        max_clamped to turn on.

        * size (int, optional): Number of components displayed for input.

        * min_clamped (bool, optional): Activates and deactivates the enforcment of
        min_value.

        * max_clamped (bool, optional): Activates and deactivates the enforcment of
        max_value.

        * on_enter (bool, optional): Only runs callback on enter.

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

    Command: `dearpygui.add_input_intx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    size: Property[int] = ...
    min_clamped: Property[bool] = ...
    max_clamped: Property[bool] = ...
    on_enter: Property[bool] = ...
    readonly: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., min_value: int = ..., max_value: int = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., min_value: int = ..., max_value: int = ..., size: int = ..., min_clamped: bool = ..., max_clamped: bool = ..., on_enter: bool = ..., readonly: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'min_value', 'max_value', 'size', 'min_clamped', 'max_clamped', 'on_enter', 'readonly'], Any]: ...


class mvInputText(SupportsSized, SupportsCallback, BasicType):
    """Adds input for text.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (str, optional): hint (str, optional): Displayed only when value is
        an empty string. Will reappear if input value is set to empty string. Will not show
        if default value is anything other than default empty string.

        * multiline (bool, optional): Allows for multiline text input.

        * no_spaces (bool, optional): Filter out spaces and tabs.

        * uppercase (bool, optional): Automatically make all inputs uppercase.

        * tab_input (bool, optional): Allows tabs to be input into the string value instead
        of changing item focus.

        * decimal (bool, optional): Only allow characters 0123456789.+-*/.

        * hexadecimal (bool, optional): Only allow characters 0123456789ABCDEFabcdef.

        * readonly (bool, optional): Activates read only mode where no text can be input but
        text can still be highlighted.

        * password (bool, optional): Display all input characters as '*'.

        * scientific (bool, optional): Only allow characters 0123456789.+-*/eE (Scientific
        notation input).

        * on_enter (bool, optional): Only runs callback on enter key press.

    Command: `dearpygui.add_input_text`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    hint: Property[str] = ...
    multiline: Property[bool] = ...
    no_spaces: Property[bool] = ...
    uppercase: Property[bool] = ...
    tab_input: Property[bool] = ...
    decimal: Property[bool] = ...
    hexadecimal: Property[bool] = ...
    readonly: Property[bool] = ...
    password: Property[bool] = ...
    scientific: Property[bool] = ...
    on_enter: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., hint: str = ..., multiline: bool = ..., no_spaces: bool = ..., uppercase: bool = ..., tab_input: bool = ..., decimal: bool = ..., hexadecimal: bool = ..., readonly: bool = ..., password: bool = ..., scientific: bool = ..., on_enter: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., hint: str = ..., multiline: bool = ..., no_spaces: bool = ..., uppercase: bool = ..., tab_input: bool = ..., decimal: bool = ..., hexadecimal: bool = ..., readonly: bool = ..., password: bool = ..., scientific: bool = ..., on_enter: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'hint', 'multiline', 'no_spaces', 'uppercase', 'tab_input', 'decimal', 'hexadecimal', 'readonly', 'password', 'scientific', 'on_enter'], Any]: ...


class mvInt4Value(BasicType):
    """Adds a int4 value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Sequence[int], optional): parent (int | str, optional): Parent to
        add this item to. (runtime adding).

    Command: `dearpygui.add_int4_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvIntValue(BasicType):
    """Adds a int value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (int, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_int_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: int = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: int = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvItemHandlerRegistry(RegistryType):
    """Adds an item handler registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_handler_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvKeyDownHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a key down handler.

    Args:
        * key (int, optional): Submits callback for all keys.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_key_down_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvKeyPressHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a key press handler.

    Args:
        * key (int, optional): Submits callback for all keys.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_key_press_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvKeyReleaseHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a key release handler.

    Args:
        * key (int, optional): Submits callback for all keys.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_key_release_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(key: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvKnobFloat(SupportsSized, SupportsCallback, BasicType):
    """Adds a knob that rotates based on change in x mouse position.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): min_value (float, optional): Applies lower limit
        to value.

        * max_value (float, optional): Applies upper limit to value.

    Command: `dearpygui.add_knob_float`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., min_value: float = ..., max_value: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., min_value: float = ..., max_value: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'min_value', 'max_value'], Any]: ...


class mvLabelSeries(PlottingType, BasicType):
    """Adds a label series to a plot.

    Args:
        * x (float): y (float):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * x_offset (int, optional): y_offset (int, optional):.

    Command: `dearpygui.add_text_point`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    x_offset: Property[int] = ...
    y_offset: Property[int] = ...
    vertical: Property[bool] = ...
    def __init__(self, x: float, y: float, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., x_offset: int = ..., y_offset: int = ..., vertical: bool = ...) -> None: ...
    @staticmethod
    def command(x: float, y: float, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., x_offset: int = ..., y_offset: int = ..., vertical: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'x_offset', 'y_offset', 'vertical'], Any]: ...


class mvLineSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a line series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_line_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show'], Any]: ...


class mvListbox(SupportsCallback, BasicType):
    """Adds a listbox. If height is not large enough to show all items a scroll bar will appear.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown in the listbox. Can
        consist of any combination of types. All items will be displayed as strings.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (str, optional): String value of the item that will be selected by
        default.

        * num_items (int, optional): Expands the height of the listbox to show specified
        number of items.

    Command: `dearpygui.add_listbox`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    num_items: Property[int] = ...
    def __init__(self, items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., num_items: int = ...) -> None: ...
    @staticmethod
    def command(items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., num_items: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'num_items'], Any]: ...


class mvLoadingIndicator(SupportsSized, BasicType):
    """Adds a rotating animated loading symbol.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

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

    Command: `dearpygui.add_loading_indicator`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    style: Property[int] = ...
    circle_count: Property[int] = ...
    speed: Property[float] = ...
    radius: Property[float] = ...
    thickness: Property[float] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    secondary_color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., style: int = ..., circle_count: int = ..., speed: float = ..., radius: float = ..., thickness: float = ..., color: tuple[int, int, int, int | None] | list[int] = ..., secondary_color: tuple[int, int, int, int | None] | list[int] = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., style: int = ..., circle_count: int = ..., speed: float = ..., radius: float = ..., thickness: float = ..., color: tuple[int, int, int, int | None] | list[int] = ..., secondary_color: tuple[int, int, int, int | None] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'drop_callback', 'show', 'pos', 'style', 'circle_count', 'speed', 'radius', 'thickness', 'color', 'secondary_color'], Any]: ...


class mvMenu(ContainerType, BasicType):
    """Adds a menu to an existing menu bar.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

    Command: `dearpygui.add_menu`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'drop_callback', 'show', 'enabled', 'filter_key', 'delay_search', 'tracked', 'track_offset'], Any]: ...


class mvMenuBar(ContainerType, BasicType):
    """Adds a menu bar to a window.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Command: `dearpygui.add_menu_bar`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    show: Property[bool] = ...
    delay_search: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'show', 'delay_search'], Any]: ...


class mvMenuItem(SupportsCallback, BasicType):
    """Adds a menu item to an existing menu. Menu items act similar to selectables and has a bool
    value. When placed in a menu the checkmark will reflect its value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (bool, optional): This value also controls the checkmark when shown.

        * shortcut (str, optional): Displays text on the menu item. Typically used to show a
        shortcut key command.

        * check (bool, optional): Displays a checkmark on the menu item when it is selected
        and placed in a menu.

    Command: `dearpygui.add_menu_item`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    shortcut: Property[str] = ...
    check: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., shortcut: str = ..., check: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., shortcut: str = ..., check: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'callback', 'drop_callback', 'show', 'enabled', 'filter_key', 'tracked', 'track_offset', 'shortcut', 'check'], Any]: ...


class mvMouseClickHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_click_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseDoubleClickHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse double click handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_double_click_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseDownHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse down handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_down_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseDragHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse drag handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * threshold (float, optional): The threshold the mouse must be dragged before the
        callback is ran.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_drag_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., threshold: float = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., threshold: float = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseMoveHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse move handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_move_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseReleaseHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse release handler.

    Args:
        * button (int, optional): Submits callback for all mouse buttons.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_release_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(button: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvMouseWheelHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a mouse wheel handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_mouse_wheel_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvNode(NodeType, ContainerType, BasicType):
    """Adds a node to a node editor.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * draggable (bool, optional): Allow node to be draggable.

    Command: `dearpygui.add_node`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    draggable: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., draggable: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., draggable: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'draggable'], Any]: ...


class mvNodeAttribute(NodeType, ContainerType, BasicType):
    """Adds a node attribute to a node.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * attribute_type (int, optional): mvNode_Attr_Input, mvNode_Attr_Output, or
        mvNode_Attr_Static.

        * shape (int, optional): Pin shape.

        * category (str, optional): Category.

    Command: `dearpygui.add_node_attribute`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    attribute_type: Property[int] = ...
    shape: Property[int] = ...
    category: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., attribute_type: int = ..., shape: int = ..., category: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., attribute_type: int = ..., shape: int = ..., category: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'show', 'filter_key', 'tracked', 'track_offset', 'attribute_type', 'shape', 'category'], Any]: ...


class mvNodeEditor(SupportsCallback, NodeEditorType, ContainerType, BasicType):
    """Adds a node editor.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * delink_callback (Callable, optional): Callback ran when a link is detached.

        * menubar (bool, optional): Shows or hides the menubar.

        * minimap (bool, optional): Shows or hides the Minimap. New in 1.6.

        * minimap_location (int, optional): mvNodeMiniMap_Location_* constants. New in 1.6.

    Command: `dearpygui.add_node_editor`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    before: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    delink_callback: Property[Callable | None] = ...
    menubar: Property[bool] = ...
    minimap: Property[bool] = ...
    minimap_location: Property[int] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., delink_callback: Callable | None = ..., menubar: bool = ..., minimap: bool = ..., minimap_location: int = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., delink_callback: Callable | None = ..., menubar: bool = ..., minimap: bool = ..., minimap_location: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'before', 'callback', 'show', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'delink_callback', 'menubar', 'minimap', 'minimap_location'], Any]: ...


class mvNodeLink(NodeType, BasicType):
    """Adds a node link between 2 node attributes.

    Args:
        * attr_1 (int | str): attr_2 (int | str):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_node_link`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, attr_1: 'Item', attr_2: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(attr_1: 'Item', attr_2: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvPieSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an pie series to a plot.

    Args:
        * x (float): y (float):.

        * radius (float): values (Any):.

        * labels (Sequence[str]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * format (str, optional): angle (float, optional):.

    Command: `dearpygui.add_pie_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    format: Property[str] = ...
    angle: Property[float] = ...
    normalize: Property[bool] = ...
    def __init__(self, x: float, y: float, radius: float, values: Sequence[float], labels: Sequence[str], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., format: str = ..., angle: float = ..., normalize: bool = ...) -> None: ...
    @staticmethod
    def command(x: float, y: float, radius: float, values: Sequence[float], labels: Sequence[str], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., format: str = ..., angle: float = ..., normalize: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'format', 'angle', 'normalize'], Any]: ...


class mvPlot(SupportsSized, SupportsCallback, PlotType, ContainerType, BasicType):
    """Adds a plot which is used to hold series, and can be drawn to with draw commands.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * no_title (bool, optional): the plot title will not be displayed.

        * no_menus (bool, optional): the user will not be able to open context menus with
        right-click.

        * no_box_select (bool, optional): the user will not be able to box-select with
        right-click drag.

        * no_mouse_pos (bool, optional): the mouse position, in plot coordinates, will not
        be displayed inside of the plot.

        * no_highlight (bool, optional): plot items will not be highlighted when their
        legend entry is hovered.

        * no_child (bool, optional): a child window region will not be used to capture mouse
        scroll (can boost performance for single ImGui window applications).

        * query (bool, optional): the user will be able to draw query rects with middle -
        mouse or CTRL + right - click drag.

        * crosshairs (bool, optional): the default mouse cursor will be replaced with a
        crosshair when hovered.

        * anti_aliased (bool, optional): plot lines will be software anti-aliased (not
        recommended for high density plots, prefer MSAA).

        * equal_aspects (bool, optional): primary x and y axes will be constrained to have
        the same units/pixel (does not apply to auxiliary y-axes).

        * use_local_time (bool, optional): axis labels will be formatted for your timezone
        when.

        * use_ISO8601 (bool, optional): dates will be formatted according to ISO 8601 where
        applicable (e.g. YYYY-MM-DD, YYYY-MM, --MM-DD, etc.).

        * use_24hour_clock (bool, optional): times will be formatted using a 24 hour clock.

        * pan_button (int, optional): enables panning when held.

        * pan_mod (int, optional): optional modifier that must be held for panning.

        * fit_button (int, optional): fits visible data when double clicked.

        * context_menu_button (int, optional): opens plot context menu (if enabled) when
        clicked.

        * box_select_button (int, optional): begins box selection when pressed and confirms
        selection when released.

        * box_select_mod (int, optional): begins box selection when pressed and confirms
        selection when released.

        * box_select_cancel_button (int, optional): cancels active box selection when
        pressed.

        * query_button (int, optional): begins query selection when pressed and end query
        selection when released.

        * query_mod (int, optional): optional modifier that must be held for query
        selection.

        * query_toggle_mod (int, optional): when held, active box selections turn into
        queries.

        * horizontal_mod (int, optional): expands active box selection/query horizontally to
        plot edge when held.

        * vertical_mod (int, optional): expands active box selection/query vertically to
        plot edge when held.

    Command: `dearpygui.add_plot`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    no_title: Property[bool] = ...
    no_menus: Property[bool] = ...
    no_box_select: Property[bool] = ...
    no_mouse_pos: Property[bool] = ...
    no_highlight: Property[bool] = ...
    no_child: Property[bool] = ...
    query: Property[bool] = ...
    crosshairs: Property[bool] = ...
    anti_aliased: Property[bool] = ...
    equal_aspects: Property[bool] = ...
    use_local_time: Property[bool] = ...
    use_ISO8601: Property[bool] = ...
    use_24hour_clock: Property[bool] = ...
    pan_button: Property[int] = ...
    pan_mod: Property[int] = ...
    fit_button: Property[int] = ...
    context_menu_button: Property[int] = ...
    box_select_button: Property[int] = ...
    box_select_mod: Property[int] = ...
    box_select_cancel_button: Property[int] = ...
    query_button: Property[int] = ...
    query_mod: Property[int] = ...
    query_toggle_mod: Property[int] = ...
    horizontal_mod: Property[int] = ...
    vertical_mod: Property[int] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., no_title: bool = ..., no_menus: bool = ..., no_box_select: bool = ..., no_mouse_pos: bool = ..., no_highlight: bool = ..., no_child: bool = ..., query: bool = ..., crosshairs: bool = ..., anti_aliased: bool = ..., equal_aspects: bool = ..., use_local_time: bool = ..., use_ISO8601: bool = ..., use_24hour_clock: bool = ..., pan_button: int = ..., pan_mod: int = ..., fit_button: int = ..., context_menu_button: int = ..., box_select_button: int = ..., box_select_mod: int = ..., box_select_cancel_button: int = ..., query_button: int = ..., query_mod: int = ..., query_toggle_mod: int = ..., horizontal_mod: int = ..., vertical_mod: int = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., no_title: bool = ..., no_menus: bool = ..., no_box_select: bool = ..., no_mouse_pos: bool = ..., no_highlight: bool = ..., no_child: bool = ..., query: bool = ..., crosshairs: bool = ..., anti_aliased: bool = ..., equal_aspects: bool = ..., use_local_time: bool = ..., use_ISO8601: bool = ..., use_24hour_clock: bool = ..., pan_button: int = ..., pan_mod: int = ..., fit_button: int = ..., context_menu_button: int = ..., box_select_button: int = ..., box_select_mod: int = ..., box_select_cancel_button: int = ..., query_button: int = ..., query_mod: int = ..., query_toggle_mod: int = ..., horizontal_mod: int = ..., vertical_mod: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'no_title', 'no_menus', 'no_box_select', 'no_mouse_pos', 'no_highlight', 'no_child', 'query', 'crosshairs', 'anti_aliased', 'equal_aspects', 'use_local_time', 'use_ISO8601', 'use_24hour_clock', 'pan_button', 'pan_mod', 'fit_button', 'context_menu_button', 'box_select_button', 'box_select_mod', 'box_select_cancel_button', 'query_button', 'query_mod', 'query_toggle_mod', 'horizontal_mod', 'vertical_mod'], Any]: ...


class mvPlotAxis(PlotAxisType, ContainerType, BasicType):
    """Adds an axis to a plot.

    Args:
        * axis (int): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * no_gridlines (bool, optional): no_tick_marks (bool, optional):.

        * no_tick_labels (bool, optional): log_scale (bool, optional):.

        * invert (bool, optional): lock_min (bool, optional):.

        * lock_max (bool, optional): time (bool, optional):.

    Command: `dearpygui.add_plot_axis`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    no_gridlines: Property[bool] = ...
    no_tick_marks: Property[bool] = ...
    no_tick_labels: Property[bool] = ...
    log_scale: Property[bool] = ...
    invert: Property[bool] = ...
    lock_min: Property[bool] = ...
    lock_max: Property[bool] = ...
    time: Property[bool] = ...
    def __init__(self, axis: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., no_gridlines: bool = ..., no_tick_marks: bool = ..., no_tick_labels: bool = ..., log_scale: bool = ..., invert: bool = ..., lock_min: bool = ..., lock_max: bool = ..., time: bool = ...) -> None: ...
    @staticmethod
    def command(axis: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., no_gridlines: bool = ..., no_tick_marks: bool = ..., no_tick_labels: bool = ..., log_scale: bool = ..., invert: bool = ..., lock_min: bool = ..., lock_max: bool = ..., time: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'payload_type', 'drop_callback', 'show', 'no_gridlines', 'no_tick_marks', 'no_tick_labels', 'log_scale', 'invert', 'lock_min', 'lock_max', 'time'], Any]: ...


class mvPlotLegend(PlottingType, BasicType):
    """Adds a plot legend to a plot.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * location (int, optional): location, mvPlot_Location_*.

        * horizontal (bool, optional): outside (bool, optional):.

    Command: `dearpygui.add_plot_legend`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    location: Property[int] = ...
    horizontal: Property[bool] = ...
    outside: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., location: int = ..., horizontal: bool = ..., outside: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., location: int = ..., horizontal: bool = ..., outside: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'payload_type', 'drop_callback', 'show', 'location', 'horizontal', 'outside'], Any]: ...


class mvProgressBar(SupportsSized, BasicType):
    """Adds a progress bar.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * overlay (str, optional): Overlayed text onto the bar that typically used to
        display the value of the progress.

        * default_value (float, optional): Normalized value to fill the bar from 0.0 to 1.0.

    Command: `dearpygui.add_progress_bar`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    overlay: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., overlay: str = ..., default_value: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., overlay: str = ..., default_value: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'overlay'], Any]: ...


class mvRadioButton(SupportsCallback, BasicType):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.

    Args:
        * items (Sequence[str], optional): A tuple of items to be shown as radio options.
        Can consist of any combination of types. All types will be shown as strings.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (str, optional): Default selected radio option. Set by using the
        string value of the item.

        * horizontal (bool, optional): Displays the radio options horizontally.

    Command: `dearpygui.add_radio_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    horizontal: Property[bool] = ...
    def __init__(self, items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., horizontal: bool = ...) -> None: ...
    @staticmethod
    def command(items: Sequence[str] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: str = ..., horizontal: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'horizontal'], Any]: ...


class mvRawTexture(BasicType):
    """Adds a raw texture.

    Args:
        * width (int): Horizontal size of the item in pixels. Setting this value may
        override auto-scaling options for some items; this can be reversed by setting this
        back to 0. Note that the value is interpreted as unsigned.

        * default_value (Sequence[float]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * format (int, optional): Data format.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_raw_texture`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    format: Property[int] = ...
    def __init__(self, width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., format: int = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., format: int = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'format'], Any]: ...


class mvResizeHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a resize handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_resize_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvScatterSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a scatter series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_scatter_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show'], Any]: ...


class mvSelectable(SupportsSized, SupportsCallback, BasicType):
    """Adds a selectable. Similar to a button but can indicate its selected state.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (bool, optional): span_columns (bool, optional): Forces the
        selectable to span the width of all columns if placed in a table.

        * disable_popup_close (bool, optional): Disable closing a modal or popup window.

    Command: `dearpygui.add_selectable`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    span_columns: Property[bool] = ...
    disable_popup_close: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., span_columns: bool = ..., disable_popup_close: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: bool = ..., span_columns: bool = ..., disable_popup_close: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'span_columns', 'disable_popup_close'], Any]: ...


class mvSeparator(BasicType):
    """Adds a horizontal line separator.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

    Command: `dearpygui.add_separator`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'show', 'pos'], Any]: ...


class mvSeriesValue(SupportsValueArray, PlottingType, BasicType):
    """Adds a plot series value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (Any, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_series_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Any = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: Any = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvShadeSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a shade series to a plot.

    Args:
        * x (Any): y1 (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_shade_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    y2: Property[Any] = ...
    def __init__(self, x: Sequence[float], y1: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., y2: Any = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y1: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ..., y2: Any = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show', 'y2'], Any]: ...


class mvSimplePlot(PlottingType, BasicType):
    """Adds a simple plot for visualization of a 1 dimensional set of values.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[float], optional): overlay (str, optional): overlays text
        (similar to a plot title).

        * histogram (bool, optional): autosize (bool, optional):.

        * min_scale (float, optional): max_scale (float, optional):.

    Command: `dearpygui.add_simple_plot`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    overlay: Property[str] = ...
    histogram: Property[bool] = ...
    autosize: Property[bool] = ...
    min_scale: Property[float] = ...
    max_scale: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., overlay: str = ..., histogram: bool = ..., autosize: bool = ..., min_scale: float = ..., max_scale: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., overlay: str = ..., histogram: bool = ..., autosize: bool = ..., min_scale: float = ..., max_scale: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'filter_key', 'tracked', 'track_offset', 'overlay', 'histogram', 'autosize', 'min_scale', 'max_scale'], Any]: ...


class mvSlider3D(SupportsSized, SupportsCallback, BasicType):
    """Adds a 3D box slider.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[float], optional): max_x (float, optional): Applies upper
        limit to slider.

        * max_y (float, optional): Applies upper limit to slider.

        * max_z (float, optional): Applies upper limit to slider.

        * min_x (float, optional): Applies lower limit to slider.

        * min_y (float, optional): Applies lower limit to slider.

        * min_z (float, optional): Applies lower limit to slider.

        * scale (float, optional): Size of the widget.

    Command: `dearpygui.add_3d_slider`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    max_x: Property[float] = ...
    max_y: Property[float] = ...
    max_z: Property[float] = ...
    min_x: Property[float] = ...
    min_y: Property[float] = ...
    min_z: Property[float] = ...
    scale: Property[float] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., max_x: float = ..., max_y: float = ..., max_z: float = ..., min_x: float = ..., min_y: float = ..., min_z: float = ..., scale: float = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., max_x: float = ..., max_y: float = ..., max_z: float = ..., min_x: float = ..., min_y: float = ..., min_z: float = ..., scale: float = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'max_x', 'max_y', 'max_z', 'min_x', 'min_y', 'min_z', 'scale'], Any]: ...


class mvSliderDouble(SupportsSized, SupportsCallback, BasicType):
    """Adds slider for a single double value. Useful when slider float is not accurate enough.
    Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft
    limit for the slider. Use clamped keyword to also apply limits to the direct entry
    modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): vertical (bool, optional): Sets orientation of
        the slidebar and slider to vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_double`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    vertical: Property[bool] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'vertical', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSliderDoubleMulti(SupportsCallback, BasicType):
    """Adds multi slider for up to 4 double values. Usueful for when multi slide float is not
    accurate enough. Directly entry can be done with double click or CTRL+Click. Min and Max
    alone are a soft limit for the slider. Use clamped keyword to also apply limits to the
    direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Any, optional): size (int, optional): Number of doubles to be
        displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_doublex`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Any = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSliderFloat(SupportsSized, SupportsCallback, BasicType):
    """Adds slider for a single float value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (float, optional): vertical (bool, optional): Sets orientation of
        the slidebar and slider to vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the float will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_float`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    vertical: Property[bool] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: float = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'vertical', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSliderFloatMulti(SupportsCallback, BasicType):
    """Adds multi slider for up to 4 float values. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[float], optional): size (int, optional): Number of floats
        to be displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (float, optional): Applies a limit only to sliding entry only.

        * max_value (float, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_floatx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[float] = ...
    max_value: Property[float] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: Sequence[float] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: float = ..., max_value: float = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSliderInt(SupportsSized, SupportsCallback, BasicType):
    """Adds slider for a single int value. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (int, optional): vertical (bool, optional): Sets orientation of the
        slidebar and slider to vertical.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (int, optional): Applies a limit only to sliding entry only.

        * max_value (int, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_int`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    vertical: Property[bool] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: int = ..., vertical: bool = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'vertical', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSliderIntMulti(SupportsCallback, BasicType):
    """Adds multi slider for up to 4 int values. Directly entry can be done with double click or
    CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to
    also apply limits to the direct entry modes.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (Sequence[int], optional): size (int, optional): Number of ints to
        be displayed.

        * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click
        or Enter key allowing to input text directly into the item.

        * clamped (bool, optional): Applies the min and max limits to direct entry methods
        also such as double click and CTRL+Click.

        * min_value (int, optional): Applies a limit only to sliding entry only.

        * max_value (int, optional): Applies a limit only to sliding entry only.

        * format (str, optional): Determines the format the int will be displayed as use
        python string formatting.

    Command: `dearpygui.add_slider_intx`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    size: Property[int] = ...
    no_input: Property[bool] = ...
    clamped: Property[bool] = ...
    min_value: Property[int] = ...
    max_value: Property[int] = ...
    format: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., enabled: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: tuple[int, int, int, int | None] | list[int] = ..., size: int = ..., no_input: bool = ..., clamped: bool = ..., min_value: int = ..., max_value: int = ..., format: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'indent', 'before', 'source', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'enabled', 'pos', 'filter_key', 'tracked', 'track_offset', 'size', 'no_input', 'clamped', 'min_value', 'max_value', 'format'], Any]: ...


class mvSpacer(SupportsSized, BasicType):
    """Adds a spacer item that can be used to help with layouts or can be used as a placeholder
    item.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

    Command: `dearpygui.add_spacer`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'show', 'pos'], Any]: ...


class mvStage(RootType):
    """Adds a stage.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

    Command: `dearpygui.add_stage`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvStairSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a stair series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_stair_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show'], Any]: ...


class mvStaticTexture(BasicType):
    """Adds a static texture.

    Args:
        * width (int): Horizontal size of the item in pixels. Setting this value may
        override auto-scaling options for some items; this can be reversed by setting this
        back to 0. Note that the value is interpreted as unsigned.

        * default_value (Sequence[float]): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

    Command: `dearpygui.add_static_texture`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(width: int, height: int, default_value: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvStemSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds a stem series to a plot.

    Args:
        * x (Any): y (Any):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_stem_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], y: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'source', 'show'], Any]: ...


class mvStringValue(BasicType):
    """Adds a string value.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * default_value (str, optional): parent (int | str, optional): Parent to add this
        item to. (runtime adding).

    Command: `dearpygui.add_string_value`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    source: Property['Item'] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: str = ..., parent: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., source: 'Item' = ..., default_value: str = ..., parent: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'source'], Any]: ...


class mvSubPlots(SupportsSized, SupportsCallback, PlottingType, ContainerType, BasicType):
    """Adds a collection of plots.

    Args:
        * rows (int): columns (int):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * row_ratios (Sequence[float], optional): column_ratios (Sequence[float],
        optional):.

        * no_title (bool, optional): no_menus (bool, optional): the user will not be able to
        open context menus with right-click.

        * no_resize (bool, optional): resize splitters between subplot cells will be not be
        provided.

        * no_align (bool, optional): subplot edges will not be aligned vertically or
        horizontally.

        * link_rows (bool, optional): link the y-axis limits of all plots in each row (does
        not apply auxiliary y-axes).

        * link_columns (bool, optional): link the x-axis limits of all plots in each column.

        * link_all_x (bool, optional): link the x-axis limits in every plot in the subplot.

        * link_all_y (bool, optional): link the y-axis limits in every plot in the subplot
        (does not apply to auxiliary y-axes).

        * column_major (bool, optional): subplots are added in column major order instead of
        the default row major order.

    Command: `dearpygui.add_subplots`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    row_ratios: Property[Sequence[float]] = ...
    column_ratios: Property[Sequence[float]] = ...
    no_title: Property[bool] = ...
    no_menus: Property[bool] = ...
    no_resize: Property[bool] = ...
    no_align: Property[bool] = ...
    link_rows: Property[bool] = ...
    link_columns: Property[bool] = ...
    link_all_x: Property[bool] = ...
    link_all_y: Property[bool] = ...
    column_major: Property[bool] = ...
    def __init__(self, rows: int, columns: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., row_ratios: Sequence[float] = ..., column_ratios: Sequence[float] = ..., no_title: bool = ..., no_menus: bool = ..., no_resize: bool = ..., no_align: bool = ..., link_rows: bool = ..., link_columns: bool = ..., link_all_x: bool = ..., link_all_y: bool = ..., column_major: bool = ...) -> None: ...
    @staticmethod
    def command(rows: int, columns: int, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., row_ratios: Sequence[float] = ..., column_ratios: Sequence[float] = ..., no_title: bool = ..., no_menus: bool = ..., no_resize: bool = ..., no_align: bool = ..., link_rows: bool = ..., link_columns: bool = ..., link_all_x: bool = ..., link_all_y: bool = ..., column_major: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'row_ratios', 'column_ratios', 'no_title', 'no_menus', 'no_resize', 'no_align', 'link_rows', 'link_columns', 'link_all_x', 'link_all_y', 'column_major'], Any]: ...


class mvTab(ContainerType, BasicType):
    """Adds a tab to a tab bar.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * closable (bool, optional): Creates a button on the tab that can hide the tab.

        * no_tooltip (bool, optional): Disable tooltip for the given tab.

        * order_mode (bool, optional): set using a constant: mvTabOrder_Reorderable: allows
        reordering, mvTabOrder_Fixed: fixed ordering, mvTabOrder_Leading: adds tab to front,
        mvTabOrder_Trailing: adds tab to back.

    Command: `dearpygui.add_tab`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    closable: Property[bool] = ...
    no_tooltip: Property[bool] = ...
    order_mode: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., no_tooltip: bool = ..., order_mode: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., closable: bool = ..., no_tooltip: bool = ..., order_mode: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'drop_callback', 'show', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'closable', 'no_tooltip', 'order_mode'], Any]: ...


class mvTabBar(SupportsCallback, ContainerType, BasicType):
    """Adds a tab bar.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * reorderable (bool, optional): Allows for the user to change the order of the tabs.

    Command: `dearpygui.add_tab_bar`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    reorderable: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., reorderable: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., reorderable: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'reorderable'], Any]: ...


class mvTabButton(SupportsCallback, BasicType):
    """Adds a tab button to a tab bar.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * no_reorder (bool, optional): Disable reordering this tab or having another tab
        cross over this tab. Fixes the position of this tab in relation to the order of
        neighboring tabs at start.

        * leading (bool, optional): Enforce the tab position to the left of the tab bar
        (after the tab list popup button).

        * trailing (bool, optional): Enforce the tab position to the right of the tab bar
        (before the scrolling buttons).

        * no_tooltip (bool, optional): Disable tooltip for the given tab.

    Command: `dearpygui.add_tab_button`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    no_reorder: Property[bool] = ...
    leading: Property[bool] = ...
    trailing: Property[bool] = ...
    no_tooltip: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_reorder: bool = ..., leading: bool = ..., trailing: bool = ..., no_tooltip: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., no_reorder: bool = ..., leading: bool = ..., trailing: bool = ..., no_tooltip: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'filter_key', 'tracked', 'track_offset', 'no_reorder', 'leading', 'trailing', 'no_tooltip'], Any]: ...


class mvTable(SupportsSized, SupportsCallback, TableItemType, ContainerType, BasicType):
    """Adds a table.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * header_row (bool, optional): show headers at the top of the columns.

        * clipper (bool, optional): Use clipper (rows must be same height).

        * inner_width (int, optional): policy (int, optional):.

        * freeze_rows (int, optional): freeze_columns (int, optional):.

        * sort_multi (bool, optional): Hold shift when clicking headers to sort on multiple
        column.

        * sort_tristate (bool, optional): Allow no sorting, disable default sorting.

        * resizable (bool, optional): Enable resizing columns.

        * reorderable (bool, optional): Enable reordering columns in header row (need
        calling TableSetupColumn() + TableHeadersRow() to display headers).

        * hideable (bool, optional): Enable hiding/disabling columns in context menu.

        * sortable (bool, optional): Enable sorting. Call TableGetSortSpecs() to obtain sort
        specs. Also see ImGuiTableFlags_SortMulti and ImGuiTableFlags_SortTristate.

        * context_menu_in_body (bool, optional): Right-click on columns body/contents will
        display table context menu. By default it is available in TableHeadersRow().

        * row_background (bool, optional): Set each RowBg color with ImGuiCol_TableRowBg or
        ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with
        ImGuiTableBgFlags_RowBg0 on each row manually).

        * borders_innerH (bool, optional): Draw horizontal borders between rows.

        * borders_outerH (bool, optional): Draw horizontal borders at the top and bottom.

        * borders_innerV (bool, optional): Draw vertical borders between columns.

        * borders_outerV (bool, optional): Draw vertical borders on the left and right
        sides.

        * no_host_extendX (bool, optional): Make outer width auto-fit to columns, overriding
        outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch
        columns are not used.

        * no_host_extendY (bool, optional): Make outer height stop exactly at outer_size.y
        (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY
        are disabled. Data below the limit will be clipped and not visible.

        * no_keep_columns_visible (bool, optional): Disable keeping column always minimally
        visible when ScrollX is off and table gets too small. Not recommended if columns are
        resizable.

        * precise_widths (bool, optional): Disable distributing remainder width to stretched
        columns (width allocation on a 100-wide table with 3 columns: Without this flag:
        33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will
        appear to be less smooth.

        * no_clip (bool, optional): Disable clipping rectangle for every individual columns.

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

        * no_saved_settings (bool, optional): Never load/save settings in .ini file.

    Command: `dearpygui.add_table`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    header_row: Property[bool] = ...
    clipper: Property[bool] = ...
    inner_width: Property[int] = ...
    policy: Property[int] = ...
    freeze_rows: Property[int] = ...
    freeze_columns: Property[int] = ...
    sort_multi: Property[bool] = ...
    sort_tristate: Property[bool] = ...
    resizable: Property[bool] = ...
    reorderable: Property[bool] = ...
    hideable: Property[bool] = ...
    sortable: Property[bool] = ...
    context_menu_in_body: Property[bool] = ...
    row_background: Property[bool] = ...
    borders_innerH: Property[bool] = ...
    borders_outerH: Property[bool] = ...
    borders_innerV: Property[bool] = ...
    borders_outerV: Property[bool] = ...
    no_host_extendX: Property[bool] = ...
    no_host_extendY: Property[bool] = ...
    no_keep_columns_visible: Property[bool] = ...
    precise_widths: Property[bool] = ...
    no_clip: Property[bool] = ...
    pad_outerX: Property[bool] = ...
    no_pad_outerX: Property[bool] = ...
    no_pad_innerX: Property[bool] = ...
    scrollX: Property[bool] = ...
    scrollY: Property[bool] = ...
    no_saved_settings: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., header_row: bool = ..., clipper: bool = ..., inner_width: int = ..., policy: int = ..., freeze_rows: int = ..., freeze_columns: int = ..., sort_multi: bool = ..., sort_tristate: bool = ..., resizable: bool = ..., reorderable: bool = ..., hideable: bool = ..., sortable: bool = ..., context_menu_in_body: bool = ..., row_background: bool = ..., borders_innerH: bool = ..., borders_outerH: bool = ..., borders_innerV: bool = ..., borders_outerV: bool = ..., no_host_extendX: bool = ..., no_host_extendY: bool = ..., no_keep_columns_visible: bool = ..., precise_widths: bool = ..., no_clip: bool = ..., pad_outerX: bool = ..., no_pad_outerX: bool = ..., no_pad_innerX: bool = ..., scrollX: bool = ..., scrollY: bool = ..., no_saved_settings: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., header_row: bool = ..., clipper: bool = ..., inner_width: int = ..., policy: int = ..., freeze_rows: int = ..., freeze_columns: int = ..., sort_multi: bool = ..., sort_tristate: bool = ..., resizable: bool = ..., reorderable: bool = ..., hideable: bool = ..., sortable: bool = ..., context_menu_in_body: bool = ..., row_background: bool = ..., borders_innerH: bool = ..., borders_outerH: bool = ..., borders_innerV: bool = ..., borders_outerV: bool = ..., no_host_extendX: bool = ..., no_host_extendY: bool = ..., no_keep_columns_visible: bool = ..., precise_widths: bool = ..., no_clip: bool = ..., pad_outerX: bool = ..., no_pad_outerX: bool = ..., no_pad_innerX: bool = ..., scrollX: bool = ..., scrollY: bool = ..., no_saved_settings: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'before', 'source', 'callback', 'show', 'pos', 'filter_key', 'delay_search', 'header_row', 'clipper', 'inner_width', 'policy', 'freeze_rows', 'freeze_columns', 'sort_multi', 'sort_tristate', 'resizable', 'reorderable', 'hideable', 'sortable', 'context_menu_in_body', 'row_background', 'borders_innerH', 'borders_outerH', 'borders_innerV', 'borders_outerV', 'no_host_extendX', 'no_host_extendY', 'no_keep_columns_visible', 'precise_widths', 'no_clip', 'pad_outerX', 'no_pad_outerX', 'no_pad_innerX', 'scrollX', 'scrollY', 'no_saved_settings'], Any]: ...


class mvTableCell(TableType, ContainerType, BasicType):
    """Adds a table.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

    Command: `dearpygui.add_table_cell`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    height: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'height', 'before', 'show', 'filter_key'], Any]: ...


class mvTableColumn(TableType, BasicType):
    """Adds a table column.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * enabled (bool, optional): Sets the item's operational state. Setting to False
        disables the item's functionality. An item's operational state also affects which
        elements/components of a theme are applied to it (based off the *enabled_state*
        value of each theme component). This setting does not affect the item's visibility
        state.

        * init_width_or_weight (float, optional): default_hide (bool, optional): Default as
        a hidden/disabled column.

        * default_sort (bool, optional): Default as a sorting column.

        * width_stretch (bool, optional): Column will stretch. Preferable with horizontal
        scrolling disabled (default if table sizing policy is _SizingStretchSame or
        _SizingStretchProp).

        * width_fixed (bool, optional): Column will not stretch. Preferable with horizontal
        scrolling enabled (default if table sizing policy is _SizingFixedFit and table is
        resizable).

        * no_resize (bool, optional): Disable manual resizing.

        * no_reorder (bool, optional): Disable manual reordering this column, this will also
        prevent other columns from crossing over this column.

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

        * prefer_sort_ascending (bool, optional): Make the initial sort direction Ascending
        when first sorting on this column (default).

        * prefer_sort_descending (bool, optional): Make the initial sort direction
        Descending when first sorting on this column.

        * indent_enable (bool, optional): Use current Indent value when entering cell
        (default for column 0).

        * indent_disable (bool, optional): Ignore current Indent value when entering cell
        (default for columns > 0). Indentation changes _within_ the cell will still be
        honored.

    Command: `dearpygui.add_table_column`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    enabled: Property[bool] = ...
    init_width_or_weight: Property[float] = ...
    width_stretch: Property[bool] = ...
    width_fixed: Property[bool] = ...
    no_resize: Property[bool] = ...
    no_reorder: Property[bool] = ...
    no_hide: Property[bool] = ...
    no_clip: Property[bool] = ...
    no_sort: Property[bool] = ...
    no_sort_ascending: Property[bool] = ...
    no_sort_descending: Property[bool] = ...
    no_header_width: Property[bool] = ...
    prefer_sort_ascending: Property[bool] = ...
    prefer_sort_descending: Property[bool] = ...
    indent_enable: Property[bool] = ...
    indent_disable: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., enabled: bool = ..., init_width_or_weight: float = ..., default_hide: bool = ..., default_sort: bool = ..., width_stretch: bool = ..., width_fixed: bool = ..., no_resize: bool = ..., no_reorder: bool = ..., no_hide: bool = ..., no_clip: bool = ..., no_sort: bool = ..., no_sort_ascending: bool = ..., no_sort_descending: bool = ..., no_header_width: bool = ..., prefer_sort_ascending: bool = ..., prefer_sort_descending: bool = ..., indent_enable: bool = ..., indent_disable: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., enabled: bool = ..., init_width_or_weight: float = ..., default_hide: bool = ..., default_sort: bool = ..., width_stretch: bool = ..., width_fixed: bool = ..., no_resize: bool = ..., no_reorder: bool = ..., no_hide: bool = ..., no_clip: bool = ..., no_sort: bool = ..., no_sort_ascending: bool = ..., no_sort_descending: bool = ..., no_header_width: bool = ..., prefer_sort_ascending: bool = ..., prefer_sort_descending: bool = ..., indent_enable: bool = ..., indent_disable: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'before', 'show', 'enabled', 'init_width_or_weight', 'width_stretch', 'width_fixed', 'no_resize', 'no_reorder', 'no_hide', 'no_clip', 'no_sort', 'no_sort_ascending', 'no_sort_descending', 'no_header_width', 'prefer_sort_ascending', 'prefer_sort_descending', 'indent_enable', 'indent_disable'], Any]: ...


class mvTableRow(TableType, ContainerType, BasicType):
    """Adds a table row.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

    Command: `dearpygui.add_table_row`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    height: Property[int] = ...
    before: Property['Item'] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., height: int = ..., parent: 'Item' = ..., before: 'Item' = ..., show: bool = ..., filter_key: str = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'height', 'before', 'show', 'filter_key'], Any]: ...


class mvTemplateRegistry(RegistryType):
    """Adds a template registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

    Command: `dearpygui.add_template_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvText(BasicType):
    """Adds text. Text can have an optional label that will display to the right of the text.

    Args:
        * default_value (str, optional): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * wrap (int, optional): Number of pixels from the start of the item until wrapping
        starts.

        * bullet (bool, optional): Places a bullet to the left of the text.

        * color (Sequence[int], optional): Color of the text (rgba).

        * show_label (bool, optional): Displays the label to the right of the text.

    Command: `dearpygui.add_text`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    wrap: Property[int] = ...
    bullet: Property[bool] = ...
    color: Property[tuple[int, int, int, int | None] | list[int]] = ...
    show_label: Property[bool] = ...
    def __init__(self, default_value: str = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., wrap: int = ..., bullet: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., show_label: bool = ...) -> None: ...
    @staticmethod
    def command(default_value: str = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., wrap: int = ..., bullet: bool = ..., color: tuple[int, int, int, int | None] | list[int] = ..., show_label: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'source', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'wrap', 'bullet', 'color', 'show_label'], Any]: ...


class mvTextureRegistry(RegistryType):
    """Adds a dynamic texture.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_texture_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvTheme(ThemeType, RegistryType):
    """Adds a theme.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

    Command: `dearpygui.add_theme`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvThemeColor(SupportsValueArray, ThemeType, BasicType):
    """Adds a theme color.

    Args:
        * target (int, optional): value (Sequence[int], optional):.

        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots,
        mvThemeCat_Nodes.

    Command: `dearpygui.add_theme_color`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    category: Property[int] = ...
    def __init__(self, target: int = ..., value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., category: int = ...) -> None: ...
    @staticmethod
    def command(target: int = ..., value: tuple[int, int, int, int | None] | list[int] = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., category: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'category'], Any]: ...


class mvThemeComponent(ThemeType, ContainerType, BasicType):
    """Adds a theme component.

    Args:
        * item_type (int, optional): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

    Command: `dearpygui.add_theme_component`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    enabled_state: Property[bool] = ...
    def __init__(self, item_type: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., enabled_state: bool = ...) -> None: ...
    @staticmethod
    def command(item_type: int = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., enabled_state: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'enabled_state'], Any]: ...


class mvThemeStyle(SupportsValueArray, ThemeType, BasicType):
    """Adds a theme style.

    Args:
        * target (int, optional): x (float, optional):.

        * y (float, optional): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * category (int, optional): Options include mvThemeCat_Core, mvThemeCat_Plots,
        mvThemeCat_Nodes.

    Command: `dearpygui.add_theme_style`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    category: Property[int] = ...
    def __init__(self, target: int = ..., x: float = ..., y: float = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., category: int = ...) -> None: ...
    @staticmethod
    def command(target: int = ..., x: float = ..., y: float = ..., *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., category: int = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'category'], Any]: ...


class mvTimePicker(SupportsCallback, BasicType):
    """Adds a time picker.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_value (dict, optional): hour24 (bool, optional): Show 24 hour clock
        instead of 12 hour.

    Command: `dearpygui.add_time_picker`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    callback: Property[Callable | None] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    hour24: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., hour24: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., callback: Callable | None = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., tracked: bool = ..., track_offset: float = ..., default_value: dict = ..., hour24: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'callback', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'tracked', 'track_offset', 'hour24'], Any]: ...


class mvToggledOpenHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a togged open handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_toggled_open_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvTooltip(ContainerType, BasicType):
    """Adds a tooltip window.

    Args:
        * parent (int | str): A reference to an existing item (as a `int` uuid, `str` alias,
        or `int` item interface) that will become this item's parent. If None or 0
        (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_tooltip`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    def __init__(self, parent: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(parent: 'Item', *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show'], Any]: ...


class mvTreeNode(ContainerType, BasicType):
    """Adds a tree node to add items to.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * payload_type (str, optional): Sender string type must be the same as the target
        for the target to run the payload_callback.

        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.

        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * pos (Sequence[int], optional): Places the item relative to window coordinates,
        [0,0] is top left.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * tracked (bool, optional): Enables (True, default) or disables (False) the item's
        ability to be tracked while scrolling.

        * track_offset (float, optional): A numeric value between 0 and 1 that affects item
        tracking while scrolling when *tracked* is True. Common values are 0.0 (top), 0.5
        (center, default), and 1.0 (bottom).

        * default_open (bool, optional): Sets the tree node open by default.

        * open_on_double_click (bool, optional): Need double-click to open node.

        * open_on_arrow (bool, optional): Only open when clicking on the arrow part.

        * leaf (bool, optional): No collapsing, no arrow (use as a convenience for leaf
        nodes).

        * bullet (bool, optional): Display a bullet instead of arrow.

        * selectable (bool, optional): Makes the tree selectable.

    Command: `dearpygui.add_tree_node`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    before: Property['Item'] = ...
    payload_type: Property[str] = ...
    drag_callback: Property[Callable | None] = ...
    drop_callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    tracked: Property[bool] = ...
    track_offset: Property[float] = ...
    open_on_double_click: Property[bool] = ...
    open_on_arrow: Property[bool] = ...
    leaf: Property[bool] = ...
    bullet: Property[bool] = ...
    selectable: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., selectable: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., before: 'Item' = ..., payload_type: str = ..., drag_callback: Callable | None = ..., drop_callback: Callable | None = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., default_open: bool = ..., open_on_double_click: bool = ..., open_on_arrow: bool = ..., leaf: bool = ..., bullet: bool = ..., selectable: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'before', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'pos', 'filter_key', 'delay_search', 'tracked', 'track_offset', 'open_on_double_click', 'open_on_arrow', 'leaf', 'bullet', 'selectable'], Any]: ...


class mvVLineSeries(SupportsValueArray, PlottingType, BasicType):
    """Adds an infinite vertical line series to a plot.

    Args:
        * x (Any): label (str, optional): Overrides 'name' as label.

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * before (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that is parented by the container that will
        soon parent this one. If specified, this item will be inserted into the parent's
        child slot preceding the referenced item. If this value is None or 0 (default), the
        item will be added to the end of the slot.

        * source (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface). If specified, getting or setting this item's
        value will instead get or set the value of the referenced item. If the item normally
        displays its' value, it will instead display the referenced item's value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_vline_series`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    before: Property['Item'] = ...
    source: Property['Item'] = ...
    show: Property[bool] = ...
    def __init__(self, x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(x: Sequence[float], *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., before: 'Item' = ..., source: 'Item' = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'before', 'source', 'show'], Any]: ...


class mvValueRegistry(RegistryType):
    """Adds a value registry.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

    Command: `dearpygui.add_value_registry`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label'], Any]: ...


class mvViewportDrawlist(DrawingType, RootType):
    """A container that is used to present draw items or layers directly to the viewport. By
    default this will draw to the back of the viewport. Layers and draw items should be
    added to this widget as children.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * filter_key (str, optional): The text value of the item that will be used when
        applying filters.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

        * front (bool, optional): Draws to the front of the view port instead of the back.

    Command: `dearpygui.add_viewport_drawlist`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    show: Property[bool] = ...
    filter_key: Property[str] = ...
    delay_search: Property[bool] = ...
    front: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., front: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., show: bool = ..., filter_key: str = ..., delay_search: bool = ..., front: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'show', 'filter_key', 'delay_search', 'front'], Any]: ...


class mvViewportMenuBar(ContainerType, BasicType):
    """Adds a menubar to the viewport.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

        * delay_search (bool, optional): Delays searching container for specified items
        until the end of the app. Possible optimization when a container has many children
        that are not accessed often.

    Command: `dearpygui.add_viewport_menu_bar`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    indent: Property[int] = ...
    show: Property[bool] = ...
    delay_search: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., indent: int = ..., parent: 'Item' = ..., show: bool = ..., delay_search: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'indent', 'show', 'delay_search'], Any]: ...


class mvVisibleHandler(SupportsCallback, HandlerType, BasicType):
    """Adds a visible handler.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * parent (int | str, optional): A reference to an existing item (as a `int` uuid,
        `str` alias, or `int` item interface) that will become this item's parent. If None
        or 0 (default), Dear PyGui will default to using whatever item that is on top of the
        container stack.

        * callback (Callable, optional): Called by Dear PyGui when the item is interacted
        with (usually clicked). Can be None, or any callable with a `__code__` attribute.
        Dear PyGui will send up to three positional arguments to the callback; `sender`
        (`tag` of the item *callback* is registered to), `app_data` (None, or an updated
        value associated with `sender`), and `user_data` (registered *user_data* value of
        `sender`). However, the callback is not required to accept all or any of these
        arguments.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

    Command: `dearpygui.add_item_visible_handler`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    callback: Property[Callable | None] = ...
    show: Property[bool] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., parent: 'Item' = ..., callback: Callable | None = ..., show: bool = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'callback', 'show'], Any]: ...


class mvWindowAppItem(SupportsSized, WindowType, RootType):
    """Creates a new window for following items to be added to.

    Args:
        * label (str, optional): An informal name for the item. Items that are visible in
        the user interface may also use this as their display name. The `"##"` delimiter can
        be used within the label text. If present, only text preceding the first use of this
        delimiter will be shown when displaying the label. You can prevent this behavior by
        escaping the second hash character with a carriage return (`#\\r#`).

        * user_data (Any, optional): Can be set as any value or reference. For items with
        callback-related configuration options, Dear PyGui will send this as the third
        positional argument when invoking the callback(s).

        * use_internal_label (bool, optional): True (default) will append `'##<item_uuid>'`
        to the item's *label* value.

        * tag (int | str, optional): An item reference (as a `int` uuid, `str` alias, or
        `int` item interface) to bind to the interface. If None or 0 (default), or if the
        integer/string value of the reference is new or unused by another item, the
        interface creates a new item of its' type during initialization. If the value is not
        a new binding reference, the interface will (try to) operate on the item with an
        identifier matching that value.

        * width (int, optional): Horizontal size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * height (int, optional): Vertical size of the item in pixels. Setting this value
        may override auto-scaling options for some items; this can be reversed by setting
        this back to 0. Note that the value is interpreted as unsigned.

        * indent (int, optional): Horizontal padding added to the left of the widget.
        Multiplicative with the `mvStyleVar_IndentSpacing` theme style element.

        * show (bool, optional): Setting to True (default) will render the item and allow it
        to be seen, while False does the opposite. For items that cannot be visible in the
        user interface (handlers, registries, etc), the behavior of *show* is similar to
        that of *enabled* where False disables their functionality.

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

        * no_move (bool, optional): Allows for the window's position to be changed or fixed.

        * no_scrollbar (bool, optional): Disable scrollbars. (window can still scroll with
        mouse or programmatically).

        * no_collapse (bool, optional): Disable user collapsing window by double-clicking on
        it.

        * horizontal_scrollbar (bool, optional): Allow horizontal scrollbar to appear. (off
        by default).

        * no_focus_on_appearing (bool, optional): Disable taking focus when transitioning
        from hidden to visible state.

        * no_bring_to_front_on_focus (bool, optional): Disable bringing window to front when
        taking focus. (e.g. clicking on it or programmatically giving it focus).

        * no_close (bool, optional): Disable user closing the window by removing the close
        button.

        * no_background (bool, optional): Sets Background and border alpha to transparent.

        * modal (bool, optional): Fills area behind window according to the theme and
        disables user ability to interact with anything except the window.

        * popup (bool, optional): Fills area behind window according to the theme, removes
        title bar, collapse and close. Window can be closed by selecting area in the
        background behind the window.

        * no_saved_settings (bool, optional): Never load/save settings in .ini file.

        * no_open_over_existing_popup (bool, optional): Don't open if there's already a
        popup.

        * on_close (Callable, optional): Callback ran when window is closed.

    Command: `dearpygui.add_window`
    """
    __slots__: tuple[str, ...] = ()
    label: Property[str | None] = ...
    user_data: Property[Any] = ...
    use_internal_label: Property[bool] = ...
    width: Property[int] = ...
    height: Property[int] = ...
    indent: Property[int] = ...
    show: Property[bool] = ...
    pos: Property[tuple[int, int] | list[int]] = ...
    delay_search: Property[bool] = ...
    min_size: Property[Sequence[int]] = ...
    max_size: Property[Sequence[int]] = ...
    menubar: Property[bool] = ...
    collapsed: Property[bool] = ...
    autosize: Property[bool] = ...
    no_resize: Property[bool] = ...
    no_title_bar: Property[bool] = ...
    no_move: Property[bool] = ...
    no_scrollbar: Property[bool] = ...
    no_collapse: Property[bool] = ...
    horizontal_scrollbar: Property[bool] = ...
    no_focus_on_appearing: Property[bool] = ...
    no_bring_to_front_on_focus: Property[bool] = ...
    no_close: Property[bool] = ...
    no_background: Property[bool] = ...
    modal: Property[bool] = ...
    popup: Property[bool] = ...
    no_saved_settings: Property[bool] = ...
    no_open_over_existing_popup: Property[bool] = ...
    on_close: Property[Callable | None] = ...
    def __init__(self, *, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., delay_search: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., menubar: bool = ..., collapsed: bool = ..., autosize: bool = ..., no_resize: bool = ..., no_title_bar: bool = ..., no_move: bool = ..., no_scrollbar: bool = ..., no_collapse: bool = ..., horizontal_scrollbar: bool = ..., no_focus_on_appearing: bool = ..., no_bring_to_front_on_focus: bool = ..., no_close: bool = ..., no_background: bool = ..., modal: bool = ..., popup: bool = ..., no_saved_settings: bool = ..., no_open_over_existing_popup: bool = ..., on_close: Callable | None = ...) -> None: ...
    @staticmethod
    def command(*, label: str | None = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: 'Item' = ..., width: int = ..., height: int = ..., indent: int = ..., show: bool = ..., pos: tuple[int, int] | list[int] = ..., delay_search: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., menubar: bool = ..., collapsed: bool = ..., autosize: bool = ..., no_resize: bool = ..., no_title_bar: bool = ..., no_move: bool = ..., no_scrollbar: bool = ..., no_collapse: bool = ..., horizontal_scrollbar: bool = ..., no_focus_on_appearing: bool = ..., no_bring_to_front_on_focus: bool = ..., no_close: bool = ..., no_background: bool = ..., modal: bool = ..., popup: bool = ..., no_saved_settings: bool = ..., no_open_over_existing_popup: bool = ..., on_close: Callable | None = ...) -> Item: ...
    def configuration(self) -> dict[Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'show', 'pos', 'delay_search', 'min_size', 'max_size', 'menubar', 'collapsed', 'autosize', 'no_resize', 'no_title_bar', 'no_move', 'no_scrollbar', 'no_collapse', 'horizontal_scrollbar', 'no_focus_on_appearing', 'no_bring_to_front_on_focus', 'no_close', 'no_background', 'modal', 'popup', 'no_saved_settings', 'no_open_over_existing_popup', 'on_close'], Any]: ...



ActivatedHandler = mvActivatedHandler
ActiveHandler = mvActiveHandler
AreaSeries = mvAreaSeries
BarSeries = mvBarSeries
BoolValue = mvBoolValue
Button = mvButton
CandleSeries = mvCandleSeries
CharRemap = mvCharRemap
Checkbox = mvCheckbox
ChildWindow = mvChildWindow
ClickedHandler = mvClickedHandler
Clipper = mvClipper
CollapsingHeader = mvCollapsingHeader
ColorButton = mvColorButton
ColorEdit = mvColorEdit
ColorMap = mvColorMap
ColorMapButton = mvColorMapButton
ColorMapRegistry = mvColorMapRegistry
ColorMapScale = mvColorMapScale
ColorMapSlider = mvColorMapSlider
ColorPicker = mvColorPicker
ColorValue = mvColorValue
Combo = mvCombo
CustomSeries = mvCustomSeries
DatePicker = mvDatePicker
DeactivatedAfterEditHandler = mvDeactivatedAfterEditHandler
DeactivatedHandler = mvDeactivatedHandler
Double4Value = mvDouble4Value
DoubleClickedHandler = mvDoubleClickedHandler
DoubleValue = mvDoubleValue
DragDouble = mvDragDouble
DragDoubleMulti = mvDragDoubleMulti
DragFloat = mvDragFloat
DragFloatMulti = mvDragFloatMulti
DragInt = mvDragInt
DragIntMulti = mvDragIntMulti
DragLine = mvDragLine
DragPayload = mvDragPayload
DragPoint = mvDragPoint
DrawArrow = mvDrawArrow
DrawBezierCubic = mvDrawBezierCubic
DrawBezierQuadratic = mvDrawBezierQuadratic
DrawCircle = mvDrawCircle
DrawEllipse = mvDrawEllipse
DrawImage = mvDrawImage
DrawImageQuad = mvDrawImageQuad
DrawLayer = mvDrawLayer
DrawLine = mvDrawLine
DrawNode = mvDrawNode
DrawPolygon = mvDrawPolygon
DrawPolyline = mvDrawPolyline
DrawQuad = mvDrawQuad
DrawRect = mvDrawRect
DrawText = mvDrawText
DrawTriangle = mvDrawTriangle
Drawlist = mvDrawlist
DynamicTexture = mvDynamicTexture
EditedHandler = mvEditedHandler
ErrorSeries = mvErrorSeries
FileDialog = mvFileDialog
FileExtension = mvFileExtension
FilterSet = mvFilterSet
Float4Value = mvFloat4Value
FloatValue = mvFloatValue
FloatVectValue = mvFloatVectValue
FocusHandler = mvFocusHandler
Font = mvFont
FontChars = mvFontChars
FontRange = mvFontRange
FontRangeHint = mvFontRangeHint
FontRegistry = mvFontRegistry
Group = mvGroup
HLineSeries = mvHLineSeries
HandlerRegistry = mvHandlerRegistry
HeatSeries = mvHeatSeries
HistogramSeries = mvHistogramSeries
HistogramSeries2D = mv2dHistogramSeries
HoverHandler = mvHoverHandler
Image = mvImage
ImageButton = mvImageButton
ImageSeries = mvImageSeries
InputDouble = mvInputDouble
InputDoubleMulti = mvInputDoubleMulti
InputFloat = mvInputFloat
InputFloatMulti = mvInputFloatMulti
InputInt = mvInputInt
InputIntMulti = mvInputIntMulti
InputText = mvInputText
Int4Value = mvInt4Value
IntValue = mvIntValue
ItemHandlerRegistry = mvItemHandlerRegistry
KeyDownHandler = mvKeyDownHandler
KeyPressHandler = mvKeyPressHandler
KeyReleaseHandler = mvKeyReleaseHandler
KnobFloat = mvKnobFloat
LabelSeries = mvLabelSeries
LineSeries = mvLineSeries
Listbox = mvListbox
LoadingIndicator = mvLoadingIndicator
Menu = mvMenu
MenuBar = mvMenuBar
MenuItem = mvMenuItem
MouseClickHandler = mvMouseClickHandler
MouseDoubleClickHandler = mvMouseDoubleClickHandler
MouseDownHandler = mvMouseDownHandler
MouseDragHandler = mvMouseDragHandler
MouseMoveHandler = mvMouseMoveHandler
MouseReleaseHandler = mvMouseReleaseHandler
MouseWheelHandler = mvMouseWheelHandler
Node = mvNode
NodeAttribute = mvNodeAttribute
NodeEditor = mvNodeEditor
NodeLink = mvNodeLink
PieSeries = mvPieSeries
Plot = mvPlot
PlotAnnotation = mvAnnotation
PlotAxis = mvPlotAxis
PlotLegend = mvPlotLegend
ProgressBar = mvProgressBar
RadioButton = mvRadioButton
RawTexture = mvRawTexture
ResizeHandler = mvResizeHandler
ScatterSeries = mvScatterSeries
Selectable = mvSelectable
Separator = mvSeparator
SeriesValue = mvSeriesValue
ShadeSeries = mvShadeSeries
SimplePlot = mvSimplePlot
Slider3D = mvSlider3D
SliderDouble = mvSliderDouble
SliderDoubleMulti = mvSliderDoubleMulti
SliderFloat = mvSliderFloat
SliderFloatMulti = mvSliderFloatMulti
SliderInt = mvSliderInt
SliderIntMulti = mvSliderIntMulti
Spacer = mvSpacer
Stage = mvStage
StairSeries = mvStairSeries
StaticTexture = mvStaticTexture
StemSeries = mvStemSeries
StringValue = mvStringValue
SubPlots = mvSubPlots
Tab = mvTab
TabBar = mvTabBar
TabButton = mvTabButton
Table = mvTable
TableCell = mvTableCell
TableColumn = mvTableColumn
TableRow = mvTableRow
TemplateRegistry = mvTemplateRegistry
Text = mvText
TextureRegistry = mvTextureRegistry
Theme = mvTheme
ThemeColor = mvThemeColor
ThemeComponent = mvThemeComponent
ThemeStyle = mvThemeStyle
TimePicker = mvTimePicker
ToggledOpenHandler = mvToggledOpenHandler
Tooltip = mvTooltip
TreeNode = mvTreeNode
VLineSeries = mvVLineSeries
ValueRegistry = mvValueRegistry
ViewportDrawlist = mvViewportDrawlist
ViewportMenuBar = mvViewportMenuBar
VisibleHandler = mvVisibleHandler
Window = mvWindowAppItem
mvWindow = mvWindowAppItem