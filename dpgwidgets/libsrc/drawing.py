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
