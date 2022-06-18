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
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    """
    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvTemplateRegistry, "mvTemplateRegistry")
    __is_container__ : bool       = True
    __is_root_item__ : bool       = True
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = ()
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_template_registry

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


class ProgressBar(Widget):
    """Adds a progress bar.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * overlay (str, optional): Overlayed text onto the bar that typically used to display the value of the progress.
            * default_value (float, optional): Initial starting value for the item. Normalized value to fill the bar from 0.0 to 1.0.
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    overlay       : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float                       = ItemProperty(INFORM, None, None)
    value         : float                       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvProgressBar, "mvProgressBar")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_progress_bar

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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


class Spacer(Widget):
    """Adds a spacer item that can be used to help with layouts or can be used as a placeholder item.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
    """
    width  : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos    : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSpacer, "mvSpacer")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_spacer

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
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


class Separator(Widget):
    """Adds a horizontal line separator.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
    """
    indent : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos    : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSeparator, "mvSeparator")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_separator

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
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


class TimePicker(Widget):
    """Adds a time picker.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (dict, optional): Initial starting value for the item.
            * hour24 (bool, optional): Show 24 hour clock instead of 12 hour.
    """
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : dict                        = ItemProperty(INFORM, None, None)
    hour24        : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : dict                        = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTimePicker, "mvTimePicker")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_time_picker

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
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


class DatePicker(Widget):
    """Adds a data picker.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (dict, optional): Initial starting value for the item.
            * level (int, optional): Use avaliable constants. mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year
    """
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : dict                        = ItemProperty(INFORM, None, None)
    level         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : dict                        = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused           : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_activated         : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDatePicker, "mvDatePicker")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvDatePicker', 'mvDatePickerLevel_Day', 'mvDatePickerLevel_Month', 'mvDatePickerLevel_Year')
    __command__       : Callable   = dearpygui.add_date_picker

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
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


class Slider3D(Widget):
    """Adds a 3D box slider.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (list[float] | tuple[float, ...], optional): Initial starting value for the item.
            * max_x (float, optional): Applies upper limit to slider.
            * max_y (float, optional): Applies upper limit to slider.
            * max_z (float, optional): Applies upper limit to slider.
            * min_x (float, optional): Applies lower limit to slider.
            * min_y (float, optional): Applies lower limit to slider.
            * min_z (float, optional): Applies lower limit to slider.
            * scale (float, optional): Size of the widget.
    """
    width         : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...]     = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = ItemProperty(INFORM, None, None)
    max_x         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_y         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_z         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_x         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_y         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_z         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    scale         : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSlider3D, "mvSlider3D")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_3d_slider

    def __init__(
        self,
        label             : str                                   = None                ,
        user_data         : Any                                   = None                ,
        use_internal_label: bool                                  = True                ,
        width             : int                                   = 0                   ,
        height            : int                                   = 0                   ,
        indent            : int                                   = -1                  ,
        parent            : int | str                       = 0                   ,
        before            : int | str                       = 0                   ,
        source            : int | str                       = 0                   ,
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


class KnobFloat(Widget):
    """Adds a knob that rotates based on change in x mouse position.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (float, optional): Initial starting value for the item.
            * min_value (float, optional): Applies lower limit to value.
            * max_value (float, optional): Applies upper limit to value.
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float                       = ItemProperty(INFORM, None, None)
    min_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config", target="min_scale")
    max_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config", target="max_scale")
    value         : float                       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active            : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused           : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited            : bool           = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated         : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated       : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvKnobFloat, "mvKnobFloat")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_knob_float

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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


class LoadingIndicator(Widget):
    """Adds a rotating animated loading symbol.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * style (int, optional): 0 is rotating dots style, 1 is rotating bar style.
            * circle_count (int, optional): Number of dots show if dots or size of circle if circle.
            * speed (float, optional): Speed the anamation will rotate.
            * radius (float, optional): Radius size of the loading indicator.
            * thickness (float, optional): Thickness of the circles or line.
            * color (list[int] | tuple[int, ...], optional): Color of the growing center circle.
            * secondary_color (list[int] | tuple[int, ...], optional): Background of the dots in dot mode.
    """
    width               : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height              : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent              : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type        : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback       : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show                : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                 : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    style               : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    circle_count        : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    speed               : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    radius              : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    thickness           : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    color               : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    secondary_color     : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized           : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked    : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered           : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible           : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_min             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvLoadingIndicator, "mvLoadingIndicator")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_loading_indicator

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
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


class FileDialog(Widget):
    """Displays a file or directory selector depending on keywords. Displays a file dialog by default. Callback will be ran when the file or directory picker is closed. The app_data arguemnt will be populated with information related to the file and directory as a dictionary.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * default_path (str, optional): Path that the file dialog will default to when opened.
            * default_filename (str, optional): Default name that will show in the file name input.
            * file_count (int, optional): Number of visible files in the dialog.
            * modal (bool, optional): Forces user interaction with the file selector.
            * directory_selector (bool, optional): Shows only directory/paths as options. Allows selection of directory/paths only.
    """
    width              : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height             : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback           : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show               : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_path       : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_filename   : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    file_count         : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    modal              : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    directory_selector : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFileDialog, "mvFileDialog")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = True
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __commands__      : tuple      = ('get_file_dialog_info',)
    __command__       : Callable   = dearpygui.add_file_dialog

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


class FileExtension(Widget):
    """Creates a file extension filter option in the file dialog.

        Args:
            * extension (str): Extension that will show as an when the parent is a file dialog.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * custom_text (str, optional): Replaces the displayed text in the drop down for this extension.
            * color (list[int] | tuple[int, ...], optional): Color for the text that will be shown with specified extensions.
    """
    extension   : str                         = ItemProperty(CONFIG, None, "set_item_config")
    width       : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height      : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    custom_text : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    color       : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFileExtension, "mvFileExtension")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvStage, dearpygui.mvFileDialog, dearpygui.mvTemplateRegistry)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_file_extension

    def __init__(
        self,
        extension         : str,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        height            : int                         = 0,
        parent            : int | str                   = 0,
        before            : int | str                   = 0,
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
