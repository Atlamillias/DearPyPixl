from abc import ABCMeta, abstractmethod
from typing import Callable

from . import dpg


class Item(metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    __config = set()

    def __init__(self, **kwargs):
        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)
        kwargs["label"] = kwargs.get('label') or self.__class__.__name__

        self.__id = self.__class__._command(**kwargs)

        # cache config attrs for future items of the same type
        if not self.__config:
            self.__class__.__config = {optn for optn in kwargs.keys()
                                       if optn != "id"}

        super().__init__()

    def __str__(self):
        try:
            return self.label
        except AttributeError:
            return f"{self.__id}"

    def __int__(self):
        return self.__id

    def __repr__(self):
        mVAppType = dpg.get_item_info(self.id)["type"].lstrip('::')[-1]
        return f"{self.__class__.__qualname__} ({type(self)}) => \
            (<{mVAppType} '{self.__id}'>)"

    def __getattribute__(self, attr: str):
        if attr.startswith("_") or attr == "id":
            return super().__getattribute__(attr)
        elif attr in super().__getattribute__("_Item__config"):
            id = super().__getattribute__("_Item__id")
            return dpg.get_item_configuration(id)[attr]
        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        if attr in object.__getattribute__(self, "_Item__config"):
            dpg.configure_item(self.__id, **{attr: value})
        else:
            object.__setattr__(self, attr, value)

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        """Return the current state of the widget."""
        return dpg.get_item_state(self.__id)

    @property
    def value(self):
        """Return the widget value (if any)."""
        return dpg.get_value(self.__id)

    @value.setter
    def value(self, value):
        dpg.set_value(self.__id, value)

    def remove(self):
        """Deletes the widget (and children)."""
        dpg.delete_item(self.__id)

    def refresh(self):
        """Deletes all children in the widget, if any."""
        dpg.delete_item(self.id, children_only=True)

    def configure(self, **config):
        """Updates the widget configuration."""
        dpg.configure_item(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current widget configuration, or
        only <option> if specified."""
        if option:
            return dpg.get_item_configuration(self.__id)[option]

        return dpg.get_item_configuration(self.__id)

    def set_value(self, value):
        dpg.set_value(self.__id, value)


class ContextSupport:  # mixin
    def __enter__(self):
        dpg.push_container_stack(self.id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        dpg.pop_container_stack()
