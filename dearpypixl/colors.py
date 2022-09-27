from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *


__all__ = [
    "ColorMapRegistry",
    "ColorButton",
    "ColorEdit",
    "ColorPicker",
    "ColorMapScale",
    "ColorMap",
    "ColorMapButton",
    "ColorMapSlider",
]


class ColorMapRegistry(Item):
    """Adds a colormap registry.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorMapRegistry, "mvColorMapRegistry"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvColorMap,),
        command=dearpygui.add_colormap_registry,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class ColorButton(WidgetItem):
    """Adds a color button.

        Args:
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
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
            * no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
            * no_border (bool, optional): Disable border around the image.
            * no_drag_drop (bool, optional): Disable ability to drag and drop small preview (color square) to apply colors to other items.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorButton, "mvColorButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_color_button,
    )

    default_value : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None)
    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_alpha      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_border     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_drag_drop  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 255),
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
        no_alpha           : bool                        = False,
        no_border          : bool                        = False,
        no_drag_drop       : bool                        = False,
        **kwargs
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_border=no_border,
            no_drag_drop=no_drag_drop,
            **kwargs,
        )


class ColorEdit(WidgetItem):
    """Adds an RGBA color editor. Left clicking the small color preview will provide a color picker. Click and draging the small color preview will copy the color to be applied on any other color widget.

        Args:
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
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
            * no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
            * no_picker (bool, optional): Disable picker popup when color square is clicked.
            * no_options (bool, optional): Disable toggling options menu when right-clicking on inputs/small preview.
            * no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            * no_tooltip (bool, optional): Disable tooltip when hovering the preview.
            * no_label (bool, optional): Disable display of inline text label.
            * no_drag_drop (bool, optional): Disable ability to drag and drop small preview (color square) to apply colors to other items.
            * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
            * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            * display_mode (int, optional): mvColorEdit_rgb, mvColorEdit_hsv, or mvColorEdit_hex
            * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
            * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorEdit, "mvColorEdit"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        constants=('mvColorEdit', 'mvColorEdit_AlphaPreviewNone', 'mvColorEdit_AlphaPreview', 'mvColorEdit_AlphaPreviewHalf', 'mvColorEdit_uint8', 'mvColorEdit_float', 'mvColorEdit_rgb', 'mvColorEdit_hsv', 'mvColorEdit_hex', 'mvColorEdit_input_rgb', 'mvColorEdit_input_hsv'),
        command=dearpygui.add_color_edit,
    )

    default_value    : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None)
    width            : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height           : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
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
    no_alpha         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_picker        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_options       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_small_preview : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_inputs        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tooltip       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_label         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_drag_drop     : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    alpha_bar        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    alpha_preview    : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_mode     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_type     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    input_mode       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value            : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 255),
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
        no_alpha           : bool                        = False,
        no_picker          : bool                        = False,
        no_options         : bool                        = False,
        no_small_preview   : bool                        = False,
        no_inputs          : bool                        = False,
        no_tooltip         : bool                        = False,
        no_label           : bool                        = False,
        no_drag_drop       : bool                        = False,
        alpha_bar          : bool                        = False,
        alpha_preview      : int                         = 0,
        display_mode       : int                         = 1048576,
        display_type       : int                         = 8388608,
        input_mode         : int                         = 134217728,
        **kwargs
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_picker=no_picker,
            no_options=no_options,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            no_drag_drop=no_drag_drop,
            alpha_bar=alpha_bar,
            alpha_preview=alpha_preview,
            display_mode=display_mode,
            display_type=display_type,
            input_mode=input_mode,
            **kwargs,
        )


class ColorPicker(WidgetItem):
    """Adds an RGB color picker. Right click the color picker for options. Click and drag the color preview to copy the color and drop on any other color widget to apply. Right Click allows the style of the color picker to be changed.

        Args:
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
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
            * no_alpha (bool, optional): Removes the displayed slider that can change alpha channel.
            * no_side_preview (bool, optional): Disable bigger color preview on right side of the picker, use small colored square preview instead , unless small preview is also hidden.
            * no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            * no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            * no_tooltip (bool, optional): Disable tooltip when hovering the preview.
            * no_label (bool, optional): Disable display of inline text label.
            * alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
            * display_rgb (bool, optional): Override _display_ type among RGB/HSV/Hex.
            * display_hsv (bool, optional): Override _display_ type among RGB/HSV/Hex.
            * display_hex (bool, optional): Override _display_ type among RGB/HSV/Hex.
            * picker_mode (int, optional): mvColorPicker_bar or mvColorPicker_wheel
            * alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            * display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
            * input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorPicker, "mvColorPicker"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        constants=('mvColorPicker', 'mvColorPicker_bar', 'mvColorPicker_wheel'),
        command=dearpygui.add_color_picker,
    )

    default_value    : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None)
    width            : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height           : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
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
    no_alpha         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_side_preview  : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_small_preview : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_inputs        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_tooltip       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    no_label         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    alpha_bar        : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_rgb      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_hsv      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_hex      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    picker_mode      : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    alpha_preview    : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    display_type     : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    input_mode       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value            : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 255),
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
        no_alpha           : bool                        = False,
        no_side_preview    : bool                        = False,
        no_small_preview   : bool                        = False,
        no_inputs          : bool                        = False,
        no_tooltip         : bool                        = False,
        no_label           : bool                        = False,
        alpha_bar          : bool                        = False,
        display_rgb        : bool                        = False,
        display_hsv        : bool                        = False,
        display_hex        : bool                        = False,
        picker_mode        : int                         = 33554432,
        alpha_preview      : int                         = 0,
        display_type       : int                         = 8388608,
        input_mode         : int                         = 134217728,
        **kwargs
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            no_alpha=no_alpha,
            no_side_preview=no_side_preview,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            alpha_bar=alpha_bar,
            display_rgb=display_rgb,
            display_hsv=display_hsv,
            display_hex=display_hex,
            picker_mode=picker_mode,
            alpha_preview=alpha_preview,
            display_type=display_type,
            input_mode=input_mode,
            **kwargs,
        )


def _set_item_colormap(__obj: object, __name: str, value: Any):
    try:
        colormap_uuid = int(value)
    except TypeError:
        raise TypeError(f"{__name!r} must be an instance of `Colormap` (got {type(value).__qualname__!r}).")
    dearpygui.bind_colormap(__obj._tag, colormap_uuid)

class ColorMapScale(WidgetItem):
    """Adds a legend that pairs values with colors. This is typically used with a heat series.

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
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * colormap (int | str, optional): mvPlotColormap_* constants or mvColorMap uuid from a color map registry
            * min_scale (float, optional): Sets the min number of the color scale. Typically is the same as the min scale from the heat series.
            * max_scale (float, optional): Sets the max number of the color scale. Typically is the same as the max scale from the heat series.
            * drag_callback (Callable, optional): (deprecated)
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorMapScale, "mvColorMapScale"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_colormap_scale,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    colormap      : int | str                   = __dearpypixl__.set_configuration(None, _set_item_colormap)
    min_scale     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    max_scale     : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
        source             : Item | int                  = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        colormap           : int | str                   = 0,
        min_scale          : float                       = 0.0,
        max_scale          : float                       = 1.0,
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
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            colormap=colormap,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )


class ColorMap(WidgetItem):
    """Adds a legend that pairs colors with normalized value 0.0->1.0. Each color will be  This is typically used with a heat series. (ex. [[0, 0, 0, 255], [255, 255, 255, 255]] will be mapped to a soft transition from 0.0-1.0)

        Args:
            * colors (Any): colors that will be mapped to the normalized value 0.0->1.0
            * qualitative (bool): Qualitative will create hard transitions for color boundries across the value range when enabled.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorMap, "mvColorMap"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvColorMapRegistry,dearpygui.mvTemplateRegistry),
        able_children=(),
        commands=('bind_colormap', 'sample_colormap', 'get_colormap_color'),
        constants=('mvColorMap', 'mvPlotColormap_Default', 'mvPlotColormap_Deep', 'mvPlotColormap_Dark', 'mvPlotColormap_Pastel', 'mvPlotColormap_Paired', 'mvPlotColormap_Viridis', 'mvPlotColormap_Plasma', 'mvPlotColormap_Hot', 'mvPlotColormap_Cool', 'mvPlotColormap_Pink', 'mvPlotColormap_Jet', 'mvPlotColormap_Twilight', 'mvPlotColormap_RdBu', 'mvPlotColormap_BrBG', 'mvPlotColormap_PiYG', 'mvPlotColormap_Spectral', 'mvPlotColormap_Greys'),
        command=dearpygui.add_colormap,
    )

    colors      : list[list[int] | tuple[int, ...]] = __dearpypixl__.set_configuration(None, None)
    qualitative : bool                              = __dearpypixl__.set_configuration(None, None)
    show        : bool                              = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        colors            : list[list[int] | tuple[int, ...]]      ,
        qualitative       : bool                                         ,
        label             : str                                    = None,
        user_data         : Any                                    = None,
        use_internal_label: bool                                   = True,
        show              : bool                                   = True,
        parent            : Item | int                       = 14  ,
        **kwargs
    ) -> None:
        super().__init__(
            colors=colors,
            qualitative=qualitative,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            parent=parent,
            **kwargs,
        )

    # TODO: Maybe make list-like for access to `colors`.
    def get_color_at_value(self, value: float) -> list[float] | tuple[float, ...]:
        """Return the normalized values of a color from the ColorMap at <value>.
        Up to four values can be returned in the sequence: red, green, blue, alpha.

        Args:
            * value (float): Value of the colormap to sample. Minimum value is 0.0,
            maximum value is 1.0.
        """
        return dearpygui.sample_colormap(self._tag, value)

    def get_color_at_index(self, index: int) -> list[float] | tuple[float, ...]:
        """Return the normalized values of a color from the ColorMap at <index>. For example,
        `index=0` vould return the first color in ColorMap's list of colors (`colors` argument
        used to create this item). Modulo will be performed against the number of items in the
        color list. Up to four values can be returned in the sequence: red, green, blue, alpha.

        Args:
            * index (int): Position of the color in the ColorMap's list of colors to quiey.
        """
        return dearpygui.get_colormap_color(self._tag, index)


class ColorMapButton(WidgetItem):
    """Adds a button that a color map can be bound to.

        Args:
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
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
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorMapButton, "mvColorMapButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_colormap_button,
    )

    default_value : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None)
    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    enabled       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 255),
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
        **kwargs
    ) -> None:
        super().__init__(
            default_value=default_value,
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
            **kwargs,
        )


class ColorMapSlider(WidgetItem):
    """Adds a color slider that a color map can be bound to.

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
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * drag_callback (Callable, optional): (deprecated)
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorMapSlider, "mvColorMapSlider"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_colormap_slider,
    )

    width         : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback      : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    drop_callback : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")
    show          : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key    : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float                       = __dearpypixl__.set_information(None, None)
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
        payload_type       : str                         = '$$DPG_PAYLOAD',
        callback           : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
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
            payload_type=payload_type,
            callback=callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            **kwargs,
        )
