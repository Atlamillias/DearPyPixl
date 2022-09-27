from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *
from dearpypixl._internal import registry


__all__ = [
    "StaticTexture",
    "DynamicTexture",
    "RawTexture",

    "Image",
    "ImageButton",
]



class TextureItem(WidgetItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(internal_only=True)




class StaticTexture(TextureItem):
    """Adds a static texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvStaticTexture, "mvStaticTexture"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvTextureRegistry),
        able_children=(),
        command=dearpygui.add_static_texture,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = __dearpypixl__.set_information(None, None)
    value         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 12,
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


class DynamicTexture(TextureItem):
    """Adds a dynamic texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDynamicTexture, "mvDynamicTexture"),
        is_container=False,
        is_root_item=False,
        is_value_able=True,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvTextureRegistry),
        able_children=(),
        command=dearpygui.add_dynamic_texture,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = __dearpypixl__.set_information(None, None)
    value         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 12,
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


class RawTexture(TextureItem):
    """Adds a raw texture.

        Args:
            * width (int):
            * height (int):
            * default_value (list[float] | tuple[float, ...]): Initial starting value for the item. The value type and
            the effects the value has on an item varies between item types.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * format (int, optional): Data format.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvRawTexture, "mvRawTexture"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry,dearpygui.mvTextureRegistry),
        able_children=(),
        constants=('mvRawTexture', 'mvFormat_Float_rgba', 'mvFormat_Float_rgb'),
        command=dearpygui.add_raw_texture,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    default_value : list[float] | tuple[float, ...] = __dearpypixl__.set_information(None, None)
    format        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    value         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_value", "set_item_value")

    def __init__(
        self,
        width             : int,
        height            : int,
        default_value     : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        format            : int                              = 0,
        parent            : Item | int                       = 12,
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


class Image(WidgetItem):
    """Adds an image from a specified texture. uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using range (0.0,0.0)->(1.0,1.0) for texture coordinates will generally display the entire texture.

        Args:
            * texture_tag (int | str): The texture_tag should come from a texture that was added to a texture registry.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * source (Item | int, optional): A value-able item or tag. This item will directly
            reference/modify the value of the reference as if it were its own value. Defaults to 0.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * tint_color (list[float] | tuple[float, ...], optional): Applies a color tint to the entire texture.
            * border_color (list[float] | tuple[float, ...], optional): Displays a border of the specified color around the texture. If the theme style has turned off the border it will not be shown.
            * uv_min (list[float] | tuple[float, ...], optional): Normalized texture coordinates min point.
            * uv_max (list[float] | tuple[float, ...], optional): Normalized texture coordinates max point.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvImage, "mvImage"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_image,
    )

    width         : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent        : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source        : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type  : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key    : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked       : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset  : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tint_color    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    border_color  : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_min        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_max        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(
        self,
        texture_item      : TextureItem | int,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        height            : int                             = 0,
        indent            : int                             = -1,
        parent            : Item | int                      = 0,
        before            : Item | int                      = 0,
        source            : Item | int                      = 0,
        payload_type      : str                             = '$$DPG_PAYLOAD',
        drag_callback     : Callable                        = None,
        drop_callback     : Callable                        = None,
        show              : bool                            = True,
        pos               : list[int] | tuple[int, ...]     = [],
        filter_key        : str                             = '',
        tracked           : bool                            = False,
        track_offset      : float                           = 0.5,
        tint_color        : list[float] | tuple[float, ...] = (255, 255, 255, 255),
        border_color      : list[float] | tuple[float, ...] = (0, 0, 0, 0),
        uv_min            : list[float] | tuple[float, ...] = (0.0, 0.0),
        uv_max            : list[float] | tuple[float, ...] = (1.0, 1.0),
        **kwargs
    ) -> None:
        super().__init__(
            texture_item=texture_item,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            tint_color=tint_color,
            border_color=border_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )

    @property
    @__dearpypixl__.as_configuration
    def texture_item(self) -> TextureItem:
        texture_uuid = dearpygui.get_item_configuration(self.tag)["texture_tag"]
        return registry.get_item(texture_uuid)


class ImageButton(WidgetItem):
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvImageButton, "mvImageButton"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(),
        command=dearpygui.add_image_button,
    )

    width            : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height           : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    indent           : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    source           : ItemT                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    payload_type     : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drag_callback    : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    drop_callback    : Callable                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show             : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos              : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    filter_key       : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tracked          : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset     : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    frame_padding    : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    tint_color       : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    background_color : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    border_color     : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_min           : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_max           : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    is_resized           : bool           = __dearpypixl__.set_state("get_item_state", None, target="resized")
    is_middle_clicked    : bool           = __dearpypixl__.set_state("get_item_state", None, target="middle_clicked")
    is_right_clicked     : bool           = __dearpypixl__.set_state("get_item_state", None, target="right_clicked")
    is_left_clicked      : bool           = __dearpypixl__.set_state("get_item_state", None, target="left_clicked")
    is_hovered           : bool           = __dearpypixl__.set_state("get_item_state", None, target="hovered")
    is_active            : bool           = __dearpypixl__.set_state("get_item_state", None, target="active")
    is_focused           : bool           = __dearpypixl__.set_state("get_item_state", None, target="focused")
    is_clicked           : bool           = __dearpypixl__.set_state("get_item_state", None, target="clicked")
    is_visible           : bool           = __dearpypixl__.set_state("get_item_state", None, target="visible")
    is_activated         : bool           = __dearpypixl__.set_state("get_item_state", None, target="activated")
    is_deactivated       : bool           = __dearpypixl__.set_state("get_item_state", None, target="deactivated")
    rect_min             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_min")
    rect_max             : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_max")
    rect_size            : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="rect_size")
    content_region_avail : list[int, int] = __dearpypixl__.set_state("get_item_state", None, target="content_region_avail")

    def __init__(self,
        texture_tag       : ItemT,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        width             : int                             = 0,
        height            : int                             = 0,
        indent            : int                             = -1,
        parent            : ItemT                           = 0,
        before            : ItemT                           = 0,
        source            : ItemT                           = 0,
        payload_type      : str                             = '$$DPG_PAYLOAD',
        callback          : Callable                        = None,
        drag_callback     : Callable                        = None,
        drop_callback     : Callable                        = None,
        show              : bool                            = True,
        enabled           : bool                            = True,
        pos               : list[int] | tuple[int, ...]     = [],
        filter_key        : str                             = '',
        tracked           : bool                            = False,
        track_offset      : float                           = 0.5,
        frame_padding     : int                             = -1,
        tint_color        : list[float] | tuple[float, ...] = (255, 255, 255, 255),
        background_color  : list[float] | tuple[float, ...] = (0, 0, 0, 0),
        uv_min            : tuple[float, float] = (0.0, 0.0),
        uv_max            : tuple[float, float] = (1.0, 1.0),
        **kwargs
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            frame_padding=frame_padding,
            tint_color=tint_color,
            background_color=background_color,
            uv_min=uv_min,
            uv_max=uv_max,
            **kwargs,
        )

    @property
    @__dearpypixl__.as_configuration
    def texture_item(self) -> TextureItem:
        texture_uuid = dearpygui.get_item_configuration(self.tag)["texture_tag"]
        return registry.get_item(texture_uuid)
