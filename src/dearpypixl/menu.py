import sys
import typing
import threading
import collections

from dearpygui import dearpygui, _dearpygui

from dearpypixl.core import protocols
from dearpypixl.core import itemtype
from dearpypixl.core import codegen
from dearpypixl import items, color, style, theming

__all__ = (
    "ContextMenuStack",
    "ContextMenu", "add_context_menu", "context_menu",
    "ContextMenuItem", "add_context_menu_item",
)




_MISSING = object()


class ContextMenuStack:
    __slots__ = ("_stack", "_lock", "_root_menu", "_open_handler", "_close_handler", "_handlers")

    @property
    def root_menu(self, /) -> ContextMenu | None:
        return self._root_menu
    @root_menu.setter
    def root_menu(self, value: ContextMenu | None, /) -> None:
        try:
            if value is None:
                self._open_handler.callback = None
            else:
                self._open_handler.callback = self._cb_open_menus
        except AttributeError:
            self._item_init()
            self.root_menu = value

        self._root_menu  = value

    def __init__(self, /) -> None:
        self._stack = collections.deque[tuple["ContextMenu", "ContextMenuItem | None"]]()
        self._lock = threading.RLock()

    def __del__(self, /) -> None:
        if sys.is_finalizing():
            return
        try:
            dearpygui.delete_item(self._handlers)
        except (AttributeError, SystemError):
            pass

    def __enter__(self) -> None:
        self._lock.acquire()

    def __exit__(self, exc_type=None, error=None, traceback=None, /) -> None:
        self._lock.release()

    def __bool__(self, /) -> bool:
        return bool(self._stack)

    def __iter__(self):
        return iter(self._stack)

    def __len__(self):
        return len(self._stack)

    def __getitem__(self, index: typing.SupportsIndex, /):
        return self._stack[index]

    def _item_init(self, /):
        self._handlers = items.handler_registry()
        self._close_handler = items.add_mouse_down_handler(parent=self._handlers, callback=self._cb_close_menus)
        self._open_handler = items.add_mouse_release_handler(_dearpygui.mvMouseButton_Right, parent=self._handlers)

    def _menus_opened(self, /) -> None:
        try:
            self._close_handler.show = True
            self._open_handler.show = False
        except AttributeError:
            self._item_init()
            self._menus_opened()

    def _menus_closed(self, /) -> None:
        try:
            self._close_handler.show = False
            self._open_handler.show = True
        except AttributeError:
            self._item_init()
            self._menus_closed()

    def _cb_close_menus(self, _, input_info: tuple[int,  float], /) -> None:
        if not self._stack:
            return

        duration = input_info[1]
        if duration >= 0.05 or self.hovered():  # ignore long-press/drag events
            return

        self.clear()

    def _cb_open_menus(self, /) -> None:
        root_menu = self.root_menu
        if not root_menu:
            return

        root_menu.to_cursor()

    _PUSH_KWARGS: typing.Any = {"show": True, "no_bring_to_front_on_focus": False}

    def push(self, context: ContextMenu | tuple[ContextMenu, ContextMenuItem | None], /, **config) -> None:
        config.update(__class__._PUSH_KWARGS)

        with self._lock:
            if not isinstance(context, tuple):
                if self._stack:
                    raise TypeError("owner item required when stack is not empty")
                context = (context, None)

            if not self._stack:
                self._menus_opened()

            self._stack.appendleft(context)
            context[0].configure(**config)

    _POP_KWARGS: typing.Any = {"show": False, "no_bring_to_front_on_focus": False}

    def pop(self, /) -> tuple[ContextMenu, ContextMenuItem | None]:
        with self._lock:
            items = self._stack.popleft()
            items[0].configure(**__class__._POP_KWARGS)

            if not self._stack:
                self._menus_closed()

        return items

    def hovered(self) -> tuple[ContextMenu, ContextMenuItem | None] | None:
        with self._lock:
            csr_x_pos, csr_y_pos = _dearpygui.get_mouse_pos(local=False)
            for menus in self._stack:
                state = menus[0].state()
                x_pos, y_pos   = state['pos']        # type: ignore
                x_size, y_size = state['rect_size']  # type: ignore
                if (
                    (x_pos <= csr_x_pos <= x_pos + x_size)
                    and
                    (y_pos <= csr_y_pos <=  y_pos + y_size)
                ):
                    return menus

    def remove(self, context: ContextMenu | tuple[ContextMenu, ContextMenuItem | None], /) -> None:
        if not isinstance(context, tuple):
            context = (context, None)

        stack = self._stack
        config = __class__._POP_KWARGS

        with self._lock:
            if not stack:
                return

            target_menu, target_owner = context

            while True:
                items = (menu, owner) = stack.popleft()
                if menu == target_menu:
                    self._stack.appendleft(items)
                    break

                if owner != target_owner:
                    menu.configure(**config)

            if not stack:
                self._menus_closed()

    def clear(self, /) -> None:
        config = __class__._POP_KWARGS

        with self._lock:
            if not self._stack:
                return

            for menu, owner in self._stack:
                menu.configure(**config)

            self._menus_closed()
            self._stack.clear()


_CONTEXT_STACK = ContextMenuStack()  # type: ignore




class ContextMenuColor(
    theming.color_component_type((
        color.button,
        color.button_active,
        color.button_hovered,
        color.header,
        color.header_active,
        color.header_hovered,
        color.window_bg,
    ))
):
    __slots__ = ()

    button: typing.Any
    button_active: typing.Any
    button_hovered: typing.Any
    header: typing.Any
    header_active: typing.Any
    header_hovered: typing.Any
    window_bg: typing.Any

class ContextMenuStyle(
    theming.style_component_type((
        style.item_spacing,
        style.window_rounding,
        style.window_rounding,
        style.window_padding,
        style.popup_rounding,
        style.frame_rounding,
        style.frame_padding,
        style.frame_padding,
    ))
):
    __slots__ = ()

    item_spacing: typing.Any
    window_rounding: typing.Any
    window_rounding: typing.Any
    window_padding: typing.Any
    popup_rounding: typing.Any
    frame_rounding: typing.Any
    frame_padding: typing.Any
    frame_padding: typing.Any




class ContextMenuItem(itemtype.CompositeItem, items.mvGroup):
    _name_text: items.mvText
    _tail_text: items.mvText
    _child_menu: ContextMenu | None = None  # see `ContextMenu.pop()`

    context_stack: ContextMenuStack = _CONTEXT_STACK
    callback: protocols.ItemCallback | None = None

    @typing.overload
    @classmethod
    def create(cls, label: str, *, context_stack: ContextMenuStack | None = None, callback: typing.Callable | None = None, user_data: typing.Any = None, use_internal_label: bool = True, tag: int | str = 0, width: int = 0, height: int = 0, indent: int = -1, parent: int | str = 0, before: int | str = 0, payload_type: str = '$', drag_callback: protocols.ItemCallback0 | protocols.ItemCallback1[int | str] | protocols.ItemCallback2[int | str, typing.Any] | protocols.ItemCallback3[int | str, typing.Any, typing.Any] | None = None, drop_callback: protocols.ItemCallback0 | protocols.ItemCallback1[int | str] | protocols.ItemCallback2[int | str, typing.Any] | protocols.ItemCallback3[int | str, typing.Any, typing.Any] | None = None, show: bool = True, enabled: bool = True, pos: typing.Sequence[int] = ..., filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0, **kwargs) -> typing.Self: ... # pyright: ignore[reportInconsistentOverload]
    @classmethod
    def create(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        label: str,
        *,
        context_stack: typing.Any = None,
        callback: typing.Any = None,
        **kwargs,
    ) -> typing.Self:
        self = cls(tag=cls.__itemtype_command__(**kwargs))

        if context_stack is not None:
            self.context_stack = context_stack

        with items.mvItemHandlerRegistry.create() as handlers:
            items.mvHoverHandler.create(callback=self._on_hover)
        self.handlers = handlers

        # This button is this item's clickable element and will
        # span the entire group. It's used over other items for
        # theme element compatibility (e.g. rounded corners, etc).
        items.add_button(width=-1, height=1, callback=self._on_click, parent=self).theme = __class__._get_clickitem_theme()

        with items.table(
            parent=items.add_group(label="[1] layout", parent=self),  # needed for rect size & positioning
            header_row=False,
            no_host_extendX=True,
            no_keep_columns_visible=True,
            context_menu_in_body=False,
            sortable=False,
            resizable=False,
            reorderable=False,
            scrollY=False,
            scrollX=False,
            no_clip=True,
        ):
            row = items.add_table_row()

            # padding (affected by theme padding)
            items.add_table_column(label='[0] padding', width_fixed=True, no_clip=True, no_reorder=True, no_sort=True)
            items.add_spacer(parent=row)
            # text (name)
            items.add_table_column(label='[1] text (name)', width_fixed=True, no_clip=True, no_reorder=True, no_sort=True)
            self._name_text = items.add_text(parent=row)
            # spacing (affected by theme spacing)
            # XXX: This "spacer" is needed so the parent group can
            # report an accurate rect size. An empty, stretchy column
            # is not enough — it needs content to consume the space.
            items.add_table_column(label='[2] spacing', no_reorder=True, no_sort=True, width_stretch=True, indent_disable=True, indent_enable=False)
            items.add_button(parent=row, width=-1, height=1).theme = __class__._get_dummyitem_theme()
            # text (tail)
            items.add_table_column(label='[3] text (tail)', width_fixed=True, no_reorder=True, no_sort=True)
            self._tail_text = items.add_text(parent=row)
            # padding (affected by theme padding)
            items.add_table_column(label='[4] padding', width_fixed=True, no_clip=True, no_reorder=True, no_sort=True)
            items.add_spacer(parent=row)

        self.label = label
        self.callback = callback
        self.components = (handlers,)

        return self

    @property
    def label(self, /) -> str:
        return _dearpygui.get_item_configuration(self)["label"]
    @label.setter
    def label(self, value: str, /) -> None:
        _dearpygui.configure_item(self, label=value)
        name, _, tail = value.partition("##")
        self._name_text.value = name
        self._tail_text.value = tail
    @label.deleter
    def label(self, /) -> None:
        _dearpygui.configure_item(self, label='')
        self._name_text.value = self._tail_text.value = ''

    @typing.overload
    def configure(self, *, label: str = ..., user_data: typing.Any = None, use_internal_label: bool = True, width: int = 0, height: int = 0, indent: int = -1, payload_type: str = '$', drag_callback: protocols.ItemCallback | None = None, drop_callback: protocols.ItemCallback, show: bool = True, enabled: bool = True, pos: typing.Sequence[int] = ..., filter_key: str = '', tracked: bool = False, track_offset: float = 0.5, horizontal: bool = False, horizontal_spacing: float = -1, xoffset: float = 0) -> None: ... # pyright: ignore[reportInconsistentOverload]
    def configure(self, *, label=_MISSING, callback=_MISSING, **kwargs):
        super().configure(**kwargs)
        if callback is not _MISSING:
            self.callback = callback  # type: ignore
        if label is not _MISSING:
            self.label = label  # type: ignore

    def configuration(self) -> dict[typing.Literal['label', 'user_data', 'use_internal_label', 'width', 'height', 'indent', 'payload_type', 'drag_callback', 'drop_callback', 'show', 'enabled', 'filter_key', 'tracked', 'track_offset', 'horizontal', 'horizontal_spacing', 'xoffset', 'callback'], typing.Any]: # pyright: ignore[reportIncompatibleMethodOverride]
        config = super().configuration()
        config["callback"] = self.callback # type: ignore
        return config # type: ignore

    @staticmethod
    def _get_clickitem_theme():
        alias = f"{__name__}.{__class__.__name__}.<internal-0>"
        if _dearpygui.does_item_exist(alias):
            return items.mvTheme(tag=alias)

        with items.mvTheme.create(tag=alias) as theme:
            with items.mvThemeComponent.create():
                color.button(0, 0, 0, 0)

        return theme

    @staticmethod
    def _get_dummyitem_theme():
        alias = f"{__name__}.{__class__.__name__}.<internal-1>"
        if _dearpygui.does_item_exist(alias):
            return items.mvTheme(tag=alias)

        with items.mvTheme.create(tag=alias) as theme:
            with items.mvThemeComponent.create():
                color.button(0, 0, 0, 0)
                color.button_active(0, 0, 0, 0)
                color.button_hovered(0, 0, 0, 0)

        return theme

    def _on_click(self, sender = 0, app_data = None, user_data = None, /) -> None:
        callback = self.callback
        if callback is None:
            return

        match callback.__code__.co_argcount:
            case 0:
                args = ()
            case 1:
                args = (self,)
            case 2:
                args = (self, app_data)
            case _:
                args = (self, app_data, self.user_data)

        self.context_stack.clear()
        callback(*args)  # pyright: ignore[reportArgumentType]

    def _on_hover(self, sender = 0, app_data = None, user_data = None, /) -> None:
        child_menu  = self._child_menu
        parent_menu = ContextMenu(tag=self.root_parent)

        stack = self.context_stack
        entry = (child_menu, self)

        with stack:
            if stack:
                if stack[0] == entry:
                    return

                stack.remove(parent_menu)

            if child_menu is None:
                return

            # HACK: imgui won't calculate an item's size if it hasn't
            # been rendered yet, so show it off-screen and wait a frame
            # BUG: this will make imgui calculate the the menu's inner
            # padding, but the menu's content size — it still risks getting
            # clipped off-screen when displayed for the first time
            menu_wt, menu_ht = child_menu.rect_size
            if not (menu_wt or menu_ht):
                client_wt = _dearpygui.get_viewport_configuration(0)["client_width"]
                child_menu.configure(show=True, pos=(100 + client_wt, 0))
                _dearpygui.split_frame(delay=16)

                menu_wt, menu_ht = child_menu.rect_size

            # the position of the child menu defaults to the right/down, but
            # may be positioned left/up if the menu is at risk of clipping
            viewport_config = _dearpygui.get_viewport_configuration(0)
            viewport_wt = viewport_config["client_width"]
            viewport_ht = viewport_config["client_height"]

            state = _dearpygui.get_item_state(self)
            x_min, y_min = state["rect_min"]
            x_max, y_max = state["rect_max"]

            # horizontal alignment
            x_offset = int((parent_menu.rect_size[0] - state["rect_size"][0]) * 0.25)  # w/50% of our parent's padding
            if menu_wt < viewport_wt - x_max:
                x_pos = x_max + x_offset  # show menu right
            else:
                x_pos = x_min - menu_wt - x_offset  # show menu left
            # vertical alignment
            if menu_ht < viewport_ht - y_min:
                # position menu so that the the top edge of its first child
                # aligns with the top edge of THIS item
                try:
                    menu_child_item = _dearpygui.get_item_info(child_menu)['children'][1][0]
                except IndexError:  # menu is empty
                    y_pos = y_min
                else:
                    y_pos = y_min - _dearpygui.get_item_state(menu_child_item)['pos'][1]
            else:
                y_pos = viewport_ht - menu_ht
                if y_pos < 0:
                    y_pos = 0

            stack.push(entry, pos=(x_pos, y_pos))  # pyright: ignore[reportArgumentType]
            #parent_menu.configure(no_bring_to_front_on_focus=True)


@codegen.wrapped(ContextMenuItem.create)
def add_context_menu_item(*args, **kwargs) -> ContextMenuItem:  # pyright: ignore
    return ContextMenuItem.create(*args, **kwargs)




class _ContextMenuItemCommand[T: ContextMenuItem = ContextMenuItem](typing.Protocol):
    def __call__(self, *, label: str, parent: int | str, tag: int | str = ..., context_stack: ContextMenuStack = ...) -> T: ...


class ContextMenu[U = typing.Any, C: ContextMenuItem = typing.Any](itemtype.CompositeItem, items.mvWindowAppItem[U, C]):
    __itemtype_indexer_type__ = ContextMenuItem
    __itemtype_indexer_slot__ = 1

    @staticmethod
    def get_default_theme() -> items.mvTheme[typing.Any, items.mvThemeComponent]:
        alias = f"{__name__}.{__class__.__name__}.theme<default>"
        if _dearpygui.does_item_exist(alias):
            return items.mvTheme(tag=alias)

        with items.mvTheme.create(tag=alias) as theme:
            color = ContextMenuColor.create(
                tag=f"{__name__}.{__class__.__name__}.color<default>"
            )
            color.button = (0, 0, 0, 0)
            color.button_active = (29, 151, 236, 103)
            color.button_hovered = (29, 151, 236, 103)
            color.header = (0, 0, 0, 0)
            color.header_active = (29, 151, 236, 103)
            color.header_hovered = (29, 151, 236, 103)
            color.window_bg = (37, 37, 38, 255)

            style = ContextMenuStyle.create(
                tag=f"{__name__}.{__class__.__name__}.style<default>"
            )
            style.item_spacing = (8, 10)
            style.window_rounding = (0, -1)
            style.window_rounding = (0, -1)
            style.window_padding = (24, 8)
            style.popup_rounding = (0, -1)
            style.frame_rounding = (0, -1)
            style.frame_padding = (4, 3)
            style.frame_padding = (4, 3)

        return theme

    context_stack: ContextMenuStack = _CONTEXT_STACK
    item_factory: _ContextMenuItemCommand = ContextMenuItem.create

    @classmethod
    def create(
        cls,
        label         = '',
        *,
        context_stack: ContextMenuStack | None = None,
        item_factory: _ContextMenuItemCommand | None = None,
        width        = -1,
        height       = -1,
        show         = False,
        autosize     = True,
        no_resize    = True,
        no_title_bar = True,
        no_move      = True,
        min_size     = (5, 5),
        # ignored
        no_focus_on_appearing      = False,
        no_bring_to_front_on_focus = False,
        no_collapse                = True,
        modal                      = False,
        popup                      = False,
        **kwargs,
    ):
        item = cls.__itemtype_command__(
            label=label,
            width=width,
            height=height,
            show=show,
            autosize=autosize,
            no_resize=no_resize,
            no_title_bar=no_title_bar,
            no_move=no_move,
            min_size=min_size,
            **kwargs,
            no_focus_on_appearing=False,
            no_bring_to_front_on_focus=False,
            no_collapse=True,
            modal=False,
            popup=False,

        )
        self = cls(tag=item)

        if context_stack is not None:
            self.context_stack = context_stack
        if item_factory is not None:
            self.item_factory = item_factory

        handlers = self.handlers = items.item_handler_registry()
        items.add_item_resize_handler(callback=self._on_resize, parent=handlers)

        self.theme = self.get_default_theme()
        self.components = (handlers,)

        return self

    _cascade_arrow = '\u009b'

    @property
    def cascade_arrow(self, /) -> str:
        return self._cascade_arrow
    @cascade_arrow.setter
    def cascade_arrow(self, value: str, /) -> None:
        self._cascade_arrow = value

    # independent of "context_stack"
    __stack_lock = threading.RLock()
    __window_stack = collections.deque["ContextMenu[typing.Any, typing.Any]"]()

    def push(self) -> bool:
        with __class__.__stack_lock:
            stack = __class__.__window_stack
            if not stack or stack[0] != self:
                stack.appendleft(self)

        return super().push()

    def __enter__(self, /) -> typing.Self:
        self.push()
        return self

    def pop(self) -> None:   # pyright: ignore[reportIncompatibleMethodOverride]
        super().pop()
        with __class__.__stack_lock:
            stack = __class__.__window_stack
            if stack and stack[0] == self:
                stack.popleft()

                if not (stack and stack[0] != self):
                    return

                # if we've gotten this far, we're going to emulate a "parent" for
                # this window (the context menu atop the stack)
                parent = stack[0]
            else:
                return

        label = self.label
        assert label is not None
        label = f'{label.partition("##")[0]}{self.cascade_arrow}'

        # This item represents our menu in the parent menu. Our menu
        # will be displayed when the representative is hovered.
        item = self.item_factory(label=label, parent=parent, context_stack=self.context_stack)
        item._child_menu = self

    def __exit__(self, exc_type=None, value=None, traceback=None, /) -> None:
        self.pop()

    def _on_resize(self, handler: int | str = 0, /):
        configure_item = _dearpygui.configure_item
        get_item_state = _dearpygui.get_item_state

        for menu in self[:]:
            button, group = menu.children(1)

            rect_info = get_item_state(group)
            configure_item(
                button, pos=rect_info["pos"], height=rect_info["rect_size"][1]
            )

    @staticmethod
    def _fix_menu_position(menu_x_size: int, menu_y_size: int, x_pos: int, y_pos: int):
        "Adjust menu's new position depending on the menu's size."
        # XXX: The only difference between this positioning behavior
        # and `ContextMenuItem._cb_hovered`s behavior is that padding isn't
        # a factor here.
        viewport_config = _dearpygui.get_viewport_configuration(0)
        viewport_wt = viewport_config['client_width']  # type: ignore
        viewport_ht = viewport_config['client_height'] # type: ignore

        if menu_x_size > viewport_wt - x_pos:
            x_pos -= menu_x_size
        if menu_y_size > viewport_ht - y_pos:
            y_pos = max(0, y_pos - menu_y_size)

        return x_pos, y_pos

    def to_position(self: ContextMenu, /, x_pos: int, y_pos: int, *, content_aware: bool = True) -> None:
        """Close all context menus, then show this menu at the
        the given position. The menu will be brought into the
        foreground as the active window.

        Args:
            * x_pos: The menu's new horizontal position.

            * y_pos: The menu's new vertical position.

            * content_aware: If True (default), try to position the
            menu in a way that would avoid clipping its' content. If
            False, always positions the menu's top-left corner at
            the given coordinates.


        This is a no-op when the cursor is positioned over an open
        context menu.
        """
        stack = self.context_stack
        with stack:
            if not stack.hovered():
                stack.clear()

                if content_aware:
                    pos = self._fix_menu_position(*self.rect_size, x_pos, y_pos)  # type: ignore
                else:
                    pos = (x_pos, y_pos)
                stack.push(self, pos=pos)

    def to_cursor(self: ContextMenu, /) -> None:
        """Close all context menus, then show this menu at the
        cursor's position. The menu will be brought into the
        foreground as the active window.

        This is a no-op when the cursor is positioned over an open
        context menu.
        """
        stack = self.context_stack
        with stack:
            if not stack.hovered():
                stack.clear()
                stack.push(
                    self,
                    pos=self._fix_menu_position(
                        # BUG: Just like with `ContextMenuItem`s on-hover behavior, this
                        # menu's size will be 0 if it has never been rendered. The
                        # menu's content is at risk of getting clipped for its
                        # first viewing.
                        *self.rect_size, *_dearpygui.get_mouse_pos(local=False)
                    )
                )

    def as_root(self, /) -> typing.Self:
        self.context_stack.root_menu = self
        return self


@codegen.wrapped(ContextMenu.create)
def context_menu(*args, **kwargs):
    return ContextMenu.create(*args, **kwargs)

@codegen.wrapped(ContextMenu.create)
def add_context_menu(*args, **kwargs):
    return ContextMenu.create(*args, **kwargs)
