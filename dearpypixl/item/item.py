"""Lowest-level types for DearPyPixl."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, TypeVar, Union
from enum import IntEnum
from inspect import signature
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
    ItemAttribute,
    get_unmanagable,
)


__all__ = [
    "ItemT",
    "ProtoItem",
    "Item",
    ]


ItemT = TypeVar("ItemT", bound="ProtoItem")


class objectmethod(classmethod):
    """Method descriptor. Wrapped methods will recieve `self` as their first argument
    if the method is called on an instance object (i.e. "instance method"). Otherwise,
    `cls` is passed as the first argument to the method (i.e. `classmethod`)."""
    def __get__(self, instance, __type):
        method = super().__get__ if instance is None else self.__func__.__get__
        return method(instance, __type)



class ProtoItem:
    """Updates attribute dictionaries for `Item` class derivatives, ensuring
    that the new subclass has all configuration, information, and state attributes/keys
    from their ancestor(s), along with any new additions of its own. Mixin classes
    can (should) inherit from this as well if they define new attributes with the
    intention of passing them onto descendants as internally managed attributes.

    Attributes:
        * config_attrs: A collection of item attributes that can be used as an
        argument for an item's creation, and can still be configured afterwards.
        * inform_attrs: A collection of item attributes that can potentially
        be used as an argument for an item's creation, but is generally read-only
        afterwards.
        * states_attrs: A collection of item attributes that are read-only. They
        are not used as item-creation arguments and are not configurable.
        * attr_aliases: A mapping of an item's defined class or instance attributes
        pointing to the name of the internal item attribute that they actually manage.
    """
    # NOTE: ALL Item-related class objects in DearPyPixl should be inheriting from this in some
    #       fashion. This includes the `Item` base type, and ALL (App)Item mixin classes. Default
    #       implementations for exposing the registered managed attributes is defined on `Item`.
    __slots__ = (
                    "_config_attrs"   ,
                    "_inform_attrs"   ,
                    "_states_attrs"   ,
                    "_init_params"    ,
                    "_unmanaged_attrs",
                )

    _AppItemsRegistry: dict[int, ItemT]       = {}
    _ItemTypeRegistry: dict[str, type[ItemT]] = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        config_attrs = ItemAttribute.next_class_item_attrs["configuration"]
        inform_attrs = ItemAttribute.next_class_item_attrs["information"]
        states_attrs = ItemAttribute.next_class_item_attrs["state"]
        init_params  = set()
        # Iterate from oldest to newest parent class; excluding `object`
        # and `ItemAttributeCache` (2 oldest) and `cls` (newest).
        for derived_from in cls.mro()[-3:0:-1]:
            config_attrs |= derived_from.__dict__.get("_config_attrs", set())
            inform_attrs |= derived_from.__dict__.get("_inform_attrs", set())
            states_attrs |= derived_from.__dict__.get("_states_attrs", set())
            init_params  |= derived_from.__dict__.get("_init_params" , set())
        cls._config_attrs = cls.__dict__.get("_config_attrs", set()) | config_attrs
        cls._inform_attrs = cls.__dict__.get("_inform_attrs", set()) | inform_attrs
        cls._states_attrs = cls.__dict__.get("_states_attrs", set()) | states_attrs
        cls._init_params  = {*signature(cls).parameters} | init_params
        # Reset `next_class_item_attrs.values()` for the next class.
        for collection in ItemAttribute.next_class_item_attrs.values():
            collection.clear()
        # Storing unmanagable attribute names. These cannot be gotten or set from DPG 
        # after item creation. Their default implementation is a read-only property.
        unmanaged_attrs = set()
        for attr_name in {*cls._config_attrs, *cls._inform_attrs}:
            attr = getattr(cls, attr_name)
            # Checking for descriptor 
            if isinstance(attr, ItemAttribute) and attr.fget == get_unmanagable:
                unmanaged_attrs.add(attr_name)
        cls._unmanaged_attrs = unmanaged_attrs



class Item(ProtoItem, metaclass=ABCMeta):
    """
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
    """

    __slots__ = (
                    "_tag",
                )

    _is_container    : bool  = False
    _is_root_item    : bool  = False
    _unique_parents  : tuple = ()
    _unique_children : tuple = ()
    _unique_commands : tuple = ()
    _unique_constants: tuple = ()

    @abstractmethod
    def _command() -> Callable: ...


    def __init__(self, **kwargs):
        cls = type(self)
        self._tag = kwargs.pop("tag", generate_uuid())

        _unmanaged_attrs = self._unmanaged_attrs
        for kw, val in kwargs.items():
            # Values: `Item` -> `Item.tag`, `IntEnum` -> `IntEnum.value`
            if isinstance(val, (Item, IntEnum)):
                kwargs[kw] = int(val)
            # "unmanaged" == item configuration that cannot be gotten or set after
            # item creation. Default implementation is a read-only property.
            if kw in _unmanaged_attrs:
                setattr(self, f"_{kw}", val)

        cls._command(tag=self._tag, **kwargs)
        self._AppItemsRegistry[self._tag] = self

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

    @objectmethod
    def as_template(obj: Union[ItemT, type[ItemT]], **config) -> ItemTemplate:
        """Return an instance of `ItemTemplate` -- a mapping-like factory object 
        that can create instances of items from a freely-customizable default
        configuration. This method has slightly different behavior depending on if
        it is called on an instance or class object. If called on an instance,
        <config> is merged into a copy of the item's existing configuration, which
        is then sent to the `ItemTemplate` constructor as the initial default
        configuration for items made from the template. If called on the class,
        <config> will instead be merged into a copy of the default parameters used
        to initialize an instance of it.

        Args:
            * config (keyword-only, optional): Overriding configuration to be used
            as initial default configuration for future items.
        """
        # If `obj` is an instance, we copy the existing configuration from it
        # and pass it to the template constructor.
        if isinstance(obj, Item):
            # `config` overrides the existing configuration.
            config = obj.configuration() | config
            obj = type(obj)
        return ItemTemplate(obj , **config)

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
    def parent(self) -> ItemT:
        """Return the direct progenitor of this item.
        """
        return self._AppItemsRegistry.get(get_item_info(self._tag)["parent"], None)

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
        """Update the item's configuration, or other instance attributes.
        """
        for key, value in config.items():
            setattr(self, key, value)

    def children(self, slot: int = None) -> list[ItemT]:
        """Return a list of the item's children. If a slot number is passed, then
        the list will only contain the children in that slot (in the order of their
        current positions).
        """
        children = [val for val in get_item_info(self._tag)["children"].values()]
        children = children if slot is None else children[slot]
        appitems = type(self)._AppItemsRegistry
        return [child_item for childs in children
                for child in childs if
                (child_item := appitems.get(child, None))]

    def focus(self) -> None:
        """Brings a visual item into focus. Does nothing to un-viewable items.
        """
        focus_item(self._tag)

    def move(self, parent: Union[ItemT, int] = 0, before: Union[ItemT, int] = 0) -> None:
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
        appitems = self._AppItemsRegistry
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

    def duplicate(self: ItemT, **config) -> ItemT:
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







class ItemTemplate():
    _target_params = ()
    _configuration = ()

    def __init__(self, target_item, **kwargs):
        self._target_item = target_item
        self._target_params = tuple([*target_item._init_params])
        self._configuration = {}
        self.configure(**kwargs)

    def __setattr__(self, attr, value):
        if attr in self._target_params:
            self._configuration[attr] = value
            return None
        elif attr.startswith("_"):  # allow private attributes
            return object.__setattr__(self, attr, value)
        raise AttributeError(
            f"{self._target_item!r} does not accept this parameter.")

    def __getattr__(self, attr):
        if attr in self._configuration:
            return self._configuration[attr]
        elif attr in self._target_params:
            return None
        raise AttributeError(f"{type(self)!r} has no attribute {attr!r}.")

    def create(self):
        """Return an instance from the target item using this object's configuration.
        """
        return self._target_item(**self._configuration)

    def parameters(self) -> tuple:
        """Return a tuple containing the accepted parameters for the
        target constructor.
        """
        return self._target_params

    def configuration(self) -> dict:
        return self._configuration

    def configure(self, **config) -> None:
        _setattr = self.__setattr__
        [_setattr(optn, value) for optn, value in config.items()]

