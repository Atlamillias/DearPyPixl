import typing
import threading

from dearpygui import _dearpygui

from dearpypixl.core.protocols import Item, Array
from dearpypixl.core import appitem
from dearpypixl.core import management
from dearpypixl.lib.items import (
    mvThemeComponent,
    mvThemeColor,
    mvThemeStyle,
    mvFontRegistry,
    mvFont,
)
from dearpypixl.lib import application
from dearpypixl import color
from dearpypixl import style


__all__ = (
    "ElementProperty", "color_property", "style_property",
    "SizedFont",  "add_sized_font",
)




# [ ElementProperty ]

class ElementProperty[T: Array[int | float, typing.Literal[2]] | Array[int, typing.Literal[3, 4]], R: mvThemeColor | mvThemeStyle]:
    __slots__ = ("_name", "_type", "_default", "_factory",)

    @typing.overload
    def __init__(self, default: T, factory: typing.Callable[..., R] = ..., /) -> None: ...
    @typing.overload
    def __init__(self, default: T, cls: type[R], category: int, target: int) -> None: ...
    def __init__(self, default, obj = None, category = None, target = None, /):
        self._default = default
        self._factory = (obj, category, target)

    def __set_name__(self, cls: type[mvThemeComponent], name: str, /) -> None:
        obj, category, target = self._factory  # type: ignore

        if obj is None:
            color_factory = getattr(color, name, None)
            style_factory = getattr(style, name, None)

            if color_factory is not None:
                assert style_factory is None
                self._factory = color_factory
                self._type = mvThemeColor
            elif style_factory is not None:
                self._factory = style_factory
                self._type = mvThemeStyle
            else:
                raise RuntimeError(f"could not find appropriate factory named {name!r}")

        elif category is None:
            assert callable(obj)
            self._factory = obj

        elif issubclass(obj, mvThemeColor):

            def _factory(value, *, parent=0, tag=0, __type=obj, __category=category, __target=target):
                return __type.create(__target, value, category=__category, parent=parent, tag=tag)

            self._factory = _factory
            self._type = obj

        else:
            assert issubclass(obj, mvThemeStyle)

            def _factory(value, *, parent=0, tag=0, __type=obj, __category=category, __target=target):
                return __type.create(__target, *value, category=__category, parent=parent, tag=tag)

            self._factory = _factory
            self._type = obj

        self._name = name

    def _get_element_item(self, instance: mvThemeComponent, /) -> R:
        alias = f'mvThemeComponent<{instance.tag}>.{self._name}'
        item = _dearpygui.get_alias_id(alias)
        if not item:
            item = self._factory(self._default, parent=instance, tag=alias)  # ty:ignore[call-non-callable]
            try:
                self._type
            except AttributeError:
                self._type = type(item)
        else:
            item = self._type(tag=item)

        return item  # ty:ignore[invalid-return-type]

    @typing.overload
    def __get__(self, obj: None = None, cls: type | None = None, /) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: mvThemeComponent, cls: type | None = ..., /) -> R: ...
    def __get__(self, instance: mvThemeComponent | None = None, cls = None, /):
        if instance is None:
            return self
        return self._get_element_item(instance)

    def __set__(self, instance: mvThemeComponent, value: T, /) -> None:
        item = self._get_element_item(instance)
        item.value = value

    def __delete__(self, instance: mvThemeComponent, /) -> None:
        try:
            _dearpygui.delete_item(f'mvThemeComponent<{instance.tag}>.{self._name}', children_only=False, slot=-1)
        except SystemError:
            pass

@typing.overload
def color_property(default: Array[int, typing.Literal[3, 4]] = ..., /) -> ElementProperty[Array[int, typing.Literal[3, 4]], mvThemeColor]: ...
@typing.overload
def color_property(name: str, default: Array[int, typing.Literal[3, 4]] = ..., /) -> ElementProperty[Array[int, typing.Literal[3, 4]], mvThemeColor]: ...
def color_property(obj = None, default = (0, 0, 0, -255), /):
    """Lazy descriptor for :py:class:`mvThemeComponent` subclasses. The descriptor
    uses a :py:class:`mvThemeColor` factory function from the :py:module:`color`
    module with the same name as *name* (if omitted, the name of the variable
    bound to the descriptor object is used, instead). On instance lookup, the
    function is invoked to create a :py:class:`mvThemeColor` item and interface unique
    to the :py:class:`mvThemeComponent` instance if it does not exist.

    The descriptor implements the following methods:

    - ``__get__()``: Returns a :py:class:`mvThemeColor` item interface.

    - ``__set__()``: Set the **value** of the associated :py:class:`mvThemeColor` item/interface.

    - ``__delete__()``: Destroys the :py:class:`mvThemeColor` item. It may be re-created via a `__get__()` or `__set__()` operation.

    .. code-block:: python3
        :emphasize-lines: 18

        class ThemeComponent(mvThemeComponent):
            __slots__ = ()

            # factory == `color.window_bg()`
            window_bg = color_property()

            # factory == `color.button()`
            button_bg = color_property("button", (255, 0, 0, 255))

        with mvTheme() as theme:
            color_component = ThemeComponent.create()

            # creates the item (first access) and updates the value
            color_component.window_bg = [200, 200, 200, 255]

            # creates the item (first access) and update the alpha channel
            color_component.button_bg[-1] = 120

    """
    if obj is None:
        return ElementProperty(default)

    if isinstance(obj, str):
        try:
            factory = getattr(color, obj)
        except AttributeError:
            raise ValueError(f"could not find appropriate theme color factory named {obj!r}")

        return ElementProperty(default, factory)

    return ElementProperty(obj)

@typing.overload
def style_property(default: Array[int | float, typing.Literal[2]] = ..., /) -> ElementProperty[Array[int | float, typing.Literal[2]], mvThemeStyle]: ...
@typing.overload
def style_property(name: str, default: Array[int | float, typing.Literal[2]] = ..., /) -> ElementProperty[Array[int, typing.Literal[3, 4]], mvThemeStyle]: ...
def style_property(obj = None, default = (1, -1), /):
    """Lazy descriptor for :py:class:`mvThemeComponent` subclasses. The descriptor
    uses a :py:class:`mvThemeStyle` factory function from the :py:module:`style`
    module with the same name as *name* (if omitted, the name of the variable
    bound to the descriptor object is used, instead). On instance lookup, the
    function is invoked to create a :py:class:`mvThemeStyle` item and interface unique
    to the :py:class:`mvThemeComponent` instance if it does not exist.

    The descriptor implements the following methods:

    * ``__get__()``: Returns a :py:class:`mvThemeStyle` item/interface.

    * ``__set__()``: Set the **value** of the associated :py:class:`mvThemeStyle` item/interface.

    * ``__delete__()``: Destroys the :py:class:`mvThemeStyle` item. It may be re-created via a `__get__()` or `__set__()` operation.

    .. code-block:: python3
        :emphasize-lines: 18

        class ThemeComponent(mvThemeComponent):
            __slots__ = ()

            # factory == `style.window_bg()`
            window_bg = style_property()

            # factory == `style.button()`
            button_bg = style_property("button", (255, 0, 0, 255))

        with mvTheme() as theme:
            style_component = ThemeComponent.create()

            # creates the item (first access) and updates the value
            style_component.window_bg = [200, 200, 200, 255]

            # creates the item (first access) and update the alpha channel
            style_component.button_bg[-1] = 120

    """
    if obj is None:
        return ElementProperty(default)

    if isinstance(obj, str):
        try:
            factory = getattr(style, obj)
        except AttributeError:
            raise ValueError(f"could not find appropriate theme style factory named {obj!r}")

        return ElementProperty(default, factory)

    return ElementProperty(obj)




# [ SizedFont ]

class _FontCommand(typing.Protocol):
    def __call__(self, file: str, size: typing.Any, /, *, parent: Item = ..., tag: Item = ...) -> int | str: ...


class SizedFont(appitem.CompositeItem, mvFontRegistry):
    _file: str

    @property
    def file(self, /) -> str:
        return self._file

    _size: int

    @property
    def size(self) -> int:
        """[**get**, **set**] the current font size."""
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
    def create(cls, /, file: str, size: int = 16, *, item_factory: _FontCommand = mvFont.create, label: str | None = None, user_data: typing.Any = None, use_internal_label: bool = True, tag: int | str = 0, show: bool = True, **kwargs) -> typing.Self:   # pyright: ignore[reportIncompatibleMethodOverride]  # ty:ignore[invalid-method-override]
        self = super().create(
            label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show
        )

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


@management.cast_signature(SizedFont.create)
def add_sized_font(*args, **kwargs):
    return SizedFont.create(*args, **kwargs)
