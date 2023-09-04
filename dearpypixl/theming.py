import types
import enum
import functools
import itertools  # type: ignore
import os
from dearpygui import dearpygui
from ._dearpypixl.common import (
    Any,
    Item,
    overload,
)
from . import items, color, style
from ._dearpypixl import api, interface, tools
from ._dearpypixl.api import Registry as RegistryAPI, Item as ItemAPI




# TODO: re-implement ez-theme

Theme = items.Theme



class FontRangeHint(enum.Enum):
    # XXX I suspect that the internal structure accepting characters expects
    # unsigned shorts. Characters exceeding a value of 65535 (some below)
    # are seemingly ignored.

    DEFAULT = tuple(range(0x0000, 0x00ff))  # basic Latin + Latin, 0x1 Supplement
    LATIN = tuple(itertools.chain(
        range(0x0100 , 0x017F  + 1),     # Latin Extended A
        range(0x0180 , 0x024F  + 1),     # Latin Extended B
        range(0x0250 , 0x02AF  + 1),     # IPA Extensions
        range(0x02B0 , 0x02FF  + 1),     # Spacing Modifier Letters
        range(0x1D00 , 0x1D7F  + 1),     # Phonetic Extensions
        range(0x1D80 , 0x1DBF  + 1),     # Phonetic Extensions Supplement
        range(0x1E00 , 0x1EFF  + 1),     # Latin Extended Additional
        range(0x2070 , 0x209F  + 1),     # Superscripts and Subscripts
        range(0x2100 , 0x214F  + 1),     # Letterlike Symbols
        range(0x2150 , 0x218F  + 1),     # Number Forms
        range(0x2C60 , 0x2C7F  + 1),     # Latin Extended C
        range(0xA720 , 0xA7FF  + 1),     # Latin Extended D
        range(0xAB30 , 0xAB6F  + 1),     # Latin Extended E
        range(0xFB00 , 0xFB4F  + 1),     # Alphabetic Presentation Forms (Latin ligatures)
        range(0xFF00 , 0xFFEF  + 1),     # Halfwidth and Fullwidth Forms
        range(0x10780, 0x107BF + 1),     # Latin Extended F
        range(0x1DF00, 0x1DFFF + 1),     # Latin Extended G
    ))
    JAPANESE = tuple(itertools.chain(
        # Hiragana
        range(0x3041, 0x3096 + 1),
        # Katakana
        range(0x30a0, 0x30ff + 1),   # full-width
        range(0xff5f, 0xff9f + 1),   # half-width (+punctuation)
        # Kanji
        range(0x3400, 0x4db5 + 1),
        range(0x4e00, 0x9fcb + 1),
        range(0xF900, 0xFA6A + 1),
        range(0x2e80, 0x2fd5 + 1),  #  radicals
        range(0x3000, 0x303f + 1),  # |
        range(0x31f0, 0x31ff + 1),  # |- symbols, punctuation, & misc characters
        range(0x3220, 0x3243 + 1),  # |
        range(0x3280, 0x337F + 1),  # |
    ))
    KOREAN = tuple(itertools.chain(
        range(0x2000, 0x4000 + 1),
        range(0x5B00, 0x5F00 + 1),
        range(0x7B00, 0x7D00 + 1),
        range(0xA000, 0xA100 + 1),
        range(0xA700, 0xA900 + 1),
        range(0xB600, 0xB700 + 1),
        range(0x2010, 0x2011 + 1),
        range(0x2014, 0x2015 + 1),
        range(0x2018, 0x2019 + 1),
        range(0x201C, 0x201D + 1),
        range(0x2020, 0x2021 + 1),
        range(0x2025, 0x2026 + 1),
        range(0x2032, 0x2033 + 1),
        range(0x3001, 0x3003 + 1),
        range(0x3008, 0x3011 + 1),
        range(0x3014, 0x3015 + 1),
        range(0x3141, 0x3142 + 1),
        range(0x3147, 0x3148 + 1),
        range(0x314A, 0x314E + 1),
        range(0xAC00, 0xD7A3 + 1),
        range(0xFF01, 0xFF03 + 1),
        range(0xFF05, 0xFF0A + 1),
        range(0xFF0C, 0xFF0F + 1),
        range(0xFF1A, 0xFF1B + 1),
        range(0xFF1F, 0xFF20 + 1),
        range(0xFF3B, 0xFF3D + 1),
        (0xBF00, 0x2030, 0x203B, 0x203E,
         0x20AC, 0x301C, 0x30FB, 0x3131,
         0x3134, 0x3137, 0x3139, 0x3145,
         0xFF3F, 0xFF5B, 0xFF5D),
    ))
    CHINESE = tuple(itertools.chain(
        range(0x4E00, 0x9FFF + 1),  # CJK Unified Ideographs
        range(0x2f00, 0x2fdf + 1),  # CJK/Kangxi Radicals
        range(0x2e80, 0x2EFF + 1),  # CJK Radicals Supplement
        range(0x3000, 0x303F + 1),  # CJK symbols & punctuation
    ))
    CHINESE_SIMPLIFIED_COMMON = CHINESE
    CHINESE_FULL = tuple(itertools.chain(
        range(0x3400 , 0x4DBF  + 1),  # CJK Unified Ideographs Extension A      (rare)
        range(0x20000, 0x2A6DF + 1),  # CJK Unified Ideographs Extension B      (rare, historic)
        range(0x2A700, 0x2B73F + 1),  # CJK Unified Ideographs Extension C      (rare, historic)
        range(0x2B740, 0x2B81F + 1),  # CJK Unified Ideographs Extension D      (uncommon, some in current use)
        range(0x2B820, 0x2CEAF + 1),  # CJK Unified Ideographs Extension E      (rare, historic)
        range(0x2CEB0, 0x2EBEF + 1),  # CJK Unified Ideographs Extension F      (rare, historic)
        range(0x30000, 0x3134F + 1),  # CJK Unified Ideographs Extension G      (rare, historic)
        range(0x31350, 0x323AF + 1),  # CJK Unified Ideographs Extension H      (rare, historic)
        range(0xF900 , 0xFAFF  + 1),  # CJK Compatibility Ideographs            (duplicates, unifiable variants, corporate characters)
        range(0x2F800, 0x2FA1F + 1),  # CJK Compatibility Ideographs Supplement (unifiable variants)
    ))
    CYRILLIC = tuple(itertools.chain(
        range(0x0400 , 0x04FF  + 1),  # basic (256 characters)
        range(0x0500 , 0x052F  + 1),  # Supplement
        range(0x2DE0 , 0x2DFF  + 1),  # Ext-A
        range(0xA640 , 0xA69F  + 1),  # Ext-B
        range(0x1C80 , 0x1C8F  + 1),  # Ext-C
        range(0x1E030, 0x1E08F + 1),  # Ext-D
        range(0xFE2E , 0xFE2F  + 1),  # Combining Half Marks
        range(0x1D2B , 0x1D78  + 1),  # Phonetic Extensions
    ))
    THAI = tuple(range(0x0e00, 0x0e7f + 1))
    VIETNAMESE = tuple(itertools.chain(
        range(0x0020, 0x002F + 1),
        range(0x0030, 0x0039 + 1),
        range(0x003A, 0x0040 + 1),
        range(0x0041, 0x005A + 1),
        range(0x005B, 0x0060 + 1),
        range(0x0061, 0x007A + 1),
        range(0x007B, 0x007E + 1),
        range(0x00C0, 0x00C3 + 1),
        range(0x00C8, 0x00CA + 1),
        range(0x00CC, 0x00CD + 1),
        range(0x00D2, 0x00D5 + 1),
        range(0x00D9, 0x00DA + 1),
        range(0x00E0, 0x00E3 + 1),
        range(0x00E8, 0x00EA + 1),
        range(0x00EC, 0x00ED + 1),
        range(0x00F2, 0x00F5 + 1),
        range(0x00F9, 0x00FA + 1),
        range(0x0102, 0x0103 + 1),
        range(0x0110, 0x0111 + 1),
        range(0x0128, 0x0129 + 1),
        range(0x0168, 0x0169 + 1),
        range(0x01A0, 0x01B0 + 1),
        range(0x1EA0, 0x1EF9 + 1),
        range(0x02C6, 0x0323 + 1),
        (0x00DD, 0x00FD, 0x00D0),
    ))
    ALL = tuple(range(256, 0xffff + 1))

    @classmethod
    def _missing_(cls, value: Any) -> 'FontRangeHint | None':
        return _MVFRH_TO_PXFRH.get(value, None)


_MVFRH_TO_PXFRH: dict[int, FontRangeHint] = {  # helper for `FontRangeHint._missing_`
    dearpygui.mvFontRangeHint_Default                  : FontRangeHint.DEFAULT,
    dearpygui.mvFontRangeHint_Japanese                 : FontRangeHint.JAPANESE,
    dearpygui.mvFontRangeHint_Korean                   : FontRangeHint.KOREAN,
    dearpygui.mvFontRangeHint_Chinese_Full             : FontRangeHint.CHINESE_FULL,
    dearpygui.mvFontRangeHint_Chinese_Simplified_Common: FontRangeHint.CHINESE_SIMPLIFIED_COMMON,
    dearpygui.mvFontRangeHint_Cyrillic                 : FontRangeHint.CYRILLIC,
    dearpygui.mvFontRangeHint_Thai                     : FontRangeHint.THAI,
    dearpygui.mvFontRangeHint_Vietnamese               : FontRangeHint.VIETNAMESE,
}





class SizedFont(items.mvFontRegistry):
    """A DearPyGui font registry interface that manages font items of different sizes
    of a specific font.

    A high-level perspective of `pxFont` -- it acts less like a font registry item and more
    like an individual font item.
        >>> font_fpath: str = ""  # "ProggyClean-Black.ttf", etc.
        >>> # include a default size and other sizes
        >>> pc_fonts = pxFonts(font_fpath, 12.0, 14.0, 18.0, default_size=16.0)
        >>> pc_fonts.add_characters(0x2126, 0xfb26)  # 'ohm', 'half-life'
        >>>
        >>> wndw1 = dpg.add_window(label="\\u2126")
        >>> wndw2 = dpg.add_window(label="\\ufb26")
        >>> pc_fonts.bind(wndw1, wndw2)  # multiple items per call

    Want to change the font size? It's your choice of an assignment or method call.
        >>> pc_fonts.size = 12         # rounded down -- sets as 12.0
        >>> pc_fonts.size = 15.08      # rounded down -- sets as 15.0
        >>> pc_fonts.set_size(28.04)   # rounded down -- sets as 28.0

    Since DearPyGui loads glyphs from any new font into a single texture, a font's `size`
    can't actually be updated. Instead, the registry manages individual font items of
    different sizes. When setting the size, it will search its cache for a font of *size*
    and re-bind all bound items to that font item. If a font of of *size* is not cached,
    the registry will create one (using the font file passed on initialization) and cache it
    for future use. Calling the instance and passing a *size* argument will return the a
    `mvFont` interface for the underlying font item of that size.

    Management of additional characters can be done through various `.add_char*` and `.del_char*`
    methods. Adding or removing additional characters, remaps, or range hints will update all
    underlying font items accordingly. A read-only view of additional and remapped characters
    can be accessed through the `.characters` and `.remapped_characters` properties respectively.
    As an implementation detail, `pxFont` does not add range hints or character ranges using
    DearPyGui's `add_font_range` or `add_font_range_hint` functions; character ranges are
    calculated and added to font items as additional characters, while font range hints -- members
    of the 'FontRangeHint' enumeration containing pre-defined character sets -- are handled
    similarly.

    NOTE: Fonts generally do not support all codepoints/glyphs, and many use different
    codepoint-to-glyph mappings. If a glyph/codepoint does not appear in DearPyGui's
    font manager, it's likely that the font does not have a glyph mapped to that codepoint
    (i.e. it's unsupported).
    """
    DEFAULT                   = FontRangeHint.DEFAULT
    LATIN                     = FontRangeHint.LATIN
    JAPANESE                  = FontRangeHint.JAPANESE
    KOREAN                    = FontRangeHint.KOREAN
    CHINESE                   = FontRangeHint.CHINESE                    # |- these are the same
    CHINESE_SIMPLIFIED_COMMON = FontRangeHint.CHINESE_SIMPLIFIED_COMMON  # |
    CHINESE_FULL              = FontRangeHint.CHINESE_FULL
    CYRILLIC                  = FontRangeHint.CYRILLIC
    THAI                      = FontRangeHint.THAI
    VIETNAMESE                = FontRangeHint.VIETNAMESE
    ALL                       = FontRangeHint.ALL

    __glbl_lock  = tools.Lock()
    __glbl_binds = {}

    _font_cache : dict[float, Item]
    _bound_items: frozenset[Item]
    _characters : frozenset[int]
    _char_remaps: dict[int, int]

    def __init__(self, file: str, *sizes: float, label: str = "", default_size: float = 16.0, **kwargs) -> None:
        """Args:
            * file : Path (string) pointing to a .ttf or .otf font file.

            * sizes: Sizes (other than *default_size*) to pre-load.

            * default_size: The initial "active size" for the registry. Defaults to 16.0.
        """
        file = str(file)
        self._filename = file.split(os.sep)[-1]
        super().__init__(label=label or f"pxFont [{self._filename}]", **kwargs)
        ItemAPI.set_alias(self, f"{file}##{self.tag}")

        self._font_cache   = {}
        self._bound_items  = frozenset()
        self._characters   = frozenset()
        self._char_remaps  = {}
        self._active_size  = default_size
        self._font_factory = functools.partial(
            dearpygui.add_font,
            file,
            user_data=self,
            parent=self,
            use_internal_label=True,
        )
        self._get_font_of_size(default_size)
        self.add_sizes(*sizes)

    def __call__(self, size: float) -> items.mvFont:
        return self._get_font_of_size(size)

    def _get_font_of_size(self, size: float) -> items.mvFont:
        try:
            size = float(f"{size:1f}")
        except TypeError:
            raise TypeError(
                f"expected float for `size` (got {type(size).__qualname__!r})."
            ) from None

        if font:=self._font_cache.get(size, None):
            return items.mvFont.new(font)

        font = self._font_factory(
            size,  # type: ignore
            label=f"{self._filename} [{size}]",
        )
        self._font_cache[size] = font
        self._upd_font_details(font)
        return items.mvFont.new(font)

    def _upd_font_details(self, font_item: Item = 0) -> None:
        """Update one or all fonts in the registry."""
        fonts = self._font_cache.values() if not font_item else (font_item,)
        chars = tuple(self.characters)
        for font in fonts:
            RegistryAPI.delete_item(font, children_only=True, slot=1)
            dearpygui.add_font_chars(chars, parent=font)

    def bind(self, *items: Item, app_level: bool = False) -> None:
        """Bind items to the registry and/or set the registry to apply the application-level
        font. They will reflect a font of `self.file` and `self.size`.

        Args:
            * item: Identifiers of items to bind.

            * app_level: If True, the application default font will always be set to a font of
            `self.file` and `self.size`. Default is False.
        """
        self_id = self.tag
        font_id = self._get_font_of_size(self._active_size)
        bound_items   = set(self._bound_items)
        missing_items = set()
        with self.__glbl_lock:
            try:
                for item in items:
                    try:
                        ItemAPI.set_font(item, font_id)
                    except SystemError:
                        if not RegistryAPI.item_exists(item):
                            missing_items.add(item)
                            continue
                        raise
                    bound_items.add(item)
                if app_level:
                    api.Application.set_font(font_id)
            finally:
                self.__glbl_binds.update({item: self_id for item in bound_items})
                for item in missing_items:
                    if item in self.__glbl_binds:
                        del self.__glbl_binds[item]
                self._bound_items = frozenset(bound_items.difference(missing_items))

    def unbind(self, *items: Item, app_level: bool = False) -> None:
        with self.__glbl_lock:
            for item in items:
                try:
                    ItemAPI.set_font(item, 0)
                except SystemError:
                    pass
            if app_level:
                api.Application.set_font(0)
            for item in items:
                if item in self.__glbl_binds:
                    del self.__glbl_binds[item]
            self._bound_items = self._bound_items.difference(items)

    @property
    def file(self) -> str:
        """[get] Return the file used for fonts created and parented by the
        registry.
        """
        return self.alias.split("##")[0]  # type: ignore


    @property
    def characters(self) -> frozenset[int]:
        """[get] Return all additional font characters in the registry."""
        return self._characters

    def add_characters(self, *characters: int) -> None:
        """Add additional characters to the registry.

        Args:
            * characters: Codepoints (unicode) to add.
        """
        self._characters = self._characters.union(characters)
        self._upd_font_details()

    def del_characters(self, *characters: int) -> None:
        """Remove characters formerly added from the registry.

        Characters that are not additonally added are ignored.
        """
        self._characters = self._characters.difference(characters)
        self._upd_font_details()

    def add_char_range(self, start: int, stop: int) -> None:
        """Add a range of characters to the registry."""
        # XXX `add_font_range` "items" are not used because;
        #   - glyphs added this way can be accessed only by viewing them in the
        #   font manager (cannot query DPG)
        #   - it reduces item/uuid bloat
        #   - simplifies pxFont structure
        self.add_characters(*(c for c in range(start, stop)))

    def del_char_range(self, start: int, stop: int) -> None:
        """Remove a range of characters formerly added to the registry.

        Characters that are not additonally added are ignored.
        """
        self.del_characters(*(c for c in range(start, stop)))

    def add_char_hint(self, range_hint: int | FontRangeHint) -> None:
        """Add characters to the registry from a pre-defined arrangement.

        Args:
            * range_hint: A member of `FontRangeHint` or a DearPyGui "mvFontRangeHint_*"
            constant.
        """
        # XXX `add_font_range_hint` "items" are not used because;
        #   - glyphs added from those hints do not show in the font manager
        #   - it reduces item/uuid bloat
        #   - simplifies pxFont structure
        try:
            characters = FontRangeHint(range_hint).value
        except TypeError:
            raise TypeError(
                f"expected `int`, `FontRangeHint` member (got {type(range_hint).__qualname__!r})."
            ) from None
        self.add_characters(*characters)  # type: ignore

    def del_char_hint(self, range_hint: int | FontRangeHint) -> None:
        """Remove characters formerly added to the registry from a pre-defined
        arrangement.

        Args:
            * range_hint: A member of `FontRangeHint` or DearPyGui "mvFontRangeHint_*"
            integer constant.
        """
        try:
            characters = FontRangeHint(range_hint).value
        except TypeError:
            raise TypeError(
                f"expected `int`, `FontRangeHint` member (got {type(range_hint).__qualname__!r})."
            ) from None
        self.del_characters(*characters)  # type: ignore


    @property
    def remapped_characters(self) -> types.MappingProxyType[int, int]:
        """[get] Return a mapping of remapped characters."""
        return types.MappingProxyType(self._char_remaps)

    def add_remapped_char(self, character: int, new_character: int) -> None:
        """Remap an existing character to a new one."""
        self._char_remaps[character] = new_character
        self._upd_font_details()

    def del_remapped_char(self, *characters: int) -> None:
        """Restore the original mapping of a remapped character.

        Ignores characters that are not remapped.
        """
        for c in characters:
            self._char_remaps.pop(c, None)
        self._upd_font_details()


    @property
    def size(self) -> float:
        """[get] Return the size currently in use by items bound to the registry."""
        return self._active_size
    @size.setter
    def size(self, value: float):
        """[set] Set the active font size for items bound to the registry."""
        self.set_size(value)

    def set_size(self, size: float) -> None:
        """Set the active font size for items bound to the registry."""
        self._active_size = size
        self.bind(*self._bound_items, app_level=True if api.Application.get_font() == self else False)

    @property
    def sizes(self) -> tuple[float, ...]:
        """[get] Return all font sizes loaded in the registry."""
        return tuple(sorted(self._font_cache))

    def add_sizes(self, *sizes: float) -> None:
        """Ensure that font items of *sizes* exist in the registry. Useful for
        "pre-loading" font items.

        This method exists for convenience -- the registry creates font items
        automatically as necessary.
        """
        for size in sizes:
            self._get_font_of_size(size)

    @overload
    def add_size_range(self, stop: float, /) -> None: ...
    @overload
    def add_size_range(self, start: float, stop: float, step: float = 1.0) -> None: ...
    def add_size_range(self, start: float, stop: float | None = None, step: float = 1.0) -> None:
        """Create missing font items from a range of sizes. Useful for
        "pre-loading" font items.

        This method exists for convenience -- the registry creates font items
        automatically as necessary."""
        if stop is None:
            rng = range(start)  # type: ignore
        else:
            i = start
            rng = []
            while i < stop:
                rng.append(i)
                i += step
        self.add_sizes(*rng)
