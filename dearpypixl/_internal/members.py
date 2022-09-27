from __future__ import annotations
import functools
import logging
from enum import Enum
from typing import (
    Any,
    Callable,
    Literal,
    TYPE_CHECKING,
)
from typing_extensions import Self, TypeAlias
from dearpygui._dearpygui import (
    get_item_info as _get_item_info,    # registered handler for `PixlProperty`
    get_item_state as _get_item_state,  # registered handler for `PixlProperty`
    get_value,
    set_value,
    get_item_configuration,
    configure_item,
)
from .callback import Event, EventStack, is_dearpypixl_callback
from .utilities import prep_callback, set_cached_attribute

if TYPE_CHECKING:
    from dearpypixl._internal.item import ItemData, ItemType



class PixlPCategory(Enum):
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


CONFIG = PixlPCategory.CONFIG
INFORM = PixlPCategory.INFORM
STATES = PixlPCategory.STATES

ItemPGetter  : TypeAlias = Callable[['ItemType', str], Any]         # getattr-like callable
ItemPSetter  : TypeAlias = Callable[['ItemType', str,  Any], None]  # setattr-like callable
ItemPCategory: TypeAlias = Literal[CONFIG, 0, "configuration",
                                   INFORM, 1, "information"  ,
                                   STATES, 2, "state"        ]




def _default_fget(item: ItemType, name: str):
    """Return the cached value for <name>.
    """
    return item.__itemdict__[name]

def _default_fset(item: ItemType, name: str, value: Any):
    """Raise AttributeError (read-only member).
    """
    raise AttributeError(f"Cannot set read-only attribute {name!r}.")


class ItemMember:
    __slots__ = (
        "_category",
        "_fget",
        "_fset",
        "_name",
        "_target",
        "_cached_on_set",
        "_default_fget",
        "_default_fset",
        "_log_info",
        "_metadata",
        "_repr",
    )

    def __init__(
        self,
        metadata    : ItemData,
        category    : PixlPCategory,
        fget        : str | ItemPGetter | None = None,
        fset        : str | ItemPSetter | None = None,
        *,
        name        : str         = "",
        target      : str         = None,
        repr        : bool        = False,
        log_info    : str         = None,   # reason for `target` override
        default_fget: ItemPGetter = _default_fget,
        default_fset: ItemPSetter = _default_fset,
    ):
        self._metadata      = metadata
        self._category      = category
        self._name          = None
        self._target        = target
        self._log_info      = log_info
        self._repr          = repr
        self._default_fget  = default_fget
        self._default_fset  = default_fset
        self._fget          = self._manage_handler(default_fget, fget)
        self._fset          = self._manage_handler(default_fset, fset)
        self._cached_on_set = False

        if name:  # do not wait for ItemType's metaclass if able
            self.__set_name__(None, name)

    def __set_name__(self, itemtype: type[ItemType], name: str):
        if not self._name:
            self._name     = name
            self._target   = self._target or name
            self._metadata._as_member(name, category=self._category)
            if self._repr:
                self._metadata.repr.append(self._name)
            self._apply_cache_changes()

            if self._target != self._name and self._log_info:
                cls_name = itemtype.__qualname__
                logging.info(f"Using member alias for {cls_name!r}. {self._target!r} -> {cls_name}.{self._name}")

    def __get__(self, item: ItemType, itemtype: type[ItemType]):
        if item is None:
            return self
        return self._fget(item, self._target)

    def __set__(self, item: ItemType, value):
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
    ) -> ItemPGetter | ItemPSetter:
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
        # The only time caching needs to be enabled is when there is no viable getter.
        # The fallback getter is set to pull from the attribute cache.
        if not fget:
            # If a non-default `fset` handler is used, then the cache needs to be
            # updated when setting any DearPyGui value. Since `fget` is None, it is
            # assumed the value cannot be accessed from DPG.
            if fset:
                self._fset = self._set_cached_attribute(self._fset)
                self._cached_on_set = True
            # Regardless, ensure that the attribute is sorted properly.
            if self._name:
                self._metadata.members[-1].add(self._name)
        # Using a non-default `fget` handler. If also using a non-default `fset` handler
        # while it was previously set to cache on update, the handler needs to be
        # unwrapped as there is now a viable getter.
        elif fset and self._cached_on_set:
            self._fset = self._fset.__wrapped__
            self._cached_on_set = False
            # The attribute is no longer cached.
            self._metadata.members[-1].discard(self._name)
        # There is a non-default `fget` handler, so caching is not needed regardless of
        # the state of `fset`.
        else:
            self._metadata.members[-1].discard(self._name)

    @staticmethod
    def _set_cached_attribute(func: Callable[[ItemType, str, Any], None]) -> Callable[[ItemType, str, Any], None]:
        # This alters the behavior of the non-default `fset` handler to cache the value
        # in addition to setting the value in DPG.
        @functools.wraps(func)
        def attribute_setter(__obj: ItemType, __name: str, value: Any):
            func(__obj, __name, value)
            set_cached_attribute(__obj, __name, value)
        return attribute_setter

    _handlers: dict[str, ItemPGetter | ItemPSetter] = {}

    @classmethod
    def _set_handler(cls, func: Callable):
        """Decorator method for registering PixlProperty handlers.
        """
        # Once registered, the name of the callable can be passed to  `fget` and `fset`
        # arguments instead of the object reference/pointer so that they don't need to
        # be imported.
        cls._handlers[func.__qualname__] = func
        return func


@ItemMember._set_handler
def get_item_config(item: ItemType, name: str):
    return get_item_configuration(item._tag)[name]

@ItemMember._set_handler
def get_item_info(item: ItemType, name: str):
    return _get_item_info(item._tag)[name]

@ItemMember._set_handler
def get_item_state(item: ItemType, name: str):
    return _get_item_state(item._tag)[name]

@ItemMember._set_handler
def get_item_value(item: ItemType, name: str = None):
    return get_value(item._tag)

# registered fset handlers
@ItemMember._set_handler
def set_item_config(item: ItemType, name: str, value: Any):
    configure_item(item._tag, **{name: value})

@ItemMember._set_handler
def set_item_value(item: ItemType, name: str, value: Any):
    # `value`, `default_value`
    set_value(item._tag, value)

@ItemMember._set_handler
def set_item_callback(item: ItemType, name: str, value: Any):
    if value and not is_dearpypixl_callback(item):
        value = EventStack((value,), sender=item)
    configure_item(item._tag, **{name: value})
