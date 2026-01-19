"""Items for emulating consoles and other streams."""
import sys
import types
import typing
import codeop
import functools
import traceback
import threading
import itertools
import collections

from dearpygui import _dearpygui

from dearpypixl.core.protocols import Item, ItemCommand, ItemCallback
from dearpypixl.core import itemtype
from dearpypixl.core import codegen
from dearpypixl import items
from dearpypixl import color
from dearpypixl import style
from dearpypixl import constants




class _Event[T: typing.Callable]:
    __slots__ = ("_subscribers", "_lock", "_positional_only", "_pos_arg_count", "_callback")

    _callback: typing.Any

    def __init__(self, positional_only: bool = True, pos_arg_count: int = -1) -> None:
        self._lock = threading.Lock()
        self._positional_only = positional_only
        self._pos_arg_count = None if pos_arg_count < 0 else pos_arg_count
        self._callback = None
        self._subscribers = []

    @staticmethod
    def _noop(*args, **kwargs):
        pass

    def _create_callback(self, /) -> typing.Callable:
        if len(self._subscribers) == 0:
            return __class__._noop

        if self._pos_arg_count is not None:
            s_args = [f"arg{i}" for i in range(self._pos_arg_count)]
        else:
            s_args = ("*args",)

        if self._positional_only:
            s_kwds = ()
        else:
            s_kwds = ("**kwargs",)

        fn_lcls = {f"func{i}":func for i,func in enumerate(self._subscribers)}
        fn_args = (*s_args, *s_kwds)
        fn_body = f"({', '.join(fn_args)})\n".join(fn_lcls).split("\n")
        fn_body[-1] = fn_body[-1] + f"({', '.join(fn_args)})"

        return codegen.create_function(
            "callback", fn_args, fn_body, module=__name__, globals=globals(), locals=fn_lcls,
        )

    def notify(self, *args, **kwargs):
        callback = self._callback
        try:
            callback(*args, **kwargs)
            return
        except TypeError:
            if callback is not None:
                raise

        with self._lock:
            if self._callback is not None:
                callback = self._callback
            else:
                callback = self._callback = self._create_callback()

        callback(*args, **kwargs)

    __call__ = notify

    def subscribe(self, callback: T, /) -> T:
        with self._lock:
            self._subscribers.append(callback)
            self._callback = None
        return callback

    def unsubscribe(self, callback: typing.Any, /) -> None:
        with self._lock:
            self._subscribers.remove(callback)
            self._callback = None

    def subscribed(self, callback: typing.Any, /) -> bool:
        return callback in self._subscribers

    def cancel(self) -> None:
        with self._lock:
            self._subscribers.clear()
            self._callback = None


class LogRegistry[U = typing.Any](itemtype.CompositeItem, itemtype.SupportsValueArray[str], items.mvValueRegistry[U]):
    type _AddValueCallback = typing.Callable[[LogRegistry, Item], None]
    type _DelValueCallback = typing.Callable[[LogRegistry, Item], None]
    type _SetValueCallback = typing.Callable[[LogRegistry, Item, str], typing.Any]

    item_factory: ItemCommand

    on_value_add: _Event[_AddValueCallback]
    on_value_del: _Event[_DelValueCallback]
    on_value_set: _Event[_SetValueCallback]

    @classmethod
    def create(
        cls,
        default_value: typing.Sequence[str] | str = '',
        max_len: int | None = None,
        *,
        item_factory: ItemCommand = items.mvStringValue.__itemtype_command__,
        label: str | None = None,
        use_internal_label: bool = True,
        tag: Item = 0,
        user_data: U = None,
        **kwargs
    ) -> typing.Self:
        item = cls.__itemtype_command__(
            label=label,
            use_internal_label=use_internal_label,
            user_data={"user_data": user_data},
            tag=tag
        )

        self = cls(tag=item)
        self.max_len = max_len
        self.item_factory = item_factory
        self.on_value_add = _Event(True, 2)
        self.on_value_del = _Event(True, 2)
        self.on_value_set = _Event(True, 3)

        if default_value:
            self.set_value(default_value)

        return self

    def destroy(self, /) -> None:
        for attr in ("on_value_add", "on_value_set", "on_value_del"):
            try:
                event = getattr(self, attr)
            except AttributeError:
                pass
            else:
                event.cancel()
        super().destroy()

    @property
    def max_len(self) -> int | None:
        return self._max_len
    @max_len.setter
    def max_len(self, value: int | None):
        if value is not None and value < 0:
            raise ValueError("`max_len` cannot be less than zero.")
        self._max_len = value
    @max_len.deleter
    def max_len(self, /) -> None:
        self._max_len = None

    @property
    def value(self) -> list[str]:  # pyright: ignore[reportIncompatibleMethodOverride]
        return self.get_value()
    @value.setter
    def value(self, value: list[str], /) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        self.set_value(value)
    @value.deleter
    def value(self) -> None:
        self.set_value('')

    def get_value(self) -> list[str]:
        return _dearpygui.get_values(_dearpygui.get_item_configuration(self)["children"][1])

    def set_value(self, value: typing.Sequence[typing.Any], /) -> None:   # pyright: ignore[reportIncompatibleMethodOverride]
        update_child = self._update_child
        delete_child = self._delete_child

        items = self.children(1)
        for v, item in zip(value, self._itergen_items(items)):
            update_child(item, v)

        # delete leftover children
        for item in items[len(value):]:
            delete_child(item)

        self._truncate()

    def __str__(self) -> str:
        return '\n'.join(self.get_value())

    def __len__(self) -> int:
        return len(self._get_children())

    def __iter__(self) -> typing.Iterator[str]:
        yield from self.get_value()

    @typing.overload
    def __setitem__(self, index: typing.SupportsIndex, value: str, /) -> None: ...
    @typing.overload
    def __setitem__(self, slice: slice, value: list[str], /) -> None: ...
    def __setitem__(self, index, value, /) -> None:   # pyright: ignore[reportIncompatibleMethodOverride]
        items = self._get_children()
        if isinstance(index, slice):
            items = items[index]
            if len(items) != len(value):
                raise ValueError("slice and string sequence must be the same length")

            update_child = self._update_child
            for item, text in zip(items[index], value):
                update_child(item, text)
        else:
            self._update_child(items[index], value)

    def insert(self, index: typing.SupportsIndex, value: typing.Any, /) -> None:
        """Insert *value* at *index*, offsetting the position of trailing values by 1.
            >>> f = LogRegistry(["one", "two", "three"])
            >>> f.insert(1, "four")
            >>> arr
            ["one", "four", "two", "three"]
        """
        # value items don't have a "before" option, so first create
        # the child then reorder the children
        items = self._get_children()
        child = self._create_child()
        self._update_child(child, value)
        items.insert(index, child)
        self.reorder(1, items)
        self._truncate()

    def remove(self, value: str, /) -> None:
        """Remove the first line equal to *value*."""
        index = self.get_value().index(value)
        self._delete_child(self.children(1)[index])

    def extend(self, value: typing.Iterable[str]) -> None:
        v = self.get_value()
        v.extend(value)
        self.set_value(v)

    def append(self, value: str, /) -> None:
        self._update_child(self._create_child(), value)
        self._truncate()

    def clear(self) -> None:
        self.set_value('')

    # writable stream
    write = append
    writelines = extend

    def flush(self) -> None:
        pass

    def _itergen_items(self, items: typing.Iterable) -> typing.Generator[Item, None, None]:
        yield from items
        item_factory = self._create_child
        while True:
            yield item_factory()

    def _create_child(self, /, *args, parent = 0, **kwargs):
        child = self.item_factory(*args, parent=self, **kwargs)
        self.on_value_add(self, child)
        return child

    def _delete_child(self, child: Item, /):
        self.on_value_del(self, child)
        _dearpygui.delete_item(child, children_only=False, slot=-1)

    def _update_child(self, child: Item, value: str, /):
        _dearpygui.set_value(child, value)
        self.on_value_set(self, child, value)

    def _get_children(self, /):
        return _dearpygui.get_item_configuration(self)["children"][1]

    def _truncate(self):
        if self._max_len is not None:
            delete_child = self._delete_child
            for item in self._get_children()[self._max_len:]:
                delete_child(item)


@codegen.wrapped(LogRegistry.create)
def add_log_registry(*args, **kwargs):
    return LogRegistry.create(*args, **kwargs)




class Console[U = typing.Any, P: itemtype.ContainerItemT = typing.Any](itemtype.CompositeItem, items.mvChildWindow[U, P]):
    """Renders an underlying `LogRegistry` item."""

    _item_factory: ItemCommand

    log: LogRegistry
    auto_scroll: bool
    wrap_text: bool

    @typing.overload
    @classmethod
    def create(cls, default_value: typing.Sequence[str] | str = ..., max_len: int | None = ..., /, *, item_factory: ItemCommand = ..., auto_scroll: bool = ..., wrap_text: bool = ..., label: str | None = ..., user_data: U = ..., use_internal_label: bool = ..., tag: int | str = ..., width: int = ..., height: int = ..., indent: int = ..., parent: int | str = ..., before: int | str = ..., payload_type: str = ..., drop_callback: ItemCallback | None = ..., show: bool = ..., pos: typing.Sequence[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ..., no_scroll_with_mouse: bool = ..., flattened_navigation: bool = ..., always_use_window_padding: bool = ..., resizable_x: bool = ..., resizable_y: bool = ..., always_auto_resize: bool = ..., frame_style: bool = ..., auto_resize_x: bool = ..., auto_resize_y: bool = ..., **kwargs) -> typing.Self: ...
    @typing.overload
    @classmethod
    def create(cls, /, *, log_registry: LogRegistry | Item, item_factory: ItemCommand = ..., auto_scroll: bool = ..., wrap_text: bool = ..., label: str | None = ..., user_data: U = ..., use_internal_label: bool = ..., tag: int | str = ..., width: int = ..., height: int = ..., indent: int = ..., parent: int | str = ..., before: int | str = ..., payload_type: str = ..., drop_callback: ItemCallback | None = ..., show: bool = ..., pos: typing.Sequence[int] = ..., filter_key: str = ..., delay_search: bool = ..., tracked: bool = ..., track_offset: float = ..., border: bool = ..., autosize_x: bool = ..., autosize_y: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., menubar: bool = ..., no_scroll_with_mouse: bool = ..., flattened_navigation: bool = ..., always_use_window_padding: bool = ..., resizable_x: bool = ..., resizable_y: bool = ..., always_auto_resize: bool = ..., frame_style: bool = ..., auto_resize_x: bool = ..., auto_resize_y: bool = ..., **kwargs) -> typing.Self: ...
    @classmethod
    def create(
        cls,
        default_value: typing.Sequence[str] | str = '',
        max_len: int | None = None,
        /, *,
        log_registry: typing.Any = 0,
        auto_scroll: bool = True,
        wrap_text: bool = True,
        item_factory: ItemCommand = items.mvText.__itemtype_command__,
        tag: Item = 0,
        user_data: U = None,
        **kwargs
    ):
        item = cls.__itemtype_command__(user_data={"user_data": user_data, }, tag=tag, **kwargs)

        self = cls(tag=item)
        self._item_factory = item_factory
        self.auto_scroll = auto_scroll
        self.wrap_text = wrap_text

        if log_registry:
            if not isinstance(log_registry, LogRegistry):
                log_registry = LogRegistry(tag=log_registry)
        else:
            log_registry = LogRegistry.create(default_value, max_len)
            self.components = (log_registry,)  # cleanup on `destroy()`

        self.log = log_registry
        log_registry.on_value_add.subscribe(self._on_value_add)
        log_registry.on_value_del.subscribe(self._on_value_del)

        return self

    def destroy(self, /) -> None:
        try:
            log = self.log
        except AttributeError:
            pass
        else:
            try:
                log.on_value_add.unsubscribe(self._on_value_add)
            except (AttributeError, ValueError):
                pass

            try:
                log.on_value_del.unsubscribe(self._on_value_del)
            except (AttributeError, ValueError):
                pass

        super().destroy()

    def write(self, s: str, /) -> None:
        self.log.write(s)

    def writelines(self, s: typing.Iterable[str], /) -> None:
        self.log.writelines(s)

    def flush(self) -> None:
        self.log.flush()

    def _on_value_add(self, log: LogRegistry, item: Item, /):
        text_item = self._item_factory(parent=self, source=item)

        if self.wrap_text and 'wrap' in _dearpygui.get_item_configuration(text_item):
            _dearpygui.configure_item(text_item, wrap=self.content_region_avail[0])

        # our callback on item delete will receive the registry value item
        # but not out text item, so store a reference so it can find it later
        _dearpygui.configure_item(item, user_data=text_item)

        if self.auto_scroll:
            self.y_scroll_pos = -1.0

    def _on_value_del(self, log: LogRegistry, item: Item, /):
        text_item = _dearpygui.get_item_configuration(item)["user_data"]
        _dearpygui.delete_item(text_item, children_only=False, slot=-1)




# [ PyRepl ]

class PyInterpreter:
    type _CompileMode = typing.Literal["single", "exec", "eval"]

    class _WritableBuffer[T](typing.Protocol):
        def write(self, object: T, /) -> typing.Any: ...

    def _write_traceback(self, exc_type, error, trace, source = '', /):
        sys.last_type, sys.last_traceback = exc_type, trace

        error = error.with_traceback(trace)
        if source and isinstance(error, SyntaxError):
            err_text = error.text
            err_line = error.lineno
            if not err_text and err_line is not None and source.count("\n") >= err_line:
                error.text = source.splitlines()[err_line - 1]

        sys.last_exc = sys.last_value = error

        lines = traceback.format_exception(exc_type, error, trace)
        self._stderr.write(''.join(lines))

    def _write_syntaxerror(self, filename: str, source: str = ''):
        try:
            exc_type, error, trace = sys.exc_info()

            if filename and isinstance(error, SyntaxError):
                error.filename = filename

            self._write_traceback(exc_type, error, None, source)
        finally:
            exc_type = error = trace = None

    def _write_exception(self):
        self._write_traceback(*sys.exc_info(), "")

    _stdout_lock = threading.Lock()
    _stdout_stack = collections.deque()

    @staticmethod
    def _redirect_stdout(file, /, *, __lock=_stdout_lock, __stack=_stdout_stack):
        __lock.acquire()
        sys.stdout, stdout = file, sys.stdout
        __stack.appendleft(stdout)

    @staticmethod
    def _restore_stdout(*, __lock=_stdout_lock, __stack=_stdout_stack):
        sys.stdout = __stack.popleft()
        __lock.release()

    del _stdout_lock, _stdout_stack

    def __init__(
        self,
        /,
        locals: dict[str, typing.Any] | None = None,
        stdout: _WritableBuffer[str] | None = None,
        stderr: _WritableBuffer[str] | None = None,
        history: typing.Sequence[str] = (),
        histlen: int | None = 64,
        filename: str = "<console>"
    ) -> None:
        if locals is None:
            try:
                locals = sys.modules["__main__"].__dict__
            except KeyError, AttributeError:
                locals = {"__name__": "__console__", "__doc__" : None}

        try:
            if stdout is None:
                stdout = sys.stdout
                if stdout is None:
                    raise SystemError
            if stderr is None:
                stderr = sys.stderr
                if stderr is None:
                    raise SystemError
        except AttributeError, SystemError:
            raise SystemError(f"`stdout` and/or `stderr` not found") from None

        self._compile = codeop.CommandCompiler()
        self._stdout = stdout
        self._stderr = stderr
        self.filename = filename
        self.locals = locals
        self.buffer = collections.deque[str]()
        self.history = collections.deque[str](history, histlen)

    def execute(self, code: types.CodeType, source: str = '', /):
        self.flush()
        if source.strip() and (not self.history or self.history[0] != source):
            self.history.appendleft(source)

        try:
            __class__._redirect_stdout(self._stdout)
            try:
                exec(code, self.locals)
            finally:
                __class__._restore_stdout()
        except SystemExit:
            raise
        except:
            self._write_exception()

    def compile(self, source: str, filename: str, mode: _CompileMode = 'single'):
        try:
            return self._compile(source, filename, mode)
        except (OverflowError, SyntaxError, ValueError):

            self.flush()
            if source.strip() and (not self.history or self.history[0] != source):
                self.history.appendleft(source)

            self._write_syntaxerror(filename, source)
            return 1

    def push(self, line: str, filename: str = '', mode: _CompileMode = 'single'):
        """Compile a string as source code.

        The return of this method varies based on the outcome of the compilation:
            * `None`: More input is required.
            * `0`: Input compiled successfully and was executed (the result of
            which is uncertain).
            * `1`: An exception was raised compiling the input.

        When this method returns non-`None`, the completed source string is
        pushed to the history cache and the input buffer is flushed.
        """
        self.buffer.append(line)
        source = "\n".join(self.buffer)

        code = self.compile(source, filename, mode)
        if code == 1:
            return 1

        if code is not None:
            self.execute(code, source)
            return 0

        return None

    def write(self, s: str, /):
        self.push(s)

    def flush(self):
        """Clear the input buffer."""
        self.buffer.clear()


class PyRepl[U = typing.Any, P: itemtype.ContainerItemT = typing.Any](itemtype.CompositeItem, items.mvChildWindow[U, P]):
    ps1 = ">>>"
    ps2 = "..."

    python: PyInterpreter
    console: Console
    cprompt: items.mvText
    cinput: items.mvInputText

    cin_frame: items.mvChildWindow

    @typing.overload
    @classmethod
    def create(cls, locals: dict[str, typing.Any] | None = ..., *, log_registry: LogRegistry | Item = ..., label: str | None = None, user_data: typing.Any = None, use_internal_label: bool = True, tag: int | str = 0, width: int = 0, height: int = 0, indent: int = -1, parent: int | str = 0, before: int | str = 0, payload_type: str = '$', drop_callback: ItemCallback | None = None, show: bool = True, pos: typing.Sequence[int] = ..., filter_key: str = '', delay_search: bool = False, tracked: bool = False, track_offset: float = 0.5, border: bool = True, autosize_x: bool = False, autosize_y: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, flattened_navigation: bool = True, always_use_window_padding: bool = False, resizable_x: bool = False, resizable_y: bool = False, always_auto_resize: bool = False, frame_style: bool = False, auto_resize_x: bool = False, auto_resize_y: bool = False, **kwargs) -> typing.Self:  ... # pyright: ignore[reportInconsistentOverload]
    @classmethod
    def create(cls, locals = None, *, parent: int | str = 0, log_registry: Item = 0, no_scrollbar = True, no_scroll_with_mouse=True, **kwargs) ->  typing.Any:
        if locals is None:
            try:
                locals = sys.modules["__main__"].__dict__
            except KeyError, AttributeError:
                locals = {"__name__": "__console__", "__doc__" : None}

        item = cls.__itemtype_command__(
            parent=parent or _dearpygui.top_container_stack() or cls._create_window_parent(),
            no_scrollbar=True,
            no_scroll_with_mouse=True,
            **kwargs,
        )
        self = cls(tag=item)

        with items.handler_registry() as key_handlers:
            items.add_key_press_handler(constants.Key.UP, callback=self.set_history_text_next)
            items.add_key_press_handler(constants.Key.DOWN, callback=self.set_history_text_prev)
            items.add_key_press_handler(constants.Key.ESC, callback=self.set_history_text_prev)

        with items.theme() as theme:
            with items.theme_component():
                color.frame_bg(0, 0, 0, 0)
                color.child_bg(0, 0, 0)
                style.window_padding(8, 0)
                style.frame_padding(4, 4)
                style.item_spacing(8, 1)

        self.theme = theme

        with self:
            self.console = Console.create(log_registry=log_registry, autosize_x=True, height=10, border=False)
            self.console.log.on_value_set.subscribe(self.on_value_set)

            with items.child_window(no_scrollbar=True, border=False, auto_resize_y=True) as self.cin_frame:
                with items.group(horizontal=True, horizontal_spacing=0, indent=0) as group:

                    with items.item_handler_registry() as handlers:
                        items.add_item_visible_handler(callback=self.resize_console)

                    group.handlers = handlers

                    self.cprompt = items.add_text(self.ps1, indent=4)
                    self.cinput = self._create_console_input()

        self.python = PyInterpreter(locals, self.console, self.console)
        self.components = (key_handlers, handlers, theme, self.console)

        self.console.write(
            ''.join((
                "Python ", sys.version, " on ", sys.platform,
                '\nType "help", "copyright", "credits" or "license" for more information.\n\n'
            ))
        )

        return self

    _echo: bool = False

    def on_value_set(self, log: LogRegistry, item: Item, value: str):
        text_item = _dearpygui.get_item_configuration(item)['user_data']
        if self._echo:
            label = "stdin"
            color = 50, 210, 230, 150
        elif value.startswith("Traceback (") or '\nSyntaxError:' in value or '\nIndentationError:' in value:
            label = "stderr"
            color = 255, 20, 20, 255
        else:
            label = "stdout"
            color = 255, 255, 255, 255
        _dearpygui.configure_item(text_item, label=label, color=color)

    _ihist_offset: int = -1

    def reset_history_index(self, /):
        self._ihist_offset = -1

    def set_history_text(self, index: int, /):
        try:
            value = self.python.history[index]
        except IndexError:  # concurrency issue?
            return self.reset_history_index()

        # BUG/HACK [concurrency issue?]: Setting the input's value right now
        # doesn't "stick", so re-create it instead. The issue is re-produced
        # if we try re-using the old uuid.
        cinput = self.cinput
        parent = self.cinput.parent
        cinput.destroy()
        cinput = self.cinput = self._create_console_input(value, parent)
        cinput.focus()

    def set_history_text_next(self, /):
        hist_len = len(self.python.history)
        if not (
            hist_len and
            self.cinput.is_focused and
            self.cprompt.value == self.ps1
        ):
            return

        index = self._ihist_offset + 1

        if index > hist_len:
            self._ihist_offset = hist_len
            return

        self.set_history_text(index)

        if index == hist_len:
            self._ihist_offset = index - 1
        else:
            self._ihist_offset = index

    def set_history_text_prev(self, /):
        hist_len = len(self.python.history)
        if not (
            hist_len and
            self.cinput.is_focused and
            self.cprompt.value == self.ps1
        ):
            return

        index = self._ihist_offset - 1

        if index == -1:
            self.reset_history_index()
            self.cinput.value = ''
            return
        if index < -1:
            return

        self.set_history_text(index)
        self._ihist_offset = index

    def on_cinput_enter(self, sender: Item, text: str, user_data = None):
        self.cinput.value = ''

        if text:
            try:
                self._echo = True
                self.console.write(f"{self.cprompt.value} {text}")
            finally:
                self._echo = False

        result = self.python.push(text)
        if result is None:
            self.cprompt.value = self.ps2
        else:
            self.reset_history_index()
            self.cprompt.value = self.ps1

        self.cinput.focus()

    def resize_console(self, /):
        # 4 == padding/2
        ht_avail = self.rect_size[1] - self.cin_frame.rect_size[1] - 4
        if ht_avail < 4:
            self.console.configure(show=False)
        else:
            self.console.configure(show=True, height=ht_avail)

    @staticmethod
    def _create_window_parent():
        return items.window(width=600, height=400, no_scrollbar=True, no_scroll_with_mouse=True)

    def _create_console_input(self, default_value='', parent=0, tag=0):
        return items.add_input_text(
            default_value=default_value,
            parent=parent,
            tag=tag,
            hint="(enter a partial or complete Python expression/statement)",
            on_enter=True,
            escape_clears_all=True,
            width=-1,
            callback=self.on_cinput_enter,
        )


@codegen.wrapped(PyRepl.create)
def add_pyrepl(*args, **kwargs): # type: ignore
    return PyRepl.create(*args, **kwargs)
