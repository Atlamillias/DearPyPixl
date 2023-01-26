"""Theming extensions for DearPyGui."""

import collections
import dearpygui._dearpygui as dearpygui
from .appitems import mvTheme, mvThemeComponent
from .px_items import AppItemType
from .px_typing import overload, Any, ItemId
from .px_utils import classproperty
from . import _tcoloritems as color
from . import _tstyleitems as style




class pxThemeComponent(mvThemeComponent):
    def trim(self) -> None:
        """Update the values of the oldest element of the same kind, target, and category
        to that of the newest element and delete the former newer elements.

        Normally, newer elements of the same kind, target, and category are shown over older
        ones. This method eases the burden of having to update references to a newer element
        item. Additionally, it allows a user to forgo reference keeping of elements when
        they simply want to update its value periodically without needing to tunnel through
        the theme component's (sometimes duplicate) element children.
        """
        origin_elems: dict[str, dict[tuple[int, int], ItemId]] = collections.defaultdict(dict)
        for e in self.children(1):
            _cfg = dearpygui.get_item_configuration(e)
            elem_key = _cfg["target"], _cfg["category"]
            elements = origin_elems[dearpygui.get_item_info(e)["type"]]
            if elem_key in elements:
                dearpygui.set_value(elements[elem_key], dearpygui.get_value(e))
                dearpygui.delete_item(e)
            else:
                elements[elem_key] = e

    def pop_stack(self) -> None:
        super().pop_stack()
        self.trim()


class pxTheme(mvTheme):
    """A DearPyGui theme item interface that greatly simplifies the process of adding
    and updating theme elements. Good for creating themes of average complexity.

    When creating a `pxTheme` instance, two theme components are created; one for the "enabled"
    item state, and the other for the "disabled" state. The `item_type` constructor parameter
    is passed to both components. When a `pxTheme` item is pushed to the container stack, it
    also pushes one of the two theme components (*"enabled" one by default). This simplifies
    theme creation from this:
        >>> with dpg.theme() as theme:
        ...     with dpg.theme_component(dpg.mvAll):
        ...        color_item1 = dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (200, 50, 50))

    To this:
        >>> with pxTheme(dpg.mvAll) as theme:
        ...     color_item1 = dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (200, 50, 50))

    *NOTE: The default theme component hook is exposed through the `default` instance attribute.
    It can be changed by setting it explicitly, or by calling the `set_default_enabled` or
    `set_default_disabled` methods.

    The class-level, read-only properties `pxTheme.color` and `pxTheme.style` return the `color`
    and `style` modules respectively (also available in `dearpypixl.theme`). They contain
    convienience objects for creating elements that omit the need of passing the `target` and
    `category` arguments. Here's the equivelent to the above example:
        >>> with pxTheme(dpg.mvAll) as theme:
        ...     # Color element RGB(A) values can also be sent to the constructor individually,
        ...     # i.e. `theme.color.WindowBg(200, 50, 50)` or `theme.color.WindowBg(*(200, 50, 50))`.
        ...     color_item1 = theme.color.WindowBg((200, 50, 50))

    Additionally, the theme component's child elements are simplified. When adding an element
    of the same kind, target, and category as an existing element in the manner above, the
    new element item is deleted, but the old element's value is updated to match that of the new
    element. This eases the need of reference keeping element items.
        >>> with theme:
        ...     # This instance won't work correctly once the `with` statement falls
        ...     # out of scope since the item it interfaces with will be deleted.
        ...     color_item2 = theme.color.WindowBg((50, 50, 255, 150))
        ...     old_ci1_val = color_item1.value
        ...     ci2_val = color_item2.value
        >>> dpg.does_item_exist(color_item2)
        False
        >>> color_item1.value == ci2_val
        True

    NOTE: If this behavior is undesirable, consider setting the `pxTheme.tc_factory` class attribute
    to `mvThemeComponent` (default is `pxThemeComponent`).
    """
    tc_factory: type[mvThemeComponent] = pxThemeComponent

    @overload
    def __init__(self, item_type: int = 0, *, label: str = None, user_data: Any = None, use_internal_label: bool = True, tag: ItemId = 0, **kwargs) -> None: ...
    def __init__(self, item_type: int = 0, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.enabled  = self.tc_factory(item_type, parent=self, enabled_state=True)
        self.disabled = self.tc_factory(item_type, parent=self, enabled_state=False)
        self.default  = self.enabled

    @classproperty
    def color(cls) -> color:
        return color

    @classproperty
    def style(cls) -> style:
        return style

    def push_stack(self) -> None:
        super().push_stack()
        self.default.push_stack()

    def pop_stack(self) -> None:
        self.default.pop_stack()
        super().pop_stack()

    def set_default_enabled(self) -> None:
        self.default = self.enabled

    def set_default_disabled(self) -> None:
        self.default = self.disabled

    def bind(self, item: ItemId | None = None) -> None:
        """Bind an item to this theme, or set the application-level theme.

        Args:
            * item: The identifier of an item to bind. If None, this theme is
            used as the application-level theme. If 0, the application-level theme
            unset. Default is None.
        """
        if item:
            AppItemType.set_theme(item, self)
        else:
            dearpygui.bind_theme(self)

