from typing import *

from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import _ElementItem, _HandlerItem

from dearpygui import _dearpygui, dearpygui

if TYPE_CHECKING:
    from dearpypixl.lib.items import (
        AppItem,
        mvStaticTexture,
        mvDynamicTexture,
        mvRawTexture,
        mvBoolValue,
        mvDoubleValue,
        mvDouble4Value,
        mvColorValue,
        mvIntValue,
        mvInt4Value,
        mvFloatValue,
        mvFloat4Value,
        mvFloatVectValue,
        mvSeriesValue,
        mvStringValue,
        mvPlotLegend,
        mvAnnotation,
        mv2dHistogramSeries,
        mvAreaSeries,
        mvBarGroupSeries,
        mvBarSeries,
        mvCandleSeries,
        mvCustomSeries,
        mvDigitalSeries,
        mvErrorSeries,
        mvHeatSeries,
        mvHistogramSeries,
        mvImageSeries,
        mvInfLineSeries,
        mvLabelSeries,
        mvLineSeries,
        mvPieSeries,
        mvScatterSeries,
        mvShadeSeries,
        mvStairSeries,
        mvStemSeries,
        mvKeyDownHandler,
        mvKeyPressHandler,
        mvKeyReleaseHandler,
        mvMouseClickHandler,
        mvMouseDoubleClickHandler,
        mvMouseDownHandler,
        mvMouseDragHandler,
        mvMouseMoveHandler,
        mvMouseReleaseHandler,
        mvMouseWheelHandler,
        mvActivatedHandler,
        mvActiveHandler,
        mvClickedHandler,
        mvDeactivatedAfterEditHandler,
        mvDeactivatedHandler,
        mvDoubleClickedHandler,
        mvEditedHandler,
        mvFocusHandler,
        mvHoverHandler,
        mvResizeHandler,
        mvScrollHandler,
        mvToggledOpenHandler,
        mvVisibleHandler,
        mvCharRemap,
        mvFontChars,
        mvFontRange,
        mvFontRangeHint,
        mvDrawArrow,
        mvDrawBezierCubic,
        mvDrawBezierQuadratic,
        mvDrawCircle,
        mvDrawEllipse,
        mvDrawImage,
        mvDrawImageQuad,
        mvDrawLine,
        mvDrawNode,
        mvDrawPolygon,
        mvDrawPolyline,
        mvDrawQuad,
        mvDrawRect,
        mvDrawText,
        mvDrawTriangle,
        mvDrawLayer,
        mvMenuItem,
    )
    from dearpypixl.lib.constants import (
        mvKey, mvMouseButton,
        mvEventType,
        mvThemeCat,
        mvThemeCol, mvPlotCol, mvNodeCol,
        mvStyleVar, mvPlotStyleVar, mvNodeStyleVar,
    )




# [ font system ]

class mvFont:
    def add_char_remap[T](self, source: int, target: int, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvCharRemap[T]:
        """Create a new char remap item as a child of this font.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvCharRemap.create(source, target, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def add_font_chars[T](self, chars: Array[int, Any], /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvFontChars[T]:
        """Create a new font characters item as a child of this font.

        :raises `SystemError`: DearPyGui-related error.

        **NOTE**: The `mvFontChars` item type and associated callables are deprecated as of Dear PyGui v2.3.
        """
        kwargs["parent"] = self
        return mvFontChars.create(chars, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def add_font_range[T](self, first_char: int, last_char: int, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvFontRange[T]:
        """Create a new font range item as a child of this font.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFontRange.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def add_font_range_hint[T](self, hint: int, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvFontRangeHint[T]:
        """Create a new font range hint item as a child of this font.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFontRangeHint.create(hint, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def get_text_size(self, text: str, /, *, wrap_width: int = -1) -> list[float]:
        """Return the width and height of *text* rendered with this font.
        Note that if called before rendering the first frame, the width
        and height returned will be zero.

        :type text: `str`
        :param text: Text to measure.

        :type wrap_width: `int` (optional)
        :param wrap_width: The maximum horizontal size of a single line of
            rendered text in pixels. Defaults to `-1`.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.get_text_size(text, wrap_width=wrap_width, font=self)  # type: ignore


class mvFontRegistry:
    __item_index_type__ = mvFont

    def add_font[T](self, file: str, size: int, /, *, pixel_snapH: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvFont[T]:
        """Create a new font item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFont.create(file, size, label=label, pixel_snapH=pixel_snapH, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)  # ty:ignore[unresolved-attribute]




# [ event handler system ]

class mvHandlerRegistry:
    __item_index_type__ = _HandlerItem

    def add_key_down_handler[T](self, key: mvKey | int = _dearpygui.mvKey_None, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvKeyDownHandler[T]:
        """Create a new key down handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvKeyDownHandler.create(key, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_key_press_handler[T](self, key: mvKey | int = _dearpygui.mvKey_None, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvKeyPressHandler[T]:
        """Create a new key pressed handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvKeyPressHandler.create(key, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_key_release_handler[T](self, key: mvKey | int = _dearpygui.mvKey_None, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvKeyReleaseHandler[T]:
        """Create a new key released handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvKeyReleaseHandler.create(key, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_click_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseClickHandler[T]:
        """Create a new mouse clicked handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseClickHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_double_click_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseDoubleClickHandler[T]:
        """Create a new mouse double clicked handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseDoubleClickHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_down_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseDownHandler[T]:
        """Create a new mouse down handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseDownHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_drag_handler[T](self, button: mvMouseButton | int = -1, threshold: float = 10.0, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseDragHandler[T]:
        """Create a new mouse drag handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseDragHandler.create(button, threshold, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_move_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseMoveHandler[T]:
        """Create a new mouse move handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseMoveHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_release_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseReleaseHandler[T]:
        """Create a new mouse released handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseReleaseHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_mouse_wheel_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvMouseWheelHandler[T]:
        """Create a new mouse wheel handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvMouseWheelHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)


class mvItemHandlerRegistry:
    __item_index_type__ = _HandlerItem

    def add_item_activated_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvActivatedHandler[T]:
        """Create a new activated handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvActivatedHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_active_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvActiveHandler[T]:
        """Create a new active handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvActiveHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_clicked_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvClickedHandler[T]:
        """Create a new clicked handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvClickedHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_deactivated_after_edit_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvDeactivatedAfterEditHandler[T]:
        """Create a new deactivated after edit handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDeactivatedAfterEditHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_deactivated_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvDeactivatedHandler[T]:
        """Create a new deactivated handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDeactivatedHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_double_clicked_handler[T](self, button: mvMouseButton | int = -1, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvDoubleClickedHandler[T]:
        """Create a new double clicked handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDoubleClickedHandler.create(button, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_edited_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvEditedHandler[T]:
        """Create a new edited handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvEditedHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_focus_handler[T](self, *, event_type: mvEventType | int | None = _dearpygui.mvEventType_On, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvFocusHandler[T]:
        """Create a new focus handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFocusHandler.create(event_type=event_type, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_hover_handler[T](self, *, event_type: mvEventType | int | None = _dearpygui.mvEventType_On, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvHoverHandler[T]:
        """Create a new hover handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvHoverHandler.create(event_type=event_type, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_resize_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvResizeHandler[T]:
        """Create a new resize handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvResizeHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_scroll_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvScrollHandler[T]:
        """Create a new scroll handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvScrollHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_toggled_open_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvToggledOpenHandler[T]:
        """Create a new toggled open handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvToggledOpenHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)

    def add_item_visible_handler[T](self, *, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: int | str = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvVisibleHandler[T]:
        """Create a new visible handler item as a child of this registry.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvVisibleHandler.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, callback=callback, show=show, **kwargs)



# [ theme system ]

class mvThemeColor:
    identify = _ElementItem.identify


class mvThemeStyle:
    identify = _ElementItem.identify


class mvThemeComponent:
    __item_index_type__ = _ElementItem

    @overload
    def add_theme_color[T](self, target: mvThemeCol | mvPlotCol | mvNodeCol | int, value: Array[int, Literal[3, 4]] = (0, 0, 0, 255), /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: T = ..., tag: Item = 0, **kwargs) -> mvThemeColor[T]: ...
    @overload
    def add_theme_color[T](self, target: mvThemeCol | mvPlotCol | mvNodeCol | int, r: int, g: int, b: int, a: int = 255, /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvThemeColor[T]: ...
    def add_theme_color(self, target, obj = (0, 0, 0, 255), g = -1, b = -1, a = 255, /, **kwargs) -> mvThemeColor:
        """Create a new theme color item as a child of this theme component

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvThemeColor.create(target, obj if g == -1 else (obj, g, b, a), **kwargs)  # ty:ignore[unresolved-attribute]

    @overload
    def add_theme_style[T](self, target: mvStyleVar | mvPlotStyleVar | mvNodeStyleVar | int, value: Array[int | float, Literal[2]] = (1.0, -1.0), /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvThemeStyle[T]: ...
    @overload
    def add_theme_style[T](self, target: mvStyleVar | mvPlotStyleVar | mvNodeStyleVar | int, x: float, y: float = -1.0, /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, **kwargs) -> mvThemeStyle[T]: ...
    def add_theme_style(self, target, obj = None, y = -1.0, /, **kwargs) -> mvThemeStyle:
        """Create a new theme style item as a child of this theme component

        :raises `SystemError`: DearPyGui-related error.
        """
        if obj is None:
            x = 1.0
        elif hasattr(obj, "__iter__"):
            x, y = obj
        kwargs["parent"] = self
        return mvThemeStyle.create(target, x, y, **kwargs)  # ty:ignore[unresolved-attribute]


class mvTheme:
    __item_index_type__ = mvThemeComponent

    def add_theme_component[T](self, item_type: type[AppItem] | int = 0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True, tag: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> mvThemeComponent[T]:
        """Create a new theme component item as a child of this theme

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvThemeComponent.create(int(item_type), label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, before=before, enabled_state=enabled_state, **kwargs)  # ty:ignore[unresolved-attribute]




# [ value system ]

class mvValueRegistry:
    def add_bool_value[T](self, /, default_value: bool = False, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvBoolValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new boolean value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvBoolValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_double_value[T](self, /, default_value: float = 0.0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvDoubleValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new double value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDoubleValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_double4_value[T](self, /, default_value: Array[float, Literal[4]] = (0.0, 0.0, 0.0, 0.0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvDouble4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length double value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDouble4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_color_value[T](self, /, default_value: Array[int, Literal[3, 4]] = (0, 0, 0, 0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvColorValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new color value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvColorValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_int_value[T](self, /, default_value: int = 0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvIntValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new int value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvIntValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_int4_value[T](self, /, default_value: Array[int, Literal[4]] = (0, 0, 0, 0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvInt4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length int value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvInt4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float_value[T](self, /, default_value: float = 0.0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloatValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new float value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFloatValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float4_value[T](self, /, default_value: Array[float, Literal[4]] = (0.0, 0.0, 0.0, 0.0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloat4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length float value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFloat4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float_vect_value[T](self, /, default_value: Array[float, Any] = (), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloatVectValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new float vector value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvFloatVectValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_series_value[T](self, /, default_value: Array[float, Any] = (), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvSeriesValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new series value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvSeriesValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_string_value[T](self, /, default_value: str = '', *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvStringValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new string value item as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvStringValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)




# [ texture system ]

class mvTextureRegistry:

    @staticmethod
    def load_image(file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, **kwargs) -> tuple[int, int, Literal[1, 2, 3, 4], mvBuffer] | None:
        """Open and read an image, returning it's width, height, number of
        channels, and image data (an instance of `mvBuffer`) as a 4-tuple.
        Returns `None` on failure.

        :type file: `str`
        :param file: A file path pointing to an image in JPEG, PNG, BMP,
            PSD, GIF, HDR, PIC, PPM, or PGM format.

        :type gamma: `float` (optional)
        :param gamma: Luminance correction scalar. A value of `1.0`
            disables correction. Defaults to `1.0`.

        :type gamma_scale_factor: `float` (optional)
        :param gamma_scale_factor: *gamma* intensity scalar. Defaults to `1.0`.

        :rtype: `tuple[int, int, Literal[1, 2, 3, 4], mvBuffer]`
        :return: The width, height, channel count, and data loaded from *file*.

        :raises `SystemError`: DearPyGui-related error.
        """
        return dearpygui.load_image(file, gamma=gamma, gamma_scale_factor=gamma_scale_factor, **kwargs)

    @staticmethod
    def save_image(file: str, width: int, height: int, data: Array[int, Any], /, *, components: Literal[1, 2, 3, 4] = 4, quality: int = 50, **kwargs) -> None:
        """Dump an image to a file.

        :type file: `str`
        :param file: Destination file path for the saved image. The file name's
            suffix/extension determines the resulting image's format. Supported
            save formats are PNG, JPEG, BMP, TGA, and HDR.

        :type width: `int`
        :param width: Horizontal size of the image in pixels.

        :type height: `int`
        :param height: Vertical size of the image in pixels.

        :type data: `Array[int | float, Any]`
        :param data: A sequence-like buffer containing the image's data to save.

        :type components: `Literal[1, 2, 3, 4]` (optional)
        :param components: Number of channels per pixel. `1` is monochrome, `2`
            is monochrome w/alpha, `3` is RGB, and `4` is RGBA. Defaults to `4`.

        :type quality: `int` (optional)
        :param quality: Image stride as a number of bytes. Only used when the
            image is saved in JPEG format. Defaults to `50`.

        :raises `SystemError`: DearPyGui-related error.
        """
        dearpygui.save_image(file, width, height, data, components=components, quality=quality, **kwargs)

    def add_static_texture[T](self, width: int, height: int, default_value: Array[int | float, Any], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvStaticTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a static texture as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvStaticTexture.create(width, height, default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)  # ty:ignore[unresolved-attribute]

    def add_dynamic_texture[T](self, width: int, height: int, default_value: Array[int | float, Any], /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvDynamicTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a dynamic texture as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDynamicTexture.create(width, height, default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)  # ty:ignore[unresolved-attribute]

    def add_raw_texture[T](self, width: int, height: int, default_value: Array[int | float, Any], /, *, format: int = _dearpygui.mvFormat_Float_rgba, label: str | None = None, user_data: T = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvRawTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a raw texture as a child of this registry

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvRawTexture.create(width, height, default_value, format=format, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)  # ty:ignore[unresolved-attribute]


class mvStaticTexture:
    @staticmethod
    def create_from_file[T](file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvStaticTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Create a texture from an image file.

        Additional keyword arguments are forwarded to the texture item type's
        constructor.

        :type file: `str`
        :param file: A file path pointing to an image in JPEG, PNG, BMP,
            PSD, GIF, HDR, PIC, PPM, or PGM format.

        :type gamma: `float` (optional)
        :param gamma: Luminance correction scalar. A value of `1.0`
            disables correction. Defaults to `1.0`.

        :type gamma_scale_factor: `float` (optional)
        :param gamma_scale_factor: *gamma* intensity scalar. Defaults to `1.0`.

        :raises `IOError`: Unable to load the file.
        :raises `SystemError`: DearPyGui-related error.
        """
        try:
            wt, ht, ch, im = dearpygui.load_image(file, gamma=gamma, gamma_scale_factor=gamma_scale_factor)
        except ValueError:
            raise IOError(f"failed to load {file!r}") from None
        return __class__.create(wt, ht, im, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent, **kwargs)

    def save(self, file: str, /, *, components: Literal[1, 2, 3, 4] = 4, quality: int = 50, **kwargs) -> None:
        """Dump the texture as an image file.

        :type file: `str`
        :param file: Destination file path for the saved image. The file name's
            suffix/extension determines the resulting image's format. Supported
            save formats are PNG, JPEG, BMP, TGA, and HDR.

        :type components: `Literal[1, 2, 3, 4]` (optional)
        :param components: Number of channels per pixel. `1` is monochrome, `2`
            is monochrome w/alpha, `3` is RGB, and `4` is RGBA. Defaults to `4`.

        :type quality: `int` (optional)
        :param quality: Image stride as a number of bytes. Only used when the
            image is saved in JPEG format. Defaults to `50`.

        :raises `SystemError`: DearPyGui-related error.
        """
        buffer = _dearpygui.get_value(self)
        if (b_size := len(buffer)) > 0 and isinstance(buffer[0], float):
            trunc  = float.__trunc__
            buffer = [trunc(buffer[i] * 255.0) for i in range(b_size)]

        config = _dearpygui.get_item_configuration(self)
        dearpygui.save_image(file, config["width"], config["height"], buffer, components=components, quality=quality, **kwargs)


class mvDynamicTexture:
    @staticmethod
    def create_from_file[T](file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvDynamicTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Create a texture from an image file.

        Additional keyword arguments are forwarded to the texture item type's
        constructor.

        :type file: `str`
        :param file: A file path pointing to an image in JPEG, PNG, BMP,
            PSD, GIF, HDR, PIC, PPM, or PGM format.

        :type gamma: `float` (optional)
        :param gamma: Luminance correction scalar. A value of `1.0`
            disables correction. Defaults to `1.0`.

        :type gamma_scale_factor: `float` (optional)
        :param gamma_scale_factor: *gamma* intensity scalar. Defaults to `1.0`.

        :raises `IOError`: Unable to load the file.
        :raises `SystemError`: DearPyGui-related error.
        """
        try:
            wt, ht, ch, im = dearpygui.load_image(file, gamma=gamma, gamma_scale_factor=gamma_scale_factor)
        except ValueError:
            raise IOError(f"failed to load {file!r}") from None
        return __class__.create(wt, ht, im, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent, **kwargs)

    def save(self, file: str, /, *, components: Literal[1, 2, 3, 4] = 4, quality: int = 50, **kwargs) -> None:
        """Dump the texture as an image file.

        :type file: `str`
        :param file: Destination file path for the saved image. The file name's
            suffix/extension determines the resulting image's format. Supported
            save formats are PNG, JPEG, BMP, TGA, and HDR.

        :type components: `Literal[1, 2, 3, 4]` (optional)
        :param components: Number of channels per pixel. `1` is monochrome, `2`
            is monochrome w/alpha, `3` is RGB, and `4` is RGBA. Defaults to `4`.

        :type quality: `int` (optional)
        :param quality: Image stride as a number of bytes. Only used when the
            image is saved in JPEG format. Defaults to `50`.

        :raises `SystemError`: DearPyGui-related error.
        """
        buffer = _dearpygui.get_value(self)
        if (b_size := len(buffer)) > 0 and isinstance(buffer[0], float):
            trunc  = float.__trunc__
            buffer = [trunc(buffer[i] * 255.0) for i in range(b_size)]

        config = _dearpygui.get_item_configuration(self)
        dearpygui.save_image(file, config["width"], config["height"], buffer, components=components, quality=quality, **kwargs)


class mvRawTexture:
    @staticmethod
    def create_from_file[T](file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, format: int = _dearpygui.mvFormat_Float_rgba, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvRawTexture[T]:  # ty:ignore[invalid-parameter-default]
        """Create a texture from an image file.

        Additional keyword arguments are forwarded to the texture item type's
        constructor.

        :type file: `str`
        :param file: A file path pointing to an image in JPEG, PNG, BMP,
            PSD, GIF, HDR, PIC, PPM, or PGM format.

        :type gamma: `float` (optional)
        :param gamma: Luminance correction scalar. A value of `1.0`
            disables correction. Defaults to `1.0`.

        :type gamma_scale_factor: `float` (optional)
        :param gamma_scale_factor: *gamma* intensity scalar. Defaults to `1.0`.

        :raises `IOError`: Unable to load the file.
        :raises `SystemError`: DearPyGui-related error.
        """
        try:
            wt, ht, ch, im = dearpygui.load_image(file, gamma=gamma, gamma_scale_factor=gamma_scale_factor)
        except ValueError:
            raise IOError(f"failed to load {file!r}") from None
        return __class__.create(wt, ht, im, format=format, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, parent=parent, **kwargs)




# [ drawing system ]

class mvViewportDrawlist:
    def add_draw_layer[T](self, /, *, perspective_divide: bool = False, depth_clipping: bool = False, cull_mode: int = 0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawLayer[T]:  # ty: ignore
        """Create a new add_draw_layer item as a child of this canvas.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawLayer.create(perspective_divide=perspective_divide, depth_clipping=depth_clipping, cull_mode=cull_mode, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)  # ty: ignore

    def add_draw_node[T](self, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawNode[T]:  # ty:ignore[invalid-type-arguments]
        """Create a new drawing node item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawNode.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)  # ty:ignore[unresolved-attribute]

    def draw_arrow[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), thickness: float = 1.0, size: int = 4, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawArrow[T]:
        """Create a new arrow item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawArrow.create(p1, p2, color=color, thickness=thickness, size=size, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_bezier_cubic[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], p3: Array[float, Literal[2]], p4: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawBezierCubic[T]:
        """Create a new bezier cubic item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawBezierCubic.create(p1, p2, p3, p4, color=color, thickness=thickness, segments=segments, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_bezier_quadratic[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], p3: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), thickness: float = 1.0, segments: int = 0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawBezierQuadratic[T]:
        """Create a new bezier quadratic item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawBezierQuadratic.create(p1, p2, p3, color=color, thickness=thickness, segments=segments, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_circle[T](self, center: Array[float, Literal[2]], radius: float, /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawCircle[T]:
        """Create a new circle item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawCircle.create(center, radius, color=color, fill=fill, thickness=thickness, segments=segments, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_ellipse[T](self, pmin: Array[float, Literal[2]], pmax: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), thickness: float = 1.0, segments: int = 32, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawEllipse[T]:
        """Create a new ellipse item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawEllipse.create(pmin, pmax, color=color, fill=fill, thickness=thickness, segments=segments, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_image[T](self, texture_tag: Item, pmin: Array[float, Literal[2]], pmax: Array[float, Literal[2]], /, *, uv_min: List[float] | Tuple[float, ...] = (0.0, 0.0), uv_max: List[float] | Tuple[float, ...] = (1.0, 1.0), color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawImage[T]:
        """Create a new image item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawImage.create(texture_tag, pmin, pmax, uv_min=uv_min, uv_max=uv_max, color=color, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_image_quad[T](self, texture_tag: Item, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], p3: Array[float, Literal[2]], p4: Array[float, Literal[2]], /, *, uv1: List[float] | Tuple[float, ...] = (0.0, 0.0), uv2: List[float] | Tuple[float, ...] = (1.0, 0.0), uv3: List[float] | Tuple[float, ...] = (1.0, 1.0), uv4: List[float] | Tuple[float, ...] = (0.0, 1.0), color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawImageQuad[T]:
        """Create a new image quad item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawImageQuad.create(texture_tag, p1, p2, p3, p4, uv1=uv1, uv2=uv2, uv3=uv3, uv4=uv4, color=color, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_line[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), thickness: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawLine[T]:
        """Create a new line item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawLine.create(p1, p2, color=color, thickness=thickness, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_polygon[T](self, points: Array[Array[float, Literal[2]], Any], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), thickness: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawPolygon[T]:
        """Create a new polygon item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawPolygon.create(points, color=color, fill=fill, thickness=thickness, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_polyline[T](self, points: Array[Array[float, Literal[2]], Any], /, *, closed: bool = False, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), thickness: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawPolyline[T]:
        """Create a new polyline item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawPolyline.create(points, closed=closed, color=color, thickness=thickness, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_quad[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], p3: Array[float, Literal[2]], p4: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), thickness: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawQuad[T]:
        """Create a new quad item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawQuad.create(p1, p2, p3, p4, color=color, fill=fill, thickness=thickness, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_rectangle[T](self, pmin: Array[float, Literal[2]], pmax: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), multicolor: bool = False, rounding: float = 0.0, thickness: float = 1.0, corner_colors: Any = None, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawRect[T]:
        """Create a new rectangle item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawRect.create(pmin, pmax, color=color, fill=fill, multicolor=multicolor, rounding=rounding, thickness=thickness, corner_colors=corner_colors, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_text[T](self, pos: Array[float, Literal[2]], text: str, /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), size: float = 10.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawText[T]:
        """Create a new text item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawText.create(pos, text, color=color, size=size, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)

    def draw_triangle[T](self, p1: Array[float, Literal[2]], p2: Array[float, Literal[2]], p3: Array[float, Literal[2]], /, *, color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), thickness: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, show: bool = True, **kwargs) -> mvDrawTriangle[T]:
        """Create a new triangle item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvDrawTriangle.create(p1, p2, p3, color=color, fill=fill, thickness=thickness, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, show=show, **kwargs)


class mvDrawlist:
    __item_index_slot__ = 2

    add_draw_layer = mvViewportDrawlist.add_draw_layer
    add_draw_node = mvViewportDrawlist.add_draw_node
    draw_arrow = mvViewportDrawlist.draw_arrow
    draw_bezier_cubic = mvViewportDrawlist.draw_bezier_cubic
    draw_bezier_quadratic = mvViewportDrawlist.draw_bezier_quadratic
    draw_circle = mvViewportDrawlist.draw_circle
    draw_ellipse = mvViewportDrawlist.draw_ellipse
    draw_image = mvViewportDrawlist.draw_image
    draw_image_quad = mvViewportDrawlist.draw_image_quad
    draw_line = mvViewportDrawlist.draw_line
    draw_polygon = mvViewportDrawlist.draw_polygon
    draw_polyline = mvViewportDrawlist.draw_polyline
    draw_quad = mvViewportDrawlist.draw_quad
    draw_rectangle = mvViewportDrawlist.draw_rectangle
    draw_text = mvViewportDrawlist.draw_text
    draw_triangle = mvViewportDrawlist.draw_triangle


class mvDrawLayer:
    __item_index_slot__ = 2

    add_draw_node = mvViewportDrawlist.add_draw_node
    draw_arrow = mvViewportDrawlist.draw_arrow
    draw_bezier_cubic = mvViewportDrawlist.draw_bezier_cubic
    draw_bezier_quadratic = mvViewportDrawlist.draw_bezier_quadratic
    draw_circle = mvViewportDrawlist.draw_circle
    draw_ellipse = mvViewportDrawlist.draw_ellipse
    draw_image = mvViewportDrawlist.draw_image
    draw_image_quad = mvViewportDrawlist.draw_image_quad
    draw_line = mvViewportDrawlist.draw_line
    draw_polygon = mvViewportDrawlist.draw_polygon
    draw_polyline = mvViewportDrawlist.draw_polyline
    draw_quad = mvViewportDrawlist.draw_quad
    draw_rectangle = mvViewportDrawlist.draw_rectangle
    draw_text = mvViewportDrawlist.draw_text
    draw_triangle = mvViewportDrawlist.draw_triangle

    def set_clip_space(self, top_left_x: float, top_left_y: float, width: float, height: float, min_depth: float, max_depth: float, /) -> None:
        """Set the point clipping area for the drawing layer. Only enabled when
        the layer's `depth_clipping` setting is `True`.

        :type top_left_x: `float`
        :param top_left_x: Pixel position of the clip region's top-left corner.

        :type top_left_y: `float`
        :param top_left_y: Pixel position of the clip region's top-right corner.

        :type width: `float`
        :param width: The clip region's horizontal size in pixels.

        :type height: `float`
        :param height: The clip region's vertical size in pixels.

        :type min_depth: `float`
        :param min_depth: Lower-bound depth clamp.

        :type max_depth: `float`
        :param max_depth: Upper-bound depth clamp.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.set_clip_space(self, top_left_x, top_left_y, width, height, min_depth, max_depth)


class mvDrawNode:
    __item_index_slot__ = 2

    add_draw_node = mvViewportDrawlist.add_draw_node
    draw_arrow = mvViewportDrawlist.draw_arrow
    draw_bezier_cubic = mvViewportDrawlist.draw_bezier_cubic
    draw_bezier_quadratic = mvViewportDrawlist.draw_bezier_quadratic
    draw_circle = mvViewportDrawlist.draw_circle
    draw_ellipse = mvViewportDrawlist.draw_ellipse
    draw_image = mvViewportDrawlist.draw_image
    draw_image_quad = mvViewportDrawlist.draw_image_quad
    draw_line = mvViewportDrawlist.draw_line
    draw_polygon = mvViewportDrawlist.draw_polygon
    draw_polyline = mvViewportDrawlist.draw_polyline
    draw_quad = mvViewportDrawlist.draw_quad
    draw_rectangle = mvViewportDrawlist.draw_rectangle
    draw_text = mvViewportDrawlist.draw_text
    draw_triangle = mvViewportDrawlist.draw_triangle

    def apply_transform(self, transform: Array[float, Literal[4]], /) -> None:
        """Apply a transformation to the drawing node. The transform
        is used to used to multiply the points of the node's children.
        If a child is another node, the matricies will concatenate.

        :type transform: `Array[float, Literal[4]]`
        :param transform: A flat 4x4 matrix that will be used in the
            transformation.
        """
        _dearpygui.apply_transform(self, transform)




# [ node system ]

class mvNodeEditor:
    def selected_nodes(self, /) -> list[Item]:
        """Return the editor's selected nodes.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.get_selected_nodes(self)  # type:ignore

    def selected_links(self, /) -> list[Item]:
        """Return the editor's selected links.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.get_selected_links(self)  # type:ignore

    def clear_selected_nodes(self, /) -> None:
        """Clear the editor's selected nodes.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.clear_selected_nodes(self)

    def clear_selected_links(self, /) -> None:
        """Clear the editor's selected links.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.clear_selected_links(self)




# [ plotting system ]

class mvPlotAxis:
    def add_2dhistogram_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, xbins: int = -1, ybins: int = -1, xmin_range: float = 0, xmax_range: float = 0, ymin_range: float = 0, ymax_range: float = 0, density: bool = False, outliers: bool = False, col_major: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mv2dHistogramSeries[T]:  # ty: ignore
        """Create a new 2dhistogram series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        mv2dHistogramSeries.create(x, y, xbins=xbins, ybins=ybins, xmin_range=xmin_range, xmax_range=xmax_range, ymin_range=ymin_range, ymax_range=ymax_range, density=density, outliers=outliers, col_major=col_major, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_area_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, fill: Array[int, Literal[3, 4]] = (0, 0, 0, -255), contribute_to_bounds: bool = True, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: int | str = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvAreaSeries[T]:
        """Create a new area series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvAreaSeries.create(x, y, fill=fill, contribute_to_bounds=contribute_to_bounds, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_bargroup_series[T](self, values: Array[float, Any], label_ids: Array[str, Any], group_size: int, /, *, group_width: float = 0.67, shift: int = 0, horizontal: bool = False, stacked: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: int | str = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvBarGroupSeries[T]:
        """Create a new bargroup series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvBarGroupSeries.create(values, label_ids, group_size, group_width=group_width, shift=shift, horizontal=horizontal, stacked=stacked, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_bar_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, weight: float = 1, horizontal: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, parent: int | str = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvBarSeries[T]:
        """Create a new bar series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvBarSeries.create(x, y, weight=weight, horizontal=horizontal, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_candle_series[T](self, dates: Array[float, Any], opens: Array[float, Any], closes: Array[float, Any], lows: Array[float, Any], highs: Array[float, Any], /, *, bull_color: Array[int, Literal[3, 4]] = (0, 255, 113, 255), bear_color: Array[int, Literal[3, 4]] = (218, 13, 79, 255), weight: float = 0.25, tooltip: bool = True, time_unit: int = 5, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvCandleSeries[T]:
        """Create a new candle series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvCandleSeries.create(dates, opens, closes, lows, highs, bull_color=bull_color, bear_color=bear_color, weight=weight, tooltip=tooltip, time_unit=time_unit, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_custom_series[T](self, x: Array[float, Any], y: Array[float, Any], channel_count: int, /, *, y1: Array[float, Any] = (), y2: Array[float, Any] = (), y3: Array[float, Any] = (), tooltip: bool = True, no_fit: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, callback: Callable | None = None, show: bool = True, **kwargs) -> mvCustomSeries[T]:  # ty: ignore
        """Create a new custom series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvCustomSeries.create(x, y, channel_count, y1=y1, y2=y2, y3=y3, tooltip=tooltip, no_fit=no_fit, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, callback=callback, show=show, **kwargs)

    def add_digital_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvDigitalSeries[T]:
        """Create a new digital series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvDigitalSeries.create(x, y, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_error_series[T](self, x: Array[float, Any], y: Array[float, Any], negative: Array[float, Any], positive: Array[float, Any], /, *, contribute_to_bounds: bool = True, horizontal: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvErrorSeries[T]:
        """Create a new error series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvErrorSeries.create(x, y, negative, positive, contribute_to_bounds=contribute_to_bounds, horizontal=horizontal, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_heat_series[T](self, x: Array[float, Any], rows: int, cols: int, /, *, scale_min: float = 0, scale_max: float = 1, bounds_min: Array[float, Any] = (0, 0), bounds_max: Array[float, Any] = (1, 1), format: str = '%0.1f', contribute_to_bounds: bool = True, col_major: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvHeatSeries[T]:
        """Create a new heat series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvHeatSeries.create(x, rows, cols, scale_min=scale_min, scale_max=scale_max, bounds_min=bounds_min, bounds_max=bounds_max, format=format, contribute_to_bounds=contribute_to_bounds, col_major=col_major, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_histogram_series[T](self, x: Array[float, Any], /, *, bins: int = -1, bar_scale: float = 1, min_range: float = 0, max_range: float = 0, cumulative: bool = False, density: bool = False, outliers: bool = True, horizontal: bool = False, contribute_to_bounds: bool = True, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvHistogramSeries[T]:
        """Create a new histogram series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvHistogramSeries.create(x, bins=bins, bar_scale=bar_scale, min_range=min_range, max_range=max_range, cumulative=cumulative, density=density, outliers=outliers, horizontal=horizontal, contribute_to_bounds=contribute_to_bounds, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_image_series[T](self, texture_tag: Item, bounds_min: Array[float, Any], bounds_max: Array[float, Any], /, *, uv_min: Array[float, Any] = (0, 0), uv_max: Array[float, Any] = (1, 1), tint_color: Array[int, Literal[3, 4]] = (255, 255, 255, 255), label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvImageSeries[T]:
        """Create a new image series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvImageSeries.create(texture_tag, bounds_min, bounds_max, uv_min=uv_min, uv_max=uv_max, tint_color=tint_color, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_infline_series[T](self, x: Array[float, Any], /, *, horizontal: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvInfLineSeries[T]:
        """Create a new infline series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvInfLineSeries.create(x, horizontal=horizontal, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_text_point[T](self, x: float, y: float, /, *, offset: Array[float, Any] = (0, 0), vertical: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvLabelSeries[T]:
        """Create a new label series item to this plot axis.

        **NOTE**: The `add_text_point()` and `add_label_series()` methods are functionally identical.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvLabelSeries.create(x, y, offset=offset, vertical=vertical, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_label_series[T](self, x: float, y: float, /, *, offset: Array[float, Any] = (0, 0), vertical: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvLabelSeries[T]:
        """Create a new label series item to this plot axis.

        **NOTE**: The `add_text_point()` and `add_label_series()` methods are functionally identical.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvLabelSeries.create(x, y, offset=offset, vertical=vertical, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_line_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, segments: bool = False, loop: bool = False, skip_nan: bool = False, no_clip: bool = False, shaded: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvLineSeries[T]:
        """Create a new line series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvLineSeries.create(x, y, segments=segments, loop=loop, skip_nan=skip_nan, no_clip=no_clip, shaded=shaded, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_pie_series[T](self, x: float, y: float, radius: float, values: Array[float, Any], labels: Array[str, Any], /, *, format: str = '%0.2f', angle: float = 90, normalize: bool = False, ignore_hidden: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvPieSeries[T]:
        """Create a new pie series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvPieSeries.create(x, y, radius, values, labels, format=format, angle=angle, normalize=normalize, ignore_hidden=ignore_hidden, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_scatter_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, no_clip: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvScatterSeries[T]:
        """Create a new scatter series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvScatterSeries.create(x, y, no_clip=no_clip, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_shade_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, y2: Array[float, Any] = (), label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvShadeSeries[T]:
        """Create a new shade series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvShadeSeries.create(x, y, y2=y2, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_stair_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, pre_step: bool = False, shaded: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvStairSeries[T]:
        """Create a new stair series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvStairSeries.create(x, y, pre_step=pre_step, shaded=shaded, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, before=before, source=source, show=show, **kwargs)

    def add_stem_series[T](self, x: Array[float, Any], y: Array[float, Any], /, *, horizontal: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, indent: int = -1, parent: int | str = 0, before: Item = 0, source: Item = 0, show: bool = True, **kwargs) -> mvStemSeries[T]:
        """Create a new stem series item to this plot axis.

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvStemSeries.create(x, y, horizontal=horizontal, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, indent=indent, parent=parent, before=before, source=source, show=show, **kwargs)

    @property
    def limits(self, /) -> list[float]:
        return _dearpygui.get_axis_limits(self)  # type: ignore
    @limits.setter
    def limits(self, value: Sequence[float] | tuple[float, float], /) -> None:
        _dearpygui.set_axis_limits(self, *value)
    @limits.deleter
    def limits(self, /) -> None:
        _dearpygui.set_axis_limits_auto(self)

    def set_pan_limits(self, vmin: float, vmax: float, /) -> None:
        """Apply pan constraints.

        :type vmin: `float`
        :param vmin:

        :type vmax: `float`
        :param vmax:

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.set_axis_limits_constraints(self, vmin, vmax)

    def reset_pan_limits(self, /) -> None:
        """Remove the axis' pan limit constraints.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.reset_axis_limits_constraints(self)

    def set_zoom_limits(self, vmin: float, vmax: float, /) -> None:
        """Apply zoom constraints.

        :type vmin: `float`
        :param vmin:

        :type vmax: `float`
        :param vmax:

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.set_axis_zoom_constraints(self, vmin, vmax)

    def reset_zoom_limits(self, /) -> None:
        """Remove the axis' zoom constraints.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.reset_axis_zoom_constraints(self)

    def set_ticks(self, label_pairs: Sequence[tuple[str, int | str]], /):
        """Update the axis' tick labels and values.

        :type label_pairs: `Sequence[tuple[str, int | str]]`
        :param label_pairs:  A sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.set_axis_ticks(self, label_pairs)

    def reset_ticks(self, /) -> None:
        """Clear explicitly set tick labels and values.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.reset_axis_ticks(self)

    def auto_fit_data(self, /) -> None:
        """Set the viewing area of the plot to the boundries of
        the visible plotted data.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.fit_axis_data(self)


class mvPlot:
    __item_index_type__ = mvPlotAxis

    def add_plot_axis[T](self, axis: int, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: Callable | None = None, show: bool = True, no_label: bool = False, no_gridlines: bool = False, no_tick_marks: bool = False, no_tick_labels: bool = False, no_initial_fit: bool = False, no_menus: bool = False, no_side_switch: bool = False, no_highlight: bool = False, opposite: bool = False, foreground_grid: bool = False, tick_format: str = '', scale: int = _dearpygui.mvPlotScale_Linear, invert: bool = False, auto_fit: bool = False, range_fit: bool = False, pan_stretch: bool = False, lock_min: bool = False, lock_max: bool = False, **kwargs) -> mvPlotAxis[T]:
        """Create a new axis item as a child of this plot

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvPlotAxis.create(axis, label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, payload_type=payload_type, drop_callback=drop_callback, show=show, no_label=no_label, no_gridlines=no_gridlines, no_tick_marks=no_tick_marks, no_tick_labels=no_tick_labels, no_initial_fit=no_initial_fit, no_menus=no_menus, no_side_switch=no_side_switch, no_highlight=no_highlight, opposite=opposite, foreground_grid=foreground_grid, tick_format=tick_format, scale=scale, invert=invert, auto_fit=auto_fit, range_fit=range_fit, pan_stretch=pan_stretch, lock_min=lock_min, lock_max=lock_max, **kwargs)  # ty:ignore[unresolved-attribute]

    def add_plot_annotation[T](self, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, before: Item = 0, source: Item = 0, show: bool = True, default_value: Any = (0, 0), offset: Array[float, Literal[2]] = (0.0, 0.0), color: Array[int, Literal[3, 4]] = (0, 0, 0, 255), clamped: bool = True, **kwargs) -> mvAnnotation[T]:
        """Create a new annotation item as a child of this plot

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvAnnotation.create(label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, before=before, source=source, show=show, default_value=default_value, offset=offset, color=color, clamped=clamped, **kwargs)

    def add_plot_legend[T](self, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, payload_type: str = '$$DPG_PAYLOAD', drop_callback: Callable | None = None, show: bool = True, location: int = _dearpygui.mvPlot_Location_East, horizontal: bool = False, sort: bool = False, outside: bool = False, no_highlight_item: bool = False, no_highlight_axis: bool = False, no_menus: bool = False, no_buttons: bool = False, **kwargs) -> mvPlotLegend[T]:  # ty: ignore
        """Create a new legend item as a child of this plot

        :raises `SystemError`: DearPyGui-related error.
        """
        kwargs["parent"] = self
        return mvPlotLegend.create(location=location, horizontal=horizontal, sort=sort, outside=outside, no_highlight_item=no_highlight_item, no_highlight_axis=no_highlight_axis, no_menus=no_menus, no_buttons=no_buttons, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, drop_callback=drop_callback, payload_type=payload_type, show=show, **kwargs)
    @property
    def query_rects(self) -> list[list[float]]:
        return _dearpygui.get_plot_query_rects(self)

    def _axis_from_index(self, index: SupportsIndex, /) -> int:
        return _dearpygui.get_item_info(self)["children"][1][index]

    def auto_fit_data(self, iaxis: SupportsIndex, /) -> None:
        """Set the viewing area of the plot to the boundries of
        an axis' visibly plotted data.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.fit_axis_data(self._axis_from_index(iaxis))

    def get_axis_limits(self, iaxis: SupportsIndex, /) -> list[float]:
        """Return the lower and upper limits of the axis.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.get_axis_limits(self._axis_from_index(iaxis))  # type: ignore

    def set_axis_limits(self, iaxis: SupportsIndex, ymin: float, ymax: float, /):
        """Set the axis' lower and upper limits.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :type ymin: `float`
        :param ymin: Lower-bound axis limit.

        :type ymax: `float`
        :param ymax: Upper-bound axis limit.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.set_axis_limits(self._axis_from_index(iaxis), ymin, ymax)

    def reset_axis_limits(self, iaxis: SupportsIndex, /):
        """Clear any set lower and upper limits.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :raises `SystemError`: DearPyGui-related error.
        """
        _dearpygui.set_axis_limits_auto(self._axis_from_index(iaxis))

    def set_axis_ticks(self, iaxis: SupportsIndex, label_pairs: Sequence[tuple[str, int | str]], /):
        """Update the axis' tick labels and values.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :type label_pairs: `Sequence[tuple[str, int | float | str]]`
        :param label_pairs: A Sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.set_axis_ticks(self._axis_from_index(iaxis), label_pairs)

    def reset_axis_ticks(self, iaxis: SupportsIndex, /):
        """Clear custom tick labels and values.

        :type iaxis: `SupportsIndex`
        :param iaxis: Position of target plot axis in child slot 1.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.reset_axis_ticks(self._axis_from_index(iaxis))




# [ table system ]

class mvTableRow:
    pass


class mvTable:
    __item_index_type__ = mvTableRow

    def index(self, item: Item, /) -> int:    # type: ignore
        """Get the position of a table row or column in the table.

        :type item: `Item`
        :param item: Identifier of a table row or column.

        :raises `ValueError`: *item* is not not parented by this container,
            or is not in the specified child slot.

        :raises `SystemError`: DearPyGui-related error.
        """
        if isinstance(item, str):
            tag = _dearpygui.get_alias_id(item)
        else:
            tag = item

        get_item_info = _dearpygui.get_item_info

        children = get_item_info(self)["children"]

        rows = children[1]
        try:
            return rows.index(tag)
        except ValueError:
            pass

        cols = [
            c for c in children[0]
            if get_item_info(c)["type"] == "myAppItemType::mvTableColumn"
        ]
        try:
            return cols.index(tag)
        except ValueError:
            pass

        raise ValueError(f"{item!r} is not a row or column parented by this table")

    def is_cell_highlighted(self, irow: int, icol: int, /) -> bool:
        """Return True if a specific cell is highlighted.

        :type irow: `int`
        :param irow: The index of the cell's row.

        :type icol: `int`
        :param icol: The index of the cell's column.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.is_table_cell_highlighted(self, irow, icol)

    def is_column_highlighted(self, icol: int, /) -> bool:
        """Return True if a specific column is highlighted.

        :type icol: `int`
        :param icol: The index of the column to query.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.is_table_column_highlighted(self, icol)

    def is_row_highlighted(self, irow: int, /) -> bool:
        """Return True if a specific row is highlighted.

        :type irow: `int`
        :param irow: The index of the row to query.

        :raises `SystemError`: DearPyGui-related error.
        """
        return _dearpygui.is_table_row_highlighted(self, irow)

    def set_cell_highlight(self, irow: int, icol: int, color: Array[int, Literal[3, 4]] | None, /) -> None:
        """Highlight or remove the highlight of a specific cell in
        the table.

        :type irow: `int`
        :param irow: The index of the cell's row.

        :type icol: `int`
        :param icol: The index of the cell's column.

        :type color: `Array[int, Literal[3, 4]] | None`
        :param color: RGB[A] value to use for the highlight. A value of `None`
            clears the current color.

        :raises `SystemError`: DearPyGui-related error.
        """
        if color is None:
            _dearpygui.unhighlight_table_cell(self, irow, icol)
        else:
            _dearpygui.highlight_table_cell(self, irow, icol, color)  # type: ignore

    def set_column_highlight(self, icol: int, color: Array[int, Literal[3, 4]] | None, /) -> None:
        """Highlight or remove the highlight of a specific column in
        the table.

        :type icol: `int`
        :param icol: The index of the column.

        :type color: `Array[int, Literal[3, 4]] | None`
        :param color: RGB[A] value to use for the highlight. A value of `None`
            clears the current color.

        :raises `SystemError`: DearPyGui-related error.
        """
        if color is None:
            _dearpygui.unhighlight_table_column(self, icol)
        else:
            _dearpygui.highlight_table_column(self, icol, color)  # type: ignore

    def set_row_highlight(self, irow: int, color: Array[int, Literal[3, 4]] | None, /) -> None:
        """Highlight or remove the highlight of a specific row in
        the table.

        :type irow: `int`
        :param irow: The index of the row.

        :type color: `Array[int, Literal[3, 4]] | None`
        :param color: RGB[A] value to use for the highlight. A value of `None`
            clears the current color.

        :raises `SystemError`: DearPyGui-related error.
        """
        if color is None:
            _dearpygui.unhighlight_table_row(self, irow)
        else:
            _dearpygui.highlight_table_row(self, irow, color)  # type: ignore

    def set_row_color(self, irow: int, color: Array[int, Literal[3, 4]] | None, /) -> None:
        """Update the background color of a row in the table.

        :type irow: `int`
        :param irow: The index of the row.

        :type color: `Array[int, Literal[3, 4]] | None`
        :param color: RGB[A] value to use for the highlight. A value of `None`
            clears the current color.

        :raises `SystemError`: DearPyGui-related error.
        """
        if color is None:
            _dearpygui.unset_table_row_color(self, irow)
        else:
            _dearpygui.set_table_row_color(self, irow, color)  # type: ignore




# [ menu system ]

class mvViewportMenuBar:
    def add_menu[T](self, /, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, indent: int = -1, before: Item = 0, show: bool = True, filter_key: str = '', drop_callback: Callable = None, payload_type: str = '$$DPG_PAYLOAD', tracked: bool = False, track_offset: float = 0.5, enabled: bool = True, **kwargs) -> mvMenu[T]:
        """Create a new menu as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvMenu.create(label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, indent=indent, before=before, show=show, filter_key=filter_key, drop_callback=drop_callback, payload_type=payload_type, tracked=tracked, track_offset=track_offset, enabled=enabled, **kwargs)  # ty:ignore[unresolved-attribute]

    def add_menu_item[T](self, /, *, default_value: bool = False, shortcut: str = '', check: bool = False, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, indent: int = -1, before: Item = 0, callback: Callable = None, show: bool = True, filter_key: str = '', drop_callback: Callable = None, payload_type: str = '$$DPG_PAYLOAD', tracked: bool = False, track_offset: float = 0.5, enabled: bool = True, **kwargs) -> mvMenuItem[T]:
        """Create a new menu item as a child of this container.

        :raises `SystemError`: DearPyGui-related error."""
        kwargs["parent"] = self
        return mvMenuItem.create(default_value=default_value, shortcut=shortcut, check=check, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, indent=indent, before=before, callback=callback, show=show, filter_key=filter_key, drop_callback=drop_callback, payload_type=payload_type, tracked=tracked, track_offset=track_offset, enabled=enabled, **kwargs)


class mvMenuBar:
    add_menu = mvViewportMenuBar.add_menu
    add_menu_item = mvViewportMenuBar.add_menu_item


class mvMenu:
    add_menu = mvViewportMenuBar.add_menu
    add_menu_item = mvViewportMenuBar.add_menu_item
