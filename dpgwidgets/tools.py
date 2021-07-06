from enum import Enum
from typing import Any
from dataclasses import dataclass, asdict


@dataclass
class Constant:
    def __iter__(self):
        return iter(asdict(self))

    def __getitem__(self, item):
        # calling <title> on the key so lower-case
        # strings can be used
        return self.__dict__[item.title()]

    def get(self, key, default_value = None) -> Any:
        try:
            return getattr(self, key.title())
        except AttributeError:
            return default_value
