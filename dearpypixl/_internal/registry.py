from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    overload,
    final,
    Any,
    Literal,
    Sequence,
    ItemsView,
    KeysView,
    ValuesView,
)
from abc import ABC, abstractmethod
from dearpygui._dearpygui import (
    get_all_items,
    last_container,
    last_item,
    last_root,
)
from .comtypes import ItemRef, NullRef
from .utilities import itemized_return

if TYPE_CHECKING:
    from dearpypixl._internal.item import (
        Item as _Item,
        LinkedItem as _BItem,
    )


__all__ = [
    # registries (read-only)
    "itemtypes",
    "items",
    # convenience callables
    "get_itemtype",
    "get_item",
    "refresh",

    "last_item",
    "last_container",
    "last_root",
]


_NULL = object()



class RegGet:
    __slots__ = ("_mapping",)

    def __init__(self, mapping: dict):
        self._mapping = mapping

    @overload
    def __call__(self, __key: int | str, /) -> Any | None: ...
    @overload
    def __call__(self, __key: int | str, __default: Any, /) -> Any | None: ...
    def __call__(self, __key: int | str, __default: Any = _NULL, /) -> Any | None:
        try:
            return self._mapping[__key]
        except KeyError:
            if __default is not _NULL:
                return __default
            raise


class Registry(ABC, dict):
    def __new__(cls, *args, **kwargs):
        reg_dict = super().__new__(cls, *args, **kwargs)
        reg_dict.get = cls.get(reg_dict)
        return reg_dict





@final
class ItemRegGet(RegGet):
    __slots__ = ()

    def by_tag(self, *tag: ItemRef) -> tuple[_Item]:
        """Return all items with a matching unique identifier.

        Args:
            * tag (int, positional-only): If an item's unique identifier
            matches any of these arguments, it will be included in the return.
        """
        return tuple((item for t in tag if (item:=self(t, None))))

    def by_type(self, *itemtype: type[_Item]) -> tuple[_Item]:
        """Return all items that are of a [derived] type(s).

        Args:
            * itemtype (type[_Item], positional-only): If an item is an instance of
            any of these arguments, it will be included in the return.
        """
        return tuple((item for item in self._mapping.values() if isinstance(item, itemtype)))


@final
class ItemRegistry(Registry):
    get = ItemRegGet

    def __init__(self):
        # BindingItems themselves act as a binding category. The values
        # of each is another mapping. The keys in the nested mapping
        # are the unique identifiers (i.e. "tag") of all living LinkedItem
        # instances of that binding category.
        self.__itembinds: dict[type[_BItem], dict[ItemRef, set[ItemRef]]] = {}

    def refresh(self) -> None:
        """Flush the registry(s) of references to items that no
        longer exist.
        """
        itembinds = self.__itembinds
        live_uuids = get_all_items()
        null_uuids = set(self).difference(live_uuids)
        # items
        for item_uuid in null_uuids:
            if (pixl_item:=self.get(item_uuid, None)) and not pixl_item.is_salvage:
                del self[item_uuid]
        # binds
        for tgt_bind in itembinds:
            binding_items = itembinds[tgt_bind]
            pop_bind_item = binding_items.pop
            # binding items
            for item_uuid in null_uuids:
                pop_bind_item(item_uuid, None)
            # bound items
            for bound_uuids in binding_items.values():
                discard_uuid = bound_uuids.discard
                for item_uuid in null_uuids:
                    discard_uuid(item_uuid)

    def register(self, item: _Item) -> None:
        """Register an ItemType instance."""
        self[item.tag] = item

    def unregister(self, item: _Item) -> None:
        """De-register an ItemType instance."""

    def _register_category(self, target: type[_BItem]) -> None:
        self.__itembinds[target] = {}

    def _register_binding_item(self, binder: _BItem) -> None:
        self.__itembinds[binder.CATEGORY][binder.tag] = set()

    def _set_item_binding(
        self,
        binder: _BItem | type[_BItem],
        item  : _Item,
        *,
        unbind_only: bool = False
    ) -> None:
        # NOTE: If `unbind_only` is True, `binder` does not need to be
        # an instance.
        item_uuid = item.tag
        bound_items = self.__itembinds[binder.CATEGORY]
        # Unbind from any/all other items within the target bind. An item
        # can only be bound to one item-per-itemtype at a time.
        for item_uuids in bound_items.values():
            item_uuids.discard(item_uuid)
        binder._unbind(item_uuid)
        # Bind to the binder.
        if not unbind_only:
            bound_items[binder.tag].add(item_uuid)
            binder._bind(item_uuid, binder.tag)

    def _get_binding_item(self, binder: type[_BItem], item: _Item) -> _BItem:
        item_uuid   = item.tag
        bound_items = self.__itembinds[binder.CATEGORY]
        for binding_uuid, bound_uuids in bound_items.items():
            if item_uuid in bound_uuids:
                return self[binding_uuid]
        return None

    def _get_bound_items(self, binder: _BItem) -> tuple[_Item]:
        bound_items  = self.__itembinds[binder.CATEGORY]
        binding_uuid = binder.tag
        return tuple((self[item_uuid] for item_uuid in bound_items[binding_uuid]))

    def _is_registered_binding_item(self, item: _BItem | type[_BItem]):
        return item.CATEGORY in self.__itembinds




@final
class ItemTypeRegGet(RegGet):
    __slots__ = ()

    def __call__(self, __key: int | str, __default: Any = _NULL, /) -> Any | None:

        try:
            return self._mapping[__key]
        except KeyError:
            try:
                return self.by_typeid_name(__key)[0]
            except IndexError:
                if __default is not _NULL:
                    return __default
                raise

    def by_name(self, name: str, default: Any = _NULL) -> Any | None:
        """Search for an ItemType by its qualname or typename uuid. For example, using
        "Window" OR "mvAppItemType::mvWindowAppItem" as <name> returns the `Window`
        item type.

        Args:
            * name (str): String used for the search.

            * default (Any): If a match is not found using <name>, return this
            instead. KeyError is raised otherwise.
        """
        mapping = self._mapping
        key = self._mapping._typenames.get(name, name)
        try:
            return mapping[key]
        except KeyError:
            if default is not _NULL:
                return default
            raise

    def by_type(self, *itemtype: type[_Item]) -> tuple[type[_Item]]:
        """Return all item types that are of a [derived] type(s).

        Args:
            * itemtype (type[_Item], positional-only): All item types [derived] of any
            of these arguments will be included in the return.
        """
        return tuple((item for item in self._mapping.values() if issubclass(item, itemtype)))

    def by_typeid_number(self, *itemtype_id: int) -> tuple[type[_Item]]:
        """Return all item types with a matching numeric type id.

        Args:
            * itemtype_id (int, positional-only): If an ItemType's type id number
            matches any of these arguments, it will be included in the return.
        """
        return self._by_typeid(0, itemtype_id)

    def by_typeid_name(self, *itemtype_id: str) -> tuple[type[_Item]]:
        """Return all item types with a matching type name id.

        Args:
            * itemtype_id (str, positional-only): If an ItemType's type id name
            matches any of these arguments, it will be included in the return.
        """
        return self._by_typeid(1, itemtype_id)

    def _by_typeid(
        self,
        index: Literal[0, 1],  # `ItemTypeId` index
        itemtype_ids: Sequence[int] | Sequence[str],
    ) -> tuple[type[_Item]]:
        return tuple((item_type for item_type in self._mapping.values()
                      if item_type.__dearpypixl__.identity[index] in itemtype_ids))


@final
class ItemTypeRegistry(Registry):
    def __init__(self):
        # Mapping linking a type name id to an ItemType's qualname i.e.
        # {"mvAppItemType::mvButton": "Button"}.
        self.__typenames: dict[str, str] = {}

    @overload
    def get(self, __key: str, /) -> Any | None: ...
    @overload
    def get(self, __key: str, __default: Any, /) -> Any | None: ...

    get = ItemTypeRegGet

    def register(self, itemtype: type[_Item]) -> None:
        """Register an ItemType."""
        itemtype_name = itemtype.__qualname__
        typeid_name   = itemtype.__dearpypixl__.identity[1]
        # ItemType class names are used to reference the actual ItemType.
        # Existing keys with the same name will be overwritten. This
        # means the newest subclass will be registered in place of its
        # parent ONLY if it shares the same name. Most users won't do this
        # by accident. This makes it very easy to replace/extend existing
        # "built-in" ItemTypes.
        self[itemtype_name] = itemtype
        # Store the DearPyGui type name as a lookup alias when searching
        # for the item type. Since these should only be linked to DearPyPixl
        # (DearPyGui) built-in types, it's only set once IF it doesn't exist.
        # This is so `UserDefinedWindow` item type isn't referenced when
        # looking for 'mvAppItemType::mvWindowAppItem', expecting the real
        # `Window` type. Any proper replacement or extension of `Window`
        # should have the same name, so 'mvAppItemType::mvWindowAppItem'
        # should already point to the name 'Window' from a previous `Window`
        # class' registration.
        typeid_names = self.__typenames
        if typeid_name not in typeid_names and typeid_name.startswith("mvAppItemType::"):
            typeid_names[typeid_name] = itemtype_name




class RegistryProxy(KeysView):  # BUT OF COURSE `MappingProxyType` is final...
    __slots__ = ()

    def __init__(self, mapping):
        super().__setattr__("_mapping", mapping)

    def __getitem__(self, key):
        return self._mapping.__getitem__(key)

    @overload
    def get(self, __key: Any, /) -> Any | None: ...
    @overload
    def get(self, __key: Any, __default: Any, /) -> Any | None: ...
    def get(self, *args, **kwargs):
        return self._mapping.get(*args, **kwargs)

    def items(self):
        return ItemsView(self._mapping)

    def keys(self):
        return KeysView(self._mapping)

    def values(self):
        return ValuesView(self._mapping)





_itemtypes: ItemTypeRegistry[str, type[_Item]] = ItemTypeRegistry()
_items    : ItemRegistry[int, _Item]           = ItemRegistry()

itemtypes = RegistryProxy(_itemtypes)
items     = RegistryProxy(_items)


def get_itemtype(): ...
get_itemtype: ItemTypeRegGet = _itemtypes.get


def get_item(): ...
get_item: ItemRegGet = _items.get


def refresh():
    return _items.refresh()


last_item      = itemized_return(last_item)
last_root      = itemized_return(last_root)
last_container = itemized_return(last_container)
