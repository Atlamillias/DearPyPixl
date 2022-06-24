from typing import (
    Callable,
    Any,
)
from dearpygui import dearpygui
from dearpypixl.itemtypes import *


__all__ = [
    "RadioButton",
    "Listbox",
    "Checkbox",
    "Button",
    "Selectable",
    "Combo",

    "SliderFloat",  # TODO: Maybe move to 'inputs'
    "DragFloat",    # TODO: Maybe move to 'inputs'

    "Text",
    "TabButton",
    "MenuItem",
    "Image",
    "ImageButton",
]



class RadioButton(Widget):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.

        Args:
            * items (list[str], tuple[str | ...], optional): A tuple of items to be shown as radio options. Can consist of any combination of types. All types will be shown as strings.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
            * default_value (str, optional): Initial starting value for the item. Default selected radio option. Set by using the string value of the item.
            * horizontal (bool, optional): Displays the radio options horizontally.
        Returns:
            int | str
    """
    items         : list[str] | tuple[str, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : str                         = ItemProperty(INFORM, None, None)
    horizontal    : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : str                         = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvRadioButton, "mvRadioButton")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_radio_button

    def __init__(
        self,
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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
        horizontal         : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            items=items,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            horizontal=horizontal,
            **kwargs,
        )


class Listbox(Widget):
    """Adds a listbox. If height is not large enough to show all items a scroll bar will appear.

        Args:
            * items (list[str] | tuple[str, ...], optional): A tuple of items to be shown in the listbox. Can consist of any combination of types. All items will be displayed as strings.
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
            * default_value (str, optional): Initial starting value for the item. String value fo the item that will be selected by default.
            * num_items (int, optional): Expands the height of the listbox to show specified number of items.
        Returns:
            int | str
    """
    items         : list[str] | tuple[str, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : str                         = ItemProperty(INFORM, None, None)
    num_items     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : str                         = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvListbox, "mvListbox")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_listbox

    def __init__(
        self,
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label: bool                         = True,
        width              : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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
        num_items          : int                         = 3,
        **kwargs
    ) -> None:
        super().__init__(
            items=items,
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
            num_items=num_items,
            **kwargs,
        )


class Checkbox(Widget):
    """Adds a checkbox.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
            * default_value (bool, optional): Initial starting value for the item. Sets the default value of the checkmark
        Returns:
            int | str
    """
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : bool                        = ItemProperty(INFORM, None, None)
    value         : bool                        = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked         : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered                : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_active                 : bool           = ItemProperty(STATES, "get_item_state", None, target="active")
    is_focused                : bool           = ItemProperty(STATES, "get_item_state", None, target="focused")
    is_clicked                : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible                : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    is_activated              : bool           = ItemProperty(STATES, "get_item_state", None, target="activated")
    is_deactivated            : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated")
    is_deactivated_after_edit : bool           = ItemProperty(STATES, "get_item_state", None, target="deactivated_after_edit")
    rect_min                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvCheckbox, "mvCheckbox")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_checkbox

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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
        default_value      : bool                        = False,
        **kwargs,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            **kwargs,
        )


class Button(Widget):
    """Adds a button.

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
            * callback (Callable, optional): Registers a callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * small (bool, optional): Shrinks the size of the button to the text of the label it contains. Useful for embedding in text.
            * arrow (bool, optional): Displays an arrow in place of the text string. This requires the direction keyword.
            * direction (int, optional): Sets the cardinal direction for the arrow buy using constants mvDir_Left, mvDir_Up, mvDir_Down, mvDir_Right, mvDir_None. Arrow keyword must be set to True.
        Returns:
            int | str
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    small         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    arrow         : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    direction     : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")

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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvButton, "mvButton")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvButton', 'mvAll', 'mvTool_About', 'mvTool_Debug', 'mvTool_Doc', 'mvTool_ItemRegistry', 'mvTool_Metrics', 'mvTool_Style', 'mvTool_Font', 'mvFontAtlas', 'mvAppUUID', 'mvInvalidUUID', 'mvDir_None', 'mvDir_Left', 'mvDir_Right', 'mvDir_Up', 'mvDir_Down')
    __command__       : Callable   = dearpygui.add_button

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
        callback           : Callable                    = None,
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        enabled            : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        small              : bool                        = False,
        arrow              : bool                        = False,
        direction          : int                         = 0,
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
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            small=small,
            arrow=arrow,
            direction=direction,
            **kwargs,
        )


class Selectable(Widget):
    """Adds a selectable. Similar to a button but can indicate its selected state.

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
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (bool, optional): Initial starting value for the item.
            * span_columns (bool, optional): Forces the selectable to span the width of all columns if placed in a table.
        Returns:
            int | str
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : bool                        = ItemProperty(INFORM, None, None)
    span_columns  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : bool                        = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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
    is_toggled_open           : bool           = ItemProperty(STATES, "get_item_state", None, target="toggled_open")
    rect_min                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_min")
    rect_max                  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_max")
    rect_size                 : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")
    content_region_avail      : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="content_region_avail")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSelectable, "mvSelectable")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_selectable

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
        enabled            : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : bool                        = False,
        span_columns       : bool                        = False,
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
            span_columns=span_columns,
            **kwargs,
        )


class Combo(Widget):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window. All items will be shown as selectables on the dropdown.

        Args:
            * items (list[str] | tuple[str, ...], optional): A tuple of items to be shown in the drop down window. Can consist of any combination of types but will convert all items to strings to be shown.
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
            * default_value (str, optional): Initial starting value for the item. Sets a selected item from the drop down by specifying the string value.
            * popup_align_left (bool, optional): Align the contents on the popup toward the left.
            * no_arrow_button (bool, optional): Display the preview box without the square arrow button indicating dropdown activity.
            * no_preview (bool, optional): Display only the square arrow button and not the selected value.
            * height_mode (int, optional): Controlls the number of items shown in the dropdown by the constants mvComboHeight_Small, mvComboHeight_Regular, mvComboHeight_Large, mvComboHeight_Largest
        Returns:
            int | str
    """
    items            : list[str] | tuple[str, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    width            : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent           : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source           : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type     : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback         : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback    : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback    : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show             : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos              : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key       : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value    : str                         = ItemProperty(INFORM, None, None)
    popup_align_left : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_arrow_button  : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_preview       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height_mode      : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value            : str                         = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvCombo, "mvCombo")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvCombo', 'mvComboHeight_Small', 'mvComboHeight_Regular', 'mvComboHeight_Large', 'mvComboHeight_Largest')
    __command__       : Callable   = dearpygui.add_combo

    def __init__(
        self,
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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
        popup_align_left   : bool                        = False,
        no_arrow_button    : bool                        = False,
        no_preview         : bool                        = False,
        height_mode        : int                         = 1,
        **kwargs
    ) -> None:
        super().__init__(
            items=items,
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
            popup_align_left=popup_align_left,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
            height_mode=height_mode,
            **kwargs,
        )


class InputText(Widget):
    """Adds input for text.

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
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (str, optional): Initial starting value for the item.
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
        Returns:
            int | str
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : str                         = ItemProperty(INFORM, None, None)
    hint          : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    multiline     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config", target="multline")
    no_spaces     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    uppercase     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tab_input     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    decimal       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    hexadecimal   : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    readonly      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    password      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    scientific    : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    on_enter      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : str                         = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInputText, "mvInputText")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_input_text

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


class SliderFloat(Widget):
    """Adds slider for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.

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
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (float, optional): Initial starting value for the item.
            * vertical (bool, optional): Sets orientation of the slidebar and slider to vertical.
            * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click or Enter key allowing to input text directly into the item.
            * clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            * min_value (float, optional): Applies a limit only to sliding entry only.
            * max_value (float, optional): Applies a limit only to sliding entry only.
            * format (str, optional): Determines the format the float will be displayed as use python string formatting.
        Returns:
            int | str
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float                       = ItemProperty(INFORM, None, None)
    vertical      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_input      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    clamped       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    format        : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : float                       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSliderFloat, "mvSliderFloat")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_slider_float

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
        enabled            : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        default_value      : float                       = 0.0,
        vertical           : bool                        = False,
        no_input           : bool                        = False,
        clamped            : bool                        = False,
        min_value          : float                       = 0.0,
        max_value          : float                       = 100.0,
        format             : str                         = '%.3f',
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
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )


class DragFloat(Widget):
    """Adds drag for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.

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
            * speed (float, optional): Sets the sensitivity the float will be modified while dragging.
            * min_value (float, optional): Applies a limit only to draging entry only.
            * max_value (float, optional): Applies a limit only to draging entry only.
            * no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            * clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
        Returns:
            int | str
    """
    width         : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_callback")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float                       = ItemProperty(INFORM, None, None)
    format        : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    speed         : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    min_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    max_value     : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_input      : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    clamped       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : float                       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    is_resized                : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDragFloat, "mvDragFloat")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_drag_float

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
        indent             : int                         = -1,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        source             : int | str                   = 0,
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
        default_value      : float                       = 0.0,
        format             : str                         = '%0.3f',
        speed              : float                       = 1.0,
        min_value          : float                       = 0.0,
        max_value          : float                       = 100.0,
        no_input           : bool                        = False,
        clamped            : bool                        = False,
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
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )


class Text(Widget):
    """Adds text. Text can have an optional label that will display to the right of the text.

        Args:
            * default_value (str, optional): Initial starting value for the item.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
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
            * wrap (int, optional): Number of pixels from the start of the item until wrapping starts.
            * bullet (bool, optional): Places a bullet to the left of the text.
            * color (list[int] | tuple[int, ...], optional): Color of the text (rgba).
            * show_label (bool, optional): Displays the label to the right of the text.
        Returns:
            int | str
    """
    default_value : str                         = ItemProperty(INFORM, None, None)
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
    wrap          : int                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    bullet        : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    color         : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show_label    : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : str                         = ItemProperty(CONFIG, "get_item_value", "set_item_value")

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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvText, "mvText")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_text

    def __init__(
        self,
        default_value      : str                         = '',
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
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
        wrap               : int                         = -1,
        bullet             : bool                        = False,
        color              : list[int] | tuple[int, ...] = (-255, 0, 0, 255),
        show_label         : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
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
            wrap=wrap,
            bullet=bullet,
            color=color,
            show_label=show_label,
            **kwargs,
        )


class TabButton(Widget):
    """Adds a tab button to a tab bar.

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
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * no_reorder (bool, optional): Disable reordering this tab or having another tab cross over this tab. Fixes the position of this tab in relation to the order of neighboring tabs at start.
            * leading (bool, optional): Enforce the tab position to the left of the tab bar (after the tab list popup button).
            * trailing (bool, optional): Enforce the tab position to the right of the tab bar (before the scrolling buttons).
            * no_tooltip (bool, optional): Disable tooltip for the given tab.
        Returns:
            int | str
    """
    indent        : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key    : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_reorder    : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    leading       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    trailing      : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    no_tooltip    : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvTabButton, "mvTabButton")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvTabBar, dearpygui.mvStage, dearpygui.mvTemplateRegistry)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_tab_button

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        payload_type       : str       = '$$DPG_PAYLOAD',
        callback           : Callable  = None,
        drag_callback      : Callable  = None,
        drop_callback      : Callable  = None,
        show               : bool      = True,
        filter_key         : str       = '',
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        no_reorder         : bool      = False,
        leading            : bool      = False,
        trailing           : bool      = False,
        no_tooltip         : bool      = False,
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
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            no_reorder=no_reorder,
            leading=leading,
            trailing=trailing,
            no_tooltip=no_tooltip,
            **kwargs,
        )


class MenuItem(Widget):
    """Adds a menu item to an existing menu. Menu items act similar to selectables and has a bool value. When placed in a menu the checkmark will reflect its value.

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
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (bool, optional): Initial starting value for the item. This value also controls the checkmark when shown.
            * shortcut (str, optional): Displays text on the menu item. Typically used to show a shortcut key command.
            * check (bool, optional): Displays a checkmark on the menu item when it is selected and placed in a menu.
            * drag_callback (Callable, optional): (deprecated)
        Returns:
            int | str
    """
    indent        : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback      : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    enabled       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key    : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : bool     = ItemProperty(INFORM, None, None)
    shortcut      : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    check         : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : bool     = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvMenuItem, "mvMenuItem")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = True
    __able_parents__ : tuple      = ()
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_menu_item

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        payload_type       : str       = '$$DPG_PAYLOAD',
        callback           : Callable  = None,
        drop_callback      : Callable  = None,
        show               : bool      = True,
        enabled            : bool      = True,
        filter_key         : str       = '',
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        default_value      : bool      = False,
        shortcut           : str       = '',
        check              : bool      = False,
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
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            shortcut=shortcut,
            check=check,
            **kwargs,
        )


class Image(Widget):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) for texture coordinates will generally display the entire texture.

        Args:
            * texture_tag (int | str): The texture_tag should come from a texture that was added to a texture registry.
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
            * tint_color (list[float] | tuple[float, ...], optional): Applies a color tint to the entire texture.
            * border_color (list[float] | tuple[float, ...], optional): Displays a border of the specified color around the texture. If the theme style has turned off the border it will not be shown.
            * uv_min (list[float] | tuple[float, ...], optional): Normalized texture coordinates min point.
            * uv_max (list[float] | tuple[float, ...], optional): Normalized texture coordinates max point.
        Returns:
            int | str
    """
    texture_tag   : int | str                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    width         : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source        : int | str                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type  : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...]     = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked       : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tint_color    : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    border_color  : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    uv_min        : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    uv_max        : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")

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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvImage, "mvImage")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_image

    def __init__(
        self,
        texture_tag       : int | str,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        height            : int                             = 0,
        indent            : int                             = -1,
        parent            : int | str                       = 0,
        before            : int | str                       = 0,
        source            : int | str                       = 0,
        payload_type      : str                             = '$$DPG_PAYLOAD',
        drag_callback     : Callable                        = None,
        drop_callback     : Callable                        = None,
        show              : bool                            = True,
        pos               : list[int] | tuple[int, ...]     = [],
        filter_key        : str                             = '',
        tracked           : bool                            = False,
        track_offset      : float                           = 0.5,
        tint_color        : list[float] | tuple[float, ...] = (255, 255, 255, 255),
        border_color      : list[float] | tuple[float, ...] = (0, 0, 0, 0),
        uv_min            : list[float] | tuple[float, ...] = (0.0, 0.0),
        uv_max            : list[float] | tuple[float, ...] = (1.0, 1.0),
        **kwargs
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
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
            tint_color=tint_color,
            border_color=border_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )


class ImageButton(Widget):
    texture_tag      : ItemT                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    width            : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height           : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    indent           : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    source           : ItemT                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    payload_type     : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback    : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback    : Callable                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show             : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos              : list[int] | tuple[int, ...]     = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key       : str                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked          : bool                            = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset     : float                           = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    frame_padding    : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tint_color       : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    background_color : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    border_color     : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    uv_min           : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    uv_max           : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")

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

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvImageButton, "mvImageButton")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_image_button

    def __init__(self,
        texture_tag       : ItemT,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        height            : int                             = 0,
        indent            : int                             = -1,
        parent            : ItemT                           = 0,
        before            : ItemT                           = 0,
        source            : ItemT                           = 0,
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
        frame_padding     : int                             = -1,
        tint_color        : list[float] | tuple[float, ...] = (255, 255, 255, 255),
        background_color  : list[float] | tuple[float, ...] = (0, 0, 0, 0),
        uv_min            : list[float] | tuple[float, ...] = (0.0, 0.0),
        uv_max            : list[float] | tuple[float, ...] = (1.0, 1.0),
        **kwargs
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
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
            frame_padding=frame_padding,
            tint_color=tint_color,
            background_color=background_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )
