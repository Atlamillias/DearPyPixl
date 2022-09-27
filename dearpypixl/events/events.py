import functools
import collections
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence
from dearpygui import dearpygui
from dearpygui._dearpygui import (
    get_frame_count,
    set_frame_callback,
    set_exit_callback,
    bind_item_handler_registry,
)
from dearpygui.dearpygui import add_item_handler_registry, add_handler_registry
from dearpypixl._internal.utilities import TypeGuard, get_positional_args_count, prep_callback
from .handlers import *
from .keycodes import Key, Mouse
from .._internal.item import (
    Item,
    LinkedItem,
    ItemData,
)


def _manage_handler(handler: HandlerItem):
    def wrapped_method(_method):
        @functools.wraps(_method)
        def register_callback(self, callback: Callable = None, **kwargs):
            @functools.wraps(callback)
            def create_handler(callback):
                handler(
                    label=callback.__name__,
                    callback=callback,
                    parent=int(self),
                    **kwargs,
                )
                return callback

            if callback is None:
                return create_handler
            return create_handler(callback)

        return register_callback

    return wrapped_method


class AppEvents(Item):
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvHandlerRegistry, "mvHandlerRegistry"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(
            dearpygui.mvKeyDownHandler,
            dearpygui.mvKeyPressHandler,
            dearpygui.mvKeyReleaseHandler,
            dearpygui.mvMouseMoveHandler,
            dearpygui.mvMouseWheelHandler,
            dearpygui.mvMouseClickHandler,
            dearpygui.mvMouseDoubleClickHandler,
            dearpygui.mvMouseDownHandler,
            dearpygui.mvMouseReleaseHandler,
            dearpygui.mvMouseDragHandler,
        ),
        command=add_handler_registry,
    )

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        show: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )

    @_manage_handler(KeyDownHandler)
    def while_key_down(
        self,
        callback: Callable = None,
        *,
        key: Key | int = Key.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(KeyPressHandler)
    def on_key_press(
        self,
        callback: Callable = None,
        *,
        key: Key | int = Key.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(KeyReleaseHandler)
    def on_key_up(
        self,
        callback: Callable = None,
        *,
        key: Key | int = Key.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(MouseDownHandler)
    def on_mouse_button_down(
        self,
        callback: Callable = None,
        *,
        button: Mouse | int = Mouse.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(MouseClickHandler)
    def on_mouse_button_click(
        self,
        callback: Callable = None,
        *,
        button: Mouse | int = Mouse.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(MouseDoubleClickHandler)
    def on_mouse_button_double_click(
        self,
        callback: Callable = None,
        *,
        button: Mouse | int = Mouse.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(MouseReleaseHandler)
    def on_mouse_button_up(
        self,
        callback: Callable = None,
        *,
        button: Mouse | int = Mouse.ANY,
        user_data: Any = None,
        **kwargs,
    ):
        ...

    @_manage_handler(MouseMoveHandler)
    def on_mouse_move(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ):
        ...

    @_manage_handler(MouseWheelHandler)
    def on_mouse_wheel_scroll(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ):
        ...

    @_manage_handler(MouseDragHandler)
    def on_mouse_drag(
        self,
        callback: Callable = None,
        *,
        button: Mouse | int = Mouse.ANY,
        threshold: float = 10.0,
        user_data: Any = None,
        **kwargs,
    ):
        ...


class ItemEvents(LinkedItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvItemHandlerRegistry, "mvItemHandlerRegistry"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        command=add_item_handler_registry,
        able_parents=(),
        able_children=(
            dearpygui.mvActivatedHandler,
            dearpygui.mvActiveHandler,
            dearpygui.mvClickedHandler,
            dearpygui.mvDeactivatedAfterEditHandler,
            dearpygui.mvDeactivatedHandler,
            dearpygui.mvEditedHandler,
            dearpygui.mvFocusHandler,
            dearpygui.mvHoverHandler,
            dearpygui.mvResizeHandler,
            dearpygui.mvToggledOpenHandler,
            dearpygui.mvVisibleHandler,
        ),
    )

    _bind = bind_item_handler_registry  # ABC
    CATEGORY = True  # ABC

    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        show: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )

    @_manage_handler(ActiveHandler)
    def while_active(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(ActivatedHandler)
    def on_activation(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(DeactivatedHandler)
    def on_deactivation(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(DeactivatedAfterEditHandler)
    def on_deactivation_after_edit(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(ClickedHandler)
    def on_click(
        self, callback: Callable = None, *, user_data: Any = None, button=-1, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(EditedHandler)
    def on_edit(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(FocusHandler)
    def on_focus(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(HoverHandler)
    def on_hover(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(ResizeHandler)
    def on_resize(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(ToggledOpenHandler)
    def on_toggle_open(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    @_manage_handler(VisibleHandler)
    def on_visible(
        self, callback: Callable = None, *, user_data: Any = None, **kwargs
    ) -> Callable:
        ...

    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")


@dataclass
class Callback:
    _callback: Callable = field(repr=False)
    _user_data: Any = field(repr=False, default=None)
    _sender: Any = field(repr=False, default=None)
    _app_data: Any = field(repr=False, default=None)

    def __post_init__(self) -> None:
        # Note that DearPyGui doesn't send any arguments to callbacks set
        # with `dpg.set_exit_callback` or `dpg.set_frame_callback` even if
        # you include user_data. This implementation will try to send those
        # arguments regardless (if able) to emulate the missing behavior.
        self._pos_arg_cnt = ...
        self._arguments = ...
        self._unwrapped_cb = self._callback
        self.update(callback=self._callback)

    def __call__(self, *_, **kwargs) -> None:
        # `_` could be `sender`, `app_data`, and `user_data` arguments
        # from DPG. They aren't needed.
        self._callback(*self._arguments, **kwargs)

    @property
    def callback(self) -> Callable:
        return self._callback

    @property
    def sender(self) -> Any:
        return self._sender

    @property
    def app_data(self) -> Any:
        return self._app_data

    @property
    def user_data(self) -> Any:
        return self._user_data

    __NULL = object()

    def update(
        self,
        *,
        callback: Callable = None,
        sender: Any = __NULL,
        app_data: Any = __NULL,
        user_data: Any = __NULL,
    ) -> None:
        NULL = self.__NULL
        if sender is not NULL:
            self._sender = sender
            # re-wrap callback because `prep_callback` replaces 'sender' with the
            # first argument used to call it...
            self._callback = prep_callback(self._sender or self, self._unwrapped_cb)
        if app_data is not NULL:
            self._app_data = app_data
        if user_data is not NULL:
            self._user_data = user_data

        if callback:
            if not callable(callback):
                raise ValueError("`callback` is not callable.")
            self._unwrapped_cb = callback
            self._callback = prep_callback(self._sender or self, self._unwrapped_cb)
            self._pos_arg_cnt = get_positional_args_count(self._unwrapped_cb)

        # `prep_callback` already has `sender` locally-bound -- it will send
        # it in place of the first argument.
        self._arguments = (None, self._app_data, self._user_data)[: self._pos_arg_cnt]


class FrameEvents(dict):
    """A dictionary-like object that manages frame callbacks.

    Almost every method accepts a `frame` (int) argument. This argument must
    be must be greater than or equal to -1. A value of -1 specifies callbacks to
    run on the last frame (application exit) and a value of 0 specifies callbacks
    scheduled to run every frame. Every other value is tied to a specific frame
    (rendered or otherwise).

    DearPyGui only allows a maximum of 50 callbacks to be scheduled between all
    frames. However, you can schedule as many callbacks as you want for the last
    frame (uses key -1) and all frames (uses key 0).
    """
    # TODO: Inherit from `defaultdict`
    setdefault = NotImplementedError
    pop = NotImplementedError
    popitem = NotImplementedError
    update = NotImplementedError

    __keyguard = TypeGuard((int,), lambda key: key >= -1)
    __unlocked_exists = False

    ALL_FRAMES = 0
    LAST_FRAME = -1

    def __init__(self, *, locked: bool = True) -> None:
        # NOTE: While this was made for the `Application` class, it can be used
        # elsewhere. However, there should only ever be ONE unlocked instance
        # of this class (`Application` uses the unlocked instance).
        super().__init__()
        super().__setitem__(0, [])  # avoiding `_set_frame_callback` in `get`
        if locked:
            self._set_frame_callback = NotImplemented
            self.get = super().__getitem__
        else:
            if self.__unlocked_exists:
                raise ValueError(f"Unlocked instance already exists.")
            type(self).__unlocked_exists = True

    def _set_frame_callback(self, frame: int) -> None:
        """Sets the main callback for a specific frame. It will call any event
        that is set to run on that frame.
        """

        def frame_callback(*args, **kwargs) -> None:
            for event in self[frame]:
                event(*args, **kwargs)

        if frame == self.LAST_FRAME:
            set_exit_callback(frame_callback)
        else:
            set_frame_callback(frame, frame_callback)

    @__keyguard.wraps(target_idx=1)
    def get(self, frame: int) -> list[Callback]:
        """Return the list of callbacks set to run on the specified frame.

        Args:
            * frame (int): Frame to query.
        """
        # This is basically a combination of `setdefault` and `get` methods. It
        # will not raise KeyError if <frame> isn't a key. It will be added as a
        # new entry.
        if frame not in self:
            super().__setitem__(frame, [])
            self._set_frame_callback(frame)
        return super().__getitem__(frame)

    @__keyguard.wraps(target_idx=1)
    def __setitem__(
        self, frame: int, callback: Callback | tuple[Callable, Any] | Callable
    ):
        # No work needs to be done.
        if isinstance(callback, Callback):
            return self[frame].append(callback)
        # Create a FrameEvent instance for the callback.
        elif not isinstance(callback, Sequence):
            callback = (callback,)
        self[frame].append(Callback(*callback))

    __getitem__ = get

    def clear(self) -> None:
        """Clear/unregister all callbacks for all frames."""
        for frame_events in self.values():
            frame_events.clear()

    def flush(self, frame: int = None) -> None:
        """Clear/unregister all callbacks for the specified frame.

        Args:
            * frame (int, optional): Clear callbacks for this frame. If
            default, clears callbacks for frames already rendered.
        """
        # Once added, a frame key should NEVER be deleted, even if it's
        # empty (so no `self.pop`). When the default key/value is initially
        # added, `dpg.set_frame_callback` is called creating setting a main
        # callback loop for that frame. If the key (frame) is re-created
        # for a frame that has not been rendered yet, another main loop will
        # be created for the same frame. Technically, it's safe to destroy
        # keys for frames already rendered, but why complicate things...?
        if frame is None:  # all previously-rendered frames
            current_frame = get_frame_count()
            for _, f in enumerate(self):
                if current_frame > f:
                    self[f].clear()
        else:
            self[frame].clear()

    def on_frame(
        self,
        callback: Callable = None,
        /,
        *,
        frame: int = ALL_FRAMES,
        user_data: Any = None,
        **kwargs,
    ):
        """(Decorator) Schedules a callback to run on a specific frame.

        Args:
            * callback (Callable): Callable object to run.

            * frame (int, optional): The callback will run before this frame is rendered. If this
            value is 0, it will run every frame. If -1, it will run on the last frame (application
            exit). Defaults to 0.

            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
        """
        def _on_frame(_callback):
            self[frame] = _callback, user_data, kwargs
            return _callback

        if callback is None:
            return _on_frame
        return _on_frame(callback)
