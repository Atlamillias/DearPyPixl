from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.item import Item, ContextSupport

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "ActivatedHandler",
    "ActiveHandler",
    "ClickedHandler",
    "DeactivatedAfterEditHandler",
    "DeactivatedHandler",
    "EditedHandler",
    "FocusHandler",
    "HoverHandler",
    "KeyDownHandler",
    "KeyPressHandler",
    "KeyReleaseHandler",
    "MouseClickHandler",
    "MouseDoubleClickHandler",
    "MouseDownHandler",
    "MouseDragHandler",
    "MouseMoveHandler",
    "MouseReleaseHandler",
    "MouseWheelHandler",
    "ResizeHandler",
    "ToggledOpenHandler",
    "VisibleHandler",
]


class ActivatedHandler(Item):
    _command = dearpygui.dearpygui.add_activated_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class ActiveHandler(Item):
    _command = dearpygui.dearpygui.add_active_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class ClickedHandler(Item):
    _command = dearpygui.dearpygui.add_clicked_handler

    def __init__(
        self, 
        parent: int, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class DeactivatedAfterEditHandler(Item):
    _command = dearpygui.dearpygui.add_deactivated_after_edit_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class DeactivatedHandler(Item):
    _command = dearpygui.dearpygui.add_deactivated_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class EditedHandler(Item):
    _command = dearpygui.dearpygui.add_edited_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class FocusHandler(Item):
    _command = dearpygui.dearpygui.add_focus_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class HoverHandler(Item):
    _command = dearpygui.dearpygui.add_hover_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class KeyDownHandler(Item):
    _command = dearpygui.dearpygui.add_key_down_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class KeyPressHandler(Item):
    _command = dearpygui.dearpygui.add_key_press_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class KeyReleaseHandler(Item):
    _command = dearpygui.dearpygui.add_key_release_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseClickHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseDoubleClickHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_double_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseDownHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_down_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseDragHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_drag_handler

    def __init__(
        self, 
        button: int = -1, 
        threshold: float = 10.0, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            threshold=threshold,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.threshold = threshold
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseMoveHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_move_handler

    def __init__(
        self, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseReleaseHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_release_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class MouseWheelHandler(Item):
    _command = dearpygui.dearpygui.add_mouse_wheel_handler

    def __init__(
        self, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.parent = parent


class ResizeHandler(Item):
    _command = dearpygui.dearpygui.add_resize_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class ToggledOpenHandler(Item):
    _command = dearpygui.dearpygui.add_toggled_open_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data


class VisibleHandler(Item):
    _command = dearpygui.dearpygui.add_visible_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
