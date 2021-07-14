from typing import Callable, Any

from . import dpg
from ._item import Item, ContextSupport


##################################################
## Note: this file was automatically generated. ##
##################################################


class FontChars(Item):
    _command: Callable = dpg.add_font_chars

    def __init__(
        self,
        chars: list[int],
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        chars=chars,
        label=label,
        parent=parent,
        user_data=user_data,
        **kwargs
        )
        self.chars = chars
        self.label = label
        self.parent = parent
        self.user_data = user_data


class FontRange(Item):
    _command: Callable = dpg.add_font_range

    def __init__(
        self,
        first_char: int,
        last_char: int,
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        first_char=first_char,
        last_char=last_char,
        label=label,
        parent=parent,
        user_data=user_data,
        **kwargs
        )
        self.first_char = first_char
        self.last_char = last_char
        self.label = label
        self.parent = parent
        self.user_data = user_data


class FontRangeHint(Item):
    _command: Callable = dpg.add_font_range_hint

    def __init__(
        self,
        hint: int,
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        **kwargs
    ):
        super().__init__(
        hint=hint,
        label=label,
        parent=parent,
        user_data=user_data,
        **kwargs
        )
        self.hint = hint
        self.label = label
        self.parent = parent
        self.user_data = user_data


class ThemeColor(Item):
    _command: Callable = dpg.add_theme_color

    def __init__(
        self,
        target: int = 0,
        value: list[int] = [0, 0, 0, 255],
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        category: int = 0,
        **kwargs
    ):
        super().__init__(
        target=target,
        value=value,
        label=label,
        parent=parent,
        user_data=user_data,
        category=category,
        **kwargs
        )
        self.target = target
        self.value = value
        self.label = label
        self.parent = parent
        self.user_data = user_data
        self.category = category


class ThemeStyle(Item):
    _command: Callable = dpg.add_theme_style

    def __init__(
        self,
        target: int = 0,
        x: float = 1.0,
        y: float = -1.0,
        label: str = None,
        parent: int = 0,
        user_data: Any = None,
        category: int = 0,
        **kwargs
    ):
        super().__init__(
        target=target,
        x=x,
        y=y,
        label=label,
        parent=parent,
        user_data=user_data,
        category=category,
        **kwargs
        )
        self.target = target
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.user_data = user_data
        self.category = category


class Theme(Item, ContextSupport):
    _command: Callable = dpg.add_theme

    def __init__(self, label: str = None, user_data: Any = None, default_theme: bool = False, **kwargs):
        super().__init__(label=label, user_data=user_data, default_theme=default_theme, **kwargs)
        self.label = label
        self.user_data = user_data
        self.default_theme = default_theme


class Font(Item, ContextSupport):
    _command: Callable = dpg.add_font

    def __init__(
        self,
        file: str,
        size: int,
        label: str = None,
        user_data: Any = None,
        default_font: bool = False,
        parent: int = 10,
        **kwargs
    ):
        super().__init__(
        file=file,
        size=size,
        label=label,
        user_data=user_data,
        default_font=default_font,
        parent=parent,
        **kwargs
        )
        self.file = file
        self.size = size
        self.label = label
        self.user_data = user_data
        self.default_font = default_font
        self.parent = parent
