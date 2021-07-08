from enum import Enum
from typing import Any
from dataclasses import dataclass, asdict


@dataclass
class Lookup:
    __map = None

    def __post_init__(self):
        self.__map = asdict(self)

    def __iter__(self):
        return iter(self.__map)

    def __getitem__(self, item):
        return self.__map[item]

    def get(self, key, default_value = None) -> Any:
        try:
            return getattr(self, key)
        except AttributeError:
            return default_value
