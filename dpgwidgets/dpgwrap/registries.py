from typing import Callable, Any

from . import dpg
from ._item import Item, Context


##################################################
## Note: this file was automatically generated. ##
##################################################


class FontRegistry(Item, Context):
    _command: Callable = dpg.add_font_registry

    def __init__(self, label: str = None, show: bool = True, user_data: Any = None, **kwargs):
        super().__init__(label=label, show=show, user_data=user_data, **kwargs)
        self.label = label
        self.show = show
        self.user_data = user_data


class HandlerRegistry(Item, Context):
    _command: Callable = dpg.add_handler_registry

    def __init__(self, label: str = None, show: bool = True, user_data: Any = None, **kwargs):
        super().__init__(label=label, show=show, user_data=user_data, **kwargs)
        self.label = label
        self.show = show
        self.user_data = user_data


class TextureRegistry(Item, Context):
    _command: Callable = dpg.add_texture_registry

    def __init__(self, label: str = None, user_data: Any = None, show: bool = False, **kwargs):
        super().__init__(label=label, user_data=user_data, show=show, **kwargs)
        self.label = label
        self.user_data = user_data
        self.show = show


class ValueRegistry(Item, Context):
    _command: Callable = dpg.add_value_registry

    def __init__(self, label: str = None, user_data: Any = None, **kwargs):
        super().__init__(label=label, user_data=user_data, **kwargs)
        self.label = label
        self.user_data = user_data
