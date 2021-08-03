from typing import Any, Callable
import dearpygui.dearpygui
from dpgwidgets.widget import Container, Widget

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
    """Creates a layer that can be drawn to. Useful for grouping drawing items.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_draw_layer

    def __init__(
        self, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data


class Drawlist(Container):
    """A container widget that is used to present draw items or layers. Layers and draw items should be added to this widget as children.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **width (int): Width of the item.
            **height (int): Height of the item.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **payload_type (str): Sender string type must be the same as the target for the target to run the payload_callback.
            **callback (Callable): Registers a callback.
            **drag_callback (Callable): Registers a drag callback for drag and drop.
            **drop_callback (Callable): Registers a drop callback for drag and drop.
            **show (bool): Attempt to render widget.
            **pos (List[int]): Places the item relative to window coordinates, [0,0] is top left.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **tracked (bool): Scroll tracking
            **track_offset (float): 0.0f:top, 0.5f:center, 1.0f:bottom
            **user_data (Any): User data for callbacks.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_drawlist

    def __init__(
        self, 
        label: str = None, 
        width: int = 0, 
        height: int = 0, 
        parent: int = 0, 
        before: int = 0, 
        payload_type: str = '$$DPG_PAYLOAD', 
        callback: Callable = None, 
        drag_callback: Callable = None, 
        drop_callback: Callable = None, 
        show: bool = True, 
        pos: list[int] = [], 
        filter_key: str = '', 
        delay_search: bool = False, 
        tracked: bool = False, 
        track_offset: float = 0.5, 
        user_data: Any = None, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            user_data=user_data,
            **kwargs,
        )
        self.label = label
        self.width = width
        self.height = height
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.user_data = user_data


class ViewportDrawlist(Container):
    """A container that is used to present draw items or layers directly to the viewport. By default this will draw to the back of teh viewport. Layers and draw items should be added to this widget as children.
    Args:
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **show (bool): Attempt to render widget.
            **filter_key (str): Used by filter widget.
            **delay_search (bool): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            **user_data (Any): User data for callbacks.
            **front (bool): Draws to the front of the view port instead of the back.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.add_viewport_drawlist

    def __init__(
        self, 
        label: str = None, 
        show: bool = True, 
        filter_key: str = '', 
        delay_search: bool = False, 
        user_data: Any = None, 
        front: bool = True, 
        **kwargs, 
    ):
        super().__init__(
            label=label,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            user_data=user_data,
            front=front,
            **kwargs,
        )
        self.label = label
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.user_data = user_data
        self.front = front


class Arrow(Widget):
    """Draws an arrow on a drawing.
    Args:
            p1 (List[float]): Arrow tip.
            p2 (List[float]): Arrow tail.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **thickness (float): 
            **size (int): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_arrow

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        size: int = 4, 
        **kwargs, 
    ):
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            thickness=thickness,
            size=size,
            **kwargs,
        )
        self.p1 = p1
        self.p2 = p2
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.thickness = thickness
        self.size = size


class BezierCubic(Widget):
    """Draws a cubic bezier curve on a drawing.
    Args:
            p1 (List[float]): First point in curve.
            p2 (List[float]): Second point in curve.
            p3 (List[float]): Third point in curve.
            p4 (List[float]): Fourth point in curve.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **thickness (float): 
            **segments (int): Number of segments to approximate bezier curve.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_bezier_cubic

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        p3: list[float], 
        p4: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
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
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
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
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.thickness = thickness
        self.segments = segments


class BezierQuadratic(Widget):
    """Draws a quadratic bezier curve on a drawing.
    Args:
            p1 (List[float]): First point in curve.
            p2 (List[float]): Second point in curve.
            p3 (List[float]): Third point in curve.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **thickness (float): 
            **segments (int): Number of segments to approximate bezier curve.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_bezier_quadratic

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        p3: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        segments: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.thickness = thickness
        self.segments = segments


class Circle(Widget):
    """Draws a circle on a drawing.
    Args:
            center (List[float]): 
            radius (float): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **thickness (float): 
            **segments (int): Number of segments to approximate circle.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_circle

    def __init__(
        self, 
        center: list[float], 
        radius: float, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        segments: int = 0, 
        **kwargs, 
    ):
        super().__init__(
            center=center,
            radius=radius,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )
        self.center = center
        self.radius = radius
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.thickness = thickness
        self.segments = segments


class Ellipse(Widget):
    """Draws an ellipse on a drawing.
    Args:
            pmin (List[float]): Min point of bounding rectangle.
            pmax (List[float]): Max point of bounding rectangle.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **thickness (float): 
            **segments (int): Number of segments to approximate bezier curve.
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_ellipse

    def __init__(
        self, 
        pmin: list[float], 
        pmax: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        segments: int = 32, 
        **kwargs, 
    ):
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            fill=fill,
            thickness=thickness,
            segments=segments,
            **kwargs,
        )
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.thickness = thickness
        self.segments = segments


class Image(Widget):
    """Draws an image on a drawing. p_min (top-left) and p_max (bottom-right) represent corners of the rectangle the image will be drawn to.Setting the p_min equal to the p_max will sraw the image to with 1:1 scale.uv_min and uv_max represent the normalized texture coordinates of the original image that will be shown. Using (0.0,0.0)->(1.0,1.0) texturecoordinates will generally display the entire texture.
    Args:
            texture_id (int): 
            pmin (List[float]): Point of to start drawing texture.
            pmax (List[float]): Point to complete drawing texture.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **uv_min (List[float]): Normalized coordinates on texture that will be drawn.
            **uv_max (List[float]): Normalized coordinates on texture that will be drawn.
            **color (List[int]): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_image

    def __init__(
        self, 
        texture_id: int, 
        pmin: list[float], 
        pmax: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        uv_min: list[float] = (0.0, 0.0), 
        uv_max: list[float] = (1.0, 1.0), 
        color: list[int] = (255, 255, 255, 255), 
        **kwargs, 
    ):
        super().__init__(
            texture_id=texture_id,
            pmin=pmin,
            pmax=pmax,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            uv_min=uv_min,
            uv_max=uv_max,
            color=color,
            **kwargs,
        )
        self.texture_id = texture_id
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.uv_min = uv_min
        self.uv_max = uv_max
        self.color = color


class Line(Widget):
    """Draws a line on a drawing.
    Args:
            p1 (List[float]): Start of line.
            p2 (List[float]): End of line.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_line

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            p1=p1,
            p2=p2,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            thickness=thickness,
            **kwargs,
        )
        self.p1 = p1
        self.p2 = p2
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.thickness = thickness


class Polygon(Widget):
    """Draws a polygon on a drawing. First and and last point should be the same to close teh polygone.
    Args:
            points (List[List[float]]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_polygon

    def __init__(
        self, 
        points: list[list[float]], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            points=points,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )
        self.points = points
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.thickness = thickness


class Polyline(Widget):
    """Draws connected lines on a drawing from points.
    Args:
            points (List[List[float]]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **closed (bool): Will close the polyline by returning to the first point.
            **color (List[int]): 
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_polyline

    def __init__(
        self, 
        points: list[list[float]], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        closed: bool = False, 
        color: list[int] = (255, 255, 255, 255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            points=points,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            closed=closed,
            color=color,
            thickness=thickness,
            **kwargs,
        )
        self.points = points
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.closed = closed
        self.color = color
        self.thickness = thickness


class Quad(Widget):
    """Draws a quad on a drawing.
    Args:
            p1 (List[float]): 
            p2 (List[float]): 
            p3 (List[float]): 
            p4 (List[float]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_quad

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        p3: list[float], 
        p4: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            p4=p4,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
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
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.thickness = thickness


class Rectangle(Widget):
    """Draws a rectangle on a drawing.
    Args:
            pmin (List[float]): Min point of bounding rectangle.
            pmax (List[float]): Max point of bounding rectangle.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **rounding (float): Number of pixels of the radius that will round the corners of the rectangle.
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_rectangle

    def __init__(
        self, 
        pmin: list[float], 
        pmax: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        rounding: float = 0.0, 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            pmin=pmin,
            pmax=pmax,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            fill=fill,
            rounding=rounding,
            thickness=thickness,
            **kwargs,
        )
        self.pmin = pmin
        self.pmax = pmax
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.rounding = rounding
        self.thickness = thickness


class Text(Widget):
    """Draws a text on a drawing.
    Args:
            pos (List[float]): Top left point of bounding text rectangle.
            text (str): Text to draw.
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **size (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_text

    def __init__(
        self, 
        pos: list[float], 
        text: str, 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        size: float = 10.0, 
        **kwargs, 
    ):
        super().__init__(
            pos=pos,
            text=text,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            size=size,
            **kwargs,
        )
        self.pos = pos
        self.text = text
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.size = size


class Triangle(Widget):
    """Draws a triangle on a drawing.
    Args:
            p1 (List[float]): 
            p2 (List[float]): 
            p3 (List[float]): 
            **label (str): Overrides 'name' as label.
            **id (int): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            **parent (int): Parent to add this item to. (runtime adding)
            **before (int): This item will be displayed before the specified item in the parent.
            **show (bool): Attempt to render widget.
            **user_data (Any): User data for callbacks.
            **color (List[int]): 
            **fill (List[int]): 
            **thickness (float): 
    Returns:
            int
    
    """
    _command = dearpygui.dearpygui.draw_triangle

    def __init__(
        self, 
        p1: list[float], 
        p2: list[float], 
        p3: list[float], 
        label: str = None, 
        parent: int = 0, 
        before: int = 0, 
        show: bool = True, 
        user_data: Any = None, 
        color: list[int] = (255, 255, 255, 255), 
        fill: list[int] = (0, 0, 0, -255), 
        thickness: float = 1.0, 
        **kwargs, 
    ):
        super().__init__(
            p1=p1,
            p2=p2,
            p3=p3,
            label=label,
            parent=parent,
            before=before,
            show=show,
            user_data=user_data,
            color=color,
            fill=fill,
            thickness=thickness,
            **kwargs,
        )
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.user_data = user_data
        self.color = color
        self.fill = fill
        self.thickness = thickness
