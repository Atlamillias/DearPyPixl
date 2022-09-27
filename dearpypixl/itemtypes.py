"""Extending an existing ItemType is fairly painless and non-restrictive. The most
    important step in ensuring everything will work is including a variable keyword-only
    parameter (i.e. `**kwargs`) in all user-defined `__init__` methods. Ideally, they
    should also be passed to `super().__init__()`.

    >>> class UserWindow(Window):
    ...     def __init__(self, arg1, arg2, **kwargs):
    ...         super().__init__(**kwargs)
    ...         self.attr1 = arg1
    ...         self.attr2 = arg2
    ...

    For most, the above is all that is necessary. Controlling which keyword arguments
    are passed to `super().__init__()` can influence the functionality of some factory
    operations such as `Item.copy()` and item templates, which may be desired in some
    cases. The only requirement is that the constructor simply accepts a variable
    keyword-only argument -- nothing else to it.

    However, things are a bit different if you, for example, want to categorize your
    user-defined attribute as a configuration, information, or state attribute, or include
    an new/existing atribute in the ItemType's `__repr__`. To do something like this, the
    ItemType's metadata must be updated in the class' definition.


    All item types have a `__dearpypixl__` class attribute containing metadata regarding
    the item type. It strongly influences how an ItemType will be created, the behavior of
    its methods, and several other aspects. Typically, its creation is automatic with its
    contents copied from the parent class. It can also be created manually; by assigning
    an instance of `ItemData` (exposed in the `itemtypes` module) to the `__dearpypixl__`
    attribute in the class definition, you have more control of its actual identity.

    >>> class UserWindow(Window):
    ...     # Add attributes to <category>, include in `__repr__`, etc.
    ...
    ...     __dearpypixl__ = ItemData(repr=("hello",))
    ...
    ...     hello = "world"
    ...     foo = __dearpypixl__.as_information("foo", repr=True, value="bar")
    ...
    ...     @property
    ...     @__dearpypixl__.as_information
    ...     def bar(self):
    ...         return "foo"
    ...
    ...     @bar.setter
    ...     def bar(self, value):
    ...         ...

    In the above, the `hello` and `foo` attributes will be included in the repr string
    of UserWindow instances. The `foo` and `bar` attributes will also be included in the
    return of `UserWindow().information()`. The ItemData instance provides three methods
    for categorizing attributes; `as_configuration`, `as_information`, and `as_state`. In
    the first use case of `as_information`, the name of the attribute was included as
    the first argument. Normally, this first argument would be returned back from the
    method. Since a `value` keyword argument was included, "bar" will be returned instead
    -- setting the value of `UserWindow.foo` to "bar". In the second use case, the method
    is used as a decorator around the `bar` method. Unlike the first use of `as_information`
    , the first argument (the attribute name) is infered from the name of the callable. As
    previously mentioned, this argument (the `bar` method) is returned as a result,
    unmodified.

    Categorized membership will persist through subclassing *unless* the member is redefined
    on the subclass. In the example below, a Window subclass redefines the `width` attribute
    (formerly a data descriptor, categorized as configuration). As such, `width` will not
    be included in `UserWindow().configuration()` unless it is re-registered. As a
    consequence, factory operations such as the `copy` method will also not pass `width` to
    the ItemType constructor; a behavior gained from an attribute's inclusion in the
    configuration category.

    >>> class UserWindow(Window):
    ...     __dearpypixl__ = ItemData()
    ...
    ...     width = 100

    Just like redefining any other class member, redefining a categorized attribute removes
    any kind of special handling it had previously as it is no longer inherited from the
    parent class. `UserWindow.width` is just a typical class attribute.

    More examples of this can be found throughout the library within other ItemType
    definitions.

"""
from typing import TypeVar
from os import PathLike
from ._internal import registry
from ._internal.item import (
    ItemT,
    ItemData,
    ItemType,
    AppItem,
    Item,
)
from ._internal.utilities import (
    generate_itemtype_uuid,
    get_reflected_linkeditem,
    auto_itemtype_init,
)
from ._internal.comtypes import Filepath
from .events import ItemEvents
from .theme import Theme
from .font import Font, FontFamily


__all__ = [
    "auto_itemtype_init",
    "generate_itemtype_uuid",

    "ItemT",
    "WidgetItemT",

    "ItemData",

    "ItemType",
    "AppItem",
    "Item",
    "WidgetItem",
]


WidgetItemT  = TypeVar("WidgetItemT", bound='WidgetItem')


class WidgetItem(Item):
    """An extension to the Item class supporting additional features.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(internal_only=True)

    def __init__(
        self,
        font  : Font | FontFamily | Filepath  = None,
        theme : Theme | bool                  = None,
        events: ItemEvents | bool             = None,
        **kwargs
    ):
        """Args:
            * font (Font | FontFamily | str, optional): An existing Font or FontFamily
            item for this item to use. If a path-like string pointing to a font file is
            passed, a new FontFamily item will be created for the item. Defaults to None.

            * theme (Theme | bool, optional): An existing theme for this item to use.
            If True, a new `Theme` instance will be created for the item. Defaults to None.

            * events (ItemEvents | bool, optional): An existing events registry for
            this item to use. If True, a new `ItemEvents` instance will be created for the
            item. Defaults to None.
        """
        super().__init__(**kwargs)

        if theme is True:
            theme = Theme()
        if theme:
            self.theme = theme

        if events is True:
            events = ItemEvents()
        if events:
            self.events = events

    @property
    @__dearpypixl__.as_configuration
    def theme(self) -> Theme | None:
        return registry._items._get_binding_item(Theme.CATEGORY, self)
    @theme.setter
    def theme(self, value: Theme | None) -> None:
        if isinstance(value, Theme):
            value.bind(self)
        else:
            Theme.unbind(self)

    @property
    @__dearpypixl__.as_configuration
    def font(self) -> FontFamily | Font | None:
        return registry._items._get_binding_item(Font.CATEGORY, self)
    @font.setter
    def font(self, value: FontFamily | Font | Filepath | None) -> None:
        match value:
            case FontFamily() | Font():
                value.bind()
            case str() | PathLike():
                FontFamily(value).bind(self)
            case _:
                FontFamily.unbind(self)
                Font.unbind(self)

    @property
    @__dearpypixl__.as_configuration
    def font_size(self) -> float:
        ...

    @property
    @__dearpypixl__.as_configuration
    def events(self) -> ItemEvents | None:
        return registry._items._get_binding_item(ItemEvents.CATEGORY, self)
    @events.setter
    def events(self, value: ItemEvents | None):
        if isinstance(value, ItemEvents):
            value.bind(self)
        else:
            ItemEvents.unbind(self)

    def get_reflected_theme(self) -> Theme:
        """Starting from this item, search upward through the item hierarchy for an item
        bound to a Theme -- return the first Theme item found. If no Theme item is found,
        return the application default Theme item.
        """
        return get_reflected_linkeditem(self, "theme")

    def get_reflected_font(self) -> Font:
        """Starting from this item, search upward through the item hierarchy for an item
        bound to a Font -- return the first Font item found. If no Font item is found,
        return the application default Font item.
        """
        return get_reflected_linkeditem(self, "font")
