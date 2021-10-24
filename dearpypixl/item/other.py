import functools
from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from typing import Callable, Any, Iterable
from dearpypixl.item import Item


__all__ = [
    "UniqueItemMeta",
    "ItemLike",
]


class UniqueItemMeta(ABCMeta):
    """A metaclass for singleton classes.
    """
    __instance__ = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super().__call__(*args, **kwargs)
        return cls.__instance__


class ItemLike(metaclass=ABCMeta):
    """A template for item-like subclasses.
    """
    @abstractmethod
    def _configuration() -> dict: ...
    @abstractmethod
    def _configure() -> None: ...
    @abstractmethod
    def _configurations() -> Iterable: ...
    @abstractmethod
    def _tag(self) -> Any: ...

    __repr__ = Item.__repr__

    _appitems = Item._appitems
    tag = Item.tag

    def __getattr__(self, attr):
        try:
            return self._configuration()[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {attr!r}."
            )

    def __setattr__(self, attr, value):
        # Prioritizing descriptors
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        if attr in self._configurations:
            return self._configure(**{attr: value})
        object.__setattr__(self, attr, value)

    def configure(self, **config) -> None:
        [setattr(self, option, value) for option, value in config.items()]

    def configuration(self) -> dict:
        return {attr: val for attr, val in self._configuration().items()
                if attr in self._configurations}


class UpdaterList(list, metaclass=ABCMeta):
    """An instance of `list` that runs a callable immediately after
    the list has been updated through various methods.
    """
    @staticmethod
    @abstractmethod
    def _on_update(__iterable: Iterable): ...

    def __init__(self, __iterable = None):
        if __iterable:
            list.__init__(self, __iterable)
        else:
            list.__init__(self)

        self._on_update(self)

    def __on_update(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            rtn = method(self, *args, **kwargs)
            self._on_update(self)
            return rtn
        return wrapper

    @__on_update
    def __add__(self, x: list) -> list:
        list.__add__(self, x)

    @__on_update
    def append(self, __object):
        list.append(self, __object)

    @__on_update
    def extend(self, __iterable) -> None:
        list.extend(self, __iterable)

    @__on_update
    def pop(self, __index = ...) -> object:
        list.pop(self, __index)

    @__on_update
    def insert(self, __index, __object) -> None:
        list.insert(self, __index, __object)

    @__on_update
    def remove(self, __value) -> None:
        list.remove(self, __value)

    @__on_update
    def reverse(self) -> None:
        list.reverse(self)

    @__on_update
    def clear(self) -> None:
        list.clear(self)
