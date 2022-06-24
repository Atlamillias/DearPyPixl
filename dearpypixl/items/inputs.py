from typing import (
    Callable,
    Any,
)
from dearpygui import dearpygui
from dearpypixl.itemtypes import *
from dearpypixl.items.basic import Text

__all__ = [
    "InputInt",
    "InputIntMulti",
    "InputFloat",
    "InputFloatMulti",
    "InputText",
]


class InputFloat(Widget):
    """Adds input for an float. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Overrides 'name' as label.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        * width (int, optional): Width of the item.
        * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        * parent (int | str, optional): Parent to add this item to. (runtime adding)
        * before (int | str, optional): This item will be displayed before the specified item in the parent.
        * source (int | str, optional): Overrides 'id' as value storage key.
        * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        * callback (Callable, optional): Registers a callback.
        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        * show (bool, optional): Attempt to render widget.
        * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
        * filter_key (str, optional): Used by filter widget.
        * tracked (bool, optional): Scroll tracking
        * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        * default_value (float, optional): Initial starting value for the item.
        * format (str, optional): Determines the format the float will be displayed as use python string formatting.
        * min_value (float, optional): Value for lower limit of input. By default this limits the step buttons. Use min_clamped to limit manual input.
        * max_value (float, optional): Value for upper limit of input. By default this limits the step buttons. Use max_clamped to limit manual input.
        * step (float, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
        * step_fast (float, optional): After holding the step buttons for extended time the increments will switch to this value.
        * min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        * max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        * on_enter (bool, optional): Only runs callback on enter key press.
        * readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
    """
    width        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent       : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source       : ItemT                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback     : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback: Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback: Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state" , "set_item_config")
    filter_key   : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    format       : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value    : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value    : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    step         : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    step_fast    : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_clamped  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_clamped  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_enter     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    readonly     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value        : float                       = ItemProperty(CONFIG, "get_item_value" , "set_item_value" )
    default_value: float                       = ItemProperty(INFORM, None, None             )

    is_middle_clicked        : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked         : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked          : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered               : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused               : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked               : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible               : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited                : bool           = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated             : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated           : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit: bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail     : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInputFloat, "mvInputFloat")
    __is_container__  : bool     = False
    __is_root_item__  : bool     = False
    __is_value_able__ : bool     = True
    __able_parents__  : tuple    = ()
    __able_children__ : tuple    = ()
    __command__       : Callable = dearpygui.add_input_float

    def __init__(
        self,
        label             : str = None,
        user_data         : Any = None,
        use_internal_label: bool = True,
        width             : int = 0,
        indent            : int = -1,
        parent            : int | str = 0,
        before            : int | str = 0,
        source            : int | str = 0,
        payload_type      : str = '$$DPG_PAYLOAD',
        callback          : Callable = None,
        drag_callback     : Callable = None,
        drop_callback     : Callable = None,
        show              : bool = True,
        enabled           : bool = True,
        pos               : list[int] | tuple[int,...] = (),
        filter_key        : str = '',
        tracked           : bool = False,
        track_offset      : float = 0.5,
        default_value     : float = 0.0,
        format            : str = '%.3f',
        min_value         : float = 0.0,
        max_value         : float = 100.0,
        step              : float = 0.1,
        step_fast         : float = 1.0,
        min_clamped       : bool = False,
        max_clamped       : bool = False,
        on_enter          : bool = False,
        readonly          : bool = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )


class InputFloatMulti(Widget):
    """Adds multi float input for up to 4 float values.

    Args:
        * label (str, optional): Overrides 'name' as label.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        * width (int, optional): Width of the item.
        * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        * parent (int | str, optional): Parent to add this item to. (runtime adding)
        * before (int | str, optional): This item will be displayed before the specified item in the parent.
        * source (int | str, optional): Overrides 'id' as value storage key.
        * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        * callback (Callable, optional): Registers a callback.
        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        * show (bool, optional): Attempt to render widget.
        * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
        * filter_key (str, optional): Used by filter widget.
        * tracked (bool, optional): Scroll tracking
        * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        * default_value (list[float] | tuple[float, ...], optional): Initial starting value for the item.
        * format (str, optional): Determines the format the float will be displayed as (use python string formatting).
        * min_value (float, optional): Value for lower limit of input for each cell. Use min_clamped to turn on.
        * max_value (float, optional): Value for upper limit of input for each cell. Use max_clamped to turn on.
        * size (int, optional): Number of components displayed for input.
        * min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        * max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        * on_enter (bool, optional): Only runs callback on enter key press.
        * readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
    """
    width                    : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent                   : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source                   : ItemT                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type             : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback                 : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback            : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback            : Callable                          = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show                     : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled                  : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos                      : list[int] | tuple[int, ...]       = ItemProperty(CONFIG, "get_item_state" , "set_item_config")
    filter_key               : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked                  : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset             : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    format                   : str                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value                : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value                : float                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    size                     : int                               = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_clamped              : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_clamped              : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_enter                 : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    readonly                 : bool                              = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value                    : list[float] | tuple[float, ...]   = ItemProperty(CONFIG, "get_item_value", "set_item_value"  )
    default_value            : list[float] | tuple[float, ...]   = ItemProperty(INFORM, None, None             )

    is_middle_clicked        : bool                              = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked         : bool                              = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked          : bool                              = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered               : bool                              = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                : bool                              = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused               : bool                              = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked               : bool                              = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible               : bool                              = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited                : bool                              = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated             : bool                              = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated           : bool                              = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit: bool                              = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                 : list[int, int]                    = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                 : list[int, int]                    = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                : list[int, int]                    = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail     : list[int, int]                    = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInputFloatMulti, "mvInputFloatMulti")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_input_floatx

    def __init__(
        self,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        indent            : int                             = -1,
        parent            : int | str                       = 0,
        before            : int | str                       = 0,
        source            : int | str                       = 0,
        payload_type      : str                             = '$$DPG_PAYLOAD',
        callback          : Callable                        = None,
        drag_callback     : Callable                        = None,
        drop_callback     : Callable                        = None,
        show              : bool                            = True,
        enabled           : bool                            = True,
        pos               : list[int] | tuple[int, ...]     = [],
        filter_key        : str                             = '',
        tracked           : bool                            = False,
        track_offset      : float                           = 0.5,
        default_value     : list[float] | tuple[float, ...] = (0.0, 0.0, 0.0, 0.0),
        format            : str                             = '%.3f',
        min_value         : float                           = 0.0,
        max_value         : float                           = 100.0,
        size              : int                             = 4,
        min_clamped       : bool                            = False,
        max_clamped       : bool                            = False,
        on_enter          : bool                            = False,
        readonly          : bool                            = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )


class InputInt(Widget):
    """Adds input for an int. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Overrides 'name' as label.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        * width (int, optional): Width of the item.
        * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        * parent (int | str, optional): Parent to add this item to. (runtime adding)
        * before (int | str, optional): This item will be displayed before the specified item in the parent.
        * source (int | str, optional): Overrides 'id' as value storage key.
        * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        * callback (Callable, optional): Registers a callback.
        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        * show (bool, optional): Attempt to render widget.
        * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
        * filter_key (str, optional): Used by filter widget.
        * tracked (bool, optional): Scroll tracking
        * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        * default_value (int, optional): Initial starting value for the item.
        * min_value (int, optional): Value for lower limit of input. By default this limits the step buttons. Use min_clamped to limit manual input.
        * max_value (int, optional): Value for upper limit of input. By default this limits the step buttons. Use max_clamped to limit manual input.
        * step (int, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
        * step_fast (int, optional): After holding the step buttons for extended time the increments will switch to this value.
        * min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        * max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        * on_enter (bool, optional): Only runs callback on enter key press.
        * readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : ItemT                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state" , "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    step          : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    step_fast     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_clamped   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_clamped   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_enter      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    readonly      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : int                         = ItemProperty(CONFIG, "get_item_value", "set_item_value"  )
    default_value : int                         = ItemProperty(INFORM, None, None             )

    is_middle_clicked         : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered                : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                 : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused                : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked                : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible                : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited                 : bool           = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated              : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated            : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInputInt, "mvInputInt")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_input_int

    def __init__(
        self,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        indent            : int                         = -1,
        parent            : int | str                   = 0,
        before            : int | str                   = 0,
        source            : int | str                   = 0,
        payload_type      : str                         = '$$DPG_PAYLOAD',
        callback          : Callable                    = None,
        drag_callback     : Callable                    = None,
        drop_callback     : Callable                    = None,
        show              : bool                        = True,
        enabled           : bool                        = True,
        pos               : list[int] | tuple[int, ...] = [],
        filter_key        : str                         = '',
        tracked           : bool                        = False,
        track_offset      : float                       = 0.5,
        default_value     : int                         = 0,
        min_value         : int                         = 0,
        max_value         : int                         = 100,
        step              : int                         = 1,
        step_fast         : int                         = 100,
        min_clamped       : bool                        = False,
        max_clamped       : bool                        = False,
        on_enter          : bool                        = False,
        readonly          : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )


class InputIntMulti(Widget):
    """Adds multi int input for up to 4 integer values.

    Args:
        * label (str, optional): Overrides 'name' as label.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
        * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
        * width (int, optional): Width of the item.
        * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
        * parent (int | str, optional): Parent to add this item to. (runtime adding)
        * before (int | str, optional): This item will be displayed before the specified item in the parent.
        * source (int | str, optional): Overrides 'id' as value storage key.
        * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
        * callback (Callable, optional): Registers a callback.
        * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
        * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
        * show (bool, optional): Attempt to render widget.
        * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
        * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
        * filter_key (str, optional): Used by filter widget.
        * tracked (bool, optional): Scroll tracking
        * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
        * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item.
        * min_value (int, optional): Value for lower limit of input for each cell. Use min_clamped to turn on.
        * max_value (int, optional): Value for upper limit of input for each cell. Use max_clamped to turn on.
        * size (int, optional): Number of components displayed for input.
        * min_clamped (bool, optional): Activates and deactivates the enforcment of min_value.
        * max_clamped (bool, optional): Activates and deactivates the enforcment of max_value.
        * on_enter (bool, optional): Only runs callback on enter.
        * readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : ItemT                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state" , "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    size          : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_clamped   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_clamped   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_enter      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    readonly      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_value" , "set_item_value" )
    default_value : list[int] | tuple[int, ...] = ItemProperty(INFORM, None, None             )

    is_middle_clicked         : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered                : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                 : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused                : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked                : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible                : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_edited                 : bool           = ItemProperty(STATES, "get_item_state", None, target="edited")
    is_activated              : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated            : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInputIntMulti, "mvInputIntMulti")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_input_intx


    def __init__(
        self,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        indent            : int                         = -1,
        parent            : int | str                   = 0,
        before            : int | str                   = 0,
        source            : int | str                   = 0,
        payload_type      : str                         = '$$DPG_PAYLOAD',
        callback          : Callable                    = None,
        drag_callback     : Callable                    = None,
        drop_callback     : Callable                    = None,
        show              : bool                        = True,
        enabled           : bool                        = True,
        pos               : list[int] | tuple[int, ...] = (),
        filter_key        : str                         = '',
        tracked           : bool                        = False,
        track_offset      : float                       = 0.5,
        default_value     : list[int] | tuple[int, ...] = (0, 0, 0, 0),
        min_value         : int                         = 0,
        max_value         : int                         = 100,
        size              : int                         = 4,
        min_clamped       : bool                        = False,
        max_clamped       : bool                        = False,
        on_enter          : bool                        = False,
        readonly          : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs
        )