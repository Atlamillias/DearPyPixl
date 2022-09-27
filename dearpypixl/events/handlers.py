import functools
from typing import Callable, Any
from dearpygui import dearpygui
from dearpygui._dearpygui import configure_item
from dearpypixl._internal.item import (
    Item,
    ItemData,
)
from dearpypixl._internal.members import (
    get_item_config,
    set_item_callback
)
from dearpypixl._internal.utilities import (
    get_positional_args_count,
    prep_callback,
)
from dearpypixl._internal import registry


__all__ = [
    "HandlerItem",
    "ItemHandlerItem",
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
    __slots__ = ()
    __dearpypixl__ = ItemData(
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_children=(),
        internal_only=True,
    )

    callback = __dearpypixl__.set_configuration("get_item_config", "set_item_callback")

    def __init__(self, callback: Callable | None, **kwargs):
        super().__init__(callback=callback, **kwargs)


class ItemHandlerItem(HandlerItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(internal_only=True)

    def __init__(self, callback: Callable | None = None, **kwargs):
        # Item handler callbacks require a bit more formatting than usual,
        # so it is set through the descriptor and not formated through the
        # base constructor.
        super().__init__(callback=None, **kwargs)
        self.callback = callback

    @property
    @__dearpypixl__.as_configuration
    def callback(self) -> Callable | None:
        return get_item_config(self, "callback")
    @callback.setter
    def callback(self, _callback: Callable | None) -> None:
        @functools.wraps(_callback)
        def _fmt_app_data(sender=None, app_data: tuple[int, int] = None, user_data=None, **kwargs):
            app_data = app_data[0], registry.get_item(app_data[1])
            _callback(sender, app_data, user_data, **kwargs)

        _callback = prep_callback(self, _callback)
        # Item handlers pass the "target" item as the second argument of
        # app_data -- pass the reference instead.
        if _callback and get_positional_args_count(_callback) >= 2:
            callback_obj = _fmt_app_data
        else:
            callback_obj = _callback
        configure_item(self.tag, callback=callback_obj)


#####################################################################################
############################### Global Event Handlers ###############################
#####################################################################################
class KeyDownHandler(HandlerItem):
    """Adds a key down handler.

        Args:
            * key (int, optional): Submits callback for all keys
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvKeyDownHandler, "mvKeyDownHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_key_down_handler,
    )

    key : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvKeyPressHandler, "mvKeyPressHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_key_press_handler,
    )

    key : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvKeyReleaseHandler, "mvKeyReleaseHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_key_release_handler,
    )

    key : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseMoveHandler, "MouseMoveHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_move_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseWheelHandler, "mvMouseWheelHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_wheel_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseClickHandler, "mvMouseClickHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_click_handler,
    )

    button: int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseDoubleClickHandler, "mvMouseDoubleClickHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_double_click_handler,
    )

    button: int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseDownHandler, "mvMouseDownHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_down_handler,
    )

    button: int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseReleaseHandler, "mvMouseReleaseHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_release_handler,
    )

    button: int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvMouseDragHandler, "mvMouseDragHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvHandlerRegistry),
        command=dearpygui.add_mouse_drag_handler,
    )

    button   : int   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    threshold: float = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show     : bool  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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
class HoverHandler(ItemHandlerItem):
    """Adds a hover handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvHoverHandler, "mvHoverHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_hover_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ResizeHandler(ItemHandlerItem):
    """Adds a resize handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvResizeHandler, "mvResizeHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_resize_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class FocusHandler(ItemHandlerItem):
    """Adds a focus handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFocusHandler, "mvFocusHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_focus_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ActiveHandler(ItemHandlerItem):
    """Adds a active handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvActiveHandler, "mvActiveHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_active_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class VisibleHandler(ItemHandlerItem):
    """Adds a visible handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvVisibleHandler, "mvVisibleHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_visible_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ActivatedHandler(ItemHandlerItem):
    """Adds a activated handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvActivatedHandler, "mvActivatedHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_activated_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class DeactivatedHandler(ItemHandlerItem):
    """Adds a deactivated handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDeactivatedHandler, "mvDeactivatedHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_deactivated_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class EditedHandler(ItemHandlerItem):
    """Adds an edited handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvEditedHandler, "mvEditedHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_edited_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class DeactivatedAfterEditHandler(ItemHandlerItem):
    """Adds a deactivated after edit handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDeactivatedAfterEditHandler, "mvDeactivatedAfterEditHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_deactivated_after_edit_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ToggledOpenHandler(ItemHandlerItem):
    """Adds a togged open handler.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvToggledOpenHandler, "mvToggledOpenHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_toggled_open_handler,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class ClickedHandler(ItemHandlerItem):
    """Adds a clicked handler.

        Args:
            * button (int, optional): Submits callback for all mouse buttons
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvClickedHandler, "mvClickedHandler"),
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvItemHandlerRegistry),
        command=dearpygui.add_item_clicked_handler,
    )

    button: int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Item | int      = 0   ,
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
