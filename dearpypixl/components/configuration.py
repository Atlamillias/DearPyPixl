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


class DearPyGuiConfiguration:
    def __set_name__(self, __type: type, name: str):
        self.name = name

    def __get__(self, instance, pytype: type):
        ...

    def __set__(self, instance, value):
        ...