from typing import Callable, Any
from dearpygui import dearpygui
from ..item import Item, ItemProperty, ItemIdType, CONFIG


__all__ = [
    "FontRegistry",
    "Font",
    "FontChars",
    "FontRange",
    "FontRangeHint",
    "CharRemap",
]


class FontRegistry(Item):
    """Adds a font registry.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * show (bool, optional): Attempt to render widget.
    """
    show: bool = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvFontRegistry, "FontRegistry")
    __is_container__ : bool       = True
    __is_root_item__ : bool       = True
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = ()
    __able_children__: tuple      = (dearpygui.mvFont,)
    __command__      : Callable   = dearpygui.add_font_registry

    def __init__(
        self,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class Font(Item):
    """Adds font to a font registry.

        Args:
            * file (str):
            * size (int):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * default_font (bool, optional): (deprecated)
    """
    file: str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    size: int = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvFont, "mvFont")
    __is_container__ : bool       = True
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = (dearpygui.mvFontRegistry,)
    __able_children__: tuple      = (dearpygui.mvFontChars, dearpygui.mvFontRange, dearpygui.mvCharRemap, dearpygui.mvFontRangeHint, dearpygui.mvTemplateRegistry)
    __commands__     : tuple      = ('bind_font', 'get_text_size')
    __command__      : Callable   = dearpygui.add_font

    def __init__(
        self,
        file              : str                   ,
        size              : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str = 10  ,
        **kwargs
    ) -> None:
        super().__init__(
            file=file,
            size=size,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontChars(Item):
    """Adds specific font characters to a font.

        Args:
            * chars (list[int] | tuple[int, ...]):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    chars: list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvFontChars, "mvFontChars")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = (dearpygui.mvFont, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_font_chars

    def __init__(
        self,
        chars             : list[int] | tuple[int, ...]      ,
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : int | str                  = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            chars=chars,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontRange(Item):
    """Adds a range of font characters to a font.

        Args:
            * first_char (int):
            * last_char (int):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    first_char: int = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    last_char : int = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvFontRange, "mvFontRange")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = (dearpygui.mvFont, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_font_range

    def __init__(
        self,
        first_char        : int                   ,
        last_char         : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            first_char=first_char,
            last_char=last_char,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class FontRangeHint(Item):
    """Adds a range of font characters (mvFontRangeHint_ constants).

        Args:
            * hint (int):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    hint: int  = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvFontRangeHint, "mvFontRangeHint")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = (dearpygui.mvFont, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __constants__    : tuple      = ('mvFontRangeHint', 'mvFontRangeHint_Default', 'mvFontRangeHint_Japanese', 'mvFontRangeHint_Korean', 'mvFontRangeHint_Chinese_Full', 'mvFontRangeHint_Chinese_Simplified_Common', 'mvFontRangeHint_Cyrillic', 'mvFontRangeHint_Thai', 'mvFontRangeHint_Vietnamese')
    __command__      : Callable   = dearpygui.add_font_range_hint

    def __init__(
        self,
        hint              : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            hint=hint,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class CharRemap(Item):
    """Remaps a character.

        Args:
            * source (int):
            * target (int):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    source: int = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    target: int = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    __itemtype_id__  : ItemIdType = ItemIdType(dearpygui.mvCharRemap, "mvCharRemap")
    __is_container__ : bool       = False
    __is_root_item__ : bool       = False
    __is_value_able__: bool       = False
    __able_parents__ : tuple      = (dearpygui.mvFont, dearpygui.mvTemplateRegistry)
    __able_children__: tuple      = ()
    __command__      : Callable   = dearpygui.add_char_remap

    def __init__(
        self,
        source            : int                   ,
        target            : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str = 0   ,
        **kwargs
    ) -> None:
        super().__init__(
            source=source,
            target=target,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )