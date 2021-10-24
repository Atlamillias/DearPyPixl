from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from dearpypixl.item import Item

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
    """Adds a bool value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (bool, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: bool = False, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class ColorValue(Item):
    """Adds a color value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Union[List[float], Tuple[float, ...]], optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class Double4Value(Item):
    """Adds a double value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Any, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Any = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class DoubleValue(Item):
    """Adds a double value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (float, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: float = 0.0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class Float4Value(Item):
    """Adds a float4 value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Union[List[float], Tuple[float, ...]], optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class FloatValue(Item):
    """Adds a float value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (float, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: float = 0.0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class FloatVectValue(Item):
    """Adds a float vect value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Union[List[float], Tuple[float, ...]], optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Union[List[float], Tuple[float, ...]] = (), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class Int4Value(Item):
    """Adds a int4 value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Union[List[int], Tuple[int, ...]], optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 0), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class IntValue(Item):
    """Adds a int value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (int, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: int = 0, 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class SeriesValue(Item):
    """Adds a plot series value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (Any, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: Any = (), 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value


class StringValue(Item):
    """Adds a string value.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            source (Union[int, str], optional): Overrides 'id' as value storage key.
            default_value (str, optional): 
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            id (Union[int, str], optional): (deprecated) 
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
        value: str = '', 
        parent: Union[int, str] = 13, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            value=value,
            parent=parent,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.source = source
        self.value = value
