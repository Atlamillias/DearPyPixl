from typing import Callable, Any

from . import idpg
from ._item import Item, Context


##################################################
## Note: this file was automatically generated. ##
##################################################


class FontRegistry(Item, Context):
    _command: Callable = idpg.add_font_registry

    def __init__(self, label: str = None, show: bool = True, **kwargs):
        super().__init__(label=label, show=show, **kwargs)
        self.label = label
        self.show = show


class HandlerRegistry(Item, Context):
    _command: Callable = idpg.add_handler_registry

    def __init__(self, label: str = None, show: bool = True, **kwargs):
        super().__init__(label=label, show=show, **kwargs)
        self.label = label
        self.show = show


class TextureRegistry(Item, Context):
    _command: Callable = idpg.add_texture_registry

    def __init__(self, label: str = None, show: bool = False, **kwargs):
        super().__init__(label=label, show=show, **kwargs)
        self.label = label
        self.show = show


class ValueRegistry(Item, Context):
    _command: Callable = idpg.add_value_registry

    def __init__(self, label: str = None, **kwargs):
        super().__init__(label=label, **kwargs)
        self.label = label
