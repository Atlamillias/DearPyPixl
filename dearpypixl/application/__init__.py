from typing import Callable
from abc import abstractmethod, ABCMeta, ABC
from dearpypixl.components import ItemAttribute, Item, ProtoItem



class AppItemMeta(type):
    def __setattr__(cls, name, value):
        # Workaround to emulate a set-able classmethod property without
        # overwriting the descriptor.
        if name in cls._item_config_attrs:
            return setattr(cls.__instance__, name, value)
        super().__setattr__(name, value)
    
    def __repr__(cls) -> str:
        return f"{cls.__qualname__}(tag={cls.tag!r})"

    def __int__(cls)  -> int:
        return cls.tag


class AppItem(ProtoItem, ABC, metaclass=type("AppItemType", (AppItemMeta, ABCMeta), {})):
    @abstractmethod
    def tag()           -> int | str: ...
    @abstractmethod
    def configuration() -> Callable : ...
    @abstractmethod
    def information()   -> Callable : ...
    @abstractmethod
    def state()         -> Callable : ...

    __slots__    = ()
    __instance__ = None
    
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.mro()[1] == AppItem:
            cls.__instance__ = cls()


class AppAttribute(ItemAttribute):
    def __get__(self, instance: object, _type: AppItem):
        # Effectively a classmethod property.
        if not _type.__instance__:
            return self
        return self.fget(_type, self.target)


