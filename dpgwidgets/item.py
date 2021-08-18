from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Callable, Any

from dearpygui import dearpygui as dpg
from dearpygui._dearpygui import (
    configure_item,
    get_item_configuration,
    get_item_info,
    set_value,
    get_value,
    delete_item,
    generate_uuid,
)
from dpgwidgets.error import AppItemConfigError


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
    _appitem_config = set()
    _addl_config_in_repr: list[str] = []  # custom attrs/properties included in repr

    APPITEMS = {}

    def __init__(self, **kwargs):
        self._id = kwargs.pop("id", None) or generate_uuid()
        cls = type(self)
        # Internal library returns `int` (id) when making items. Calling int on
        # a parent means it can be <class 'Item'> instances or 'raw' items.
        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)
        # Provides a readable label if None. Not using false equality i.e.
        # `if not x` because passing an empty string is a valid value 
        # (it hides the label).
        if kwargs.get("label", None) is None:
            kwargs["label"] = cls.__name__

        # Item is created here.
        cls._command(id=self._id,**kwargs)
        # We aren't tracking 'default_value' - most items can have a 'value'
        # but only some have 'default_value', which is weird.
        if default_value := kwargs.pop("default_value", None):
            set_value(self._id, default_value)
        # `__getattribute__` and `__setattr__` catch attrs found in
        # self._appitem_config to properly get/set them. They are bound to 
        # the class and not instance. This is so the behavior can be 
        # "turned off" by binding self._appitem_config to an empty sequence.
        # Deleting the instance attribute will restore the behavior.
        if not self._appitem_config:
            # We aren't tracking "special" configuration. They either
            # can't be set, or have gimmicks and require unique handling.
            kwargs.pop("id", None)
            kwargs.pop("parent", None)
            cls._appitem_config = {option for option in kwargs.keys()}

        # Registering new item.
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
        # Building this early to have some control over the order.
        config = {"id": self._id, "label": None} | {attr: getattr(self,attr) for
                                                    attr in self._addl_config_in_repr}
        for optn, val in self.configuration().items():
            # Wrapping strings w/single quotes to improve readability.
            if isinstance(val, str):
                val = f"'{val}'"
            config[optn] = val
        # Output as "class(param=p_value,...)"
        config = ", ".join((
            f'{optn}={val}' for optn, val in config.items()
        )).rstrip(", ")
        return f"{type(self).__qualname__}({config})"

    def __getattribute__(self, attr: str):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_appitem_config"):
            id = _OBJ_GET_ATTRIBUTE(self, "_id")
            return get_item_configuration(id)[attr]
        return _OBJ_GET_ATTRIBUTE(self, attr)

    def __setattr__(self, attr, value):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_appitem_config"):
            configure_item(self._id, **{attr: value})
            return None
        object.__setattr__(self, attr, value)

    @property
    def id(self):
        """The unique identifier for the item. Cannot be changed
        once the item has been instantiated.
        """
        return self._id

    @property
    def parent(self):
        """The item parenting this one. Setting this will attempt to
        re-parent the item.
        """
        current_parent = get_item_info(self._id)["parent"]
        # Tries to return the parent object, but returns
        # the id if it doesn't exist.
        return type(self).APPITEMS.get(current_parent, current_parent)
    @parent.setter
    def parent(self, value):
        value = int(value)
        current_parent = get_item_info(self._id)["parent"]
        # If the value would be the default value (0 or None),
        # or if the parent wouldn't change, do nothing.
        if not value or value == current_parent:
            return None
        # Moving the item is the only way to "re-parent".
        try:
            dpg.move_item(self._id, parent=value)
        except SystemError:
            item_exists = dpg.does_item_exist(value)
            # 2021-08-18: `get_item_info(...)["container"]` always
            # returns False on window items. Unsure if this is a bug.
            if item_exists and get_item_info(value)["container"]:
                msg = f"'parent' is unsupported by <class '{type(self).__name__}'> and cannot be set."
            elif item_exists:
                msg = f"'parent' must be a container."
            else:
                msg = f"'parent' could not be found or does not exist."
            raise AppItemConfigError(msg)

    @property
    def value(self) -> Any:
        """Return the item value (if any).
        """
        return get_value(self.id)
    @value.setter
    def value(self, value: Any):
        try:
            set_value(self.id, value)
        except SystemError:
            raise AppItemConfigError(
                f"'value' is unsupported by <class '{type(self).__name__}'> and cannot be set."
            )
        # 2021-08-06: A SystemError should be thrown if the item
        # isn't capable of having a value set on it, but it is
        # being supressed internally - the `except` code will
        # never actually run. As a workaround, we check to see if
        # the value we tried to set "stuck". If the value is still
        # None, we raise an error. This should be deleted later
        # once the issue is resolved.
        if get_value(self.id) != value:
            raise AppItemConfigError(
                f"'value' is unsupported by <class '{type(self).__name__}'> and cannot be set."
            )

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

        type(self).APPITEMS.pop(self._id, None)

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




