from __future__ import annotations
import functools
from abc import ABCMeta, abstractmethod
from typing import Callable, Any
from dearpygui import dearpygui
from dearpygui.dearpygui import (
    get_item_info,
    delete_item,
    generate_uuid,
    configure_item,
    get_all_items,
    get_item_configuration,
    get_item_state,
    set_value,
    get_value,
    move_item,
    unstage,
)
from dearpypixl.constants import ItemCategory, SETUP_ONLY_ATTR, READ_ONLY_ATTR
from dearpypixl.errors import DearPyGuiErrorHandler


__all__ = [
    "Item",
    ]


_CONFIG_OVERRIDES: dict = None
_GETATTRIBUTE = object.__getattribute__



def configuration_override(class_attr=None, key: str = None):
    """Include (or override) a key-value pair in the return of `get_configuration`.
    *key* (or *class_attr*.__name__) will be used as the key, and the return of
    *object*.__getattribute__ will be used as the value. In order to override
    a configuration entry, *key* or the defined name of *class_attr* must match
    the name of the option (key) you are trying to override.

    Args:
        * class_attr ([type], optional): ...
        * key (str, optional): Name of the key to override. Defaults to None.
    """
    # NOTE: `wrapper` is *meant* to return `property(class_attr)` to avoid
    # multiple decorations. This breaks pylance's introspection even w/return
    # type hints (verified the signature is correct at runtime). In order to preserve
    # it the decorations need to be seperate i.e.:
    # @property -> @configuration_override -> method
    @functools.wraps(class_attr)
    def wrapper(class_attr):
        global _CONFIG_OVERRIDES
        name = class_attr.__name__
        try:
            _CONFIG_OVERRIDES[key or name] = name
        except TypeError:
            _CONFIG_OVERRIDES = {key or name: name}
        return class_attr

    if not class_attr:
        return wrapper
    return wrapper(class_attr)


def get_configuration(item: Item):
    # Several sources possible...
    item_uuid = item._tag
    item_params = item._setup_params
    all_configuration = {"label": None, } | {**get_item_configuration(item_uuid),
                                             **get_item_info(item_uuid),
                                             "pos": get_item_state(item_uuid)["pos"],
                                             "value": get_value(item_uuid)}
    configuration = {k: v for k, v in all_configuration.items()
                     if k in item_params}
    for config_option, attribute in item._config_overrides.items():
        configuration.pop(config_option, None)   # no key overwrite if aliased
        configuration[attribute] = _GETATTRIBUTE(item, attribute)
    return configuration



class ItemSupport(metaclass=ABCMeta):
    # NOTE: Should be included in mixins.
    def __init_subclass__(cls):
        global _CONFIG_OVERRIDES
        super().__init_subclass__()
        overrides = {}
        for base_c in cls.mro():
            overrides |= base_c.__dict__.get("_config_overrides", {})
        if _CONFIG_OVERRIDES:
            cls._config_overrides = overrides | _CONFIG_OVERRIDES
            _CONFIG_OVERRIDES = None  # reset for next subclass


class _Item(ItemSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    _appitems: dict[int, Item] = {None: None}  # master registry
    # populates below containers when False (first instantiation)
    _cached: bool = False
    _setup_params: set = ()          # all parameters used by the constructor
    _config_params: set = ()         # DPG configurable
    _readonly_params: set = ()       # read-only configuration

    def __init__(self, untrack: bool = False, **kwargs):
        cls = type(self)
        if not cls._cached:
            cls._setup_params = {param for param in kwargs}
            cls._config_params = {param for param in kwargs if param not
                                  in [*READ_ONLY_ATTR, *SETUP_ONLY_ATTR]}
            cls._readonly_params = {param for param in kwargs if
                                    param not in READ_ONLY_ATTR}
            cls._cached = True

        self._tag = kwargs.pop("tag", generate_uuid())

        # Converting all `Item` instances (values) to `int` for their `tag`.
        [kwargs.update({kw: int(val)})
         for kw, val in kwargs.items() if isinstance(val, Item)]
        # Checks for `None` because an empty sting is meaningful (hides the label)
        if kwargs.get("label", None) is None:
            kwargs["label"] = cls.__name__
        # Constructor expects "default_value", but wrappers use "value" instead.
        if value := kwargs.pop("value", None):
            kwargs["default_value"] = value

        with DearPyGuiErrorHandler(self):
            type(self)._command(id=self._tag, **kwargs)  # item creation

        # Registering new item.
        if not untrack:
            self._appitems[self._tag] = self

    def __getattr__(self, attr):
        try:
            return get_configuration(self)[attr]
        except KeyError:
            raise AttributeError(f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __setattr__(self, attr, value):
        # Prioritizing descriptors.
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        elif attr in self._config_params:
            with DearPyGuiErrorHandler(self, attr, value):
                return configure_item(self._tag, **{attr: value})
        elif attr in self._readonly_params:
            raise AttributeError(f"{attr!r} is read-only and cannot be set.")
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if attr in self._config_params:
            raise AttributeError(f"{attr!r} is used for the item's internal configuration and cannot be deleted.")
        object.__delattr__(self, attr)

    def __repr__(self):
        configuration = {
            "tag": self._tag,
            "label": get_item_configuration(self._tag)["label"],
            "is_container": get_item_info(self._tag)["container"],
        }
        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={val!r}' for attr,
                         val in configuration.items()))
            + f")"
        )

    def __int__(self):
        return self._tag



class Item(_Item, metaclass=ABCMeta):
    """Base class for all wrapped items. Cannot be instantiated -- must be
    subclassed.

    Args:
    * untrack (bool, optional): If True, no references will be added to the item
    registry for this item. Defaults to False.


    Abstract Methods
    ----------------
    * _command (Callable): Class attribute - Internal API command that can
    be called to create the item.


    Properties
    ----------
    * tag (read-only)
    * item_category (read-only)


    Methods
    -------
    * children
    * configure
    * configuration
    * delete
    * renew
    * duplicate
    * unstage


    Returns:
        *Item*
    """
    @abstractmethod
    def _command() -> Callable: ...

    @property
    def tag(self) -> int:
        """This item's unique identifier.
        """
        return self._tag

    @property
    def is_container(self) -> bool:
        return get_item_info(self._tag)["container"]

    @property
    @configuration_override(key="type")
    def item_category(self) -> ItemCategory:
        """The enum member that represents the item's type.
        """
        try:
            return ItemCategory[type(self).__qualname__]
        except (AttributeError, KeyError):
            return None

    @property
    def value(self) -> Any:
        return get_value(self._tag)
    @value.setter
    def value(self, value: Any):
        try:
            set_value(self._tag, value)
        except SystemError:
            if "value" in self._config_params:
                raise ValueError(f"Incorrect type for `value` configuration.")
            raise ValueError(f"{type(self)!r} item does not support `value` configuration.")

    @property
    @configuration_override
    def parent(self) -> Item:
        """Return the direct progenitor of this item.
        """
        return self._appitems[get_item_info(self._tag)["parent"]]
    @parent.setter
    def parent(self, value: Item) -> None:
        with DearPyGuiErrorHandler(self, "parent", value):
            return move_item(self._tag, parent=int(value))

    def configure(self, **config) -> None:
        """Updates the item configuration item. It is the equivelent
        of calling `setattr`, and can be used to configure multiple
        attributes.
        """
        _setattr = self.__setattr__
        [_setattr(option, value) for option, value in config.items()]

    def configuration(self) -> dict[str, Any]:
        """Returns the item's configuration options and values
        that are internally used to manage the item.
        """
        return get_configuration(self)

    def children(self) -> list[Item]:
        """Returns a list of the item's children.
        """
        children = (val for val in get_item_info(self._tag)["children"].values())
        appitems = type(self)._appitems
        return [child_item for childs in children
                for child in childs if
                (child_item := appitems.get(child, None))]

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

    def delete(self) -> None:
        """Deletes the item and all children, if any.

        NOTE: The `del` does not properly delete items -- this method
        does.
        """
        # NOTE: Previous method. Trying new implementation.
        # for child in self.children():
        #     child.delete()
        # type(self).APPITEMS.pop(self._tag, None)
        # try:
        #     delete_item(self._tag)
        # except SystemError:
        #     pass
        # del self

        appitems = self._appitems
        try:
            delete_item(self._tag)
        except SystemError:
            pass
        # Registry cleanup
        condemned_ref_uuids = {tag for tag in appitems} - set(get_all_items())
        [appitems.pop(tag, None) for tag in condemned_ref_uuids]
        del self

    def renew(self) -> None:
        """Deletes all of the item's children, if any.
        """
        appitems = self._appitems
        delete_item(self._tag, children_only=True, slot=-1)
        condemned_ref_uuids = {tag for tag in appitems} - set(get_all_items())
        [appitems.pop(tag, None) for tag in condemned_ref_uuids]

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

