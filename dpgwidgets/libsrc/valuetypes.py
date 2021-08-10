from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.item import Item, ContextSupport

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "BoolValue",
    "ColorValue",
    "Double4Value",
    "DoubleValue",
    "Float4Value",
    "FloatValue",
    "FloatVectValue",
    "Int4Value",
    "IntValue",
    "SeriesValue",
    "StringValue",
]


class BoolValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (bool): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_bool_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: bool = False, 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class ColorValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (List[float]): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_color_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class Double4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (Any): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_double4_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: Any = (0.0, 0.0, 0.0, 0.0), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class DoubleValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (float): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_double_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: float = 0.0, 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class Float4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (List[float]): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_float4_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: list[float] = (0.0, 0.0, 0.0, 0.0), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class FloatValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (float): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_float_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: float = 0.0, 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class FloatVectValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (List[float]): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_float_vect_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: list[float] = (), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class Int4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (List[int]): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_int4_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: list[int] = (0, 0, 0, 0), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class IntValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (int): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_int_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: int = 0, 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class SeriesValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (Any): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_series_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: Any = (), 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent


class StringValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (int): Overrides 'id' as value storage key.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **default_value (str): 
            **parent (int): Parent to add this item to. (runtime adding)
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_string_value

    def __init__(
        self, 
        label: str = None, 
        source: int = 0, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        default_value: str = '', 
        parent: int = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            source=source,
            user_data=user_data,
            use_internal_label=use_internal_label,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.source = source
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.default_value = default_value
        self.parent = parent
