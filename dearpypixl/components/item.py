"""Lowest-level types for DearPyPixl."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, TypeVar, Union, Mapping, Iterator
from typing_extensions import Self
from enum import IntEnum
from inspect import Parameter
import functools
import inspect
import itertools

from dearpygui import dearpygui
from dearpygui._dearpygui import (
    push_container_stack,
    pop_container_stack,
    reset_pos,

    generate_uuid,
    get_all_items,
    unstage,
    get_item_info,
    get_item_state,
    get_all_items,
    get_value,
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
    CONFIGURATION,
    INFORMATION,
    STATE
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
        configuration = self.configuration()
        kwargs = configuration.pop("kwargs", {})
        params = configuration | kwargs | config
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


def _enter(self: ItemT):
    push_container_stack(self._tag)
    return self

def _exit(self: ItemT, exc_type, exc_instance, traceback):
    pop_container_stack()
        

class ProtoItem(metaclass=ABCMeta):
    """Updates attribute dictionaries for `Item` class derivatives, ensuring
    that the new subclass has all configuration, information, and state attributes/keys
    from their ancestor(s), along with any new additions of its own. Mixin classes
    can (should) inherit from this as well if they define new attributes with the
    intention of passing them onto descendants as internally managed attributes.
    """
    # NOTE: ALL Item-related class objects in DearPyPixl should be inheriting from
    #       this in some fashion. This includes the `Item` base type and ALL
    #       (App)Item mixin classes. Default implementations for exposing the registered
    #       managed attributes is defined on `Item`.
    __slots__ = ()

    _AppItemsRegistry : dict[int, ItemT]       = {}  # Item instances
    _ItemTypeRegistry : dict[str, type[ItemT]] = {}  # Item types (All)
    _RootItemRegistry : list[str]              = []  # Item types (root items only)

    _is_root_item     : bool  = False

    _item_init_params : dict[str, Parameter]   = {}
    _item_config_attrs: set[str]               = set()
    _item_inform_attrs: set[str]               = set()
    _item_states_attrs: set[str]               = set()
    _item_cached_attrs: set[str]               = set()
    _item_template_obj: TemplateT

    def __init_subclass__(cls):
        super().__init_subclass__()
        ###############################################################
        # [Section 1] Controlling Inherited (Managed) Item Attributes #
        # [Section 2] Item Class Template                             #
        # [Section 3] Container Context Control                       #
        # [Section 4] Item Registration                               #
        #
        # The process in which new Item subtypes are created is not
        # overly complex, but not completely straight-forward either.
        # It involves registering both the new type as well as regi-
        # stering any "managed item attributes" it may use. 
        ###############################################################

        #### [Section 1] ####
        parent_cls = cls.mro()[1]
        # Merging the parent class's __init__ parameters into its own. That way,
        # the "total signature" of the item class can be easily retrieved.
        cls._item_init_params  = getattr(parent_cls, "_item_init_params", {}) | \
                                 dict(inspect.signature(cls).parameters)
        # Import categorized managed item attributes (registered from `ItemAttribute`
        # and `item_attribute`).
        cls._item_config_attrs = [*ItemAttribute.next_class_item_attrs["configuration"]]
        cls._item_inform_attrs = [*ItemAttribute.next_class_item_attrs[INFORMATION]]
        cls._item_states_attrs = [*ItemAttribute.next_class_item_attrs["state"]]
        cls._item_cached_attrs = [*ItemAttribute.next_class_item_attrs["cached"]]

        # Reset `next_class_item_attrs.values()` for the next item class.
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
                # If the attribute is defined anywhere on `cls` (newest object) or is in its an
                # `_item x_attrs` collection, the attribute is ignored. This allows for expected
                # inheritance of registered attributes. It also means that attributes can be
                # for the newest object simply by redefining them.
                if item_attr not in cls_attributes:
                    getattr(cls, coll_name).append(item_attr)

        cls._item_config_attrs = tuple(cls._item_config_attrs)
        cls._item_inform_attrs = tuple(cls._item_inform_attrs)
        cls._item_states_attrs = tuple(cls._item_states_attrs)
        cls._item_cached_attrs = tuple(cls._item_cached_attrs)


        #### [Section 2] ####
        # Creating new `Template` type for this item class, and binding it to it. 
        cls._item_template_obj = type(
            f"{cls.__qualname__}{Template.__qualname__}",
            (Template,),
            {"__slots__": tuple(cls._item_init_params.keys())}
        )
        cls._item_template_obj._target_factory = cls


        #### [Section 3] ####
        # NOTE: The `Container` class was removed in favor of this.
        # If the item is a container, it can be used as a context manager.
        if hasattr(cls, "_is_container") and cls._is_container:
            # Don't want accidentally redefine an existing __enter__/__exit__ method.
            if not hasattr(cls, "__enter__"):
                cls.__enter__ = _enter
            if not hasattr(cls, "__exit__"):
                cls.__exit__  = _exit


        #### [Section 4] ####
        # Register new item class. This is mainly for item duplication and 
        # UI reconstitution/creation from a data file.
        cls._ItemTypeRegistry[cls.__qualname__] = cls
        if cls._is_root_item:
            cls._RootItemRegistry.append(cls.__qualname__)


class Item(ProtoItem, metaclass=ABCMeta):
    """Base class for all wrapped DearPyGui item types.


    Attributes & Properties
    -----------------------
        * unique_parents (class property, read-only)
        * unique_children (class property, read-only)
        * is_root_item (class property, read-only)
        * is_container (class property, read-only)
        * is_ok (read-only)
        * is_enabled (read-only)
        * tag (read-only)
        * parent (read-only)


    Methods
    -------
        * raw_init (classmethod)
        * as_template (classmethod)

    """

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
        configuration = {}
        empty         = inspect.Parameter.empty
        for param in cls._item_init_params.values():
            default = None if param.default is empty else param.default
            configuration[param.name] = default

        configuration.pop("kwargs", None)
        configuration |= config

        return cls._item_template_obj(**configuration)

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def unique_parents(cls) -> tuple[str, ...]:
        """Return the names of all item types that can parent this item IF the item requires
        specific parent items. If the returned tuple is empty, then the item can be parented by
        most non-root container items.
        """
        return cls._unique_parents

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def unique_children(cls) -> tuple[str, ...]:
        """Return the names of all item types that this item can parent. If the returned tuple
        is empty, then this type of item can parent most non-root items.
        """
        return cls._unique_children

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls._is_container

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_root_item(cls) -> bool:
        """Return True if this item does not require a parent item to exist
        (and cannot be parented by other items).
        """
        return cls._is_root_item
    
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls._is_value_able

    @property
    @item_attribute(category=INFORMATION)
    def tag(self) -> int:
        """This item's unique identifier.
        """
        return self._tag

    @property
    @item_attribute(category=INFORMATION)
    def parent(self) -> 'Item':
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
        # The only two keys in the return that can be used for item creation
        # are `tag` and `parent`. However, they are read-only so they're included here.
        return {attr: getattr(self, attr) for attr in self._item_inform_attrs}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        # Similar to the speed-up implementation for the `configuration` method
        # but a little more hacky (and for less 'profit').
        states = {f"is_{state}":v for state, v in get_item_state(self._tag).items()}
        item_states_attrs = self._item_states_attrs
        return {attr:(states[attr] if attr in states else
                getattr(self, attr)) for attr in item_states_attrs}

    def configure(self, **config) -> None:
        """Update the item's configuration, or other instance attributes.

        """
        for key, value in config.items():
            setattr(self, key, value)

    def children(self, slot: int = None) -> list['Item']:
        """Return a list of the item's children.

        Args:
            * slot (int, optional): Return children only in this slot.
            Default is None (from all slots). 
        """
        appitems    = self._AppItemsRegistry
        child_slots = [slot for slot in self._children()]
        if slot is None:
            return [appitems[child_id] for child_id in itertools.chain.from_iterable(child_slots)]
        return [appitems[child_id] for child_id in child_slots[slot]]

    def get_item_slot_info(self, *, start: int = 0, stop: int = None) -> tuple[int, int] | None:
        """Search the child slots of this item's parent; return the slot number the item is in, and
        its position/index in that slot. Returns None if the item's parent is None.

        Args:
            * start (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is 0.
            * stop (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is None.
        """
        try:
            return self.parent.get_child_slot_info(self, start=start, stop=stop)
        except AttributeError:  # parent is None
            return None

    def get_child_slot_info(self, value: ItemT, *, start: int = 0, stop: int = None) -> tuple[int, int]:
        """Return the slot number of value and its position/index in that slot. Raises ValueError if
        the item does not parent value.

        Args:
            * value (ItemT): A child item that this item parents.
            * start (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is 0.
            * stop (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is None.
        """
        item_id     = value._tag
        child_slots = [slot for slot in self._children()]
        for slot, children in enumerate(child_slots):
            if item_id in children:
                return slot, children.index(value, start=start, stop=stop or len(children))
        else:
            raise ValueError(f"{self!r} is not the parent of value {value!r}.")

    def item_tree(self, descendants_only: bool = False) -> dict['Item', list[list['Item', list]]]:
        """Return the entire parential tree that includes the item starting from the
        root parent. Non-table items are represented as 2-item lists `[item, [childs]]`
        where each child of that item is also represented as a 2-item list `[item, [childs]]`.
        Table items (only `mvAppItemType::Table`) are represented as
        `[table_item, [rows], [columns]]`.

        `FileExtension`, `FontRangeHint`, `NodeLink`, `Annotation`, `DragLine`,
        `DragPoint`, `DragPayload`, and `Legend` items are excluded from the tree.

        Args:
            * item (int | str): The tag of an item.
            * descendants_only (bool, optional): If True, the tree will start from this item
            and not its root parent. Default is False.
        """
        root_item = self if descendants_only else None
        current_item = self
        while root_item is None:
            if current_item.is_root_item:
                root_item = current_item
            current_item = current_item.parent
        
        return root_item._item_tree()

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

    def copy(self, recursive: bool = False, **config) -> Self:  # kinda mimic list method
        """Create and return a copy of this item. Children of the copied item
        will not be duplicated unless `recursive` is True.

        Args:
            * recursive (bool, optional): If True, all item children will also be
            duplicated. Default is False.
            * config (keyword-only, optional): Configuration that will override
            the copied configuration for the new item copy.
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
                child.copy(recursive=recursive, parent=self_copy)

        return self_copy

    def delete(self, children_only: bool = False, slot: int = -1) -> None:
        """Deletes the item and all children.

        Args:
            * children_only (bool, optional): If True, only this item's children
            will be deleted (and NOT this item). Default is False.
            * slot (int, optional): Only children in this slot will be deleted if
            <children_only> is True. Default is -1 (all slots).

        NOTE: The `del` statement does not properly delete items -- use this method
        instead of `del.
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

    def focus(self) -> None:
        """Brings an item into focus. Does nothing to items that cannot be
        displayed.
        """
        focus_item(self._tag)

    def unstage(self) -> None:
        """Sets this item to be rendered as normal if it has been staged.
        """
        try:
            unstage(self._tag)
        except SystemError:
            pass

    def reset_pos(self) -> None:
        """Returns the item at its original position (`pos`).
        """
        try:
            reset_pos(self.tag)
        except SystemError:
            raise TypeError(f"")

    ######################
    ###### END API #######
    ######################

    __slots__ = ("_tag",)

    _is_container    : bool
    _is_root_item    : bool
    _is_value_able   : bool
    _unique_parents  : tuple[str, ...]
    _unique_children : tuple[str, ...]
    _unique_commands : tuple[str, ...]
    _unique_constants: tuple[str, ...]

    __draw_item_types = (  # used for `item_tree`
        51,  # DrawArrow
        55,  # DrawBezierCubic
        56,  # DrawBezierQuadratic
        53,  # DrawCircle
        54,  # DrawEllipse
        62,  # DrawImage
        98,  # DrawLayer
        50,  # DrawLine
        60,  # DrawPolygon
        61,  # DrawPolyline
        57,  # DrawQuad
        58,  # DrawRect
        59,  # DrawText
        52,  # DrawTriangle
        32,  # Drawlist
        99,  # ViewportDrawlist
    )


    ## Abstract Methods ##
    @abstractmethod
    def _command()          -> Callable[..., Any]: ...
    @abstractmethod
    def _is_container()     -> bool              : ...
    @abstractmethod
    def _is_root_item()     -> bool              : ...
    @abstractmethod
    def _is_value_able()    -> bool              : ...
    @abstractmethod
    def _unique_parents()   -> tuple[str, ...]   : ...
    @abstractmethod
    def _unique_children()  -> tuple[str, ...]   : ...
    @abstractmethod
    def _unique_commands()  -> tuple[str, ...]   : ...
    @abstractmethod
    def _unique_constants() -> tuple[str, ...]   : ...


    ## Special Methods ##
    def __init__(self, **kwargs):
        self._tag = kwargs.pop("tag", generate_uuid())

        cached_attrs = self._item_cached_attrs
        # `user_data` needs to be excluded from type casting as it is allowed
        # to be anything.
        user_data = kwargs.pop("user_data", None)
        for arg, val in kwargs.items():
            # Recasting int-like values.
            if isinstance(val, (Item, IntEnum)):
                kwargs[arg] = int(val)
            # Storing attributes that cannot be fetched from DPG on instance. 
            if arg in cached_attrs:
                setattr(self, f"_{arg}", val)

        type(self)._command(tag=self._tag, user_data=user_data, **kwargs)
        self._AppItemsRegistry[self._tag] = self  # Registering Item obj

    def __repr__(self):
        item_id = self._tag
        label   = get_item_configuration(item_id)["label"]
        value   = get_value(item_id)
        return f"{type(self).__qualname__}(tag={item_id!r}, label={label!r})"
 
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

    # indexing and slicing
    @functools.singledispatchmethod
    def __getitem__(self, value):
        raise NotImplemented("This slice or index operation is not supported.")

    @__getitem__.register
    def __getitem_from_slice(self, value: slice) -> list[ItemT]:
        return self.children(slot=1)[value.start: value.stop: value.step]

    @__getitem__.register
    def __getitem_from_index(self, value: int) -> ItemT:
        child_slots = [slot for slot in self._children()]
        # If this item is a drawing item, search slot 2. Otherwise search slot 1.
        slot_target = 2 if self._is_draw_item() else 1
        children    = child_slots[slot_target]
        return self._AppItemsRegistry[children[value]]

    @__getitem__.register
    def __getitem_from_matrix(self, value: tuple) -> ItemT:
        # NOTE: The `dispatch` wrapper in `singledispatch` can't properly deal
        # w/parameterized generics. This is why the type hint for `value` is `tuple`
        # and not `tuple[int, int]`.
        if self._item_index() != 47:  # `Table`
            raise NotImplemented("This slice or index operation is not supported.")

        row_idx, col_idx = value
        row_id           = get_item_info(self._tag)["children"][1][row_idx]
        row_child_id     = get_item_info(row_id)["children"][1][col_idx]
        return self._AppItemsRegistry[row_child_id]


    ## private/internal methods ##
    def _children(self) -> Iterator[list[int]]:
        yield from get_item_info(self._tag)["children"].values()

    def _item_tree(self) -> list['Item', list['Item', list]]:
        tree        = [self, []]
        child_slots = [*get_item_info(self._tag)["children"].values()]
        # slots 1 (most items) and 2 (draw items)
        appitems = self._AppItemsRegistry
        children = child_slots[2 if self._is_draw_item() else 1]
        for child in children:
            child = appitems[child]
            child_tree = child._item_tree()
            tree[1].append(child_tree)
        return tree

    @classmethod
    def _item_index(cls) -> int:
        """Return the integer that represents the item's type.
        """
        return int(ItemIndex[cls.__qualname__])

    @classmethod
    def _is_draw_item(cls) -> bool:
        return cls._item_index() in cls.__draw_item_types


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



                





