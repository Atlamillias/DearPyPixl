"""Objects for various uses (except as Item-subclass mixins).
"""
import functools
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable
from dearpypixl.components.item import ProtoItem, Item


__all__ = [
    "UniqueItemMeta",
    "ItemLike",
    "UpdaterList",
]


class UniqueItemMeta(ABCMeta):
    """A metaclass for singleton classes.
    """
    __instance__ = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super().__call__(*args, **kwargs)
        return cls.__instance__


class ItemLike(ProtoItem, metaclass=ABCMeta):
    """A template for item-like subclasses. Mimics the core `Item` API.
    """
    __slots__ = ()
    
    @abstractmethod
    def _get_configuration(self) -> dict: ...
    @abstractmethod
    def _set_configuration(self, **kwargs) -> None: ...
    @abstractmethod
    def _config_params() -> Iterable: ...
    @abstractmethod
    def _tag(self) -> Any: ...

    _appitems = Item._AppItemsRegistry
    _setup_params: set = ()          # all parameters used by the constructor
    _readonly_params: set = ()       # read-only configuration
    _command = None

    tag = Item.tag

    def __init__(self, **kwargs):
        # Used in `configuration`.
        if not self._setup_params:
            self._setup_params = self._config_params

        # `_command` is not abstract for this object and is optional.
        if self._command:
            self._command(**kwargs)  # Item Creation

    def __repr__(self):
        configuration = {"tag": self._tag, **self.configuration()}

        return (
            f"{type(self).__qualname__}("
            + f", ".join((f'{attr}={val!r}' for attr,
                         val in configuration.items()))
            + f")"
        )

    def __getattr__(self, attr):
        try:
            return self._get_configuration()[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {attr!r}.")

    def __setattr__(self, attr, value):
        # Prioritizing descriptors.
        if hasattr(type(self), attr):
            return object.__setattr__(self, attr, value)
        elif attr in self._config_params:
            return self._set_configuration(**{attr: value})
        elif attr in self._readonly_params:
            raise AttributeError(f"{attr!r} is read-only and cannot be set.")
        object.__setattr__(self, attr, value)

    def configure(self, **config) -> None:
        return Item.configure(self, **config)

    def configuration(self) -> dict:
        setup_params = self._setup_params
        configuration = {optn: val for optn, val in
                         self._get_configuration().items()
                         if optn in setup_params}
        getattribute = object.__getattribute__

        for option, attribute in self._config_overrides.items():
            configuration.pop(option, None)   # no key overwrite if aliased
            configuration[attribute] = getattribute(self, attribute)
        return configuration


class UpdaterList(list, metaclass=ABCMeta):
    """An instance of `list` that runs a callable immediately after
    the list has been updated through various methods.
    """
    @staticmethod
    @abstractmethod
    def _on_update(__iterable: Iterable): ...

    def __init__(self, __iterable=None):
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
    def pop(self, __index=...) -> object:
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
