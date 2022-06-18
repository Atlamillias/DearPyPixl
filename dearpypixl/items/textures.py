from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "StaticTexture",
    "DynamicTexture",
    "RawTexture",
]


class StaticTexture(Widget):
    """Adds a static texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    width         : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = ItemProperty(INFORM, None, None)
    value         : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvStaticTexture, "mvStaticTexture")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvTextureRegistry)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_static_texture

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : int | str                        = 12,
        **kwargs
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class DynamicTexture(Widget):
    """Adds a dynamic texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    width         : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = ItemProperty(INFORM, None, None)
    value         : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvDynamicTexture, "mvDynamicTexture")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = True
    __able_parents__  : tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvTextureRegistry)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_dynamic_texture

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : int | str                        = 12,
        **kwargs
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            **kwargs,
        )


class RawTexture(Widget):
    """Adds a raw texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item.
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * format (int, optional): Data format.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
    """
    width         : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = ItemProperty(INFORM, None, None)
    format        : int                             = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    value         : list[float] | tuple[float, ...] = ItemProperty(CONFIG, "get_item_value", "set_item_value")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvRawTexture, "mvRawTexture")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvTextureRegistry)
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvRawTexture', 'mvFormat_Float_rgba', 'mvFormat_Float_rgb')
    __command__       : Callable   = dearpygui.add_raw_texture

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        format            : int                              = 0,
        parent            : int | str                        = 12,
        **kwargs
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            format=format,
            parent=parent,
            **kwargs,
        )
