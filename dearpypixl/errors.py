import functools
from typing import Callable
from dataclasses import dataclass
from enum import IntEnum
from dearpygui import dearpygui

# NOTE: error codes are in:
# "DearPyGui/src/core/PythonUtilities/mvPythonExceptions"



_dedicated_errors: dict[str, Callable] = {}


class DearPyGuiErrorHandler:
    use_dedicated_errors = True
    dedicated_errors = _dedicated_errors

    def __init__(self, item_instance: object, attr: str = None, value = None):
        self.item = item_instance
        self.attr = attr
        self.value = value
        self.info = None

        self.error_info = None
        self.traceback = None

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        if not exc_type:
            return None
        elif not self.use_dedicated_errors:
            raise exc_type

        self.traceback = traceback
        error_handler = self._get_exception(exc_value)
        if not error_handler:
            raise exc_value
        error = error_handler()
        raise error from None

    @staticmethod
    def _new_message_formatter(message: str, line_length: int = 80):
        if (msg_length := len(message)) <= line_length:
            return message
        # Converting extra inner whitespace chars to 1 space.
        message = " ".join(message.split())
        buffer = []
        remaining_lines = round(msg_length / line_length)
        start_pos = 0
        prev_whitespace_pos = ...
        for pos, char in enumerate(message):
            # Track the last whitespace character so we don't split
            # through words.
            if char.isspace():
                prev_whitespace_pos = pos
            if not pos or not pos % line_length == 0:
                continue
            # Append the message section (whole line) and build the next.
            buffer.append(message[start_pos: prev_whitespace_pos])
            start_pos = prev_whitespace_pos + 1
            remaining_lines -= 1
            # Skip the entire above process if it's the last section
            # as it's length will be less than or equal to `line_length`.
            if remaining_lines == 1:
                buffer.append(message[start_pos:])
                break
        else:
            buffer.append(message)
        return "\n".join(buffer)

    @staticmethod
    def _old_message_formatter(context_msg: str):
        categories = [
            "Error:",
            "Command:",
            "Label:",
            "Item Type:",
            "Message:",
            "Item:"
        ]
        cat_map = {
            "Error:": "error_code",
            "Command:": "command",
            "Label:": "label",
            "Item Type:": "item_type",
            "Message:": "message",
            "Item:": "item_uuid"
        }
        error_info = {
            "error_code": None,
        }
        # Some error messages are multiline and some aren't (for
        # *some* reason). Flattening...
        context_msg = context_msg.replace("\n", " ")
        context_msg = " ".join(context_msg.split())
        found_categories = {cat: category_pos for cat in categories
                            if (category_pos := context_msg.find(cat)) != -1}
        # Sorting based off the position found.
        found_categories = sorted(
            found_categories.items(), key=lambda pair: pair[1])
        positions = [pos for _, pos in found_categories]

        error_info = {}
        for idx, (cat, pos) in enumerate(found_categories):
            try:
                info = context_msg[pos: positions[idx + 1]]
            except IndexError:
                info = context_msg[pos:]
            # Seperating category from actual information.
            info = info.split(cat)[-1]
            # The "Error:" category value will be enclosed in brackets.
            error_info[cat_map[cat]] = info.strip(" []")
        return error_info

    def _general_str_format(self, str_to_format: str):
        # Calls `str_to_format.format()`. Formatting is done on
        # substitutions `item`, `value`, `info`, and `attr` (instance attrs).
        # Substitutions for the former two will be wrapped in
        # `type(sub).__qualname__`. This is for general cases to avoid
        # some mistakes in repeating commonly used code.
        format_params = {}
        if '{item}' in str_to_format:
            format_params["item"] = f"{type(self.item).__qualname__!r}"
        if '{value}' in str_to_format:
            format_params["value"] = f"{type(self.value).__qualname__!r}"
        if '{attr}' in str_to_format:
            format_params["attr"] = f"{self.attr!r}"
        if '{info}' in str_to_format:
            format_params["info"] = f"{self.info}"
        return str_to_format.format(**format_params)

    def _get_exception(self, error: SystemError):
        error_info = self._old_message_formatter(error.__context__.args[0])
        self.error_info = error_info
        if error_info["error_code"] not in self.dedicated_errors:
            return None
        return eval(f'self.{self.dedicated_errors[error_info["error_code"]]}')


    def dearpygui_error(error_code):
        def wrapper(method):
            @functools.wraps(method)
            def error_handler(self, *args, **kwargs) -> Exception:
                if not self.item:
                    return self.error_info["message"]
                error: Exception = method(self)
                error.__traceback__ = self.traceback
                error.args = (self._new_message_formatter(error.args[0]),)
                return error
            _dedicated_errors[error_code] = method.__name__
            return error_handler
        error_code = str(error_code)
        return wrapper

    @dearpygui_error(1000)
    def invalid_parameter(self):
        # Error: [1000] Message: 	<INFO> keyword does not exist.
        error = TypeError
        message1 = "{item} got an unexpected keyword argument {info}."

        self.info = f'{self.error_info["message"].split(" ", maxsplit=1)[0]!r}'
        return error(self._general_str_format(message1))

    @dearpygui_error(1003)
    def incompatible_parent(self) -> TypeError:
        # Error:   1003
        # Message: Incompatible parent. Acceptable parents include: mvAppItemType::<ITEM>\n
        # mvAppItemType::<ITEM>\n
        error = TypeError
        # Failure at assignment...
        message1 = "{value} is an incompatible parent for {item}. \
                    Applicable parents for {item} are: {info}."
        # Failure at item creation...
        message2 = "Cannot create {item} item as its parent would be incompatible.\
                    Applicable parents for {item} are: {info}."
        unfmt_parents = self.error_info["message"].split(": ", maxsplit=1)[-1]
        parents = [f'{parent.split("::mv")[-1]!r}' for parent in unfmt_parents.split()]
        self.info = f'{", ".join(parents[:-1])}, and {parents[-1]}'
        if not self.value:
            message = message2
        else:
            message = message1
        return error(self._general_str_format(message))

    @dearpygui_error(1005)
    def item_not_found(self) -> ValueError:
        # Error:   1005
        # Message: Item not found: <tag>
        error = ValueError
        message1 = "{value} item could not be found."
        message2 = "Cannot assign the parent of top-level container item {item}."
        # When it is attempted to move a root item into another root item,
        # DPG will return this error. We're making sure that `self.value` absolutely
        # does not exist, and return a different `message` depending on the result.
        if dearpygui.does_item_exist(int(self.value)):
            message = message2
        else:
            message = message1
        return error(self._general_str_format(message))

    @dearpygui_error(1011)
    def parent_not_deduced(self) -> TypeError:
        error = TypeError
        message = "The `parent` argument is required to create a {item} item in \
                   this context."
        return error(self._general_str_format(message))

        

class NullError(Exception):
    message = None


class TextureNotFoundError(Exception):
    message = None


class IncompatibleTypeError(Exception):
    message = None


class IncompatibleChildError(Exception):
    message = None


 


class SourceNotFoundError(Exception):
    message = None


class SourceNotCompatibleError(Exception):
    message = None


class WrongTypeError(Exception):
    message = None


class ContainerStackEmptyError(Exception):
    message = None


class StagingModeOffError(Exception):
    message = None


class ParentNotDeducedError(Exception):
    message = None


class IncompatibleParentError(Exception):
    

    def __init__(self, message: str, item: object = None, value = None, *args):
        
        if not item or not value:
            super().__init__(message)
        else:
            self.message = self.message
            message = message.split(": ", maxsplit=1)[1]
            r_possible_parents = message.splitlines()
            possible_parents = [parent for _, parent in 
                                r_possible_parents.split("::mv", maxsplit=1)]

            self.message = self.message.format(
                value=f'{type(value).__qualname__!r}',
                item=f'{type(item).__qualname__!r}',
                info=", ".join(possible_parents)
                )
            super().__init__(self.message)







class FontSizeError(Exception):
    """Raised if a font size is not valid.
    """


class ItemConfigurationError(Exception):
    """Raised when a general error occurs regarding an item's
    internal configuration.
    """


class ItemConfigValueError(Exception):
    """A `ValueError` or `TypeError` used regarding an item's
    internal configuration when the configuration option is applicable,
    but the value or the type of value isn't correct.
    """
    def __init__(self, obj, value, msg: str):
        self.message = msg or (
            f"Incompatable value or value type for {type(obj)!r} item, got {value} ({type(value)}).")
        super().__init__(self.message)




class ItemBindingError(Exception):
    """Raised when an item cannot be (un)bound to another.
    """


class ItemCompatabilityError(Exception):
    """Raised when an item would be incompatible to another.
    w"""
