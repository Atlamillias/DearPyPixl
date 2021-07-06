from __future__ import annotations
from typing import Callable, Any
from abc import abstractmethod, ABCMeta


from . import idpg
from .dpgwrap._widget import Container


class Registry(Container, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(
        self,
        show: bool = True,
        label: str = None,
        **kwargs,
    ):
        super().__init__(
            show=show,
            label=label,
            **kwargs
        )
        self.show = show
        self.label = label


class FontRegistry(Registry):
    _command = idpg.add_font_registry

class HandlerRegistry(Registry):
    _command = idpg.add_handler_registry

class TextureRegistry(Registry):
    _command = idpg.add_texture_registry

class ValueRegistry(Container):  # excludes "show"/"enabled"
    _command = idpg.add_value_registry

    def __init__(self, label: str = None, **kwargs):
        super().__init__(label=label, **kwargs)
        self.label = label
