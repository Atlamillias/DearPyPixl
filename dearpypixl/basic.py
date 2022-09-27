from typing import Callable, Any
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
]


class RadioButton(WidgetItem):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.

        Args:
            * items (Sequence[Any], optional): A button will be created for each value, storing the
            string representation of each (the values themselves can be of any type, but will be
            converted to strings). The string representation is displayed next to each button.
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
            * default_value (str, optional): A string representation of a value in <items>. It will be
            the initial selection.
            * horizontal (bool, optional): If True, the set of buttons will be displayed horizontally.
            Defaults to False.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvRadioButton, "mvRadioButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_radio_button,
    )

    items         : list[str] | tuple[str, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : str                         = __dearpypixl__.set_information(None, None)
    horizontal    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : str                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
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


class Listbox(WidgetItem):
    """Adds a listbox. If height is not large enough to show all items a scroll bar will appear.

        Args:
            * items (Sequence[Any], optional): The string representation of each value will be displayed
            within this item (the values themselves can be of any type, but will be converted to strings).
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
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
            * default_value (str, optional): A string representation of a value in <items>. It will be
            the initial selection.
            * num_items (int, optional): The number of values to display in this item before needing to
            scroll (affects height).
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvListbox, "mvListbox"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_listbox,
    )

    items         : list[str] | tuple[str, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : str                         = __dearpypixl__.set_information(None, None)
    num_items     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : str                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label: bool                         = True,
        width              : int                         = 0,
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


class Checkbox(WidgetItem):
    """Adds a checkbox.

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
            * default_value (bool, optional): If True, "check" this checkbox item. Defaults to False.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvCheckbox, "mvCheckbox"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_checkbox,
    )

    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : bool                        = __dearpypixl__.set_information(None, None)
    value         : bool                        = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    is_resized                : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked         : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked          : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered                : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active                 : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused                : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked                : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible                : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
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


class Button(WidgetItem):
    """Adds a button.

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
            * small (bool, optional): Shrinks the size of the button to the text of the label it contains. Useful for embedding in text.
            * arrow (bool, optional): Displays an arrow in place of the text string. This requires the direction keyword.
            * direction (int, optional): Sets the cardinal direction for the arrow buy using constants mvDir_Left, mvDir_Up, mvDir_Down, mvDir_Right, mvDir_None. Arrow keyword must be set to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvButton, "mvButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        is_callable=True,
        able_parents=(),
        able_children=(),
        constants=('mvButton', 'mvAll', 'mvTool_About', 'mvTool_Debug', 'mvTool_Doc', 'mvTool_ItemRegistry', 'mvTool_Metrics', 'mvTool_Style', 'mvTool_Font', 'mvFontAtlas', 'mvAppUUID', 'mvInvalidUUID', 'mvDir_None', 'mvDir_Left', 'mvDir_Right', 'mvDir_Up', 'mvDir_Down'),
        command=dearpygui.add_button,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    small         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    arrow         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    direction     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
        width              : int                         = 0,
        height             : int                         = 0,
        indent             : int                         = -1,
        parent             : Item | int                  = 0,
        before             : Item | int                  = 0,
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


class Selectable(WidgetItem):
    """Adds a selectable. Similar to a button but can indicate its selected state.

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
            * default_value (bool, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * span_columns (bool, optional): Forces the selectable to span the width of all columns if placed in a table.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSelectable, "mvSelectable"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_selectable,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : bool                        = __dearpypixl__.set_information(None, None)
    span_columns  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : bool                        = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
    is_toggled_open           : bool           = __dearpypixl__.set_state("get_item_state", None, target="toggled_open")
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


class Combo(WidgetItem):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window. All items will be shown as selectables on the dropdown.

        Args:
            * items (Sequence[Any], optional): The string representation of each value will be displayed
            within this item (the values themselves can be of any type, but will be converted to strings).
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
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
            * popup_align_left (bool, optional): Align the contents on the popup toward the left.
            * no_arrow_button (bool, optional): Display the preview box without the square arrow button indicating dropdown activity.
            * no_preview (bool, optional): Display only the square arrow button and not the selected value.
            * height_mode (int, optional): Controlls the number of items shown in the dropdown by the constants mvComboHeight_Small, mvComboHeight_Regular, mvComboHeight_Large, mvComboHeight_Largest
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvCombo, "mvCombo"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        constants=('mvCombo', 'mvComboHeight_Small', 'mvComboHeight_Regular', 'mvComboHeight_Large', 'mvComboHeight_Largest'),
        command=dearpygui.add_combo,
    )

    items            : list[str] | tuple[str, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    width            : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent           : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source           : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type     : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback         : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback    : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback    : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show             : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos              : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key       : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value    : str                         = __dearpypixl__.set_information(None, None)
    popup_align_left : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_arrow_button  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_preview       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height_mode      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value            : str                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        items              : list[str] | tuple[str, ...] = (),
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        width              : int                         = 0,
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



class SliderFloat(WidgetItem):
    """Adds slider for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.

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
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * vertical (bool, optional): Sets orientation of the slidebar and slider to vertical.
            * no_input (bool, optional): Disable direct entry methods double-click or ctrl+click or Enter key allowing to input text directly into the item.
            * clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            * min_value (float, optional): Applies a limit only to sliding entry only.
            * max_value (float, optional): Applies a limit only to sliding entry only.
            * format (str, optional): Determines the format the float will be displayed as use python string formatting.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSliderFloat, "mvSliderFloat"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_slider_float,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float                       = __dearpypixl__.set_information(None, None)
    vertical      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_input      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    clamped       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    format        : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : float                       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class DragFloat(WidgetItem):
    """Adds drag for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
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
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * format (str, optional): Determines the format the float will be displayed as use python string formatting.
            * speed (float, optional): Sets the sensitivity the float will be modified while dragging.
            * min_value (float, optional): Applies a limit only to draging entry only.
            * max_value (float, optional): Applies a limit only to draging entry only.
            * no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            * clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDragFloat, "mvDragFloat"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_drag_float,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float                       = __dearpypixl__.set_information(None, None)
    format        : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    speed         : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    min_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_value     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_input      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    clamped       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : float                       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class Text(WidgetItem):
    """Adds text. Text can have an optional label that will display to the right of the text.

        Args:
            * default_value (str, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
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
            * wrap (int, optional): Number of pixels from the start of the item until wrapping starts.
            * bullet (bool, optional): Places a bullet to the left of the text.
            * color (list[int] | tuple[int, ...], optional): Color of the text (rgba).
            * show_label (bool, optional): Displays the label to the right of the text.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvText, "mvText"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_text,
    )

    default_value : str                         = __dearpypixl__.set_information(None, None)
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
    wrap          : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    bullet        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show_label    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : str                         = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        default_value      : str                         = '',
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
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


class TabButton(WidgetItem):
    """Adds a tab button to a tab bar.

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
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * no_reorder (bool, optional): Disable reordering this tab or having another tab cross over this tab. Fixes the position of this tab in relation to the order of neighboring tabs at start.
            * leading (bool, optional): Enforce the tab position to the left of the tab bar (after the tab list popup button).
            * trailing (bool, optional): Enforce the tab position to the right of the tab bar (before the scrolling buttons).
            * no_tooltip (bool, optional): Disable tooltip for the given tab.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvTabButton, "mvTabButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTabBar, dearpygui.mvStage,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.add_tab_button,
    )

    indent        : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key    : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_reorder    : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    leading       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    trailing      : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tooltip    : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class MenuItem(WidgetItem):
    """Adds a menu item to an existing menu. Menu items act similar to selectables and has a bool value.
    When placed in a menu the checkmark will reflect its value.

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
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * enabled (bool, optional): If False, prevent interaction with this item through the UI. The
            item will also reflect "disabled" theme elements. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (bool, optional): If True, display a checkmark near the item's label.
            Defaults to False.
            * shortcut (str, optional): Displays text on the menu item. Typically used to show a shortcut key command.
            * check (bool, optional): If True, display a checkmark near the item's label.
            Defaults to False.
            * drag_callback (Callable, optional): (deprecated)
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMenuItem, "mvMenuItem"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_menu_item,
    )

    indent        : int      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key    : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : bool     = __dearpypixl__.set_information(None, None)
    shortcut      : str      = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    check         : bool     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : bool     = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
