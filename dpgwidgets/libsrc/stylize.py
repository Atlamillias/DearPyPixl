from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.item import Item, ContextSupport

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Font",
    "Theme",
    "FontChars",
    "FontRange",
    "FontRangeHint",
    "ThemeColor",
    "ThemeStyle",
]


class Font(Item, ContextSupport):
    """Undocumented function
    Args:
            file (str): 
            size (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **default_font (bool): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_font

    def __init__(
        self, 
        file: str, 
        size: int, 
        label: str = None, 
        user_data: Any = None, 
        default_font: bool = False, 
        parent: int = 10, 
        **kwargs, 
    ):
        super().__init__(
            file=file,
            size=size,
            label=label,
            user_data=user_data,
            default_font=default_font,
            parent=parent,
            **kwargs,
        )
        self.file = file
        self.size = size
        self.label = label
        self.user_data = user_data
        self.default_font = default_font
        self.parent = parent


class Theme(Item, ContextSupport):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **user_data (Any): User data for callbacks.
            **default_theme (bool): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_theme

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        default_theme: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            default_theme=default_theme,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.default_theme = default_theme


class FontChars(Item):
    """Undocumented function
    Args:
            chars (List[int]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_font_chars

    def __init__(
        self, 
        chars: list[int], 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            chars=chars,
            label=label,
            parent=parent,
            user_data=user_data,
            **kwargs,
        )
        self.chars = chars
        self.label = label
        self.parent = parent
        self.user_data = user_data


class FontRange(Item):
    """Undocumented function
    Args:
            first_char (int): 
            last_char (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_font_range

    def __init__(
        self, 
        first_char: int, 
        last_char: int, 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            first_char=first_char,
            last_char=last_char,
            label=label,
            parent=parent,
            user_data=user_data,
            **kwargs,
        )
        self.first_char = first_char
        self.last_char = last_char
        self.label = label
        self.parent = parent
        self.user_data = user_data


class FontRangeHint(Item):
    """Undocumented function
    Args:
            hint (int): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_font_range_hint

    def __init__(
        self, 
        hint: int, 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            hint=hint,
            label=label,
            parent=parent,
            user_data=user_data,
            **kwargs,
        )
        self.hint = hint
        self.label = label
        self.parent = parent
        self.user_data = user_data


class ThemeColor(Item):
    """Undocumented function
    Args:
            *target (int): 
            *value (List[int]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
            **category (int): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_theme_color

    def __init__(
        self, 
        target: int = 0, 
        value: list[int] = (0, 0, 0, 255), 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        category: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            target=target,
            value=value,
            label=label,
            parent=parent,
            user_data=user_data,
            category=category,
            **kwargs,
        )
        self.target = target
        self.value = value
        self.label = label
        self.parent = parent
        self.user_data = user_data
        self.category = category


class ThemeStyle(Item):
    """Undocumented function
    Args:
            *target (int): 
            *x (float): 
            *y (float): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **user_data (Any): User data for callbacks.
            **category (int): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_theme_style

    def __init__(
        self, 
        target: int = 0, 
        x: float = 1.0, 
        y: float = -1.0, 
        label: str = None, 
        parent: int = 0, 
        user_data: Any = None, 
        category: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            target=target,
            x=x,
            y=y,
            label=label,
            parent=parent,
            user_data=user_data,
            category=category,
            **kwargs,
        )
        self.target = target
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.user_data = user_data
        self.category = category
