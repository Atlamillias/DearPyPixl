from typing import Callable, Any

from . import dpg
from ._widget import Widget


##################################################
## Note: this file was automatically generated. ##
##################################################


class Slider(Widget):
    _command: Callable = dpg.add_3d_slider

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
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        max_x: float = 100.0,
        max_y: float = 100.0,
        max_z: float = 100.0,
        min_x: float = 0.0,
        min_y: float = 0.0,
        min_z: float = 0.0,
        scale: float = 1.0,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_button

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_char_remap

    def __init__(
        self,
        source: int,
        target: int,
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        source=source,
        target=target,
        label=label,
        parent=parent,
        user_data=user_data,
        **kwargs
        )
        self.source = source
        self.target = target
        self.label = label
        self.parent = parent
        self.user_data = user_data


class Checkbox(Widget):
    _command: Callable = dpg.add_checkbox

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_color_button

    def __init__(
        self,
        default_value: list[int] = [0, 0, 0, 255],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_color_edit

    def __init__(
        self,
        default_value: list[int] = [0, 0, 0, 255],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_color_picker

    def __init__(
        self,
        default_value: list[int] = [0, 0, 0, 255],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_colormap_scale

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_combo

    def __init__(
        self,
        items: list[str] = [],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_date_picker

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_drag_float

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_drag_floatx

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
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        size: int = 4,
        format: str = '%0.3f',
        speed: float = 1.0,
        min_value: float = 0.0,
        max_value: float = 100.0,
        no_input: bool = False,
        clamped: bool = False,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_drag_int

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_drag_intx

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
        default_value: list[int] = [0, 0, 0, 0],
        size: int = 4,
        format: str = '%d',
        speed: float = 1.0,
        min_value: int = 0,
        max_value: int = 100,
        no_input: bool = False,
        clamped: bool = False,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_drag_line

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
        color: list[int] = [0, 0, 0, -255],
        thickness: float = 1.0,
        show_label: bool = True,
        vertical: bool = True,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_dummy

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_dynamic_texture

    def __init__(
        self,
        width: int,
        height: int,
        default_value: list[float],
        label: str = None,
        user_data: Any = None,
        parent: int = 12,
        **kwargs
    ):
        super().__init__(
        width=width,
        height=height,
        default_value=default_value,
        label=label,
        user_data=user_data,
        parent=parent,
        **kwargs
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.parent = parent


class FileExtension(Widget):
    _command: Callable = dpg.add_file_extension

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
        color: list[float] = [-255, 0, 0, 255],
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_image

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
        tint_color: list[float] = [255, 255, 255, 255],
        border_color: list[float] = [0, 0, 0, 0],
        uv_min: list[float] = [0.0, 0.0],
        uv_max: list[float] = [1.0, 1.0],
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_image_button

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
        tint_color: list[float] = [255, 255, 255, 255],
        background_color: list[float] = [0, 0, 0, 0],
        uv_min: list[float] = [0.0, 0.0],
        uv_max: list[float] = [1.0, 1.0],
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_input_float

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_input_floatx

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
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        format: str = '%.3f',
        min_value: float = 0.0,
        max_value: float = 100.0,
        size: int = 4,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_input_int

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_input_intx

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
        default_value: list[int] = [0, 0, 0, 0],
        min_value: int = 0,
        max_value: int = 100,
        size: int = 4,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_input_text

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_knob_float

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_listbox

    def __init__(
        self,
        items: list[str] = [],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_loading_indicator

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
        color: list[int] = [51, 51, 55, 255],
        secondary_color: list[int] = [29, 151, 236, 103],
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_menu_item

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_progress_bar

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_radio_button

    def __init__(
        self,
        items: list[str] = [],
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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_raw_texture

    def __init__(
        self,
        width: int,
        height: int,
        default_value: list[float],
        label: str = None,
        user_data: Any = None,
        format: int = 0,
        parent: int = 12,
        **kwargs
    ):
        super().__init__(
        width=width,
        height=height,
        default_value=default_value,
        label=label,
        user_data=user_data,
        format=format,
        parent=parent,
        **kwargs
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.format = format
        self.parent = parent


class SameLine(Widget):
    _command: Callable = dpg.add_same_line

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        user_data: Any = None,
        xoffset: float = 0.0,
        spacing: float = -1.0,
        **kwargs
    ):
        super().__init__(
        label=label,
        parent=parent,
        before=before,
        show=show,
        user_data=user_data,
        xoffset=xoffset,
        spacing=spacing,
        **kwargs
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.xoffset = xoffset
        self.spacing = spacing


class Selectable(Widget):
    _command: Callable = dpg.add_selectable

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_separator

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        pos: list[int] = [],
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        label=label,
        indent=indent,
        parent=parent,
        before=before,
        show=show,
        pos=pos,
        user_data=user_data,
        **kwargs
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.user_data = user_data


class SliderFloat(Widget):
    _command: Callable = dpg.add_slider_float

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_slider_floatx

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
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        size: int = 4,
        no_input: bool = False,
        clamped: bool = False,
        min_value: float = 0.0,
        max_value: float = 100.0,
        format: str = '%.3f',
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_slider_int

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_slider_intx

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
        default_value: list[int] = [0, 0, 0, 0],
        size: int = 4,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%d',
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_spacing

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_static_texture

    def __init__(
        self,
        width: int,
        height: int,
        default_value: list[float],
        label: str = None,
        user_data: Any = None,
        parent: int = 12,
        **kwargs
    ):
        super().__init__(
        width=width,
        height=height,
        default_value=default_value,
        label=label,
        user_data=user_data,
        parent=parent,
        **kwargs
        )
        self.width = width
        self.height = height
        self.default_value = default_value
        self.label = label
        self.user_data = user_data
        self.parent = parent


class TabButton(Widget):
    _command: Callable = dpg.add_tab_button

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_table_column

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
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_table_next_column

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        label=label,
        parent=parent,
        before=before,
        show=show,
        user_data=user_data,
        **kwargs
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data


class Text(Widget):
    _command: Callable = dpg.add_text

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
        color: list[float] = [-1, -1, -1, -1],
        show_label: bool = False,
        **kwargs
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
        **kwargs
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
    _command: Callable = dpg.add_time_picker

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
        **kwargs
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
        **kwargs
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
