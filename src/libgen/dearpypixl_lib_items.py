from typing import *

from dearpypixl.core.protocols import *
from dearpypixl.core.appitem import _ElementItem

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
    )
    from dearpypixl.lib.constants import (
        mvThemeCat,
        mvThemeCol, mvPlotCol, mvNodeCol,
        mvStyleVar, mvPlotStyleVar, mvNodeStyleVar,
    )




class mvThemeColor:
    identify = _ElementItem.identify


class mvThemeStyle:
    identify = _ElementItem.identify


class mvThemeComponent:
    __item_index_type__ = _ElementItem

    @overload
    def add_theme_color[T](self, target: mvThemeCol | mvPlotCol | mvNodeCol | int, value: Array[int, Literal[3, 4]] = (0, 0, 0, 255), /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: T = ..., tag: Item = 0, **kwargs) -> mvThemeColor[T]: ...
    @overload
    def add_theme_color[T](self, target: mvThemeCol | mvPlotCol | mvNodeCol | int, r: int, g: int, b: int, a: int = 255, /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: Item = 0, **kwargs) -> mvThemeColor[T]: ...
    def add_theme_color(self, target, obj = (0, 0, 0, 255), g = -1, b = -1, a = 255, /, **kwargs) -> mvThemeColor:
        """Create a new theme color item as a child of this theme component."""
        kwargs["parent"] = self
        return mvThemeColor.create(target, obj if g == -1 else (obj, g, b, a), **kwargs)

    @overload
    def add_theme_style[T](self, target: mvStyleVar | mvPlotStyleVar | mvNodeStyleVar | int, value: Array[int | float, Literal[2]] = (1.0, -1.0), /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: Item = 0, **kwargs) -> mvThemeStyle[T]: ...
    @overload
    def add_theme_style[T](self, target: mvStyleVar | mvPlotStyleVar | mvNodeStyleVar | int, x: float, y: float = -1.0, /, *, category: mvThemeCat | int = _dearpygui.mvThemeCat_Core, label: str | None = None, use_internal_label: bool = True, user_data: Any | None = None, tag: Item = 0, **kwargs) -> mvThemeStyle[T]: ...
    def add_theme_style(self, target, obj = None, y = -1.0, /, **kwargs) -> mvThemeStyle:
        """Create a new theme style item as a child of this theme component."""
        if obj is None:
            x = 1.0
        elif hasattr(obj, "__iter__"):
            x, y = obj
        kwargs["parent"] = self
        return mvThemeStyle.create(target, x, y, **kwargs)


class mvTheme:
    __item_index_type__ = mvThemeComponent

    def add_theme_component[T](self, item_type: type[AppItem] | int = 0, /, *, label: str | None = None, user_data: T = None, use_internal_label: bool = True, tag: Item = 0, before: Item = 0, enabled_state: bool = True, **kwargs) -> mvThemeComponent[T]:  # ty: ignore
        """Create a new theme component item as a child of this theme."""
        kwargs["parent"] = self
        return mvThemeComponent.create(int(item_type), label=label, user_data=user_data, use_internal_label=use_internal_label, tag=tag, before=before, enabled_state=enabled_state, **kwargs)


class mvValueRegistry:
    def add_bool_value[T](self, /, default_value: bool = False, *, label: str | None = None, use_internal_label: bool = True, user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvBoolValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new boolean value item as a child of this registry."""
        kwargs["parent"] = self
        return mvBoolValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_double_value[T](self, /, default_value: float = 0.0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvDoubleValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new double value item as a child of this registry."""
        kwargs["parent"] = self
        return mvDoubleValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_double4_value[T](self, /, default_value: Array[float, Literal[4]] = (0.0, 0.0, 0.0, 0.0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvDouble4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length double value item as a child of this registry."""
        kwargs["parent"] = self
        return mvDouble4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_color_value[T](self, /, default_value: Array[int, Literal[3, 4]] = (0, 0, 0, 0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvColorValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new color value item as a child of this registry."""
        kwargs["parent"] = self
        return mvColorValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_int_value[T](self, /, default_value: int = 0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvIntValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new int value item as a child of this registry."""
        kwargs["parent"] = self
        return mvIntValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_int4_value[T](self, /, default_value: Array[int, Literal[4]] = (0, 0, 0, 0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvInt4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length int value item as a child of this registry."""
        kwargs["parent"] = self
        return mvInt4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float_value[T](self, /, default_value: float = 0.0, *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloatValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new float value item as a child of this registry."""
        kwargs["parent"] = self
        return mvFloatValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float4_value[T](self, /, default_value: Array[float, Literal[4]] = (0.0, 0.0, 0.0, 0.0), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloat4Value[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new 4-length float value item as a child of this registry."""
        kwargs["parent"] = self
        return mvFloat4Value.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_float_vect_value[T](self, /, default_value: Array[float, Any] = (), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvFloatVectValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new float vector value item as a child of this registry."""
        kwargs["parent"] = self
        return mvFloatVectValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_series_value[T](self, /, default_value: Array[float, Any] = (), *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvSeriesValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new series value item as a child of this registry."""
        kwargs["parent"] = self
        return mvSeriesValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)

    def add_string_value[T](self, /, default_value: str = '', *, label: str | None = None, use_internal_label: bool = True,  user_data: T = None, tag: Item = 0, source: Item = 0, **kwargs) -> mvStringValue[T]:  # ty:ignore[invalid-parameter-default]
        """Creates a new string value item as a child of this registry."""
        kwargs["parent"] = self
        return mvStringValue.create(default_value=default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, source=source, **kwargs)



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

    def add_static_texture(self, width: int, height: int, default_value: Array[int | float, Any], /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvStaticTexture:
        """Creates a static texture as a child of this registry."""
        kwargs["parent"] = self
        return mvStaticTexture.create(width, height, default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def add_dynamic_texture(self, width: int, height: int, default_value: Array[int | float, Any], /, *, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvDynamicTexture:
        """Creates a dynamic texture as a child of this registry."""
        kwargs["parent"] = self
        return mvDynamicTexture.create(width, height, default_value, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)

    def add_raw_texture(self, width: int, height: int, default_value: Array[int | float, Any], /, *, format: int = _dearpygui.mvFormat_Float_rgba, label: str | None = None, user_data: Any = None, use_internal_label: bool = True, tag: Item = 0, **kwargs) -> mvRawTexture:
        """Creates a raw texture as a child of this registry."""
        kwargs["parent"] = self
        return mvRawTexture.create(width, height, default_value, format=format, label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag, **kwargs)


class mvStaticTexture:
    @staticmethod
    def create_from_file(file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: Any = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvStaticTexture:
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
    def create_from_file(file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, label: str | None = None, use_internal_label: bool = True, user_data: Any = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvDynamicTexture:
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
    def create_from_file(file: str, /, *, gamma: float = 1.0, gamma_scale_factor: float = 1.0, format: int = _dearpygui.mvFormat_Float_rgba, label: str | None = None, use_internal_label: bool = True, user_data: Any = None, tag: Item = 0, parent: Item = 0, **kwargs) -> mvRawTexture:
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


class mvDrawLayer:
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
    def apply_transform(self, transform: Array[float, Literal[4]], /) -> None:
        """Apply a transformation to the drawing node. The transform
        is used to used to multiply the points of the node's children.
        If a child is another node, the matricies will concatenate.

        :type transform: `Array[float, Literal[4]]`
        :param transform: A flat 4x4 matrix that will be used in the
            transformation.
        """
        _dearpygui.apply_transform(self, transform)


class mvFont:
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


class mvPlotAxis:
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
        _dearpygui.set_axis_limits_constraints(self, vmin, vmax)

    def reset_pan_limits(self, /) -> None:
        _dearpygui.reset_axis_limits_constraints(self)

    def set_zoom_limits(self, vmin: float, vmax: float, /) -> None:
        _dearpygui.set_axis_zoom_constraints(self, vmin, vmax)

    def reset_zoom_limits(self, /) -> None:
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
