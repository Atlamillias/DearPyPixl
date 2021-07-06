from typing import Callable, Any

from . import idpg
from ._item import Item


##################################################
## Note: this file was automatically generated. ##
##################################################


class BoolValue(Item):
    _command: Callable = idpg.add_bool_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: bool = False,
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class ColorValue(Item):
    _command: Callable = idpg.add_color_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class Double4Value(Item):
    _command: Callable = idpg.add_double4_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: Any = (0.0, 0.0, 0.0, 0.0),
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class DoubleValue(Item):
    _command: Callable = idpg.add_double_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: float = 0.0,
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class Float4Value(Item):
    _command: Callable = idpg.add_float4_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class FloatValue(Item):
    _command: Callable = idpg.add_float_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: float = 0.0,
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class FloatVectValue(Item):
    _command: Callable = idpg.add_float_vect_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: list[float] = [],
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class Int4Value(Item):
    _command: Callable = idpg.add_int4_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: list[int] = [0, 0, 0, 0],
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class IntValue(Item):
    _command: Callable = idpg.add_int_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: int = 0,
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class SeriesValue(Item):
    _command: Callable = idpg.add_series_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: Any = (),
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent


class StringValue(Item):
    _command: Callable = idpg.add_string_value

    def __init__(
        self,
        label: str = None,
        source: int = 0,
        user_data: Any = None,
        default_value: str = '',
        parent: int = 13,
        **kwargs
    ):
        super().__init__(
        label=label,
        source=source,
        user_data=user_data,
        default_value=default_value,
        parent=parent,
        **kwargs
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.default_value = default_value
        self.parent = parent
