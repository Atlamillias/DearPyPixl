from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

__all__ = [
    "InputInt",
    "InputIntMulti",
    "InputFloat",
    "InputFloatMulti",
    "InputText",
]




class InputText(WidgetItem):
    """Adds input for text.

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
            * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (str, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * hint (str, optional): Displayed only when value is an empty string. Will reappear if input value is set to empty string. Will not show if default value is anything other than default empty string.
            * multiline (bool, optional): Allows for multiline text input.
            * no_spaces (bool, optional): Filter out spaces and tabs.
            * uppercase (bool, optional): Automatically make all inputs uppercase.
            * tab_input (bool, optional): Allows tabs to be input into the string value instead of changing item focus.
            * decimal (bool, optional): Only allow characters 0123456789.+-*/
            * hexadecimal (bool, optional): Only allow characters 0123456789ABCDEFabcdef
            * readonly (bool, optional): Activates read only mode where no text can be input but text can still be highlighted.
            * password (bool, optional): Display all input characters as '*'.
            * scientific (bool, optional): Only allow characters 0123456789.+-*/eE (Scientific notation input)
            * on_enter (bool, optional): Only runs callback on enter key press.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInputText, "mvInputText"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_input_text,
    )

    width        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source       : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback     : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback: Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback: Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key   : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    hint         : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    multiline    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config", target="multline")
    no_spaces    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uppercase    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tab_input    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    decimal      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    hexadecimal  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    readonly     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    password     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    scientific   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_enter     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value        : str                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    default_value: str                         = __dearpypixl__.set_information(None, None)

    is_resized                : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered                : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused                : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked                : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible                : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated              : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated            : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

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
        enabled            : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : str                         = '',
        hint               : str                         = '',
        multiline          : bool                        = False,
        no_spaces          : bool                        = False,
        uppercase          : bool                        = False,
        tab_input          : bool                        = False,
        decimal            : bool                        = False,
        hexadecimal        : bool                        = False,
        readonly           : bool                        = False,
        password           : bool                        = False,
        scientific         : bool                        = False,
        on_enter           : bool                        = False,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hint=hint,
            multiline=multiline,
            no_spaces=no_spaces,
            uppercase=uppercase,
            tab_input=tab_input,
            decimal=decimal,
            hexadecimal=hexadecimal,
            readonly=readonly,
            password=password,
            scientific=scientific,
            on_enter=on_enter,
            **kwargs,
        )


class InputFloat(WidgetItem):
    """Adds input for an float. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Display name for the item. Defaults to None.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.        * width (int, optional): Width of the item.
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
        * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInputFloat, "mvInputFloat"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_input_float,
    )

    width        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source       : ItemT                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback     : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback: Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback: Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key   : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    format       : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value    : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value    : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    step         : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    step_fast    : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_clamped  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_clamped  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_enter     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    readonly     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value        : float                       = __dearpypixl__.set_configuration("get_item_value" , "set_item_value" )
    default_value: float                       = __dearpypixl__.set_information(None, None             )

    is_middle_clicked        : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered               : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused               : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked               : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible               : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated             : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated           : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit: bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail     : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

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


class InputFloatMulti(WidgetItem):
    """Adds multi float input for up to 4 float values.

    Args:
        * label (str, optional): Display name for the item. Defaults to None.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.        * width (int, optional): Width of the item.
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
        * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInputFloatMulti, "mvInputFloatMulti"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_input_floatx,
    )

    width                    : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent                   : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source                   : ItemT                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type             : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback                 : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback            : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback            : Callable                          = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show                     : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled                  : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos                      : list[int] | tuple[int, ...]       = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key               : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked                  : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset             : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    format                   : str                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value                : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value                : float                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    size                     : int                               = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_clamped              : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_clamped              : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_enter                 : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    readonly                 : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value                    : list[float] | tuple[float, ...]   = __dearpypixl__.set_configuration("get_item_value", "set_item_value"  )
    default_value            : list[float] | tuple[float, ...]   = __dearpypixl__.set_information(None, None             )

    is_middle_clicked        : bool                              = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked         : bool                              = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked          : bool                              = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered               : bool                              = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                : bool                              = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused               : bool                              = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked               : bool                              = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible               : bool                              = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                : bool                              = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated             : bool                              = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated           : bool                              = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit: bool                              = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                 : list[int, int]                    = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                 : list[int, int]                    = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                : list[int, int]                    = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail     : list[int, int]                    = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        indent            : int                             = -1,
        parent            : Item | int                      = 0,
        before            : Item | int                      = 0,
        source            : Item | int                      = 0,
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


class InputInt(WidgetItem):
    """Adds input for an int. +/- buttons can be activated by setting the value of step.

    Args:
        * label (str, optional): Display name for the item. Defaults to None.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.        * width (int, optional): Width of the item.
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
        * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInputInt, "mvInputInt"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_input_int,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : ItemT                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    step          : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    step_fast     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_clamped   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_clamped   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_enter      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    readonly      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : int                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value"  )
    default_value : int                         = __dearpypixl__.set_information(None, None             )

    is_middle_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered                : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused                : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked                : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible                : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated              : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated            : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        indent            : int                         = -1,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        source            : Item | int                  = 0,
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


class InputIntMulti(WidgetItem):
    """Adds multi int input for up to 4 integer values.

    Args:
        * label (str, optional): Display name for the item. Defaults to None.
        * user_data (Any, optional): User data for callbacks
        * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.        * width (int, optional): Width of the item.
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
        * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInputIntMulti, "mvInputIntMulti"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_input_intx,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : ItemT                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    size          : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_clamped   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_clamped   : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    on_enter      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    readonly      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value" , "set_item_value" )
    default_value : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None             )

    is_middle_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered                : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused                : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked                : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible                : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_edited                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="edited")
    is_activated              : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated            : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        width             : int                         = 0,
        indent            : int                         = -1,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        source            : Item | int                  = 0,
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
