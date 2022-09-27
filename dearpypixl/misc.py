from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *


__all__ = [
    "TemplateRegistry",
    "ProgressBar",
    "Spacer",
    "Separator",
    "TimePicker",
    "DatePicker",
    "Slider3D",
    "KnobFloat",
    "LoadingIndicator",
    "FileDialog",
    "FileExtension",
]


class TemplateRegistry(Item):
    """Adds a template registry.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTemplateRegistry, "mvTemplateRegistry"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_template_registry,
    )

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


class ProgressBar(WidgetItem):
    """Adds a progress bar.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * overlay (str, optional): Overlayed text onto the bar that typically used to display the value of the progress.
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvProgressBar, "mvProgressBar"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_progress_bar,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    overlay       : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float                       = __dearpypixl__.set_information(None, None)
    value         : float                       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        source             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        overlay            : str                         = '',
        default_value      : float                       = 0.0,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            overlay=overlay,
            default_value=default_value,
            **kwargs,
        )


class Spacer(WidgetItem):
    """Adds a spacer item that can be used to help with layouts or can be used as a placeholder item.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSpacer, "mvSpacer"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_spacer,
    )

    width  : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos    : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            **kwargs,
        )


class Separator(WidgetItem):
    """Adds a horizontal line separator.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * indent (int, optional): Outer horizontal padding (in pixels) to add to the left side of
            the item, multiplied by the value of the indent/horizontal padding theme element affecting
            the item (1.0 by default). If -1, no additional padding is added. Defaults to -1.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSeparator, "mvSeparator"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_separator,
    )

    indent : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos    : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            **kwargs,
        )


class TimePicker(WidgetItem):
    """Adds a time picker.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * indent (int, optional): Outer horizontal padding (in pixels) to add to the left side of
            the item, multiplied by the value of the indent/horizontal padding theme element affecting
            the item (1.0 by default). If -1, no additional padding is added. Defaults to -1.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (dict, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * hour24 (bool, optional): Show 24 hour clock instead of 12 hour.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTimePicker, "mvTimePicker"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_time_picker,
    )

    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : dict                        = __dearpypixl__.set_information(None, None)
    hour24        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : dict                        = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        callback           : Callable                    = None,
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : dict                        = {'hour': 14, 'min': 32, 'sec': 23},
        hour24             : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hour24=hour24,
            **kwargs,
        )


class DatePicker(WidgetItem):
    """Adds a data picker.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * indent (int, optional): Outer horizontal padding (in pixels) to add to the left side of
            the item, multiplied by the value of the indent/horizontal padding theme element affecting
            the item (1.0 by default). If -1, no additional padding is added. Defaults to -1.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (dict, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * level (int, optional): Use avaliable constants. mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDatePicker, "mvDatePicker"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        constants=('mvDatePicker', 'mvDatePickerLevel_Day', 'mvDatePickerLevel_Month', 'mvDatePickerLevel_Year'),
        command=dearpygui.add_date_picker,
    )

    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : dict                        = __dearpypixl__.set_information(None, None)
    level         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : dict                        = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        callback           : Callable                    = None,
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : dict                        = {'month_day': 14, 'year': 20, 'month': 5},
        level              : int                         = 0,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            level=level,
            **kwargs,
        )


class Slider3D(WidgetItem):
    """Adds a 3D box slider.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (list[float] | tuple[float, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * max_x (float, optional): Applies upper limit to slider.
            * max_y (float, optional): Applies upper limit to slider.
            * max_z (float, optional): Applies upper limit to slider.
            * min_x (float, optional): Applies lower limit to slider.
            * min_y (float, optional): Applies lower limit to slider.
            * min_z (float, optional): Applies lower limit to slider.
            * scale (float, optional): Size of the widget.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSlider3D, "mvSlider3D"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_3d_slider,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = __dearpypixl__.set_information(None, None)
    max_x         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_y         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_z         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_x         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_y         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_z         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    scale         : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        width             : int                                   = 0                   ,
        height            : int                                   = 0                   ,
        indent            : int                                   = -1                  ,
        parent            : Item | int                      = 0                   ,
        before            : Item | int                      = 0                   ,
        source            : Item | int                      = 0                   ,
        payload_type      : str                                   = '$$DPG_PAYLOAD'     ,
        callback          : Callable                              = None                ,
        drag_callback     : Callable                              = None                ,
        drop_callback     : Callable                              = None                ,
        show              : bool                                  = True                ,
        pos               : list[int] | tuple[int, ...]     = []                  ,
        filter_key        : str                                   = ''                  ,
        tracked           : bool                                  = False               ,
        track_offset      : float                                 = 0.5                 ,
        default_value     : list[float] | tuple[float, ...] = (0.0, 0.0, 0.0, 0.0),
        max_x             : float                                 = 100.0               ,
        max_y             : float                                 = 100.0               ,
        max_z             : float                                 = 100.0               ,
        min_x             : float                                 = 0.0                 ,
        min_y             : float                                 = 0.0                 ,
        min_z             : float                                 = 0.0                 ,
        scale             : float                                 = 1.0                 ,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            max_x=max_x,
            max_y=max_y,
            max_z=max_z,
            min_x=min_x,
            min_y=min_y,
            min_z=min_z,
            scale=scale,
            **kwargs,
        )


class KnobFloat(WidgetItem):
    """Adds a knob that rotates based on change in x mouse position.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * min_value (float, optional): Applies lower limit to value.
            * max_value (float, optional): Applies upper limit to value.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvKnobFloat, "mvKnobFloat"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_knob_float,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float                       = __dearpypixl__.set_information(None, None)
    min_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config", target="min_scale")
    max_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config", target="max_scale")
    value         : float                       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited            : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        source             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        callback           : Callable                    = None,
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : float                       = 0.0,
        min_value          : float                       = 0.0,
        max_value          : float                       = 100.0,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            **kwargs,
        )


class LoadingIndicator(WidgetItem):
    """Adds a rotating animated loading symbol.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * style (int, optional): 0 is rotating dots style, 1 is rotating bar style.
            * circle_count (int, optional): Number of dots show if dots or size of circle if circle.
            * speed (float, optional): Speed the anamation will rotate.
            * radius (float, optional): Radius size of the loading indicator.
            * thickness (float, optional): Thickness of the circles or line.
            * color (list[int] | tuple[int, ...], optional): Color of the growing center circle.
            * secondary_color (list[int] | tuple[int, ...], optional): Background of the dots in dot mode.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvLoadingIndicator, "mvLoadingIndicator"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_loading_indicator,
    )

    width               : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height              : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent              : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type        : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback       : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show                : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                 : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    style               : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    circle_count        : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    speed               : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    radius              : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness           : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color               : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    secondary_color     : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        style              : int                         = 0,
        circle_count       : int                         = 8,
        speed              : float                       = 1.0,
        radius             : float                       = 3.0,
        thickness          : float                       = 1.0,
        color              : list[int] | tuple[int, ...] = (51, 51, 55, 255),
        secondary_color    : list[int] | tuple[int, ...] = (29, 151, 236, 103),
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            style=style,
            circle_count=circle_count,
            speed=speed,
            radius=radius,
            thickness=thickness,
            color=color,
            secondary_color=secondary_color,
            **kwargs,
        )


class FileDialog(WidgetItem):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by default. Callback will be ran when the file or directory picker is closed. The app_data arguemnt will be populated with information related to the file and directory as a dictionary.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * default_path (str, optional): Path that the file dialog will default to when opened.
            * default_filename (str, optional): Default name that will show in the file name input.
            * file_count (int, optional): Number of visible files in the dialog.
            * modal (bool, optional): Forces user interaction with the file selector.
            * directory_selector (bool, optional): Shows only directory/paths as options. Allows selection of directory/paths only.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFileDialog, "mvFileDialog"),
        is_container=True,
        is_root_item=True,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        commands=('get_file_dialog_info',),
        command=dearpygui.add_file_dialog,
    )

    width              : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height             : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback           : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show               : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_path       : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_filename   : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    file_count         : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    modal              : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    directory_selector : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label             : str      = None ,
        user_data         : Any      = None ,
        use_internal_label: bool     = True ,
        width             : int      = 0    ,
        height            : int      = 0    ,
        callback          : Callable = None ,
        show              : bool     = True ,
        default_path      : str      = ''   ,
        default_filename  : str      = '.'  ,
        file_count        : int      = 0    ,
        modal             : bool     = False,
        directory_selector: bool     = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            callback=callback,
            show=show,
            default_path=default_path,
            default_filename=default_filename,
            file_count=file_count,
            modal=modal,
            directory_selector=directory_selector,
            **kwargs,
        )


class FileExtension(WidgetItem):
    """Creates a file extension filter option in the file dialog.

        Args:
            * extension (str): Extension that will show as an when the parent is a file dialog.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * custom_text (str, optional): Replaces the displayed text in the drop down for this extension.
            * color (list[int] | tuple[int, ...], optional): Color for the text that will be shown with specified extensions.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFileExtension, "mvFileExtension"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvFileDialog,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_file_extension,
    )

    extension   : str                         = __dearpypixl__.set_configuration(None, "set_item_config")
    width       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    custom_text : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color       : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        extension         : str,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        height            : int                         = 0,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        custom_text       : str                         = '',
        color             : list[int] | tuple[int, ...] = (-255, 0, 0, 255),
        **kwargs
    ) -> None:
        super().__init__(
            extension=extension,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            custom_text=custom_text,
            color=color,
            **kwargs,
        )
