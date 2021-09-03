from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any, Union
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


def _set_parent(item: Item, parent):
    item_id = item._id

    parent = int(parent)
    current_parent = get_item_info(item_id)["parent"]
    # If the value would be the default value (0 or None),
    # or if the parent wouldn't change, do nothing.
    if not parent or parent == current_parent:
        return None

    return move_item(item_id, parent=int(parent))


def _set_value(item: Item, value: Any):
    return dpg_set_value(item._id, value)



_SET_CONFIG = {
    "parent": _set_parent,
    "value": _set_value,
    "default_value": _set_value,
}


def set_configuration(item: Item, attribute: str, value: Any):
    if func := _SET_CONFIG.get(attribute, None):
        return func(item, value)
    return configure_item(item._id, **{attribute: value})


def get_configuration(item: Item):
    # This function acts as a patched `get_item_configuration`. All
    # configuration options that an item *might* have are returned.
    item_id = item._id
    return {
        **get_item_configuration(item_id),
        "parent": get_item_info(item_id)["parent"],
        "pos": get_item_state(item_id)["pos"],
        "value": get_value(item_id),
    }




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
            * stage (bool, optional): If True, the item will be created but not
            rendered. The `unstage` method needs to be called to render it.
            Defaults to False.

            * untrack (bool, optional): If True, no references will be added to the item
            registry for this item. Defaults to False.
        """
        self._id = kwargs.pop("id", generate_uuid())
        cls = type(self)

        # Attributes in _configurations is have unique handling.
        if not cls._configurations:
            cls._configurations = {option for option in kwargs if option != "id"}

        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)
        if kwargs.get("label", None) is None:  # empty strings have value here
            kwargs["label"] = cls.__name__
        # Constructor expects "default_value", but wrappers use "value" instead.
        value = kwargs.pop("value", None)

        if not untrack:
            self.APPITEMS[self._id] = self

        type(self)._command(id=self._id, **kwargs)

        if value is not None:
            dpg_set_value(self._id, value)

    
    def __int__(self):
        return self._id

    def __repr__(self):
        # These next few lines of code pretty much make up the body
        # of `Item.configuration`. However, it is possible that the method
        # could be overloaded. 
        unfiltered_config = {"id": self._id} | get_configuration(self)
        configurations = self._configurations
        config = {attr: val for attr, val in unfiltered_config.items()
                  if attr in configurations or attr == "id"}
        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={val!r}' for attr, val in config.items()))
            + f")"
        )

    def __getattr__(self, attr):
        try:
            return get_configuration(self)[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __setattr__(self, attr, value):
        # Allowing special methods, descriptors, etc.
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        if attr in self._configurations:
            return set_configuration(self, attr, value)
        object.__setattr__(self, attr, value)

    @property
    def id(self) -> int:
        """Unique identifier for the item.
        """
        return self._id

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
                  if attr in configurations or attr == "id"}
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
            delete_item(self._id)
        except SystemError:
            pass

        type(self).APPITEMS.pop(self._id, None)
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
                  get_item_info(self._id)["children"].items()
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
                get_item_info(self._id)["children"][3]]

    def unstage(self) -> None:
        """Unstages the item.
        """
        unstage_items([self._id])

    def duplicate(self) -> Item:
        """Creates a copy of the item and returns it.

        Args:
            config (keyword-only, optional): Options/values to use instead
            of the 'copied' options/values.
        """
        ...
