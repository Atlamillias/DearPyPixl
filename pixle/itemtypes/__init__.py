from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, Union
from dearpygui import dearpygui
from dearpygui.dearpygui import (
    get_item_info,
    delete_item,
    generate_uuid,
    configure_item,
    get_item_configuration,
    get_item_state,
    set_value as dpg_set_value,
    get_value,
    move_item,
    unstage_items,
)


__all__ = ["Item"]


# There are several commands to get/set DPG item configuration.
# When it is changed in the future, I can clean up this mess...
def _get_before(item: Item):
    item_id = item._tag
    parent = get_item_info(item_id)["parent"]
    parent_childs: dict[str, list] = get_item_info(parent)["children"]
    for childs in parent_childs.values():
        if item_id in childs and item_id != childs[-1]:
            return childs.index(item_id) + 1
    return None

def _set_parent(item: Item, parent):
    item_id = item._tag

    parent = int(parent)
    current_parent = get_item_info(item_id)["parent"]
    # If the value would be the default value (0 or None),
    # or if the parent wouldn't change, do nothing.
    if not parent or parent == current_parent:
        return None

    return move_item(item_id, parent=int(parent))

def _set_before(item: Item, before):
    item_id = item._tag
    before = int(before)

    # If the value would be the default value (0 or None), do nothing.
    if not before or before == _get_before(item):
        return None

    return move_item(item_id, before=before)

def _set_value(item: Item, value: Any):
    return dpg_set_value(item._tag, value)

_SET_CONFIG = {
    "parent": _set_parent,
    "before": _set_before,
    "value": _set_value,
    "default_value": _set_value,
}

def set_configuration(item: Item, attribute: str, value: Any):
    if func := _SET_CONFIG.get(attribute, None):
        return func(item, value)
    return configure_item(item._tag, **{attribute: value})

def get_configuration(item: Item):
    # This function acts as a patched `get_item_configuration`. All
    # configuration options that an item *might* have are returned.
    item_id = item._tag
    config = {
        **get_item_configuration(item_id),
        "parent": get_item_info(item_id)["parent"],
        "before": None,
        "pos": get_item_state(item_id)["pos"],
        "value": get_value(item_id),
    }
    # Getting object reference from id's
    if parent_id := config["parent"]:
        config["parent"] = Item.APPITEMS.get(parent_id, parent_id)

        before_id = _get_before(item)
        config["before"] = Item.APPITEMS.get(before_id, before_id)

    return config


# TODO: 
#    - Include layout import/export methods.
#    - Use the weakref module instead of strong refs for the registry.

class Item(metaclass=ABCMeta):
    """Base class for all wrapped items. Cannot be instantiated -- must be
    subclassed.


    Abstract Methods
    ----------------
    * _command (Callable): Class attribute - Internal API command that can
    be called to create the item.


    Properties
    ----------
    * id (read-only)


    Methods
    -------
    * configure
    * configuration
    * delete
    * children
    * handlers
    * duplicate
    * unstage


    Returns:
        *Item*
    """
    @abstractmethod
    def _command() -> Callable: ...
    _configurations: set = set()

    APPITEMS: dict[int,"Item"] = {}

    def __init__(self, untrack: bool = False, **kwargs):
        """Initializes an instance of *Item*.

        Args:
            * untrack (bool, optional): If True, no references will be added to the item
            registry for this item. Defaults to False.
        """
        self._tag = kwargs.pop("tag", generate_uuid())
        cls = type(self)

        # Attributes in _configurations is have unique handling.
        if not cls._configurations:
            cls._configurations = {option for option in kwargs if option != "tag"}
        # Untracked in item registry...?
        if not untrack:
            self.APPITEMS[self._tag] = self

        # Need the id of any Item instance passed as a value for configuration.
        [kwargs.update({kw: int(val)}) for kw, val in kwargs.items() if isinstance(val, Item)]
        # Checking specifically for None because passing an empty string is
        # meaningful.
        if kwargs.get("label", None) is None:
            kwargs["label"] = cls.__name__
        # Constructor expects "default_value", but wrappers use "value" instead.
        value = kwargs.pop("value", None)

        type(self)._command(id=self._tag, **kwargs)  # item creation

        # Setting `value` if one was passed...
        if value is not None:
            dpg_set_value(self._tag, value)

    def __int__(self):
        return self._tag

    def __repr__(self):
        # These next few lines of code pretty much make up the body
        # of `Item.configuration`. However, it is possible that the method
        # could be overloaded. 
        unfiltered_config = {"tag": self._tag} | get_configuration(self)
        configurations = self._configurations
        config = {attr: val for attr, val in unfiltered_config.items()
                  if attr in configurations or attr == "tag"}
        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={val!r}' for attr, val in config.items()))
            + f")"
        )

    def __hash__(self):
        return hash((type(self).__qualname__,self._tag))

    def __eq__(self, other: object):
        return hash(self) == hash(other)

    def __getattr__(self, attr):
        try:
            return get_configuration(self)[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __setattr__(self, attr, value):
        # Prioritizing descriptors, etc.
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        if attr in self._configurations:
            return set_configuration(self, attr, value)
        object.__setattr__(self, attr, value)

    @property
    def tag(self) -> int:
        """Unique identifier for the item.
        """
        return self._tag

    def configure(self, **config) -> None:
        """Updates the item configuration item. It is the equivelent
        of calling `setattr`, and can be used to configure multiple
        attributes.
        
        """
        [setattr(self, option, value) for option, value in config.items()]

    def configuration(self, option: str = None) -> Union[dict[str, Any], Any]:
        """Returns the item's configuration options and values
        that are internally used to manage the item. If <option>
        is included, only the value of that option will be returned.
        
        NOTE: Typically, attributes included in configuration are the
        parameters used to create an instance of an item. This will
        not include other instance attributes, and does not replace
        `getattr`.
        """
        config = get_configuration(self)
        configurations = self._configurations
        config = {attr: val for attr, val in
                  get_configuration(self).items()
                  if attr in configurations or attr == "tag"}
        return config.get(option, config)

    def delete(self) -> None:
        """Deletes the item and any child items it may have.

        NOTE: Call this method instead of `del` when deleting
        items.
        """
        for child in self.children():
            try:
                child.delete()
            except SystemError:
                pass

        try:
            delete_item(self._tag)
        except SystemError:
            pass

        type(self).APPITEMS.pop(self._tag, None)
        del self

    def children(self) -> list["Item"]:
        """Returns a list of the item's children.
        """
        # Slot 0: mvFileExtension,
        #         mvFontRangeHint,
        #         mvNodeLink,
        #         mvAnnotation,
        #         mvDragLine,
        #         mvDragPoint,
        #         mvLegend,
        #         mvTableColumn
        # Slot 1: All other app items
        # Slot 2: Draw items
        cls = type(self)
        childs = (val for slot, val in
                  get_item_info(self._tag)["children"].items()
                  if slot in (0, 1, 2))
        # Flattening list of lists.
        return [cls.APPITEMS[child]
                for c_list in childs for child in c_list]

    def handlers(self) -> list[Item]:
        """Returns a list of event handlers that are currently registered
        to the item.
        """
        # Items in Slot 3 are event handlers.
        cls = type(self)
        return [cls.APPITEMS[handler] for handler in
                get_item_info(self._tag)["children"][3]]

    def unstage(self) -> None:
        """Unstages the item.
        """
        unstage_items([self._tag])

    def duplicate(self, **config) -> Item:
        """Creates a (recursive) copy of the item and returns a reference to the
        object. If the item is a top-level item (a container that cannot have a
        parent), a new item created containing copies of the original item's
        children. Otherwise, the copy will be parented by this item's parent.

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
        if is_container and not is_top_level or type(self).__qualname__ == "Window":
            if new_item_parent := config.get("parent", None):
                item_config["parent"] = new_item_parent

        new_item = item_type(**item_config)

        # copying theme
        dearpygui.set_item_theme(new_item._tag, item_info["theme"])
        dearpygui.set_item_theme(new_item._tag, item_info["disabled_theme"])
        dearpygui.set_item_font(new_item.tag, item_info["font"])
        
        # duplicating children
        for child in self.children():
            child.duplicate(parent=new_item)

        return new_item
