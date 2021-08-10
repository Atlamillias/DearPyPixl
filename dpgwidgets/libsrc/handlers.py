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
    """Adds a handler which runs a given callback when the specified item is activated.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_activated_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class ActiveHandler(Item):
    """Adds a handler which runs a given callback when the specified item is active.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_active_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class ClickedHandler(Item):
    """Adds a handler which runs a given callback when the specified item is clicked.
    Args:
            parent (int): 
            *button (int): Submits callback for all mouse buttons
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_clicked_handler

    def __init__(
        self, 
        parent: int, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class DeactivatedAfterEditHandler(Item):
    """Adds a handler which runs a given callback when the specified item is deactivated after edit.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_deactivated_after_edit_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class DeactivatedHandler(Item):
    """Adds a handler which runs a given callback when the specified item is deactivated.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_deactivated_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class EditedHandler(Item):
    """Adds a handler which runs a given callback when the specified item is edited.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_edited_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class FocusHandler(Item):
    """Adds a handler which runs a given callback when the specified item is focused.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_focus_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class HoverHandler(Item):
    """Adds a handler which runs a given callback when the specified item is hovered.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_hover_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class KeyDownHandler(Item):
    """Adds a handler which runs a given callback when the specified key is down. Parent must be a handler registry.
    Args:
            *key (int): Submits callback for all keys
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_key_down_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class KeyPressHandler(Item):
    """Adds a handler which runs a given callback when the specified key is pressed. Parent must be a handler registry.
    Args:
            *key (int): Submits callback for all keys
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_key_press_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class KeyReleaseHandler(Item):
    """Adds a handler which runs a given callback when the specified key is released. Parent must be a handler registry.
    Args:
            *key (int): Submits callback for all keys
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_key_release_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseClickHandler(Item):
    """Adds a handler which runs a given callback when the specified mouse button is clicked. Parent must be a handler registry.
    Args:
            *button (int): Submits callback for all mouse buttons
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseDoubleClickHandler(Item):
    """Adds a handler which runs a given callback when the specified mouse button is double clicked. Parent must be a handler registry.
    Args:
            *button (int): Submits callback for all mouse buttons
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_double_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseDownHandler(Item):
    """Adds a handler which runs a given callback when the specified mouse button is down. Parent must be a handler registry.
    Args:
            *button (int): Submits callback for all mouse buttons
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_down_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseDragHandler(Item):
    """Adds a handler which runs a given callback when the specified mouse button is clicked and dragged a set threshold. Parent must be a handler registry.
    Args:
            *button (int): Submits callback for all mouse buttons
            *threshold (float): The threshold the mouse must be dragged before the callback is ran
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_drag_handler

    def __init__(
        self, 
        button: int = -1, 
        threshold: float = 10.0, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
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
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.threshold = threshold
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseMoveHandler(Item):
    """Adds a handler which runs a given callback when the mouse is moved. Parent must be a handler registry.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_move_handler

    def __init__(
        self, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseReleaseHandler(Item):
    """Adds a handler which runs a given callback when the specified mouse button is released. Parent must be a handler registry.
    Args:
            *button (int): Submits callback for all mouse buttons
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_release_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class MouseWheelHandler(Item):
    """Adds a handler which runs a given callback when the vertical mouse wheel is scrolled. Parent must be a handler registry.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_mouse_wheel_handler

    def __init__(
        self, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: int = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class ResizeHandler(Item):
    """Adds a handler which runs a given callback when the specified item is resized.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_resize_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class ToggledOpenHandler(Item):
    """Adds a handler which runs a given callback when the specified item is toggled open.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_toggled_open_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label


class VisibleHandler(Item):
    """Adds a handler which runs a given callback when the specified item is visible.
    Args:
            parent (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **callback (Callable): Registers a callback.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_visible_handler

    def __init__(
        self, 
        parent: int, 
        label: str = None, 
        callback: Callable = None, 
        show: bool = True, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            parent=parent,
            label=label,
            callback=callback,
            show=show,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )
        self.parent = parent
        self.label = label
        self.callback = callback
        self.show = show
        self.user_data = user_data
        self.use_internal_label = use_internal_label
