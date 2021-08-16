from typing import (
    Any,
    Callable,
    Union,
    Dict,
    Tuple,
    Set,
    List,
)
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
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **default_font (bool): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_font

    def __init__(
        self, 
        file: str, 
        size: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_font: bool = False, 
        parent: Union[int, str] = 10, 
        **kwargs, 
    ):
        super().__init__(
            file=file,
            size=size,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_font=default_font,
            parent=parent,
            **kwargs,
        )
        self.file = file
        self.size = size
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_font = default_font
        self.parent = parent


class Theme(Item, ContextSupport):
    """Undocumented function
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **default_theme (bool): 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_theme

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_theme: bool = False, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_theme=default_theme,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_theme = default_theme


class FontChars(Item):
    """Undocumented function
    Args:
            chars (Union[List[int], Tuple[int]]): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_font_chars

    def __init__(
        self, 
        chars: Union[List[int], Tuple[int]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        **kwargs, 
    ):
        super().__init__(
            chars=chars,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.chars = chars
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class FontRange(Item):
    """Undocumented function
    Args:
            first_char (int): 
            last_char (int): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_font_range

    def __init__(
        self, 
        first_char: int, 
        last_char: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        **kwargs, 
    ):
        super().__init__(
            first_char=first_char,
            last_char=last_char,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.first_char = first_char
        self.last_char = last_char
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class FontRangeHint(Item):
    """Undocumented function
    Args:
            hint (int): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_font_range_hint

    def __init__(
        self, 
        hint: int, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        **kwargs, 
    ):
        super().__init__(
            hint=hint,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )
        self.hint = hint
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent


class ThemeColor(Item):
    """Undocumented function
    Args:
            *target (int): 
            *value (Union[List[int], Tuple[int]]): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
            **category (int): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_theme_color

    def __init__(
        self, 
        target: int = 0, 
        value: Union[List[int], Tuple[int]] = (0, 0, 0, 255), 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        category: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            target=target,
            value=value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            category=category,
            **kwargs,
        )
        self.target = target
        self.value = value
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.category = category


class ThemeStyle(Item):
    """Undocumented function
    Args:
            *target (int): 
            *x (float): 
            *y (float): 
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
            **category (int): Options include mvThemeCat_Core, mvThemeCat_Plots, mvThemeCat_Nodes.
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_theme_style

    def __init__(
        self, 
        target: int = 0, 
        x: float = 1.0, 
        y: float = -1.0, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        category: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            target=target,
            x=x,
            y=y,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            category=category,
            **kwargs,
        )
        self.target = target
        self.x = x
        self.y = y
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.category = category
