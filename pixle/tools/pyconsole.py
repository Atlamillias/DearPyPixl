from code import InteractiveInterpreter
import io
import contextlib
import traceback
import sys

from dearpygui import dearpygui, _dearpygui
from pixle.application import Application
from pixle.containers import Window, Child, Group
from pixle.widgets import Text, InputText
from pixle.itemtypes import Item


__all__ = [
    "PyConsole",
]


class PycSTDOut(io.StringIO):
    msg_flag = {
        "-c": {"color": (200, 125, 0, 150)},  # code
        "-r": {"color": (0, 255, 120, 255), "indent": 5},  # return
        "-e": {"color": (255, 100, 100, 255)},  # error
    }

    def __init__(self, widget: Item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stdout_w = widget

    def write(self, string, flag: str = None):
        if string in ("", "\n"):
            return None

        params = self.msg_flag.get(flag, self.msg_flag["-r"])
        pretxt = f" << {string}"
        if flag == "-e":
            pretxt = f"  {string}"
        Text(pretxt, parent=self.stdout_w,**params,)


class PyConsole(InteractiveInterpreter):
    sys.ps1 = ">>> "
    sys.ps2 = "...  "

    def __init__(
        self,
        locals: dict = None,
        filename: str = None,
    ):
        super().__init__(locals)
        self.App = Application()
        self.parent = Window("InteractivePythonConsole",width=600, height=400)
        self.locals = locals or vars(__import__(__name__.split(".")[0]))
        self.filename = filename or self.__class__.__name__
        self.banner_msg = (
            f'Python ({self.__class__.__name__}) {sys.version} on {sys.platform}.\n'
            f'Type "help", "copyright", "credits" or "license" for more information.\n'
        )
        self.exit_msg = f"Exiting {self.__class__.__name__}...\n"

        with self.parent:
            self.parent.no_scrollbar = True
            self.parent.theme.style.item_spacing = 0,0
            self.parent.theme.style.item_inner_spacing = 0, 0
            self.parent.theme.style.window_padding = 4, 4
            with Child(autosize_x=True) as self.stdout:
                Text(self.banner_msg)
            dearpygui.add_dummy(height=1)
            with Child(no_scrollbar=True) as self.stdin_parent:
                with Group(horizontal=True):
                    self.prompt1 = Text(sys.ps1)
                    self.prompt2 = Text(sys.ps2, show=False)
                    self.stdin = InputText(
                        label="",
                        height=25,
                        on_enter=True,
                        tab_input=True,
                        callback=self.process,
                    )

        self._buffer = []
        self._file = PycSTDOut(self.stdout)
        self._unfinished_input = None
        self._parent_pad_x = self.parent.theme.style.window_padding
        self.stdin_parent.height = 35
        self.stdin.width = self.parent.width
        self.stdout.height = self.parent.height - 72

        @self.parent.on_resize
        def stdio_resize():
            self.stdin.width = self.parent.width
            self.stdout.height = self.parent.height - 72

    def __enter__(self):
        _dearpygui.push_container_stack(self.parent.id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        _dearpygui.pop_container_stack()

    def process(self, *args):
        Text(self.stdin.value, parent=self.stdout, color=[200, 125, 0, 150],)
        try:
            with contextlib.redirect_stderr(self._file):
                with contextlib.redirect_stdout(self._file):
                    self._unfinished_input = self.push(self.stdin.value)
        except KeyboardInterrupt:
            self._unfinished_input = None
            self._buffer = []

        if self._unfinished_input:
            self.prompt1.show = False
            self.prompt2.show = True

        else:
            self.prompt1.show = True
            self.prompt2.show = False

        # prep for next input
        self.stdout.y_scroll_pos = -1.0  # to the end
        self.stdin.value = ""
        self.stdin.focus()

    def push(self, line):
        self._buffer.append(line)
        code = "\n".join(self._buffer)
        more = self.runsource(code, self.filename)
        if not more:
            self._buffer = []
        return more

    def runcode(self, code):
        try:
            exec(code, self.locals)
        except SystemExit:
            raise
        except:
            self.showtraceback()

    def showtraceback(self):
        sys.last_type, sys.last_value, prev_traceback = ei = sys.exc_info()
        sys.last_traceback = prev_traceback
        try:
            lines = traceback.format_exception(ei[0], ei[1], prev_traceback.tb_next)
            if sys.excepthook is sys.__excepthook__:
                self._file.write(''.join(lines), "-e")
            else:
                # If someone has set sys.excepthook, we let that take precedence
                # over self.write
                sys.excepthook(ei[0], ei[1], prev_traceback)
        finally:
            prev_traceback = ei = None

    def showsyntaxerror(self, filename=None):
        type, value, tb = sys.exc_info()
        sys.last_type = type
        sys.last_value = value
        sys.last_traceback = tb
        if filename and type is SyntaxError:
            # Work hard to stuff the correct filename in the exception
            try:
                msg, (dummy_filename, lineno, offset, line) = value.args
            except ValueError:
                # Not the format we expect; leave it alone
                pass
            else:
                # Stuff in the right filename
                value = SyntaxError(msg, (filename, lineno, offset, line))
                sys.last_value = value
        if sys.excepthook is sys.__excepthook__:
            lines = traceback.format_exception_only(type, value)
            self._file.write(''.join(lines), "-e")
        else:
            # If someone has set sys.excepthook, we let that take precedence
            # over self.write
            sys.excepthook(type, value, tb)
