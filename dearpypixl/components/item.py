"""Basic type implementations for DearPyPixl."""
import functools
import itertools
from abc import ABCMeta, abstractmethod
from enum import IntEnum
from inspect import signature, isabstract, Parameter, _VAR_POSITIONAL, _KEYWORD_ONLY
from typing import Callable, Any, TypeVar, MutableMapping, Iterator, NamedTuple, Iterable, Literal
from typing_extensions import Self
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
    get_item_info as _get_item_info,
    get_item_state as _get_item_state,
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

# TODO: Finish __itemtype_id__ implementation and cleanup ItemIndex remnants.
# TODO: Deal w/strong references in __registry__.
# TODO: Move error helper functions out of Item namespace and into their own
# module. Implement better exception when thrown at item creation.

__all__ = [
    # TypeVars
    "ItemT",
    "TemplateT",

    # Classes
    "Item",
    "ItemType",
    "RegistryType",
    "InternalType",
    "ItemIdType",

    # Helper functions
    "prep_callback",
    "prep_init_args",
    "get_positional_args_count",
    "set_cached_attribute",
    "register_item",
    "refresh_registry",
]


ItemT     = TypeVar("ItemT"    , bound="ItemType")
TemplateT = TypeVar("TemplateT", bound="TemplateType")


##########################################
######### Misc. Helper Functions #########
##########################################
def get_positional_args_count(obj: Callable) -> int:
    """Return the number of positional arguments for a given object.
    """
    # Emulating how DearPyGui doesn't require callbacks having 3 positional
    # arguments. Only pass sender/app_data/user_data if there's "room" to 
    # do so.
    pos_arg_cnt = 0
    for param in signature(obj).parameters.values():
        if param.kind == _VAR_POSITIONAL:
            pos_arg_cnt = 3
        elif param.kind != _KEYWORD_ONLY:
            pos_arg_cnt += 1

        if pos_arg_cnt >= 3:
            pos_arg_cnt = 3
            break
    return pos_arg_cnt


def prep_callback(obj, _callback: Callable | None):
    """DearPyGui callback wrapper.
    """
    @functools.wraps(_callback)
    def callable_object(_=None, app_data=None, user_data=None, **kwargs):
        args = (obj, app_data, user_data)[0:pos_arg_cnt]
        _callback(*args, **kwargs)
    # Wrapping is done for a couple of reasons. Firstly, to ensure that
    # the Item instance of `sender` is returned instead of the identifier.
    # And second; nuitka compilation doesn't like DPG callbacks unless
    # they are wrapped (lambda, etc.)...for some reason.
    if callable(_callback):
        wrapper = callable_object
        pos_arg_cnt = get_positional_args_count(_callback)
    elif _callback is None:
        wrapper = None
    else:
        raise ValueError(f"`callback` is not callable (got {type(_callback)!r}.")
    return wrapper


def prep_init_args(obj: ItemT, **kwargs) -> dict:
    """Readies initializer arguments;
        - Wraps callback-related arguments so they conform to the rest
        of the library
        - Recast int-like values so they are accepted by DearPyGui's
        Python parser.
        - Cache the initial value of managed attributes inaccessable
        through DearPyGui.

    Args:
        * obj (ItemT): The ItemType instance to initialize.
        * kwargs (keyword-only): Arguments used to create an item.
    """
    cached_members = obj.__cached__
    # `user_data` should be excluded from type casting as it is allowed
    # to be anything.
    user_data = kwargs.pop("user_data", None)
    for arg, val in kwargs.items():
        # This wraps all callback-related arguments so that the `sender`
        # is the instance object instead of just the item identifier.
        if "callback" in arg and val:  # callback, drag_callback, drop_callback
            kwargs[arg] = prep_callback(obj, val)
            continue
        # Recasting int-like values. This includes other Item instances that
        # would be used as parents, or integer enums members.
        if isinstance(val, (Item, IntEnum)):
            kwargs[arg] = int(val)
        # Storing attributes that cannot be fetched from DPG on instance.
        # Otherwise, they not be accessible later.
        if arg in cached_members:
            cached_members[arg] = val
    # There's no harm in including user_data if it's None since every item
    # should accept it as an argument.
    kwargs["user_data"] = user_data
    return kwargs


def set_cached_attribute(__obj, __name, value) -> None:
    """Convenience function for setting the cached value of an attribute.
    """
    __obj.__cached__[__name] = value


def register_item(item: ItemT):
    """Add an ItemType instance to the global registry.
    """
    ItemType.__registry__[0][item.tag] = item


def refresh_registry():
    """Clear the DearPyPixl item registry of items whose tags do not exist
    in the DearPyGui item registry.
    """
    # There should not be many situations where a strong reference exists
    # in __registry__[0], but the item itself is non-existant in the
    # DearPyGui registry. It can happen if DearPyPixl items aren't deleted
    # correctly I guess.
    registry = ItemType.__registry__[0]
    pop_func = registry.pop
    deleted_item_uuids = {tag for tag in registry} - set(get_all_items())
    for item_uuid in deleted_item_uuids:
        pop_func(item_uuid, None)




##########################################
######### Item Member Management #########
##########################################
CONFIG = "configuration"
INFORM = "information"
STATES = "state"


class ItemAttribute:
    """Descriptor object for managing DearPyGui item attributes. Functionally similar
    to the `property` built-in, but cannot be used as a decorator (for a usable deco-
    rator, see the `register_member` class method).
    """
    _manager_commands     = {}
    next_class_item_attrs = {
        CONFIG  : set(),
        INFORM  : set(),
        STATES  : set(),
        "cached": set(),
    }

    def __init__(
        self                                                                  ,
        category    : Literal["configuration", "information", "state"]        ,
        getter      : str | Callable                                          ,
        setter      : str | Callable | None                                   ,
        target      : str                                              =  None,
        doc         : str                                              =  None,
        cache_on_set: bool                                             = False,
    ):
        """Args:
            * category (str): Value should be `configuration`, `information` or `state`.
            * getter (str | Callable | None): Object to call that will return the
            attribute value. If the command is registered, the name of the command is also
            an accepted value. A call to the object must be able be resolved using the same
            arguments required for `getattr`.
            * setter (str | Callable | None): Object to call that will set the value of an
            attribute. If the command is registered, the name of the command is also
            an accepted value. A call to the object must be able to be resolved using the same
            arguments required for `setattr`.
            * target (str): This is used to get the value instead of self._name. Defaults
            to None.
            * doc (str): Docstring for the attribute. Defaults to None.
            * cache_on_set (bool): If True, <fset> will be altered to store a copy of the
            value on the item instance. This is used if a configuration attribute can be
            set but not accessed from DearPyGui. Defaults to None.

            NOTE: The `target` parameter mainly exists due to minor typos in DearPyGui's
            item configuration. 
        """
        if doc is None and getter is not None:
            doc = getter.__doc__
        if setter is None:
            self.__set__ = self._readonly_setter

        self.category     = category
        self.fget         = getter  
        self.fset         = setter
        self.target       = target
        self.cache_on_set = cache_on_set

        self.__doc__ = doc
        self._name   = ''

    def __set_name__(self, __type: type, name: str):
        self._name  = name
        self.target = name if not self.target else self.target
        
        if self.category not in self.next_class_item_attrs:
            raise ValueError(f"`category` must be 'configuration', 'state', or 'information' (got {self.category!r}).")

        # There's a little bit of repeated code here, but it's not enough to
        # motivate met to condense it.
        fget = self.fget
        if isinstance(fget, str):
            try:
                fget = self._manager_commands[fget]
            except KeyError:
                raise ValueError(f"No registered command found for {fget!r}.")
        elif callable(fget):
            self.register_manager(fget)
        else:
            raise ValueError(f"{fget!r} value is not a registered command, or has the incorrect signature.")
        self.fget = fget

        fset = self.fset
        if fset is not None:
            if isinstance(fset, str):
                try:
                    fset = self._manager_commands[fset]
                except KeyError:
                    raise ValueError(f"No registered command found for {fset!r}.")
            elif callable(fset):
                self.register_manager(fset)
            else:
                raise ValueError(f"{fset!r} value is not a registered command, or has the incorrect signature.")
            
            if self.cache_on_set:
                fset = self._cached_attribute(fset)
            self.fset = fset

        self.next_class_item_attrs[self.category].add(name)
        # Mark attribute as cached if necessary.
        # TODO: Implement a less piss-poor way to do this.
        if "cache" in self.fget.__qualname__:
            self.next_class_item_attrs["cached"].add(name)

    def __get__(self, instance: object, _type: type):
        if instance is None:
            return self
        return self.fget(instance, self.target)

    def __set__(self, instance: object, value):
        self.fset(instance, self.target, value)

    def _readonly_setter(self, instance: object, value):
        # Replaces self.__set__ for read-only attributes.
        raise AttributeError(f"Cannot set read-only attribute {self._name!r}.")
    
    @staticmethod
    def _cached_attribute(func: Callable):
        # This alters the behavior of self.fset to cache a copy of the new
        # value on the instance (see `cache_on_set` parameter).
        def attribute_setter(__obj: object, __name: str, value: Any):
            func(__obj, __name, value)
            set_cached_attribute(__obj, __name, value)
        return attribute_setter


    #### Decorators ####
    @classmethod
    def register_manager(cls, func: Callable):
        """(Decorator) Registers a function as an item attribute command. The name of a
        registered command (string) can be passed as the getter/setter argument
        for an `ItemAttribute` instance."""

        cls._manager_commands[func.__qualname__] = func
        return func

    @classmethod
    def register_member(cls, cls_attribute: Callable | str = None, *, category: Literal["configuration", "information", "state"]):
        """(Decorator) Alternative to using the `ItemAttribute` descriptor. Registers class-
        defined attributes that are to be managed as item attributes without using the
        descriptor.

        Args:
            * cls_attribute (Callable | str): The attribute to register. If it is a method,
            `cls_attribute.__name__` is registered.
            * category (Literal, keyword-only): Category to register the attribute under.
            Must be "configuration", "information", or "state".

        Examples:
        >>> class ProtoItem:
        ...     x = item_attribute("x", category="configuration")
        None
        >>> class ProtoItem:
        ...     @property
        ...     @item_attribute(category="configuration")
        ...     def config_property(self):
        ...         ...
        None
        """

        @functools.wraps(cls_attribute)
        def register(obj):
            # Register the attribute by category.
            if isinstance(obj, str):
                name = obj
            elif callable(obj):
                # `obj` should be a method
                name = obj.__name__
            else:
                raise ValueError(f"`obj` must be a string or callable method (got {type(obj)!r}).")
                
            try:
                cls.next_class_item_attrs[category].add(name)
            except KeyError:
                raise ValueError(f"`category` must be 'configuration', 'state', or 'information' (got {category!r}).")
            return obj
        
        if cls_attribute:
            return register(cls_attribute)
        return register


# Member Getters
@ItemAttribute.register_manager
def get_item_config(__o: object, __name: str):
    return get_item_configuration(__o._tag)[__name]


@ItemAttribute.register_manager
def get_item_info(__o: object, __name: str):
    return _get_item_info(__o._tag)[__name]


@ItemAttribute.register_manager
def get_item_state(__o: object, __name: str):
    return _get_item_state(__o._tag)[__name]


@ItemAttribute.register_manager
def get_item_cached(__o: object, __name: str):
    # Pull private attribute.
    return __o.__cached__[__name]


@ItemAttribute.register_manager
def get_item_value(__o: object, __name: str = None):
    return get_value(__o._tag)


# Member Setters
@ItemAttribute.register_manager
def set_item_config(__obj: object, __name: str, value: Any):
    configure_item(__obj._tag, **{__name: value})


@ItemAttribute.register_manager
def set_item_value(__obj: object, __name: str, value: Any):
    # `value`, `default_value`
    set_value(__obj._tag, value)


@ItemAttribute.register_manager
def set_item_callback(__obj: object, __name: str, value: Any):
    configure_item(__obj._tag, **{__name: prep_callback(__obj, value)})




######################################
##### Lower-Level Structures/API #####
######################################
class RegistryType(NamedTuple):
    """Contains references to Item objects.

    Args:
        * items (dict[int, ItemT]): Contains references to Item instances
        as `{instance.tag: instance}`.
        * types (dict[str, type[ItemT]]): Contains references to created
        Item types as `{type(ItemT).__qualname__: type(ItemT)}`.
    """
    # TODO: Use weakrefs.
    items: dict[int, ItemT]       = {}
    types: dict[str, type[ItemT]] = {}


class InternalType(NamedTuple):
    """Contains data collections used internally by DearPyPixl.

    Args:
        * config_members (tuple[str, ...]): Managed configuration attributes.
        * inform_members (tuple[str, ...]): Managed information attributes.
        * states_members (tuple[str, ...]): Managed states attributes.
        * cached_members (tuple[str, ...]): Managed configuration attributes
        that are stored in `__cached__`. These attributes cannot be fetched
        from DearPyGui.
        * init_params (dict[str, Parameter]): Parameters passed to the
        constructor to create instances of this Item type (collected
        from all classes in its inheritance tree).
        * template_item (TemplateT): The bound Template object created
        specifically for this Item type.
    """
    config_members: tuple[str, ...]      = ()
    inform_members: tuple[str, ...]      = ()
    states_members: tuple[str, ...]      = ()
    cached_members: tuple[str, ...]      = ()
    init_params   : dict[str, Parameter] = {}
    template_item : TemplateT            = None


class ItemIdType(NamedTuple):
    """Contains information regarding an item type's identity. Converting to an
    integer or string will return the appropriate value.

    Args:
        * integer (int): The enum value used internally by DearPyGui representing
        the item's type.
        * string (str): The name of the item type used internally by DearPyGui.
       It should be the result of
       `dearpygui.get_item_info(self.tag)["type"].split('::')[-1]`.
    """
    integer: int
    string : str

    def __int__(self) -> int:
        return self[0]

    def __str__(self) -> str:
        return f"mvAppItemType::{self[1]}"

        
class ItemType(metaclass=ABCMeta):
    """Lowest-level parent class for Item subclasses. Provides default values of
    internally used attributes, and ensures expected functionality of inherited
    managed item members. All Item-related types, including mixin types,
    should be directly or indirectly derived from this object.

    Attributes:
        * __registry__ (RegistryType): Stores references to Item objects. This
        is never dynamically assigned, and should NOT be redefined on subclasses.

        * __internal__ (InternalType): Stores collections of data used internally
        by DearPyPixl. The structures containing information regarding managed
        attributes are collected from the managed item attributes registered for
        the ItemType. -- merged into a copy of the identical structure from the
        derived type. Similarly, the initialization parameters structure includes
        the parameters of the entire inheritance tree, including those for the
        new type. This attribute is assigned to new derived ItemType classes when 
        they are created. Assigning directly on subclasses does nothing.

        * __cached__ (dict[str, Any]): Stores managed item attributes that cannot
        be accessed through the DearPyGui API. Some (configuration attributes) can
        still be properly set. Others are immutable once set via the constructor
        and are read-only. This attribute is automatically assigned per ItemType
        instance, so redefining it on the class does nothing. 
        

        The following attributes should be redefined per derived ItemType as
        necessary;

        * __itemtype_id__ (ItemTypeIdType | None): A sequence containing informa-
        tion used internally by DearPyGui regarding an item type's identity. It
        may be set to None to indicate that the item type is "complex". A complex
        item type does not (or cannot) associate with an existing type. Examples
        include ItemTypes that are only item-like (it exposes only a part of the
        Item API), or compound types that are created with or manage more than
        one type of item.

        * __is_root_item__ (bool): If True, instances of this ItemType cannot be
        parented by any type of item. `__is_container__` should also be True.

        * __is_container__ (bool): If True, instances of this ItemType can parent
        other items.

        * __able_parents__ (tuple[str, ...]): A sequence of ItemType names that
        items of this type can parent. If empty, then instances of this ItemType
        are known to parent most items.

        * __able_children__ (tuple[str, ...]): A sequence of ItemType names that
        can parent instances this type. If empty, then most container ItemType
        instances can parent instances of this ItemType.

        * __is_value_able__ (bool): If True, then instances of this ItemType can
        hold a value when once is set. The type of the value can vary between
        item types.

        * __command__ (Callable): An object with a defined `__call__` method
        that, when invoked, (in)directly calls the appropriate DearPyGui command
        that creates an item of this type and returns its unique identifier.

        NOTE: Redefining the `__able_parents__` or `__able_children__` attributes
        does not extend the sequence of parents/children inherited from the parent
        type. As expected, it literally redefines the attribute.
    """
    # This section is pretty comment-heavy because I have the short-term
    # memory of a tunafish.

    @abstractmethod
    def tag(self) -> int: ...

    __slots__ = ()

    # "Convention" discourages the use of custom dunder members. These
    # attributes fall somewhere in the middle of public and private. To
    # avoid namespace collisions without obfuscating them, all internally
    # -used members are dunder attributes.
    __registry__      : RegistryType   = RegistryType()
    __internal__      : InternalType   = InternalType()
    __cached__        : dict[str, Any] = {}
    
    __itemtype_id__   : ItemIdType | None = None
    __is_root_item__  : bool                  = False
    __is_container__  : bool                  = False
    __able_parents__  : tuple                 = ()
    __able_children__ : tuple                 = ()
    __is_value_able__ : bool                  = False
    __command__       : Callable              = None
    # The `__constants__` attribute is also defined on many items. This is
    # not (and likely won't be) used by the Item API. It contains the names
    # of constants in DearPyGui that are associated with that item type
    # (i.e. it's for "me").

    def __init_subclass__(cls):
        super().__init_subclass__()
        ##############################################################################
        # [Section 1] Controlling (Inherited) Item Members                           #
        # [Section 2] Item Class Template                                            #
        # [Section 3] Container Context Control                                      #
        # [Section 4] Item Registration                                              #
        #                                                                            #        
        ##############################################################################
        
        # TODO: Possibly apply a `value` property on `Item`, and set the setter
        # here if the item is value-able.

        #### [Section 1] #############################################################
        # Merging the parent class's __init__ parameters into its own. That way,
        # the "complete signature" of the item class can be easily retrieved
        # even after subclassing. Less mro traversal.
        parent_cls      = cls.mro()[1]
        parent_internal = getattr(parent_cls, "__internal__", ItemType.__internal__)

        # Managed item members are stored via `ItemAttribute`.
        config_members  = [*ItemAttribute.next_class_item_attrs[CONFIG]]
        inform_members  = [*ItemAttribute.next_class_item_attrs[INFORM]]
        states_members  = [*ItemAttribute.next_class_item_attrs[STATES]]
        cached_members  = [*ItemAttribute.next_class_item_attrs["cached"]]
        init_params     = parent_internal[4] | dict(signature(cls).parameters)
        init_params.pop("kwargs", None)  # Don't need this.

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
        # There's no need to create a template for a class that is never instantiated,
        # so we avoid ABC's (also when registering the "Item" class an error would be
        # thrown as the template base class is is defined after it).
        if not isabstract(cls):
            template = type(
                f"{cls.__qualname__}Template",
                (TemplateType,),
                {"__slots__"        : tuple(cls.__internal__[4].keys()),
                 "_factory"         : cls                              }
            )
        else:
            template = None
        

        #### [Section 3] #############################################################
        # [4/28/2022] The `Container` class was removed in favor of this.
        # If the item is a container, set the appropriate methods so it can be used as
        # a context manager. However, don't overwrite an existing implementation.
        if cls.__is_container__:
            if not hasattr(cls, "__enter__"):
                cls.__enter__ = cls.__enter
            if not hasattr(cls, "__exit__"):
                cls.__exit__  = cls.__exit


        #### [Section 4] ############################################################
        # Finalize and register new item type...
        cls.__internal__ = InternalType(
            tuple(config_members),  # <  Several methods defined on the `Item` class
            tuple(inform_members),  # <  are dependant on these collections. An
            tuple(states_members),  # <  attribute included in any of these can be
            tuple(cached_members),  # <  considered "registered".
            init_params,           
            template,                  
        )
        # Only registering Item classes that can be instantiated.
        # For the sake of readability, `isabstract` is unnecessarily called
        # again just so I can keep these sections seperate.
        if not isabstract(cls):
            cls.__registry__[1][cls.__qualname__] = cls
        # Clear the item member registry cache for the next derived class.
        # NOTE: Shit gets weird if this cache is populated outside of an
        # appropriate class body.
        # TODO: Deal with the above. Bugs relating to the `ItemAttribute`
        # descriptor are annoying to find as-is. It doesn't need help.
        for collection in ItemAttribute.next_class_item_attrs.values():
            collection.clear()

    def __dir__(self) -> Iterable[str]:
        # Exclude name-mangled attributes from instance dir.
        # I'm not trying to completely obfuscate the internal
        # attributes, so I'm leaving the class dir alone.
        prefixes = {f"_{cls.__qualname__}__" for cls in type(self).mro()}
        return [attr for attr in super().__dir__()
                if not any(attr.startswith(prefix)
                for prefix in prefixes)]

    def __enter(self):
        push_container_stack(self.tag)
        return self

    def __exit(self, exc_type, exc_instance, traceback):
        pop_container_stack()




#####################################
######## High-Level Item API ########
#####################################
class Item(ItemType, metaclass=ABCMeta):
    """Base class for object-oriented DearPyGui items.

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
        * get_able_parents (classmethod)
        * get_able_children (classmethod)
        * configure
        * configuration
        * information
        * state
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
    # Internal members and abstract methods are toward the bottom.

    @classmethod
    def raw_init(cls, **config) -> int | str:
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
        """Return a an instance of the ItemType's template class; a mapping-like
        factory object that can create instances of items from a freely-customizable
        default configuration.

        Args:
            * config (keyword-only, optional): Used as default arguments when creating
            future items.
        """
        configuration = {}
        empty         = Parameter.empty
        for param in cls.__internal__[4].values():
            default = None if param.default is empty else param.default
            configuration[param.name] = default

        configuration.pop("kwargs", None)
        configuration |= config
        return cls.__internal__[5](**configuration)


    #### Configuration Properties ####
    @property
    @ItemAttribute.register_member(category=CONFIG)
    def label(self) -> str:
        return get_item_configuration(self._tag)["label"]
    @label.setter
    def label(self, value: str) -> None:
        configure_item(self._tag, label=value)

    @property
    @ItemAttribute.register_member(category=CONFIG)
    def use_internal_label(self) -> str:
        return get_item_configuration(self._tag)["use_internal_label"]
    @use_internal_label.setter
    def use_internal_label(self, value: str) -> None:
        configure_item(self._tag, use_internal_label=value)

    @property
    @ItemAttribute.register_member(category=CONFIG)
    def user_data(self) -> str:
        return get_item_configuration(self._tag)["user_data"]
    @user_data.setter
    def user_data(self, value: str) -> None:
        configure_item(self._tag, user_data=value)


    #### Information Properties ####
    @property
    @ItemAttribute.register_member(category=INFORM)
    def tag(self) -> int:
        """Return this item's unique integer identifier.
        """
        return self._tag

    @property
    @ItemAttribute.register_member(category=INFORM)
    def alias(self) -> str | None:
        """Return this item's unique string identifier.
        """
        return get_item_alias(self._tag) or None

    @property
    @ItemAttribute.register_member(category=INFORM)
    def parent(self) -> 'Item':
        """Return the direct progenitor of this item.
        """
        return self.__registry__[0].get(_get_item_info(self._tag)["parent"], None)

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls.__is_container__

    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def is_root_item(cls) -> bool:
        """Return True if this item does not require a parent item to exist
        (and cannot be parented by other items).
        """
        return cls.__is_root_item__
    
    @classmethod
    @property
    @ItemAttribute.register_member(category=INFORM)
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls.__is_value_able__


    #### States Properties ####
    @property
    @ItemAttribute.register_member(category=STATES)
    def is_ok(self) -> bool:
        """Return True if the item is render-able.
        """
        return _get_item_state(self._tag)["ok"]

    @property
    @ItemAttribute.register_member(category=STATES)
    def is_enabled(self) -> bool:
        """Return True if the item is not disabled.
        """
        return get_item_configuration(self._tag)["enabled"]


    #### Methods ####
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

    def configuration(self) -> dict[str, Any]:
        """Return the configurable options used to manage this item, along
        with their current values.

        This is not an exact equivelent of DearPyGui's `configure_item`
        function. If the option is not included as a parameter in signature
        of `type(self).__init__`, it is not considered to be "configuration"
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
        states = {f"is_{state}":v for state, v in _get_item_state(self._tag).items()}
        item_states_attrs = self.__internal__[2]
        return {attr:(states[attr] if attr in states else
                getattr(self, attr)) for attr in item_states_attrs}

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

    def move(self, parent: ItemT | int = 0, before: ItemT | int = 0, **kwargs) -> None:
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
                if _get_item_info(before)["parent"] != parent:
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

    def copy(self, _recursive: bool = True, **config) -> Self:
        """Return a newly-created item of this item's type using it's current
        configuration as arguments.

        Args:
            * _recursive (bool, optional): If True, all item children will also be
            duplicated. Default is True.
            * config (keyword-only, optional): The arguments to include when creating
            creating the direct copy item (not children, if <_recursive> is True).
            They will be merged into a copy of this item's current configuration before
            sending it to the constructor.
        """
        # NOTE: Understand that copied items will also honor bound item states that
        # are available as constructor parameters (such as `theme` and `events` for
        # `Widget` derivatives). Since they are independent of the item's tree they
        # will not be copied. However, they are registered as configuration attrib-
        # utes, so references to these items will be passed to the item's construc-
        # tor (inherited from the original item's configuration) where they will be
        # bound.

        cls = type(self)
        configuration = self.configuration() | config

        # Add an explicit parent if the copy item supports it (as it is not included
        # in self.configuration()).
        if not cls.is_root_item and "parent" not in config:
            configuration["parent"] = self.parent

        # If the item supports `pos`, accessing the value from DearPyGui will return
        # [0, 0] regardless if the argument was left as the default empty sequence on
        # creation. The problem is that [0, 0] is an actual value, so the copy item's
        # position will be set as such if passed as-is to the constructor. Because it
        # is uncommon that this value is purposeful and "real", a value of [0, 0] is
        # replaced with the accepted version of "None".
        if "pos" in config:  # was explicitly included, so honor it regardless.
            ...
        elif configuration.get("pos", None) == [0, 0]:
            configuration["pos"] = []

        self_copy = cls(**configuration)

        # Make sure to set the copy item's value to match the real item's value.
        # `default_value` is not always included as an argument when an item is
        # value-able, and it isn't known if other arguments would set the internal
        # value. So the value is copied over only if the copy item's value is None
        # after it has been created.
        if cls.is_value_able and getattr(self_copy, "value", None) is None:
            dearpygui.set_value(self_copy._tag, self.value)

        # Recursively copy the children, ensuring that the copied item parents
        # them.
        if _recursive:
            for child in self.children():
                child.copy(recursive=_recursive, parent=self_copy)

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
        refresh_registry()

        if not children_only:
            del self

    def focus(self, **kwargs) -> None:
        """Brings an item into focus. Does nothing if the item cannot be
        displayed.
        """
        focus_item(self._tag)

    def toggle(self, **kwargs) -> None:
        """If the item supports `show`, hide/show the item. Does nothing if
        `show` is not a invalid configuration option.
        """
        # Because configuration attributes are exposed as properties and several
        # DPG items don't support `show`, I'm not inclined to define a `show` function.
        # Wrapping `window.show = True/False` in a lambda for a callback is
        # kinda dumb though so I wanted to make something user and callback friendly.
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
        original position. Does nothing if `pos` is not a valid configuration
        option.
        """
        try:
            reset_pos(self.tag)
        except SystemError:
            pass

    ######################
    ###### END API #######
    ######################

    __slots__ = ("_tag")

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
        self.__cached__ = dict.fromkeys(self.__internal__[3], None)

        kwargs = prep_init_args(self, **kwargs)

        # If `tag` is a string or None, generate an new integer id.
        identifier = kwargs.pop("tag", None) or generate_uuid()
        alias      = None
        if isinstance(identifier, str):
            alias      = identifier
            identifier = generate_uuid()
        try:
            self._tag = type(self).__command__(tag=identifier, **kwargs)
        except SystemError:
            raise SystemError(f"Error creating {type(self).__qualname__!r} item. Verify that the arguments are appropriate.")
        # If `tag` was a string, it is an alias and should be set as such.
        alias and add_alias(alias, identifier)
        register_item(self)

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
        if not isinstance(other, ItemType):
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
        row_id           = _get_item_info(self._tag)["children"][1][row_idx]
        row_child_id     = _get_item_info(row_id)["children"][1][col_idx]
        return self.__registry__[0][row_child_id]

    ## private/internal methods ##
    def _children(self) -> Iterator[list[int]]:
        """Private `children` method. Yields children's tags.
        """
        # Unlike the public `children` method, this one is an iterator
        # yielding "raw" children. This is preferrable functionality
        # for some things.
        yield from _get_item_info(self._tag)["children"].values()

    def _item_tree(self) -> list['Item', list['Item', list]]:
        tree        = [self, []]
        child_slots = [*_get_item_info(self._tag)["children"].values()]
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


class TemplateType(MutableMapping, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def _factory(cls) -> ItemT: ...

    __slots__    = ("_tag")  # subclasses should also include __slots__

    # Pull various read-only members from the owner item type. The
    # signature of the method that returns a template instance is
    # set to the ItemType and not the template, so I can get away
    # with being lazy here without fear of mucking up introspection.
    for __attr in ("__registry__"     ,
                   "__internal__"     ,
                   "__itemtype_id__"  ,
                   "__is_root_item__" ,
                   "__is_container__" ,
                   "__able_parents__" ,
                   "__able_children__",
                   "__is_value_able__",
                   "__command__"      ,
                   "is_container"     ,
                   "is_root_item"     ,
                   "is_value_able"    ,
                   "get_able_parents" ,
                   "get_able_children"):
        exec(f"{__attr} = property(lambda self: getattr(self._factory, '{__attr}'))")

    def __init__(self, **config):
        self._tag        = None
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

    def __delitem__(self):
        return NotImplemented

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

    def configure(self, **config) -> None:
        return Item.configure(self, **config)

    def configuration(self) -> dict[str, Any]:
        return {attr:getattr(self, attr) for attr in self._parameters}

    @property
    def tag(self) -> int | str | None:
        return self._tag
    @tag.setter
    def tag(self, value: int | str | None) -> None:
        self._tag = value

    @property
    def _parameters(self) -> dict[str, Parameter]:
        return self.__internal__[4]

    def _not_implemented(self, attr: str, *args, **kwargs) -> NotImplementedError:
        return NotImplementedError(f"{attr!r} member is not available as a template.")
