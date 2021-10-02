from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from pixle.itemtypes.widget import Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Slider",
    "Button",
    "Checkbox",
    "ColorButton",
    "ColorEdit",
    "ColorPicker",
    "Colormap",
    "ColormapButton",
    "ColormapScale",
    "ColormapSlider",
    "Combo",
    "DatePicker",
    "DragFloat",
    "DragFloatx",
    "DragInt",
    "DragIntx",
    "DragLine",
    "DynamicTexture",
    "FileExtension",
    "Image",
    "ImageButton",
    "InputFloat",
    "InputFloatx",
    "InputInt",
    "InputIntx",
    "InputText",
    "KnobFloat",
    "Listbox",
    "LoadingIndicator",
    "MenuItem",
    "ProgressBar",
    "RadioButton",
    "RawTexture",
    "Selectable",
    "Separator",
    "SliderFloat",
    "SliderFloatx",
    "SliderInt",
    "SliderIntx",
    "Spacer",
    "StaticTexture",
    "TabButton",
    "Text",
    "TimePicker",
]


class Slider(Widget):
    """Adds a 3D box slider.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[float], Tuple[float]], optional): 
            max_x (float, optional): Applies upper limit to slider.
            max_y (float, optional): Applies upper limit to slider.
            max_z (float, optional): Applies upper limit to slider.
            min_x (float, optional): Applies lower limit to slider.
            min_y (float, optional): Applies lower limit to slider.
            min_z (float, optional): Applies lower limit to slider.
            scale (float, optional): Size of the widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_3d_slider

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        max_x: float = 100.0, 
        max_y: float = 100.0, 
        max_z: float = 100.0, 
        min_x: float = 0.0, 
        min_y: float = 0.0, 
        min_z: float = 0.0, 
        scale: float = 1.0, 
        **kwargs, 
    ):
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
            value=value,
            max_x=max_x,
            max_y=max_y,
            max_z=max_z,
            min_x=min_x,
            min_y=min_y,
            min_z=min_z,
            scale=scale,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z
        self.scale = scale


class Button(Widget):
    """Adds a button.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            small (bool, optional): Small button, useful for embedding in text.
            arrow (bool, optional): Arrow button, requires the direction keyword.
            direction (int, optional): A cardinal direction for arrow.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_button

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        small: bool = False, 
        arrow: bool = False, 
        direction: int = 0, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.small = small
        self.arrow = arrow
        self.direction = direction


class Checkbox(Widget):
    """Adds a checkbox.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_checkbox

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value


class ColorButton(Widget):
    """Adds a color button.
    
    Args:
            default_value (Union[List[int], Tuple[int]], optional): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_alpha (bool, optional): Ignore Alpha component.
            no_border (bool, optional): Disable border around the image.
            no_drag_drop (bool, optional): Disable display of inline text label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_color_button

    def __init__(
        self, 
        value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        no_alpha: bool = False, 
        no_border: bool = False, 
        no_drag_drop: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            value=value,
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
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_border = no_border
        self.no_drag_drop = no_drag_drop


class ColorEdit(Widget):
    """Adds an RGBA color editor. Click the small color preview will provide a color picker. Click and draging the small color preview will copy the color to be applied on any other color widget.
    
    Args:
            default_value (Union[List[int], Tuple[int]], optional): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_alpha (bool, optional): Disable Alpha component.
            no_picker (bool, optional): Disable picker popup when color square is clicked.
            no_options (bool, optional): Disable toggling options menu when right-clicking on inputs/small preview.
            no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            no_tooltip (bool, optional): Disable tooltip when hovering the preview.
            no_label (bool, optional): Disable display of inline text label.
            no_drag_drop (bool, optional): Disable ability to drag and drop small preview (color square) to apply colors.
            alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
            alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            display_mode (int, optional): mvColorEdit_rgb, mvColorEdit_hsv, or mvColorEdit_hex
            display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
            input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_color_edit

    def __init__(
        self, 
        value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        no_alpha: bool = False, 
        no_picker: bool = False, 
        no_options: bool = False, 
        no_small_preview: bool = False, 
        no_inputs: bool = False, 
        no_tooltip: bool = False, 
        no_label: bool = False, 
        no_drag_drop: bool = False, 
        alpha_bar: bool = False, 
        alpha_preview: int = 0, 
        display_mode: int = 1048576, 
        display_type: int = 8388608, 
        input_mode: int = 134217728, 
        **kwargs, 
    ):
        super().__init__(
            value=value,
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
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_picker = no_picker
        self.no_options = no_options
        self.no_small_preview = no_small_preview
        self.no_inputs = no_inputs
        self.no_tooltip = no_tooltip
        self.no_label = no_label
        self.no_drag_drop = no_drag_drop
        self.alpha_bar = alpha_bar
        self.alpha_preview = alpha_preview
        self.display_mode = display_mode
        self.display_type = display_type
        self.input_mode = input_mode


class ColorPicker(Widget):
    """Adds an RGB color picker. Right click the color picker for options. Click and drag the color preview to copy the color and drop on any other color widget to apply. Right Click allows the style of the color picker to be changed.
    
    Args:
            default_value (Union[List[int], Tuple[int]], optional): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_alpha (bool, optional): Ignore Alpha component.
            no_side_preview (bool, optional): Disable bigger color preview on right side of the picker, use small colored square preview instead , unless small preview is also hidden.
            no_small_preview (bool, optional): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            no_inputs (bool, optional): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            no_tooltip (bool, optional): Disable tooltip when hovering the preview.
            no_label (bool, optional): Disable display of inline text label.
            alpha_bar (bool, optional): Show vertical alpha bar/gradient in picker.
            display_rgb (bool, optional): Override _display_ type among RGB/HSV/Hex.
            display_hsv (bool, optional): Override _display_ type among RGB/HSV/Hex.
            display_hex (bool, optional): Override _display_ type among RGB/HSV/Hex.
            picker_mode (int, optional): mvColorPicker_bar or mvColorPicker_wheel
            alpha_preview (int, optional): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            display_type (int, optional): mvColorEdit_uint8 or mvColorEdit_float
            input_mode (int, optional): mvColorEdit_input_rgb or mvColorEdit_input_hsv
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_color_picker

    def __init__(
        self, 
        value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        no_alpha: bool = False, 
        no_side_preview: bool = False, 
        no_small_preview: bool = False, 
        no_inputs: bool = False, 
        no_tooltip: bool = False, 
        no_label: bool = False, 
        alpha_bar: bool = False, 
        display_rgb: bool = False, 
        display_hsv: bool = False, 
        display_hex: bool = False, 
        picker_mode: int = 33554432, 
        alpha_preview: int = 0, 
        display_type: int = 8388608, 
        input_mode: int = 134217728, 
        **kwargs, 
    ):
        super().__init__(
            value=value,
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
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_side_preview = no_side_preview
        self.no_small_preview = no_small_preview
        self.no_inputs = no_inputs
        self.no_tooltip = no_tooltip
        self.no_label = no_label
        self.alpha_bar = alpha_bar
        self.display_rgb = display_rgb
        self.display_hsv = display_hsv
        self.display_hex = display_hex
        self.picker_mode = picker_mode
        self.alpha_preview = alpha_preview
        self.display_type = display_type
        self.input_mode = input_mode


class Colormap(Widget):
    """Adds a legend that pairs values with colors. This is typically used with a heat series.
    
    Args:
            colors (Any): 
            qualitative (bool): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_colormap

    def __init__(
        self, 
        colors: List[List[int]], 
        qualitative: bool, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = True, 
        parent: Union[int, str] = 14, 
        **kwargs, 
    ):
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
        self.colors = colors
        self.qualitative = qualitative
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.show = show
        self.parent = parent


class ColormapButton(Widget):
    """Adds a color button.
    
    Args:
            default_value (Union[List[int], Tuple[int]], optional): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_alpha (bool, optional): Ignore Alpha component.
            no_border (bool, optional): Disable border around the image.
            no_drag_drop (bool, optional): Disable display of inline text label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_colormap_button

    def __init__(
        self, 
        value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        no_alpha: bool = False, 
        no_border: bool = False, 
        no_drag_drop: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            value=value,
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
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_border = no_border
        self.no_drag_drop = no_drag_drop


class ColormapScale(Widget):
    """Adds a legend that pairs values with colors. This is typically used with a heat series. 
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            colormap (Union[int, str], optional): mvPlotColormap_* constants or mvColorMap uuid
            min_scale (float, optional): Sets the min number of the color scale. Typically is the same as the min scale from the heat series.
            max_scale (float, optional): Sets the max number of the color scale. Typically is the same as the max scale from the heat series.
            id (Union[int, str], optional): (deprecated) 
            drag_callback (Callable, optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_colormap_scale

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        colormap: Union[int, str] = 0, 
        min_scale: float = 0.0, 
        max_scale: float = 1.0, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.colormap = colormap
        self.min_scale = min_scale
        self.max_scale = max_scale


class ColormapSlider(Widget):
    """Adds a color button.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (float, optional): 
            id (Union[int, str], optional): (deprecated) 
            drag_callback (Callable, optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_colormap_slider

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: float = 0.0, 
        **kwargs, 
    ):
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
            value=value,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value


class Combo(Widget):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window.
    
    Args:
            items (Union[List[str], Tuple[str]], optional): A tuple of items to be shown in the drop down window. Can consist of any combination of types.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (str, optional): 
            popup_align_left (bool, optional): Align the popup toward the left.
            no_arrow_button (bool, optional): Display the preview box without the square arrow button.
            no_preview (bool, optional): Display only the square arrow button.
            height_mode (int, optional): mvComboHeight_Small, _Regular, _Large, _Largest
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_combo

    def __init__(
        self, 
        items: Union[List[str], Tuple[str, ...]] = (), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: str = '', 
        popup_align_left: bool = False, 
        no_arrow_button: bool = False, 
        no_preview: bool = False, 
        height_mode: int = 1, 
        **kwargs, 
    ):
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
            value=value,
            popup_align_left=popup_align_left,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
            height_mode=height_mode,
            **kwargs,
        )
        self.items = items
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.popup_align_left = popup_align_left
        self.no_arrow_button = no_arrow_button
        self.no_preview = no_preview
        self.height_mode = height_mode


class DatePicker(Widget):
    """Adds a data picker.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (dict, optional): 
            level (int, optional): Use avaliable constants. mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_date_picker

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: dict = {'month_day': 14, 'year': 20, 'month': 5}, 
        level: int = 0, 
        **kwargs, 
    ):
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
            value=value,
            level=level,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.level = level


class DragFloat(Widget):
    """Adds drag for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (float, optional): 
            format (str, optional): 
            speed (float, optional): 
            min_value (float, optional): Applies a limit only to draging entry only.
            max_value (float, optional): Applies a limit only to draging entry only.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_float

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: float = 0.0, 
        format: str = '%0.3f', 
        speed: float = 1.0, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        no_input: bool = False, 
        clamped: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragFloatx(Widget):
    """Adds drag input for a set of float values up to 4. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[float], Tuple[float]], optional): 
            size (int, optional): Number of components
            format (str, optional): 
            speed (float, optional): 
            min_value (float, optional): Applies a limit only to draging entry only.
            max_value (float, optional): Applies a limit only to draging entry only.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_floatx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        size: int = 4, 
        format: str = '%0.3f', 
        speed: float = 1.0, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        no_input: bool = False, 
        clamped: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            size=size,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.size = size
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragInt(Widget):
    """Adds drag for a single int value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (int, optional): 
            format (str, optional): 
            speed (float, optional): 
            min_value (int, optional): Applies a limit only to draging entry only.
            max_value (int, optional): Applies a limit only to draging entry only.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_int

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: int = 0, 
        format: str = '%d', 
        speed: float = 1.0, 
        min_value: int = 0, 
        max_value: int = 100, 
        no_input: bool = False, 
        clamped: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragIntx(Widget):
    """Adds drag input for a set of int values up to 4. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[int], Tuple[int]], optional): 
            size (int, optional): Number of components.
            format (str, optional): 
            speed (float, optional): 
            min_value (int, optional): Applies a limit only to draging entry only.
            max_value (int, optional): Applies a limit only to draging entry only.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_intx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[int], Tuple[int]] = (0, 0, 0, 0), 
        size: int = 4, 
        format: str = '%d', 
        speed: float = 1.0, 
        min_value: int = 0, 
        max_value: int = 100, 
        no_input: bool = False, 
        clamped: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            size=size,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.size = size
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragLine(Widget):
    """Adds a drag line to a plot.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            default_value (Any, optional): 
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            show_label (bool, optional): 
            vertical (bool, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drag_line

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        value: Any = 0.0, 
        color: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        show_label: bool = True, 
        vertical: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            value=value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            vertical=vertical,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.value = value
        self.color = color
        self.thickness = thickness
        self.show_label = show_label
        self.vertical = vertical


class DynamicTexture(Widget):
    """Adds a dynamic texture.
    
    Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_dynamic_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        value: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            value=value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class FileExtension(Widget):
    """Creates a file extension filter option in the file dialog.
    
    Args:
            extension (str): Extension that will show as an when the parent is a file dialog.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            custom_text (str, optional): Replaces the displayed text in the drop down for this extension.
            color (Union[List[float], Tuple[float]], optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_file_extension

    def __init__(
        self, 
        extension: str, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        custom_text: str = '', 
        color: Union[List[float], Tuple[float]] = (-255, 0, 0, 255), 
        **kwargs, 
    ):
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
        self.extension = extension
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.parent = parent
        self.before = before
        self.custom_text = custom_text
        self.color = color


class Image(Widget):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) for texture coordinates will generally display the entire texture.
    
    Args:
            texture_id (Union[int, str]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            tint_color (Union[List[float], Tuple[float]], optional): Applies a color tint to the entire texture.
            border_color (Union[List[float], Tuple[float]], optional): Displays a border of the specified color around the texture.
            uv_min (Union[List[float], Tuple[float]], optional): Normalized texture coordinates min point.
            uv_max (Union[List[float], Tuple[float]], optional): Normalized texture coordinates max point.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_image

    def __init__(
        self, 
        texture_id: Union[int, str], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        tint_color: Union[List[float], Tuple[float]] = (255, 255, 255, 255), 
        border_color: Union[List[float], Tuple[float]] = (0, 0, 0, 0), 
        uv_min: Union[List[float], Tuple[float]] = (0.0, 0.0), 
        uv_max: Union[List[float], Tuple[float]] = (1.0, 1.0), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
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
        self.texture_id = texture_id
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.tint_color = tint_color
        self.border_color = border_color
        self.uv_min = uv_min
        self.uv_max = uv_max


class ImageButton(Widget):
    """Adds an button with a texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) texture coordinates will generally display the entire texture
    
    Args:
            texture_id (Union[int, str]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            frame_padding (int, optional): 
            tint_color (Union[List[float], Tuple[float]], optional): Applies a color tint to the entire texture.
            background_color (Union[List[float], Tuple[float]], optional): Displays a border of the specified color around the texture.
            uv_min (Union[List[float], Tuple[float]], optional): Normalized texture coordinates min point.
            uv_max (Union[List[float], Tuple[float]], optional): Normalized texture coordinates max point.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_image_button

    def __init__(
        self, 
        texture_id: Union[int, str], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        frame_padding: int = -1, 
        tint_color: Union[List[float], Tuple[float]] = (255, 255, 255, 255), 
        background_color: Union[List[float], Tuple[float]] = (0, 0, 0, 0), 
        uv_min: Union[List[float], Tuple[float]] = (0.0, 0.0), 
        uv_max: Union[List[float], Tuple[float]] = (1.0, 1.0), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
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
        self.texture_id = texture_id
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.frame_padding = frame_padding
        self.tint_color = tint_color
        self.background_color = background_color
        self.uv_min = uv_min
        self.uv_max = uv_max


class InputFloat(Widget):
    """Adds input for an float.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (float, optional): 
            format (str, optional): 
            min_value (float, optional): Value for lower limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            max_value (float, optional): Value for upper limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            step (float, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
            step_fast (float, optional): After holding the step buttons for extended time the increments will switch to this value.
            min_clamped (bool, optional): Activates and deactivates min_value.
            max_clamped (bool, optional): Activates and deactivates max_value.
            on_enter (bool, optional): Only runs callback on enter key press.
            readonly (bool, optional): Activates a read only mode for the input.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_input_float

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: float = 0.0, 
        format: str = '%.3f', 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        step: float = 0.1, 
        step_fast: float = 1.0, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.format = format
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.step_fast = step_fast
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputFloatx(Widget):
    """Adds multi float input for up to 4 float values.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[float], Tuple[float]], optional): 
            format (str, optional): 
            min_value (float, optional): Value for lower limit of input for each cell. Use clamped to turn on.
            max_value (float, optional): Value for upper limit of input for each cell. Use clamped to turn on.
            size (int, optional): Number of components.
            min_clamped (bool, optional): Activates and deactivates min_value.
            max_clamped (bool, optional): Activates and deactivates max_value.
            on_enter (bool, optional): Only runs callback on enter key press.
            readonly (bool, optional): Activates a read only mode for the inputs.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_input_floatx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        format: str = '%.3f', 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        size: int = 4, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.format = format
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputInt(Widget):
    """Adds input for an int.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (int, optional): 
            min_value (int, optional): Value for lower limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            max_value (int, optional): Value for upper limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            step (int, optional): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
            step_fast (int, optional): After holding the step buttons for extended time the increments will switch to this value.
            min_clamped (bool, optional): Activates and deactivates min_value.
            max_clamped (bool, optional): Activates and deactivates max_value.
            on_enter (bool, optional): Only runs callback on enter key press.
            readonly (bool, optional): Activates a read only mode for the input.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_input_int

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: int = 0, 
        min_value: int = 0, 
        max_value: int = 100, 
        step: int = 1, 
        step_fast: int = 100, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.step_fast = step_fast
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputIntx(Widget):
    """Adds multi int input for up to 4 integer values.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[int], Tuple[int]], optional): 
            min_value (int, optional): Value for lower limit of input for each cell. Use clamped to turn on.
            max_value (int, optional): Value for upper limit of input for each cell. Use clamped to turn on.
            size (int, optional): Number of components.
            min_clamped (bool, optional): Activates and deactivates min_value.
            max_clamped (bool, optional): Activates and deactivates max_value.
            on_enter (bool, optional): Only runs callback on enter.
            readonly (bool, optional): Activates a read only mode for the inputs.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_input_intx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[int], Tuple[int]] = (0, 0, 0, 0), 
        min_value: int = 0, 
        max_value: int = 100, 
        size: int = 4, 
        min_clamped: bool = False, 
        max_clamped: bool = False, 
        on_enter: bool = False, 
        readonly: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputText(Widget):
    """Adds input for text.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (str, optional): 
            hint (str, optional): Displayed only when value is empty string. Will reappear if input value is set to empty string. Will not show if default value is anything other than default empty string.
            multiline (bool, optional): Allows for multiline text input.
            no_spaces (bool, optional): Filter out spaces and tabs.
            uppercase (bool, optional): Automatically make all inputs uppercase.
            tab_input (bool, optional): Allows tabs to be input instead of changing widget focus.
            decimal (bool, optional): Only allow 0123456789.+-*/
            hexadecimal (bool, optional): Only allow 0123456789ABCDEFabcdef
            readonly (bool, optional): Activates read only mode.
            password (bool, optional): Password mode, display all characters as '*'.
            scientific (bool, optional): Only allow 0123456789.+-*/eE (Scientific notation input)
            on_enter (bool, optional): Only runs callback on enter key press.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_input_text

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: str = '', 
        hint: str = '', 
        multiline: bool = False, 
        no_spaces: bool = False, 
        uppercase: bool = False, 
        tab_input: bool = False, 
        decimal: bool = False, 
        hexadecimal: bool = False, 
        readonly: bool = False, 
        password: bool = False, 
        scientific: bool = False, 
        on_enter: bool = False, 
        **kwargs, 
    ):
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
            value=value,
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.hint = hint
        self.multiline = multiline
        self.no_spaces = no_spaces
        self.uppercase = uppercase
        self.tab_input = tab_input
        self.decimal = decimal
        self.hexadecimal = hexadecimal
        self.readonly = readonly
        self.password = password
        self.scientific = scientific
        self.on_enter = on_enter


class KnobFloat(Widget):
    """Adds a knob that rotates based on change in x mouse position.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (float, optional): 
            min_value (float, optional): Applies lower limit to value.
            max_value (float, optional): Applies upper limit to value.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_knob_float

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: float = 0.0, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        **kwargs, 
    ):
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
            value=value,
            min_value=min_value,
            max_value=max_value,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.min_value = min_value
        self.max_value = max_value


class Listbox(Widget):
    """Adds a listbox. If height is not large enought to show all items a scroll bar will appear.
    
    Args:
            items (Union[List[str], Tuple[str]], optional): A tuple of items to be shown in the listbox. Can consist of any combination of types.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (str, optional): 
            num_items (int, optional): Expands the height of the listbox to show specified number of items.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_listbox

    def __init__(
        self, 
        items: Union[List[str], Tuple[str, ...]] = (), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: str = '', 
        num_items: int = 3, 
        **kwargs, 
    ):
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
            value=value,
            num_items=num_items,
            **kwargs,
        )
        self.items = items
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.num_items = num_items


class LoadingIndicator(Widget):
    """Adds a rotating animated loading symbol.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            style (int, optional): 0 is rotating dots style, 1 is rotating bar style.
            circle_count (int, optional): Number of dots show if dots or size of circle if circle.
            speed (float, optional): Speed the anamation will rotate.
            radius (float, optional): Radius size of the loading indicator.
            thickness (float, optional): Thickness of the circles or line.
            color (Union[List[int], Tuple[int]], optional): Color of the growing center circle.
            secondary_color (Union[List[int], Tuple[int]], optional): Background of the dots in dot mode.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_loading_indicator

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        style: int = 0, 
        circle_count: int = 8, 
        speed: float = 1.0, 
        radius: float = 3.0, 
        thickness: float = 1.0, 
        color: Union[List[int], Tuple[int]] = (51, 51, 55, 255), 
        secondary_color: Union[List[int], Tuple[int]] = (29, 151, 236, 103), 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.style = style
        self.circle_count = circle_count
        self.speed = speed
        self.radius = radius
        self.thickness = thickness
        self.color = color
        self.secondary_color = secondary_color


class MenuItem(Widget):
    """Adds a menu item to an existing menu. Menu items act similar to selectables.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (bool, optional): 
            shortcut (str, optional): Displays text on the menu item. Typically used to show a shortcut key command.
            check (bool, optional): Displays a checkmark on the menu item when it is selected.
            id (Union[int, str], optional): (deprecated) 
            drag_callback (Callable, optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_menu_item

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: bool = False, 
        shortcut: str = '', 
        check: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            shortcut=shortcut,
            check=check,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.shortcut = shortcut
        self.check = check


class ProgressBar(Widget):
    """Adds a progress bar.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            overlay (str, optional): Overlayed text.
            default_value (float, optional): Normalized value to fill the bar from 0.0 to 1.0.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_progress_bar

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        overlay: str = '', 
        value: float = 0.0, 
        **kwargs, 
    ):
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
            value=value,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.overlay = overlay
        self.value = value


class RadioButton(Widget):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.
    
    Args:
            items (Union[List[str], Tuple[str]], optional): A tuple of items to be shown as radio options. Can consist of any combination of types.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (str, optional): 
            horizontal (bool, optional): Displays the radio options horizontally.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_radio_button

    def __init__(
        self, 
        items: Union[List[str], Tuple[str, ...]] = (), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: str = '', 
        horizontal: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            horizontal=horizontal,
            **kwargs,
        )
        self.items = items
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.horizontal = horizontal


class RawTexture(Widget):
    """Adds a raw texture.
    
    Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            format (int, optional): Data format.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_raw_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        value: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        format: int = 0, 
        parent: Union[int, str] = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            value=value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            format=format,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.format = format
        self.parent = parent


class Selectable(Widget):
    """Adds a selectable.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (bool, optional): 
            span_columns (bool, optional): Span the width of all columns if placed in a table.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_selectable

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: bool = False, 
        span_columns: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            span_columns=span_columns,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.span_columns = span_columns


class Separator(Widget):
    """Adds a horizontal separator.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_separator

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos


class SliderFloat(Widget):
    """Adds slider for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (float, optional): 
            vertical (bool, optional): Sets orientation to vertical.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            min_value (float, optional): Applies a limit only to sliding entry only.
            max_value (float, optional): Applies a limit only to sliding entry only.
            format (str, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_slider_float

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: float = 0.0, 
        vertical: bool = False, 
        no_input: bool = False, 
        clamped: bool = False, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        format: str = '%.3f', 
        **kwargs, 
    ):
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
            value=value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderFloatx(Widget):
    """Adds multi slider for up to 4 float values. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[float], Tuple[float]], optional): 
            size (int, optional): Number of components.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            min_value (float, optional): Applies a limit only to sliding entry only.
            max_value (float, optional): Applies a limit only to sliding entry only.
            format (str, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_slider_floatx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        size: int = 4, 
        no_input: bool = False, 
        clamped: bool = False, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        format: str = '%.3f', 
        **kwargs, 
    ):
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
            value=value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderInt(Widget):
    """Adds slider for a single int value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (int, optional): 
            vertical (bool, optional): Sets orientation to vertical.
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            min_value (int, optional): Applies a limit only to sliding entry only.
            max_value (int, optional): Applies a limit only to sliding entry only.
            format (str, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_slider_int

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: int = 0, 
        vertical: bool = False, 
        no_input: bool = False, 
        clamped: bool = False, 
        min_value: int = 0, 
        max_value: int = 100, 
        format: str = '%d', 
        **kwargs, 
    ):
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
            value=value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderIntx(Widget):
    """Adds multi slider for up to 4 int values. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (Union[List[int], Tuple[int]], optional): 
            size (int, optional): number of components
            no_input (bool, optional): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            clamped (bool, optional): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            min_value (int, optional): Applies a limit only to sliding entry only.
            max_value (int, optional): Applies a limit only to sliding entry only.
            format (str, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_slider_intx

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: Union[List[int], Tuple[int]] = (0, 0, 0, 0), 
        size: int = 4, 
        no_input: bool = False, 
        clamped: bool = False, 
        min_value: int = 0, 
        max_value: int = 100, 
        format: str = '%d', 
        **kwargs, 
    ):
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
            value=value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class Spacer(Widget):
    """Adds a spacer.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_spacer

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos


class StaticTexture(Widget):
    """Adds a static texture.
    
    Args:
            width (int): 
            height (int): 
            default_value (Union[List[float], Tuple[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_static_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        value: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            value=value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class TabButton(Widget):
    """Adds a tab button to a tab bar.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            no_reorder (bool, optional): Disable reordering this tab or having another tab cross over this tab.
            leading (bool, optional): Enforce the tab position to the left of the tab bar (after the tab list popup button).
            trailing (bool, optional): Enforce the tab position to the right of the tab bar (before the scrolling buttons).
            no_tooltip (bool, optional): Disable tooltip for the given tab.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_tab_button

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        no_reorder: bool = False, 
        leading: bool = False, 
        trailing: bool = False, 
        no_tooltip: bool = False, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip


class Text(Widget):
    """Adds text. Text can have an optional label that will display to the right of the text.
    
    Args:
            default_value (str, optional): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            wrap (int, optional): Number of pixels until wrapping starts.
            bullet (bool, optional): Makes the text bulleted.
            color (Union[List[float], Tuple[float]], optional): Color of the text (rgba).
            show_label (bool, optional): Displays the label.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_text

    def __init__(
        self, 
        value: str = '', 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        source: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        wrap: int = -1, 
        bullet: bool = False, 
        color: Union[List[float], Tuple[float]] = (-1, -1, -1, -1), 
        show_label: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            value=value,
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
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.wrap = wrap
        self.bullet = bullet
        self.color = color
        self.show_label = show_label


class TimePicker(Widget):
    """Adds a time picker.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            callback (Callable, optional): Registers a callback.
            drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            default_value (dict, optional): 
            hour24 (bool, optional): Show 24 hour clock instead of 12 hour.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_time_picker

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        indent: int = -1, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        value: dict = {'hour': 14, 'min': 32, 'sec': 23}, 
        hour24: bool = False, 
        **kwargs, 
    ):
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
            value=value,
            hour24=hour24,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.value = value
        self.hour24 = hour24
