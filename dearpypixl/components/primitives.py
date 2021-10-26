"""Compound primitive types for Item subclasses. Used internally for
building basic items.
"""
from typing import Callable, Iterable, Any
from abc import ABCMeta, abstractmethod
from dearpygui._dearpygui import pop_container_stack, push_container_stack
from dearpypixl.components.item import Item, ItemAttrOverride



class AbstractBoundItem(metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...              # class attribute
    @abstractmethod
    def bind(self, item: Item) -> None: ...      # method
    @abstractmethod
    def unbind(self, item: Item) -> None: ...    # method

    def __init__(self, **kwargs):
        self._target_uuids: set[int] = set()
        super().__init__(**kwargs)


    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        pop_container_stack()

    @property
    def targets(self) -> list[Item]:
        """Return a list of items that are bound to this item.
        """
        target_uuids = self._target_uuids
        appitems = type(self)._appitems
        return [target_item for targets in target_uuids
                for target in targets if
                (target_item := appitems.get(target, None))]


class RegistryItem(Item, metaclass=ABCMeta):
    """Extendable base object for registry items.
    """
    @abstractmethod
    def _command() -> Callable: ...              # class attribute

    def __init__(
        self,
        label: str = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        **kwargs,
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )

        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label

    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        pop_container_stack()
