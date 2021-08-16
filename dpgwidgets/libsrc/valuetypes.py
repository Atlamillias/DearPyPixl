from typing import (
    Any,
    Callable,
    Union,
    Dict,
    Tuple,
    Set,
    List,
)
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
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (bool): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_bool_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: bool = False, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class ColorValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Union[List[float], Tuple[float]]): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_color_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class Double4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Any): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_double4_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Any = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class DoubleValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (float): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_double_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: float = 0.0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class Float4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Union[List[float], Tuple[float]]): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_float4_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Union[List[float], Tuple[float]] = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class FloatValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (float): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_float_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: float = 0.0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class FloatVectValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Union[List[float], Tuple[float]]): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_float_vect_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Union[List[float], Tuple[float]] = (), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class Int4Value(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Union[List[int], Tuple[int]]): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_int4_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Union[List[int], Tuple[int]] = (0, 0, 0, 0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class IntValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (int): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_int_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: int = 0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class SeriesValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (Any): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_series_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: Any = (), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent


class StringValue(Item):
    """Undocumented
    Args:
            **label (str): Overrides 'name' as label.
            **user_data (Any): User data for callbacks.
            **use_internal_label (bool): Use generated internal label instead of user specified (appends ### uuid).
            **id (Union[int, str]): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **source (Union[int, str]): Overrides 'id' as value storage key.
            **default_value (str): 
            **parent (Union[int, str]): Parent to add this item to. (runtime adding)
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_string_value

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        source: Union[int, str] = 0, 
        default_value: str = '', 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.default_value = default_value
        self.parent = parent
