"""Basic type implementations for DearPyPixl."""
import functools
import itertools
import threading
from functools import singledispatchmethod as overloadmethod
from abc import ABCMeta, abstractmethod
from enum import Enum, IntEnum
from collections import namedtuple
from inspect import signature, isabstract, Parameter, _VAR_POSITIONAL, _KEYWORD_ONLY
from typing import Any, Callable, TypeVar, MutableMapping, NamedTuple, Iterable, Literal, ClassVar, Final
from typing_extensions import Self, TypeAlias
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
    get_item_info as _get_item_info,    # registered handler for `ItemProperty`
    get_item_state as _get_item_state,  # registered handler for `ItemProperty`
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
from dearpypixl.errors import (
    err_item_not_created,
    err_if_existential_crisis,
    err_if_root_item,
)

# TODO: Deal w/strong references in __registry__.


__all__ = [
    # TypeVars
    "ItemT",
    "AppItemT",

    # Classes
    "RegistryType",
    "InternalType",
    "ItemIdType",

    "ItemType",
    "Item",
    "AppItem",

    # Misc/Helper functions
    "prep_callback",
    "prep_init_args",
    "get_positional_args_count",
    "set_cached_attribute",
]


ItemT     = TypeVar("ItemT"    , bound="Item")
AppItemT  = TypeVar("AppItemT" , bound="AppItem")

####################################################################################
################################# Helper Functions #################################
####################################################################################

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
        - Cache the initial value of managed attributes inaccessible
        through DearPyGui once set.

    Args:
        * obj (ItemT): The ItemType instance to initialize.
        * kwargs (keyword-only): Arguments used to create an item.
    """
    cached_mbr_map = obj.__cached__
    # `user_data` is left alone. Changing it in any way would lead to
    # unexpected behavior for users.
    user_data = kwargs.pop("user_data", None)
    # Default handlers for the `ItemProperty` descriptor can only manage
    # attributes of *created* items, so they don't get to touch the initial
    # arguments. Some work needs to be done before they are passed to DPG.
    for arg, val in kwargs.items():
        # This wraps `callback`, `drag_callback`, and `drop_callback` arguments
        # so that the `sender` is the instance object instead of just the item
        # identifier. It also allows callbacks to actually *work* for any nuitka
        # users.
        if "callback" in arg and val:
            kwargs[arg] = prep_callback(obj, val)
            continue
        # Recasting int-like values. This includes other Item instances that
        # would be used as parents, or integer enums members.
        # NOTE: Checking for instances of `Item` and not `ItemType`. This is
        # because it's possible that a subclass of the latter is not a "true"
        # item type, and may be mimicing the Item API (`Application`,
        # `Viewport`, etc). If an instance is derived from `Item` then I know
        # that it will be accepted by DearPyGui.
        if isinstance(val, (Item, IntEnum)):
            kwargs[arg] = int(val)
        # This might be the only opportunity to cache the values of members
        # unaccessable through the DearPyGui API.
        if arg in cached_mbr_map:
            cached_mbr_map[arg] = val
    kwargs["user_data"] = user_data
    return kwargs


def set_cached_attribute(__obj, __name, value) -> None:
    """Convenience function for setting the cached value of an attribute.
    """
    __obj.__cached__[__name] = value



####################################################################################
############################## Lower-Level Structures ##############################
####################################################################################

class RegistryType(NamedTuple):  # NOTE: Unrelated to DearPyGui registry items.
    """Contains references to Item objects.

    Args:
        * items (dict[int, ItemT]): Contains references to Item instances
        as `{instance.tag: instance}`.
        * types (dict[str, type[ItemT]]): Contains references to created
        Item types.
        * alias (dict[str, str]): Alternate keys for <types> values (i.e
        "built-in" item types).
    """
    # TODO: Use weakrefs.
    items: dict[int, ItemT]       = {}
    types: dict[str, type[ItemT]] = {}
    alias: dict[str, str]         = {}

    def register_item(self, item: ItemT) -> None:
        """Stores an ItemType instance into the item registry.
        """
        self[0][item.tag] = item

    def register_type(self, itemtype: type[ItemT]) -> None:
        """Register an ItemType.
        """
        itemtype_name = itemtype.__qualname__
        typeid_name   = itemtype.__itemtype_id__[1]
        # ItemType class names are used to reference the actual ItemType.
        # Existing keys with the same name will be overwritten. This
        # means the newest subclass will be registered in place of its
        # parent only IF it shares the same name. Most users won't do this
        # by accident (which is great) because this makes it very easy for
        # me to replace or extend existing "built-in" ItemType objects via
        # `class Window(Window): ...`.
        self[1][itemtype_name] = itemtype
        # Store the DearPyGui type name as a lookup alias when searching
        # for the item type. Since these should only be linked to DearPyPixl
        # (DearPyGui) built-in types, it's only set once IF it doesn't exist.
        # This is so `UserDefinedWindow` item type isn't referenced when
        # looking for 'mvAppItemType::mvWindowAppItem', expecting the real
        # `Window` type. Any proper replacement or extension of `Window`
        # should have the same name, so 'mvAppItemType::mvWindowAppItem'
        # should already point to the name 'Window' from a previous `Window`
        # class' registration.
        if typeid_name not in self[2] and typeid_name.startswith("mvAppItemType::"):
            self[2][typeid_name] = itemtype_name

    def get_item(self, key: int, *default: Any) -> ItemT:
        """Return the stored item reference of <key>, or a default value
        if it doesn't exist (raises KeyError if no default value).

        Args:
            * key (str): Unique item identifier.
            * default (Any, optional): Return this value if the key loopup fails.
        """
        # NOTE: The `default` parameter doesn't support multiple arguments. It's
        # a var positional to avoid writing a try:except/cond.check/sentinel
        # value. I can unpack it into the built-in `get` and have it do the work.
        return self[0].get(key, *default)

    def get_type(self, key: str, *default: Any) -> type[ItemT]:
        """Return the ItemType of <key>, or a default value if it doesn't
        exist (raises KeyError if no default value).

        Args:
            * key (str): `ItemType.__qualname__` or `ItemType.__itemtype_id__[1]`.
            * default (Any, optional): Return this value if the key lookup fails.
        """
        # NOTE: The `default` parameter doesn't support multiple arguments. It's
        # a var positional to avoid writing a try:except/cond.check/sentinel
        # value. I can unpack it into the built-in `get` and have it do the work.

        # Assume <key> is an alias and pull the real key first. Otherwise, assume
        # <key> is the real key.
        return self[1].get(self[2].get(key, key), *default)

    def get_types_by_id(self, *itemtype_id: int) -> list[type[ItemT]]:
        """Return a list of item types with a numeric type id matching an
        id in <itemtype_id>.

        Args:
            * itemtype_id (int | var-positional): Returned item types will
            have a numeric type id matching one of these.
        """
        type_ids  = itemtype_id
        itemtypes = []
        for item_t in self[1].values():
            if item_t.__itemtype_id__[0] not in type_ids:
                continue
            itemtypes.append(item_t)
        return itemtypes

    def refresh(self) -> None:
        """Clear the DearPyPixl item registry of items whose tags do not exist
        in the DearPyGui item registry.
        """
        # There should not be many situations where a strong reference exists
        # but the item itself is non-existant in the DearPyGui registry. It can
        # happen if DearPyPixl items aren't deleted correctly I guess.
        registry = self[0]
        pop_func = registry.pop
        deleted_item_uuids = {tag for tag in registry} - set(get_all_items())
        for item_uuid in deleted_item_uuids:
            pop_func(item_uuid, None)


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
        * template_item (Template): The bound Template object created
        specifically for this Item type.
    """
    config_members: tuple[str, ...]      = ()
    inform_members: tuple[str, ...]      = ()
    states_members: tuple[str, ...]      = ()
    cached_members: tuple[str, ...]      = ()
    init_params   : dict[str, Parameter] = {}
    template_item : 'TemplateItem'       = None


class ItemIdType(tuple):  # improvised NamedTuple (can't redefine __new__ otherwise)
    """Contains information regarding an item's type identity.

    Args:
        * uuid (int): The integer value used internally by DearPyGui representing
        the item's type.
        * name (str): The name of the item type used internally by DearPyGui.
    """
    uuid: int
    name: str

    _cls: tuple[int, str] = namedtuple("ItemIdType", ("uuid", "name"))

    def __new__(cls, uuid: int, name: str):
        if name.startswith("mv"):
            name = f"mvAppItemType::{name}"
        return cls._cls(uuid, name)



#####################################################################################
####################### ItemType Creation & Member Management #######################
#####################################################################################
class _ItemPCategory(Enum):
    CONFIG = (0, "configuration")
    INFORM = (1, "information"  )
    STATES = (2, "state"        )

    def __int__(self) -> int:
        return self.value[0]

    def __str__(self) -> str:
        return self.value[1]

    @classmethod
    def _missing_(cls, value: int | str) -> Self:
        for member in cls.__members__.values():
            if value not in member.value:
                continue
            return member
        raise ValueError(f"{value!r} is not a valid {cls.__qualname__!r}.")


_ItemPCategoryError = ValueError(f"`category` must be a member, or an integer or string representing a member, of {_ItemPCategory.__qualname__!r}.")


CONFIG = _ItemPCategory.CONFIG
INFORM = _ItemPCategory.INFORM
STATES = _ItemPCategory.STATES

ItemPCategory: TypeAlias = Literal[CONFIG, 0, 'configuration',
                                   INFORM, 1, 'information',
                                   STATES, 2, 'state']
ItemPGetter  : TypeAlias = Callable[[ItemT, str], Any]         # getattr-like callable
ItemPSetter  : TypeAlias = Callable[[ItemT, str,  Any], None]  # setattr-like callable
ItemPCallable: TypeAlias = Callable[[ItemT, str], Any] | Callable[[ItemT, str, Any], None]


def _default_fget(item: ItemT, name: str):
    """Return the cached value for <name>.
    """
    return item.__cached__[name]

def _default_fset(item: ItemT, name: str, value: Any):
    """Raise AttributeError (read-only member).
    """
    raise AttributeError(f"Cannot set read-only attribute {name!r}.")


class ItemProperty:
    """Descriptor object for managing DearPyGui item attributes. Functionally similar
    to the `property` built-in, but cannot be used as a decorator.
    """
    __slots__ = ("_category_idx",
                 "_fget",
                 "_fset",
                 "_name",
                 "_target",
                 "_cached_on_set",
                 "_default_fget",
                 "_default_fset")

    # Members cannot be registered and instances cannot be created while
    # these are set to  None. They are set appropriately in ItemType's
    # metaclass before processing a new ItemType's namespace.
    _current_itemtype: str       = None
    _current_members : list[set] = None

    @classmethod
    def register(cls, cls_member: Callable | str = None, *, category: ItemPCategory):
        """Decorator method for registering ItemType class members without using a
        `ItemProperty` descriptor.

        Args:
            * cls_member (Callable | str): The attribute to register. If it is a method,
            `cls_member.__name__` is registered.

            * category (str | int): Must be a member, or an integer or string representing
            a member, of `_ItemPCategory`.

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
        @functools.wraps(cls_member)
        def _register(obj):
            # Register the attribute by category.
            if isinstance(obj, str):
                name = obj
            elif callable(obj):
                # `obj` should be a method
                name = obj.__name__
            else:
                raise ValueError(f"`cls_member` must be a string or callable method (got {type(obj)!r}).")

            try:
                cls._current_members[int(_ItemPCategory(category))].add(name)
            except (KeyError, ValueError):
                raise _ItemPCategoryError
            except TypeError:  # _current_members is None
                raise RuntimeError("Cannot register member outside of class creation.")
            return obj

        if cls_member is not None:
            return _register(cls_member)
        return _register


    def __init__(
        self,
        category     : str | int | _ItemPCategory      ,
        fget         : str | ItemPGetter | None =  None,
        fset         : str | ItemPSetter | None =  None,
        *,
        target       : str                      =  None,
        default_fget : ItemPGetter              = _default_fget,
        default_fset : ItemPSetter              = _default_fset,
    ):
        """Args:
            * category (str | int): Must be a member, or an integer or string representing
            a member, of `_ItemPCategory`.

            * fget (str | Callable | None): Object to call that will return the
            attribute value. If the command is registered, the name of the command is also
            an accepted value. Must be `getattr`-like. If None, <default_fget> is used.

            * fset (str | Callable | None): Object to call that will set the value of an
            attribute. If the command is registered, the name of the command is also
            an accepted value. Must be `setattr`-like. If None, <default_fset> is used.

            NOTE: The following are optional, keyword-only arguments;

            * target (str): This is will be passed to <fget> and <fset> as the second
            parameter. Used when it is desired to use <name> -- different from the
            actual name DearPyGui uses (*OR* when there are typos in the DearPyGui
            attribute name, i.e. InputText's "multiline" is "multline" on access).

            * default_fget(Callable[[object, name], Any]): A gettattr-like callable
            invoked when accessing the attribute's value. Cannot be None. Defaults to
            accessing a cached value.

            * default_fset(Callable[[object, name, value], None]): A settattr-like
            callable invoked when accessing the attribute's value. Cannot be None.
            Defaults to raising AttributeError when invoked.
        """
        if self._current_itemtype is None:
            raise RuntimeError(f"Cannot be instantiated outside of class creation.")

        try:
            self._category_idx  = int(_ItemPCategory(category))
        except ValueError:
            raise _ItemPCategoryError
        self._target        = target
        self._default_fget  = default_fget
        self._default_fset  = default_fset
        self._fget          = self._manage_handler(default_fget, fget)
        self._fset          = self._manage_handler(default_fset, fset)
        self._name          = ''
        self._cached_on_set = False

    def __set_name__(self, itemtype: type[ItemT], name: str):
        if not isinstance(itemtype, _ItemTypeMeta):
            raise TypeError(f"Class must be a subclass of {ItemType.__qualname__!r} (got {itemtype.__qualname__!r}).")
        elif itemtype.__qualname__ != self._current_itemtype:
            if self._current_itemtype is not None:
                raise RuntimeError(f"Unfinished registration of derived ItemType {ItemProperty._current_itemtype!r}.")
            raise RuntimeError("Cannot register outside of class creation.")

        self._current_members[self._category_idx].add(name)

        self._name     = name
        self._target   = self._target or name
        self._apply_cache_changes()

    def __get__(self, item: ItemT, itemtype: type[ItemT]):
        if item is None:
            return self
        return self._fget(item, self._target)

    def __set__(self, item: ItemT, value):
        self._fset(item, self._target, value)

    @property
    def fget(self) -> Callable | None:
        # Returns None if using the default handler.
        value = self._fget
        if value == self._default_fget:
            return None
        return self._fget
    @fget.setter
    def fget(self, value: str | Callable | None):
        getter = self._manage_handler(self._default_fget, value)
        # Update cache setting on a notable change.
        if getter != self._fget:
            self._fget = getter
            self._apply_cache_changes()

    @property
    def fset(self) -> Callable | None:
        # Returns None if using the default handler.
        value = self._fset
        if value == self._default_fset:
            return None
        return self._fset
    @fset.setter
    def fset(self, value: str | Callable | None):
        setter = self._manage_handler(self._default_fset, value)
        # Update cache setting on a notable change.
        if setter != self._fset:
            self._fset = setter
            self._apply_cache_changes()

    @property
    def target(self) -> str:
        return self._target
    @target.setter
    def target(self, value: str | None) -> None:
        self._target = value or self._name

    def _manage_handler(
        self,
        default: ItemPGetter | ItemPSetter,
        value: str | ItemPGetter | ItemPSetter | None
    ) -> ItemPSetter:
        """Return the appropriate handler from the given value.
        """
        if value is not None:
            if isinstance(value, str):
                try:
                    value = self._handlers[value]
                except KeyError:
                    raise ValueError(f"{value!r} is not a registered attribute handler.")
            elif not callable(value):
                raise ValueError(f"{value!r} is not callable.")
        else:
            value = default
        return value

    def _apply_cache_changes(self) -> None:
        """Update cache settings based on the state of `self.fget` and `self.fset`.
        """
        fget = self.fget
        fset = self.fset
        # The only time caching needs to be enabled is when there
        # is no viable getter. The fallback getter is set to pull
        # from the attribute cache.
        if not fget:
            # If a non-default `fset` handler is used, then the cache
            # needs to be updated when setting any DearPyGui value.
            # Since `fget` is None, it is assumed the value cannot
            # be accessed from DPG.
            if fset:
                self._fset = self._set_cached_attribute(self._fset)
                self._cached_on_set = True
            # Regardless, ensure that the attribute is sorted properly.
            if self._name:
                self._current_members[-1].add(self._name)
        # Using a non-default `fget` handler. If also using a non-
        # default `fset` handler while it was previously set to
        # cache on update, the handler needs to be unwrapped as
        # there is now a viable getter.
        elif fset and self._cached_on_set:
            self._fset = self._fset.__wrapped__
            self._cached_on_set = False
            # The attribute is no longer cached.
            self._current_members[-1].discard(self._name)
        # There is a non-default `fget` handler, so caching is not
        # needed regardless of the state of `fset`.
        else:
            self._current_members[-1].discard(self._name)

    @staticmethod
    def _set_cached_attribute(func: Callable[[ItemT, str, Any], None]) -> Callable[[ItemT, str, Any], None]:
        # This alters the behavior of the non-default `fset` handler
        # to cache the value in addition to setting the value in DPG.
        @functools.wraps(func)
        def attribute_setter(__obj: ItemT, __name: str, value: Any):
            func(__obj, __name, value)
            set_cached_attribute(__obj, __name, value)
        return attribute_setter

    _handlers: dict[str, ItemPCallable] = {}

    @classmethod
    def _set_handler(cls, func: Callable):
        """Decorator method for registering ItemProperty handlers.
        """
        # Once registered, the name of the callable can be passed to
        # `fget` and `fset` arguments instead of the object reference/
        # pointer so that they don't need to be imported.
        cls._handlers[func.__qualname__] = func
        return func


# registered fget handlers
@ItemProperty._set_handler
def get_item_config(item: ItemT, name: str):
    return get_item_configuration(item._tag)[name]

@ItemProperty._set_handler
def get_item_info(item: ItemT, name: str):
    return _get_item_info(item._tag)[name]

@ItemProperty._set_handler
def get_item_state(item: ItemT, name: str):
    return _get_item_state(item._tag)[name]

@ItemProperty._set_handler
def get_item_value(item: ItemT, name: str = None):
    return get_value(item._tag)

# registered fset handlers
@ItemProperty._set_handler
def set_item_config(item: ItemT, name: str, value: Any):
    configure_item(item._tag, **{name: value})

@ItemProperty._set_handler
def set_item_value(item: ItemT, name: str, value: Any):
    # `value`, `default_value`
    set_value(item._tag, value)

@ItemProperty._set_handler
def set_item_callback(item: ItemT, name: str, value: Any):
    configure_item(item._tag, **{name: prep_callback(item, value)})


class _ItemTypeMeta(ABCMeta):
    # Previously, `ItemType.__init_subclass__` had to "prep" ItemProperty's
    # member cache. This was error prone for several (although niche) sit-
    # uations:
    #   *  if the created class wasn't derived from `ItemType`
    #   *  when instantiating `ItemProperty` outside of class creation (required
    #   for proper registration)
    #   *  when creating a new derived class before the previous had finished
    #   (threading, nested class creation, etc)
    #   *  extensions to __init__subclass__ that required access to the
    #   members-to-register before they are registered/cache is cleared
    #
    # While a "global" member cache is still necessary, this implementation
    # (along with a few small changes to `ItemProperty`) enforce restrictions
    # to prevent those weird errors from being discovered the hard way.

    def __new__(mcls, name, bases, body, **kwargs):
        # Prevent accesses from other threads until ItemType creation and
        # registration has finished (very unlikely, but still).
        with threading.RLock():
            cls = super().__new__(mcls, name, bases, body, **kwargs)
            cls.__clear_reg()
        return cls

    @classmethod
    def  __prepare__(mcls, name, bases, **kwds):
        # NOTE: `ItemProperty` is prepped here, and only here.
        mcls.__prepare_reg(name)
        return kwds

    def __dir__(cls) -> Iterable[str]:
        # excluding name-mangled attributes
        prefixes = {f"_{cls.__qualname__}__" for cls in cls.mro()}
        return [attr for attr in super().__dir__()
                if not any(attr.startswith(prefix)
                for prefix in prefixes)]

    @staticmethod
    def __prepare_reg(itemtype_name: str):
        # This prevents attempts at creating new ItemType subclasses if one
        # is still "processing".
        if ItemProperty._current_itemtype is not None:
            raise RuntimeError(f"Unfinished registration of derived ItemType {ItemProperty._current_itemtype!r}.")
        # Allow ItemProperty instances and member registration.
        ItemProperty._current_itemtype = itemtype_name
        ItemProperty._current_members  = [set() for _ in range(0, len(_ItemPCategory.__members__) + 1)]

    @staticmethod
    def __clear_reg():
        # Lock ItemProperty instantiation and member registration.
        ItemProperty._current_itemtype = None
        ItemProperty._current_members  = None


class ItemType(metaclass=_ItemTypeMeta):
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
        instance when `prep_init_args` is called. If `prep_init_args` is not
        called, it will not be set.


        The following attributes should be redefined per derived ItemType as
        necessary;

        * __itemtype_id__ (ItemTypeIdType | None): A sequence containing informa-
        tion used internally by DearPyGui regarding an item type's identity.

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
    @abstractmethod
    def tag(self) -> int: ...

    __slots__ = ()

    __registry__      : Final[RegistryType]      = RegistryType()
    __internal__      : ClassVar[InternalType]   = InternalType()
    __cached__        : ClassVar[dict[str, Any]] = None

    __itemtype_id__   : ClassVar[ItemIdType] = None
    __is_root_item__  : ClassVar[bool]       = False
    __is_container__  : ClassVar[bool]       = False
    __able_parents__  : ClassVar[tuple]      = ()
    __able_children__ : ClassVar[tuple]      = ()
    __is_value_able__ : ClassVar[bool]       = False
    __command__       : ClassVar[Callable]   = None
    # __constants__   : Not (and likely won't be) used by the Item API. Contains
    # Contains the names of constants in DearPyGui that are associated with that
    # item type.
    # __commands__    : Lists several other function names that exist only because
    # the item type exists.

    def __init_subclass__(cls):
        super().__init_subclass__()
        ##############################################################################
        # [Section 1] Controlling (Inherited) Item Members                           #
        # [Section 2] Build Template                                                 #
        # [Section 3] Container Context Control                                      #
        # [Section 4] Item Registration                                              #
        ##############################################################################

        #### [Section 1] #############################################################
        # Pulling init parameters and registered members from this class' parent.
        parent_cls      = cls.mro()[1]
        parent_internal = getattr(parent_cls, "__internal__", None) or ItemType.__internal__
        cls_reg_members = ItemProperty._current_members  # metaclass clears this later

        init_params  = parent_internal[4] | dict(signature(cls).parameters)
        init_params.pop("kwargs", None)

        config_members = [*cls_reg_members[0]]
        inform_members = [*cls_reg_members[1]]
        states_members = [*cls_reg_members[2]]
        cached_members = [*cls_reg_members[-1]]

        # Ensuring that the new item class doesn't inherit a managed attribute if
        # it has it's own implementation, allowing for expected inheritance. For
        # example; `label` is a managed attribute defined on the `Item` class (below).
        # It will continue to be a registered managed attribute through inheritance
        # until a subclass re-defines `label` (which would unregister it).
        itemt_members = {*getattr(cls, "__dict__" , ()),
                         *getattr(cls, "__slots__", ()),
                         *config_members,
                         *inform_members,
                         *states_members,
                         *cached_members}
        item_mbr_caches   = (config_members, inform_members, states_members, cached_members)
        parent_mbr_caches = parent_internal[0:4]
        for item_sequence, parent_sequence in zip(item_mbr_caches, parent_mbr_caches):
            for member in parent_sequence:
                if member in itemt_members:
                    continue
                item_sequence.append(member)

        #### [Section 2] #############################################################
        # There's no need to create a template for a class that is never instantiated,
        # so we avoid ABC's (also when registering the `Item` class an error would be
        # thrown as the `Template` class isn't defined until later).
        if not isabstract(cls):
            template = type(
                f"{cls.__qualname__}Template",
                (TemplateItem,),
                {"__slots__": tuple(init_params.keys()),
                 "_factory" : cls                              }
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
        # Finalize and register new subclass.
        cls.__internal__ = InternalType(
            tuple(config_members),  # <  Several methods defined on the `Item` class
            tuple(inform_members),  # <  are dependant on these collections. An
            tuple(states_members),  # <  attribute included in any of these can be
            tuple(cached_members),  # <  considered "registered".
            init_params,
            template,
        )
        # ABC's cannot be instantiated, so avoid registering them.
        # NOTE: `isabstract` is unnecessarily called again to help keep these
        # sections seperate.
        if not isabstract(cls) and cls.__itemtype_id__:
            cls.__registry__.register_type(cls)

    def __dir__(self) -> Iterable[str]:
        # excluding name-mangled attributes
        prefixes = {f"_{cls.__qualname__}__" for cls in type(self).mro()}
        return [attr for attr in super().__dir__()
                if not any(attr.startswith(prefix)
                for prefix in prefixes)]

    def __enter(self):
        push_container_stack(self.tag)
        return self

    def __exit(self, exc_type, exc_instance, traceback):
        pop_container_stack()


####################################################################################
##################################### Item API #####################################
####################################################################################
class Item(ItemType, metaclass=ABCMeta):
    """Base class for object-oriented DearPyGui items.

    **Properties**
    -----------------------
        * label
        * use_internal_label
        * user_data
        * tag (read-only)
        * alias (read-only)
        * parent (read-only)
        * is_container (class property, read-only)
        * is_root_item (class property, read-only)
        * is_draw_item (class property, read-only)
        * is_plot_item (class property, read-only)
        * is_node_item (class property, read-only)
        * is_table_item (class property, read-only)
        * is_value_able (class property, read-only)
        * is_ok (read-only)
        * is_enabled (read-only)

    **Public Methods**
    -----------------------
        * as_template (classmethod)
        * able_parents (classmethod)
        * able_children (classmethod)
        * configure
        * configuration
        * information
        * state
        * slot_info
        * get_item_tree
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

    """

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
    @ItemProperty.register(category=CONFIG)
    def label(self) -> str:
        return get_item_configuration(self._tag)["label"]
    @label.setter
    def label(self, value: str) -> None:
        configure_item(self._tag, label=value)

    @property
    @ItemProperty.register(category=CONFIG)
    def use_internal_label(self) -> str:
        return get_item_configuration(self._tag)["use_internal_label"]
    @use_internal_label.setter
    def use_internal_label(self, value: str) -> None:
        configure_item(self._tag, use_internal_label=value)

    @property
    @ItemProperty.register(category=CONFIG)
    def user_data(self) -> str:
        return get_item_configuration(self._tag)["user_data"]
    @user_data.setter
    def user_data(self, value: str) -> None:
        configure_item(self._tag, user_data=value)


    #### Information Properties ####
    @property
    @ItemProperty.register(category=INFORM)
    def tag(self) -> int:
        """Return this item's unique integer identifier.
        """
        return self._tag

    @property
    @ItemProperty.register(category=INFORM)
    def alias(self) -> str | None:
        """Return this item's unique string identifier.
        """
        return get_item_alias(self._tag) or None

    @property
    @ItemProperty.register(category=INFORM)
    def parent(self) -> 'Item':
        """Return the direct progenitor of this item.
        """
        return self.__registry__[0].get(_get_item_info(self._tag)["parent"], None)

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls.__is_container__

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_root_item(cls) -> bool:
        """Return True if items of this type cannot be parented by other items.
        """
        return cls.__is_root_item__

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_draw_item(cls) -> bool:
        return "Draw" in cls.__itemtype_id__[1]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_node_item(cls) -> bool:
        """Return True if items of this type are used in creating interactive
        node interfaces.
        """
        type_name = cls.__itemtype_id__[1]
        return "Node" in type_name and not "Draw" in type_name

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_plot_item(cls) -> bool:
        """Return True if items of this type are used in creating simple or
        dynamic plots.
        """
        type_name = cls.__itemtype_id__[1]
        return any(name in type_name for name in ("mvAnnotation", "Plot", "Series"))

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_table_item(cls) -> bool:
        """Return True if items of this type are used in creating data tables.
        """
        return "mvTable" in cls.__itemtype_id__[1]

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls.__is_value_able__


    #### States Properties ####
    @property
    @ItemProperty.register(category=STATES)
    def is_ok(self) -> bool:
        """Return True if the item is render-able.
        """
        return _get_item_state(self._tag)["ok"]

    @property
    @ItemProperty.register(category=STATES)
    def is_enabled(self) -> bool:
        """Return True if the item is not disabled.
        """
        # TODO: Check if `enabled` is available to every DPG item -- Maybe move
        # to "configuration" category.
        return get_item_configuration(self._tag)["enabled"]


    #### Methods ####
    @classmethod
    def able_parents(cls) -> tuple[ItemT, ...]:
        """Return all item types that can parent this item IF the item requires
        specific parent items. If the returned tuple is empty, then the item can
        be parented by most non-root container items.
        """
        return tuple(cls.__registry__.get_types_by_id(*cls.__able_parents__))

    @classmethod
    def able_children(cls) -> tuple[ItemT, ...]:
        """Return all item types that this item can parent. If the returned tuple
        is empty, then this type of item can parent most non-root items.
        """
        return tuple(cls.__registry__.get_types_by_id(*cls.__able_children__))

    def configuration(self) -> dict[str, Any]:
        """Return the configurable options used to manage this item, along
        with their current values.

        This is not an exact equivelent of DearPyGui's `configure_item`
        function. If the option is not included as a parameter in signature
        of `type(self).__init__`, it is not considered to be "configuration"
        and will not be included in the return (see the `information` method).
        """
        # Descriptors are slow. Only go through them if the attributes cannot be
        # accessed though DearPyGui. Tests w/timeit calling this method on a
        # `Window` item 1,000,000 times:
        #   * Python lookup only      : 155.3 seconds
        #   * Python lookup (fallback):  25.4 seconds   <- using this one
        cfg_attrs  = self.__internal__[0]
        dpg_config = get_item_configuration(self._tag)
        return {attr:(dpg_config[attr] if attr in dpg_config else getattr(self, attr))
                for attr in cfg_attrs}

    def information(self) -> dict[str, Any]:
        """Return various read-only information about the item.
        """
        # DearPyPixl's "information" category greatly differs from DearPyGui. Most
        # of it won't be found using `get_item_info`, so this won't benefit from
        # the same performance optimization used in the `configuration` method.
        return {attr: getattr(self, attr)
                for attr in self.__internal__[1]}

    def state(self) -> dict[str, Any]:
        """Return the current state(s) of the item.
        """
        # Similar to the speed-up used in the `configuration` method, but more
        # hacky. Still ~3x faster on average.
        ste_attrs  = {f"is_{state}":v for state, v in _get_item_state(self._tag).items()}
        dpg_states = self.__internal__[2]
        return {attr:(ste_attrs[attr] if attr in ste_attrs else getattr(self, attr))
                for attr in dpg_states}

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
        return root_item._item_tree()

    def configure(self, **config) -> None:
        """Update the item's configuration, or other instance attributes.
        """
        for key, value in config.items():
            setattr(self, key, value)

    def children(self, slot: int = None) -> tuple[ItemT]:
        """Return references to the item's children.

        Args:
            * slot (int, optional): Only include children in this slot. If None,
            children from all slots will be included -- However, they will be
            unordered (order is preserved otherwise). Default is None.
        """
        appitems    = self.__registry__[0]
        child_slots = [*_get_item_info(self._tag)["children"].values()]
        if slot is None:
            children = [appitems[child_id] for child_id in
                        itertools.chain.from_iterable(child_slots)]
        else:
            children = [appitems[child_id] for child_id in child_slots[slot]]
        return tuple(children)

    def move(self, parent: ItemT | int = 0, before: ItemT | int = 0) -> None:
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
            err_if_existential_crisis(self)
            err_if_root_item(self)
            # This does not have a "graceful" ending. It's simply trying to identify
            # the actual problem before throwing an appropriate error to the user as
            # DearPyGui errors are not always descriptive and/or convenient...
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

    def move_up(self) -> None:
        """If the item is a child, it is moved above/before the item
        that immediately precedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_up(self._tag)
        except SystemError:
            err_if_existential_crisis(self)
            err_if_root_item(self)
            raise

    def move_down(self) -> None:
        """If the item is a child, it is placed below/after the item
        that immediately procedes it. An error will be thrown if this item
        is not (and cannot be) parented by another item.
        """
        try:
            move_item_down(self._tag)
        except SystemError:
            err_if_existential_crisis(self)
            err_if_root_item(self)
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
        # `Widget` derivatives). Since they are independent of the item's tree they
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
        try:
            delete_item(self._tag, children_only=children_only, slot=slot)
        except SystemError:
            pass
        self.__registry__.refresh()

        if not children_only:
            del self

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
        if "show" in self.__internal__[0]:
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


    ######################
    ###### END API #######
    ######################

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
    @abstractmethod
    def __command__()       -> Callable[..., Any]: ...

    __slots__ = ("_tag",)

    def __init__(self, **kwargs):
        self.__cached__ = dict.fromkeys(self.__internal__[3], None)

        kwargs = prep_init_args(self, **kwargs)

        identifier = tag if (tag := kwargs.pop("tag", None)) else generate_uuid()
        alias      = None
        if isinstance(identifier, str):
            alias      = identifier
            identifier = generate_uuid()
        try:
            self._tag = type(self).__command__(tag=identifier, **kwargs)
        except SystemError:
            raise err_item_not_created(self, {"tag": identifier, **kwargs})
        # If `tag` was a string, it is an alias and should be set as such.
        alias and add_alias(alias, identifier)
        self.__registry__.register_item(self)

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

    @overloadmethod
    def __getitem__(self, key):
        """Subscript operation support for Item instances. Behavior is altered
        for some item types, and not implemented for others.

        Example via index:
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

        Example via `slice` object:
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

        Example via matrices subscript (i.e. `Table` items):
            >>> with Table(tag=5000) as table:
            ...     col = TableColumn(tag=6000)
            ...     row = TableRow(tag=7000)
            ...     with row:
            ...         cell = TableCell(tag=8000)
            >>>
            >>> # The first index indicates row, the second indicates column.
            >>> table[0].tag
            7000  # row
            >>> table[0, 0].tag
            8000  # cell
        """
        return NotImplemented
    @__getitem__.register
    def _(self, key: int) -> ItemT:
        slot_idx   = 2 if self.is_draw_item else 1
        child_uuid = self._children()[slot_idx][key]
        return self.__registry__.get_item(child_uuid)
    @__getitem__.register
    def _(self, key: slice) -> list[ItemT]:
        slot_idx = 2 if self.is_draw_item else 1
        return self._children()[slot_idx][key.start: key.stop: key.step]
    @__getitem__.register
    def _(self, key: tuple) -> ItemT:
        if self.__itemtype_id__[0] != dearpygui.mvTable:
            raise TypeError(f"Unsupported subscript operation for {type(self).__qualname__!r} item.")
        match key:
            case int() as row_idx, int() as col_idx:
                row_uuid        = self._children()[1][row_idx]
                item_at_col_idx = _get_item_info(row_uuid)["children"][1][col_idx]
                return self.__registry__.get_item(item_at_col_idx, item_at_col_idx)
            case _:
                raise ValueError(f"Expected 2 `int` values (got {len(key)}).")

    ## private/internal methods ##
    @classmethod
    def _command(cls, **config) -> int | str:
        """Directly call the DearPyGui command used to create the item and return
        its unique identifier.
        """
        for kw, val in config.items():
            if isinstance(val, (Item, IntEnum)):
                config[kw] = int(val)
        return cls.__command__(**config)

    def _children(self) -> list[int]:
        return [*_get_item_info(self._tag)["children"].values()]

    def _item_tree(self) -> list['Item', list['Item', list]]:
        children = self._children(slot=2 if self.is_draw_item else 1)
        tree     = [self, []]
        for child in children:
            child_tree = child._item_tree()
            tree[1].append(child_tree)
        if self.__itemtype_id__[0] == dearpygui.mvTable:
            # If the item is a table, include the columns.
            for column in self._children(slot=0):
                child_tree = column._item_tree()
                tree[2].append(child_tree)
        return tree


class AppItem(ItemType):
    """Provides a minimal Item API for application-level objects.
    """
    # NOTE: General configuration and information getters should be available on
    # the class, but configuration setters on instances. This is because a descriptor
    # would be overwritten if re-assigned on a class. A metaclass would work -- However,
    # instances would not have access to descriptors set on the metaclass. This would be
    # annoying to work around as a developer, and confusing to work with as a user.
    @classmethod
    @abstractmethod
    def tag(cls) -> int | str     : ...

    @classmethod
    @abstractmethod
    def configuration(cls) -> dict[str, Any]: ...

    @classmethod
    @abstractmethod
    def information(cls) -> dict[str, Any]: ...

    @classmethod
    @abstractmethod
    def state(cls) -> dict[str, Any]: ...

    __slots__  =  ()
    __cached__ =  {   # set per-instance for normal items via `prep_init_args`
        "app_uuid"     : 1,
        "viewport_uuid": "DPG NOT USED YET",
        "theme_uuid"   : 0,
        "font_uuid"    : 0,
    }
    __is_root_item__ = True

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_container(cls) -> bool:
        """Return True if items of this type are capable of parenting other items.
        """
        return cls.__is_container__

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_root_item(cls) -> bool:
        """Return True if items of this type cannot be parented by other items.
        """
        return cls.__is_root_item__

    @classmethod
    @property
    @ItemProperty.register(category=INFORM)
    def is_value_able(cls) -> bool:
        """Return True if items of this type can hold a value.
        """
        return cls.__is_value_able__

    def configure(self, **config):
        return Item.configure(self, **config)


class TemplateItem(MutableMapping, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def _factory(cls) -> ItemT: ...

    __slots__ = ("_tag",)  # subclasses should also include __slots__

    # Hooks for various read-only members from the owner item type.
    # The signature of the method that returns a template instance
    # is set to the ItemType and not the template, so I can get away
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
                   "is_table_item"    ,
                   "is_draw_item"     ,
                   "is_plot_item"     ,
                   "is_node_item"     ,
                   "is_value_able"    ,
                   "able_parents"     ,
                   "able_children"    ):
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
            raise NotImplementedError(f"{attr!r} member is not available as a template.")
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
