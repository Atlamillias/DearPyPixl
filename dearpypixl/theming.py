"""Theming extensions for DearPyGui."""

import collections
import contextlib
from dearpygui import dearpygui, _dearpygui
from .px_items import AppItemType
from .px_typing import overload, Any, ItemId, Self, Sequence
from .px_theme import pxThemeColor, pxThemeStyle
from . import appitems, px_utils
from . import _tcoloritems as color
from . import _tstyleitems as style


__all__ = [
    "color",
    "style",
    "pxTheme",
]




class _ThemeColor(pxThemeColor):
    def __init__(self, target: int, category: int, value: Sequence[int | float], **kwargs) -> None:
        self.target   = target
        self.category = category
        super().__init__(*value, **kwargs)

class _ThemeStyle(pxThemeStyle):
    def __init__(self, target: int, category: int, value: Sequence[int | float], **kwargs) -> None:
        self.target   = target
        self.category = category
        super().__init__(*value, **kwargs)

_TPSTR_TO_ITP = {
    _ThemeColor.identity[1]: _ThemeColor,
    _ThemeStyle.identity[1]: _ThemeStyle,
}

def _trim_comp_elements(element_items: Sequence[ItemId]) -> None:
    origin_elems: dict[str, dict[tuple[int, int], ItemId]] = collections.defaultdict(dict)
    for e in element_items:
        _cfg = px_utils.get_config(e)
        elem_key = _cfg["target"], _cfg["category"]
        elements = origin_elems[px_utils.get_info(e)["type"]]
        if elem_key in elements:
            px_utils.set_value(elements[elem_key], px_utils.get_value(e))
            _dearpygui.delete_item(e)
        else:
            elements[elem_key] = e


class pxTheme(appitems.mvTheme):
    """A DearPyGui theme item interface that automatically manages theme components. It greatly
    simplifies the process of adding and updating theme elements.

    Basic usage will simplify this:
        >>> with dpg.theme() as theme:
        ...     with dpg.theme_component(dpg.mvAll):
        ...        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (200, 50, 50))
    To this:
        >>> with pxTheme(dpg.mvAll) as theme:
        ...     dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (200, 50, 50))

    The constructor accepts an arbitrary number of item types. These values can be any value that
    would be accepted by `dpg.add_theme_component` as the *item_type* argument, in addition to any
    usable `AppItemType` subclass. `dpg.mvAll` is used as a fallback if no values are passed.

    Two theme components are made for each item type value passed to the constructor; an "enabled state"
    component and a "disabled state" component. When creating theme elements in a `with` statement using
    a `pxTheme`, the underlying theme components will be updated with new theme elements to match. Which
    components are updated depends on the value of the instance's `default_state` value; `True` (default)
    would mean that "enabled state" components are updated, and vice-versa. You can update components
    of a specific state without changine the `default_state` attribute by using the `.enabled_state` and
    `.disabled_state` context manager instance methods.

    Each theme component managed by the instance will never parent more than one element of the same
    target and category. Instead, the newest element is deleted and oldest element's value is updated
    accordingly.

    The class-level read-only properties `.color` and `.style` return the `color` and `style` modules
    respectively (available in `dearpypixl.theme`). The objects in these modules wrap DearPyGui's
    `add_theme_color` and `add_theme_style` functions to automatically include `target` and `category`
    arguments. The user only needs to include the color/style value(s).

    Here's the equivelent to the initial above example:
        >>> with pxTheme(dpg.mvAll) as theme:
        ...     theme.color.WindowBg((200, 50, 50))  # *(200, 50, 50) would also work!

    NOTE: It's worth mentioning that the constructors aren't picky about how you send the values -- as
    sequence as `(200, 50, 50)` or individually as `200, 50, 50` is fine.
    """

    _components: dict[bool, tuple[ItemId, frozenset[ItemId]]]

    @overload
    def __init__(self, *item_types: int | type[AppItemType], default_state: bool = True, label: str = None, user_data: Any = None, use_internal_label: bool = True, tag: ItemId = 0, **kwargs) -> None: ...
    def __init__(self, *item_types: int | type[AppItemType], default_state: bool = True, **kwargs) -> None:
        super().__init__(**kwargs)
        self.default_state = default_state

        self._components = {True: [], False: []}
        itp_constants  = []
        for tp in set(item_types) if item_types else set((0,)):
            tp = int(tp)  # AppItemType -> tp const
            self._components[True ].append(dearpygui.add_theme_component(tp, parent=self, enabled_state=True))
            self._components[False].append(dearpygui.add_theme_component(tp, parent=self, enabled_state=False))
            itp_constants.append(tp)
        # Set aside a component of each state to operate on later. They will parent "original"
        # theme elements created by the user. This helps prevent references made to elements in
        # ctx from dying once closed -- a side effect from deleting the original elements and
        # replacing with copies only. All other components are updated with copy elements.
        self._components[True ] = self._components[True ].pop(0), frozenset(self._components[True ])
        self._components[False] = self._components[False].pop(0), frozenset(self._components[False])

    __ctx_comp : ItemId
    __ctx_elems: frozenset[int]
    __ctx_state: bool

    def __enter__(self) -> Self:
        """Updates enabled/disabled state theme components based on theme elements created
        in-context.

        Updates to the `.default_state` attribute while in-context are internally ignored.
        """
        self.__ctx_state = self.default_state
        self.__ctx_comp  = self._components[self.__ctx_state][0]
        self.__ctx_elems = frozenset(px_utils.get_info(self.__ctx_comp)["children"][1])
        dearpygui.push_container_stack(self.__ctx_comp)
        return self

    def __exit__(self, *args) -> None:
        if dearpygui.top_container_stack() == self.__ctx_comp:
            dearpygui.pop_container_stack()

        tgt_elements = px_utils.get_info(self.__ctx_comp)["children"][1]
        new_elements = (e for e in tgt_elements if e not in self.__ctx_elems)
        new_elem_cfg = []
        # cache element metadata to avoid recursive getter calls later
        for element in new_elements:
            _cfg = px_utils.get_config(element)
            new_elem_cfg.append(
                (
                    px_utils.get_info(element)["type"],
                    _cfg["target"],
                    _cfg["category"],
                    px_utils.get_value(element)
                )
            )
        _trim_comp_elements(tgt_elements)
        for comp in self._components[self.__ctx_state][1]:
            for tp_str, target, category, value in new_elem_cfg:
                itp = _TPSTR_TO_ITP[tp_str]
                itp(target, category, value, parent=comp)
            _trim_comp_elements(px_utils.get_info(comp)["children"][1])
        del self.__ctx_comp, self.__ctx_state, self.__ctx_elems

    @contextlib.contextmanager
    def enabled_state(self):
        """Context manager instance method for updating "enabled state" theme components.

        Upon opening the context manager, the `.default_state` attribute is set to `True`.
        It is restored to the prior state when the context manager closes.

        Updates to the `.default_state` attribute while in-context are internally ignored.
        """
        try:
            prev_state = self.default_state
            self.default_state = True
            yield self.__enter__()
        finally:
            self.__exit__()
            self.default_state = prev_state

    @contextlib.contextmanager
    def disabled_state(self):
        """Context manager instance method for updating "disabled state" theme components.

        Upon opening the context manager, the `.default_state` attribute is set to `False`.
        It is restored to the prior state when the context manager closes.

        Updates to the `.default_state` attribute while in-context are internally ignored.
        """
        try:
            prev_state = self.default_state
            self.default_state = False
            yield self.__enter__()
        finally:
            self.__exit__()
            self.default_state = prev_state

    @px_utils.classproperty
    def color(cls) -> color:
        """Module containing wrappers that create specific DearPyGui theme colors."""
        return color

    @px_utils.classproperty
    def style(cls) -> style:
        """Module containing wrappers that create specific DearPyGui theme styles."""
        return style

    def bind(self, item: ItemId | None = None) -> None:
        """Bind an item to this theme, or set the application-level theme.

        Args:
            * item: The identifier of an item to bind. If None, this theme is
            used as the application-level theme. If 0, the application-level theme
            unset. Default is None.
        """
        # set item-level theme
        if item:
            AppItemType.set_theme(item, self)
        # set application-level theme to internal DPG/IMGUI default
        elif item == 0:
            dearpygui.bind_theme(0)
        # set as application-level theme
        else:
            dearpygui.bind_theme(self)

