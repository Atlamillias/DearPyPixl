from typing import (
    Any,
    Callable,
    Union,
    Tuple,
    List,
)
import dearpygui.dearpygui
from pixle.itemtypes.container import Container
from pixle.itemtypes.widget import Widget

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "DrawLayer",
    "Drawlist",
    "ViewportDrawlist",
    "Arrow",
    "BezierCubic",
    "BezierQuadratic",
    "Circle",
    "Ellipse",
    "Image",
    "Line",
    "Polygon",
    "Polyline",
    "Quad",
    "Rectangle",
    "Text",
    "Triangle",
]


class DrawLayer(Container):
    """Creates a layer useful for grouping drawlist items.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_draw_layer

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            show=show,
            **kwargs,
        )
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show


class Drawlist(Container):
    """Adds a drawing canvas.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            width (int, optional): Width of the item.
            height (int, optional): Height of the item.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            callback (Callable, optional): Registers a callback.
            show (bool, optional): Attempt to render widget.
            pos (Union[List[int], Tuple[int]], optional): Places the item relative to window coordinates, [0,0] is top left.
            filter_key (str, optional): Used by filter widget.
            delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            tracked (bool, optional): Scroll tracking
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_drawlist

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        width: int = 0, 
        height: int = 0, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        callback: Callable = None, 
        show: bool = True, 
        pos: Union[List[int], Tuple[int]] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.width = width
        self.height = height
        self.parent = parent
        self.before = before
        self.callback = callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset


class ViewportDrawlist(Container):
    """A container that is used to present draw items or layers directly to the viewport. By default this will draw to the back of the viewport. Layers and draw items should be added to this widget as children.
    
    Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            show (bool, optional): Attempt to render widget.
            filter_key (str, optional): Used by filter widget.
            delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            front (bool, optional): Draws to the front of the view port instead of the back.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.add_viewport_drawlist

    def __init__(
        self, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        show: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        front: bool = True, 
        **kwargs, 
    ):
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
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.front = front


class Arrow(Widget):
    """Adds an arrow.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): Arrow tip.
            p2 (Union[List[float], Tuple[float]]): Arrow tail.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            size (int, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_arrow

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        size: int = 4, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.thickness = thickness
        self.size = size


class BezierCubic(Widget):
    """Adds a cubic bezier curve.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): First point in curve.
            p2 (Union[List[float], Tuple[float]]): Second point in curve.
            p3 (Union[List[float], Tuple[float]]): Third point in curve.
            p4 (Union[List[float], Tuple[float]]): Fourth point in curve.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            segments (int, optional): Number of segments to approximate bezier curve.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_bezier_cubic

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        p3: Union[List[float], Tuple[float, ...]], 
        p4: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        segments: int = 0, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.thickness = thickness
        self.segments = segments


class BezierQuadratic(Widget):
    """Adds a quadratic bezier curve.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): First point in curve.
            p2 (Union[List[float], Tuple[float]]): Second point in curve.
            p3 (Union[List[float], Tuple[float]]): Third point in curve.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            segments (int, optional): Number of segments to approximate bezier curve.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_bezier_quadratic

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        p3: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        segments: int = 0, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.thickness = thickness
        self.segments = segments


class Circle(Widget):
    """Adds a circle
    
    Args:
            center (Union[List[float], Tuple[float]]): 
            radius (float): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            fill (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            segments (int, optional): Number of segments to approximate circle.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_circle

    def __init__(
        self, 
        center: Union[List[float], Tuple[float, ...]], 
        radius: float, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        segments: int = 0, 
        **kwargs, 
    ):
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
        self.center = center
        self.radius = radius
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.fill = fill
        self.thickness = thickness
        self.segments = segments


class Ellipse(Widget):
    """Adds an ellipse.
    
    Args:
            pmin (Union[List[float], Tuple[float]]): Min point of bounding rectangle.
            pmax (Union[List[float], Tuple[float]]): Max point of bounding rectangle.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            fill (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            segments (int, optional): Number of segments to approximate bezier curve.
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_ellipse

    def __init__(
        self, 
        pmin: Union[List[float], Tuple[float, ...]], 
        pmax: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        segments: int = 32, 
        **kwargs, 
    ):
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
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.fill = fill
        self.thickness = thickness
        self.segments = segments


class Image(Widget):
    """Adds an image (for a drawing).
    
    Args:
            texture_id (Union[int, str]): 
            pmin (Union[List[float], Tuple[float]]): Point of to start drawing texture.
            pmax (Union[List[float], Tuple[float]]): Point to complete drawing texture.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            uv_min (Union[List[float], Tuple[float]], optional): Normalized coordinates on texture that will be drawn.
            uv_max (Union[List[float], Tuple[float]], optional): Normalized coordinates on texture that will be drawn.
            color (Union[List[int], Tuple[int]], optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_image

    def __init__(
        self, 
        texture_id: Union[int, str], 
        pmin: Union[List[float], Tuple[float, ...]], 
        pmax: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        uv_min: Union[List[float], Tuple[float]] = (0.0, 0.0), 
        uv_max: Union[List[float], Tuple[float]] = (1.0, 1.0), 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
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
        self.texture_id = texture_id
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.uv_min = uv_min
        self.uv_max = uv_max
        self.color = color


class Line(Widget):
    """Adds a line.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): Start of line.
            p2 (Union[List[float], Tuple[float]]): End of line.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_line

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.thickness = thickness


class Polygon(Widget):
    """Adds a polygon.
    
    Args:
            points (List[List[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            fill (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_polygon

    def __init__(
        self, 
        points: List[List[float]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.points = points
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.fill = fill
        self.thickness = thickness


class Polyline(Widget):
    """Adds a polyline.
    
    Args:
            points (List[List[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            closed (bool, optional): Will close the polyline by returning to the first point.
            color (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_polyline

    def __init__(
        self, 
        points: List[List[float]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        closed: bool = False, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.points = points
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.closed = closed
        self.color = color
        self.thickness = thickness


class Quad(Widget):
    """Adds a quad.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): 
            p2 (Union[List[float], Tuple[float]]): 
            p3 (Union[List[float], Tuple[float]]): 
            p4 (Union[List[float], Tuple[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            fill (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_quad

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        p3: Union[List[float], Tuple[float, ...]], 
        p4: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.fill = fill
        self.thickness = thickness


class Rectangle(Widget):
    """Adds a rectangle.
    
    Args:
            pmin (Union[List[float], Tuple[float]]): Min point of bounding rectangle.
            pmax (Union[List[float], Tuple[float]]): Max point of bounding rectangle.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            color_upper_left (Union[List[int], Tuple[int]], optional): 'multicolor' must be set to 'True'
            color_upper_right (Union[List[int], Tuple[int]], optional): 'multicolor' must be set to 'True'
            color_bottom_right (Union[List[int], Tuple[int]], optional): 'multicolor' must be set to 'True'
            color_bottom_left (Union[List[int], Tuple[int]], optional): 'multicolor' must be set to 'True'
            fill (Union[List[int], Tuple[int]], optional): 
            multicolor (bool, optional): 
            rounding (float, optional): Number of pixels of the radius that will round the corners of the rectangle. Note: doesn't work with multicolor
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_rectangle

    def __init__(
        self, 
        pmin: Union[List[float], Tuple[float, ...]], 
        pmax: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        color_upper_left: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        color_upper_right: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        color_bottom_right: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        color_bottom_left: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        multicolor: bool = False, 
        rounding: float = 0.0, 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.color_upper_left = color_upper_left
        self.color_upper_right = color_upper_right
        self.color_bottom_right = color_bottom_right
        self.color_bottom_left = color_bottom_left
        self.fill = fill
        self.multicolor = multicolor
        self.rounding = rounding
        self.thickness = thickness


class Text(Widget):
    """Adds text (drawlist).
    
    Args:
            pos (Union[List[float], Tuple[float]]): Top left point of bounding text rectangle.
            text (str): Text to draw.
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            size (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_text

    def __init__(
        self, 
        pos: Union[List[float], Tuple[float, ...]], 
        text: str, 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        size: float = 10.0, 
        **kwargs, 
    ):
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
        self.pos = pos
        self.text = text
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.size = size


class Triangle(Widget):
    """Adds a triangle.
    
    Args:
            p1 (Union[List[float], Tuple[float]]): 
            p2 (Union[List[float], Tuple[float]]): 
            p3 (Union[List[float], Tuple[float]]): 
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
            before (Union[int, str], optional): This item will be displayed before the specified item in the parent.
            show (bool, optional): Attempt to render widget.
            color (Union[List[int], Tuple[int]], optional): 
            fill (Union[List[int], Tuple[int]], optional): 
            thickness (float, optional): 
            id (Union[int, str], optional): (deprecated) 
    Returns:
            Union[int, str]
    
    """
    _command = dearpygui.dearpygui.draw_triangle

    def __init__(
        self, 
        p1: Union[List[float], Tuple[float, ...]], 
        p2: Union[List[float], Tuple[float, ...]], 
        p3: Union[List[float], Tuple[float, ...]], 
        label: str = None, 
        user_data: Any = None, 
        use_internal_label: bool = True, 
        parent: Union[int, str] = 0, 
        before: Union[int, str] = 0, 
        show: bool = True, 
        color: Union[List[int], Tuple[int]] = (255, 255, 255, 255), 
        fill: Union[List[int], Tuple[int]] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.label = label
        self.user_data = user_data
        self.use_internal_label = use_internal_label
        self.parent = parent
        self.before = before
        self.show = show
        self.color = color
        self.fill = fill
        self.thickness = thickness
