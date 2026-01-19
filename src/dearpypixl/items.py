import typing
from typing import Any

from dearpygui import _dearpygui

from .core import appitem
from .core import parsing
from .core import protocols
from .core.protocols import Item, ItemCallback, property
from .core import itemtype
from .core.itemtype import (
    SupportsValueArray,
    SupportsCallback,
    SupportsRect,
    ChildItem,
    ContainerItem, ContainerItemT,
    RootItem,
    ChildContainerItem,
    ChildValueArrayItem,
    ChildCallbackItem,
)




def _build[T: type](cls: T, /, *, _build=appitem.build, _register=itemtype.register) -> T:
    cls = _register(_build(cls))

    info = cls.__itemtype_info__

    func = info.function
    globals()[func.__name__] = cls.create

    func = info.function2
    if func is not None:
        globals()[func.__name__] = cls.create

    return cls




# [ special ]

@_build
class mvStage[U = Any, C: itemtype.ChildItemT = Any](RootItem[U, C, None]):
    __slots__ = ()

@_build
class mvWindowAppItem[U = Any, C: itemtype.ChildItemT = Any](SupportsRect, RootItem[U, C, None]):
    __slots__ = ()

    x_scroll_max: property[float, typing.Never]  # type: ignore
    x_scroll_pos: property[float, float]  # type: ignore
    y_scroll_max: property[float, typing.Never]  # type: ignore
    y_scroll_pos: property[float, float]  # type: ignore

    @property
    def x_scroll_max(self) -> float:
        return _dearpygui.get_x_scroll_max(self)

    @property
    def x_scroll_pos(self) -> float:
        return _dearpygui.get_x_scroll(self)
    @x_scroll_pos.setter
    def x_scroll_pos(self, value: float):
        _dearpygui.set_x_scroll(self, value)

    @property
    def y_scroll_max(self) -> float:
        return _dearpygui.get_y_scroll_max(self)

    @property
    def y_scroll_pos(self) -> float:
        return _dearpygui.get_y_scroll(self)
    @y_scroll_pos.setter
    def y_scroll_pos(self, value: float):
        _dearpygui.set_y_scroll(self, value)

    @property
    def is_active(self) -> bool:  # pyright: ignore[reportIncompatibleVariableOverride]
        """[get] Return True if this window or any of its' children
        are focused."""
        return self.uuid == _dearpygui.get_active_window()

@_build
class mvChildWindow[U = Any, P: ContainerItemT = Any](
    SupportsRect,
    ChildContainerItem[U, None, P],
):
    __slots__ = ()

    x_scroll_max: property[float, typing.Never] = mvWindowAppItem.x_scroll_max  # type: ignore
    x_scroll_pos: property[float, float] = mvWindowAppItem.x_scroll_pos  # type: ignore
    y_scroll_max: property[float, typing.Never] = mvWindowAppItem.y_scroll_max  # type: ignore
    y_scroll_pos: property[float, float] = mvWindowAppItem.y_scroll_pos  # type: ignore




# [ table ]

@_build
class mvTableColumn[U = Any](ChildItem[U, None, "mvTable"]):
    __slots__ = ()
@_build
class mvTableRow[U = Any](ChildContainerItem[U, None, "mvTable"]):
    __slots__ = ()
@_build
class mvTableCell[U = Any](ChildContainerItem[U, None, mvTableRow]):
    __slots__ = ()

@_build
class mvTable[U = Any, P: ContainerItemT = Any](
    SupportsRect,
    SupportsCallback[protocols.ItemCallback2],
    ChildContainerItem[U, str | None, P, mvTableRow],
):
    __slots__ = ()

    __itemtype_indexer_type__ = mvTableRow

    if parsing.DEARPYGUI_VERSION >= (1, 9, 2):
        x_scroll_max = mvWindowAppItem.x_scroll_max
        x_scroll_pos = mvWindowAppItem.x_scroll_pos
        y_scroll_max = mvWindowAppItem.y_scroll_max
        y_scroll_pos = mvWindowAppItem.y_scroll_pos

    def __call__(self: Any, sort_spec: list[tuple[Item, typing.Literal[1, -1]]] | None = None, /) -> None: # pyright: ignore[reportIncompatibleMethodOverride]
        callback = _dearpygui.get_item_configuration(self)["callback"]
        if callback is not None:
            callback(self, sort_spec)

    __code__ = __call__.__code__

    def index(self, item: Item, /) -> int:
        if isinstance(item, str):
            tag = _dearpygui.get_alias_id(item)
        else:
            tag = item

        children = _dearpygui.get_item_info(self)["children"]

        rows = children[1]
        try:
            return rows.index(tag)
        except ValueError:
            pass

        cols = [
            c for c in children[0]
            if _dearpygui.get_item_info(c)["type"] == "myAppItemType::mvTableColumn"
        ]
        try:
            return cols.index(tag)
        except ValueError:
            pass

        raise ValueError(f"{item!r} is not a row or column parented by this table")

    def is_cell_highlighted(self, irow: int, icol: int, /) -> bool:
        """Return True if a specific cell is highlighted.

        Args:
            * irow: The index of the cell's row.

            * icol: The index of the cell's column.
        """
        return _dearpygui.is_table_cell_highlighted(self, irow, icol)

    def is_column_highlighted(self, icol: int, /) -> bool:
        """Return True if a specific column is highlighted.

        Args:
            * icol: The index of the column to query.
        """
        return _dearpygui.is_table_column_highlighted(self, icol)

    def is_row_highlighted(self, irow: int, /) -> bool:
        """Return True if a specific row is highlighted.

        Args:
            * irow: The index of the row to query.
        """
        return _dearpygui.is_table_row_highlighted(self, irow)

    def set_cell_highlight(self, irow: int, icol: int, color: protocols.RGBA | None, /):
        """Highlight or remove the highlight of a specific cell in
        the table.

        Args:
            * irow: The index of the cell's row.

            * icol: The index of the cell's column.

            * color: An RGB or RGBA color value typing.Sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_cell(self, irow, icol)
        else:
            _dearpygui.highlight_table_cell(self, irow, icol, color)  # type: ignore

    def set_column_highlight(self, icol: int, color: protocols.RGBA | None, /):
        """Highlight or remove the highlight of a specific column in
        the table.

        Args:
            * icol: The index of the column.

            * color: An RGB or RGBA color value typing.Sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_column(self, icol)
        else:
            _dearpygui.highlight_table_column(self, icol, color)  # type: ignore

    def set_row_highlight(self, irow: int, color: protocols.RGBA | None, /):
        """Highlight or remove the highlight of a specific row in
        the table.

        Args:
            * irow: The index of the row.

            * color: An RGB or RGBA color value typing.Sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_row(self, irow)
        else:
            _dearpygui.highlight_table_row(self, irow, color)  # type: ignore

    def set_row_color(self, irow: int, color: protocols.RGBA | None, /):
        """Update the background color of a row in the table.

        Args:
            * irow: The index of the row.

            * color: An RGB or RGBA color value typing.Sequence when changing or
            setting a color, or None to use the default background color.
        """
        if color is None:
            _dearpygui.unset_table_row_color(self, irow)
        else:
            _dearpygui.set_table_row_color(self, irow, color)  # type: ignore




# [ registries (& children)]

@_build
class mvThemeComponent[U = Any](itemtype.ThemeAPI, ChildContainerItem[U, None, "mvTheme", itemtype.ElementItem]):
    __slots__ = ()
    __itemtype_indexer_type__ = itemtype.ElementItem
@_build
class mvTheme[U = Any, C: mvThemeComponent = mvThemeComponent](itemtype.ThemeAPI, RootItem[U, C]):
    __slots__ = ()
    __itemtype_indexer_type__ = mvThemeComponent

@_build
class mvThemeColor[U = Any, V: int | float = float](itemtype.ThemeAPI, ChildValueArrayItem[U, V, mvThemeComponent]):
    __slots__ = ()

    def identity(self, /) -> parsing.ThemeElementInfo:
        return self.identify_element(self)

@_build
class mvThemeStyle[U = Any, V: int | float = float](itemtype.ThemeAPI, ChildValueArrayItem[U, V, mvThemeComponent]):
    __slots__ = ()

    def identity(self, /) -> parsing.ThemeElementInfo:
        return self.identify_element(self)


@_build
class mvFont[U = Any](itemtype.FontAPI, ChildContainerItem[U, None, "mvFontRegistry"]):
    __slots__ = ()
@_build
class mvFontRegistry[U = Any, C: mvFont = mvFont](itemtype.FontAPI, RootItem[U, C]):
    __slots__ = ()
    __itemtype_indexer_type__ = mvFont
@_build
class mvFontChars[U = Any](itemtype.FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()
@_build
class mvFontRange[U = Any](itemtype.FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()
@_build
class mvFontRangeHint[U = Any](itemtype.FontAPI, ChildItem[U, None, mvFont]):
    __slots__ = ()


class _HandlerDelegate:
    __slots__ = ("handler_type",)

    def __init__(self, handler_type: type, /):
        self.handler_type = handler_type

    def __get__(self, inst=None, cls=None):
        return self

    def __set_name__(self, cls, name):
        handler_type = self.handler_type
        del self.handler_type
        setattr(cls, name, self._build_method(cls, name, handler_type))

    @staticmethod
    def _build_method(cls, name, handler_type):  # pyright: ignore[reportSelfClsParameterName]
        handler_name = handler_type.__name__

        if handler_name.startswith("mvMouse"):
            def overload1(self, /, button: int = -1, *, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag : Item = 0, parent : Item = 0, show : bool = True, **kwargs): ... # pyright: ignore[reportRedeclaration]
            def overload2(self, callback: ItemCallback, /, button: int = -1, *, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag : Item = 0, parent : Item = 0, show : bool = True, **kwargs): ...  # pyright: ignore[reportRedeclaration]
            def method(self, callback = None, /, button: int = -1, *, __constructor=handler_type.create, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Any = None, show: bool = True, **kwargs): # pyright: ignore[reportRedeclaration]
                if isinstance(callback, int):
                    callback, button = None, callback

                if callback is not None:
                    return __constructor(callback=callback, key=button, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                def capture_callback(callback):
                    return __constructor(callback=callback, key=button, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                return capture_callback

        elif handler_name.startswith("mvKey"):
            def overload1(self, /, key: int = -1, *, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag : Item = 0, parent: Item = 0, show: bool = True, **kwargs): ... # pyright: ignore[reportRedeclaration]
            def overload2(self, callback: ItemCallback, /, key: int = -1, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs): ... # pyright: ignore[reportRedeclaration]
            def method(self, callback = None, /, key: int = -1, *, __constructor=handler_type.create, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Any = None, show: bool = True, **kwargs):  # pyright: ignore[reportRedeclaration]
                if isinstance(callback, int):
                    callback, key = None, callback

                if parent is None:
                    parent = self

                if callback is not None:
                    return __constructor(callback=callback, key=key, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                def capture_callback(callback):
                    return __constructor(callback=callback, key=key, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                return capture_callback
        else:
            def overload1(self, /, *, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag : Item = 0, parent: Item = 0, show: bool = True, **kwargs): ... # pyright: ignore[reportRedeclaration]
            def overload2(self, callback: ItemCallback, /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Item = 0, show: bool = True, **kwargs): ... # pyright: ignore[reportRedeclaration]
            def method(self, callback = None, /, *, __constructor=handler_type.create, label: str | None = None, user_data : Any = None, use_internal_label: bool = True, tag: Item = 0, parent: Any = None, show: bool = True, **kwargs):
                if callback is not None:
                    return __constructor(callback=callback, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                def capture_callback(callback):
                    return __constructor(callback=callback, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, show=show, parent=self)

                return capture_callback

        overload1.__annotations__["return"] = typing.Callable[[ItemCallback], handler_type]
        overload2.__annotations__["return"] = handler_type
        overload1.__name__ = overload2.__name__ = method.__name__ = name
        overload1.__qualname__ = overload2.__qualname__ = method.__qualname__ = f"{cls.__name__}.{name}"
        typing.overload(overload1)
        typing.overload(overload2)

        del cls, name, handler_type, handler_name, overload1, overload2

        return method

def _bind_handler_method(handler_type):
    return _HandlerDelegate(handler_type)


@_build
class mvKeyDownHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvKeyPressHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvKeyReleaseHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseClickHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseDoubleClickHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseDownHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseDragHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseMoveHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseReleaseHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvMouseWheelHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvHandlerRegistry[U = Any, C: itemtype.ChildItemT = itemtype.HandlerItem](RootItem[U, C]):
    __slots__ = ()
    __itemtype_indexer_type__ = itemtype.HandlerItem
    on_mouse_click = _bind_handler_method(mvMouseClickHandler)
    on_mouse_click_down = _bind_handler_method(mvMouseDownHandler)
    on_mouse_click_up = _bind_handler_method(mvMouseReleaseHandler)
    on_mouse_double_click = _bind_handler_method(mvMouseDoubleClickHandler)
    on_mouse_wheel = _bind_handler_method(mvMouseWheelHandler)
    on_mouse_move = _bind_handler_method(mvMouseMoveHandler)
    on_mouse_drag = _bind_handler_method(mvMouseDragHandler)
    on_key_down = _bind_handler_method(mvKeyDownHandler)
    on_key_press = _bind_handler_method(mvKeyPressHandler)
    on_key_up = _bind_handler_method(mvKeyReleaseHandler)


@_build
class mvActivatedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvActiveHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvClickedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvDeactivatedAfterEditHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvDeactivatedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvDoubleClickedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvEditedHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvFocusHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvHoverHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvResizeHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvToggledOpenHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvVisibleHandler[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, "mvItemHandlerRegistry", CB]):
    __slots__ = ()
@_build
class mvItemHandlerRegistry[U = Any, C: itemtype.ChildItemT = itemtype.HandlerItem](RootItem[U, C]):
    __slots__ = ()
    __itemtype_indexer_type__ = itemtype.HandlerItem
    on_resize = _bind_handler_method(mvResizeHandler)
    on_click = _bind_handler_method(mvClickedHandler)
    on_toggle_open = _bind_handler_method(mvToggledOpenHandler)
    on_edit = _bind_handler_method(mvEditedHandler)
    on_deactivation_after_edit = _bind_handler_method(mvDeactivatedAfterEditHandler)
    on_activation = _bind_handler_method(mvActivatedHandler)
    on_deactivation = _bind_handler_method(mvDeactivatedHandler)
    while_active = _bind_handler_method(mvActiveHandler)
    while_visible = _bind_handler_method(mvVisibleHandler)
    while_focused = _bind_handler_method(mvFocusHandler)
    while_hovered = _bind_handler_method(mvHoverHandler)


@_build
class mvColorMapRegistry[U = Any](RootItem[U]):
    __slots__ = ()
@_build
class mvColorButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvColorEdit[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvColorMap[U = Any](ChildItem[U, None, mvColorMapRegistry]):
    __slots__ = ()
@_build
class mvColorMapButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvColorMapScale[U = Any, P: ContainerItemT = Any](SupportsRect, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvColorMapSlider[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsCallback[CB], ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvColorPicker[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsRect, SupportsValueArray[float], SupportsCallback[CB], ChildItem[U, list[float], P]):
    __slots__ = ()

@_build
class mvValueRegistry[U = Any, C: itemtype.ChildItemT = itemtype.ChildItem](RootItem[U, C]):
    __slots__ = ()
@_build
class mvFloat4Value[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
@_build
class mvFloatValue[U = Any](ChildItem[U, float, mvValueRegistry]):
    __slots__ = ()
@_build
class mvFloatVectValue[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
@_build
class mvInt4Value[U = Any](ChildValueArrayItem[U, int, mvValueRegistry]):
    __slots__ = ()
@_build
class mvIntValue[U = Any](ChildItem[U, int, mvValueRegistry]):
    __slots__ = ()
@_build
class mvDouble4Value[U = Any](ChildValueArrayItem[U, float, mvValueRegistry]):
    __slots__ = ()
@_build
class mvDoubleValue[U = Any](ChildItem[U, float, mvValueRegistry]):
    __slots__ = ()
@_build
class mvColorValue[U = Any, V: int | float = float](ChildValueArrayItem[U, V, mvValueRegistry]):
    __slots__ = ()
@_build
class mvBoolValue[U = Any, V: bool = bool](ChildItem[U, V, mvValueRegistry]):
    __slots__ = ()

@_build
class mvTemplateRegistry[U = Any, C: itemtype.ChildItemT = Any](RootItem[U, C]):
    __slots__ = ()

@_build
class mvTextureRegistry[U = Any, C: itemtype.ChildItemT = Any](RootItem[U, C]):
    __slots__ = ()




# [ nodes ]

@_build
class mvNodeEditor[U = Any, P: ContainerItemT = Any](
    SupportsCallback[protocols.ItemCallback2 | protocols.ItemCallback3], ChildContainerItem[U, None, P, "mvNode"],
):
    __slots__ = ()

    def selected_nodes(self, /) -> list[Item]:
        """Return the editor's selected nodes."""
        return _dearpygui.get_selected_nodes(self)  # type:ignore

    def selected_links(self, /) -> list[Item]:
        """Return the editor's selected links."""
        return _dearpygui.get_selected_links(self)  # type:ignore

    def clear_selected_nodes(self, /) -> None:
        """Clear the editor's selected nodes."""
        _dearpygui.clear_selected_nodes(self)

    def clear_selected_links(self, /) -> None:
        """Clear the editor's selected links."""
        _dearpygui.clear_selected_links(self)

@_build
class mvNode[U = Any](ChildContainerItem[U, None, mvNodeEditor]):
    __slots__ = ()
@_build
class mvNodeLink[U = Any](ChildItem[U, None, mvNodeEditor]):
    __slots__ = ()
@_build
class mvNodeAttribute[U = Any](ChildContainerItem[U, None, mvNode]):
    __slots__ = ()





# [ plotting ]

@_build
class mvPlotAxis[U = Any](ChildContainerItem[U, None, "mvPlot"]):
    __slots__ = ()

    @property
    def limits(self) -> list[float]:
        return _dearpygui.get_axis_limits(self)  # pyright: ignore[reportReturnType]
    @limits.setter
    def limits(self, value: typing.Sequence[float] | tuple[float, float], /) -> None:
        _dearpygui.set_axis_limits(self, *value)
    @limits.deleter
    def limits(self) -> None:
        _dearpygui.set_axis_limits_auto(self)

    def set_pan_limits(self, /, vmin: float, vmax: float) -> None:
        _dearpygui.set_axis_limits_constraints(self, vmin, vmax)

    def reset_pan_limits(self) -> None:
        _dearpygui.reset_axis_limits_constraints(self)

    def set_zoom_limits(self, /, vmin: float, vmax: float) -> None:
        _dearpygui.set_axis_zoom_constraints(self, vmin, vmax)

    def reset_zoom_limits(self) -> None:
        _dearpygui.reset_axis_zoom_constraints(self)

    def set_ticks(self, label_pairs: typing.Sequence[tuple[str, int | str] | typing.Sequence[str | int]]):
        """Update the axis' tick labels and values.

        Args:
            * label_pairs: A typing.Sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.
        """
        return _dearpygui.set_axis_ticks(self, label_pairs)

    def reset_ticks(self):
        """Clear explicitly set tick labels and values."""
        return _dearpygui.reset_axis_ticks(self)

    def auto_fit_data(self):
        """Set the viewing area of the plot to the boundries of
        the visible plotted data.
        """
        return _dearpygui.fit_axis_data(self)

@_build
class mvPlot[U = Any, P: ContainerItemT = Any](
    SupportsRect,
    SupportsCallback,
    ChildContainerItem[U, None, P, mvPlotAxis]
):
    __slots__ = ()

    __itemtype_indexer_type__ = mvPlotAxis

    @property
    def query_rects(self) -> list[list[float]]:
        return _dearpygui.get_plot_query_rects(self)

    def index(self, axis: Item, /) -> int:
        if isinstance(axis, str):
            tag = _dearpygui.get_alias_id(axis)
        else:
            tag = axis

        return _dearpygui.get_item_info(self)["children"][1].index(tag)

    def _axis_from_index(self, index: typing.SupportsIndex) -> int:
        return _dearpygui.get_item_info(self)["children"][1][index]

    def auto_fit_data(self, iaxis: typing.SupportsIndex) -> None:
        """Set the viewing area of the plot to the boundries of
        an axis' visibly plotted data.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        return _dearpygui.fit_axis_data(self._axis_from_index(iaxis))

    def get_axis_limits(self, iaxis: typing.SupportsIndex) -> list[float]:
        """Return the lower and upper limits of the axis of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        return _dearpygui.get_axis_limits(self._axis_from_index(iaxis))  # type: ignore

    def set_axis_limits(self, iaxis: typing.SupportsIndex, ymin: float, ymax: float):
        """Set the axis' lower and upper limits of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.

            * ymin: Lower-bound axis limit.

            * ymax: Upper-bound axis limit.
        """
        _dearpygui.set_axis_limits(self._axis_from_index(iaxis), ymin, ymax)

    def reset_axis_limits(self, iaxis: typing.SupportsIndex):
        """Clear explicitly set lower and upper limits of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        _dearpygui.set_axis_limits_auto(self._axis_from_index(iaxis))

    def set_axis_ticks(self, iaxis: typing.SupportsIndex, label_pairs: typing.Sequence[tuple[str, int | str] | typing.Sequence[str | int]]):
        """Update the axis' tick labels and values of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.

            * label_pairs: A typing.Sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.
        """
        return _dearpygui.set_axis_ticks(self._axis_from_index(iaxis), label_pairs)

    def reset_axis_ticks(self, iaxis: typing.SupportsIndex):
        """Clear explicitly set tick labels and values of an axis."""
        return _dearpygui.reset_axis_ticks(self._axis_from_index(iaxis))

@_build
class mvAreaSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvBarGroupSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvBarSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvCandleSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvCustomSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildContainerItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvDigitalSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvErrorSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvHeatSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvHistogramSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mv2dHistogramSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvImageSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvInfLineSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvLabelSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvLineSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvPieSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvScatterSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvShadeSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvStairSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvStemSeries[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvPlotAxis]):
    __slots__ = ()
@_build
class mvAnnotation[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
@_build
class mvPlotLegend[U = Any](ChildItem[U, None, mvPlot]):
    __slots__ = ()




# [ drawing ]

@_build
class mvViewportDrawlist[U = Any, C: itemtype.ChildItemT = Any](itemtype.DrawingAPI, RootItem[U, C]):
    __slots__ = ()
@_build
class mvDrawlist[U = Any, P: ContainerItemT = Any](SupportsRect, SupportsCallback, itemtype.DrawingAPI, ChildContainerItem[U, P]):
    __slots__ = ()

@_build
class mvDrawLayer[U = Any, P: mvDrawlist[Any, Any] | mvViewportDrawlist[Any] | mvWindowAppItem[Any] = Any](
    itemtype.DrawingAPI, ChildContainerItem[U, None, P]
):
    __slots__ = ()

    def set_clip_space(self, top_left_x : float, top_left_y : float, width : float, height : float, min_depth : float, max_depth : float) -> None:
        """Set the point clipping area for the drawing layer.

        Only enabled when the layer's "depth_clipping" setting is
        True.

        Args:
            * top_left_x: Pixel position of the clip region's top-left corner.

            * top_left_y: Pixel position of the clip region's top-right corner.

            * width: The clip region's horizontal size in non-fractional
            pixels. Note that this value is interpreted as unsigned by Dear
            PyGui's parser.

            * height: The clip region's vertical size in non-fractional pixels.
            Note that this value is interpreted as unsigned by Dear PyGui's
            parser.

            * min_depth: Lower-bound depth clamp.

            * max_depth: Upper-bound depth clamp.
        """
        _dearpygui.set_clip_space(self, top_left_x, top_left_y, width, height, min_depth, max_depth)

type _DrawParents = mvDrawlist[Any, Any] | mvViewportDrawlist[Any] | mvWindowAppItem[Any] | mvDrawLayer[Any, Any] | mvDrawNode[Any, Any]

@_build
class mvDrawNode[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildContainerItem[U, None, P]):
    __slots__ = ()

    def apply_transform(self, transform: protocols.Vec4[float]) -> None:
        """Apply a transformation to the drawing node.

        Args:
            * transform: A flat 4x4 matrix that will be used in the
            transformation.

        *transform* will be used to multiply the points of the node's
        children. If a child is another node, the matricies will
        concatenate.
        """
        _dearpygui.apply_transform(self, transform)

@_build
class mvDrawArrow[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawBezierCubic[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawBezierQuadratic[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawCircle[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawEllipse[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawImage[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawImageQuad[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawLine[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawPolygon[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawPolyline[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawQuad[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawRect[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawText[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvDrawTriangle[U = Any, P: _DrawParents = Any](itemtype.DrawingAPI, ChildItem[U, None, P]):
    __slots__ = ()




# [ misc ]

@_build
class mvDatePicker[U = Any, P: ContainerItemT = Any](
    ChildItem[U, dict[typing.Literal["sec", "min", "hour", "month_day", "month", "year", "week_day", "year_day", "daylight_savings"], int], P]
):
    __slots__ = ()
@_build
class mvAxisTag[U = Any](ChildItem[U, float, mvPlotAxis]):
    __slots__ = ()
@_build
class mvButton[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsCallback[CB], ChildItem[U, bool, P]):
    __slots__ = ()
@_build
class mvCharRemap[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvCheckbox[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
@_build
class mvClipper[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P]):
    __slots__ = ()
@_build
class mvCollapsingHeader[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool,]):
    __slots__ = ()
@_build
class mvCombo[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, str, P]):
    __slots__ = ()
@_build
class mvDragDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvDragDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvDragFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvDragFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvDragInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
@_build
class mvDragIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
@_build
class mvDragLine[U = Any](ChildItem[U, float, mvPlot]):
    __slots__ = ()
@_build
class mvDragPayload[U = Any, P: appitem.AppItem[Any, Any, Any] = Any](ChildContainerItem[U, None, P]):  # pyright: ignore[reportInvalidTypeArguments]
    __slots__ = ()
@_build
class mvDragPoint[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
@_build
class mvDragRect[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvPlot]):
    __slots__ = ()
@_build
class mvDynamicTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
@_build
class mvFileDialog[U = Any, C: itemtype.ChildItemT = Any](RootItem[U, C, bool]):
    __slots__ = ()
@_build
class mvFileExtension[U = Any](ChildItem[U, None, mvFileDialog]):
    __slots__ = ()
@_build
class mvFilterSet[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, str, P]):
    __slots__ = ()
@_build
class mvGroup[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P]):
    __slots__ = ()
@_build
class mvImage[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvImageButton[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvInputDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvInputDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvInputFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvInputFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvInputInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
@_build
class mvInputIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
@_build
class mvInputText[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
@_build
class mvKnobFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvListbox[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
@_build
class mvLoadingIndicator[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvMenu[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P]):
    __slots__ = ()
@_build
class mvMenuBar[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool, P]):
    __slots__ = ()
@_build
class mvMenuItem[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
@_build
class mvProgressBar[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvRadioButton[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
@_build
class mvRawTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
@_build
class mvSelectable[U = Any, P: ContainerItemT = Any](ChildItem[U, bool, P]):
    __slots__ = ()
@_build
class mvSeparator[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvSeriesValue[U = Any, V: int | float = float](SupportsValueArray[V], ChildItem[U, list[V], mvValueRegistry]):
    __slots__ = ()
@_build
class mvSimplePlot[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvSlider3D[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvSliderDouble[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvSliderDoubleMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvSliderFloat[U = Any, P: ContainerItemT = Any](ChildItem[U, float, P]):
    __slots__ = ()
@_build
class mvSliderFloatMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[float], ChildItem[U, list[float], P]):
    __slots__ = ()
@_build
class mvSliderInt[U = Any, P: ContainerItemT = Any](ChildItem[U, int, P]):
    __slots__ = ()
@_build
class mvSliderIntMulti[U = Any, P: ContainerItemT = Any](SupportsValueArray[int], ChildItem[U, list[int], P]):
    __slots__ = ()
@_build
class mvSpacer[U = Any, P: ContainerItemT = Any](ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvStaticTexture[U = Any](SupportsValueArray[float], ChildItem[U, list[float], mvTextureRegistry]):
    __slots__ = ()
@_build
class mvStringValue[U = Any](ChildItem[U, str, mvValueRegistry]):
    __slots__ = ()
@_build
class mvSubPlots[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, None, P]):
    __slots__ = ()
@_build
class mvTabBar[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, int, P]):
    __slots__ = ()
@_build
class mvTab[U = Any](ChildContainerItem[U, bool, mvTabBar]):
    __slots__ = ()
@_build
class mvTabButton[U = Any](ChildItem[U, None, mvTabBar]):
    __slots__ = ()
@_build
class mvText[U = Any, P: ContainerItemT = Any](ChildItem[U, str, P]):
    __slots__ = ()
@_build
class mvTimePicker[U = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](SupportsCallback[CB], ChildItem[U, None, P]):
    __slots__ = ()
@_build
class mvTooltip[U = Any, P: appitem.AppItem[Any, Any, Any] = Any](ChildContainerItem[U, None, P]):  # pyright: ignore[reportInvalidTypeArguments]
    __slots__ = ()
@_build
class mvTreeNode[U = Any, P: ContainerItemT = Any](ChildContainerItem[U, bool, P]):
    __slots__ = ()
@_build
class mvViewportMenuBar[U = Any, C: itemtype.ChildItemT = Any](RootItem[U, C]):
    __slots__ = ()
