from abc import ABCMeta, abstractmethod
from typing import Callable
import inspect

from dearpygui import dearpygui as dpg, _dearpygui as idpg
from dearpygui._dearpygui import (
    configure_item,
    get_item_configuration,
    get_item_info,
    set_value,
    delete_item,
)


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
    __config = set()

    def __init__(self, **kwargs):
        # Internal library returns `int` (id) when making items. Calling int on
        # a parent means it can be <class 'Item'> instances or 'raw' items.
        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)

        cls = self.__class__
        # Provides a readable label if None (hidden by passing empty strings).
        kwargs["label"] = kwargs.get('label') or cls.__name__
        self.__id = cls._command(**kwargs)  # item creation
        # We aren't tracking 'default_value' - most items can have a 'value'
        # but only some have 'default_value', which is weird.
        if default_value := kwargs.pop("default_value", None):
            set_value(self.__id, default_value)

        if not self.__config:
            # id isn't tracked in config because it's set as a property and
            # can't be changed internally anyway. So if it was manually 
            # provided, we don't want it in here.
            kwargs.pop("id", None)
            cls.__config = {option for option in kwargs.keys()}
                                       
        super().__init__()

    def __str__(self):
        try:
            return self.label
        except AttributeError:
            return f"{self.__id}"

    def __int__(self):
        return self.__id

    def __repr__(self):
        mVAppType = get_item_info(self.id)["type"].lstrip('::')[-1]
        return f"{self.__class__.__qualname__} ({type(self)}) => \
            (<{mVAppType} '{self.__id}'>)"

    def __getattribute__(self, attr: str):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_Item__config"):
            id = _OBJ_GET_ATTRIBUTE(self, "_Item__id")
            return get_item_configuration(id)[attr]

        return _OBJ_GET_ATTRIBUTE(self, attr)

    def __setattr__(self, attr, value):
        if attr in _OBJ_GET_ATTRIBUTE(self, "_Item__config"):
            configure_item(self.__id, **{attr: value})
        else:
            object.__setattr__(self, attr, value)

    @property
    def id(self):
        return self.__id

    def delete(self):
        """Deletes the item and any child items it may have.
        """
        # NOTE: __del__ is not defined because it's not always called
        # when `del` is, and therefore wouldn't always call `delete_item`.
        # However this method will obviously always call `delete_item`
        # and `del`.
        try:
            delete_item(self.__id)
        except SystemError:
            pass

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
        configs = get_item_configuration(self.__id)
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
