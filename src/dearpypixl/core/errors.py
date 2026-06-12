import enum as _enum
import dataclasses as _dataclasses




class mvErrorCode(_enum.IntEnum):
    """DearPyGui error codes."""
    NONE                  = 1000  # mvErrorCode::mvNone
    TEXTURE_NOT_FOUND     = 1001  # mvErrorCode::mvTextureNotFound
    INCOMPATIBLE_TYPE     = 1002  # mvErrorCode::mvIncompatibleType
    INCOMPATIBLE_PARENT   = 1003  # mvErrorCode::mvIncompatibleParent
    INCOMPATIBLE_CHILD    = 1004  # mvErrorCode::mvIncompatibleChild
    ITEM_NOT_FOUND        = 1005  # mvErrorCode::mvItemNotFound
    SOURCE_NOT_FOUND      = 1006  # mvErrorCode::mvSourceNotFound
    SOURCE_NOT_COMPATIBLE = 1007  # mvErrorCode::mvSourceNotCompatible
    WRONG_TYPE            = 1008  # mvErrorCode::mvWrongType
    CONTAINER_STACK_EMPTY = 1009  # mvErrorCode::mvContainerStackEmpty
    STAGING_MODE_OFF      = 1010  # mvErrorCode::mvStagingModeOff
    PARENT_NOT_DEDUCED    = 1011  # mvErrorCode::mvParentNotDeduced

    @classmethod
    def from_message(cls, message: str, /) -> mvErrorCode:
        """Return the error code contained within a DearPyGui error message."""
        code = message.partition("]")[0].partition('[')[2]
        if not code.isdigit():
            code = cls.NONE

        code = int(code)

        return cls(code)

    @classmethod
    def from_exception(cls, exception: SystemError | Exception, /) -> mvErrorCode:
        """Return the error code contained within the message of an error
        set by DearPyGui or `SystemError` it caused."""
        if not exception.args[0].lstrip().startswith("Error"):
            exception = exception.__cause__ # type: ignore
            if not exception.args[0].lstrip().startswith("Error"):
                return cls.NONE

        return cls.from_message(exception.args[0])


@_dataclasses.dataclass(slots=True, frozen=True)
class mvErrorInfo:
    errno    : mvErrorCode
    command  : str                         = ''
    item     : int | str | None            = None
    item_type: str | None                  = None
    message  : str                         = ''
    metadata : tuple[tuple[str, str], ...] = ()

    def __str__(self, /):
        d: dict = {"error": self.errno, "command": self.command}

        col_size = 7

        if self.item:
            d["item"] = self.item
        if self.item_type:
            d["item_type"] = self.item_type
            col_size = 9

        for k, v in self.metadata:
            if (nchars := len(k)) > col_size:
                col_size = nchars
            d[k] = v

        d["message"] = self.message

        return '\n'.join(f"{k.ljust(col_size)}: {v}" for k,v in d.items())

    @classmethod
    def from_message(cls, message: str, /) -> mvErrorInfo:
        try:
            errno = mvErrorCode.from_message(message)
        except TypeError:
            raise ValueError("cannot parse `message` — no error code found")

        text, _, message = message.partition("]")[2].strip().replace("mvAppItemType::", '').rpartition("Message:")

        errinfo = {"command": ''}

        for ln in text.splitlines():
            key, _, val = ln.partition(': ')
            val = val.strip(' \r\t[]')
            if val: errinfo[key.lower().replace(" ", "_")] = val

        command = errinfo.pop("command")

        item = errinfo.pop("item", None)
        if item and item.isdigit():
            item = int(item)

        item_type = errinfo.pop("item_type", None)

        message = ', '.join(message.lstrip().splitlines()).replace("\t", ' ').rstrip('.') + '.'

        if not errinfo:
            metadata = ()
        else:
            metadata = tuple(errinfo.items())

        return cls(errno, command, item, item_type, message, metadata)


class DearPyGuiError(SystemError):
    """Base exception class for errors set by DearPyGui that include
    an error code.

    :py:class:`DearPyGuiError` is a direct subclass of `SystemError`.
    """
    __slots__ = ("_errinfo",)

    _ERRNO_TO_EXC_MAP = {}
    _DEFAULT_ERRINFO  = mvErrorInfo(mvErrorCode.NONE)

    errno = mvErrorCode.NONE

    @property
    def errinfo(self, /) -> mvErrorInfo:
        """Return the `mvErrorInfo` structure containing details of the
        original DearPyGui error message this exception was created from."""
        return self._errinfo

    @property
    def command(self, /):
        """Return the name of the DearPyGui function that set the original error."""
        return self._errinfo.command

    @property
    def item(self, /):
        """Return the item ID referenced within the error's context. The item may
        or may not exist."""
        return self._errinfo.item

    @property
    def item_type(self, /):
        """Return the internal item type of :py:attr:`item` (if any)."""
        return self._errinfo.item_type

    @property
    def message(self, /):
        """Return the section of the original DearPyGui error message containing
        the error's comment(s)."""
        return self._errinfo.message

    def __init__(self, /, *args):
        if args and isinstance(args[0], mvErrorInfo):
            self._errinfo, *args = args
        else:
            self._errinfo = self._DEFAULT_ERRINFO
        super().__init__(*args)

    def __str__(self, /) -> str:
        message = '\n- ' + str(self._errinfo).replace('\n', '\n- ')
        if self.args:
            message = f"{super().__str__()}\n{message}"
        return message

    @staticmethod
    def from_message(message: str, /) -> DearPyGuiError:
        """Parse *message* and return an appropriate :py:class:`DearPyGuiError`
        exception. `ValueError` is raised if a DearPyGui error code cannot be
        parsed from the message.

        :type message: `str`
        :param message: The message of the direct `Exception` error set by
            DearPyGui.

        :raises `ValueError`: The message could not be parsed.
        """
        errinfo = mvErrorInfo.from_message(message)
        return __class__._ERRNO_TO_EXC_MAP[errinfo.errno](errinfo)

    @staticmethod
    def from_exception[T: BaseException](exception: T, /) -> DearPyGuiError | T:
        """Create a new high-level exception object from an error set by
        DearPyGui (OR the `SystemError` that it caused). The original
        error is returned if a new error cannot be created e.g. it is a
        non-DearPyGui error, etc.

        New errors have the original error's context and traceback but
        with `__cause__` set to `None`, suppressing the original error(s)
        when raised.

        :type exception: `BaseException`
        :param exception: The exception in context.
        """
        exc_type = type(exception)
        if issubclass(exc_type, SystemError):
            error = exception.__cause__
            if error is None or type(error) is not Exception:
                return exception
        elif exc_type is Exception:
            error = exception
        else:
            return exception

        message = error.args[0]

        try:
            error = __class__.from_message(message)
        except ValueError:
            return exception

        error.__context__   = exception.__context__
        error.__traceback__ = exception.__traceback__
        error.__cause__     = None

        return error


def _create_dearpygui_err_type(name: str, error_code: mvErrorCode, /) -> type[DearPyGuiError]:
    class Error(DearPyGuiError):
        __slots__ = ()
        errno = error_code

    Error.__name__ = Error.__qualname__ = name
    Error._ERRNO_TO_EXC_MAP[error_code] = Error
    Error._DEFAULT_ERRINFO              = mvErrorInfo(error_code)

    return Error

TextureNotFoundError = _create_dearpygui_err_type("TextureNotFoundError", mvErrorCode.TEXTURE_NOT_FOUND)
IncompatibleTypeError = _create_dearpygui_err_type("IncompatibleTypeError", mvErrorCode.INCOMPATIBLE_TYPE)
IncompatibleParentError = _create_dearpygui_err_type("IncompatibleParentError", mvErrorCode.INCOMPATIBLE_PARENT)
IncompatibleChildError = _create_dearpygui_err_type("IncompatibleChildError", mvErrorCode.INCOMPATIBLE_CHILD)
ItemNotFoundError = _create_dearpygui_err_type("ItemNotFoundError", mvErrorCode.ITEM_NOT_FOUND)
SourceNotFoundError = _create_dearpygui_err_type("SourceNotFoundError", mvErrorCode.SOURCE_NOT_FOUND)
SourceNotCompatibleError = _create_dearpygui_err_type("SourceNotCompatibleError", mvErrorCode.SOURCE_NOT_COMPATIBLE)
WrongTypeError = _create_dearpygui_err_type("WrongTypeError", mvErrorCode.WRONG_TYPE)
ContainerStackEmptyError = _create_dearpygui_err_type("ContainerStackEmptyError", mvErrorCode.CONTAINER_STACK_EMPTY)
StagingModeOffError = _create_dearpygui_err_type("StagingModeOffError", mvErrorCode.STAGING_MODE_OFF)
ParentNotDeducedError = _create_dearpygui_err_type("ParentNotDeducedError", mvErrorCode.PARENT_NOT_DEDUCED)


err_from_exception = DearPyGuiError.from_exception
err_from_message   = DearPyGuiError.from_message


class DearPyGuiErrorHandler:
    """A context manager that automatically creates and raises high-level
    exceptions from errors set by DearPyGui should they occur. New errors
    are raised within the same context as the original.

    Non-DearPyGui errors are not handled and are propegated as normal.
    """
    __slots__ = ()

    def __enter__(self, /):
        return

    def __exit__(self, error_type, error, traceback, /):
        if error_type is None or type(error) is not SystemError:
            return

        try:
            message = error.__cause__.args[0]  # type: ignore
        except AttributeError:
            return

        new_error = DearPyGuiError.from_message(message)
        new_error.__context__   = error.__context__
        new_error.__traceback__ = error.__traceback__
        new_error.__cause__     = None
        raise new_error


error_handler = DearPyGuiErrorHandler()
