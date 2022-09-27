from typing import Callable, Any, TypeAlias
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "Drawlist",
    "DrawLine",
    "DrawArrow",
    "DrawTriangle",
    "DrawCircle",
    "DrawEllipse",
    "DrawBezierCubic",
    "DrawBezierQuadratic",
    "DrawQuad",
    "DrawRect",
    "DrawText",
    "DrawPolygon",
    "DrawPolyline",
    "DrawImage",
    "DrawLayer",
    "ViewportDrawlist",
    "DrawImageQuad",
    "DrawNode",
]

Coordinate  : TypeAlias = int | float
XYCoordinate: TypeAlias = tuple[Coordinate, Coordinate] | list[Coordinate]

class Drawlist(WidgetItem):
    """Adds a drawing canvas.

        Args:
            * width (int):
            * height (int):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawlist, "mvDrawlist"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvDrawLayer, dearpygui.mvDrawLine, dearpygui.mvDrawArrow, dearpygui.mvDrawTriangle, dearpygui.mvDrawCircle, dearpygui.mvDrawEllipse, dearpygui.mvDrawBezierCubic, dearpygui.mvDrawBezierQuadratic, dearpygui.mvDrawQuad, dearpygui.mvDrawRect, dearpygui.mvDrawText, dearpygui.mvDrawPolygon, dearpygui.mvDrawPolyline, dearpygui.mvDrawImageQuad, dearpygui.mvDrawImage,dearpygui.mvDrawNode),
        command=dearpygui.add_drawlist,
    )

    width        : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    height       : int                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    callback     : Callable                    = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show         : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pos          : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_state", "set_item_config")
    filter_key   : str                         = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool                        = __dearpypixl__.set_information(None, None)
    tracked      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    track_offset : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

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

    def __init__(
        self,
        width             : int,
        height            : int,
        label             : str                               = None,
        user_data         : Any                               = None,
        use_internal_label: bool                              = True,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        callback          : Callable                          = None,
        show              : bool                              = True,
        pos               : list[int] | tuple[int, ...] = [],
        filter_key        : str                               = '',
        delay_search      : bool                              = False,
        tracked           : bool                              = False,
        track_offset      : float                             = 0.5,
        **kwargs
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            callback=callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            **kwargs,
        )


class DrawLine(WidgetItem):
    """Adds a line.

        Args:
            * p1 (list[float] | tuple[float, ...]): Start of line.
            * p2 (list[float] | tuple[float, ...]): End of line.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawLine, "mvDrawLine"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_line,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        thickness         : float                            = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            **kwargs,
        )


class DrawArrow(WidgetItem):
    """Adds an arrow.

        Args:
            * p1 (list[float] | tuple[float, ...]): Origin position (arrow tip).
            * p2 (list[float] | tuple[float, ...]): End position (arrow tail).
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * size (int, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawArrow, "mvDrawArrow"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode, dearpygui.mvViewportDrawlist,dearpygui.mvTemplateRegistry),
        able_children=(),
        command=dearpygui.draw_arrow,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    size      : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        label             : str                            = None,
        user_data         : Any                            = None,
        use_internal_label: bool                           = True,
        parent            : Item | int                     = 0,
        before            : Item | int                     = 0,
        show              : bool                           = True,
        color             : list[int] | tuple[int, ...]    = (255, 255, 255, 255),
        thickness         : float                          = 1.0,
        size              : int                            = 4,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            size=size,
            **kwargs,
        )


class DrawTriangle(WidgetItem):
    """Adds a triangle.

        Args:
            * p1 (list[float] | tuple[float, ...]):
            * p2 (list[float] | tuple[float, ...]):
            * p3 (list[float] | tuple[float, ...]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * fill (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawTriangle, "mvDrawTriangle"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvDrawNode, dearpygui.mvWindowAppItem, dearpygui.mvPlot,dearpygui.mvViewportDrawlist),
        able_children=(),
        constants=('mvDrawTriangle', 'mvCullMode_None', 'mvCullMode_Back', 'mvCullMode_Front'),
        command=dearpygui.draw_triangle,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p3        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill      : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        p3                : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...]      = (0, 0, 0, -255),
        thickness         : float                            = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawCircle(WidgetItem):
    """Adds a circle

        Args:
            * center (list[float] | tuple[float, ...]):
            * radius (float):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * fill (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * segments (int, optional): Number of segments to approximate circle.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawCircle, "mvDrawCircle"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_circle,
    )

    center    : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    radius    : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill      : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    segments  : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        center            : list[float] | tuple[float, ...],
        radius            : float,
        label             : str                              = None                ,
        user_data         : Any                              = None                ,
        use_internal_label: bool                             = True                ,
        parent            : Item | int                       = 0                   ,
        before            : Item | int                       = 0                   ,
        show              : bool                             = True                ,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...]      = (0, 0, 0, -255)     ,
        thickness         : float                            = 1.0                 ,
        segments          : int                              = 0                   ,
        **kwargs
    ) -> None:
        super().__init__(
            center=center,
            radius=radius,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawEllipse(WidgetItem):
    """Adds an ellipse.

        Args:
            * pmin (list[float] | tuple[float, ...]): Min point of bounding rectangle.
            * pmax (list[float] | tuple[float, ...]): Max point of bounding rectangle.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * fill (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * segments (int, optional): Number of segments to approximate bezier curve.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawEllipse, "mvDrawEllipse"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_ellipse,
    )

    pmin      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pmax      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill      : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    segments  : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        pmin              : list[float] | tuple[float, ...],
        pmax              : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...]      = (0, 0, 0, -255),
        thickness         : float                            = 1.0,
        segments          : int                              = 32,
        **kwargs
    ) -> None:
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawBezierCubic(WidgetItem):
    """Adds a cubic bezier curve.

        Args:
            * p1 (list[float] | tuple[float, ...]): First point in curve.
            * p2 (list[float] | tuple[float, ...]): Second point in curve.
            * p3 (list[float] | tuple[float, ...]): Third point in curve.
            * p4 (list[float] | tuple[float, ...]): Fourth point in curve.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * segments (int, optional): Number of segments to approximate bezier curve.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawBezierCubic, "mvDrawBezierCubic"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvStage, dearpygui.mvTemplateRegistry, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_bezier_cubic,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p3        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p4        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    segments  : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        p3                : list[float] | tuple[float, ...],
        p4                : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        thickness         : float                            = 1.0,
        segments          : int                              = 0,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawBezierQuadratic(WidgetItem):
    """Adds a quadratic bezier curve.

        Args:
            * p1 (list[float] | tuple[float, ...]): First point in curve.
            * p2 (list[float] | tuple[float, ...]): Second point in curve.
            * p3 (list[float] | tuple[float, ...]): Third point in curve.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
            * segments (int, optional): Number of segments to approximate bezier curve.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawBezierQuadratic, "mvDrawBezierQuadratic"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_bezier_quadratic,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p3        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    segments  : int                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        p3                : list[float] | tuple[float, ...],
        label             : str                              = None                ,
        user_data         : Any                              = None                ,
        use_internal_label: bool                             = True                ,
        parent            : Item | int                       = 0                   ,
        before            : Item | int                       = 0                   ,
        show              : bool                             = True                ,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        thickness         : float                            = 1.0                 ,
        segments          : int                              = 0                   ,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )


class DrawQuad(WidgetItem):
    """Adds a quad.

        Args:
            * p1 (list[float] | tuple[float, ...]):
            * p2 (list[float] | tuple[float, ...]):
            * p3 (list[float] | tuple[float, ...]):
            * p4 (list[float] | tuple[float, ...]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * fill (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawQuad, "mvDrawQuad"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_quad,
    )

    p1        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p3        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p4        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill      : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        p3                : list[float] | tuple[float, ...],
        p4                : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...]      = (0, 0, 0, -255),
        thickness         : float                            = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawRect(WidgetItem):
    """Adds a rectangle.

        Args:
            * pmin (list[float] | tuple[float, ...]): Min point of bounding rectangle.
            * pmax (list[float] | tuple[float, ...]): Max point of bounding rectangle.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * color_upper_left (list[int] | tuple[int, ...], optional): 'multicolor' must be set to 'True'
            * color_upper_right (list[int] | tuple[int, ...], optional): 'multicolor' must be set to 'True'
            * color_bottom_right (list[int] | tuple[int, ...], optional): 'multicolor' must be set to 'True'
            * color_bottom_left (list[int] | tuple[int, ...], optional): 'multicolor' must be set to 'True'
            * fill (list[int] | tuple[int, ...], optional):
            * multicolor (bool, optional):
            * rounding (float, optional): Number of pixels of the radius that will round the corners of the rectangle. Note: doesn't work with multicolor
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawRect, "mvDrawRect"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_rectangle,
    )

    pmin               : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pmax               : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show               : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color              : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color_upper_left   : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color_upper_right  : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color_bottom_right : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color_bottom_left  : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill               : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    multicolor         : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    rounding           : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness          : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        pmin              : list[float] | tuple[float, ...],
        pmax              : list[float] | tuple[float, ...],
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        parent            : Item | int                      = 0,
        before            : Item | int                      = 0,
        show              : bool                            = True,
        color             : list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        color_upper_left  : list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        color_upper_right : list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        color_bottom_right: list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        color_bottom_left : list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...]     = (0, 0, 0, -255),
        multicolor        : bool                            = False,
        rounding          : float                           = 0.0,
        thickness         : float                           = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            color_upper_left=color_upper_left,
            color_upper_right=color_upper_right,
            color_bottom_right=color_bottom_right,
            color_bottom_left=color_bottom_left,
            fill=fill,
            multicolor=multicolor,
            rounding=rounding,
            thickness=thickness,
            **kwargs,
        )


class DrawText(WidgetItem):
    """Adds text (drawlist).

        Args:
            * pos (list[float] | tuple[float, ...]): Top left point of bounding text rectangle.
            * text (str): Text to draw.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * size (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawText, "mvDrawText"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_text,
    )

    pos   : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_state" , "set_item_config")
    text  : str                             = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show  : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    size  : float                           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        pos               : list[float] | tuple[float, ...],
        text              : str,
        label             : str                             = None,
        user_data         : Any                             = None,
        use_internal_label: bool                            = True,
        parent            : Item | int                      = 0,
        before            : Item | int                      = 0,
        show              : bool                            = True,
        color             : list[int] | tuple[int, ...]     = (255, 255, 255, 255),
        size              : float                           = 10.0,
        **kwargs
    ) -> None:
        super().__init__(
            pos=pos,
            text=text,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            size=size,
            **kwargs,
        )


class DrawPolygon(WidgetItem):
    """Adds a polygon.

        Args:
            * points (list[list[float]]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * color (list[int] | tuple[int, ...], optional):
            * fill (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawPolygon, "mvDrawPolygon"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_polygon,
    )

    points    : list[list[float]]           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    fill      : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        points            : list[list[float]],
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        show              : bool                        = True,
        color             : list[int] | tuple[int, ...] = (255, 255, 255, 255),
        fill              : list[int] | tuple[int, ...] = (0, 0, 0, -255),
        thickness         : float                       = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            points=points,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )


class DrawPolyline(WidgetItem):
    """Adds a polyline.

        Args:
            * points (list[list[float]]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * closed (bool, optional): Will close the polyline by returning to the first point.
            * color (list[int] | tuple[int, ...], optional):
            * thickness (float, optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawPolyline, "mvDrawPolyline"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_polyline,
    )

    points    : list[list[float]]           = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show      : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    closed    : bool                        = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color     : list[int] | tuple[int, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    thickness : float                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        points            : list[list[float]],
        label             : str                         = None,
        user_data         : Any                         = None,
        use_internal_label: bool                        = True,
        parent            : Item | int                  = 0,
        before            : Item | int                  = 0,
        show              : bool                        = True,
        closed            : bool                        = False,
        color             : list[int] | tuple[int, ...] = (255, 255, 255, 255),
        thickness         : float                       = 1.0,
        **kwargs
    ) -> None:
        super().__init__(
            points=points,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            closed=closed,
            color=color,
            thickness=thickness,
            **kwargs,
        )


class DrawImage(WidgetItem):
    """Adds an image (for a drawing).

        Args:
            * texture_tag (int | str):
            * pmin (list[float] | tuple[float, ...]): Point of to start drawing texture.
            * pmax (list[float] | tuple[float, ...]): Point to complete drawing texture.
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * uv_min (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * uv_max (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * color (list[int] | tuple[int, ...], optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawImage, "mvDrawImage"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_image,
    )

    texture_tag : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pmin        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    pmax        : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show        : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_min      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv_max      : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color       : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        texture_tag       : int | str,
        pmin              : list[float] | tuple[float, ...],
        pmax              : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        uv_min            : list[float] | tuple[float, ...]  = (0.0, 0.0),
        uv_max            : list[float] | tuple[float, ...]  = (1.0, 1.0),
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        **kwargs
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            pmin=pmin,
            pmax=pmax,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            uv_min=uv_min,
            uv_max=uv_max,
            color=color,
            **kwargs,
        )


class DrawLayer(WidgetItem):
    """New in 1.1. Creates a layer useful for grouping drawlist items.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * perspective_divide (bool, optional): New in 1.1. apply perspective divide
            * depth_clipping (bool, optional): New in 1.1. apply depth clipping
            * cull_mode (int, optional): New in 1.1. culling mode, mvCullMode_* constants. Only works with triangles currently.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawLayer, "mvDrawLayer"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvWindowAppItem, dearpygui.mvPlot,dearpygui.mvViewportDrawlist),
        able_children=(dearpygui.mvDrawLine, dearpygui.mvDrawArrow, dearpygui.mvDrawTriangle, dearpygui.mvDrawCircle, dearpygui.mvDrawEllipse, dearpygui.mvDrawBezierCubic, dearpygui.mvDrawBezierQuadratic, dearpygui.mvDrawQuad, dearpygui.mvDrawRect, dearpygui.mvDrawText, dearpygui.mvDrawPolygon, dearpygui.mvDrawPolyline, dearpygui.mvDrawImage, dearpygui.mvDrawImageQuad,dearpygui.mvDrawNode),
        commands=('set_clip_space',),
        command=dearpygui.add_draw_layer,
    )

    show               : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    perspective_divide : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    depth_clipping     : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    cull_mode          : int  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        perspective_divide : bool      = False,
        depth_clipping     : bool      = False,
        cull_mode          : int       = 0,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            perspective_divide=perspective_divide,
            depth_clipping=depth_clipping,
            cull_mode=cull_mode,
            **kwargs,
        )


class ViewportDrawlist(WidgetItem):
    """A container that is used to present draw items or layers directly to the viewport. By default this will draw to the back of the viewport. Layers and draw items should be added to this widget as children.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * front (bool, optional): Draws to the front of the view port instead of the back.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvViewportDrawlist, "mvViewportDrawlist"),
        is_container=True,
        is_root_item=True,
        is_value_able=False,
        able_parents=(),
        able_children=(dearpygui.mvDrawLine, dearpygui.mvDrawLayer, dearpygui.mvDrawArrow, dearpygui.mvDrawTriangle, dearpygui.mvDrawCircle, dearpygui.mvDrawEllipse, dearpygui.mvDrawBezierCubic, dearpygui.mvDrawBezierQuadratic, dearpygui.mvDrawQuad, dearpygui.mvDrawRect, dearpygui.mvDrawText, dearpygui.mvDrawPolygon, dearpygui.mvDrawPolyline, dearpygui.mvDrawImage, dearpygui.mvDrawImageQuad,dearpygui.mvDrawNode),
        command=dearpygui.add_viewport_drawlist,
    )

    show         : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    filter_key   : str  = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    delay_search : bool = __dearpypixl__.set_information(None, None)
    front        : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label              : str  = None,
        user_data          : Any  = None,
        use_internal_label : bool = True,
        show               : bool = True,
        filter_key         : str  = '',
        delay_search       : bool = False,
        front              : bool = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            front=front,
            **kwargs,
        )


class DrawImageQuad(WidgetItem):
    """Adds an image (for a drawing).

        Args:
            * texture_tag (int | str):
            * p1 (list[float] | tuple[float, ...]):
            * p2 (list[float] | tuple[float, ...]):
            * p3 (list[float] | tuple[float, ...]):
            * p4 (list[float] | tuple[float, ...]):
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
            * uv1 (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * uv2 (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * uv3 (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * uv4 (list[float] | tuple[float, ...], optional): Normalized coordinates on texture that will be drawn.
            * color (list[int] | tuple[int, ...], optional):
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawImageQuad, "mvDrawImageQuad"),
        is_container=False,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvDrawNode,dearpygui.mvViewportDrawlist),
        able_children=(),
        command=dearpygui.draw_image_quad,
    )

    texture_tag : int | str                       = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p1          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p2          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p3          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    p4          : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    show        : bool                            = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv1         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv2         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv3         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    uv4         : list[float] | tuple[float, ...] = __dearpypixl__.set_configuration("get_item_config", "set_item_config")
    color       : list[int] | tuple[int, ...]     = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        texture_tag       : int | str,
        p1                : list[float] | tuple[float, ...],
        p2                : list[float] | tuple[float, ...],
        p3                : list[float] | tuple[float, ...],
        p4                : list[float] | tuple[float, ...],
        label             : str                              = None,
        user_data         : Any                              = None,
        use_internal_label: bool                             = True,
        parent            : Item | int                       = 0,
        before            : Item | int                       = 0,
        show              : bool                             = True,
        uv1               : list[float] | tuple[float, ...]  = (0.0, 0.0),
        uv2               : list[float] | tuple[float, ...]  = (1.0, 0.0),
        uv3               : list[float] | tuple[float, ...]  = (1.0, 1.0),
        uv4               : list[float] | tuple[float, ...]  = (0.0, 1.0),
        color             : list[int] | tuple[int, ...]      = (255, 255, 255, 255),
        **kwargs
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            uv1=uv1,
            uv2=uv2,
            uv3=uv3,
            uv4=uv4,
            color=color,
            **kwargs,
        )


class DrawNode(WidgetItem):
    """New in 1.1. Creates a drawing node to associate a transformation matrix. Child node matricies will concatenate.

        Args:
            * label (str, optional): Display name for the item. Defaults to None.
            * user_data (Any, optional): Passed as the third positional argument to related callbacks.
            Defaults to None.
            * use_internal_label (bool, optional): If True, `##{self.tag}` will be appended to the
            item's <label> (this is hidden whenever the label would be displayed in the UI). Defaults
            to True.
            * parent (Item | int, optional): Item (or an item's tag) that will parent this item. If 0,
            the item on top of the container stack will parent the item. Defaults to 0.
            * before (Item | int, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): If False, the item will not be rendered. Defaults to True.
    """
    __slots__ = ()
    __dearpypixl__ = ItemData(
        identity=(dearpygui.mvDrawNode, "mvDrawNode"),
        is_container=True,
        is_root_item=False,
        is_value_able=False,
        able_parents=(dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvDrawlist, dearpygui.mvDrawLayer, dearpygui.mvWindowAppItem, dearpygui.mvPlot, dearpygui.mvViewportDrawlist,dearpygui.mvDrawNode),
        able_children=(dearpygui.mvDrawLine, dearpygui.mvDrawArrow, dearpygui.mvDrawTriangle, dearpygui.mvDrawCircle, dearpygui.mvDrawEllipse, dearpygui.mvDrawBezierCubic, dearpygui.mvDrawBezierQuadratic, dearpygui.mvDrawQuad, dearpygui.mvDrawRect, dearpygui.mvDrawText, dearpygui.mvDrawPolygon, dearpygui.mvDrawPolyline, dearpygui.mvDrawImage, dearpygui.mvDrawNode,dearpygui.mvDrawImageQuad),
        commands=('apply_transform', 'create_rotation_matrix', 'create_translation_matrix', 'create_scale_matrix', 'create_lookat_matrix', 'create_perspective_matrix', 'create_orthographic_matrix', 'create_fps_matrix'),
        command=dearpygui.add_draw_node,
    )

    show : bool = __dearpypixl__.set_configuration("get_item_config", "set_item_config")

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            **kwargs,
        )
