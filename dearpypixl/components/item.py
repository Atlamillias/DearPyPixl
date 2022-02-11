"""Lowest-level types for DearPyPixl."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, TypeVar, Union, Mapping
from typing_extensions import Self
from enum import IntEnum
from inspect import Parameter
import functools
import inspect
import sys

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
from dearpypixl.components.configuration import (
    item_attribute,
    ItemAttribute,
)

__all__ = [
    # TypeVars
    "ItemT",
    "ItemLikeT",
    "TemplateT",
    # Useful objects
    "ProtoItem",
    "Item",
    ]


ItemT     = TypeVar("ItemT"    , bound="ProtoItem")
TemplateT = TypeVar("TemplateT", bound="Template" )
        

class Template(Mapping, metaclass=ABCMeta):
    __slots__ = ("_target_parameters", "kwargs")

    _target_factory: ItemT

    def __init__(self, **config):
        self._target_parameters = self._target_factory._item_init_params
        if "kwargs" not in config:
            config["kwargs"] = {}
        elif not isinstance(config["kwargs"], dict):
            raise TypeError("`kwargs` must be a dictionary.")
        self.kwargs = config.pop("kwargs")
        self.configure(**config)

    def __repr__(self) -> str:
        return f"<class {type(self).__qualname__!r}>"

    def __call__(self, **config) -> ItemT:
        config_overrides = config
        config = self.configuration()
        kwargs = config.pop("kwargs", {})
        params = config | kwargs | config_overrides
        return self._target_factory(**params)

    def __getitem__(self, attr: str) -> Any:
        return getattr(self, attr)

    def __setitem__(self, attr: str, value: Any) -> None:
        return setattr(self, attr, value)
    
    def __iter__(self):
        yield from self._target_parameters

    def __len__(self) -> int:
        return len(self._target_parameters)

    def configure(self, **config) -> None:
        return Item.configure(self, **config)

    def configuration(self) -> dict[str, Any]:
        return {attr:getattr(self, attr) for attr in self._target_parameters}
        

class ProtoItem(metaclass=ABCMeta):
    """Updates attribute dictionaries for `Item` class derivatives, ensuring
    that the new subclass has all configuration, information, and state attributes/keys
    from their ancestor(s), along with any new additions of its own. Mixin classes
    can (should) inherit from this as well if they define new attributes with the
    intention of passing them onto descendants as internally managed attributes.
    """
    # NOTE: ALL Item-related class objects in DearPyPixl should be inheriting from
    #       this in some fashion. This includes the `Item` base type, and ALL
    #       (App)Item mixin classes. Default implementations for exposing the registered
    #       managed attributes is defined on `Item`.
    __slots__ = ()

    _AppItemsRegistry : dict[int, ItemT]       = {}
    _ItemTypeRegistry : dict[str, type[ItemT]] = {}
    _RootItemRegistry : list[str]              = []

    _is_root_item     : bool  = False

    _item_init_params : dict[str, Parameter]   = {}
    _item_config_attrs: set[str]               = set()
    _item_inform_attrs: set[str]               = set()
    _item_states_attrs: set[str]               = set()
    _item_cached_attrs: set[str]               = set()
    _item_template_obj: TemplateT

    def __init_subclass__(cls):
        super().__init_subclass__()
        parent_cls = cls.mro()[1]
        cls._item_init_params  = getattr(parent_cls, "_item_init_params", {}) | \
                                 dict(inspect.signature(cls).parameters)
        # Import categorized item attributes registered from `ItemAttribute`,
        # `item_attribute`.
        cls._item_config_attrs = [*ItemAttribute.next_class_item_attrs["configuration"]]
        cls._item_inform_attrs = [*ItemAttribute.next_class_item_attrs["information"]]
        cls._item_states_attrs = [*ItemAttribute.next_class_item_attrs["state"]]
        cls._item_cached_attrs = [*ItemAttribute.next_class_item_attrs["cached"]]
        # Reset `next_class_item_attrs.values()` for the next class.
        for collection in ItemAttribute.next_class_item_attrs.values():
            collection.clear()

        # Inheriting item attributes from the direct parent class.
        cls_attributes = {*cls.__dict__,
                          *cls.__slots__,
                          *cls._item_cached_attrs,
                          *cls._item_config_attrs,
                          *cls._item_inform_attrs,
                          *cls._item_states_attrs}
        inherits = ("_item_config_attrs", "_item_inform_attrs", "_item_states_attrs", "_item_cached_attrs")
        for coll_name in inherits:
            collection = getattr(parent_cls, coll_name)
            for item_attr in collection:
                # If the attribute is defined anywhere on `cls` (newest object) or is
                # in its an `_item x_attrs` collection, the attribute is ignored. This allows
                # for expected inheritance of registered attributes. It also means that
                # attributes can be unregistered for the newest object by redefining them.
                if item_attr not in cls_attributes:
                    getattr(cls, coll_name).append(item_attr)

        cls._item_config_attrs = tuple(cls._item_config_attrs)
        cls._item_inform_attrs = tuple(cls._item_inform_attrs)
        cls._item_states_attrs = tuple(cls._item_states_attrs)
        cls._item_cached_attrs = tuple(cls._item_cached_attrs)

        # Creating and binding a new `Template` obj for `cls`. 
        cls._item_template_obj = type(
            f"{cls.__qualname__}{Template.__qualname__}",
            (Template,),
            {"__slots__": tuple(cls._item_init_params.keys())}
        )
        cls._item_template_obj._target_factory = cls
        
        # Registernew item class
        cls._ItemTypeRegistry[cls.__qualname__] = cls
        if cls._is_root_item:
            cls._RootItemRegistry.append(cls.__qualname__)


class Item(ProtoItem, metaclass=ABCMeta):
    """
    Abstract Methods
    ----------------
    * _command (Callable): Class attribute - Internal API command that can
    be called to create the item.


    Properties
    ----------



    Methods
    -------

    """
    __slots__ = ("_tag",)

    _is_container    : bool  = False
    _is_root_item    : bool  = False
    _is_value_able   : bool  = False
    _unique_parents  : tuple[str, ...] = ()
    _unique_children : tuple[str, ...] = ()
    _unique_commands : tuple[str, ...] = ()
    _unique_constants: tuple[str, ...] = ()



    @abstractmethod
    def _command() -> Callable[..., Any]: ...

    def __init__(self, **kwargs):
        self._tag = kwargs.pop("tag", generate_uuid())

        _cached_attrs = self._item_cached_attrs

        # `user_data` needs to be excluded from type casting as it is allowed
        # to be anything.
        user_data = kwargs.pop("user_data", None)
        for arg, val in kwargs.items():
            # Recasting int-like values.
            if isinstance(val, (Item, IntEnum)):
                kwargs[arg] = int(val)
            # Storing attributes that cannot be fetched from DPG on instance. 
            if arg in _cached_attrs:
                setattr(self, f"_{arg}", val)

        type(self)._command(tag=self._tag, user_data=user_data, **kwargs)
        self._AppItemsRegistry[self._tag] = self  # Registering Item obj

    def __repr__(self):
        return f"{type(self).__qualname__}(tag={self._tag!r})"
 
    def __int__(self):
        return self._tag

    def __iter__(self):
        yield from self.children()

    def __hash__(self):
        return hash((type(self), self._tag))

    def __eq__(self, other):
        if not isinstance(other, ProtoItem):
            return False
        return hash(self) == hash(other)


    ## list-like methods
    @functools.singledispatchmethod
    def __getitem__(self, value):
        raise NotImplemented("This slice or index operation is not supported.")

    @__getitem__.register
    def __getslice(self, value: slice) -> list[ItemT]:
        # `value` is a slice: `[0:4:0]`, `[:]`
        return self.children(slot=1)[value.start: value.stop: value.step]

    @__getitem__.register
    def __getindex(self, value: int) -> ItemT:
        # `value` is an index: `[0]`
        # Not calling the `children` method as it is unnecessarily slow only to fetch 1 item.
        child_idx = get_item_info(self._tag)["children"][1][value]
        return self._AppItemsRegistry[child_idx]

    def index(self, __value: ItemT, __start: int = 0, __stop: int = None) -> int:
        """Return first index of `value`. Raises `ValueError` if the value is not present.
        """
        children = self.children(slot=1)
        return children.index(__value, __start, __stop or len(children))

    def copy(self, recursive: bool = False, **config) -> Self:
        """Create and return a copy of this item. Children of the copied item
        will not be duplicated unless `recursive` is True.

        Args:
            * recursive (bool, optional): If True, all item children will also be
            duplicated. Default is False.
            * config (keyword-only, optional): Configuration that will override
            the copied configuration for the returned Item instance.
        """
        cls = type(self)
        configuration = self.configuration() | config

        if configuration.get("pos", None) == [0, 0]:
            configuration["pos"] = []

        if not cls._is_root_item and "parent" not in config:
            configuration["parent"] = self.parent
        # `value` isn't typically a valid argument. Usually it's `default_value`,
        # but it's not consistent. To be safe, the value is set after item
        # creation.
        value = configuration.pop("value", None)
        self_copy = cls(**configuration)
        # Applying value (if the item isn't value-able then it simply won't "stick")
        dearpygui.set_value(self_copy._tag, value)

        if recursive:
            for child in self.children():
                child.duplicate(recursive=recursive, parent=self_copy)

        return self_copy


    @classmethod
    @property
    @item_attribute(category="information")
    def _item_index(cls) -> ItemIndex:
        """The enum member that represents the item's type.
        """
        try:
            return ItemIndex[cls.__qualname__]
        except (AttributeError, KeyError):
            return None

    @classmethod
    def raw_init(cls, **config) -> Union[int, str]:
        """Skip normal initialization -- Directly call the DearPyGui command used
        to create the item and return its unique identifier. Useful when creating
        several items (hundreds/thousands) or when object orientation for an item
        is unnecessary. This GREATLY increases performance in item creation.
        However, no instances are created, and support to manage the item is only
        available using the DearPyGui API.
        """
        for kw, val in config.items():
            # Item and IntEnum types still need to be recast.
            if isinstance(val, (Item, IntEnum)):
                config[kw] = int(val)
        return cls._command(**config)

    @classmethod
    def as_template(cls, **config) -> type[Self]:
        """Return an instance of `ItemTemplate` -- a mapping-like factory object 
        that can create instances of items from a freely-customizable default
        configuration. <config> will be merged into a copy of the default parameters
        used to initialize an instance of the class.

        Args:
            * config (keyword-only, optional): Overriding configuration to be used
            as initial default configuration for future items.
        """
        config = {p.name:p.default for p in cls._item_init_params.values()
                  if p.default is not p.empty} | config

        return cls._item_template_obj(**config)

    @classmethod
    @property
    @item_attribute(category="information")
    def unique_parents(cls) -> tuple[str, ...]:
        """Return the names of all item types that can parent this item IF the item requires
        specific parent items. If the returned tuple is empty, then the item can be parented by
        most non-root container items.
        """
        return cls._unique_parents

    @classmethod
    @property
    @item_attribute(category="information")
    def unique_children(cls) -> tuple[str, ...]:
        """Return the names of all item types that this item can parent. If the returned tuple
        is empty, then this type of item can parent most non-root items.
        """
        return cls._unique_children

    @classmethod
    @property
    @item_attribute(category="information")
    def is_container(cls) -> bool:
        """Return True if this item is capable of parenting other items.
        """
        return cls._is_container

    @classmethod
    @property
    @item_attribute(category="information")
    def is_root_item(cls) -> bool:
        """Return True if this item does not require a parent item to exist
        (and cannot be parented by other items).
        """
        return cls._is_root_item

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

        NOTE: This is not an exact equivelent of DearPyGui's `configure_item`
        command. Unlike `configure_item`, if the option is not included as a
        parameter in signature of `type(self)`, it is not considered "configuration"
        and will not be included in the return (see the `information` method). 
        """
        # This is MUCH faster than calling `getattr` on every configuration.
        # From cProfile, calling `self.configuration()` 50,000 times:
        #   * `getattr` everything (descriptors): 4.698 seconds
        #   * `getattr` only if necessary: 0.509 seconds
        config = get_item_configuration(self._tag)
        item_config_attrs = self._item_config_attrs
        return {attr:(config[attr] if attr in config else
                getattr(self, attr)) for attr in item_config_attrs}

    def information(self) -> dict[str, Any]:
        """Return various read-only information about the item.
        """
        # NOTE: The only two keys in the return that can be used for item creation
        # are `tag` and `parent`. However, they are read-only so they're included here.
        return {attr: getattr(self, attr) for attr in self._item_inform_attrs}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        # Similar to the speed-up implementation for the `configuration` method
        # but a little more hacky (and for less of a performance boost).
        # From cProfile, calling `self.state()` 50,000 times:
        #   * `getattr` everything (descriptors): 1.27 seconds
        #   * `getattr` only if necessary: 0.810 seconds
        states = {f"is_{state}":v for state, v in get_item_state(self._tag).items()}
        item_states_attrs = self._item_states_attrs
        return {attr:(states[attr] if attr in states else
                getattr(self, attr)) for attr in item_states_attrs}

    def configure(self, **config) -> None:
        """Update the item's configuration, or other instance attributes.
        """
        for key, value in config.items():
            setattr(self, key, value)

    def children(self, slot: int = None) -> tuple[ItemT, ...]:
        """Return a tuple of the item's children. If a slot number is passed, then
        the list will only contain the children in that slot (in the order of their
        current positions).
        """
        child_slots = [*get_item_info(self._tag)["children"].values()]
        child_ids   = sum(child_slots, []) if slot is None else child_slots[slot]
        appitems    = self._AppItemsRegistry
        return tuple([appitems[child_id] for child_id in child_ids])

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


    #### Work-In-Progress ####
    def _export_configuration(self) -> dict[str, Any]:
        item_type       = type(self)
        dft_init_params = {p.name: p.default for p in item_type._item_init_params.values()}
        export_config   = {
            "item"  : item_type.__qualname__,
            "tag"   : self._tag,
            "parent": self.parent
        }
        return export_config | dft_init_params | self.configuration()

    def _item_tree(self) -> list[Item, list[Item, list]]:
        tree = [self, []]
        for child in self.children():
            child_tree = child._item_tree()
            tree[1].append(child_tree)
        return tree

    def item_tree(self) -> dict[Item, list[list[Item, list]]]:
        """Return the entire parential tree for this item.
        """
        # Find the root parent first.
        root_item    = None
        current_item = self
        while root_item is None:
            if current_item.is_root_item:
                root_item = current_item
            current_item = current_item.parent
        
        tree = root_item._item_tree()
        return {tree[0]: tree[1]}

                





