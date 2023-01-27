import code
import functools
import threading
import sys
import itertools
import contextlib
import types
from dearpygui import dearpygui

from . import appitems as ui, grid, px_utils, theme, px_items
from .px_items import ValueArrayItem, AutoParentItem
from .px_typing import ItemId, Any, Sequence, DPGCommand, T, P, Callable, Self, Iterator, Iterable, cast, NamedTuple, Protocol, TypeVar, Concatenate, DPGCallback, overload




def _bind_method(obj: Any, fn: Callable[Concatenate[Any, P], T]) -> Callable[P, T]:
    return types.MethodType(fn, obj)

def _null_item_processing(pxbuffer: 'pxStringBuffer', obj: T):
    return obj

def _null_value_processing(pxbuffer: 'pxStringBuffer', obj: T, value: Any):
    return value

class pxStringBuffer(ValueArrayItem[str], ui.mvValueRegistry):
    """A DearPyGui value registry that acts like high-level Python list of strings
    representing a multiline string, text file, etc. It is a necessary component
    for other tools in this module.

    Each value in the buffer corresponds to;
    * a `mvStringValue` child item
    * a value, assigned to the above `mvStringValue` item

    When a value is added to the buffer, a new child item is created to hold the
    value. Similarly, they are deleted along with the value. Callbacks can be
    assigned for item processing immediately following their creation and right before
    their destruction, while the management of the children is performed automatically.
        >>> arr = pxStringBuffer()
        >>> arr.value = "foo\nbar"
        >>> arr.value
        ["foo", "bar"]
        >>> arr[0] = None
        >>> arr.value
        ["None", "bar"]
        >>> arr[-1] = "FOO"
        >>> arr.value
        [None, "FOO"]
        >>> arr.value = ["foobar"]
        >>> arr.value
        ["foobar"]
    The buffer has access to `list` instance methods. In addition, it also has a `.write`
    method (forwarded to the `.append` method) allowing it to be used wherever a writable
    buffer is accepted.

    Callbacks can be passed when initializing the item to add additional processing
    to the underlying child items. The callbacks must accept two arguments; the first
    is the instance of `pxStringBuffer`, and the second is the new underlying child item.
    With this, it is possible to, for example; when a value is added to the buffer,
    create a text item and assign its' *source* to the value item.
        >>> with dpg.window() as wndw:
        ...     ...
        >>>
        >>> def add_line(buffer: pxStringBuffer, value_item: int | str) -> int | str | None:
        ...     dpg.add_text(parent=wndw, source=value_item)
        >>>
        >>>
        >>> arr = pxStringBuffer(["f", "o", "o", "bar"], post_newitem_callback=add_line)
    With some tweaks, this can be changed to do the above and also delete the text item
    when its' source is deleted.
        >>> def add_line(buffer: pxStringBuffer, value_item: int | str):
        ...     text_item = dpg.add_text(parent=wndw, source=value_item)
        ...     dpg.configure_item(value_item, user_data=text_item)
        >>>
        >>> def del_line(buffer: pxStringBuffer, value_item: int | str):
        ...     dpg.delete_item(dpg.get_item_configuration(value_item)["user_data"])
        >>>
        >>>
        >>> arr = pxStringBuffer(["f", "o", "o", "bar"], post_newitem_callback=add_line, pre_delitem_callback=del_line)
    What we're left with is a primitive log display. Updating or writing to the buffer
    will dynamically change the content of the display window. If `add_input_text` is
    used instead of `add_text`, we have an interactive file widget.
    """

    # TODO: add get/set value processing for children

    def __init__(
        self,
        default_value: Sequence[str] | str | None = None,
        max_size     : int                        =    0,
        *,
        item_factory         : DPGCommand[P, T]                      = dearpygui.add_string_value,
        post_newitem_callback: Callable[[Self, T], None] | None      = _null_item_processing,
        pre_delitem_callback : Callable[[Self, T], None] | None      = _null_item_processing,
        pre_value_callback   : Callable[[Self, T, Any], Any] | None  = _null_value_processing,
        **kwargs
    ):
        """Args:
            * default_value: Starting value for the item. Default is None.

            * max_size: The total number of values the buffer can hold, following
            FIFO when a value is added to the buffer. No limit if this value is 0.
            Default is 0.

            * item_factory: Callable that returns a DearPyGui item identifier. Default
            is `mvStringValue`.

            * post_newitem_callback: Callable that accepts this item and the new child value
            item as positional arguments. Default is None.

            * pre_delitem_callback: Callable that accepts this item and the dated child value
            item as positional arguments. Default is None.
        """
        super().__init__(**kwargs)
        self._max_size = max_size

        def _vitem_new(self, *_args: P.args, **_kwargs: P.kwargs) -> T:
            vitem = item_factory(*_args, parent=self, **_kwargs)
            post_newitem_callback(self, vitem)
            return vitem
        self._vitem_new = _bind_method(self, _vitem_new)

        def _vitem_del(self, item: T) -> None:
            pre_delitem_callback(self, item)
            dearpygui.delete_item(item)
        self._vitem_del = _bind_method(self, _vitem_del)

        def _vitem_set(self, item: T, value: Any) -> None:
            px_utils.set_value(item, pre_value_callback(self, item, value))
        self._vitem_set = _bind_method(self, _vitem_set)

        if default_value:
            self.set_value(default_value)

    def __iter__(self) -> Iterator[tuple[ItemId, str]]:
        val_items = self.children(1)
        yield from zip(val_items, px_utils.get_values(val_items))

    def __setitem__(self, index: int, value: str) -> None:
        target = self.children(1)[index]
        px_utils.set_value(target, value)

    @property
    def max_size(self) -> int:
        return self._max_size
    @max_size.setter
    def max_size(self, value: int) -> None:
        if value < 0:
            raise ValueError("`max_size` cannot be less than 0.")
        self._max_size = value

    def _fix_overflow(self):
        if self._max_size:
            for vitem in self.children(1)[self._max_size:]:
                self._vitem_del(vitem)

    def get_value(self) -> list[str]:
        return px_utils.get_values(self.children(1))

    def set_value(self, value: Sequence[Any]):
        children = self.children(1)
        # apply values
        for val, item in zip(value, itertools.chain(children, px_utils.item_generator(self._vitem_new))):
            self._vitem_set(item, val)
        # del leftover children if less new vals than old vals (no new children)
        for vitem in children[len(value):]:
            self._vitem_del(vitem)
        self._fix_overflow()

    def delete(self, children_only: bool = False, slot: int = 1) -> None:
        self.flush()
        super().delete(children_only, slot)

    # list methods
    def pop(self, index: int) -> tuple[ItemId, str]:
        """Remove a line from the buffer at *index*, returning both the value item identifier
        and value."""
        vitem = self.children(1)[index]
        value = px_utils.get_value(vitem)
        self._vitem_del(vitem)
        return value

    def remove(self, value: str) -> None:
        """At the first occurence of *value*, remove the line and value."""
        index = self.get_value().index(value)
        self._vitem_del(self.children(1)[index])

    def insert(self, index: int, value: Any) -> None:
        """Insert *value* at *index*, offsetting the position of trailing values by 1.
        >>> arr = pxStringBuffer(["one", "two", "three"])
        >>> arr.insert(1, "four")
        >>> arr
        ["one", "four", "two", "three"]
        """
        # Unlike most child items, value items don't have a "before" option.
        # The new item must be added first, then rearrange the children.
        children = self.children()
        vitem = self._vitem_new()
        self._vitem_set(vitem, value)
        children.insert(index, vitem)
        self.reorder(1, children)
        self._fix_overflow()

    def append(self, value: Any) -> None:
        self._vitem_set(self._vitem_new(), value)
        self._fix_overflow()

    ## NEW METHODS ##
    def flush(self, *, skip_processing: bool = False) -> None:
        """Clear the buffer of lines and values.

        Args:
            * skip_processing: If True, pre-delete item processing is skipped.
            Default is False.
        """
        if skip_processing:
            dearpygui.delete_item(self, children_only=True, slot=1)
        else:
            self.set_value(())

    def strip(self):
        """Remove all empty lines from the start and end of the buffer.
        >>> arr = pxStringBuffer(["", "", "foo", "bar", ""])
        >>> arr.strip()
        >>> arr
        ["foo", "bar"]
        """
        for item, value in self:
            if value:
                break
            self._vitem_del(item)
        for item, value in self[::-1]:
            if value:
                break
            self._vitem_del(item)

    def join(self, s: str = '') -> str:
        """Return the result of `s.join(self.get_value())`.
        >>> arr = pxStringBuffer(['The', 'cake', '', 'is a', 'lie.'])
        >>> arr.join()
        'Thecakeis alie.'
        >>> arr.join(".")
        'The.cake..is a.lie.'
        """
        return s.join(self.get_value())

    def write(self, s: str) -> None:
        """Append to the buffer."""
        self.append(s)




class pxConsoleWindow(ui.mvChildWindow):
    """A writable window for displaying text. Changes to the underlying buffer
    update the display. The console window share the freedoms, constraints, and
    limitations with `mvChildWindow` items.

    Any text passed to the item's `.write` method is displayed as a new entry in
    the window. When used as a context manager, all writes to stdout and/or stderr
    are redirected to this item. This behavior can be changed by setting the
    `.ctx_redirect_stdout` and `.ctx_redirect_stderr` class/instance attributes
    to True or False.

    If the `.auto_scroll` attribute is True, the scroll position of the console
    will adjust to view the new content when writing to the window.
    """

    ctx_redirect_stdout: bool = True
    ctx_redirect_stderr: bool = False

    auto_scroll: bool = True

    def __init__(self, max_size: int = 100, *, pxbuffer_type: type[pxStringBuffer] = pxStringBuffer, text_factory: DPGCommand[..., ItemId] = dearpygui.add_text, **kwargs):
        super().__init__(**kwargs)
        self.text_factory = text_factory
        self.pxbuffer     = pxbuffer_type(max_size=max_size, post_newitem_callback=self.cb_on_new_entry, pre_delitem_callback=self.cb_on_del_entry, pre_value_callback=self.cb_on_value)

        self.__ctx_counter = 0
        self.__ctx_stdout  = contextlib.redirect_stdout(self)
        self.__ctx_stderr  = contextlib.redirect_stderr(self)

    __ctx_no_redirect = contextlib.nullcontext()
    __stdout_redirect = __ctx_no_redirect
    __stderr_redirect = __ctx_no_redirect

    def __enter__(self) -> Self:
        # when chaining/nesting `with` statements, redirect only once
        if self.__ctx_counter:
            self.__ctx_counter += 1
            return self
        self.__ctx_counter += 1
        if self.ctx_redirect_stdout:
            self.__stdout_redirect = self.__ctx_stdout
            self.__stdout_redirect.__enter__()
        if self.ctx_redirect_stderr:
            self.__stderr_redirect = self.__ctx_stderr
            self.__stderr_redirect.__enter__()
        return super().__enter__()

    def __exit__(self, *args, **kwargs):
        if self.__ctx_counter > 1:
            self.__ctx_counter -= 1
            return
        super().__exit__(*args, **kwargs)
        self.__stdout_redirect.__exit__(*args)
        self.__stdout_redirect = self.__ctx_no_redirect
        self.__stderr_redirect.__exit__(*args)
        self.__stderr_redirect = self.__ctx_no_redirect
        self.__ctx_counter -= 1

    def write(self, s: str) -> None:
        self.pxbuffer.write(s)

    def cb_on_resize(self, sender: ItemId | None = None, app_data: Any = None, user_data: Any = None) -> None:
        """Updates the `wrap` setting of all child text items to match the width of
        the window. Best used as a resize callback for a parenting `mvWindowAppItem`
        item."""
        width = self.content_region_avail[0]
        for child in self.children(1):
            try:
                px_utils.set_config(child, wrap=width)
            except SystemError:
                pass

    def cb_on_new_entry(self, buffer_item: pxStringBuffer, val_item: ItemId):
        txt_item = self.text_factory(parent=self, source=val_item, wrap=self.content_region_avail[0])
        # Store the text item ref in the value item so a user
        # can grab it when extending these callbacks.
        px_utils.set_config(val_item, user_data=txt_item)
        if self.auto_scroll:
            self.y_scroll_pos = -1

    def cb_on_del_entry(self, buffer_item: pxStringBuffer, val_item: ItemId):
        dearpygui.delete_item(px_utils.get_config(val_item)["user_data"])

    def cb_on_value(self, buffer_item: pxStringBuffer, val_item: ItemId, value: str) -> str:
        return value




class pxInteractivePython(code.InteractiveConsole, AutoParentItem, pxConsoleWindow, auto_parent=dearpygui.add_window):
    PROMPT_1 = ">>>"
    PROMPT_2 = "..."

    banner = "Python {} on {}\n{}\n".format(
        sys.version,
        sys.platform,
        'Type "help", "copyright", "credits" or "license" for more information.',
    )

    stdout_txt_color = (255, 255, 255, 255)
    stderr_txt_color = (255,  20,  20, 255)

    ctx_redirect_stderr = True

    def __init__(self, locals: dict[str] = None, max_size: int = 100, banner: str = None, **kwargs):
        # The classes in `code` do not invoke `super().__init__`, so this needs to be weird.
        super().__init__(locals)
        AutoParentItem.__init__(
            self,
            max_size,
            no_scrollbar=True,
            text_factory=dearpygui.add_text,
            **kwargs,
        )
        self._init_input()
        self._init_grid()
        self._init_themes()
        self._init_handlers()

        self.write(banner or self.banner)

    def _init_input(self):
        with ui.mvChildWindow(no_scrollbar=True, parent=self.parent) as self._input_wndw:
            with ui.mvGroup(horizontal=True, horizontal_spacing=0):
                self.prompt = ui.mvText(self.PROMPT_1)
                self.input  = ui.mvInputText(on_enter=True, callback=self.cb_on_enter)

    def _init_grid(self):
        self._parent_grid = grid.Grid(2, 1, padding=(8, 8), parent=self.parent)
        # Hacky workaround to deal with window titlebars.
        if px_utils.get_info(self.parent)["type"] == "mvAppItemType::mvWindowAppItem":
            self._parent_grid.rows = 3
            self._parent_grid.push(self, 1, 0, anchor="c")
            self._parent_grid.rows[0].size = 18
        else:
            self._parent_grid.push(self, 0, 0, anchor="c")
        self._parent_grid.push(self._input_wndw, -1, 0, anchor="c")
        self._reset_input_height()

    def _init_themes(self):
        with theme.pxTheme() as t:
            t.style.WindowPadding(8, 0)
            t.color.FrameBg(0, 0, 0, 0)
            t.color.ChildBg(25, 25, 25)
        self.set_theme(t)

        with theme.pxTheme() as t:
            t.style.WindowPadding(8, 0)
            t.color.FrameBg(0, 0, 0, 0)
        self._input_wndw.set_theme(t)

        with theme.pxTheme() as self._stdout_theme:
            self._stdout_theme.color.Text(self.stdout_txt_color)
            self._stdout_theme.color.FrameBg(0, 0, 0, 0)

        with theme.pxTheme() as self._stderr_theme:
            self._stderr_theme.color.Text(self.stderr_txt_color)
            self._stderr_theme.color.FrameBg(0, 0, 0, 0)

    def _init_handlers(self):
        p_info = px_utils.get_info(self.parent)
        if p_info["type"] != "mvAppItemType::mvWindowAppItem":
            return
        hreg = p_info["handlers"]
        if not hreg:
            hreg = ui.mvItemHandlerRegistry()
        ui.mvResizeHandler(callback=self.cb_on_resize, parent=hreg)
        dearpygui.bind_item_handler_registry(self.parent, hreg)

    def _reset_input_height(self):  # XXX see `.cb_resize` comment
        self.__input_adj_ht = 10
        self._parent_grid.rows[-1].size = 10

    def interact(self, *args, **kwargs): ...  # calling it would hang the thread

    def move(self, parent: ItemId = 0, **kwargs):
        if not parent:
            return
        super().move(parent=parent)
        self._input_wndw.move(parent=parent)
        self._init_grid()
        self._init_handlers()

    def write(self, s: str):
        with self:
            self.pxbuffer.write(s)

    def set_handlers(self, handler_registry: ItemId = 0):
        # share handlers w/input window
        super().set_handlers(handler_registry)
        self._input_wndw.set_handlers(handler_registry)

    def set_font(self, font: ItemId = 0):
        # share font w/input window
        super().set_font(font)
        self._input_wndw.set_font(font)
        self._reset_input_height()
        self.cb_on_resize()

    def cb_on_value(self, buffer_item: pxStringBuffer, val_item: ItemId, value: str) -> str:
        txt_item = px_utils.get_config(val_item)["user_data"]
        if value.startswith("Traceback ("):
            txt_theme = self._stderr_theme
            value += "\n"
        else:
            txt_theme = self._stdout_theme
        dearpygui.bind_item_theme(txt_item, txt_theme)
        return value

    __addtl_input: int

    def cb_on_enter(self, sender: ItemId, app_data: str = "", user_data: Any = None):
        with self:
            self.__addtl_input = self.push(app_data)
        self.prompt.value = self.PROMPT_2 if self.__addtl_input else self.PROMPT_1
        self.input.value  = ""
        self.input.focus()

    __input_adj_ht: int

    def cb_on_resize(self, sender: ItemId | None = None, app_data: Any = None, user_data: Any = None) -> None:
        super().cb_on_resize(sender, app_data, user_data)
        # input window
        self.input.configure(
            width=self.content_region_avail[0] - (dearpygui.get_text_size(self.prompt.value)or (0,))[0]
        )
        # If the input window is scrollable, it's not large enough for the
        # current font. Adjust the size until it is no longer scrollable.
        # BUG: replacing the conditional with `while` breaks the grid.
        if self._input_wndw.y_scroll_max:
            self.__input_adj_ht += 5
            self._parent_grid.rows[-1].size = self.__input_adj_ht
        # other
        self._parent_grid()



class ItemView(NamedTuple):
    button: ui.mvButton
    window: ui.mvChildWindow


class _TabBar(ui.mvChildWindow):
    focused_theme = ...
    standby_theme = ...

    def __init__(self, *args, border: bool = False, **kwargs):
        super().__init__(*args, border=border, **kwargs)
        self.views: list[ItemView] = []
        self._grid = grid.Grid()

    def new_view(self, label: str):
        ...

    def del_view(self, *, index: int = None, label: str = None):
        ...

    def get_view(self, *, index: int = None, label: str = None):
        ...

    def set_view(self, *, index: int = None, label: str = None):
        ...

    def cb_resize(self, sender: ItemId | None = None, app_data: Any = None, user_data: Any = None) -> None:
        ...




class pxItemRegView(ui.mvChildWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tabbar


class pxItemRegView(AutoParentItem, ui.mvChildWindow, auto_parent=dearpygui.add_window):
    def __init__(self, *args, border: bool = False, **kwargs):
        super().__init__(*args, border=border, **kwargs)
        self.itemreg_view = ...
        self.details_view = ...

        self._init_main_views()

    def _init_main_views(self):
        _table = ui.mvTable(borders_innerV=True, resizable=True, parent=self, header_row=False)
        ui.mvTableColumn(parent=_table)
        ui.mvTableColumn(parent=_table)
        _row = ui.mvTableRow(parent=_table)
        self.itemreg_view = ui.mvChildWindow(parent=_row)
        self.details_view = ui.mvChildWindow(parent=_row, border=False)

    def _init_itemreg_view(self):
        with self.itemreg_view: ...


    def _init_details_views(self):
        ...