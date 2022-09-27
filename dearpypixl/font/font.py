import enum
import functools
from os import PathLike
from typing import Callable, Any, Sequence
from typing_extensions import Self
from dearpygui import dearpygui, _dearpygui
from dearpygui._dearpygui import configure_item, get_item_configuration, does_item_exist
from dearpygui.dearpygui import (
    add_font,
    add_font_chars,
    add_font_range,
    add_font_range_hint,
    add_char_remap,
    add_font_registry,
    bind_item_font,
    does_item_exist,
)
from .._internal import registry
from .._internal.item import ItemType, Item, LinkedItem, ItemData
from .._internal.constants import FontRangeHint as FontRangeHintValue
from .._internal.utilities import UpdaterSet
from .._internal.comtypes import Filepath



class FontChars(Item):
    """Add specific font characters to a font.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFontChars, "mvFontChars"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvFont,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=add_font_chars,
    )

    chars: list[int] | tuple[int, ...] = __dearpypixl__.set_configuration(None, None)

    def __init__(
        self,
        chars             : list[int] | tuple[int, ...]      ,
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0   ,
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


class FontCharRemap(Item):
    """Remaps a character.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvCharRemap, "mvCharRemap"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvFont,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=add_char_remap,
    )

    source: int = __dearpypixl__.set_configuration(None, None)
    target: int = __dearpypixl__.set_configuration(None, None)

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


class FontRange(Item):
    """Adds a range of font characters to a font.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFontRange, "mvFontRange"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvFont,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=add_font_range,
    )
    first_char: int = __dearpypixl__.set_configuration(None, None)
    last_char : int = __dearpypixl__.set_configuration(None, None)

    def __init__(
        self,
        first_char        : int                   ,
        last_char         : int                   ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Item | int      = 0   ,
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
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFontRangeHint, "mvFontRangeHint"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvFont,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=add_font_range_hint,
    )
    hint: int  = __dearpypixl__.set_configuration(None, "set_item_config")

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




class FontRegistry(Item):
    """Adds a font registry.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFontRegistry, "mvFontRegistry"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvFont,),
        command=add_font_registry,
    )
    show: bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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


class Font(LinkedItem):
    """Object-oriented interface for DearPyGui font items.

    NOTE: Per <https://dearpygui.readthedocs.io/en/latest/documentation/fonts.html
    #readme-first>, remapping characters or adding characters or ranges to a font
    item will cause the font texture to be rebuilt. Loading or editing fonts at runtime
    will affect performance.

    NOTE: Attempting to create fonts of unusually large size (~+300, varies depending
    on the font used) can cause a segmentation fault.
    """
    __slots__ = ("_identity_tag",)
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFont, "mvFont"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvFontRegistry,),
        command=add_font,
        able_children=(
            dearpygui.mvFontChars,
            dearpygui.mvFontRange,
            dearpygui.mvCharRemap,
            dearpygui.mvFontRangeHint,
            dearpygui.mvTemplateRegistry,
        )
    )

    _bind = bind_item_font

    CATEGORY = True

    FONT_SIZE: float = 12.0
    AUTO_UUID: int   = _dearpygui.mvReservedUUID_0  # 10

    def __init__(
        self,
        file : Filepath,
        size : float   = FONT_SIZE,
        label: str     = None,
        *,
        user_data         : Any                               = None,
        use_internal_label: bool                              = True,
        parent            : Item | int                        = AUTO_UUID,
        **kwargs
    ) -> None:
        """Args:
            * file (str): Path pointing to a font file. Supports '.otf' and '.ttf' files.

            * size (float, optional): Size of the font.

            * label (str, optional): Display name for the item. Defaults to None.

            The following are optional, keyword-only arguments:

            * user_data (Any): Passed as the third positional argument to related callbacks.
            Defaults to None.

            * use_internal_label (bool): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.

            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
        """
        super().__init__(
            file=str(file),
            size=float(size),
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )

    file: str   = __dearpypixl__.set_configuration(None, None)
    size: float = __dearpypixl__.set_configuration(None, None)


FontRegistry(tag=Font.AUTO_UUID)  # default font registry




def _setvalue_setter(item, name, value):
    setattr(item, name, UpdaterSet(value, getattr(item, name).callback))

def _size_setter(fontitem: "Font", name, value: float):
    ...


class FontFamily(ItemType):
    """A collection of font items created from a single font file. Font instances
    created through this item will use this item's configuration, and any updates
    made to this item's configuration are applied to all fonts in the collection.
    Bound items will always use the active font size.
    """
    # NOTE: FontFamily instances are not managed by the registry.
    __slots__ = (
        "_tag",
        "_addtl_chars",
        "_char_remaps",
        "_char_ranges",
        "_range_hints",
        "_sizes",
    )
    __dearpypixl__ = ItemData(
        identity=ItemData.AUTO,
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
    )

    _bind = None

    CATEGORY: Font = Font.CATEGORY

    file       : str                     = __dearpypixl__.set_configuration(None, None)
    size       : float                   = __dearpypixl__.set_configuration(None, None)
    addtl_chars: set[int]                = __dearpypixl__.set_configuration(getattr, _setvalue_setter, target="_addtl_chars")
    char_remaps: set[tuple[int, int]]    = __dearpypixl__.set_configuration(getattr, _setvalue_setter, target="_char_remaps")
    char_ranges: set[tuple[int, int]]    = __dearpypixl__.set_configuration(getattr, _setvalue_setter, target="_char_ranges")
    range_hints: set[FontRangeHintValue] = __dearpypixl__.set_configuration(getattr, _setvalue_setter, target="_range_hints")

    def __init__(
        self,
        file : Filepath,
        size : float   = Font.FONT_SIZE,
        label: str     = None,
        *,
        addtl_chars       : Sequence[int]                      = (),
        char_remaps       : Sequence[tuple[int, int]]          = (),
        char_ranges       : Sequence[tuple[int, int]]          = (),
        range_hints       : Sequence[FontRangeHintValue | int] = (),
        user_data         : Any                                = None,
        use_internal_label: bool                               = True,
        **kwargs
    ) -> None:
        """Args:
            * file (str): Path pointing to a font file. Supports '.otf' and '.ttf' files.

            * size (float, optional): An initial Font instance of this size will be created.
            Bound items will reflect this font.

            * label (str, optional): Display name for the item. Defaults to None.

            The following are optional, keyword-only arguments:

            * addtl_chars (Sequence[int]): Additional characters/glyphs to add to the font.

            * char_remaps (Sequence[tuple[int, int]]): A sequence containing `(source, target)`
            pairs where the <source> character is remapped to the <target> character.

            * char_ranges (Sequence[tuple[int, int]]): A sequence containing `(first, last)`
            pairs where all characters from <first> to <last> are added to the font.

            * range_hint (FontRangeHintValue | int): ...

            * user_data (Any): Passed as the third positional argument to related callbacks.
            Defaults to None.

            * use_internal_label (bool): If True, `##{self.tag}` will be appended to the
            item's label (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.
        """
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )

        self._sizes: dict[float, int] = {}
        self._font_tag = ...

        self._file = str(file)
        self._size = float(size)
        self._addtl_chars = UpdaterSet(addtl_chars, )
        self._char_remaps = UpdaterSet(char_remaps, )
        self._char_ranges = UpdaterSet(char_ranges, )
        self._range_hints = UpdaterSet(range_hints, )
        self(size)

    def __call__(self, size: float):
        """Return a Font instance of <size>, creating it if it doesn't exist.
        """
        if not size:
            raise ValueError("Invalid `size`.")
        size = float(size)

        font_uuid = self._sizes.get(size, None)
        if font_uuid and does_item_exist(font_uuid):
            del self._sizes[font_uuid]
            font_uuid = None

        if not font_uuid:
            font_item = Font(
                self._file,
                size,
                self.label,
                addtl_chars=self._addtl_chars,
                char_ranges=self._char_ranges,
                range_hints=[int(h) for (h) in self._range_hints],
                parent=self,
            )
            self._sizes[size] = font_item.tag
        else:
            font_item = registry.get_item(font_uuid)

        if font_item != self._font_tag:
            self._font_tag = font_item
            self.bind(*self.bound_items())

        return font_item

    def tag(self) -> int:
        return self._tag

    def _destroy_ft_children(self, itemtype: type[FontChars | FontCharRemap | FontRange | FontRangeHint]):
        for font_item in self.children(1):
            for ft_child in font_item.children(1):
                if isinstance(ft_child, itemtype):
                    ft_child.delete(__refresh=False)
        registry.refresh()

    def _upd_fonts_addtl_chars(self):
        self._destroy_ft_children(FontChars)
        for font_item in self.children(1):
            FontChars(self._addtl_chars, parent=font_item)

    def _upd_fonts_char_remaps(self):
        self._destroy_ft_children(FontCharRemap)
        for font_item in self.children(1):
            for pair in self._char_remaps:
                FontCharRemap(*pair, parent=font_item)

    def _upd_fonts_char_ranges(self):
        self._destroy_ft_children(FontRange)
        for font_item in self.children(1):
            for pair in self._char_ranges:
                FontRange(*pair, parent=font_item)

    def _upd_fonts_range_hints(self):
        self._destroy_ft_children(FontRangeHint)
        for font_item in self.children(1):
            for hint in self._range_hints:
                FontRangeHint(hint, parent=font_item)

    def bind(self, *item: Item):
        font_item = registry.get_item(self._font_tag)
        return font_item.bind(*item)

    @classmethod
    def unbind(cls, *item: Item):
        return cls.CATEGORY.unbind(*item)
