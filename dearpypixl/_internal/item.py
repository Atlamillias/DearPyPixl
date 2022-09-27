import itertools
import logging
import inspect
from types import MappingProxyType
from functools import singledispatchmethod as overloadmethod
from itertools import chain
from abc import ABCMeta, abstractmethod
from enum import IntEnum
from inspect import signature, Parameter
from typing import (
    get_type_hints,
    Any,
    Callable,
    TypeVar,
    Mapping,
    MutableMapping,
    Sequence,
    ParamSpec,
)
from typing_extensions import Self
from dearpygui import dearpygui
from dearpygui._dearpygui import (
    push_container_stack,
    top_container_stack,
    pop_container_stack,
    does_item_exist,
    reset_pos,
    add_alias,
    generate_uuid,
    get_item_alias,
    unstage,
    get_item_info,
    get_item_state,
    get_item_configuration,
    configure_item,
    move_item,
    move_item_up,
    move_item_down,
    focus_item,
    delete_item,
)
from . import registry
from . import errors
from .members import ItemMember
from .callback import Event, EventStack, Sender, AppData, UserData
from .utilities import (
    classproperty,
    generate_itemtype_uuid,
    is_itemtype_public_api,
    get_class_members,
)
from .members import (
    PixlPCategory,
    ItemMember,
    ItemPSetter,
    ItemPGetter,
    CONFIG,
    INFORM,
    STATES,
)
from .comtypes import Null, ItemTMember


ItemT = TypeVar("ItemT", bound="Item")
_P = ParamSpec("_P")

ITEM_METADATA = "__dearpypixl__"


class ItemData(Mapping):
    """Contains ItemType metadata. Assists in the registration of managed item type
    members into one of three managed categories. It is expected that the contents
    of this structure are NOT altered outside of an ItemType's creation once bound.


    DearPyPixl uses three classifications for "attributes" exposed or managed through
    various DearPyGui functions; "configuration", "information", and "state". Although
    they may be familiar through use of the DearPyGui API, these categories are given
    different (and more rigid) definitions as to what members are included in each.


    **Configuration**

    An exposed ItemType member that is included in the return of
    `ItemType().configuration()` that is also a parameter to create an instance of
    its type. As such, a parameter of the same name MUST exist in at least
    ONE `__init__` method that is invoked on ItemType instantiation -- The result of
    `ItemType().configuration()` should be accepted in the constructor of its type i.e.
    `Window(**Window().configuration())` should produce an instance of `Window` without
    error (ideally, a near copy). The exposed member is not necessarily required to be
    writable, but should be in almost all user-defined cases.

    There are exceptions of the former in this library; all of them due to DearPyGui's
    behavior. However, most of them have been re-classified as "information". The sole
    option moved into configuration from another category is `pos`, which readable through
    `dpg.get_item_state()` but writable through `dpg.configure_item(pos=...)`.

    Those who want to include user-defined members as configuration should adhere to
    the above.


    **Information**

    An exposed ItemType member that is included in the return of
    `ItemType().information()`. All members in this category are considered
    "read-only" and should not be directly writable. Parameters of the same name
    may or may not be used to create the item. If they can, they should be optional arguments.

    Some parameters used in the DearPyGui API such as "default_value" are not configurable
    options outside of it's creation i.e. `dpg.configure_item(default_value=...)`.
    Even though `default_value` is a valid argument used in item creation, it has
    been categorized as information in DearPyPixl since it cannot be updated directly and
    is not a required argument of an ItemType's constructor. Other common examples include
    `tag` (optionally used to create items, 100% read-only) and `parent` (optionally used
    to create items, changes w/various "move" methods).

    Users are free to add members to this category even if the member's name matches a
    required argument in the ItemType's constructor.

    Insightful fun-fact; DearPyPixl handles `parent` uniquely as it is the only
    "pseudo-optional" argument commonly found in DearPyGui.


    **State**

    An exposed ItemType member that is included in the return of `ItemType().state()`.
    All members in this category should not be publicly writable. These values should
    reflect conditions of the item.

    In DearPyPixl, boolean states like `visible`,`toggled`, etc. follow a naming
    convention -- prefixed with `is_` (`is_visible`, `is_toggled`). States with other
    value types such as `content_region_avail` and `rect_size` are unchanged. Users
    are free to add members to this category however they choose with no restrictions.
    """
    __slots__ = (
        "_identity",
        "command",
        "is_container",
        "is_root_item",
        "is_value_able",
        "is_callable",
        "able_parents",
        "able_children",
        "commands",
        "constants",
        "parameters",
        "members",
        "repr",
        "template",
        "internal_only",
    )

    NULL = Null
    AUTO = "auto"

    __incl_repr = ("tag",)  # always included (and first) in repr
    __keys      = tuple((m.lstrip("_") for m in __slots__))

    def __init__(
        self,
        *,
        identity     : 'tuple[int, str] | AUTO'           = NULL,
        command      : Callable | None                    = NULL,
        is_container : bool                               = NULL,
        is_root_item : bool                               = NULL,
        is_value_able: bool                               = NULL,
        is_callable  : bool                               = NULL,
        able_parents : 'tuple[int | type[ItemType], ...]' = NULL,
        able_children: 'tuple[int | type[ItemType], ...]' = NULL,
        commands     : tuple[str, ...]                    = NULL,
        constants    : tuple[str, ...]                    = NULL,
        config       : Sequence[str]                      = (),
        inform       : Sequence[str]                      = (),
        states       : Sequence[str]                      = (),
        repr         : Sequence[str]                      = (),
        internal_only: bool                               = False,
    ):
        """NOTE: A value of NULL means that the value will be inherited from the bound ItemType's
        direct parent. Other behavior is unique to each parameter.

        Args:
            * identity (tuple[int, str] | Literal["auto"], optional): If the ItemType is a wrapped
            representation of an existing DearPyGui item type, then this should be a tuple containing
            both a numeric and string identifier for the bound ItemType. For compound or custom types,
            "auto" can be passed instead, creating a numeric and string identifier automatically. This
            is best left as default, as the bound ItemType will inherit this from its parent. Defaults
            to NULL.

            * command (Callable | None, optional): The (undecorated) DearPyGui command that, when invoked,
            creates an item and returns its unique identifier. Defaults to NULL.

            * is_container (bool, optional): If True, items of the bound ItemType can parent other items
            (does not affect actual item behavior, DOES AFFECT DEBUGGING, METHODS). If the ItemType does
            not defined `__enter__` or `__exit__` methods upon creation, the default implementation (container
            stack control) will be added. Setting to False will inverse this operation if `is_container` is
            True in the metadata of the ItemType's direct parent class. If the ItemType has custom non-default
            `__enter__ or `__exit__` methods, nothing is changed regardless of this value. Defaults to NULL.

            * is_root_item (bool, optional): If True, items of the bound ItemType cannot be parented by
            other items (does not affect actual item behavior, DOES AFFECT DEBUGGING, METHODS). This is
            best left as default. Defaults to NULL.

            * is_value_able (bool, optional): If True, items of the bound ItemType can store a value
            (documentation only, does not affect actual item behavior). If the ItemType does not have a `value`
            class attribute or property upon it's creation, a default `value` data descriptor is added to
            the ItemType's namespace. Setting to False will inverse this operation if `is_value_able` is True
            the metadata of the ItemType's direct parent class. If the ItemType has a custom non-default
            implementation of `value`, nothing is changed regardless of this value. Defaults to NULL.

            * able_parents (tuple[int | type[ItemType], ...], optional): A sequence of ItemType classes
            or their numeric identifiers (i.e. `int(type[ItemType])`). Items of the included types can
            parent those of the bound ItemType (does not affect actual item behavior, DOES AFFECT DEBUGGING,
            METHODS). Values will be inherited from the parent class' metadata only if this value
            NULL. Defaults to NULL.

            * able_children (tuple[int | type[ItemType], ...], optional): A sequence of ItemType classes
            or their numeric identifiers (i.e. `int(type[ItemType])`). Items of the included types can
            be parented by those of the bound ItemType (does not affect actual item behavior, DOES AFFECT
            DEBUGGING, METHODS). Values will be inherited from the parent class' metadata only if this value
            is NULL. Defaults to NULL.

            * commands (tuple[str, ...], optional): Misc. DearPyGui commands that, through
            some form of use, involve or include items of the bound ItemType. Not used or exposed
            otherwise through DearPyPixl's API. Defaults to NULL.

            * constants (tuple[str, ...], optional): Misc. DearPyGui constants that, through
            some form of use, involve or include items of the bound ItemType. Not used or exposed
            otherwise through DearPyPixl's API. Defaults to NULL.

            * config (Sequence[str], optional): Attributes to add to the member category
            "information". Members of the bound ItemType's direct parent class will also be
            included IF a member of the same name does not exist in the bound ItemType's namespace.
            Additionally, the `set_information` and `as_information` methods also add to this
            sequence. Defaults to ().

            * inform (Sequence[str], optional): Attributes to add to the member category
            "information". Members of the bound ItemType's direct parent class will also be
            included IF a member of the same name does not exist in the bound ItemType's namespace.
            Additionally, the `set_information` and `as_information` methods also add to this
            sequence. Defaults to ().

            * states (Sequence[str], optional): Attributes to add to the member category "state".
            Members of the bound ItemType's direct parent class will also be included IF a member
            of the same name does not exist in the bound ItemType's namespace. Additionally, the
            `set_state` and `as_state` methods also add to this sequence. Defaults to ().

            * repr (Sequence[str], optional): These attributes (and their values) will
            be included in the repr string for instances of the bound ItemType. Attributes
            are NOT required to belong to a managed category (i.e. configuration, information,
            state) to be included in the repr. This sequence will be merged with those of the
            bound ItemType's direct parent class. An attribute cannot be excluded through normal
            normal means once included. Additionally, various member registration methods can
            add to this sequence by including `repr=True`. Defaults to ().

            * internal_only (bool, optional): If True, the bound ItemType is not considered
            as part of the public API. Affects ItemType registration. Defaults to False.
        """
        self.identity      = identity
        self.command       = command
        self.is_container  = is_container
        self.is_root_item  = is_root_item
        self.is_value_able = is_value_able
        self.is_callable   = is_callable
        self.able_parents  = tuple((int(v) for v in able_parents)) if able_parents is not Null else able_parents
        self.able_children = tuple((int(v) for v in able_children)) if able_children is not Null else able_children
        self.commands      = tuple(commands) if commands is not Null else commands
        self.constants     = tuple(constants) if constants is not Null else constants
        self.internal_only = internal_only
        self.template      = None

        # recast in _finalize
        self.members = (set(config), set(inform), set(states), set())
        self.repr    = list(repr)
        self.parameters: dict[str, Parameter] = {}

    def __iter__(self):
        yield from self.__keys

    def __len__(self) -> int:
        return len(self.__keys)

    def __getitem__(self, key: str) -> Any:
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(f"{key!r}") from None

    def __setitem__(self, key: str, value):
        self.__setattr__(key, value)

    def _finalize(self):
        """Recasts several attribute values to make them immutable.
        """
        self.parameters   = MappingProxyType(self.parameters)
        self.members      = tuple(tuple(coll) for coll in self.members)
        self.repr = tuple(self.repr)

    @property
    def identity(self):
        return self._identity
    @identity.setter
    def identity(self, value) -> None:
        if not value:
            value = None
        elif value in (self.NULL, self.AUTO):
            ...
        elif isinstance(value, tuple) and len(value) == 2:
            enum_uuid, name_uuid = value
            if name_uuid.startswith("mv"):
                value = (enum_uuid, f"mvAppItemType::{name_uuid}")
        else:
            raise ValueError("Must be a two-value tuple or None.")
        self._identity = value

    @classmethod
    def origin(cls, itemtype: ItemT) -> ItemT:
        """ItemType class decorator. Finalizes type metadata after class
        creation. It should only be used once, on the base ItemType class.
        """
        itemtype.__dearpypixl__._finalize()
        return itemtype

    @classmethod
    def build(cls, itemtype: type["ItemType"]) -> Self:
        """Create and set the metadata for a (new) item type."""
        if ITEM_METADATA not in itemtype.__dict__:
            setattr(itemtype, ITEM_METADATA, cls())

        itemtype_mdata: ItemData = itemtype.__dict__[ITEM_METADATA]

        # Search for a parent's metadata structure (the first one found).
        for base_cls in itemtype.__bases__:
            parent_mdata: ItemData = getattr(base_cls, ITEM_METADATA, None)
            if parent_mdata:
                break
        else:  # This should not happen.
            raise RuntimeError(f"Unable to create ItemType subclass {itemtype.__qualname__} -- no parent metadata.")

        # Update the new ItemType's parameters as a culmination of all parameters
        # of all constructors in its inheritance tree.
        _type_hints = get_type_hints(itemtype.__init__) | {"kwargs": None}  # __future__.annotations "stringification"
        for param in signature(itemtype).parameters.values():
            itemtype_mdata.parameters[param.name] = Parameter(
                param.name,
                param.kind,
                default=param.default,
                annotation=_type_hints[param.name]
            )
        # Parameters from the new ItemType's constructor are added last to
        # account for any default/annotation deviations from the parent.
        itemtype_mdata.parameters = parent_mdata.parameters | itemtype_mdata.parameters
        itemtype_mdata.parameters.pop("kwargs", None)

        # Selectively inherit members from the parent. To honor inheritance,
        # members of the parent's metadata must not exist in the new ItemType's
        # namespace or definition -- it would indicate that the member has been
        # redefined and the prior functionality it had should not be expected.
        itemtype_members = itemtype_mdata.members
        parent_members   = parent_mdata.members
        itemtype_ns = {*itemtype.__dict__, *chain.from_iterable(itemtype_mdata.members)}
        for slot_idx, parent_mbr_slot in enumerate(parent_members):
            for parent_mbr in parent_mbr_slot:
                if parent_mbr in itemtype_ns:
                    continue
                itemtype_members[slot_idx].add(parent_mbr)

        # Filter duplicate repr inclusions while maintaining order.
        itemtype_mdata.repr += parent_mdata.repr
        final_repr = [*cls.__incl_repr]
        for member in itemtype_mdata.repr:
            if member not in final_repr:
                final_repr.append(member)
        itemtype_mdata.repr = final_repr

        # Inherit all other missing metadata fields from the parent.
        for mdf in itemtype_mdata:
            value = getattr(itemtype_mdata, mdf)
            if value is ItemData.NULL:
                itemtype_mdata[mdf] = parent_mdata[mdf]

        if itemtype_mdata.identity == ItemData.AUTO:
            itemtype_mdata.identity = (generate_itemtype_uuid(), itemtype.__name__)
        elif not itemtype_mdata.internal_only and itemtype_mdata.identity in (None, ItemData.NULL):
            logging.warn(f"Missing identity for non-internal item type {itemtype.__name__!r}.")

        itemtype_mdata._finalize()
        return itemtype_mdata

    #################################
    #### Member Descriptor Hooks ####
    #################################

    def _as_member(self, member: ItemTMember = None, / , *, category: PixlPCategory, repr: bool = False, value: object = NULL) -> ItemTMember:
        def register(obj):
            # Register the attribute by category.
            if isinstance(obj, str):
                name = obj
            elif callable(obj):
                # `obj` should be a method
                name = obj.__name__
            else:
                raise ValueError(f"`member` must be a string or descriptor (got {type(obj)!r}).")

            slot = self.members[category_idx]
            try:
                slot.add(name)
                if repr:
                    self.repr.append(name)
            except TypeError:  # finalized metadata
                raise RuntimeError(f"Cannot mutate managed members after ItemType creation.") from None

            if value is not self.NULL:
                return value
            return obj

        try:
            category_idx = int(PixlPCategory(category))
        except (TypeError, ValueError):
            raise ValueError(f"Invalid `category`.") from None

        if member is not None:
            return register(member)
        return register

    def as_configuration(self, member: ItemTMember, repr: bool = False, value: object = NULL):
        return self._as_member(member, category=CONFIG, repr=repr, value=value)

    def as_information(self, member: ItemTMember, repr: bool = False, value: object = NULL):
        return self._as_member(member, category=INFORM, repr=repr, value=value)

    def as_state(self, member: ItemTMember, repr: bool = False, value: object = NULL):
        return self._as_member(member, category=STATES, repr=repr, value=value)

    def _set_member(
        self,
        category: PixlPCategory,
        fget    : str | ItemPGetter | None = None,
        fset    : str | ItemPSetter | None = None,
        *,
        name    : str  = "",
        target  : str  = None,
        repr    : bool = False,
        **kwargs,
    ):
        return ItemMember(self, category, fget, fset, name=name, target=target, repr=repr, **kwargs)

    def set_configuration(
        self,
        fget: str | ItemPGetter | None = None,
        fset: str | ItemPSetter | None = None,
        *,
        name  : str  = "",
        target: str  = None,
        repr  : bool = False,
        **kwargs,
    ):
        return self._set_member(CONFIG, fget, fset, name=name, target=target, repr=repr, **kwargs)

    def set_information(
        self,
        fget: str | ItemPGetter | None = None,
        fset: str | ItemPSetter | None = None,
        *,
        name  : str  = "",
        target: str  = None,
        repr  : bool = False,
        **kwargs,
    ):
        return self._set_member(INFORM, fget, fset, name=name, target=target, repr=repr,  **kwargs)

    def set_state(
        self,
        fget: str | ItemPGetter | None = None,
        fset: str | ItemPSetter | None = None,
        *,
        name  : str  = "",
        target: str  = None,
        repr  : bool = False,
        **kwargs,
    ):
        return self._set_member(STATES, fget, fset, name=name, target=target, repr=repr, **kwargs)



class ItemTemplate(MutableMapping, metaclass=ABCMeta): # Unrelated to DearPyGui template items.
    @abstractmethod
    def __dearpypixl__(): ...
    @abstractmethod
    def __itemtype__(): ...

    __slots__ = ("tag",)

    is_salvage = False

    __dearpypixl__: ItemData
    __itemtype__  : type['ItemT']

    @classmethod
    def new_template_type(cls, itemtype: type['ItemT']) -> type[Self]:
        metadata  = itemtype.__dearpypixl__
        namespace = {
            "__slots__"     : tuple(metadata.parameters.keys()),
            "__dearpypixl__": metadata,
            "__itemtype__"  : itemtype,
        }
        return type(
            f"{itemtype.__qualname__}Template",
            (cls,),
            namespace | dict(get_class_members(itemtype)),
        )

    def __init__(self, **config):
        self.tag        = None
        self.configure(**config)

    def __repr__(self) -> str:
        return f"<class {type(self).__qualname__!r}>"

    def __call__(self, **config) -> ItemT:
        kwargs = self.configuration() | config
        return self.__itemtype__(**kwargs)

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        return setattr(self, key, value)

    def __delitem__(self):
        return NotImplemented

    def __getattr__(self, attr: str) -> Any:
        # The ItemTemplate signature should mimic the ItemType's
        # signature. Since this isn't actually an item, an
        # attribute may be unavailable at the time of access.
        if attr in dir(self.__itemtype__):
            raise NotImplementedError(f"{attr!r} member is not available as a template.")
        raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __iter__(self):
        yield from self.__dearpypixl__.parameters

    def __len__(self) -> int:
        return len(self.__dearpypixl__.parameters)

    def configure(self, **config) -> None:
        return Item.configure(self, **config)

    def configuration(self) -> dict[str, Any]:
        return {attr:getattr(self, attr) for attr in self.__dearpypixl__.parameters}


#############################################################################################################
#############################################################################################################

class ItemTypeMeta(ABCMeta):
    __dearpypixl__: ItemData

    def __new__(mcls, name, bases, namespace, **kwargs):
        # Adding mixin classes to bases to enable desired functionality.
        metadata: ItemData = namespace.get(ITEM_METADATA, None)
        if metadata and bases:
            bases = list(bases)
            # Python's mro linearization will prevent a mixin from being added
            # more than once, so no worries there.
            if metadata.is_container is True:
                bases.append(ContainerItem)
            if metadata.is_callable is True:
                bases.append(CallableItem)
            if metadata.is_value_able is True:
                bases.append(ValuableItem)
            bases = tuple(bases)
        return super().__new__(mcls, name, bases, namespace, **kwargs)

    def __int__(cls) -> int | None:
        try:
            return int(cls.__dearpypixl__.identity[0])
        except (TypeError, IndexError):
            return None

    def __hash__(cls) -> int:
        return hash((cls.__qualname__, cls.__dearpypixl__.identity))


@ItemData.origin
class ItemType(metaclass=ItemTypeMeta):
    """Provides the core Item API, exposing the more useful ItemType metadata.

    **Properties**
    -----------------------
        * tag (abstract)
        * is_container (class-bound, read-only)
        * is_root_item (class-bound, read-only)
        * is_value_able (class-bound, read-only)
        * is_salvage (read-only)

    **Methods**
    -----------------------
        * able_parents (class-bound)
        * able_children (class-bound)
        * configure
        * configuration
        * information
        * state
    """

    tag: int | str
    @abstractmethod
    def tag(): ...

    __slots__ = ("_tag", "_is_salvage", "__itemdict__")
    __dearpypixl__: ItemData = ItemData(
        identity=None,
        command=None,
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        commands=(),
        constants=(),
        internal_only=True,
    )

    # Mixins add this functionality. Since they are dynamically added,
    # type inference is hard for checkers. I don't know how to *properly*
    # do this...
    __enter__: Callable[..., Self]                                                     # __dearpypixl__.is_container == True
    __call__ : Callable[[Self, Sender | None, AppData | None, UserData | None], None]  # __dearpypixl__.is_callable == True


    def __init_subclass__(cls):
        super().__init_subclass__()
        itemtype_mdata = ItemData.build(cls)

        itemtype_is_public = is_itemtype_public_api(cls)

        # TODO: Maybe a less hacky implementation
        if itemtype_mdata.is_callable:
            for config in itemtype_mdata.members[0]:
                if "callback" in config:
                    ...

        # Build a new ItemTemplate class.
        if itemtype_is_public and not issubclass(cls, AppItem):
            itemtype_mdata.template = ItemTemplate.new_template_type(cls)
        else:
            itemtype_mdata.template = None

        if itemtype_is_public:
            registry._itemtypes.register(cls)
        else:
            logging.info(f"{cls.__name__!r} is marked for internal-use only and was not registered.")


    def __repr__(self):
        repr_str = ", ".join(
            (f"{m}={getattr(self, m)!r}" for m in self.__dearpypixl__.repr)
        )
        return f"{type(self).__qualname__}({repr_str})"

    def __int__(self):
        return self.tag

    def __hash__(self):
        return hash((type(self), self.tag))

    def __eq__(self, other):
        if not isinstance(other, ItemType):
            return False
        return self.__hash__() == hash(other)

    is_salvage = False

    @classproperty
    @__dearpypixl__.as_information
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls.__dearpypixl__.is_container

    @classproperty
    @__dearpypixl__.as_information
    def is_root_item(cls) -> bool:
        """Return True if items of this type cannot be parented by other items.
        """
        return cls.__dearpypixl__.is_root_item

    @classproperty
    @__dearpypixl__.as_information
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls.__dearpypixl__.is_value_able

    @classmethod
    def able_parents(cls) -> tuple[ItemT, ...]:
        """Return all item types that can parent this item IF the item requires
        specific parent items. If the returned tuple is empty, then the item can
        be parented by most non-root container items.
        """
        return registry._itemtypes.get.by_typeid_number(*cls.__dearpypixl__.able_parents)

    @classmethod
    def able_children(cls) -> tuple[ItemT, ...]:
        """Return all item types that this item can parent. If the returned tuple
        is empty, then this type of item can parent most non-root items.
        """
        return registry._itemtypes.get.by_typeid_number(*cls.__dearpypixl__.able_children)

    def configure(self, **config) -> None:
        """Update the item's configuration or other attributes. Equivelent to
        recursively invoking `setattr`.
        """
        for key, value in config.items():
            setattr(self, key, value)

    def configuration(self) -> dict[str, Any]:
        """Return the configuration members for the item along with their current
        values.

        NOTE: This is not an exact equivelent of DearPyGui's `configure_item`
        function. Only return members that can be updated are included. For others,
        see the `information` and `state` methods.
        """
        # ItemTypes use many chained decorators and descriptors which slow
        # attribute access. This implementation tries to limit using them.
        #
        # Tests w/timeit calling this method on a `Window` item 1,000,000 times:
        #   * Python lookup only      : 155.3 seconds
        #   * Python lookup (fallback):  25.4 seconds   <- using this one
        #
        # NOTE: Theoretically, this creates a problem for properties that share
        # a name with a configuration attribute that *can* be accessed through DPG, as
        # the property won't be invoked. No builtin will suffer from this, but could
        # very well happen from when a user redefines a configuration property on a
        # subclass expecting to transform the result before returning it.
        cfg_attrs  = self.__dearpypixl__.members[0]
        dpg_config = get_item_configuration(self.tag)
        return {attr:(dpg_config[attr] if attr in dpg_config else getattr(self, attr))
                for attr in cfg_attrs}

    def information(self) -> dict[str, Any]:
        """Return various read-only information about the item.
        """
        return {attr: getattr(self, attr) for attr in self.__dearpypixl__.members[1]}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        # Similar to the speed-up used in the `configuration` method, but more
        # hacky. Still ~3x faster on average.
        # NOTE: (see `configuration` method NOTE) Unlike properties hooking onto
        # configuration, there's almost zero reason for a user to redefine a state
        # property.
        ste_attrs  = {f"is_{state}":v for state, v in get_item_state(self.tag).items()}
        dpg_states = self.__dearpypixl__.members[2]
        return {attr:(ste_attrs[attr] if attr in ste_attrs else getattr(self, attr))
                for attr in dpg_states}


class AppItemProxy:
    def __init_subclass__(cls): ...


class AppItem(ItemType):
    """Base class for application-level items. Class-bound members of this
    type operate on an internal instance through a proxy.


    **Properties**
    -----------------------
        * tag (class-bound, read-only)


    **Methods**
    -----------------------
        * configure (class-bound)
        * configuration (class-bound)
        * information (class-bound)
        * state (class-bound)
    """
    __slots__  =  ()
    __dearpypixl__ = ItemData(is_root_item=True, internal_only=True)

    __itemdict__ : dict[str, Any] = None
    __itemproxy__: Self           = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.__dearpypixl__.identity in (None, ItemData.NULL):
            raise ValueError("AppItemType identity cannot be None.")
        if cls.__itemdict__ is None:
            cls.__itemdict__ = {}
        if cls.__itemproxy__ is None:
            proxy = type(f"{cls.__qualname__}Proxy", (AppItemProxy, cls), {
                ITEM_METADATA: cls.__dearpypixl__
            })
            cls.__itemproxy__ = proxy()
            registry._items.register(cls.__itemproxy__)

    @classproperty
    @__dearpypixl__.as_information
    def tag(cls):
        try:
            return cls.__dearpypixl__.identity[0]
        except TypeError:
            # This only happens when metaclass.__new__ is invoked when
            # building this specific class. Ignore it for this class
            # only.
            try:
                cls == AppItem
            except NameError:
                return None
            raise

    @classmethod
    def configure(cls, **config):
        return super().configure(cls.__itemproxy__, **config)

    @classmethod
    def configuration(cls):
        cfg_attrs = cls.__dearpypixl__.members[0]
        instance  = cls.__itemproxy__
        return {attr:getattr(instance, attr) for attr in cfg_attrs}

    @classmethod
    def information(cls):
        return super().information(cls.__itemproxy__)

    @classmethod
    def state(cls):
        return {attr:(getattr(cls, attr)) for attr in cls.__dearpypixl__.members[2]}



class Item(ItemType):
    """Base class for object-oriented DearPyGui items.

    **Properties**
    -----------------------
        * label
        * use_internal_label
        * user_data
        * tag (read-only)
        * alias (read-only)
        * parent (read-only)
        * is_container (class-bound, read-only)
        * is_root_item (class-bound, read-only)
        * is_value_able (class-bound, read-only)
        * is_draw_item (class-bound, read-only)
        * is_plot_item (class-bound, read-only)
        * is_node_item (class-bound, read-only)
        * is_table_item (class-bound, read-only)
        * is_ok (read-only)
        * is_enabled (read-only)
        * is_atop_container_stack (read-only)
        * is_salvage (read-only)

    **Methods**
    -----------------------
        * as_template (class-bound)
        * able_parents (class-bound)
        * able_children (class-bound)
        * configure
        * configuration
        * information
        * state
        * get_slot_info
        * get_item_tree
        * push_container
        * pop_container
        * children
        * move
        * move_up
        * move_down
        * copy
        * delete
        * focus
        * toggle_view
        * unstage
        * reset_pos
        * recycle
        * reuse

    """
    __slots__      = ()
    __dearpypixl__ = ItemData(internal_only=True)

    def __init__(self, **kwargs):
        """Args:
            The following are optional, keyword-only arguments:

            * tag (int | str): If an integer is passed, it will be used as the item's
            unique identifier (tag). If it is a string, it will be used as the item's
            alias, and a tag will be automatically generated. Automatically generated
            by default.

            * label (str): Display name for the item. Defaults to None.

            * user_data (Any): Passed as the third positional argument to related callbacks.
            Defaults to None.

            * use_internal_label (bool): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI).
            Defaults to True.
        """
        super().__init__()
        # create the "unaccessable member" cache and pre-populate w/those members
        self.__itemdict__ = itemdict = dict.fromkeys(self.__dearpypixl__.members[3], None)
        self._is_salvage  = False

        # Configuration pre-processing is normally done by descriptors, but they won't have an
        # opportunity to do so here.
        user_data = kwargs.pop("user_data", None)  # leave alone - DPG won't complain regardless of value
        for arg, val in kwargs.items():
            if "callback" in arg and val:  # `callback`, `drag_callback`, `drop_callback`
                is_sequence = isinstance(val, Sequence)
                is_event    = isinstance(val, Event)
                # an `Event` instance is set as-is
                if not is_event:
                    if not is_sequence:
                        val = (val,)
                    val = EventStack(val, sender=self)
                kwargs[arg] = val
                continue
            if isinstance(val, (ItemType, IntEnum)):
                kwargs[arg] = int(val)  # int(Item) -> Item.tag
            # This is the only opportunity to cache the values of members
            # unaccessable through the DearPyGui API.
            if arg in itemdict:
                itemdict[arg] = val
        kwargs["user_data"] = user_data

        identifier = tag if (tag := kwargs.pop("tag", None)) else generate_uuid()
        alias      = None
        if isinstance(identifier, str):
            alias      = identifier
            identifier = generate_uuid()
        try:
            self._tag = self.__dearpypixl__.command(tag=identifier, **kwargs)
        except SystemError:
            raise errors.err_item_not_created(self, {"tag": identifier, **kwargs})
        alias and add_alias(alias, identifier)
        registry._items.register(self)

    def __iter__(self):
        yield from self.children()

    @overloadmethod
    def __getitem__(self, key):
        """Subscript operation support for Item instances. Behavior is altered
        for some item types, and not implemented for others.
        """
        return NotImplemented
    @__getitem__.register
    def _(self, key: int) -> ItemT:
        slot_idx   = 2 if self.is_draw_item else 1
        child_uuid = self._children()[slot_idx][key]
        return registry.get_item(child_uuid)
    @__getitem__.register
    def _(self, key: slice) -> list[ItemT]:
        slot_idx = 2 if self.is_draw_item else 1
        return self._children()[slot_idx][key.start: key.stop: key.step]
    @__getitem__.register
    def _(self, key: tuple) -> ItemT:
        if self.__dearpypixl__.identity[0] != dearpygui.mvTable:
            raise TypeError(f"Unsupported subscript operation for {type(self).__qualname__!r} item.")
        match key:
            case int() as row_idx, int() as col_idx:
                row_uuid        = self._children()[1][row_idx]
                item_at_col_idx = get_item_info(row_uuid)["children"][1][col_idx]
                return registry.get_item(item_at_col_idx, item_at_col_idx)
            case _:
                raise ValueError(f"Expected 2 `int` values (got {len(key)}).")

    @classmethod
    def as_template(cls, **kwargs) -> type[Self]:
        """Return an instance of the ItemType's template class; a mapping-like
        factory object that can create instances of items from a freely-customizable
        default configuration.

        Args:
            * kwargs (keyword-only, optional): Used as default arguments when creating
            future items.
        """
        configuration = {}
        empty         = Parameter.empty
        for param in cls.__dearpypixl__.parameters.values():
            default = None if param.default is empty else param.default
            configuration[param.name] = default

        configuration.pop("kwargs", None)
        configuration |= kwargs
        return cls.__dearpypixl__.template(**configuration)


    @property
    @__dearpypixl__.as_configuration
    def label(self) -> str:
        return get_item_configuration(self._tag)["label"]
    @label.setter
    def label(self, value: str) -> None:
        configure_item(self._tag, label=value)

    @property
    @__dearpypixl__.as_configuration
    def use_internal_label(self) -> str:
        return get_item_configuration(self._tag)["use_internal_label"]
    @use_internal_label.setter
    def use_internal_label(self, value: str) -> None:
        configure_item(self._tag, use_internal_label=value)

    @property
    @__dearpypixl__.as_configuration
    def user_data(self) -> str:
        return get_item_configuration(self._tag)["user_data"]
    @user_data.setter
    def user_data(self, value: str) -> None:
        configure_item(self._tag, user_data=value)


    @property
    @__dearpypixl__.as_information
    def tag(self) -> int:
        """Return this item's unique numeric identifier.
        """
        return self._tag

    @property
    @__dearpypixl__.as_information
    def alias(self) -> str | None:
        """Return this item's unique string identifier.
        """
        return get_item_alias(self._tag) or None

    @property
    @__dearpypixl__.as_information
    def parent(self) -> 'Item':
        """Return the direct progenitor of this item.
        """
        return registry.get_item(get_item_info(self._tag)["parent"], None)

    @classproperty
    @__dearpypixl__.as_information
    def is_draw_item(cls) -> bool:
        return "Draw" in cls.__dearpypixl__.identity[1]

    @classproperty
    @__dearpypixl__.as_information
    def is_node_item(cls) -> bool:
        """Return True if items of this type are used in creating interactive
        node interfaces.
        """
        type_name = cls.__dearpypixl__.identity[1]
        return "Node" in type_name and not "Draw" in type_name

    @classproperty
    @__dearpypixl__.as_information
    def is_plot_item(cls) -> bool:
        """Return True if items of this type are used in creating simple or
        dynamic plots.
        """
        type_name = cls.__dearpypixl__.identity[1]
        return any(name in type_name for name in ("mvAnnotation", "Plot", "Series"))

    @classproperty
    @__dearpypixl__.as_information
    def is_table_item(cls) -> bool:
        """Return True if items of this type are used in creating data tables.
        """
        return "mvTable" in cls.__dearpypixl__.identity[1]


    @property
    @__dearpypixl__.as_state
    def is_ok(self) -> bool:
        """Return True if the item is render-able.
        """
        return get_item_state(self._tag)["ok"]

    @property
    @__dearpypixl__.as_state
    def is_enabled(self) -> bool:
        """Return True if the item is not disabled.
        """
        # TODO: Check if `enabled` is available to every DPG item -- Maybe move
        # to "configuration" category.
        return get_item_configuration(self._tag)["enabled"]


    #### Misc. Properties  ####
    @property
    def is_atop_container_stack(self) -> bool:
        """Return True if this item is at the top of the container stack.
        """
        return self.tag == top_container_stack()

    @property
    def is_salvage(self) -> bool:
        """Return True if this has been recycled and is awaiting reuse.
        """
        return self._is_salvage

    #### Methods ####

    def get_slot_info(self) -> tuple[int, int] | None:
        """Return the item's target slot number and its current position in that slot.

        Args:
            * start (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is 0.
            * stop (int, optional): Used in slicing the child slot to limit the search to a
            particular sequence of that child slot. Default is None.
        """
        if self.is_root_item or (parent := self.parent) is None:
            return None
        slot_idx = get_item_info(self)["target"]
        slot_pos = get_item_info(parent.tag)["children"][slot_idx].index(self.tag)
        return slot_idx, slot_pos

    def get_item_tree(self, from_root: bool = True) -> dict['Item', list[list['Item', list]]]:
        """From the root-most parent, return the parential tree that includes the item.
        Each non-Table (child) item is represented as a 2-item list (`[item, [children]]`).
        Table (`mvAppItemType::Table`) items have a slightly different representation; as
        a 3-item list (`[table_item, [rows], [columns]]`).

        NOTE: The following items will not be included in the tree: `FileExtension`,
        `FontRangeHint`, `NodeLink`, `Annotation`, `DragLine`, `DragPoint`, `DragPayload`,
        `PlotLegend`.

        Args:
            * from_root (bool, optional): If False, the returned tree will not start from
            from this item instead of the root-most parent item. Default is True.
        """
        root_item = None if from_root else self
        current_item = self
        while root_item is None:
            if current_item.is_root_item:
                root_item = current_item
            current_item = current_item.parent
        return root_item._get_item_tree()

    def _get_item_tree(self) -> list['Item', list['Item', list]]:
        children = self._children(slot=2 if self.is_draw_item else 1)
        tree     = [self, []]
        for child in children:
            child_tree = child._item_tree()
            tree[1].append(child_tree)
        if self.__dearpypixl__.identity[0] == dearpygui.mvTable:
            # If the item is a table, include the columns.
            for column in self._children(slot=0):
                child_tree = column._item_tree()
                tree[2].append(child_tree)
        return tree

    def children(self, slot: int = None) -> tuple[ItemT]:
        """Return references to the item's children.

        Args:
            * slot (int, optional): Only include children in this slot. If None,
            children from all slots will be included -- However, they will be
            unordered (order is preserved otherwise). Default is None.
        """
        appitems    = registry._items
        child_slots = self._children()
        if slot is None:
            children = [appitems[child_id] for child_id in
                        itertools.chain.from_iterable(child_slots)]
        else:
            children = [appitems[child_id] for child_id in child_slots[slot]]
        return tuple(children)

    def _children(self) -> list[int]:
        return [*get_item_info(self._tag)["children"].values()]

    def push_container(self) -> Self:
        """Add this item to the top of the container stack. TypeError is raised if
        this item is not a container.

        Items created without an explicit parent will be parented by the item on
        top of the container stack.
        """
        if not self.is_container:
            raise TypeError(f"{type(self).__qualname__!r} item is not a container.")
        push_container_stack()
        return self

    def pop_container(self) -> None:
        """Remove this item from the container stack if this item is the top item
        in the stack. Does nothing otherwise.
        """
        if self.is_atop_container_stack:
            pop_container_stack()

    def move(self, parent: ItemT | int = 0, before: ItemT | int = 0) -> None:
        """If the item is a child, it will be appended to <parent>'s list
        of children, or inserted before/above <before>. An error will be raised if
        this item does not require a parenting item to exist.

        Args:
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (int, optional): id of the child item that the widget
            will be placed above/before.
        """
        try:
            move_item(self._tag, parent=int(parent), before=int(before))
        except SystemError:
            errors.err_if_existential_crisis(self)
            errors.err_if_root_item(self)
            # This does not have a "graceful" ending. It's simply trying to identify
            # the actual problem before throwing an appropriate error to the user as
            # DearPyGui errors are not always descriptive and/or convenient...
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

    def move_up(self) -> None:
        """If the item is a child, it is moved above/before the item
        that immediately precedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_up(self._tag)
        except SystemError:
            errors.err_if_existential_crisis(self)
            errors.err_if_root_item(self)
            raise

    def move_down(self) -> None:
        """If the item is a child, it is placed below/after the item
        that immediately procedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_down(self._tag)
        except SystemError:
            errors.err_if_existential_crisis(self)
            errors.err_if_root_item(self)
            raise

    def copy(self, _recursive: bool = True, **config) -> Self:
        """Return a newly-created item of this item's type using it's current
        configuration as arguments.

        Args:
            * _recursive (bool, optional): If True, all item children will also be
            duplicated. Default is True.
            * config (keyword-only, optional): The arguments to include when creating
            creating the direct copy item (i.e. not children if <_recursive> is True).
            They will be merged into a copy of this item's current configuration before
            using them as arguments to create the copy item.
        """
        # NOTE: Understand that copied items will also honor bound item states that
        # are available as constructor parameters (such as `theme` and `events` for
        # `WidgetItem` derivatives). Since they are independent of the item's tree they
        # will not be copied. However, they are registered as configuration attrib-
        # utes, so references to these items will be passed to the item's construc-
        # tor (inherited from the original item's configuration) where they will be
        # bound.
        itemtype      = type(self)
        configuration = self.configuration() | config

        # Add an explicit parent if the copy item supports it (as it is not included
        # in self.configuration()).
        if not itemtype.is_root_item and "parent" not in config:
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

        self_copy = itemtype(**configuration)
        # Make sure to set the copy item's value to match the real item's value.
        # `default_value` is not always included as an argument when an item is
        # value-able, and it isn't known if other arguments would set the internal
        # value. So the value is copied over only if the copy item's value is None
        # after it has been created.
        if itemtype.is_value_able and getattr(self_copy, "value", None) is None:
            dearpygui.set_value(self_copy._tag, self.value)

        # Recursively copy the children, ensuring that the copied item parents
        # them.
        if _recursive:
            for child in self.children():
                child.copy(recursive=_recursive, parent=self_copy)

        return self_copy

    def focus(self) -> None:
        """Brings an item into focus. Does nothing if the item cannot be
        displayed.
        """
        focus_item(self._tag)

    def toggle_view(self) -> None:
        """If the item supports `show`, hide/show the item. Does nothing if
        `show` is not a invalid configuration option.
        """
        # Because configuration attributes are exposed as properties and several
        # DPG items don't support `show`, I'm not inclined to define a `show` function.
        # Wrapping `window.show = True/False` in a lambda for a callback is
        # kinda dumb though so I wanted to make something user and callback friendly.
        if "show" in self.__dearpypixl__.members[0]:
            show_state = get_item_configuration(self._tag)["show"]
            configure_item(self._tag, show=not show_state)

    def unstage(self) -> None:
        """If the item has been staged, re-parent this item to the item at
        the top of the container stack.
        """
        try:
            unstage(self._tag)
        except SystemError:
            pass

    def reset_pos(self) -> None:
        """If the item supports positioning (`pos`), return the item to its
        original position. Does nothing if `pos` is not a valid configuration
        option.
        """
        try:
            reset_pos(self.tag)
        except SystemError:
            pass

    """The following methods can be used to destroy/delete items. Doing so will:
        * destroy the underlying item
        * destroy any bindings including the item
        * remove any references of the item from the registry
    """
    def delete(self, children_only: bool = False, slot: int = -1, *, __refresh: bool = True) -> None:
        """Destroy this item and its' children.

        Args:
            * children_only (bool, optional): If True, only this item's children
            will be deleted (and NOT this item). Default is False.

            * slot (int, optional): Only children in this slot will be deleted if
            <children_only> is True. Default is -1 (all slots).
        """
        try:
            delete_item(self._tag, children_only=children_only, slot=slot)
        except SystemError:
            pass
        finally:
            if __refresh:
                registry.refresh()

    def recycle(self) -> Self:
        """Return this instance after destroying the underlying item. Salvage safe.

        This is identical to calling `delete` method, except the instance is preserved
        and remains in the registry. It can be re-initialized by calling the `reuse`
        method using the tag of the previous item; avoiding the overhead of creating a
        new Item instance. This is useful if items of the same type are commonly created
        and deleted. It is up to the user to manage and use these "salvaged" instances.

        **NOTE**: While an Item instance is in a salvaged state, several instance methods
        (including property access) will throw errors when invoked. You can check if
        an instance is salvage via the `is_salvage` property.
        """
        self._is_salvage = True
        self.delete(salvage=True)

    def reuse(self, **config) -> None:
        """Re-initialize an Item instance that has been salvaged as a result of the
        `recycle` method. Salvage safe.

        Args:
            * kwargs (keyword-only, optional): Keyword arguments accepted by the Item
            type's constructor i.e. `type(self).__init__`. Note that the `tag` keyword argument will
            be ignored if provided.
        """
        config["tag"] = self.tag
        self.__init__(**config)
        


class LinkedItem(Item):
    __slots__ = ()
    __dearpypixl__ = ItemData(internal_only=True)

    CATEGORY: type['LinkedItem'] | bool = False

    @abstractmethod
    def _bind(binder_uuid: int, item_uuid: int) -> Callable[[int, int], None]:
        """DearPyGui function that binds an item (first argument) to another (second argument).
        This item's identifier will be used as the second argument.
        """
        # NOTE: The assigned function is wrapped in __init_subclass__

    @classmethod
    def _unbind(cls, item_uuid: int) -> None:
        # There are no "unbind" functions in DearPyGui. Passing 0 as the
        # second argument (in place of a binding item) to the bind function
        # will do the job.
        cls._bind(item_uuid, 0)

    def __init_subclass__(cls):
        super().__init_subclass__()
        bind_fn = cls._bind
        # `_bind` should either be None or the appropriate DPG binding function.
        # If the bind function is set to None, make it callable but have it do
        # nothing. In this situation, most methods that use it should be
        # redefined. However, this way there won't be any runtime errors if one
        # is forgotten or unused.
        if not callable(bind_fn) and bind_fn is not None:
            raise TypeError(f"Abstract member `_bind` is not callable.")
        elif bind_fn is None:
            cls._bind = staticmethod(lambda *_: ...)
        # Make it a staticmethod to avoid `type(self)._bind`.
        elif not isinstance(bind_fn, staticmethod):
            cls._bind = staticmethod(bind_fn)

        category = cls.CATEGORY
        if type(category) != bool and not issubclass(category, LinkedItem):
            raise ValueError(f"Invalid value type for `CATEGORY`.")
        # Defined on the new class -- do stuff.
        if "CATEGORY" in cls.__dict__:
            # Register the new class as a binding item category
            if category is True:
                registry._items._register_category(cls)
                cls.CATEGORY = cls
            elif not registry._items._is_registered_binding_item(category):
                raise ValueError("Invalid value type for `CATEGORY`.")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        registry._items._register_binding_item(self)

    @staticmethod
    def _set_binds(binder: 'LinkedItem', items: Sequence[Item], unbind_only: bool = False):
        set_binding = registry._items._set_item_binding
        for pixl_item in items:
            set_binding(binder, pixl_item, unbind_only=unbind_only)

    def bind(self, *item: Item) -> None:
        """Bind an item(s) to this one. Each item can only be bound to one
        item per item type (any previous binding to an item of the same type
        as this one will be destroyed).

        Args:
            * item (Item, positional-only): Item instance(s) to bind.
        """
        self._set_binds(self, item, False)

    @classmethod
    def unbind(cls, *item: Item) -> None:
        """Destroy item(s) bindings for this type of item. Does nothing if the
        item(s) is not bound to this type of item.

        Args:
            * item (Item, positional-only): Item instance(s) to unbind.
        """
        cls._set_binds(cls, item, True)

    def bound_items(self) -> tuple[Item]:
        """Return all items bound to this one.
        """
        return registry._items._get_bound_items(self)

#############################################################################################################
#                                           ItemType Mixins
#############################################################################################################

class ItemTypeMixin(metaclass=ItemTypeMeta):  # unmanaged class creation
    __slots__ = ()


class ContainerItem(ItemTypeMixin):
    __slots__ = ()

    def __enter__(self) -> Self:
        push_container_stack(self.tag)
        return self

    def __exit__(self, *args):
        pop_container_stack()

class CallableItem(ItemTypeMixin):
    __slots__ = ()

    def __call__(
        self,
        sender   : Sender   = None,
        app_data : AppData  = None,
        user_data: UserData = None,
        *args,
        **kwargs
    ) -> None:
        print(sender, app_data, user_data, *args)
        try:
            callback = get_item_configuration(self.tag)["callback"]
        except KeyError:
            raise TypeError(f"{type(self).__qualname__!r} object is not callable.")
        callback(sender, app_data, user_data, **kwargs)

    __code__ = __call__.__code__

class ValuableItem(ItemTypeMixin):
    __slots__ = ()
    # TODO

#############################################################################################################
#############################################################################################################