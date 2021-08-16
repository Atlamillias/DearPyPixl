from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable

from dearpygui import dearpygui as dpg
from dearpygui._dearpygui import (
    configure_item,
    get_item_configuration,
    set_value,
    delete_item,
    generate_uuid,
)


__all__ = [
    "Item",
    "ContextSupport"
]


# This is called a lot (or called *enough*, rather)
_OBJ_GET_ATTRIBUTE = object.__getattribute__



class Item(metaclass=ABCMeta):
    """Base class for all wrapped DearPyGui items.

    Args:
        **kwargs (optional): Configuration options used to create
    an item internally.
    
    """

    @abstractmethod
    def _command() -> Callable: ...
    _item_config: list[str] = set()
    _addl_config_in_repr: list[str] = []  # custom attrs/properties included in repr

    APPITEMS = {}

    def __init__(self, **kwargs):
        self._id = kwargs.pop("id", None) or generate_uuid()
        self._item_config = {}  # this remains empty until internal item is made
        cls = type(self)
        # Internal library returns `int` (id) when making items. Calling int on
        # a parent means it can be <class 'Item'> instances or 'raw' items.
        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)
        # Provides a readable label if None (hidden by passing empty strings).
        if kwargs.get("label", None) is None:
            kwargs["label"] = cls.__name__

        cls._command(id=self._id,**kwargs)  # item creation
        # We aren't tracking 'default_value' - most items can have a 'value'
        # but only some have 'default_value', which is weird.
        if default_value := kwargs.pop("default_value", None):
            set_value(self._id, default_value)

        if not self._item_config:
            # id isn't tracked in config because it's set as a property and
            # can't be changed internally anyway. So if it was manually
            # provided, we don't want it in here.
            kwargs.pop("id", None)
            cls._item_config = {option for option in kwargs.keys()}

        # Registering new item
        cls.APPITEMS[self._id] = self
        super().__init__()

    def __str__(self):
        try:
            return get_item_configuration(self._id)["label"]
        except AttributeError:
            return f"{self._id}"

    def __int__(self):
        return self._id

    def __repr__(self):
        config = {"id": self._id, "label": None} | {attr: getattr(self,attr) for
                                                    attr in self._addl_config_in_repr}
        for optn, val in self.configuration().items():
            # Formatting strings for a proper representation.
            if isinstance(val, str):
                val = f"'{val}'"
            config[optn] = val

        config = ", ".join((
            f'{optn}={val}' for optn, val in config.items()
        )).rstrip(", ")
        return f"{self.__class__.__qualname__}({config})"

    def __getattribute__(self, attr: str):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_item_config"):
            id = _OBJ_GET_ATTRIBUTE(self, "_id")
            return get_item_configuration(id)[attr]

        return _OBJ_GET_ATTRIBUTE(self, attr)

    def __setattr__(self, attr, value):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_item_config"):
            configure_item(self._id, **{attr: value})
        else:
            object.__setattr__(self, attr, value)

    @property
    def id(self):
        return self._id

    def delete(self):
        """Deletes the item and any child items it may have.

        NOTE: Because of how `del`, `__del__`, and garbage
        collection work in Python, it is STRONGLY advised
        to call this method to delete items and not `del` to guarantee
        cleanup is ran. The `del` statement doesn't always call `__del__`,
        so cleanup might not run even if it were defined (which it's not).
        """
        try:
            delete_item(self._id)
        except SystemError:
            pass

        self.__class__.APPITEMS.pop(self._id, None)

        del self

    def configure(self, **config) -> None:
        """Updates the item configuration item. It is the equivelent
        of calling `setattr`, and can be used to configure multiple
        attributes.
        
        """
        [setattr(self, option, value) for option, value in config.items()]

    def configuration(self, option: str = None):
        """Returns the item's configuration options and values
        that are internally used to manage the item. If <option>
        is included, only the value of that option will be returned.
        
        NOTE: Typically, attributes included in configuration are the
        parameters used to create an instance of an item. This will
        not include other instance attributes, and does not replace
        `getattr`.
        """
        configs = get_item_configuration(self._id)
        return configs.get(option, configs)


    def _item_setup(self):
        ...



class ContextSupport:  # mixin
    """Mixin class for Item subclasses that are intended to act
    as containers. Containers need to be set as the "parent" -
    the item that will be holding any new items created within the
    context of their **with** statement.
    """
    def __enter__(self):
        dpg.push_container_stack(self.id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        dpg.pop_container_stack()




