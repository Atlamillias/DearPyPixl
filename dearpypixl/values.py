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


class IntValue(WidgetItem):
    """Adds a int value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (int, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvIntValue, "mvIntValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_int_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : int       = __dearpypixl__.set_information(None, None)
    value         : int       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class Int4Value(WidgetItem):
    """Adds a int4 value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (list[int] | tuple[int, ...], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvInt4Value, "mvInt4Value"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_int4_value,
    )

    source        : int | str                   = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[int] | tuple[int, ...] = __dearpypixl__.set_information(None, None)
    value         : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        source             : Item | int                  = 0,
        default_value      : list[int] | tuple[int, ...] = (0, 0, 0, 0),
        parent             : Item | int                  = 13,
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


class BoolValue(WidgetItem):
    """Adds a bool value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (bool, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvBoolValue, "mvBoolValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_bool_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : bool      = __dearpypixl__.set_information(None, None)
    value         : bool      = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class FloatValue(WidgetItem):
    """Adds a float value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFloatValue, "mvFloatValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_float_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float     = __dearpypixl__.set_information(None, None)
    value         : float     = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class Float4Value(WidgetItem):
    """Adds a float4 value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFloat4Value, "mvFloat4Value"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_float4_value,
    )

    source        : int | str                  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = __dearpypixl__.set_information(None, None)
    value         : list[float] | tuple[float] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : Item | int                 = 0,
        default_value      : list[float] | tuple[float] = (0.0, 0.0, 0.0, 0.0),
        parent             : Item | int                 = 13,
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


class StringValue(WidgetItem):
    """Adds a string value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (str, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvStringValue, "mvStringValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_string_value,
    )

    source            : int | str       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value     : str             = __dearpypixl__.set_information(None, None)
    value             : str             = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class DoubleValue(WidgetItem):
    """Adds a double value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (float, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDoubleValue, "mvDoubleValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_double_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : float     = __dearpypixl__.set_information(None, None)
    value         : float     = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        source            : Item | int      = 0   ,
        default_value     : float           = 0.0 ,
        parent            : Item | int      = 13  ,
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


class Double4Value(WidgetItem):
    """Adds a double value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (Any, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDouble4Value, "mvDouble4Value"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_double4_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : Any       = __dearpypixl__.set_information(None, None)
    value         : Any       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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


class ColorValue(WidgetItem):
    """Adds a color value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvColorValue, "mvColorValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_color_value,
    )

    source        : int | str                  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = __dearpypixl__.set_information(None, None)
    value         : list[float] | tuple[float] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : Item | int                 = 0,
        default_value      : list[float] | tuple[float] = (0.0, 0.0, 0.0, 0.0),
        parent             : Item | int                 = 13,
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


class FloatVectValue(WidgetItem):
    """Adds a float vect value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (list[float] | tuple[float], optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvFloatVectValue, "mvFloatVectValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_float_vect_value,
    )

    source        : int | str                  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float] = __dearpypixl__.set_information(None, None)
    value         : list[float] | tuple[float] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        label              : str                        = None,
        user_data          : Any                        = None,
        use_internal_label : bool                       = True,
        source             : Item | int                 = 0,
        default_value      : list[float] | tuple[float] = (),
        parent             : Item | int                 = 13,
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


class SeriesValue(WidgetItem):
    """Adds a plot series value.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * default_value (Any, optional): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvSeriesValue, "mvSeriesValue"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvValueRegistry,),
        able_children=(),
        command=dearpygui.add_series_value,
    )

    source        : int | str = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : Any       = __dearpypixl__.set_information(None, None)
    value         : Any       = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

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
