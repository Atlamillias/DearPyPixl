import functools
from typing import Any, Callable, Union
from dearpypixl.constants import Key, Mouse
from dearpypixl.components.item import Item
from dearpypixl.components.primitives import AbstractBoundItem, RegistryItem
from dearpypixl.components.handlers import *
from dearpygui import dearpygui


__all__ = [
    "Events",
]


def _manage_handler(handler: Item):
    def wrapped_method(_method):
        @functools.wraps(_method)
        def register_callback(self, callback: Callable = None, *args, **kwargs):
            @functools.wraps(callback)
            def set_handler(callback):
                handler(label=callback.__name__,  # lambdas have `<lambda>`
                        callback=callback, parent=int(self), *args, **kwargs)
                return callback

            if not callback:
                return set_handler
            return set_handler(callback)

        return register_callback

    return wrapped_method


class AppEvents(RegistryItem):
    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        show: bool = True,
        **kwargs,
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
        self.show = show

    ################################
    ######## Callback Deco. ########
    ################################
    @_manage_handler(KeyDownHandler)
    def while_key_down(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyPressHandler)
    def on_key_press(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyReleaseHandler)
    def on_key_up(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDownHandler)
    def on_mouse_button_down(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseClickHandler)
    def on_mouse_button_click(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDoubleClickHandler)
    def on_mouse_button_double_click(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseReleaseHandler)
    def on_mouse_button_up(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseMoveHandler)
    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseWheelHandler)
    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDragHandler)
    def on_mouse_drag(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, threshold: float = 10.0, user_data: Any = None, **kwargs):
        ...

    ################################
    ####### Private/Internal #######
    ################################
    _command = dearpygui.add_handler_registry




class Events(AbstractBoundItem, RegistryItem):
    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        show: bool = True,
        **kwargs,
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
        self._target_uuids: set[int] = set()

        self.show = show

    def bind(self, *item: Item):
        self_uuid = self._tag
        self_target_uuids = self._target_uuids
        for i in item:
            dearpygui.bind_item_handler_registry(i._tag, self_uuid)
            self_target_uuids.add(i._tag)

    def unbind(self, *item: Item):
        self_target_uuids = self._target_uuids
        for i in item:
            if i._tag not in self_target_uuids:
                raise ValueError(f"Cannot unbind {item.__qualname__!r} as it is not bound to this item.")
            dearpygui.bind_item_handler_registry(i._tag, 0)

    ################################
    ######## Callback Deco. ########
    ################################
    @_manage_handler(ItemActiveHandler)
    def while_active(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemActivatedHandler)
    def on_activation(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemDeactivatedHandler)
    def on_deactivation(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemDeactivatedAfterEditHandler)
    def on_deactivation_after_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemClickedHandler)
    def on_click(self, callback: Callable = None, *, user_data: Any = None, button=-1, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemEditedHandler)
    def on_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemFocusHandler)
    def on_focus(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemHoverHandler)
    def on_hover(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemResizeHandler)
    def on_resize(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemToggledOpenHandler)
    def on_toggle_open(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ItemVisibleHandler)
    def on_visible(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    ################################
    ####### Private/Internal #######
    ################################
    _command = dearpygui.add_item_handler_registry






