"""Lowest-level types for DearPyPixl."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, TypeVar, Union, MutableMapping, Iterator, NamedTuple
from typing_extensions import Self, TypeAlias
from enum import IntEnum
from inspect import Parameter
import functools
import inspect
import itertools

from dearpygui import dearpygui
from dearpygui._dearpygui import (
    push_container_stack,
    pop_container_stack,
    does_item_exist,
    reset_pos,
    add_alias,
    generate_uuid,
    get_all_items,
    get_item_alias,
    unstage,
    get_item_info,
    get_item_state,
    get_all_items,
    get_value,
    set_value,
    get_item_configuration,
    configure_item,
    move_item,
    move_item_up,
    move_item_down,
    focus_item,
    delete_item,
)
from dearpypixl.constants import ItemIndex
from dearpypixl.components.configuration import (
    ItemAttribute,
    item_attribute,
    prep_callback,
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



class _RegistryType(NamedTuple):
    items: dict[int, ItemT]       = {}
    types: dict[str, type[ItemT]] = {}


class _InternalType(NamedTuple):
    config_members: tuple[str, ...]      = ()
    inform_members: tuple[str, ...]      = ()
    states_members: tuple[str, ...]      = ()
    cached_members: tuple[str, ...]      = ()
    init_params   : dict[str, Parameter] = {}
    template_item : TemplateT            = None

        
class ProtoItem(metaclass=ABCMeta):
    """The "bookkeeper" for Item subclasses. Registers new item types
    and ensures expected functionality of inherited properties.
    """
    # NOTE: Every Item-related class object in DearPyPixl should be inheriting from
    # this in some fashion. This includes the `Item` base type and any mixins for
    # Item subclasses. Niche applications aside, derive from `Item` and not this --
    # it has all of the fancy stuff. Literally nothing here is designed to be
    # publicly accessed.
    #
    # Also, this section is pretty comment-heavy because I have the short-term
    # memory of a tunafish.

    @abstractmethod
    def tag(self) -> int: ...

    __slots__ = ()

    __registry__      : _RegistryType = _RegistryType()
    __internal__      : _InternalType = _InternalType() 

    __is_root_item__  : bool     = False
    __is_container__  : bool     = False
    __able_parents__  : tuple    = ()
    __able_children__ : tuple    = ()
    __is_value_able__ : bool     = False
    __command__       : Callable = None
    __constants__     : tuple    = ()

    def __init_subclass__(cls):
        super().__init_subclass__()
        ###############################################################
        # [Section 1] Controlling Inherited (Managed) Item Attributes #
        # [Section 2] Item Class Template                             #
        # [Section 3] Container Context Control                       #
        # [Section 4] Item Registration                               #
        #                                                             #
        # The process in which new Item subtypes are created is not   #
        # overly complex, but not completely straight-forward either. #
        # It involves registering both the new type as well as regi-  #
        # stering any "managed item attributes" it may use. Inheriti- #
        # ng from `ProtoItem` or `Item` will handle the item type     #
        # registration. The bulk of the attribute registration is     #
        # handled by the `ItemAttribute` descriptor class and the     #
        # `item_attribute` decorator function defined in              #
        # "configuration.py".                                         #
        #                                                             #
        # As attributes are used with either object, they are cached  #
        # under a specific category (configuration, state, or inform- #
        # tion). They are then registered to the NEXT subclass that   #
        # is initialzed (defined below). The initialization clears    #
        # the cache for the FOLLOWING class. It's VERY important that #
        # `ItemAttribute` and `item_attribute` only be used in the    #
        # body of a class derived from `ProtoItem` or `Item`.         #           
        ###############################################################
        
        # TODO: Possibly apply a `value` property on `Item`, and set the setter
        # here if the item is value-able.

        #### [Section 1] #############################################################
        # Merging the parent class's __init__ parameters into its own. That way,
        # the "complete signature" of the item class can be easily retrieved
        # even after subclassing. Less mro traversal.
        parent_cls      = cls.mro()[1]
        parent_internal = getattr(parent_cls, "__internal__", ProtoItem.__internal__)

        # Managed item members are stored via `ItemAttribute` and `item_attribute`.
        config_members  = [*ItemAttribute.next_class_item_attrs[CONFIGURATION]]
        inform_members  = [*ItemAttribute.next_class_item_attrs[INFORMATION]]
        states_members  = [*ItemAttribute.next_class_item_attrs[STATE]]
        cached_members  = [*ItemAttribute.next_class_item_attrs["cached"]]
        init_params     = parent_internal[4] | dict(inspect.signature(cls).parameters)

        item_mbr_seqs   = (config_members, inform_members, states_members, cached_members)
        parent_mbr_seqs = parent_internal[0:4]

        itemt_members   = {*getattr(cls, "__dict__" , ()),
                           *getattr(cls, "__slots__", ()),
                           *config_members,
                           *inform_members,
                           *states_members,
                           *cached_members}

        # Ensuring that the new item class doesn't inherit a managed attribute if
        # it has it's own implementation, allowing for expected inheritance. For
        # example; `label` is a managed attribute defined on the `Item` class (below).
        # It will continue to be a registered managed attribute through inheritance
        # until a subclass re-defines `label` (which would unregister it).
        for item_sequence, parent_sequence in zip(item_mbr_seqs, parent_mbr_seqs):
            for member in parent_sequence:
                if member in itemt_members:
                    continue
                item_sequence.append(member)

        #### [Section 2] #############################################################
        # Create a new bound template for this item.
        # [6/03/2022] Special attributes and class

        # There's no need to create a template for a class that is never instantiated.
        # Also when registering the "Item" class an error would be raised as `Template`
        # is defined after it.
        if not inspect.isabstract(cls):
            template = type(
                f"{cls.__qualname__}{Template.__qualname__}",
                (Template,),
                {"__slots__"        : tuple(("tag", *cls.__internal__[4].keys())),
                 "__is_container__" : cls.__command__      ,
                 "__is_root_item__" : cls.__is_root_item__ ,
                 "__is_value_able_" : cls.__is_value_able__,
                 "__able_parents__" : cls.__able_parents__ ,
                 "__able_children__": cls.__able_children__,
                 "__command__"      : cls.__command__      ,
                }
            )
        else:
            template = None
        

        #### [Section 3] #############################################################
        # [4/28/2022] The `Container` class was removed in favor of this.
        # If the item is a container, it can be used as a context manager.
        if cls.__is_container__:
            if not hasattr(cls, "__enter__"):
                cls.__enter__ = cls.__enter
            if not hasattr(cls, "__exit__"):
                cls.__exit__  = cls.__exit


        #### [Section 4] ############################################################
        # Finalize and register new item class...

        cls.__internal__ = _InternalType(
            tuple(config_members),  # <  Several methods defined on the `Item` class
            tuple(inform_members),  # <  are dependant on these collections. An
            tuple(states_members),  # <  attribute included in any of these can be
            tuple(cached_members),  # <  considered "registered".
            init_params,            # <
            template,               # <     
        )

        # Only registering Item classes that can be instantiated.
        # For the sake of readability, `isabstract` is unnecessarily called
        # again just so I can keep these sections seperate.
        if not inspect.isabstract(cls):
            cls.__registry__[1][cls.__qualname__] = cls

        # Clear the item member registry cache for the next derived class.
        # NOTE: Shit gets weird if this cache is populated outside of an
        # appropriate class body.
        # TODO: Deal with the above. Bugs relating to the `ItemAttribute`
        # descriptor are annoying to find as-is. It doesn't need help.
        for collection in ItemAttribute.next_class_item_attrs.values():
            collection.clear()

    def __enter(self):
        push_container_stack(self.tag)
        return self

    def __exit(self, exc_type, exc_instance, traceback):
        pop_container_stack()


class Item(ProtoItem, metaclass=ABCMeta):
    """Base class for wrapping DearPyGui items.

    Properties
    -----------------------
        * label
        * use_internal_label
        * user_data
        * tag (read-only)
        * alias (read-only)
        * parent (read-only)
        * is_root_item (class property, read-only)
        * is_container (class property, read-only)
        * is_value_able (class property, read-only)
        * is_ok (read-only)
        * is_enabled (read-only)

    Methods
    -------
        * raw_init (classmethod)
        * as_template (classmethod)
        * configure
        * configuration
        * information
        * state
        * get_able_parents (classmethod)
        * get_able_children (classmethod)
        * get_item_slot_info
        * get_child_slot_info
        * get_item_tree
        * children
        * move
        * move_up
        * move_down
        * copy
        * delete
        * focus
        * toggle
        * unstage
        * reset_pos

    """

    @classmethod
    def raw_init(cls, **config) -> Union[int, str]:
        """Skip normal initialization -- Directly call the DearPyGui command used
        to create the item and return its unique identifier. Useful when creating
        several items (hundreds/thousands) or when object orientation for an item
        is unnecessary. This greatly increases performance in item creation.
        However, no instances are created, and support to manage the item is only
        available using the DearPyGui API.
        """
        for kw, val in config.items():
            # Item and IntEnum types still need to be recast.
            if isinstance(val, (Item, IntEnum)):
                config[kw] = int(val)
        return cls.__command__(**config)

    @classmethod
    def as_template(cls, **config) -> type[Self]:
        """Return a Template object; a mapping-like factory object that can create
        instances of items from a freely-customizable default configuration. <config>
        will be merged into a copy of the default parameters used to initialize an
        instance of the class.

        Args:
            * config (keyword-only, optional): Overriding configuration to be used
            as initial default configuration for future items.
        """
        configuration = {}
        empty         = inspect.Parameter.empty
        for param in cls.__internal__[4].values():
            default = None if param.default is empty else param.default
            configuration[param.name] = default

        configuration.pop("kwargs", None)
        configuration |= config

        return cls.__internal__[5](**configuration)


    #### Properties ####

    # Configuration
    @property
    @item_attribute(category=CONFIGURATION)
    def label(self) -> str:
        return get_item_configuration(self._tag)["label"]
    @label.setter
    def label(self, value: str) -> None:
        configure_item(self._tag, label=value)

    @property
    @item_attribute(category=CONFIGURATION)
    def use_internal_label(self) -> str:
        return get_item_configuration(self._tag)["use_internal_label"]
    @use_internal_label.setter
    def use_internal_label(self, value: str) -> None:
        configure_item(self._tag, use_internal_label=value)

    @property
    @item_attribute(category=CONFIGURATION)
    def user_data(self) -> str:
        return get_item_configuration(self._tag)["user_data"]
    @user_data.setter
    def user_data(self, value: str) -> None:
        configure_item(self._tag, user_data=value)


    # Information
    @property
    @item_attribute(category=INFORMATION)
    def tag(self) -> int:
        """Return this item's unique integer identifier.
        """
        return self._tag

    @property
    @item_attribute(category=INFORMATION)
    def alias(self) -> str | None:
        """Return this item's unique string identifier.
        """
        return get_item_alias(self._tag) or None

    @property
    @item_attribute(category=INFORMATION)
    def parent(self) -> 'Item':
        """Return the direct progenitor of this item.
        """
        return self.__registry__[0].get(get_item_info(self._tag)["parent"], None)

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls.__is_container__

    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_root_item(cls) -> bool:
        """Return True if this item does not require a parent item to exist
        (and cannot be parented by other items).
        """
        return cls.__is_root_item__
    
    @classmethod
    @property
    @item_attribute(category=INFORMATION)
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls.__is_value_able__


    # State
    @property
    @item_attribute(category=STATE)
    def is_ok(self) -> bool:
        """Return True if the item is render-able.
        """
        return get_item_state(self._tag)["ok"]

    @property
    @item_attribute(category=STATE)
    def is_enabled(self) -> bool:
        """Return True if the item is not disabled.
        """
        return get_item_configuration(self._tag)["enabled"]


    #### Methods ####
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
        item_config_attrs = self.__internal__[0]
        return {attr:(config[attr] if attr in config else
                getattr(self, attr)) for attr in item_config_attrs}

    def information(self) -> dict[str, Any]:
        """Return various read-only information about the item.
        """
        # The only two keys in the return that can be used for item creation
        # are `tag` and `parent`. However, they are read-only so they're included here.
        return {attr: getattr(self, attr) for attr in self.__internal__[1]}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        # Similar to the speed-up implementation for the `configuration` method
        # but a little more hacky (and for less 'profit').
        states = {f"is_{state}":v for state, v in get_item_state(self._tag).items()}
        item_states_attrs = self.__internal__[2]
        return {attr:(states[attr] if attr in states else
                getattr(self, attr)) for attr in item_states_attrs}

    @classmethod
    def get_able_parents(cls) -> tuple[ItemT, ...]:
        """Return the names of all item types that can parent this item IF the item requires
        specific parent items. If the returned tuple is empty, then the item can be parented by
        most non-root container items.
        """
        item_types = cls.__registry__[1]
        return tuple((parent for item_name in cls.__able_parents__
                      if (parent:=item_types.get(item_name))))

    @classmethod
    def get_able_children(cls) -> tuple[ItemT, ...]:
        """Return the names of all item types that this item can parent. If the returned tuple
        is empty, then this type of item can parent most non-root items.
        """
        item_types = cls.__registry__[1]
        return tuple((child for item_name in cls.__able_children__
                      if (child:=item_types.get(item_name))))

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

    def get_item_tree(self, descendants_only: bool = False) -> dict['Item', list[list['Item', list]]]:
        """Return the entire parential tree that includes the item starting from the
        root parent. Non-table items are represented as 2-item lists `[item, [childs]]`
        where each child of that item is also represented as a 2-item list `[item, [childs]]`.
        Table items (only `mvAppItemType::Table`) are represented as `[table_item, [rows], [columns]]`.

        `FileExtension`, `FontRangeHint`, `NodeLink`, `Annotation`, `DragLine`,
        `DragPoint`, `DragPayload`, and `Legend` items are excluded from the tree.

        Args:
            * descendants_only (bool, optional): If True, this item will be root of the
            tree and not this item's root parent. Default is False.
        """
        root_item = self if descendants_only else None
        current_item = self
        while root_item is None:
            if current_item.is_root_item:
                root_item = current_item
            current_item = current_item.parent
        
        return root_item._item_tree()

    def configure(self, **config) -> None:
        """Update the item's configuration, or other instance attributes.
        """
        for key, value in config.items():
            setattr(self, key, value)

    def children(self, slot: int = None) -> list[ItemT]:
        """Return a list of the item's children.

        Args:
            * slot (int, optional): Return children only in this slot.
            Default is None (from all slots). 
        """
        appitems    = self.__registry__[0]
        child_slots = [slot for slot in self._children()]
        if slot is None:
            return [appitems[child_id] for child_id in itertools.chain.from_iterable(child_slots)]
        return [appitems[child_id] for child_id in child_slots[slot]]

    def move(self, parent: Union[ItemT, int] = 0, before: Union[ItemT, int] = 0, **kwargs) -> None:
        """If the item is a child, it will be appended to <parent>'s list
        of children, or inserted before/above <before>. An error will be raised if
        this item does not require a parenting item to exist.

        Args:
            * parent (int): Item that will contain this item.
            * before (int, optional): id of the child item that the widget 
            will be placed above/before.
        """
        try:
            move_item(self._tag, parent=int(parent), before=int(before))
        except SystemError:
            self._err_if_existential_crisis()
            self._err_if_root_item()

            # Troubleshooting problem for user (DPG errors are not always descriptive/convenient).
            if parent and not does_item_exist(parent) or before and not does_item_exist(before):
                raise ValueError(f"`parent` or `before` does not exist; possibly deleted.")
            if parent and before:
                if get_item_info(before)["parent"] != parent:
                    raise ValueError(f"`before` is not a child of `parent`.")
                ValueError(f"Could not move item; is `parent` not appropriate for this item?")
            elif parent:
                ValueError(f"Could not move item; is `parent` not appropriate for this item?")
            elif before:
                ...
            raise

    def move_up(self, **kwargs) -> None:
        """If the item is a child, it is moved above/before the item
        that immediately precedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_up(self._tag)
        except SystemError:
            self._err_if_existential_crisis()
            self._err_if_root_item()
            raise

    def move_down(self, **kwargs) -> None:
        """If the item is a child, it is placed below/after the item
        that immediately procedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_down(self._tag)
        except SystemError:
            self._err_if_existential_crisis()
            self._err_if_root_item()
            raise

    def copy(self, recursive: bool = False, **config) -> Self:  # kinda mimics list method
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

        if not cls.__is_root_item__ and "parent" not in config:
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

    def delete(self, children_only: bool = False, slot: int = -1, **kwargs) -> None:
        """Deletes the item and all children.

        Args:
            * children_only (bool, optional): If True, only this item's children
            will be deleted (and NOT this item). Default is False.
            * slot (int, optional): Only children in this slot will be deleted if
            <children_only> is True. Default is -1 (all slots).

        NOTE: The `del` statement does not properly delete items -- use this method
        instead of `del.
        """
        try:
            delete_item(self._tag, children_only=children_only, slot=slot)
        except SystemError:
            pass
        self._refresh_registry()

        if not children_only:
            del self

    def focus(self, **kwargs) -> None:
        """Brings an item into focus. Does nothing to items that cannot be
        displayed.
        """
        focus_item(self._tag)

    def toggle(self, **kwargs) -> None:
        """If the item supports `show`, hide/show the item. Does nothing if
        `show` is an invalid configuration option.
        """
        # Because configuration attributes are exposed as properties and several
        # DPG items don't support `show`, I'm not inclined to define a `show` function.
        # But I know wrapping `window.show = True/False` in a lambda for a callback is
        # kinda dumb so I wanted to make something user-and-callback-friendly.
        if "show" in self.__internal__[0]:
            show_state = get_item_configuration(self._tag)["show"]
            configure_item(self._tag, show=not show_state)

    def unstage(self, **kwargs) -> None:
        """Sets this item to be rendered as normal if it has been staged.
        """
        try:
            unstage(self._tag)
        except SystemError:
            pass

    def reset_pos(self, **kwargs) -> None:
        """If the item supports positioning (`pos`), return the item to its
        original position. Does nothing if `pos` is an invalid configuration
        option.
        """
        try:
            reset_pos(self.tag)
        except SystemError:
            pass

    ######################
    ###### END API #######
    ######################

    __slots__ = (
        "_tag",
    )

    ## Abstract Methods ##
    @abstractmethod
    def __command__()       -> Callable[..., Any]: ...
    @abstractmethod
    def __is_container__()  -> bool              : ...
    @abstractmethod
    def __is_root_item__()  -> bool              : ...
    @abstractmethod
    def __is_value_able__() -> bool              : ...
    @abstractmethod
    def __able_parents__()  -> tuple[str, ...]   : ...
    @abstractmethod
    def __able_children__() -> tuple[str, ...]   : ...

    ## Misc Attributes ##
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

    ## Special Methods ##
    def __init__(self, **kwargs):
        # Prepping argument values before item creation
        cached_attrs = self.__internal__[3]
        # `user_data` needs to be excluded from type casting as it is allowed
        # to be anything, including items and integer enums.
        user_data = kwargs.pop("user_data", None)
        for arg, val in kwargs.items():
            if "callback" in arg and val:  # `[drag_/drop_]callback`
                kwargs[arg] = prep_callback(self, val)
                continue
            # Recasting int-like values.
            if isinstance(val, (Item, IntEnum)):
                kwargs[arg] = int(val)
            # Storing attributes that cannot be fetched from DPG on instance.
            if arg in cached_attrs:
                setattr(self, f"_{arg}", val)

        # Creation and registration
        identifier = kwargs.pop("tag", None) or generate_uuid()
        alias      = None
        if isinstance(identifier, str):
            alias      = identifier
            identifier = generate_uuid()
        try:
            self._tag = type(self).__command__(tag=identifier, user_data=user_data, **kwargs)
        except SystemError:
            raise SystemError(f"Error creating {type(self).__qualname__!r} item. Verify that the arguments are appropriate.")
        alias and add_alias(alias, identifier)
        self.__registry__[0][self._tag] = self

    def __repr__(self):
        item_id = self._tag
        label   = get_item_configuration(item_id)["label"]
        return f"{type(self).__qualname__}(tag={item_id!r}, label={label!r})"
 
    def __int__(self):
        return self._tag

    def __iter__(self):
        yield from self.children()

    def __hash__(self):
        return hash((type(self), self._tag, self.alias))

    def __eq__(self, other):
        if not isinstance(other, ProtoItem):
            return False
        return hash(self) == hash(other)

    # indexing and slicing
    @functools.singledispatchmethod
    def __getitem__(self, value):
        """Indexing and slicing support for Item instances. Usually returns
        a child of the item, or a list of child items. Behavior is altered
        for some item types, and not implemented for others.
        """
        return NotImplemented

    @__getitem__.register
    def __getitem_from_slice(self, value: slice) -> list[ItemT]:
        """Return the result of slicing the return of self.children().

        Example:
            >>> with Window(tag=5000) as window:
            ...     button1 = Button(tag=6000)
            ...     button2 = Button(tag=6001)
            ...     childw1 = ChildWindow(tag=7000)
            >>> 
            >>> # The result should be the same regardless of slicing
            >>> # `window` or the result of `window.children()`.
            >>> 
            >>> window.children()[::-1] == window[::-1]
            True
        """
        return self.children(slot=1)[value.start: value.stop: value.step]

    @__getitem__.register
    def __getitem_from_index(self, value: int) -> ItemT:
        """Return the child of this item from self.children() at index.

        Example:
            >>> with Window(tag=5000) as window:
            ...     button1 = Button(tag=6000)
            ...     button2 = Button(tag=6001)
            ...     childw1 = ChildWindow(tag=7000)
            >>> 
            >>> # The result should be the same regardless of indexing
            >>> # `window` or the result of `window.children()`.
            >>> 
            >>> window.children()[1].tag == window[1].tag
            True
        """
        child_slots = [slot for slot in self._children()]
        # If this item is a drawing item, search slot 2. Otherwise search slot 1.
        slot_target = 2 if self._is_draw_item() else 1
        children    = child_slots[slot_target]
        return self.__registry__[0][children[value]]

    @__getitem__.register
    def __getitem_from_matrix(self, value: tuple) -> ItemT:
        """If one index is included, return the row of this table item at index.
        If a second index is included, return the cell resulting from indexing
        the former row (similar to a numpy matrix).

        Example:
            >>> with Table(tag=5000) as table:
            ...     col = TableColumn(tag=6000)
            ...     row = TableRow(tag=7000)
            ...     with row:
            ...         cell = TableCell(tag=8000)
            >>> 
            >>> table[0].tag
            7000  # row
            >>> table[0, 0].tag
            8000  # cell
        """
        # NOTE: The `dispatch` wrapper in `singledispatch` can't properly deal
        # w/parameterized generics. This is why the type hint for `value` is `tuple`
        # and not `tuple[int, int]`.
        if self._item_index() != 47:  # `Table`
            raise NotImplemented("This slice or index operation is not supported.")

        row_idx, col_idx = value
        row_id           = get_item_info(self._tag)["children"][1][row_idx]
        row_child_id     = get_item_info(row_id)["children"][1][col_idx]
        return self.__registry__[0][row_child_id]


    ## private/internal methods ##
    def _children(self) -> Iterator[list[int]]:
        """Private `children` method. Yields children's tags.
        """
        # Unlike the public `children` method, this one is an iterator
        # yielding "raw" children. This is preferrable functionality
        # for some things.
        yield from get_item_info(self._tag)["children"].values()

    def _item_tree(self) -> list['Item', list['Item', list]]:
        tree        = [self, []]
        child_slots = [*get_item_info(self._tag)["children"].values()]
        # slots 1 (most items) and 2 (draw items)
        appitems = self.__registry__[0]
        children = child_slots[2 if self._is_draw_item() else 1]
        for child in children:
            child      = appitems[child]
            child_tree = child._item_tree()
            tree[1].append(child_tree)
        if self._item_index() == 47:  # `Table`
            for child in child_slots[0]:  # `TableColumn` items
                child      = appitems[child]
                child_tree = child._item_tree()
                tree[2].append(child_tree)
        return tree

    @classmethod
    def _item_index(cls) -> int:
        """Return the integer that represents the item's type.
        """
        return int(ItemIndex[cls.__qualname__])

    @classmethod
    def _is_draw_item(cls) -> bool:
        return cls._item_index() in cls.__draw_item_types

    @classmethod
    def _refresh_registry(cls) -> None:
        """Clear the DearPyPixl item registry of items whose tags do not exist
        in the DearPyGui item registry.
        """
        # There should not be many situations where a strong reference exists
        # in __registry__[0], but the item itself is non-existant in the
        # DearPyGui registry. It can happen if DearPyPixl items aren't deleted
        # correctly I guess.
        # TODO: Set this to run every *n*th frame for the application.
        appitem_reg = cls.__registry__[0]
        pop_appitem = appitem_reg.pop
        deleted_item_uuids = {tag for tag in appitem_reg} - set(get_all_items())
        for item_uuid in deleted_item_uuids:
            pop_appitem(item_uuid, None)


    def _err_if_existential_crisis(self) -> None | SystemError | TypeError:
        """Raise SystemError if this item exists in DearPyPixl but not DearPyGui.
        """
        if not does_item_exist(self._tag):
            raise SystemError(f"This item does not or no longer exists; possibly deleted.")
        return None

    def _err_if_root_item(self) -> None | TypeError:
        """Raise TypeError if this item is a root item and cannot be moved.
        """
        if self.__is_root_item__:
            raise TypeError(f"Could not move item; {type(self).__qualname__!r} is a root item.")
        return None


    #### Work-In-Progress ####
    def _export_configuration(self, **kwargs) -> dict[str, Any]:
        item_type       = type(self)
        dft_init_params = {p.name: p.default for p in item_type.__internal__[4].values()}
        export_config   = {
            "item"  : item_type.__qualname__,
            "tag"   : self._tag,
            "parent": self.parent
        }
        return export_config | dft_init_params | self.configuration()


class Template(MutableMapping, metaclass=ABCMeta):
    __slots__ = (
        "__is_container__" ,
        "__is_root_item__" ,
        "__is_value_able_" ,
        "__able_parents__" ,
        "__able_children__",
        "__command__"      ,
        "tag"              ,
        "is_container"     ,
        "is_root_item"     ,
        "is_value_able"    ,
        "_parameters"      ,
    )

    _factory: ItemT
    tag     : int | str

    def __init__(self, **config):
        self.is_container
        self.is_root_item
        self.is_value_able
        self._parameters = self._factory.__internal__[4]
        self.configure(**config)

    def __repr__(self) -> str:
        return f"<class {type(self).__qualname__!r}>"

    def __call__(self, **config) -> ItemT:
        kwargs = self.configuration() | config
        return self._factory(**kwargs)

    def __getitem__(self, attr: str) -> Any:
        return getattr(self, attr)

    def __setitem__(self, attr: str, value: Any) -> None:
        return setattr(self, attr, value)

    def __getattr__(self, attr: str) -> Any:
        # The signature for templates is intended to mimic the actual
        # item. Several features are unavailable because the item
        # has not been created yet.
        if attr in dir(self._factory):
            raise self._not_implemented(attr)
        raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {attr!r}.")
    
    def __iter__(self):
        yield from self._parameters

    def __len__(self) -> int:
        return len(self._parameters)

    def _not_implemented(self, attr: str, *args, **kwargs) -> NotImplementedError:
        # In a function to play nice-nice w/__slots__.
        return NotImplementedError(f"{attr!r} member is not available as a template.")

    def configure(self, **config) -> None:
        return Item.configure(self, **config)

    def configuration(self) -> dict[str, Any]:
        return {attr:getattr(self, attr) for attr in self._parameters}
