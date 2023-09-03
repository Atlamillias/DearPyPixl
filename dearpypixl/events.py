import time
import functools
from dearpygui import dearpygui
from ._dearpypixl import api, tools, interface
from. _dearpypixl.common import (
    Item,
    ItemCallback,
    Any,
    Callable,
    TypeVar,
    TypeVarTuple,
    ParamSpec,
    overload,
)
from ._dearpypixl.callback import (
    callback,
    Callback,
    Callstack,
    CallStack,
)
from . import items


_T   = TypeVar("_T")
_N   = TypeVar("_N", float, int)
_Ts  = TypeVarTuple("_Ts")
_P   = ParamSpec("_P")




# handler signatures -- protocols are just more work here

def _handler(self, callback: ItemCallback | None = None, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...

def _mouse_handler(self, callback: ItemCallback | None = None, *, button: int = -1, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...

def _key_hander(self, callback: ItemCallback | None = None, *, key: int = -1, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs) -> ItemCallback | None: ...


def handler_hook(handler_fn: Any, protocol: Callable[_P, _T] = _handler) -> Callable[[Callable], Callable[_P, _T]]:
    def wrap_method(mthd: Any) -> Callable[_P, _T]:
        @functools.wraps(mthd)
        def mthd_add_handler(self, callback = None, *args, parent: Item = 0, **kwargs):
            def add_handler(callback):
                handler_fn(
                    callback=callback,
                    parent=parent or self,
                    **kwargs
                )
                return callback

            if callback is None:
                return add_handler
            return add_handler(callback)

        return mthd_add_handler  # type: ignore

    return wrap_method




class HandlerRegistry(items.mvHandlerRegistry):
    """`mvHandlerRegistry` extension exposing global input
    handler methods, which can optionally be used as decorators.

    The signature of each method slightly differs from the
    DearPyGui command hook used. For all methods, the *callback*
    parameter is the only positional argument. All other arguments
    are optional and keyword-only. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without
    parenthesis (you do not need to call them). Using parenthesis
    will allow for passing arguments; in this case, you should not
    include a *callback* argument.

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
    """`mvItemHandlerRegistry` extension exposing item handler
    as methods, which can optionally be used as decorators.

    The signature of each method slightly differs from the
    DearPyGui command hook used. For all methods, the *callback*
    parameter is the only positional argument. All other arguments
    are optional and keyword-only. Each method returns the
    *callback* argument.

    Handler methods can be used as decorators both with and without
    parenthesis (you do not need to call them). Using parenthesis
    will allow for passing arguments; in this case, you should not
    include a *callback* argument.

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




# [ UTILITY FUNCTIONS ]

@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, /, *, no_args: bool = False) -> Callable[[Callable[_P, Any]], Callable[_P, None]]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, /, *, no_args: bool = True) -> Callable[[Callable[[], Any]], Callable[[], None]]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = False) -> Callable[_P, None]: ...
@overload
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = True) -> Callable[[], None]: ...
def cooldown(timer_fn: Callable[[], _N], interval: _N, callback: Any = None, /, *, no_args: bool = False):
    """Return a wrapper that, when called, executes the target
    callable only if enough time has elapsed since the last time
    it was ran. This limits how often it can be executed over a
    period of time. Calls made to the returned wrapper while the
    target function is "cooling down" are no-op's.

    Can be used as a function decorator.

    Args:
        * timer_fn: A zero-argument callable that returns a time.

        * interval: The cooldown timer. The unit of time should match
        that of *timer_fn*s returned value.

        * callback: The target callable to apply the cooldown to.
        If *no_args* is set, it must be callable without arguments.

        * no_args: Improves the efficieny of the returned function,
        but limits *callback* options to zero-argument callables.

    The time units of *interval* and the return of *timer_fn*
    should match. For example, if *timer_fn* returns a number of
    fractional seconds (i.e. `time.perf_counter`), then *interval*
    is also expected to be a number of seconds.

    By default, the target callback's metadata is passed onto
    the returned wrapper via `functools.wraps`. When the *no_args*
    flag is set, the `.__next__` method of the underlying generator
    object is returned instead of a wrapper function. In this case,
    metadata is not copied over.

    This function does not create or utilize threads.
    """
    def capture_callback(callback: Callable) -> Callable:
        if no_args:

            def recurring_tasker():  # type: ignore
                ts_last_update = timer_fn() - interval
                while True:
                    ts_this_update = timer_fn()
                    if ts_this_update - ts_last_update >= interval:
                        ts_last_update = ts_this_update
                        callback()
                    yield

            dispatcher = recurring_tasker().__next__  # type: ignore

        else:

            def recurring_tasker():
                ts_last_update = timer_fn() - interval
                args, kwds = yield
                while True:
                    ts_this_update = timer_fn()
                    if ts_this_update - ts_last_update >= interval:
                        ts_last_update = ts_this_update
                        callback(*args, **kwds)
                    args, kwds = yield

            @functools.wraps(callback)
            def dispatcher(*args, **kwargs) -> None:
                _dispatcher.send((args, kwargs))

            _dispatcher = recurring_tasker()
            next(_dispatcher)  # prime generator

        return dispatcher

    if callback is None:
        return capture_callback
    return capture_callback(callback)


@overload
def cooldown_s(interval: _N, /, *, no_args: bool = False) -> Callable[[Callable[_P, Any]], Callable[_P, None]]: ...
@overload
def cooldown_s(interval: _N, /, *, no_args: bool = True) -> Callable[[Callable[[], Any]], Callable[[], None]]: ...
@overload
def cooldown_s(interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = False) -> Callable[_P, None]: ...
@overload
def cooldown_s(interval: _N, callback: Callable[_P, Any], /, *, no_args: bool = True) -> Callable[[], None]: ...
def cooldown_s(interval: _N, callback: Any = None, /, no_args: bool = False):  # type: ignore
    """Adds a cooldown to a callable with an interval in
    fractional seconds.

    Refer to the `cooldown` function for more information.
    """
    return cooldown(time.perf_counter, interval, callback, no_args=no_args)


def root_ihandler_registry(item: Item) -> items.mvItemHandlerRegistry:
    """Return the item handler registry bound to an item's
    root parent. If unbound, create a new registry,
    bind it to the root parent, and return the new registry.
    """
    root_parent = api.Item.root_parent(item)
    root_ihr = api.Item.information(root_parent)['handlers']
    if not root_ihr:
        root_ihr = items.mvItemHandlerRegistry()
        api.Item.set_handlers(root_parent, root_ihr)
        return root_ihr
    return items.mvItemHandlerRegistry.new(root_ihr)


def resized_fill_content_region(
    item: Item,
    *,
    autosize_x : bool = True,
    autosize_y : bool = True,
    share_space: bool = False,
) -> items.ResizeHandler:
    """Emulate the behavior of assigning a "stretch" policy
    onto the target item; when its' root parent is resized,
    the target will be sized to consume the available space
    within its' direct parent.

    Args:
        * item: Target item to resize.

        * autosize_x: If True, the target item's width will be
        adjusted to fill its' parent's available space. Cannot
        be False if *autosize_y* is False.

        * autosize_y: If True, the target item's height will be
        adjusted to fill its' parent's available space. Cannot
        be False if *autosize_x* is False.

        * share_space: If True, the target item will be sized
        to fit as many of its' parent's children in the default
        view as possible. Otherwise, it will occupy as much of
        the default viewing space as possible; pushing its'
        younger sibling items into its' parent's scroll region.


    A `TypeError` or `ValueError` is raised when one or more of
    the following conditions are not met prior to calling this
    function;
        - the target item must be non-root item

        - the target item must be sizable via 'width' and/or
        'height' configuration

        - the target item's direct parent must support the
        'content_region_avail' state

        - the target item's root parent must support the
        'resized' state

    This function attaches a `mvResizeHandler` onto the
    target item's root parent. If the root parent does not
    have a bound item handler registry, one is created and
    assigned prior to creating and attaching the handler.
    The created `mvResizeHandler` item is destroyed when the
    callback is triggered and either the target item or its'
    direct parent are destroyed.

    *share_space* is automatically set to False when the
    scroll region of the target's direct parent cannot be
    managed.

    The target's root parent will almost always be a
    `mvWindowAppItem` item, which supports 'resized'. Parent
    items that support 'content_region_avail' include
    `mvChildWindow` and `mvGroup` items. The target can be
    any sizable item, such as a `mvButton`, `mvChildWindow`,
    or `mvPlot` item.
    """
    item_config = api.Item.configuration(item)
    item_info   = api.Item.information(item)
    if (
        (autosize_x and "width" not in item_config) or
        (autosize_y and "height" not in item_config)
    ):
        raise TypeError(
            f"{item_info['type'].split('::')[1]!r} item {item!r} cannot be sized."
        )
    elif not (autosize_x or autosize_y):
        raise ValueError(
            f"`autosize_x/y` cannot both be False."
        )

    parent = item_info['parent']
    if not parent:
        raise TypeError(
            f"target cannot be a top-level root item."
        )
    parent_state  = api.Item.state(parent)
    if not parent_state['content_region_avail']:
        _parent_tp = api.Item.information(parent)['type'].split('::')[1]
        raise TypeError(
            f"parent {_parent_tp!r} item does not have a content region."
        )

    root_parent = api.Item.root_parent(item)
    root_info   = api.Item.information(root_parent)
    if not root_info['resized_handler_applicable']:
        raise TypeError(
            f"top-level parent {root_info['type'].split('::')[1]!r} item "
            f"does not support resize handlers."
        )

    root_ihr = root_info['handlers']
    if not root_ihr:
        root_ihr = ItemHandlerRegistry()
        api.Item.set_handlers(root_parent, root_ihr)

    if share_space:
        try:
            api.Window.get_x_scroll_pos(parent)
        except:
            share_space = False

    # When *share_space* is False, the target item will
    # always push its' younger siblings into its' parent's
    # scroll area.
    # When *share_space* is True, it tries to accomodate
    # them instead. This adjustment is made next frame to
    # allow DPG to update the parent's scroll area; taking
    # into account the prior change(s) made to the target.
    #
    # In either case, the calculation can be negative. DPG
    # will parse those values as unsigned (positive). This
    # works out fine when *share_space* is False, but `max`
    # needs to be used otherwise.
    if autosize_x and autosize_y:
        cb_body = [
            "avail_wt, avail_ht = parent.state()['content_region_avail']",
            "item.configure(",
            "    width=avail_wt - parent.x_scroll_max(),",
            "    height=avail_ht - parent.y_scroll_max(),",
            ")",
        ]
        if share_space:
            cb_body.extend((
                "split_frame()",
                "item.configure(",
                "    width=max(1, avail_wt - parent.x_scroll_max()),",
                "    height=max(1, avail_ht - parent.y_scroll_max()),",
                ")",
            ))
    elif autosize_x:
        cb_body = [
            "avail_wt = parent.state()['content_region_avail'][0]",
            "item.configure(width=avail_wt - parent.x_scroll_max())",
        ]
        if share_space:
            cb_body.extend((
                "split_frame()",
                "item.configure(width=max(1, avail_wt - parent.x_scroll_max()))",
            ))
    else:
        cb_body = [
            "avail_ht = parent.state()['content_region_avail'][1]",
            "item.configure(height=avail_ht - parent.y_scroll_max())",
        ]
        if share_space:
            cb_body.extend((
                "split_frame()",
                "item.configure(height=max(1, avail_ht - parent.y_scroll_max()))",
            ))

    cb_body = (
        "try:",
        *(f'    {ln}' for ln in cb_body),
        "except SystemError:",
        "    if not item.exists() or not parent.exists():",
        "        handler.destroy()",
        "    else:",
        "        raise",
    )

    handler  = items.ResizeHandler.new()
    callback = tools.create_function(
        'callback',
        (),
        cb_body,
        globals=globals(),
        locals={
            'item'       : interface.mvAll(item),
            'parent'     : interface.mvAll(parent),
            'handler'    : handler,
            'split_frame': api.Runtime.split_frame,
        }
    )
    handler.init(callback=callback, parent=root_ihr)
    return handler
