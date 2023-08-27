import functools
from dearpygui import dearpygui
from ._dearpypixl import api
from. _dearpypixl.common import (
    Item,
    Any,
    Callable,
    TypeVar,
    ParamSpec,
)
from ._dearpypixl.callback import *
from . import items


_T = TypeVar("_T")
_P = ParamSpec("_P")






# handler signatures -- protocols are just more work here

def _handler(self, callback: ItemCallback | None = None, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...

def _mouse_handler(self, callback: ItemCallback | None = None, *, button: int = -1, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...

def _key_hander(self, callback: ItemCallback | None = None, *, key: int = -1, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...


def handler_hook(handler_fn: Any, protocol: Callable[_P, _T] = _handler) -> Callable[[Callable], Callable[_P, _T]]:
    def wrap_method(mthd: Any) -> Callable[_P, _T]:
        @functools.wraps(mthd)
        def mthd_add_handler(self: items.mvHandlerRegistry | items.mvItemHandlerRegistry, callback = None, *args, parent: Item = 0, **kwargs):
            def add_handler(callback):
                handler_fn(callback=callback, parent=parent or self, **kwargs)
                return callback

            if callback is None:
                return add_handler
            return add_handler(callback)

        return mthd_add_handler  # type: ignore

    return wrap_method




class HandlerRegistry(items.mvHandlerRegistry):
    """`mvHandlerRegistry` extension exposing global input handler methods, which
    can optionally be used as decorators.

    The signature of each method slightly differs from the DearPyGui command hook it
    uses. For all methods, the *callback* parameter is the only positional argument
    (optional). All other arguments are optional and keyword-only, including *key*
    and *button* arguments (formerly positional OR keyword) for those that use them.
    Each method returns the *callback* argument.

    Handler methods can be used as decorators both with and without parenthesis (you
    do not need to call them). Using parenthesis will allow for passing arguments;
    in this case, you should not include a *callback* argument.

    Command: `dearpygui.add_handler_registry`
    """

    @handler_hook(dearpygui.add_mouse_click_handler, _mouse_handler)
    def on_mouse_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button down and up event
        occur on the same object.

        Command: `dearpygui.add_mouse_click_handler`
        """

    @handler_hook(dearpygui.add_mouse_down_handler, _mouse_handler)
    def on_mouse_click_down(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is clicked/pressed.

        Command: `dearpygui.add_mouse_down_handler`
        """

    @handler_hook(dearpygui.add_mouse_release_handler, _mouse_handler)
    def on_mouse_click_up(self, *args, **kwargs):
        """Schedule a callback to run when a mouse button is released.

        Command: `dearpygui.add_mouse_release_handler`
        """

    @handler_hook(dearpygui.add_mouse_double_click_handler, _mouse_handler)
    def on_mouse_double_click(self, *args, **kwargs):
        """Schedule a callback to run when a mouse click event occurs twice consecutively
        on the same object.

        Command: `dearpygui.add_mouse_double_click_handler`
        """

    @handler_hook(dearpygui.add_mouse_wheel_handler, _mouse_handler)
    def on_mouse_wheel(self, *args, **kwargs):
        """Schedule a callback to run on mouse wheel input (excluding middle click).

        Command: `dearpygui.add_mouse_wheel_handler`
        """

    @handler_hook(dearpygui.add_mouse_move_handler, _mouse_handler)
    def on_mouse_move(self, *args, **kwargs):
        """Schedule a callback to run when a mouse is moved.

        Command: `dearpygui.add_mouse_move_handler`
        """

    @handler_hook(dearpygui.add_mouse_drag_handler, _mouse_handler)
    def on_mouse_drag(self, *args, **kwargs):
        """Schedule a callback to run when a mouse move event occurs during a mouse click
        down event.

        Command: `dearpygui.add_mouse_drag_handler`
        """

    @handler_hook(dearpygui.add_key_down_handler, _key_hander)
    def on_key_down(self, *args, **kwargs):
        """Schedule a callback to run on key down input. On many OS, this will fire
        continuously while the key is down.

        Command: `dearpygui.add_key_down_handler`

        NOTE: 'Key down' and 'key press' events are similar but not identical -- A 'key down'
        event occurs before a 'key press' event.
        """

    @handler_hook(dearpygui.add_key_press_handler, _key_hander)
    def on_key_press(self, *args, **kwargs):
        """Schedule a callback to run when a key is pressed. On many OS, this will fire
        continuously while the key is pressed.

        Command: `dearpygui.add_key_press_handler`

        NOTE: 'Key down' and 'key press' events are similar but not identical -- A 'key press'
        event occurs after a 'key down' event.
        """

    @handler_hook(dearpygui.add_key_release_handler, _key_hander)
    def on_key_up(self, *args, **kwargs):
        """Schedule a callback to run when a key is released.

        Command: `dearpygui.add_key_release_handler`
        """




class ItemHandlerRegistry(items.mvItemHandlerRegistry):
    """`mvItemHandlerRegistry` extension exposing global input handler methods, which
    can optionally be used as decorators.

    The signature of each method slightly differs from the DearPyGui command hook it
    uses. For all methods, the *callback* parameter is the only positional argument
    (optional). All other arguments are optional and keyword-only, including *key*
    and *button* arguments (formerly positional OR keyword) for those that use them.
    Each method returns the *callback* argument.

    Handler methods can be used as decorators both with and without parenthesis (you
    do not need to call them). Using parenthesis will allow for passing arguments;
    in this case, you should not include a *callback* argument.

    Command: `dearpygui.add_item_handler_registry`
    """

    @handler_hook(dearpygui.add_item_resize_handler)
    def on_resize(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is resized.

        Command: `dearpygui.add_item_resize_handler`
        """

    @handler_hook(dearpygui.add_item_clicked_handler, _mouse_handler)
    def on_click(self, *args, **kwargs):
        """Schedule a callback to run when both a mouse button down and button up events
        occur consecutively on a single item bound to this registry.

        Command: `dearpygui.add_item_clicked_handler`
        """

    @handler_hook(dearpygui.add_item_toggled_open_handler)
    def on_toggle_open(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is toggled open.

        Command: `dearpygui.add_item_toggled_open_handler`
        """

    @handler_hook(dearpygui.add_item_edited_handler)
    def on_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is edited.

        Command: `dearpygui.add_item_edited_handler`
        """

    @handler_hook(dearpygui.add_item_deactivated_after_edit_handler)
    def on_deactivation_after_edit(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is deactivated and
        recently edited.

        Command: `dearpygui.add_item_deactivated_after_edit_handler`
        """

    @handler_hook(dearpygui.add_item_activated_handler)
    def on_activation(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is interacted with.

        Command: `dearpygui.add_item_activated_handler`
        """

    @handler_hook(dearpygui.add_item_deactivated_handler)
    def on_deactivation(self, *args, **kwargs):
        """Schedule a callback to run when an item bound to this registry is deactivated.

        Command: `dearpygui.add_item_deactivated_handler`
        """

    @handler_hook(dearpygui.add_item_active_handler)
    def while_enabled(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is not disabled.

        Command: `dearpygui.add_item_active_handler`
        """

    @handler_hook(dearpygui.add_item_visible_handler)
    def while_visible(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is visible.

        Command: `dearpygui.add_item_visible_handler`
        """

    @handler_hook(dearpygui.add_item_focus_handler)
    def while_focused(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is focused.

        Command: `dearpygui.add_item_focus_handler`
        """

    @handler_hook(dearpygui.add_item_hover_handler)
    def while_hovered(self, *args, **kwargs):
        """Schedules a callback to run when an item bound to this registry is hovered.

        Command: `dearpygui.add_item_hover_handler`
        """


