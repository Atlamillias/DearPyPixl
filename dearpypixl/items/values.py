from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "IntValue",
    "Int4Value",
    "BoolValue",
    "FloatValue",
    "Float4Value",
    "StringValue",
    "DoubleValue",
    "Double4Value",
    "ColorValue",
    "FloatVectValue",
    "SeriesValue",
]


class IntValue(Widget):
    """Adds a int value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (int, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : int       = ItemProperty(INFORM, None, None)
    value         : int       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvIntValue, "mvIntValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_int_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : int       = 0,
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Int4Value(Widget):
    """Adds a int4 value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str                   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[int] | tuple[int, ...] = ItemProperty(INFORM, None, None)
    value         : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvInt4Value, "mvInt4Value")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_int4_value

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        source             : int | str                   = 0,
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 0),
        parent             : int | str                   = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class BoolValue(Widget):
    """Adds a bool value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (bool, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : bool      = ItemProperty(INFORM, None, None)
    value         : bool      = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvBoolValue, "mvBoolValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_bool_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : bool      = False,
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class FloatValue(Widget):
    """Adds a float value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (float, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float     = ItemProperty(INFORM, None, None)
    value         : float     = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFloatValue, "mvFloatValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_float_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : float     = 0.0,
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Float4Value(Widget):
    """Adds a float4 value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str                  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = ItemProperty(INFORM, None, None)
    value         : list[float] | tuple[float] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFloat4Value, "mvFloat4Value")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_float4_value

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : int | str                  = 0,
        default_value      : list[float] | tuple[float] = (0.0, 0.0, 0.0, 0.0),
        parent             : int | str                  = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class StringValue(Widget):
    """Adds a string value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (str, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source            : int | str       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value     : str             = ItemProperty(INFORM, None, None)
    value             : str             = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvStringValue, "mvStringValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_string_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : str       = '',
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class DoubleValue(Widget):
    """Adds a double value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (float, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : float     = ItemProperty(INFORM, None, None)
    value         : float     = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDoubleValue, "mvDoubleValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_double_value

    def __init__(
        self,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : int | str       = 0   ,
        default_value     : float           = 0.0 ,
        parent            : int | str       = 13  ,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class Double4Value(Widget):
    """Adds a double value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (Any, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : Any       = ItemProperty(INFORM, None, None)
    value         : Any       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDouble4Value, "mvDouble4Value")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_double4_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : Any       = (0.0, 0.0, 0.0, 0.0),
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class ColorValue(Widget):
    """Adds a color value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str                  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = ItemProperty(INFORM, None, None)
    value         : list[float] | tuple[float] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvColorValue, "mvColorValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_color_value

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : int | str                  = 0,
        default_value      : list[float] | tuple[float] = (0.0, 0.0, 0.0, 0.0),
        parent             : int | str                  = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class FloatVectValue(Widget):
    """Adds a float vect value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str                  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = ItemProperty(INFORM, None, None)
    value         : list[float] | tuple[float] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvFloatVectValue, "mvFloatVectValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_float_vect_value

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : int | str                  = 0,
        default_value      : list[float] | tuple[float] = (),
        parent             : int | str                  = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )


class SeriesValue(Widget):
    """Adds a plot series value.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * source (int | str, optional): Overrides 'id' as value storage key.
            * default_value (Any, optional): Initial starting value for the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
        Returns:
            int | str
    """
    source        : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : Any       = ItemProperty(INFORM, None, None)
    value         : Any       = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvSeriesValue, "mvSeriesValue")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvValueRegistry,)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_series_value

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        source             : int | str = 0,
        default_value      : Any       = (),
        parent             : int | str = 13,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            source=source,
            default_value=default_value,
            parent=parent,
            **kwargs,
        )
