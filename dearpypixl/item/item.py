"""Lowest-level types for DearPyPixl."""
from __future__ import annotations
from typing import TypeVar
from abc import ABCMeta, abstractmethod
from typing import Callable, Any
from dearpygui import dearpygui
from dearpygui._dearpygui import (
    generate_uuid,
    get_all_items,
    unstage,
    get_item_info,
    get_item_state,
    get_all_items,
    get_item_configuration,
    move_item,
    move_item_up,
    move_item_down,
    focus_item,
    delete_item,
)
from dearpypixl.constants import ItemIndex
from dearpypixl.item.configuration import (
    item_attribute,
    ItemAttributeCache,
    ConfigContainer
)


__all__ = [
    "ItemT",

    "Item",
    ]


ItemT = TypeVar("ItemT", bound="Item")


class Item(ItemAttributeCache, metaclass=ABCMeta):
    """Base class for all wrapped items. Cannot be instantiated -- must be
    subclassed.


    Abstract Methods
    ----------------
    * _command (Callable): Class attribute - Internal API command that can
    be called to create the item.


    Properties (read-only)
    ----------
    * tag
    * item_category
    * parent
    * is_container
    * is_ok


    Methods
    -------
    * as_configuration_container (classmethod)
    * children
    * configure
    * configuration
    * information
    * state
    * delete
    * duplicate
    * unstage
    * move
    * move_up
    * move_down
    * focus


    Returns:
        *Item*
    """
    @abstractmethod
    def _command() -> Callable: ...

    _is_container: bool = False
    _is_root_item: bool = False
    _unique_parents = ()
    _unique_children = ()
    _unique_commands = ()
    _unique_constants = ()

    _appitems: dict[int, Item] = {}

    def __init__(self, **kwargs):
        cls = type(self)
        self._tag = kwargs.pop("tag", generate_uuid())

        for kw, val in kwargs.items():
            # Converting all `Item` instances (values) to `int` for their `tag`.
            if isinstance(val, Item):
                kwargs[kw] = int(val)
            # Setting unmanagable attributes in instance dictionary.
            # NOTE: `unmanagable` attributes are those that cannot be get/set through
            # dearpygui post item creation, but are used to construct the item. They are
            # set as simple read-only properties.
            if kw in self._unmanaged_attrs:
                setattr(self, f"_{kw}", val)

        cls._command(id=self._tag, **kwargs)

    def __repr__(self):
        configuration = {
            "tag": self._tag,
            "parent": self.parent,
        }
        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={val!r}' for attr,
                         val in configuration.items()))
            + f")"
        )

    def __int__(self):
        return self._tag

    @classmethod
    def as_configuration_container(cls, **config) -> ConfigContainer:
        """Return a `ConfigContainer` instance for this item type. The container's
        configuration can be freely changed, provided that the configuration
        attribute(s) is an acceptable argument to create instances of this item type.

        Args:
            * config (optional, keyword-only): configuration used to
            create an instance of this item type (<cls>). An AttributeError
            will be raised if the configuration attribute is not supported.
        """
        return ConfigContainer(cls, **config)

    @property
    @item_attribute(category="information")
    def item_index(self) -> ItemIndex:
        """The enum member that represents the item's type.
        """
        try:
            return ItemIndex[type(self).__qualname__]
        except (AttributeError, KeyError):
            return None

    @property
    @item_attribute(category="information")
    def tag(self) -> int:
        """This item's unique identifier.
        """
        return self._tag

    @property
    @item_attribute(category="information")
    def parent(self) -> Item:
        """Return the direct progenitor of this item.
        """
        return self._appitems.get(get_item_info(self._tag)["parent"], None)

    @property
    @item_attribute(category="information")
    def unique_parents(self) -> tuple(str):
        """Return the names of all item types that can parent this item.
        If the returned tuple is empty, then this type of item can be parented by
        any item type that doesn't parent any unique children.
        """
        return self._unique_parents

    @property
    @item_attribute(category="information")
    def unique_children(self) -> tuple(str):
        """Return the names of all item types that this item can parent.
        If the returned tuple is empty, then this type of item can parent any
        item type that doesn't require a unique parent.
        """
        return self._unique_children

    @property
    @item_attribute(category="information")
    def is_container(self) -> bool:
        """Return True if this item is capable of parenting other items.
        """
        return get_item_info(self._tag)["container"]

    @property
    @item_attribute(category="information")
    def is_root_item(self) -> bool:
        """Return True if this item does not require a parent item to exist
        (and cannot be parented by other items).
        """
        return self._is_root_item

    @property
    @item_attribute(category="state")
    def is_ok(self) -> bool:
        """Return True if the item is render-able.
        """
        return get_item_state(self._tag)["ok"]

    @property
    @item_attribute(category="state")
    def is_enabled(self) -> bool:
        """Return True if the item is not disabled.
        """
        return get_item_configuration(self._tag)["enabled"]

    def configuration(self) -> dict[str, Any]:
        """Return the configurable options used to manage this item, along
        with their current values.
        """
        return {attr:getattr(self, attr) for attr in self._config_attrs}

    def information(self) -> dict[str, Any]:
        """Return various read-only information about the item.
        """
        return {attr: getattr(self, attr) for attr in self._inform_attrs}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        return {attr: getattr(self, attr) for attr in self._states_attrs}

    def configure(self, **config) -> None:
        """Update the item's configuration. It is the equivelent of calling
        `setattr`, and can be used to configure multiple attributes.
        """
        _setattr = self.__setattr__
        [_setattr(option, value) for option, value in config.items()]

    def children(self, slot: int = None) -> list[Item]:
        """Return a list of the item's children. If a slot number is passed, then
        the list will only contain the children in that slot (in the order of their
        current positions).
        """
        children = [val for val in get_item_info(self._tag)["children"].values()]
        children = children if slot is None else children[slot]
        appitems = type(self)._appitems
        return [child_item for childs in children
                for child in childs if
                (child_item := appitems.get(child, None))]

    def focus(self):
        """Brings a visual item into focus. Does nothing to un-viewable items.
        """
        focus_item(self._tag)

    def move(self, parent: Item = 0, before: Item = 0) -> None:
        """If the item is a child, it will be appended to <parent>'s list
        of children, or inserted before/above <before>. An error will be raised if
        this item does not require a parenting item to exist.

        Args:
            * parent (int): Item that will contain this item.
            * before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        move_item(self._tag, parent=int(parent), before=int(before))

    def move_up(self) -> None:
        """If the item is a child, it is moved above/before the item
        that immediately precedes it. An error will be raised if this item
        does not require a parenting item to exist.
        """
        move_item_up(self._tag)

    def move_down(self) -> None:
        """If the item is a child, it is placed below/after the item
        that immediately procedes it. An error will be raised if this item
        does not require a parenting item to exist.
        """
        move_item_down(self._tag)

    def unstage(self) -> None:
        """Sets this item to be rendered as normal if it has been staged.

        NOTE: An item is **staged** when it is the child of a `Stage` or
        Stage-like item. Staged items are created and can be configured,
        but are not set for rendering until they have been **unstaged** or
        **moved**. 
        """
        try:
            unstage(self._tag)
        except SystemError:
            pass

    def delete(self, children_only: bool = False, slot: int = -1) -> None:
        """Deletes the item and all children.

        Args:
            * children_only (bool, optional): If True, only this item's children
            will be deleted (and NOT this item). Default is False.
            * slot (int, optional): Only children in this slot will be deleted if
            <children_only> is True. Default is -1 (all slots).

        NOTE: The `del` does not properly delete items -- use this method instead
        of `del.
        """
        appitems = self._appitems
        try:
            delete_item(self._tag, children_only=children_only, slot=slot)
        except SystemError:
            pass
        # Comparing DearPyPixl registry uuids to DearPyGui's registry uuids.
        # Any uuid/references in DearPyPixl's registry that are not in DearPyGui's
        # registry are removed.
        condemned_ref_uuids = {tag for tag in appitems} - set(get_all_items())
        [appitems.pop(tag, None) for tag in condemned_ref_uuids]

        if not children_only:
            del self

    def duplicate(self, **config) -> Item:
        """Creates a (recursive) copy of the item and returns a reference to the
        object. If the item is a root item, a new item created containing copies
        of the original item's children. Otherwise, the copy will be parented by
        this item's parent.

        Args:
            * config (keyword-only, optional): Configuration for the highest-
            level copy. Will be used instead of the copied parameters.

        Returns:
            Item
        """
        item_type = type(self)
        item_info = get_item_info(self._tag)
        item_config = self.configuration()

        exclude_config = ("tag", "before", "pos")
        [item_config.pop(ex, None) for ex in exclude_config]

        item_config = item_config | config

        is_container = item_info["container"]
        is_top_level = is_container and item_info["parent"] == None
        if is_container and not is_top_level:
            if new_item_parent := config.get("parent", None):
                item_config["parent"] = new_item_parent

        new_item = item_type(**item_config)

        # copying theme
        dearpygui.bind_item_theme(new_item._tag, item_info["theme"])
        dearpygui.bind_item_theme(new_item._tag, item_info["disabled_theme"])
        dearpygui.bind_item_font(new_item.tag, item_info["font"])
        
        # duplicating children
        for child in self.children():
            child.duplicate(parent=new_item)

        return new_item

