import typing
import functools
import threading

from dearpygui import _dearpygui
from dearpygui.dearpygui import (
    bind_font, bind_item_font,
    bind_theme, bind_item_theme,
)
assert getattr(bind_font, "_patched", True)
assert getattr(bind_theme, "_patched", True)

from dearpypixl.core.protocols import Item, property
from dearpypixl.core import itemtype
from dearpypixl.core import parsing
from dearpypixl.core import codegen
from dearpypixl.items import (
    mvTheme, theme, add_theme,
    mvThemeComponent, theme_component, add_theme_component,
    mvThemeColor, add_theme_color,
    mvThemeStyle, add_theme_style,
    mvFontRegistry, font_registry, add_font_registry,
    mvFont, font, add_font,
    mvFontRange, add_font_range,
    mvFontRangeHint, add_font_range_hint,
    mvCharRemap, add_char_remap,
)
from dearpypixl import application
from dearpypixl import color
from dearpypixl import style


__all__ = (
    # dearpygui
    "bind_font", "bind_item_font",
    "bind_theme", "bind_item_theme",
    # dearpypixl
    "color", "style",
    "mvTheme", "theme", "add_theme",
    "mvThemeComponent", "theme_component", "add_theme_component",
    "mvThemeColor", "add_theme_color",
    "mvThemeStyle", "add_theme_style",
    "mvFontRegistry", "font_registry", "add_font_registry",
    "mvFont", "font", "add_font",
    "mvFontRange", "add_font_range",
    "mvFontRangeHint", "add_font_range_hint",
    "mvCharRemap", "add_char_remap",
    # module
    "ColorComponent", "add_color_component", "color_component_type",
    "StyleComponent", "add_style_component", "style_component_type",
    "SizedFont",  "add_sized_font",
)




# [ mvThemeComponent extensions ]

if typing.TYPE_CHECKING:
    class ElementComponent(mvThemeComponent):
        __slots__ = ()
        def __getattr__(self, name: str, /) -> itemtype.ElementItem: ...
else:
    class ElementComponent(mvThemeComponent):
        __slots__ = ()

@functools.cache
def _build_component_type(default_value: tuple[float, ...], *elements) -> type[ElementComponent]:
    class ElementComponent(mvThemeComponent):
        __slots__ = ()

    annotations = ElementComponent.__annotations__
    for func in elements:
        name = func.__name__
        setattr(ElementComponent, name, _build_element_property(func, default_value))
        annotations[name] = itemtype.ElementItem[typing.Any, int | float]

    return ElementComponent  # pyright: ignore[reportReturnType]

@functools.cache
def _build_element_property(factory, default_value: tuple[float, ...], /):
    name = factory.__name__

    def fget(self: int, /, *, name=name, factory=factory, item_type=itemtype.ElementItem, default_value=default_value):
        alias = f'{name}<{self.real}>'
        item = _dearpygui.get_alias_id(alias)
        if not item:
            item = factory(default_value, parent=self, tag=alias)
        return item_type(tag=item)

    def fset(self: int, value: typing.Sequence[int | float], /, *, name=name, factory=factory) -> None:
        alias = f'{name}<{self.real}>'
        item = _dearpygui.get_alias_id(alias)
        if not item:
            factory(value, parent=self, tag=alias)
        else:
            _dearpygui.set_value(item, value)

    def fdel(self: int, /, *, name=name) -> None:
        try:
            _dearpygui.delete_item(f'{name}<{self.real}>', children_only=False, slot=-1)
        except SystemError:
            pass

    del name, factory, default_value

    return property(fget, fset, fdel)

def _get_element_functions(
    namespace,
    elem_info: typing.Iterable[parsing.ThemeElementInfo],
    elements: typing.Iterable | None = None,
    /
):
    if elements is None:
        elements = (getattr(namespace, info.func_name) for info in elem_info)
    else:
        module = namespace.__name__
        elements, seen, _elements = [], set(), elements

        for func in _elements:
            if func in seen:
                continue

            if isinstance(func, str):
                name = func
                func = getattr(namespace, func)
            elif func.__module__ != module:
                raise ValueError(f"must be a function [name] in the {module!r} module — got {func}")
            else:
                name = func.__name__

            seen.add(name)
            seen.add(func)
            elements.append(func)

    return sorted(elements, key=lambda fn: fn.__name__)




def color_component_type(elements: typing.Iterable | None = None, /) -> type[ElementComponent]:
    return _build_component_type(
        (0, 0, 0, 255),
        *_get_element_functions(color, parsing.theme_color_info().values(), elements)
    )

def add_color_component(item_type: int = 0, **kwargs) -> ColorComponent:
    return ColorComponent.create(**kwargs)


def style_component_type(elements: typing.Iterable | None = None, /) -> type[ElementComponent]:
    return _build_component_type(
        (1, -1),
        *_get_element_functions(style, parsing.theme_style_info().values(), elements)
    )

def add_style_component(item_type: int = 0, **kwargs) -> StyleComponent:
    return StyleComponent.create(**kwargs)


if typing.TYPE_CHECKING:
    class ColorComponent(mvThemeComponent):
        __slots__ = ()
        def __getattr__(self, name: str, /) -> itemtype.ElementItem: ...

    class StyleComponent(mvThemeComponent):
        __slots__ = ()
        def __getattr__(self, name: str, /) -> itemtype.ElementItem: ...
else:
    ColorComponent = color_component_type()
    ColorComponent.__name__ = "ColorComponent"
    StyleComponent = style_component_type()
    StyleComponent.__name__ = "StyleComponent"




# [ SizedFont ]

class _FontCommand(typing.Protocol):
    def __call__(self, file: str, size: typing.Any, /, *, parent: Item = ..., tag: Item = ...) -> int | str: ...


class SizedFont(itemtype.CompositeItem, mvFontRegistry):
    _file: str

    @property
    def file(self, /) -> str:
        return self._file

    _size: int

    @property
    def size(self) -> int:
        """[get, set] the current font size."""
        return self._size
    @size.setter
    def size(self, size: int):
        if size < 0:
            raise ValueError("'size' must be greater than zero")

        with self._lock:
            self._size = size
            self._bind_items(self._bindings)

            with application._GLOBAL_LOCK:
                font = application._get_app_font()
                try:
                    bound = font and _dearpygui.get_item_info(font)["parent"] == self.tag
                except SystemError:
                    pass
                else:
                    if bound:
                        application._set_app_font(self.get(size))

    item_factory: _FontCommand

    _lock: threading.Lock
    _bindings: set[Item]

    @classmethod
    def create(cls, /, file: str, size: int = 16, *, item_factory: _FontCommand = mvFont.__itemtype_command__, label: str | None = None, user_data: typing.Any = None, use_internal_label: bool = True, tag: int | str = 0, show: bool = True, **kwargs) -> typing.Self:   # pyright: ignore[reportIncompatibleMethodOverride]
        self = cls(tag=cls.__itemtype_command__(
            label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show
        ))

        self._bindings = set()
        self._lock = threading.Lock()
        self._file = file
        self._size = size
        self.item_factory = item_factory

        return self

    def get(self, size: int, /) -> mvFont:
        # Even though `add_font()`s `size` argument is typed as `int`, it DOES
        # process floats. However, the precision is 1/10 (one decimal position).
        alias = f"SizedFont<{self.real}>[{size}]"

        font = _dearpygui.get_alias_id(alias)
        if not font:
            if size < 0:
                raise ValueError("'size' must be greater than zero")
            font = self.item_factory(self.file, size, parent=self, tag=alias)

        return mvFont(tag=font)

    def __call__(self, size: int, /) -> mvFont:
        return self.get(size)

    def bind(self, /) -> None:
        font = self.get(self._size)
        with application._GLOBAL_LOCK:
            application._set_app_font(font)

    def unbind(self, /) -> None:
        font = self.get(self._size).real
        with application._GLOBAL_LOCK:
            if int(application._get_app_font()) == font:
                application._set_app_font(0)

    def _bind_items(self, items: typing.Collection[Item], /) -> None:
        font = self.get(self._size)
        bind = _dearpygui.bind_item_font

        add_bound = self._bindings.add
        del_bound = self._bindings.discard
        for item in items:
            try:
                bind(item, font)
            except SystemError:
                # assume the item simply doesn't exist (anymore?)
                del_bound(item)
            else:
                add_bound(item)

    def bind_item(self, /, *items: Item) -> None:
        with self._lock:
            self._bind_items(items)

    def _unbind_item(self, /, items: typing.Collection[Item]) -> None:
        bind = _dearpygui.bind_item_font

        for item in items:
            try:
                bind(item, 0)
            except SystemError:
                pass

        self._bindings.difference_update(items)

    @typing.overload
    def unbind_item(self, /, *items: Item) -> None: ...
    @typing.overload
    def unbind_item(self, /, *, all: bool = ...) -> None: ...
    def unbind_item(self, /, *items: Item, all: bool = False) -> None:
        with self._lock:
            if all:
                self._unbind_item(self._bindings)
            else:
                self._unbind_item(items)


@codegen.wrapped(SizedFont.create)
def add_sized_font(*args, **kwargs):
    return SizedFont.create(*args, **kwargs)
