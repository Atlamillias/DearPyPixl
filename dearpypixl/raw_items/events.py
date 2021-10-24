from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from dearpypixl.item import Item

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "ItemActivatedHandler",
    "ItemActiveHandler",
    "ItemClickedHandler",
    "ItemDeactivatedAfterEditHandler",
    "ItemDeactivatedHandler",
    "ItemEditedHandler",
    "ItemFocusHandler",
    "ItemHoverHandler",
    "ItemResizeHandler",
    "ItemToggledOpenHandler",
    "ItemVisibleHandler",
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
]


class ItemActivatedHandler(Item):
    """Adds a activated handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_activated_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemActiveHandler(Item):
    """Adds a active handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_active_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemClickedHandler(Item):
    """Adds a clicked handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_clicked_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemDeactivatedAfterEditHandler(Item):
    """Adds a deactivated after edit handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_deactivated_after_edit_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemDeactivatedHandler(Item):
    """Adds a deactivated handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_deactivated_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemEditedHandler(Item):
    """Adds an edited handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_edited_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemFocusHandler(Item):
    """Adds a focus handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_focus_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemHoverHandler(Item):
    """Adds a hover handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_hover_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemResizeHandler(Item):
    """Adds a resize handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_resize_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemToggledOpenHandler(Item):
    """Adds a togged open handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_toggled_open_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class ItemVisibleHandler(Item):
    """Adds a visible handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_item_visible_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class KeyDownHandler(Item):
    """Adds a key down handler.
    
    Args:
            key (int, optional): Submits callback for all keys
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_key_down_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class KeyPressHandler(Item):
    """Adds a key press handler.
    
    Args:
            key (int, optional): Submits callback for all keys
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_key_press_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class KeyReleaseHandler(Item):
    """Adds a key release handler.
    
    Args:
            key (int, optional): Submits callback for all keys
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_key_release_handler

    def __init__(
        self, 
        key: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.key = key
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseClickHandler(Item):
    """Adds a mouse click handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseDoubleClickHandler(Item):
    """Adds a mouse double click handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_double_click_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseDownHandler(Item):
    """Adds a mouse down handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_down_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseDragHandler(Item):
    """Adds a mouse drag handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            threshold (float, optional): The threshold the mouse must be dragged before the callback is ran
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_drag_handler

    def __init__(
        self, 
        button: int = -1, 
        threshold: float = 10.0, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            threshold=threshold,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.threshold = threshold
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseMoveHandler(Item):
    """Adds a mouse move handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_move_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseReleaseHandler(Item):
    """Adds a mouse release handler.
    
    Args:
            button (int, optional): Submits callback for all mouse buttons
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_release_handler

    def __init__(
        self, 
        button: int = -1, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.button = button
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show


class MouseWheelHandler(Item):
    """Adds a mouse wheel handler.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_mouse_wheel_handler

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        callback: Callable = None, 
        show: bool = True, 
        parent: Union[int, str] = 11, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.callback = callback
        self.show = show
