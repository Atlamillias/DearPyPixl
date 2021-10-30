from typing import Callable, Any
from dearpygui._dearpygui import (
    generate_uuid,
    configure_item,
    get_item_configuration,
    get_item_info,
    get_item_state,
    get_all_items,
)
from dearpygui.dearpygui import (
    delete_item,
    get_all_items,
    set_value,
    get_value,
    move_item,
    unstage,
)

class ItemAttribute:
    def __init__(
        self,
        getter: Callable = None,
        setter: Callable = None,
        attr_name: str = None,
        category: str = None,
        doc: str = None
    ):
        """DearPyGui configuration handler. Functionally similar to the `property`
        build-in, but specific to dearpygui keyword attributes. Cannot be used
        as a decorator.

        Args:
            * getter (Callable, optional): The callable used to get the attribute.
            Defaults to None.
            * setter (Callable, optional): The callable used to set the attribute.
            Defaults to None.
            * attr_name (str, optional): The key or name used for the callable(s).
            Only needed if the key or name differs from the name of the attribute.
            Defaults to None (`self._name`).
            * category (str, optional): The parameter classification. Acceptable values
            are "configuration", "state", and "information". Default is None ("configuration").
            * doc (str, optional): Docstring. Defaults to None.
        """
        self.fget = getter
        self.fset = setter
        if doc is None and getter is not None:
            doc = getter.__doc__
        self.__doc__ = doc
        self._name = ''
        self._attr_name = attr_name
        self._category = category or self._category_map[getter]

    def __set_name__(self, __type: type, name: str):
        self._name = name
        self._item = __type
        self._attr_name = self._attr_name or name

    def __get__(self, instance: object, __type: type):
        if instance is None:
            return self
        return self.fget(instance._tag)[self._attr_name]

    def __set__(self, instance: object, value):
        if self.fset is None:
            raise AttributeError(f"The {self._name!r} attribute is read-only and cannot be set.")
        self.fset(instance._tag, **{self._attr_name: value})

    _CATEGORIES = (
        "configuration",
        "information",
        "state",
    )
    _category_map = {
        get_item_configuration: _CATEGORIES[0],
        get_item_info: _CATEGORIES[1],
        get_item_state: _CATEGORIES[2],
        get_value: _CATEGORIES[0]
    }
