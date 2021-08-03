from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.widget import Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Slider",
    "Button",
    "CharRemap",
    "Checkbox",
    "ColorButton",
    "ColorEdit",
    "ColorPicker",
    "ColormapScale",
    "Combo",
    "DatePicker",
    "DragFloat",
    "DragFloatx",
    "DragInt",
    "DragIntx",
    "DragLine",
    "Dummy",
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
    "SameLine",
    "Selectable",
    "Separator",
    "SliderFloat",
    "SliderFloatx",
    "SliderInt",
    "SliderIntx",
    "Spacing",
    "StaticTexture",
    "TabButton",
    "TableColumn",
    "TableNextColumn",
    "Text",
    "TimePicker",
]


class Slider(Widget):
    """Adds a 3D box slider that allows a 3d point to be show in 2d represented cube space.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[float]): 
            **max_x (float): Applies upper limit to slider.
            **max_y (float): Applies upper limit to slider.
            **max_z (float): Applies upper limit to slider.
            **min_x (float): Applies lower limit to slider.
            **min_y (float): Applies lower limit to slider.
            **min_z (float): Applies lower limit to slider.
            **scale (float): Size of the widget.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_3d_slider

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
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
            user_data=user_data,
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
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **small (bool): Small button, useful for embedding in text.
            **arrow (bool): Arrow button, requires the direction keyword.
            **direction (int): A cardinal direction for arrow.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_button

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        small: bool = False, 
        arrow: bool = False, 
        direction: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            small=small,
            arrow=arrow,
            direction=direction,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.small = small
        self.arrow = arrow
        self.direction = direction


class CharRemap(Widget):
    """Undocumented function
    Args:
            source (int): 
            target (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_char_remap

    def __init__(
        self, 
        source: int, 
        target: int, 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            source=source,
            target=target,
            label=label,
            parent=parent,
            user_data=user_data,
            **kwargs,
        )
        self.source = source
        self.target = target
        self.label = label
        self.parent = parent
        self.user_data = user_data


class Checkbox(Widget):
    """Adds a checkbox.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_checkbox

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value


class ColorButton(Widget):
    """Adds a color button.
    Args:
            *default_value (List[int]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **no_alpha (bool): Ignore Alpha component.
            **no_border (bool): Disable border around the image.
            **no_drag_drop (bool): Disable display of inline text label.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_color_button

    def __init__(
        self, 
        default_value: list[int] = (0, 0, 0, 255), 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        no_alpha: bool = False, 
        no_border: bool = False, 
        no_drag_drop: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            default_value=default_value,
            label=label,
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
            user_data=user_data,
            no_alpha=no_alpha,
            no_border=no_border,
            no_drag_drop=no_drag_drop,
            **kwargs,
        )
        self.default_value = default_value
        self.label = label
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
        self.user_data = user_data
        self.no_alpha = no_alpha
        self.no_border = no_border
        self.no_drag_drop = no_drag_drop


class ColorEdit(Widget):
    """Adds an RGBA color editor. Click the small color preview will provide a color picker. Click and draging the small color preview will copy the color to be applied on any other color widget.
    Args:
            *default_value (List[int]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **no_alpha (bool): Disable Alpha component.
            **no_picker (bool): Disable picker popup when color square is clicked.
            **no_options (bool): Disable toggling options menu when right-clicking on inputs/small preview.
            **no_small_preview (bool): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            **no_inputs (bool): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            **no_tooltip (bool): Disable tooltip when hovering the preview.
            **no_label (bool): Disable display of inline text label.
            **no_drag_drop (bool): Disable ability to drag and drop small preview (color square) to apply colors.
            **alpha_bar (bool): Show vertical alpha bar/gradient in picker.
            **alpha_preview (int): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            **display_mode (int): mvColorEdit_rgb, mvColorEdit_hsv, or mvColorEdit_hex
            **display_type (int): mvColorEdit_uint8 or mvColorEdit_float
            **input_mode (int): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_color_edit

    def __init__(
        self, 
        default_value: list[int] = (0, 0, 0, 255), 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
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
            default_value=default_value,
            label=label,
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
            user_data=user_data,
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
        self.default_value = default_value
        self.label = label
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
        self.user_data = user_data
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
            *default_value (List[int]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **no_alpha (bool): Ignore Alpha component.
            **no_side_preview (bool): Disable bigger color preview on right side of the picker, use small colored square preview instead , unless small preview is also hidden.
            **no_small_preview (bool): Disable colored square preview next to the inputs. (e.g. to show only the inputs). This only displays if the side preview is not shown.
            **no_inputs (bool): Disable inputs sliders/text widgets. (e.g. to show only the small preview colored square)
            **no_tooltip (bool): Disable tooltip when hovering the preview.
            **no_label (bool): Disable display of inline text label.
            **alpha_bar (bool): Show vertical alpha bar/gradient in picker.
            **display_rgb (bool): Override _display_ type among RGB/HSV/Hex.
            **display_hsv (bool): Override _display_ type among RGB/HSV/Hex.
            **display_hex (bool): Override _display_ type among RGB/HSV/Hex.
            **picker_mode (int): mvColorPicker_bar or mvColorPicker_wheel
            **alpha_preview (int): mvColorEdit_AlphaPreviewNone, mvColorEdit_AlphaPreview, or mvColorEdit_AlphaPreviewHalf
            **display_type (int): mvColorEdit_uint8 or mvColorEdit_float
            **input_mode (int): mvColorEdit_input_rgb or mvColorEdit_input_hsv
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_color_picker

    def __init__(
        self, 
        default_value: list[int] = (0, 0, 0, 255), 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
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
            default_value=default_value,
            label=label,
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
            user_data=user_data,
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
        self.default_value = default_value
        self.label = label
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
        self.user_data = user_data
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


class ColormapScale(Widget):
    """Adds a legend that pairs values with colors. This is typically used with a heat series. 
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **user_data (Any): User data for callbacks.
            **default_value (int): 
            **min_scale (float): Sets the min number of the color scale. Typically is the same as the min scale from the heat series.
            **max_scale (float): Sets the max number of the color scale. Typically is the same as the max scale from the heat series.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_colormap_scale

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        user_data: Any = None, 
        default_value: int = 0, 
        min_scale: float = 0.0, 
        max_scale: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            pos=pos,
            user_data=user_data,
            default_value=default_value,
            min_scale=min_scale,
            max_scale=max_scale,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.pos = pos
        self.user_data = user_data
        self.default_value = default_value
        self.min_scale = min_scale
        self.max_scale = max_scale


class Combo(Widget):
    """Adds a combo dropdown that allows a user to select a single option from a drop down window.
    Args:
            *items (List[str]): A tuple of items to be shown in the drop down window. Can consist of any combination of types.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (str): 
            **popup_align_left (bool): Align the popup toward the left.
            **no_arrow_button (bool): Display the preview box without the square arrow button.
            **no_preview (bool): Display only the square arrow button.
            **height_mode (int): mvComboHeight_Small, _Regular, _Large, _Largest
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_combo

    def __init__(
        self, 
        items: list[str] = (), 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: str = '', 
        popup_align_left: bool = False, 
        no_arrow_button: bool = False, 
        no_preview: bool = False, 
        height_mode: int = 1, 
        **kwargs, 
    ):
        super().__init__(
            items=items,
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            popup_align_left=popup_align_left,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
            height_mode=height_mode,
            **kwargs,
        )
        self.items = items
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.popup_align_left = popup_align_left
        self.no_arrow_button = no_arrow_button
        self.no_preview = no_preview
        self.height_mode = height_mode


class DatePicker(Widget):
    """Creates a date picker.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (dict): 
            **level (int): Use avaliable constants. mvDatePickerLevel_Day, mvDatePickerLevel_Month, mvDatePickerLevel_Year
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_date_picker

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: dict = {'month_day': 14, 'year': 20, 'month': 5}, 
        level: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            level=level,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.level = level


class DragFloat(Widget):
    """Adds drag for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (float): 
            **format (str): 
            **speed (float): 
            **min_value (float): Applies a limit only to draging entry only.
            **max_value (float): Applies a limit only to draging entry only.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_float

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: float = 0.0, 
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
            user_data=user_data,
            default_value=default_value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragFloatx(Widget):
    """Adds drag input for a set of int values up to 4. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[float]): 
            **size (int): Number of components
            **format (str): 
            **speed (float): 
            **min_value (float): Applies a limit only to draging entry only.
            **max_value (float): Applies a limit only to draging entry only.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_floatx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
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
            user_data=user_data,
            default_value=default_value,
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (int): 
            **format (str): 
            **speed (float): 
            **min_value (int): Applies a limit only to draging entry only.
            **max_value (int): Applies a limit only to draging entry only.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_int

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: int = 0, 
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
            user_data=user_data,
            default_value=default_value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragIntx(Widget):
    """Adds drag input for a set of int values up to 4. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the drag. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[int]): 
            **size (int): Number of components.
            **format (str): 
            **speed (float): 
            **min_value (int): Applies a limit only to draging entry only.
            **max_value (int): Applies a limit only to draging entry only.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_intx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[int] = (0, 0, 0, 0), 
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
            user_data=user_data,
            default_value=default_value,
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **default_value (Any): 
            **color (List[int]): 
            **thickness (float): 
            **show_label (bool): 
            **vertical (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drag_line

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        default_value: Any = 0.0, 
        color: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        show_label: bool = True, 
        vertical: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            user_data=user_data,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
            vertical=vertical,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.default_value = default_value
        self.color = color
        self.thickness = thickness
        self.show_label = show_label
        self.vertical = vertical


class Dummy(Widget):
    """Adds a spacer or 'dummy' object.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_dummy

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.user_data = user_data


class DynamicTexture(Widget):
    """Undocumented function
    Args:
            width (int): 
            height (int): 
            default_value (List[float]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_dynamic_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        default_value: list[float], 
        label: str = None, 
        user_data: Any = None, 
        parent: int = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.parent = parent


class FileExtension(Widget):
    """Creates a file extension filter option in the file dialog. Only works when the parent is a file dialog.
    Args:
            extension (str): Extension that will show as an when the parent is a file dialog.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **user_data (Any): User data for callbacks.
            **custom_text (str): Replaces the displayed text in the drop down for this extension.
            **color (List[float]): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_file_extension

    def __init__(
        self, 
        extension: str, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        parent: int = 0, 
        before: int = 0, 
        user_data: Any = None, 
        custom_text: str = '', 
        color: list[float] = (-255, 0, 0, 255), 
        **kwargs, 
    ):
        super().__init__(
            extension=extension,
            label=label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            user_data=user_data,
            custom_text=custom_text,
            color=color,
            **kwargs,
        )
        self.extension = extension
        self.label = label
        self.width = width
        self.height = height
        self.parent = parent
        self.before = before
        self.user_data = user_data
        self.custom_text = custom_text
        self.color = color


class Image(Widget):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) for texture coordinates will generally display the entire texture.
    Args:
            texture_id (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **tint_color (List[float]): Applies a color tint to the entire texture.
            **border_color (List[float]): Displays a border of the specified color around the texture.
            **uv_min (List[float]): Normalized texture coordinates min point.
            **uv_max (List[float]): Normalized texture coordinates max point.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_image

    def __init__(
        self, 
        texture_id: int, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        tint_color: list[float] = (255, 255, 255, 255), 
        border_color: list[float] = (0, 0, 0, 0), 
        uv_min: list[float] = (0.0, 0.0), 
        uv_max: list[float] = (1.0, 1.0), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
            label=label,
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
            user_data=user_data,
            tint_color=tint_color,
            border_color=border_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )
        self.texture_id = texture_id
        self.label = label
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
        self.user_data = user_data
        self.tint_color = tint_color
        self.border_color = border_color
        self.uv_min = uv_min
        self.uv_max = uv_max


class ImageButton(Widget):
    """Adds an button with a texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) texture coordinates will generally display the entire texture
    Args:
            texture_id (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **frame_padding (int): 
            **tint_color (List[float]): Applies a color tint to the entire texture.
            **background_color (List[float]): Displays a border of the specified color around the texture.
            **uv_min (List[float]): Normalized texture coordinates min point.
            **uv_max (List[float]): Normalized texture coordinates max point.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_image_button

    def __init__(
        self, 
        texture_id: int, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        frame_padding: int = -1, 
        tint_color: list[float] = (255, 255, 255, 255), 
        background_color: list[float] = (0, 0, 0, 0), 
        uv_min: list[float] = (0.0, 0.0), 
        uv_max: list[float] = (1.0, 1.0), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
            label=label,
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
            user_data=user_data,
            frame_padding=frame_padding,
            tint_color=tint_color,
            background_color=background_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )
        self.texture_id = texture_id
        self.label = label
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
        self.user_data = user_data
        self.frame_padding = frame_padding
        self.tint_color = tint_color
        self.background_color = background_color
        self.uv_min = uv_min
        self.uv_max = uv_max


class InputFloat(Widget):
    """Adds input for floats. Step buttons can be turned on or off.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (float): 
            **format (str): 
            **min_value (float): Value for lower limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            **max_value (float): Value for upper limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            **step (float): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
            **step_fast (float): After holding the step buttons for extended time the increments will switch to this value.
            **min_clamped (bool): Activates and deactivates min_value.
            **max_clamped (bool): Activates and deactivates max_value.
            **on_enter (bool): Only runs callback on enter key press.
            **readonly (bool): Activates a read only mode for the input.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_input_float

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: float = 0.0, 
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
            user_data=user_data,
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
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[float]): 
            **format (str): 
            **min_value (float): Value for lower limit of input for each cell. Use clamped to turn on.
            **max_value (float): Value for upper limit of input for each cell. Use clamped to turn on.
            **size (int): Number of components.
            **min_clamped (bool): Activates and deactivates min_value.
            **max_clamped (bool): Activates and deactivates max_value.
            **on_enter (bool): Only runs callback on enter key press.
            **readonly (bool): Activates a read only mode for the inputs.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_input_floatx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
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
            user_data=user_data,
            default_value=default_value,
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
        self.user_data = user_data
        self.default_value = default_value
        self.format = format
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputInt(Widget):
    """Adds input for an int. Step buttons can be turned on or off.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (int): 
            **min_value (int): Value for lower limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            **max_value (int): Value for upper limit of input. By default this limits the step buttons. Use clamped to limit manual input.
            **step (int): Increment to change value by when the step buttons are pressed. Setting this to a value of 0 or smaller will turn off step buttons.
            **step_fast (int): After holding the step buttons for extended time the increments will switch to this value.
            **min_clamped (bool): Activates and deactivates min_value.
            **max_clamped (bool): Activates and deactivates max_value.
            **on_enter (bool): Only runs callback on enter key press.
            **readonly (bool): Activates a read only mode for the input.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_input_int

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: int = 0, 
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
            user_data=user_data,
            default_value=default_value,
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[int]): 
            **min_value (int): Value for lower limit of input for each cell. Use clamped to turn on.
            **max_value (int): Value for upper limit of input for each cell. Use clamped to turn on.
            **size (int): Number of components.
            **min_clamped (bool): Activates and deactivates min_value.
            **max_clamped (bool): Activates and deactivates max_value.
            **on_enter (bool): Only runs callback on enter.
            **readonly (bool): Activates a read only mode for the inputs.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_input_intx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[int] = (0, 0, 0, 0), 
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
            user_data=user_data,
            default_value=default_value,
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
        self.user_data = user_data
        self.default_value = default_value
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (str): 
            **hint (str): Displayed only when value is empty string. Will reappear if input value is set to empty string. Will not show if default value is anything other than default empty string.
            **multiline (bool): Allows for multiline text input.
            **no_spaces (bool): Filter out spaces and tabs.
            **uppercase (bool): Automatically make all inputs uppercase.
            **tab_input (bool): Allows tabs to be input instead of changing widget focus.
            **decimal (bool): Only allow 0123456789.+-*/
            **hexadecimal (bool): Only allow 0123456789ABCDEFabcdef
            **readonly (bool): Activates read only mode.
            **password (bool): Password mode, display all characters as '*'.
            **scientific (bool): Only allow 0123456789.+-*/eE (Scientific notation input)
            **on_enter (bool): Only runs callback on enter key press.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_input_text

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: str = '', 
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
            user_data=user_data,
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
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
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
    """Adds a knob that rotates based of change in x mouse position.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (float): 
            **min_value (float): Applies lower limit to value.
            **max_value (float): Applies upper limit to value.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_knob_float

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: float = 0.0, 
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value


class Listbox(Widget):
    """Adds a listbox. If height is not large enought to show all items a scroll bar will appear.
    Args:
            *items (List[str]): A tuple of items to be shown in the listbox. Can consist of any combination of types.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (str): 
            **num_items (int): Expands the height of the listbox to show specified number of items.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_listbox

    def __init__(
        self, 
        items: list[str] = (), 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: str = '', 
        num_items: int = 3, 
        **kwargs, 
    ):
        super().__init__(
            items=items,
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            num_items=num_items,
            **kwargs,
        )
        self.items = items
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.num_items = num_items


class LoadingIndicator(Widget):
    """Adds a rotating anamated loding symbol.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **user_data (Any): User data for callbacks.
            **style (int): 0 is rotating dots style, 1 is rotating bar style.
            **circle_count (int): Number of dots show if dots or size of circle if circle.
            **speed (float): Speed the anamation will rotate.
            **radius (float): Radius size of the loading indicator.
            **thickness (float): Thickness of the circles or line.
            **color (List[int]): Color of the growing center circle.
            **secondary_color (List[int]): Background of the dots in dot mode.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_loading_indicator

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        user_data: Any = None, 
        style: int = 0, 
        circle_count: int = 8, 
        speed: float = 1.0, 
        radius: float = 3.0, 
        thickness: float = 1.0, 
        color: list[int] = (51, 51, 55, 255), 
        secondary_color: list[int] = (29, 151, 236, 103), 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            user_data=user_data,
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
        self.width = width
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.user_data = user_data
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
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (bool): 
            **shortcut (str): Displays text on the menu item. Typically used to show a shortcut key command.
            **check (bool): Displays a checkmark on the menu item when it is selected.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_menu_item

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: bool = False, 
        shortcut: str = '', 
        check: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            default_value=default_value,
            shortcut=shortcut,
            check=check,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.default_value = default_value
        self.shortcut = shortcut
        self.check = check


class ProgressBar(Widget):
    """Adds a progress bar.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **overlay (str): Overlayed text.
            **default_value (float): Normalized value to fill the bar from 0.0 to 1.0.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_progress_bar

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        overlay: str = '', 
        default_value: float = 0.0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            overlay=overlay,
            default_value=default_value,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.overlay = overlay
        self.default_value = default_value


class RadioButton(Widget):
    """Adds a set of radio buttons. If items keyword is empty, nothing will be shown.
    Args:
            *items (List[str]): A tuple of items to be shown as radio options. Can consist of any combination of types.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (str): 
            **horizontal (bool): Displays the radio options horizontally.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_radio_button

    def __init__(
        self, 
        items: list[str] = (), 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: str = '', 
        horizontal: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            items=items,
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            horizontal=horizontal,
            **kwargs,
        )
        self.items = items
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.horizontal = horizontal


class RawTexture(Widget):
    """Undocumented function
    Args:
            width (int): 
            height (int): 
            default_value (List[float]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **format (int): Data format.
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_raw_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        default_value: list[float], 
        label: str = None, 
        user_data: Any = None, 
        format: int = 0, 
        parent: int = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            format=format,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.format = format
        self.parent = parent


class SameLine(Widget):
    """Places a widget on the same line as the previous widget. Can also be used for horizontal spacing.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **xoffset (float): Offset from containing window.
            **spacing (float): Offset from previous widget.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_same_line

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        xoffset: float = 0.0, 
        spacing: float = -1.0, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            xoffset=xoffset,
            spacing=spacing,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.xoffset = xoffset
        self.spacing = spacing


class Selectable(Widget):
    """Adds a selectable.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (bool): 
            **span_columns (bool): Span the width of all columns if placed in a table.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_selectable

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: bool = False, 
        span_columns: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            span_columns=span_columns,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.span_columns = span_columns


class Separator(Widget):
    """Adds a horizontal line.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_separator

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.user_data = user_data


class SliderFloat(Widget):
    """Adds slider for a single float value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (float): 
            **vertical (bool): Sets orientation to vertical.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            **min_value (float): Applies a limit only to sliding entry only.
            **max_value (float): Applies a limit only to sliding entry only.
            **format (str): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_slider_float

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: float = 0.0, 
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
            user_data=user_data,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderFloatx(Widget):
    """Adds multi slider for up to 4 float values. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[float]): 
            **size (int): Number of components.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            **min_value (float): Applies a limit only to sliding entry only.
            **max_value (float): Applies a limit only to sliding entry only.
            **format (str): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_slider_floatx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
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
            user_data=user_data,
            default_value=default_value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderInt(Widget):
    """Adds slider for a single int value. Directly entry can be done with double click or CTRL+Click. Min and Max alone are a soft limit for the slider. Use clamped keyword to also apply limits to the direct entry modes.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (int): 
            **vertical (bool): Sets orientation to vertical.
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            **min_value (int): Applies a limit only to sliding entry only.
            **max_value (int): Applies a limit only to sliding entry only.
            **format (str): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_slider_int

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: int = 0, 
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
            user_data=user_data,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderIntx(Widget):
    """Adds multi slider for up to 4 int values. CTRL+Click to directly modify the value.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **enabled (bool): Turns off functionality of widget and applies the disabled theme.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (List[int]): 
            **size (int): number of components
            **no_input (bool): Disable direct entry methods or Enter key allowing to input text directly into the widget.
            **clamped (bool): Applies the min and max limits to direct entry methods also such as double click and CTRL+Click.
            **min_value (int): Applies a limit only to sliding entry only.
            **max_value (int): Applies a limit only to sliding entry only.
            **format (str): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_slider_intx

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        enabled: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: list[int] = (0, 0, 0, 0), 
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
            user_data=user_data,
            default_value=default_value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class Spacing(Widget):
    """Adds vertical spacing.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **user_data (Any): User data for callbacks.
            **count (int): Number of spacings to add the size is dependant on the curret style.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_spacing

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        user_data: Any = None, 
        count: int = 1, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            user_data=user_data,
            count=count,
            **kwargs,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.user_data = user_data
        self.count = count


class StaticTexture(Widget):
    """Undocumented function
    Args:
            width (int): 
            height (int): 
            default_value (List[float]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_static_texture

    def __init__(
        self, 
        width: int, 
        height: int, 
        default_value: list[float], 
        label: str = None, 
        user_data: Any = None, 
        parent: int = 12, 
        **kwargs, 
    ):
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.parent = parent


class TabButton(Widget):
    """Adds a tab button to a tab bar.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **no_reorder (bool): Disable reordering this tab or having another tab cross over this tab.
            **leading (bool): Enforce the tab position to the left of the tab bar (after the tab list popup button).
            **trailing (bool): Enforce the tab position to the right of the tab bar (before the scrolling buttons).
            **no_tooltip (bool): Disable tooltip for the given tab.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_tab_button

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        no_reorder: bool = False, 
        leading: bool = False, 
        trailing: bool = False, 
        no_tooltip: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            no_reorder=no_reorder,
            leading=leading,
            trailing=trailing,
            no_tooltip=no_tooltip,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip


class TableColumn(Widget):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **init_width_or_weight (float): 
            **default_hide (bool): Default as a hidden/disabled column.
            **default_sort (bool): Default as a sorting column.
            **width_stretch (bool): Column will stretch. Preferable with horizontal scrolling disabled (default if table sizing policy is _SizingStretchSame or _SizingStretchProp).
            **width_fixed (bool): Column will not stretch. Preferable with horizontal scrolling enabled (default if table sizing policy is _SizingFixedFit and table is resizable).
            **no_resize (bool): Disable manual resizing.
            **no_reorder (bool): Disable manual reordering this column, this will also prevent other columns from crossing over this column.
            **no_hide (bool): Disable ability to hide/disable this column.
            **no_clip (bool): Disable clipping for this column (all NoClip columns will render in a same draw command).
            **no_sort (bool): Disable ability to sort on this field (even if ImGuiTableFlags_Sortable is set on the table).
            **no_sort_ascending (bool): Disable ability to sort in the ascending direction.
            **no_sort_descending (bool): Disable ability to sort in the descending direction.
            **no_header_width (bool): Disable header text width contribution to automatic column width.
            **prefer_sort_ascending (bool): Make the initial sort direction Ascending when first sorting on this column (default).
            **prefer_sort_descending (bool): Make the initial sort direction Descending when first sorting on this column.
            **indent_enable (bool): Use current Indent value when entering cell (default for column 0).
            **indent_disable (bool): Ignore current Indent value when entering cell (default for columns > 0). Indentation changes _within_ the cell will still be honored.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_table_column

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        init_width_or_weight: float = 0.0, 
        default_hide: bool = False, 
        default_sort: bool = False, 
        width_stretch: bool = False, 
        width_fixed: bool = False, 
        no_resize: bool = False, 
        no_reorder: bool = False, 
        no_hide: bool = False, 
        no_clip: bool = False, 
        no_sort: bool = False, 
        no_sort_ascending: bool = False, 
        no_sort_descending: bool = False, 
        no_header_width: bool = False, 
        prefer_sort_ascending: bool = True, 
        prefer_sort_descending: bool = False, 
        indent_enable: bool = False, 
        indent_disable: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            init_width_or_weight=init_width_or_weight,
            default_hide=default_hide,
            default_sort=default_sort,
            width_stretch=width_stretch,
            width_fixed=width_fixed,
            no_resize=no_resize,
            no_reorder=no_reorder,
            no_hide=no_hide,
            no_clip=no_clip,
            no_sort=no_sort,
            no_sort_ascending=no_sort_ascending,
            no_sort_descending=no_sort_descending,
            no_header_width=no_header_width,
            prefer_sort_ascending=prefer_sort_ascending,
            prefer_sort_descending=prefer_sort_descending,
            indent_enable=indent_enable,
            indent_disable=indent_disable,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.init_width_or_weight = init_width_or_weight
        self.default_hide = default_hide
        self.default_sort = default_sort
        self.width_stretch = width_stretch
        self.width_fixed = width_fixed
        self.no_resize = no_resize
        self.no_reorder = no_reorder
        self.no_hide = no_hide
        self.no_clip = no_clip
        self.no_sort = no_sort
        self.no_sort_ascending = no_sort_ascending
        self.no_sort_descending = no_sort_descending
        self.no_header_width = no_header_width
        self.prefer_sort_ascending = prefer_sort_ascending
        self.prefer_sort_descending = prefer_sort_descending
        self.indent_enable = indent_enable
        self.indent_disable = indent_disable


class TableNextColumn(Widget):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_table_next_column

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data


class Text(Widget):
    """Adds text. Text can have an optional label that will display to the right of the text.
    Args:
            *default_value (str): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **source (int): Overrides 'id' as value storage key.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **wrap (int): Number of pixels until wrapping starts.
            **bullet (bool): Makes the text bulleted.
            **color (List[float]): Color of the text (rgba).
            **show_label (bool): Displays the label.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_text

    def __init__(
        self, 
        default_value: str = '', 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        source: int = 0, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        wrap: int = -1, 
        bullet: bool = False, 
        color: list[float] = (-1, -1, -1, -1), 
        show_label: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            default_value=default_value,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            wrap=wrap,
            bullet=bullet,
            color=color,
            show_label=show_label,
            **kwargs,
        )
        self.default_value = default_value
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data
        self.wrap = wrap
        self.bullet = bullet
        self.color = color
        self.show_label = show_label


class TimePicker(Widget):
    """Adds a time picker.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **indent (int): Offsets the widget to the right the specified number multiplied by the indent style.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
            **default_value (dict): 
            **hour24 (bool): Show 24 hour clock instead of 12 hour.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_time_picker

    def __init__(
        self, 
        label: str = None, 
        indent: int = -1, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        default_value: dict = {'hour': 14, 'min': 32, 'sec': 23}, 
        hour24: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
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
            user_data=user_data,
            default_value=default_value,
            hour24=hour24,
            **kwargs,
        )
        self.label = label
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
        self.user_data = user_data
        self.default_value = default_value
        self.hour24 = hour24
