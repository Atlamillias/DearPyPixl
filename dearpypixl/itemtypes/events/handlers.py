from abc import ABC, abstractmethod
from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes.item import (
    Item,
    ItemProperty,
    ItemIdType,
    get_item_config,
    set_item_callback,
    CONFIG,
)


__all__ = [
    "HandlerItem",
    # Global Event Handlers
    "KeyDownHandler",
    "KeyPressHandler",
    "KeyReleaseHandler",
    "MouseMoveHandler",
    "MouseWheelHandler",
    "MouseClickHandler",
    "MouseDoubleClickHandler",
    "MouseDownHandler",
    "MouseReleaseHandler",
    "MouseDragHandler",
    # Item Event Handlers
    "HoverHandler",
    "ResizeHandler",
    "FocusHandler",
    "ActiveHandler",
    "VisibleHandler",
    "ActivatedHandler",
    "DeactivatedHandler",
    "EditedHandler",
    "DeactivatedAfterEditHandler",
    "ToggledOpenHandler",
    "ClickedHandler",
]




class HandlerItem(Item):
    """Base class for handler items.
    """
    @abstractmethod
    def __itemtype_id__()  -> ItemIdType: ...
    @abstractmethod
    def __able_parents__() -> tuple     : ...
    @abstractmethod
    def __command__()      -> Callable  : ...

    __is_container__ : bool  = False
    __is_root_item__ : bool  = False
    __is_value_able__: bool  = False
    __able_children__: tuple = ()

    def __init__(self, callback: Callable | None, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback

    @property
    @ItemProperty.register(category=CONFIG)
    def callback(self) -> Callable | None:
        return get_item_config(self, "callback")
    @callback.setter
    def callback(self, _callback: Callable | None) -> None:
        set_item_callback(self, "callback", _callback)



#####################################################################################
############################### Global Event Handlers ###############################
#####################################################################################
class KeyDownHandler(HandlerItem):
    """Adds a key down handler.

        Args:
            * key (int, optional): Submits callback for all keys
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    key : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvKeyDownHandler, "mvKeyDownHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_key_down_handler

    def __init__(
        self,
        key               : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class KeyPressHandler(HandlerItem):
    """Adds a key press handler.

        Args:
            * key (int, optional): Submits callback for all keys
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    key : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvKeyPressHandler, "mvKeyPressHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_key_press_handler

    def __init__(
        self,
        key               : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class KeyReleaseHandler(HandlerItem):
    """Adds a key release handler.

        Args:
            * key (int, optional): Submits callback for all keys
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    key : int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvKeyReleaseHandler, "mvKeyReleaseHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_key_release_handler

    def __init__(
        self,
        key               : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class MouseMoveHandler(HandlerItem):
    """Adds a mouse move handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseMoveHandler, "MouseMoveHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_move_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseWheelHandler(HandlerItem):
    """Adds a mouse wheel handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseWheelHandler, "mvMouseWheelHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_wheel_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseClickHandler(HandlerItem):
    """Adds a mouse click handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    button: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show  : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseClickHandler, "mvMouseClickHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_click_handler

    def __init__(
        self,
        button            : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class MouseDoubleClickHandler(HandlerItem):
    """Adds a mouse double click handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    button: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show  : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseDoubleClickHandler, "mvMouseDoubleClickHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_double_click_handler

    def __init__(
        self,
        button            : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class MouseDownHandler(HandlerItem):
    """Adds a mouse down handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    button: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show  : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseDownHandler, "mvMouseDownHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_down_handler

    def __init__(
        self,
        button            : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class MouseReleaseHandler(HandlerItem):
    """Adds a mouse release handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    button: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show  : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseReleaseHandler, "mvMouseReleaseHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_release_handler

    def __init__(
        self,
        button            : int       = -1  ,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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


class MouseDragHandler(HandlerItem):
    """Adds a mouse drag handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * threshold (float, optional): The threshold the mouse must be dragged before the callback is ran
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    button   : int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    threshold: float = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show     : bool  = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvMouseDragHandler, "mvMouseDragHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvHandlerRegistry)
    __command__     : Callable   = dearpygui.add_mouse_drag_handler

    def __init__(
        self,
        button            : int       = -1  ,
        threshold         : float     = 10.0,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        callback          : Callable  = None,
        show              : bool      = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
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




#####################################################################################
############################### Item Event Handlers #################################
#####################################################################################
class HoverHandler(HandlerItem):
    """Adds a hover handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvHoverHandler, "mvHoverHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_hover_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ResizeHandler(HandlerItem):
    """Adds a resize handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvResizeHandler, "mvResizeHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_resize_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class FocusHandler(HandlerItem):
    """Adds a focus handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvFocusHandler, "mvFocusHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_focus_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActiveHandler(HandlerItem):
    """Adds a active handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvActiveHandler, "mvActiveHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_active_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class VisibleHandler(HandlerItem):
    """Adds a visible handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvVisibleHandler, "mvVisibleHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_visible_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActivatedHandler(HandlerItem):
    """Adds a activated handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvActivatedHandler, "mvActivatedHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_activated_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedHandler(HandlerItem):
    """Adds a deactivated handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvDeactivatedHandler, "mvDeactivatedHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_deactivated_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class EditedHandler(HandlerItem):
    """Adds an edited handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvEditedHandler, "mvEditedHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_edited_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedAfterEditHandler(HandlerItem):
    """Adds a deactivated after edit handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvDeactivatedAfterEditHandler, "mvDeactivatedAfterEditHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_deactivated_after_edit_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ToggledOpenHandler(HandlerItem):
    """Adds a togged open handler.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvToggledOpenHandler, "mvToggledOpenHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_toggled_open_handler

    def __init__(
        self,
        label             : str       = None,
        user_data         : Any       = None,
        use_internal_label: bool      = True,
        parent            : int | str = 0   ,
        callback          : Callable  = None,
        show              : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ClickedHandler(HandlerItem):
    """Adds a clicked handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
    """
    button: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show  : bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__ : ItemIdType = ItemIdType(dearpygui.mvClickedHandler, "mvClickedHandler")
    __able_parents__: tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvItemHandlerRegistry)
    __command__     : Callable   = dearpygui.add_item_clicked_handler

    def __init__(
        self,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str       = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs
    ) -> None:
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
