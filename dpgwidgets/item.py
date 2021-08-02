import inspect
from abc import ABCMeta, abstractmethod
from typing import Callable

from dearpygui import dearpygui as dpg, _dearpygui as idpg


class Item(metaclass=ABCMeta):
    """Base class for all wrapped DearPyGui items.

    Args:
        **kwargs (optional): Configuration options used to create
    a DPG item.
    
    """
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
                                       if optn != "id" and
                                       optn != "default_value"}

        super().__init__()

    @classmethod
    def staged_init(cls, **kwargs):
        """Alternative constructor. <class "Item"> is initialized but
        cls._command is not called. It is assumed that the item already
        exists or will exist later. Mixin classes are initialized
        normally.
        
        Notes:
            - <id> MUST be provided in <kwargs> to initialize this way.
            - In the <class "Item"> subclass tree, only <class "Item">
            is technically initialized. All other classes are NOT.
            Default parameters are fetched from the highest-level class
            , are merged with <kwargs>, and then are set as instance
            attributes.
            - If a keyword in <kwargs> is not in the fetched parameters
            for the item, a TypeError will be raised.
        """
        # Doing this feels awful w/multiple inheritance but
        # its better than passing undocumented arguments to
        # __init__ and running code on conditionals.

        # NOTE: We're only calling __init__ on mixins, and
        # pseudo-initializing <class "Item">.

        # Item.__init__
        item = cls.__new__(cls)
        item_cls = item.__class__

        if parent := kwargs.pop("parent", None):
            kwargs["parent"] = int(parent)
        kwargs["label"] = kwargs.get('label') or item_cls.__name__

        item.__id = kwargs.pop("id")
        # cache config attrs for future items of the same type
        if not item.__config:
            item_cls.__config = {optn for optn in kwargs.keys() if
                                 optn != "id" and optn != "default_value"}

        # Initializing mixins
        [super(c, item).__init__() for c in
         item_cls.mro() if c.__name__.endswith("Support")]

        # Fetching default parameters from type(item)
        item_attrs = inspect.signature(item_cls).parameters.values()
        item_attrs = {p.name: p.default for p in
                      item_attrs if p.name != "kwargs"}
        for kw in kwargs:
            if not item_attrs.get(kw, None):
                raise TypeError(
                    f"{item_cls} got an unexpected keyword argument {kw}.")

        [setattr(item, attr, val) for attr, val in item_attrs.items()]

        return item

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
    def value(self):
        """Return the widget value (if any)."""
        return idpg.get_value(self.__id)

    @value.setter
    def value(self, value):
        idpg.set_value(self.__id, value)

    def set_value(self, value):
        idpg.set_value(self.__id, value)

    def remove(self):
        """Deletes the widget (and children)."""
        idpg.delete_item(self.__id)

    def refresh(self):
        """Deletes all children in the widget, if any."""
        idpg.delete_item(self.id, children_only=True)

    def configure(self, **config):
        """Updates the widget configuration."""
        idpg.configure_item(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current widget configuration, or
        only <option> if specified."""
        if option:
            return idpg.get_item_configuration(self.__id)[option]

        return idpg.get_item_configuration(self.__id)

    def state(self) -> dict:
        """Return the current state of the widget."""
        return idpg.get_item_state(self.__id)


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
