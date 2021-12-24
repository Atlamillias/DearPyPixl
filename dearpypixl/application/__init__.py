from typing import Callable
from abc import abstractmethod, ABCMeta
from dearpypixl.components import ItemAttribute, Item



class AppItemType(ABCMeta):
    # NOTE: 'ProtoItem` must be included in a class's mro when using `AppItemType` as a metaclass. 
    __slots__    = ()
    __instance__ = None
    __repr__     = Item.__repr__
    __int__      = Item.__int__

    @abstractmethod
    def tag()           -> int | str: ...
    @abstractmethod
    def configuration() -> Callable : ...
    @abstractmethod
    def information()   -> Callable : ...
    @abstractmethod
    def state()         -> Callable : ...

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        if not cls.__instance__:
            # Fallback instance for setting configuration properties when set on the
            # class instead of an instance.
            cls.__instance__ = cls()
        return cls

    def __setattr__(cls, name, value):
        # Workaround to emulate a set-able classmethod property without
        # overwriting the descriptor.
        if name in cls._item_config_attrs:
            return setattr(cls.__instance__, name, value)
        type.__setattr__(cls, name, value)


class AppAttribute(ItemAttribute):
    def __get__(self, instance: object, _type: AppItemType):
        # Effectively a classmethod property.
        if not _type.__instance__:
            return self
        return self.fget(_type, self.target)


