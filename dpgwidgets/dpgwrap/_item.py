from abc import ABCMeta, abstractmethod
from typing import Callable

from . import idpg



class Item(metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    __config = set()

    def __init__(self, **kwargs):
        if parent:= kwargs.pop("parent", None):
            if not isinstance(parent, Context):
                kwargs['parent'] = int(parent)
                parent = None
            else:
                idpg.push_container_stack(int(parent))

        kwargs["label"] = kwargs.get('label', self.__class__.__name__)
        self.__id = self._command(**kwargs)

        if parent:
            idpg.pop_container_stack()

        [self.__config.add(optn) for optn in kwargs.keys()]

    def __str__(self):
        return f"{self.__id}"

    def __int__(self):
        return self.__id

    def __repr__(self):
        mVAppType = idpg.get_item_info(self.id)["type"].lstrip('::')[-1]
        return f"{self.__class__.__qualname__} ({type(self)}) => \
            (<{mVAppType} '{self.__id}'>)"

    def __getattr__(self, attr):
        if attr in self.__config:
            try:
                return idpg.get_item_configuration(self.__id)[attr]
            except KeyError:
                return super().__getattr__(attr)

        return super().__getattr__(attr)

    def __setattr__(self, attr, value):
        if attr in self.__config:
            idpg.configure_item(self.__id, **{attr: value})
        else:
            super().__setattr__(attr, value)

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        """Return the current state of the widget."""
        return idpg.get_item_state(self.__id)

    @property
    def value(self):
        """Return the widget value (if any)."""
        return idpg.get_value(self.__id)

    def refresh(self):
        """Deletes all children in the widget, if any."""
        idpg.delete_item(self.__id, children_only=True)

    def remove(self):
        """Deletes the widget (and children)."""
        idpg.delete_item(self.__id)

    def configure(self, **config):
        """Updates the widget configuration."""
        idpg.configure_item(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current widget configuration, or
        only <option> if specified."""
        if option:
            return idpg.get_item_configuration(self.__id)[option]

        return idpg.get_item_configuration(self.__id)


class Context:  # mixin
    def __enter__(self):
        idpg.push_container_stack(self.id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        idpg.pop_container_stack(self.id)
