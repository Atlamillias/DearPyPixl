"""Items for emulating consoles and other streams."""
import sys   # type: ignore
import types
import codeop
import traceback
import functools
import threading
import itertools  # type: ignore
import contextlib
import types
from dearpygui import dearpygui
from ._typing import Item, Color
from . import items, color, style
from . import api, _interface, _tools
from .api import Item as ItemAPI
from ._typing import (
    Item,
    Any,
    Sequence,
    ItemCommand,
    Callable,
    Self,
    Literal,
    SupportsIndex,
    Generator,
    TypeVar,
    ParamSpec,
    Method,
    override,
)


_T = TypeVar("_T")
_P = ParamSpec("_P")





def _null_item_processing(self: 'FileStream', obj: _T) -> _T:
    return obj

def _null_value_processing(self: 'FileStream', obj: _T, value: Any) -> _T:
    return value

def _item_generator(item_factory: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Generator[_T, None, None]:
    while True:
        yield item_factory(*args, **kwargs)


class FileStream(_interface.SupportsValueArray[str], items.mvValueRegistry):
    """A value registry that acts like pseudo file stream or buffer. It
    represents itself as a living multiline string split at newlines.
        >>> f = FileStream()
        >>> f.value = "foo\\nbar"
        >>> f.value
        ['f', 'o', 'o', '\\n', 'b', 'a', 'r']
        >>> f[0] = 'b'
        >>> f.value
        ['b', 'o', 'o', '\\n', 'b', 'a', 'r']
        >>> f[-1] = "FOO"
        >>> f.value
        ['b', 'o', 'o', '\\n', 'b', 'a', 'FOO']
        >>> f.value = ["foobar"]
        >>> f.value
        ["foobar"]

    Writing to the stream appends the value written:
        >>> f.write("helloworld")
        >>> f.value
        ['foobar', 'helloworld']

    The stream will always use the string representation of any object used
    as a value or values. When setting its' value as a whole:
        >>> f.value = ['a', 'b', None, 'd']
        >>> f.value
        ['a', 'b', 'None', 'd']

    Setting part of the value at a specific line number/index:
        >>> f[1] = None
        >>> f.value
        ['a', 'None', 'None', 'd']

    The string representation of the stream is the assembled value as if
    joined by newlines:
        >>> str(f)
        'a\\nNone\\nNone\\nd\\n'


    Individual 'mvStringValue' items are created to store each value added to
    the registry. These items can be used as a source for other items. Iterating
    through the stream will yield the identifier of the 'mvStringValue' and its
    value. Alternatively, you can get the identifier of a value item at a specific
    line number by indexing the stream's children (slot 1).

    The stream accepts three optional callbacks during initialization. This
    makes it easier to interface with the stream when it performs notable
    operations. For example, when making a primitive file display:
        >>> with dpg.window() as file_window: ...
        >>>
        >>> def add_line(buffer: FileStream, value_item: int | str):
        ...     # Add a new line to the display when a value is added to
        ...     # the stream. If the value is updated at this line, the
        ...     # text will display accordingly.
        ...     # Also, store the text item id within the value item for
        ...     # `del_line`.
        ...     text_item = dpg.add_text(parent=file_window, source=value_item)
        >>>
        >>> def del_line(buffer: FileStream, value_item: int | str):
        ...     # Destroy the associated text item when the value item is
        ...     # deleted.
        ...     dpg.delete_item(dpg.get_item_configuration(value_item)["user_data"])
        >>>
        >>> f = FileStream(
        ...     ["f", "o", "o", "bar"],
        ...     add_item_callback=add_line,
        ...     del_item_callback=del_line,
        ... )
    In the above example, writing to `f` will display content written in
    `file_window`. There's a lot of room for creativity here; you can use `f`
    as a logging handler for a log display. Want a more interactive display?
    Pass `dpg.add_input_text` as the value to the *text_factory* keyword argument
    when initializing the stream.
    """

    def __init__(
        self,
        default_value: Sequence[str] | str = '',
        max_len      : int | None          = None,
        *,
        add_item_callback : Callable[[Self, _T], Any] | None       = None,
        del_item_callback : Callable[[Self, _T], Any] | None       = None,
        set_value_callback: Callable[[Self, _T, Any], Any] | None  = None,
        item_factory      : ItemCommand[_P, Item]                  = dearpygui.add_string_value,
        **kwargs
    ):
        """Args:
            * default_value: Starting value for the item.

            * max_len: The total number of lines the buffer will store. Once at
            capacity, lines are deleted in FIFO order. If unspecified or is None
            (default), the buffer can grow to an arbitrary length.

            * item_factory: Callable that returns a DearPyGui item identifier.

            * add_item_callback: Callable that accepts this item and the new child value
            item as positional arguments. It will be called immediately following the
            value item's creation.

            * del_item_callback: Callable that accepts this item and the child value item
            scheduled for destruction as item as positional arguments. It will be called
            before destroying the value item.

            * set_value_callback: Callable that accepts this item, the child value item
            who's value will be set, and the value to set, while returning the value to
            set. It will be called before updating the value of a value item.

        """
        super().__init__(**kwargs)
        self._max_len = max_len

        self._add_value_item = Method(
            _tools.create_function(
                '_new_value_item',
                ('self', "*args", "**kwargs"),
                (
                    'kwargs["parent"] = self',
                    'vitem = item_factory(*args, **kwargs)',
                    'callback(self, vitem)',
                    'return vitem',
                ),
                Item,
                locals={
                    'item_factory': item_factory,
                    'callback': add_item_callback or _null_item_processing,
                }
            ),
            self,
        )
        self._del_value_item = Method(
            _tools.create_function(
                '_del_value_item',
                ('self', 'item: int | str', '/'),
                ('callback(self, item)', 'delete_item(item)'),
                Item,
                locals={
                    'callback': del_item_callback or _null_item_processing,
                    'delete_item': api.Registry.delete_item
                }
            ),
            self,
        )
        self._set_value_item = Method(
            _tools.create_function(
                '_set_value_item',
                ('self', 'item: int | str', 'value: str', '/'),
                ('set_value(item, callback(self, item, value))',),
                locals={
                    'set_value': api.Item.set_value,
                    'callback': set_value_callback or _null_value_processing,
                }
            ),
            self,
        )

        self._generate_items = functools.partial(_item_generator, self._add_value_item)

        if default_value:
            self.set_value(default_value)

    def __str__(self):
        return '\n'.join(self.get_value())

    def __iter__(self):
        vitems = self.children(1)
        yield from zip(vitems, ItemAPI.get_values(vitems))

    def __setitem__(self, index: SupportsIndex, value: Any):
        ItemAPI.set_value(self.children(1)[index], value)

    def _add_value_item(self, *args, **kwargs) -> Item: ...

    def _del_value_item(self, item: Item, /) -> None: ...

    def _set_value_item(self, item: Item, value: str, /) -> None: ...

    def _generate_items(self, *args, **kwargs) -> Generator[Item, None, None]: ...

    def _truncate_lines(self):
        if self._max_len is not None:
            for vitem in self.children(1)[self._max_len:]:
                self._del_value_item(vitem)

    @property
    def max_len(self) -> int | None:
        return self._max_len
    @max_len.setter
    def max_len(self, value: int | None):
        if value is not None:
            value = int(value)
            if value < 0:
                raise ValueError("`max_len` cannot be less than zero.")
        self._max_len = value

    @override
    def get_value(self) -> list[str]:
        return ItemAPI.get_values(self.children(1))

    @override
    def set_value(self, value: Sequence[Any]):
        vitems = self.children(1)
        for v, item in zip(value, itertools.chain(vitems, self._generate_items())):
            self._set_value_item(item, v)
        # delete leftover children if any
        for item in vitems[len(value):]:
            self._del_value_item(item)
        self._truncate_lines()

    @override
    def delete(self, *, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        self.clear()
        super().delete(children_only=children_only, slot=slot)

    # list-like methods

    @override
    def pop(self, index: SupportsIndex) -> tuple[Item, str]:
        """Remove a line from the buffer at *index*, returning both the value
        item identifier and value."""
        vitem = self.children(1)[index]
        value = ItemAPI.get_value(vitem)
        self._del_value_item(vitem)
        return value

    @override
    def remove(self, value: str) -> None:
        """At the first occurence of *value*, remove the line and value."""
        index = self.get_value().index(value)
        self._del_value_item(self.children(1)[index])

    @override
    def insert(self, index: SupportsIndex, value: Any) -> None:
        """Insert *value* at *index*, offsetting the position of trailing values by 1.
            >>> f = FileStream(["one", "two", "three"])
            >>> f.insert(1, "four")
            >>> arr
            ["one", "four", "two", "three"]
        """
        # Unlike most child items, value items don't have a "before" option.
        # The new item must be added first, then rearrange the children.
        vitems = self.children(1)
        vitem  = self._add_value_item()
        self._set_value_item(vitem, value)
        vitems.insert(index, vitem)
        self.reorder(1, vitems)
        self._truncate_lines()

    @override
    def extend(self, value: Sequence[Any]):
        v = self.get_value()
        v.extend(value)
        self.set_value(v)

    @override
    def append(self, value: Any):
        self._set_value_item(self._add_value_item(), value)
        self._truncate_lines()

    def clear(self, *, use_del_item_callback: bool = False):
        if not use_del_item_callback:
            ItemAPI.delete(self, children_only=True, slot=1)
        else:
            self.set_value('')

    # misc

    def strip(self):
        """Remove all empty lines from the start and end of the buffer.
            >>> f = FileStream(["", "", "foo", "bar", ""])
            >>> f.strip()
            >>> arr
            ["foo", "bar"]
        """
        for item, value in self:
            if value:
                break
            self._del_value_item(item)
        for item, value in self[::-1]:
            if value:
                break
            self._del_value_item(item)

    def write(self, s: str):
        self.append(s)




class ConsoleWindow(items.mvChildWindow):
    """A child window for displaying text logs. Writing to the item updates
    the display with the written text.

    The window does not push to and pop itself from the container stack when
    used as a context manager. Instead, any write to stdout and/or stderr
    will be written to the window instead. This behavior can be altered by
    setting the boolean `.ctx_redirect_stdout` and `.ctx_redirect_stderr`
    attributes on the class or instance.

    Note that when this interface is initialized, a resize handler is
    added to the handler registry of the root parent. The handler registry
    will be created if necessary.

    """
    ctx_redirect_stdout: bool = True
    ctx_redirect_stderr: bool = False

    def __init__(
        self,
        max_len: int | None = None,
        *,
        redirect_stdout: bool | None        = None,
        redirect_stderr: bool | None        = None,
        auto_scroll    : bool               = True,
        wrap_text      : bool               = True,
        text_factory   : ItemCommand[_P, Item] = dearpygui.add_text,
        buffer_factory : type[FileStream] = FileStream,
        **kwargs,
    ):
        """Args:
            * max_len: The total number of records to display before deleting
            older records in FIFO order.

            * redirect_stdout: If True (class-level default), all writes to stdout
            will instead write to this window when it is used as a context manager.
            If None, the `.ctx_redirect_stdout` attribute will not be set at the
            instance-level.

            * redirect_stderr: If True, all writes to stderr will instead write to
            this window when it is used as a context manager. If None, the
            `.ctx_redirect_stderr` attribute will not be set at the instance-level.

            * auto_scroll: If True (default), the scroll position is set to view the newest
            record when it is added.

            * wrap_text: If True, displayed text will be wrapped when the root
            window parent item is resized. Ignored when *text_factory* does produce
            'mvText' items.

            * text_factory: Creates the text items that the window displays. Supports
            callables that create 'mvText' and 'mvInputText' items.

        """
        super().__init__(**kwargs)
        self.wrap_text    = wrap_text
        self.text_factory = text_factory
        self.auto_scroll  = auto_scroll
        self.value_buffer = buffer_factory(
            max_len=max_len,
            add_item_callback=self._cb_add_record,
            del_item_callback=self._cb_del_record,
            set_value_callback=self._cb_set_record,
        )
        self.__ctx_lock    = threading.RLock()
        self.__ctx_counter = 0
        self.__ctx_stdout  = contextlib.redirect_stdout(self)  # type: ignore
        self.__ctx_stderr  = contextlib.redirect_stderr(self)  # type: ignore
        if redirect_stdout is not None:
            self.ctx_redirect_stdout = redirect_stdout
        if redirect_stderr is not None:
            self.ctx_redirect_stderr = redirect_stderr
        self._attach_resize_handler()


    # ResizeHandler management

    _resize_handler_uuid = 0

    def _destroy_resize_handler(self):
        try:
            ItemAPI.delete(self._resize_handler_uuid)
        except SystemError:
            pass

    def _attach_resize_handler(self):
        # XXX: this needs to be called whenever the console is re-parented!
        if self._resize_handler_uuid:
            self._destroy_resize_handler()
        else:
            # this uuid is recycled and should not change for this object
            self._resize_handler_uuid = api.Registry.create_uuid()
        root_parent   = self.root_parent
        root_handlers = ItemAPI.information(root_parent)['handlers']
        if root_handlers is None:
            root_handlers = items.ItemHandlerRegistry(label='')
            ItemAPI.set_handlers(root_parent, root_handlers)
        items.ResizeHandler(
            label='',
            parent=root_handlers,
            callback=self._cb_resize,
            tag=self._resize_handler_uuid,
        )

    # buffer callbacks

    def _cb_add_record(self, b: FileStream, item: Item):
        text_item = self.text_factory(
            parent=self,
            source=item,
        )
        if self.wrap_text and 'wrap' in ItemAPI.configuration(text_item):
            ItemAPI.configure(text_item, wrap=self.content_region_avail[0])   # type: ignore
        # The 'del_item' callback will receive the source value item but
        # not the text item. Keep a reference to the text item in the value
        # item so it can be easily deleted later.
        ItemAPI.configure(item, user_data=text_item)
        if self.auto_scroll:
            self.y_scroll_pos = -1.0

    def _cb_del_record(self, b: FileStream, item: Item):
        ItemAPI.delete(ItemAPI.configuration(item)['user_data'])

    def _cb_set_record(self, b: FileStream, item: Item, value: str)  -> str:
        # XXX: This is unchanged from the default behavior and can be overridden
        return value

    def _cb_resize(self, sender: Item, *args):
        if self.wrap_text:
            width = self.content_region_avail[0]   # type: ignore
            configuraton = ItemAPI.configuration
            for text in self.children(1):
                if 'wrap' in configuraton(text):
                    try:
                        ItemAPI.configure(text, wrap=width)
                    except SystemError:
                        pass

    # context usage

    __ctx_no_redirect = contextlib.nullcontext()
    __stdout_redirect = __ctx_no_redirect
    __stderr_redirect = __ctx_no_redirect

    def __enter__(self) -> Self:
        self.redirect()
        return self

    def __exit__(self, *args):
        self.restore(*args)

    def redirect(self):
        with self.__ctx_lock:
            if self.__ctx_counter > 1:
                self.__ctx_counter += 1
                return
            self.__ctx_counter = 1
            if self.ctx_redirect_stdout:
                self.__stdout_redirect = self.__ctx_stdout
                self.__stdout_redirect.__enter__()
            if self.ctx_redirect_stderr:
                self.__stderr_redirect = self.__ctx_stderr
                self.__stderr_redirect.__enter__()

    def restore(self, *args):
        with self.__ctx_lock:
            if self.__ctx_counter > 1:
                self.__ctx_counter -= 1
                return
            self.__stdout_redirect.__exit__(*args)
            self.__stdout_redirect = self.__ctx_no_redirect
            self.__stderr_redirect.__exit__(*args)
            self.__stderr_redirect = self.__ctx_no_redirect
            self.__ctx_counter = 0

    # the rest

    @property
    def max_len(self):
        return self.value_buffer.max_len
    @max_len.setter
    def max_len(self, value: Any):
        self.value_buffer.max_len = value

    @override
    def move(self, *, parent: Item = 0, before: Item = 0) -> None:
        super().move(parent=parent, before=before)
        if parent:
            self._attach_resize_handler()

    @override
    def unstage(self):
        super().unstage()
        self._attach_resize_handler()

    @override
    def delete(self, *, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        if not children_only:
            self._destroy_resize_handler()
        self.value_buffer.delete(children_only=children_only, slot=slot)
        super().delete(children_only=children_only, slot=slot)

    @override
    def destroy(self):
        try: self._destroy_resize_handler()
        except: pass
        try: self.value_buffer.destroy()
        except: pass
        super().destroy()

    def clear(self, **kwargs):
        self.value_buffer.clear(use_del_item_callback=True)

    def write(self, s: str):
        return self.value_buffer.write(s)



class PythonConsole(ConsoleWindow):
    """A console window for displaying the output of executed Python
    code.

    See the `.push` and `.compile` methods for more information.
    """
    def __init__(
        self,
        locals : dict[str, Any] | None = None,
        max_len: int | None            = None,
        **kwargs
    ):
        super().__init__(
            max_len,
            redirect_stderr=True,
            redirect_stdout=True,
            auto_scroll=True,
            wrap_text=True,
            text_factory=dearpygui.add_text,
            **kwargs
        )
        self._compiler = codeop.CommandCompiler()

        self.locals = locals if locals is not None else {
            "__name__": "__console__",
            "__doc__" : None,
        }

        with items.mvTheme(label='') as self.theme:
            with items.mvThemeComponent(int(items.mvChildWindow), label=''):
                self.console_color = color.ChildBg(25, 25, 25)
                style.WindowPadding(8, 0)

        with items.mvTheme() as self._stdout_theme:
            with items.mvThemeComponent(label=''):
                self.stdout_color = color.Text(255, 255, 255)
                color.FrameBg(0, 0, 0, 0)

        with items.mvTheme() as self._stderr_theme:
            with items.mvThemeComponent(label=''):
                self.stderr_color = color.Text(255, 20, 20)
                color.FrameBg(0, 0, 0, 0)

    def _cb_set_record(self, b: FileStream, item: Item, value: str) -> str:
        # set the theme of the text
        text_item = ItemAPI.configuration(item)['user_data']
        if value.startswith("Traceback (") or '\nSyntaxError:' in value or '\nIndentationError:' in value:
            theme = self._stderr_theme
        else:
            theme = self._stdout_theme
        ItemAPI.set_theme(text_item, theme)
        return value

    @property
    def filename(self):
        return self.locals.get('__name__', '<console>')

    def _write_syntax_err(self):
        """Format and write the most recent syntax error set and
        write it to the console.
        """
        exc_tp, exc_val, tb  = sys.exc_info()
        sys.last_type        = exc_tp
        sys.last_value       = exc_val
        sys.last_traceback   = tb

        # SyntaxErrors don't actually include the traceback in
        # stderr. However, the traceback lines are formatted
        # the same regardless. Remove the indent(s).
        lines = traceback.format_exception_only(exc_tp, exc_val)
        indent = ""
        for char in lines[0]:
            if not char.isspace():
                break
            indent += char
        for idx, ln in enumerate(lines):
            lines[idx] = ln.removeprefix(indent)

        self.value_buffer.write(''.join(lines))

    def _write_traceback(self):
        """Format the most recent exception set and write it to the
        console.
        """
        sys.last_type, sys.last_value, last_tb = ei = sys.exc_info()
        sys.last_traceback = last_tb
        try:
            # use the next traceback because the first is from *our* code
            lines = traceback.format_exception(ei[0], ei[1], last_tb.tb_next)  # type: ignore
            self.value_buffer.write(''.join(lines))
        finally:
            last_tb = ei = None

    def compile(self, s: str, filename: str = '', mode: str = 'single'):
        """Compile a string as source code.

        The return of this method varies based on the outcome of the compilation:
            * CodeType: The code compiled sucessfully (as the returned object).

            * False: The code was compiled successfully but could not be executed
            because it is incomplete.

            * None: `SyntaxError` was thrown while compiling the code.

        All exceptions that occur from compiling the code are displayed in the
        console and are not raised.
        """
        filename = filename or self.filename
        try:
            code = self._compiler(s, filename, mode)
        except (OverflowError, SyntaxError, ValueError):
            self._write_syntax_err()
            return None   # invalid source code
        if code is None:  # incomplete source code
            return False
        return code

    def push(self, c: types.CodeType | str):
        """Compile a string as source code, execute it, and display the output
        in the console.

        The return of this method varies based on the outcome of the compilation:
            * True: The code compiled sucessfully or was not needed, and was
            executed.

            * False: The code was compiled successfully but could not be executed
            because it is incomplete.

            * None: `SyntaxError` was thrown while compiling the code.

        All exceptions that occur from compiling or executing the code are
        displayed in the console and are not raised.

        Accepts a string or `CodeType` object as an argument. This method will
        execute a `CodeType` object immediately and will always return True.
        """
        if isinstance(c, types.CodeType):
            code = c
        else:
            code = self.compile(c, self.filename)
            if not code:
                return code
        with self:
            try:
                exec(code, self.locals)
            except:
                self._write_traceback()
        return True




@_interface.auto_parent(functools.partial(  # type: ignore
    dearpygui.add_window,
    width=600,
    height=400,
    no_scrollbar=True
))
class InteractivePython(items.mvChildWindow):
    """Execute Python code from an emulated interactive session.

    This item will create a root parent window for itself if a parent is
    unspecified or unavailable.

    When this interface is initialized, a resize handler is added to the
    handler registry of the root parent. The handler registry will be
    created if necessary.
    """

    _PROMPT_1 = ">>>"
    _PROMPT_2 = "..."

    def __init__(
        self,
        locals: dict[str, Any] | None = None,
        echo  : bool                  = True,
        **kwargs
    ):
        """Args:
            * locals: Namespace used for lookups.

            * echo: If True, text from the input will be displayed in the
            console when the 'enter' key is pressed.
        """
        if not 'label' in kwargs:
            kwargs['label'] = f'[{type(self).__qualname__}]'
        super().__init__(**kwargs)
        if not self.parent.label:
            self.parent.label = f'[{type(self).__qualname__}]'
            
        self._input_pending = []

        self.echo = echo

        with items.mvTheme() as self.theme:
            with items.mvThemeComponent():
                style.WindowPadding(0, 0)
                style.FramePadding(4, 4)
                style.ItemSpacing(8, 0)
                color.FrameBg(0, 0, 0, 0)

        with items.mvTheme() as self._echo_theme:
            with items.mvThemeComponent():
                self.echo_color = color.Text(50, 210, 230, 150)  # cyan

        with self:
            # The initial height needs to be very small so the input parent can
            # have room to stretch its' legs for the initial render. Otherwise,
            # the console will squish it and its y_scroll_max will be 0.
            with PythonConsole(locals=locals, height=1) as self.console:
                ...
            with items.mvChildWindow(no_scrollbar=True, border=False, height=24) as self._input_parent:
                self._input_parent.theme = self.theme
                with items.mvGroup(horizontal=True, horizontal_spacing=0):
                    self._input_prompt = items.mvText(self._PROMPT_1, indent=8)  # indent == WindowPadding[0]
                    self.input = items.mvInputText(
                        on_enter=True,
                        callback=self._cb_enter,
                        hint="(enter a partial or complete Python expression/statement)"
                    )

        self._attach_resize_handler()

        self.console.write("Python {} on {}\n{}\n".format(
            sys.version,
            sys.platform,
            'Type "help", "copyright", "credits" or "license" for more information.\n',
        ))

    def _cb_enter(self, sender: Item, app_data: str, *args):
        self._input_pending.append(app_data)
        self.input.value = ''
        if self.echo and app_data:
            self.console.write(f"{self._input_prompt.value} {app_data}")
            ItemAPI.set_theme(self.console.children(1)[-1], self._echo_theme)
        code = self.console.compile('\n'.join(self._input_pending))
        if code:
            self.console.push(code)
            self._input_prompt.value = self._PROMPT_1
            self._input_pending.clear()
        elif code is None:  # SyntaxError, etc.
            self._input_prompt.value = self._PROMPT_1
            self._input_pending.clear()
        else:  # pending
            self._input_prompt.value = self._PROMPT_2
        self.input.focus()

    def _cb_resize(self):
        # XXX: ALL of the input window must be "visible" for the first
        # render so its' y_scroll_max gets set before `_cb_resize` reads
        # it. If it's only viewable off-screen (in the parent's scroll
        # area, etc) y_scroll_max will be initially set to 0. This can
        # be worked around by setting the initial height of the console
        # to *smol-er* to keep it from being a fatass.
        text_wt, text_ht = self.text_size(
            self._PROMPT_1,
            font=self.font or api.Application.get_font()  # type: ignore
        )
        wt_avail, ht_avail = self.content_region_avail  # type: ignore
        # Resize the input so that it's just tall enough for the
        # rendered font. It could be larger or smaller than before;
        # set the height to *smol* and wait a frame (at least), then
        # set the height based off the upd. max scroll position.
        self._input_parent.height = 5
        dearpygui.split_frame(delay=16)
        input_ht = int(self._input_parent.y_scroll_max) + 8   # account for `FramePadding[1]`
        self._input_parent.height = input_ht

        self.input.configure(width=wt_avail - text_wt - 8)  # account for `WindowPadding[0]`

        self.console.height = ht_avail - input_ht

    _resize_handler_uuid = 0

    def _destroy_resize_handler(self):
        try:
            ItemAPI.delete(self._resize_handler_uuid)
        except SystemError:
            pass

    def _attach_resize_handler(self):
        # XXX: this needs to be called whenever the console is re-parented!
        if self._resize_handler_uuid:
            self._destroy_resize_handler()
        else:
            # this uuid is recycled and should not change for this object
            self._resize_handler_uuid = api.Registry.create_uuid()
        root_parent   = self.root_parent
        root_handlers = ItemAPI.information(root_parent)['handlers']
        if root_handlers is None:
            root_handlers = items.ItemHandlerRegistry(label='')
            ItemAPI.set_handlers(root_parent, root_handlers)
        items.ResizeHandler(
            label='',
            parent=root_handlers,
            callback=self._cb_resize,
            tag=self._resize_handler_uuid,
        )

    @override
    def move(self, *, parent: Item = 0, before: Item = 0) -> None:
        super().move(parent=parent, before=before)
        if parent:
            self._attach_resize_handler()

    @override
    def unstage(self):
        super().unstage()
        self._attach_resize_handler()

    @override
    def delete(self, *, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        if not children_only:
            self._destroy_resize_handler()
        self.console.delete(children_only=children_only, slot=slot)
        super().delete(children_only=children_only, slot=slot)

    @override
    def destroy(self):
        try: self._destroy_resize_handler()
        except: pass
        try: self.console.destroy()
        except: pass
        super().destroy()

    def clear_input(self):
        """Empty the input buffer."""
        self._input_pending.clear()


