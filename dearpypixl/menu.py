"""[EXPERIMENTAL] Tools for creating and managing menus."""
import warnings
warnings.warn(f"The {__name__!r} module and its' contents are experimental and may change without notice.")

import collections
from ._typing import (
    Any,
    Callable,
    Sequence,
    overload,
    override,
    Any,
    Item,
)
from . import _interface, api,items, color, style, events
from .api import Viewport


__all__ = [
    'close_context_menus',
    'close_context_menus_from',
    'hovered_context_menu',

    'ContextMenu',
    'ContextItem',
]




class _CtxMenuStack(collections.deque[tuple['ContextMenu', 'ContextItem | None']]):
    __slots__ = ('_lock',)

    __ctx_hregistry: items.mvHandlerRegistry

    # Each pair in the stack contains a context menu and the
    # menu item that spawned it (hovered). If the menu item
    # (2nd value) is None, the menu (1st value) is the origin
    # context menu and not a sub menu. The stack will always
    # properly hide menus as they are popped, but will not
    # display them when added.

    def __init__(self, *, maxlen: int | None = None) -> None:
        super().__init__(maxlen=maxlen)
        self._lock = api.mutex()

    def __cb_close_all(self, sender, mdown_info: tuple[int,  float]):
        '''Close all context menus when a mouse down event is
        captured while the cursor is away from them.'''
        duration = mdown_info[1]
        events.Py_DECREF(mdown_info)
        # ignore long-press/drag events
        if duration >= 0.05 or self.hovered_menu():
            return
        self.close_menus()  # disables hregistry

    def __get_ctx_hregistry(self):
        try:
            return self.__ctx_hregistry

        except AttributeError:
            hr_id = f'[{items.mvHandlerRegistry.__name__}] {__name__}'

            if api.Registry.alias_exists(hr_id):
                type(self).__ctx_hregistry = items.mvHandlerRegistry.new(hr_id)

            else:
                with items.mvHandlerRegistry.aliased(tag=hr_id, show=False) as type(self).__ctx_hregistry:
                    items.mvMouseDownHandler(callback=self.__cb_close_all)

        return self.__ctx_hregistry

    def _enable_ctx_hregistry(self):
        self.__get_ctx_hregistry().configure(show=True)

    def _disable_ctx_hregistry(self):
        self.__get_ctx_hregistry().configure(show=False)

    def hovered_menu(self):
        with self._lock:
            csr_x_pos, csr_y_pos = Viewport.mouse_pos_global()
            for ctx_branch in self:
                state = ctx_branch[0].state()
                x_pos, y_pos   = state['pos']        # type: ignore
                x_size, y_size = state['rect_size']  # type: ignore
                if (
                    (x_pos <= csr_x_pos <= x_pos + x_size)
                    and
                    (y_pos <= csr_y_pos <=  y_pos + y_size)
                ):
                    return ctx_branch
            return None

    def push_menu(self, menu: 'ContextMenu', menu_item: 'ContextItem | None' = None):
        """Push a context menu branch onto the stack."""
        with self._lock:
            self.appendleft((menu, menu_item))
            self._enable_ctx_hregistry()

    def pop_menu(self):
        """Pop the most-recent context menu branch off the stack."""
        with self._lock:
            menu = self.popleft()
            menu[0].configure(
                show=False,
                no_bring_to_front_on_focus=False,
            )
            return menu

    # TODO: trigger window `on_close` callbacks

    def close_menus_from(self, menu: 'ContextMenu', menu_item: 'ContextItem | None' = None):
        with self._lock:
            if not self:
                # `menu` is the origin and not a sub menu
                self._enable_ctx_hregistry()
                return self.appendleft((menu, None))

            # XXX: An `IndexError` here is a problem, but not the
            # stacks' problem.
            while True:
                sub_menu, owner_item = self.popleft()
                if sub_menu == menu:
                    self.appendleft((sub_menu, owner_item))
                    break
                elif owner_item != menu_item:
                    sub_menu.configure(
                        show=False,
                        no_bring_to_front_on_focus=False,
                    )

    def close_menus(self):
        with self._lock:
            self._disable_ctx_hregistry()
            for sub_menu, menu_item in self:
                sub_menu.configure(
                    show=False,
                    no_bring_to_front_on_focus=False,
                )
            self.clear()




_CTX_MENU_STACK = _CtxMenuStack()


def close_context_menus():
    """Dismiss all open context menus."""
    _CTX_MENU_STACK.close_menus()


def close_context_menus_from(menu: 'ContextMenu'):
    """Close all context menus and sub menus owned (directly
    or indirectly) by other menus.

    Args:
        * menu: Target context menu.


    If *menu* is not opened, all open context menus are
    closed.
    """
    with api.mutex():
        while _CTX_MENU_STACK:
            if _CTX_MENU_STACK[0][0] == menu:
                break
            _CTX_MENU_STACK.popleft()[0].configure(
                show=False,
                no_bring_to_front_on_focus=False,
            )


def hovered_context_menu():
    """Return the open context menu or sub menu under the
    cursor.

    The result of this function is independent of the menu's
    "hovered" state and may return a menu even when that menu's
    "hovered" state is False. This is because item children
    can "own" state over their parents. Instead, this function
    compares the explicit positions of the cursor and all open
    menus.
    """
    menu_branch = _CTX_MENU_STACK.hovered_menu()
    if menu_branch:
        return menu_branch[0]








def _get_default_deps_alias(cls: type, itp: type, component_name: str) -> str:
    "Returns the alias of a class' dependency item."
    return f'[{itp.__name__}] {cls.__name__}.{component_name}'.replace('..', '.')


def _get_default_theme_items(cls: type, component_name: str):
    "Returns a class' dependency theme item and components."
    theme_alias    = _get_default_deps_alias(cls, items.mvTheme, component_name)
    tc_color_alias = _get_default_deps_alias(
        cls, items.mvThemeComponent, f'{component_name}.color'
    ).replace('..', '.')
    tc_style_alias = _get_default_deps_alias(
        cls, items.mvThemeComponent, f'{component_name}.style'
    ).replace('..', '.')

    if api.Registry.alias_exists(theme_alias):
        theme = items.mvTheme.new(theme_alias)

        if api.Registry.alias_exists(tc_color_alias):
            tc_color = items.mvThemeComponent.new(tc_color_alias)
        else:
            tc_color = items.mvThemeComponent.aliased(tag=tc_color_alias, parent=theme)

        if api.Registry.alias_exists(tc_style_alias):
            tc_style = items.mvThemeComponent.new(tc_style_alias)
        else:
            tc_style = items.mvThemeComponent.aliased(tag=tc_style_alias, parent=theme)

    else:
        with items.mvTheme.aliased(tag=theme_alias) as theme:
            tc_color = items.mvThemeComponent.aliased(tag=tc_color_alias)
            tc_style = items.mvThemeComponent.aliased(tag=tc_style_alias)

    return theme, tc_color, tc_style


def _ensure_theme_elements(theme_component: items.mvThemeComponent, *elems: tuple[Callable, tuple[float, ...]]):
    'Creates missing theme element items of dependency items.'
    tc_alias = theme_component.alias
    with theme_component:
        for fn, elem_v in elems:
            alias = f'{tc_alias}.{fn.__name__}'
            if not api.Registry.alias_exists(alias):
                element = fn(*elem_v)
                element.alias = alias


def _fix_menu_position(menu_x_size: int, menu_y_size: int, x_pos: int, y_pos: int):
    "Adjust a menu's new position depending on the menu's size."
    # XXX: The only difference between this positioning behavior
    # and `MenuItem._cb_hovered`s behavior is that padding isn't
    # a factor here.
    _vp_cfg = Viewport.configuration()
    vp_wt = _vp_cfg['client_width']  # type: ignore
    vp_ht = _vp_cfg['client_height'] # type: ignore
    if menu_x_size > vp_wt - x_pos:
        x_pos -= menu_x_size
    if menu_y_size > vp_ht - y_pos:
        y_pos = max(0, y_pos - menu_y_size)
    return x_pos, y_pos



class ContextItem(_interface.SupportsCallback, items.mvGroup):
    """A highly-customizable implementation of `mvMenuItem` for
    vertical context menus.

    > NOTE: `ContextItem`s are **compound items**; composed of several
    other items. They may break when configured using Dear PyGui's API.
    """
    # Expect some 'excessive' block comments here. This
    # implementation is confusing at a glance, but addresses many
    # issues other implementations may have;
    #   - Dependency data is not stored onto the interface, unless
    #   it can be "handled" when missing.
    #
    #   - It acts like any other built-in interface/item. Users
    #   should not need to walk on eggshells when using them (i.e.
    #   minimal 'gacha's).
    #
    #   - Most customization (color, padding, size, etc.) is made by
    #   tweaking theme element values. The default look is inherited
    #   by the parent menu, and adjustments can be made per-item by
    #   binding it to an appropriate theme. Best part is that the
    #   menu theme can just be copied (`menu.theme.__copy__()`),
    #   set onto the menu item, and adjusted from there; zero element
    #   conflicts.

    __c_area_theme: items.mvTheme
    __spacer_theme: items.mvTheme

    @overload
    def __init__(  # type: ignore
        self,
        label: str,
        *,
        callback          : Callable | None = ...,
        user_data         : Any = ...,
        use_internal_label: bool = ...,
        width             : int = ...,
        height            : int = ...,
        indent            : int = ...,
        before            : Item = ...,
        payload_type      : str = ...,
        drag_callback     : Callable | None = ...,
        drop_callback     : Callable | None = ...,
        show              : bool = ...,
        pos               : tuple[int, int] | list[int] = ...,
        filter_key        : str = ...,
        delay_search      : bool = ...,
        tracked           : bool = ...,
        track_offset      : float = ...,
        **kwargs,
    ): ...
    def __init__(self, label: str, *, callback: Callable | None = None, **kwargs) -> None:
        super().__init__(**kwargs)

        with events.root_ihandler_registry(self):
            items.ResizeHandler(callback=self._cb_resized)

        if not self.handlers:
            with items.mvItemHandlerRegistry() as self.handlers:
                items.mvHoverHandler(callback=self._cb_hovered)

        with self:
            # The button below is the menu item's "click area".
            # The label layout is within the group further down.
            # "Why a button? Why not just an in-table selectable
            # w/`span_columns=True`?"
            #   - Buttons support more customizations w/theme elements.
            #   Do you like rounded buttons? I like rounded buttons.
            #
            #   - Customization is MUCH easier w/themes vs different
            #   config. options spread thin over several items.
            #
            # In addition, the button's user_data is used internally
            # over the "face value" group item to that it's free for
            # users to use.
            button = items.mvButton(
                width=-1,
                height=1,
                callback=self._cb_clicked,
            )
            try:
                button.theme = self.__c_area_theme
            except AttributeError:
                theme, tc_color, tc_style = _get_default_theme_items(type(self), 'click_area')
                button.theme = self.__class__.__c_area_theme = theme
                _ensure_theme_elements(
                    tc_color,
                    (color.button, (0, 0, 0, 0)),
                )

            # Two reasons for this inner group. First, the click area
            # needs to scale with the table, which is a problem since
            # tables cannot be explicitly positioned and do not support
            # states/handlers. Groups support many states/handlers,
            # with a rect calculated from its' contents.
            # The second reason is that last bit -- We ONLY want the
            # table size, so the click area and table cannot be
            # parented by the same group.
            # BUG: Updates to most relevant style elements will trigger
            # a resize event on the parenting menu. However, some do not,
            # and others only do so indirectly (if, for example, the
            # parent is auto-sized). If the parent is auto-sized, the
            # vertical component of `frame_padding` and `cell_padding`
            # won't trigger one if the result causes the parent to shrink.
            with items.mvGroup(label="[1] layout"):
                with items.mvTable(
                    header_row=False,
                    no_host_extendX=True,
                    no_keep_columns_visible=True,
                    context_menu_in_body=False,
                    sortable=False,
                    resizable=False,
                    reorderable=False,
                    scrollY=False,
                    scrollX=False,
                    no_clip=True,
                ) as table:
                    with items.mvTableRow():
                        items.mvTableColumn(label='[0] padding', width_fixed=True, parent=table, no_clip=True, no_reorder=True, no_sort=True)
                        items.mvSpacer()

                        # menu name
                        items.mvTableColumn(label='[1] label (name)', width_fixed=True, parent=table, no_clip=True, no_reorder=True, no_sort=True)
                        name_lbl = items.mvText()

                        # The "spacer" is necessary for the group to calculate its
                        # size properly. An empty, stretchy column is not enough; it
                        # needs content to consume the space.
                        items.mvTableColumn(label='[2] spacing', width_stretch=True, parent=table, no_reorder=True, no_sort=True, indent_disable=True, indent_enable=False)
                        spacer = items.mvButton(width=-1, height=1)
                        try:
                            spacer.theme = self.__spacer_theme
                        except AttributeError:
                            theme, tc_color, tc_style = _get_default_theme_items(type(self), 'spacer')
                            spacer.theme = self.__class__.__spacer_theme = theme
                            _ensure_theme_elements(
                                tc_color,
                                (color.button, (0, 0, 0, 0)),
                                (color.button_active, (0, 0, 0, 0)),
                                (color.button_hovered, (0, 0, 0, 0)),
                            )

                        # menu shortcut
                        items.mvTableColumn(label='[3] label (shortcut)', width_fixed=True, parent=table, no_reorder=True, no_sort=True)
                        shortcut_lbl = items.mvText()

                        items.mvTableColumn(label='[4] padding', width_fixed=True, parent=table, no_clip=True, no_reorder=True, no_sort=True)
                        items.mvSpacer()

        self._internal_data = (name_lbl, shortcut_lbl, None, None)
        self.configure(label=label, callback=callback)

    @property
    def root_parent(self):
        return ContextMenu.new(api.Item.root_parent(self))

    @property
    def _internal_data(self) -> tuple[items.mvText, items.mvText, 'ContextMenu | None', Callable | None]:
        # store in click_area (button)
        return api.Item.configuration(self.children(1)[0])['user_data']
    @_internal_data.setter
    def _internal_data(self, value: tuple[items.mvText, items.mvText, 'ContextMenu | None', Callable | None]):
        # XXX: The submenu is set by the menus themselves and
        # not this item.
        api.Item.configure(self.children(1)[0], user_data=value)

    def _set_submenu(self, menu: 'ContextMenu | None', ):
        name_item, shtcut_item, _, callback = self._internal_data
        self._internal_data = name_item, shtcut_item, menu, callback

    def _cb_resized(self, handler: Item = 0):
        'Triggers when the parenting root item is resized.'
        try:
            button, layout = self.children(1)
        except SystemError:
            if handler and not api.Registry.item_exists(self):
                return api.Item.destroy(handler)
            raise
        layout_state = api.Item.state(layout)
        api.Item.configure(
            button,
            pos=layout_state['pos'],
            height=layout_state['rect_size'][1],    # type: ignore
        )

    def _cb_hovered(self, *args):
        'Triggers when the click area is hovered.'
        # TODO: show cascade menu on hover (popup)
        smenu = self._internal_data[2]
        pmenu = self.root_parent

        _CTX_MENU_STACK.close_menus_from(pmenu, self)
        if smenu:
            _CTX_MENU_STACK.push_menu(smenu, self)
            if not smenu.is_visible:
                # HACK: imgui won't calculate an item's size if it hasn't
                # been rendered yet. Show it off-screen and wait a frame.
                # BUG: This is enough to force imgui to calculate the
                # the menu's inner padding, but not enough to actually
                # size the menu's content. It risks getting clipped off-
                # screen when displaying for the first time.
                smenu_x_size, smenu_y_size = smenu.state()['rect_size']  # type: ignore
                if not (smenu_x_size or smenu_y_size):
                    smenu.configure(show=True, pos=(100 + Viewport.client_width, 0))
                    api.Runtime.split_frame()
                    smenu_x_size, smenu_y_size = smenu.state()['rect_size']  # type: ignore

                _vp_cfg = Viewport.configuration()
                vp_wt = _vp_cfg['client_width']  # type: ignore
                vp_ht = _vp_cfg['client_height'] # type: ignore

                _self_state = self.state()
                self_x_min, self_y_min = _self_state['rect_min']  # type: ignore
                self_x_max, self_y_max = _self_state['rect_max']  # type: ignore

                # right/left edge of sub menu aligns with x_max/x_min of this
                # item, accounting for 50% of the parent menu's inner padding
                _wndw_padx_offset = int(
                    (pmenu.state()['rect_size'][0] - _self_state['rect_size'][0]) * 0.25  # type: ignore
                )
                if smenu_x_size < vp_wt - self_x_max:
                    new_x_pos = self_x_max + _wndw_padx_offset
                else:
                    new_x_pos = self_x_min - smenu_x_size - _wndw_padx_offset

                if smenu_y_size < vp_ht - self_y_min:
                    # y_min of the sub menu('s first item) ~aligned with
                    # y_min of this menu item
                    try:
                        new_y_pos = self_y_min - api.Item.state(  # type: ignore
                            smenu.information()['children'][1][0]
                        )['pos'][1]
                    except IndexError:
                        new_y_pos = self_y_min
                else:
                    new_y_pos = max(0, vp_ht - smenu_y_size)

                smenu.configure(show=True, pos=(new_x_pos, new_y_pos), no_bring_to_front_on_focus=False)
                pmenu.configure(no_bring_to_front_on_focus=True)

    def _cb_clicked(self):
        'Triggers when the click area is clicked.'
        callback = self._internal_data[-1]
        if callback:
            _CTX_MENU_STACK.close_menus()
            # Invokes the callback set by the user as if called by
            # DPG. This is not ideal (i.e. variadics count as 1 arg),
            # but it is the fastest (and perhaps the most expected)
            # way.
            callback(
                *(self, None, self.user_data)[:callback.__code__.co_argcount]
            )

    @override
    def configure(self, **kwargs):
        name_item, shtcut_item, sub_menu, callback = self._internal_data

        if 'label' in kwargs:
            name = kwargs['label']
            if '##' in name:
                name, shortcut = name.split('##')
            else:
                shortcut = ''

            name_item.value   = name
            shtcut_item.value = shortcut
            self._cb_resized()

        if 'callback' in kwargs:
            self._internal_data = (
                name_item,
                shtcut_item,
                sub_menu,
                kwargs.pop('callback')  # `mvGroup` does not support `callback`
            )

        super().configure(**kwargs)



# TODO: separate context menu theme & bind to class
class _ContextTheme(items.mvTheme):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class ContextMenu(items.mvWindowAppItem):
    """An extension of `mvWindowAppItem` used for creating
    and managing stylized context menus.

    The main appeal of using `ContextMenu`s over `mvMenu`s are
    their styling options. Built-in items like `mvMenu` and
    `mvMenuItem` have very rigid layouts and minimal customization.
    On the other hand, `ContextMenu` and `ContextItem` -
    `ContextMenu`s child of choice - reflect a *lot* of theme
    elements. They're influenced by theme elements to such an
    extent that the `ContextMenu` class has its' own dedicated
    global theme, and exposes elements such as `frame_rounding`
    and `item_spacing` as instance properties. Additionally, users
    have a bit more control here than they would using built-in
    menu; sub-menus can be thrown as their own root context menu,
    and the hovered/in-focus menu can be easily obtained using the
    module-level `hovered_context_menu` function. And while they
    do not perfectly emulate the of built-in menus and menu items,
    their behavior is very close.


    Typically, a "context menu" is a menu that becomes visible
    on input (right-click, etc) or state change. `ContextMenu`
    instances are intended (but not limited) to replace the role
    of `mvMenu` items for that purpose. Like windows, they cannot be
    parented. However, context-manager usage mimics the tree-like
    nesting behavor of menu items when used within the statement
    body of other `ContextMenu` context managers:
        >>> import dearpypixl as dpx
        >>> from dearpypixl.menus import *
        >>>
        >>>
        >>> with ContextMenu("RootMenu") as ctx_menu:
        ...     ContextItem("Item1")
        ...     ContextItem("Item2", callback=lambda: print('clicked Item2'))
        ...
        ...     with ContextMenu("SubMenu1") as submenu_1:
        ...         dpx.ColorPicker([225, 100, 100, 255])
        ...         ContextItem("Item3")

    The menus are hidden by default. The menu's `show` configuration
    can still be updated to display/hide it like normal. The
    `.to_position` and `.to_cursor` methods are other convenient
    ways to display them on screen; taking into account the menu's
    content so that it is not clipped. When used for their intended
    purpose, opt to use the methods over the `show` configuration
    to ensure that the menu will hide when non-context menus are
    brought into focus or vice-versa.


    As with most other interfaces, `ContextMenu` instances are not
    required to create the items they manage, allowing for normal
    window items to be selectively repurposed as context menus.
    However, updates to the following configuration options should
    be avoided while the item is managed through the interface or
    `menu` module framework:
        - `no_focus_on_appearing`
        - `no_bring_to_front_on_focus`
        - `no_collapse`
        - `modal`
        - `popup`
    """
    __theme    : items.mvTheme

    mitem_factory: type[ContextItem] = ContextItem
    cascade_arrow: str               = '\u009b'

    label: str

    @overload
    def __init__(  # type: ignore
        self,
        label                      : str = '',
        *,
        width                      : int  = -1,
        height                     : int  = -1,
        show                       : bool = False,
        autosize                   : bool = True,
        no_resize                  : bool = True,
        no_title_bar               : bool = True,
        no_move                    : bool = True,
        user_data                  : Any = ...,
        use_internal_label         : bool = ...,
        tag                        : Item = ...,
        pos                        : tuple[int, int] | list[int] = ...,
        delay_search               : bool = ...,
        min_size                   : Sequence[int] = ...,
        max_size                   : Sequence[int] = ...,
        menubar                    : bool = ...,
        no_scrollbar               : bool = ...,
        horizontal_scrollbar       : bool = ...,
        no_close                   : bool = ...,
        indent                     : int = ...,
        no_background              : bool = ...,
        no_open_over_existing_popup: bool = ...,
        no_scroll_with_mouse       : bool = ...,
        on_close                   : Callable | None = ...,
        **kwargs,
    ): ...
    def __init__(
        self,
        label                     : str = '',
        *,
        width                     : int = -1,
        height                    : int = -1,
        show                      : bool = False,
        autosize                  : bool = True,
        no_resize                 : bool = True,
        no_title_bar              : bool = True,
        no_move                   : bool = True,
        min_size                  : tuple[int, int] | Sequence[int] = (5, 5),
        # ignore these kwds from caller
        no_focus_on_appearing     : Any = ...,
        no_bring_to_front_on_focus: Any = ...,
        no_collapse               : Any = ...,
        modal                     : Any = ...,
        popup                     : Any = ...,
        **kwargs,
    ) -> None:
        super().__init__(
            no_focus_on_appearing=False,
            no_bring_to_front_on_focus=False,
            no_collapse=True,
            modal=False,
            popup=False,
        )

        if not self.handlers:
            self.handlers = items.mvItemHandlerRegistry()

        if not self.theme:
            try:
                self.theme = self.__theme
            except AttributeError:
                theme, tc_color, tc_style = _get_default_theme_items(type(self), '')
                self.theme = self.__class__.__theme = theme
                _ensure_theme_elements(
                    tc_color,
                    (color.button, (0, 0, 0, 0)),
                    (color.button_active, (29, 151, 236, 103)),
                    (color.button_hovered, (29, 151, 236, 103)),
                    (color.header, (0, 0, 0, 0)),
                    (color.header_active, (29, 151, 236, 103)),
                    (color.header_hovered, (29, 151, 236, 103)),
                    (color.window_bg, (37, 37, 38, 255)),
                )
                _ensure_theme_elements(
                    tc_style,
                    (style.item_spacing, (8, 10)),
                    (style.window_rounding, (0, -1)),
                    (style.window_rounding, (0, -1)),
                    (style.window_padding, (24, 8)),
                    (style.popup_rounding, (0, -1)),
                    (style.frame_rounding, (0, -1)),
                    (style.frame_padding, (4, 3)),
                    (style.frame_padding, (4, 3)),
                )

        self.configure(
            label=label,
            width=width,
            height=height,
            show=show,
            autosize=autosize,
            no_resize=no_resize,
            no_title_bar=no_title_bar,
            no_move=no_move,
            min_size=min_size,
            **kwargs
        )

    def _get_theme_element(self, component_name: str, element_name: str) -> Any:
        theme = self.theme
        if not theme or theme == self.__theme:
            alias = _get_default_deps_alias(
                self.__class__,
                items.ThemeComponent,
                component_name
            )
            return items.interface(f'{alias}.{element_name}')  # type: ignore
        for c in theme.children(1)[1]:  # type: ignore
            for e in api.Item.children(c, 1):
                if api.ThemeElement.identify(e) == element_name:
                    return items.interface(e)  # type: ignore
        raise ValueError(f'assigned theme has no element item {element_name!r}.')

    @property
    def button(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'button')

    @property
    def button_active(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'button_active')

    @property
    def button_hovered(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'button_hovered')

    @property
    def header(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'header')

    @property
    def header_active(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'header_active')

    @property
    def header_hovered(self) -> items.mvThemeColor:
        return self._get_theme_element('color', 'header_hovered')

    @property
    def item_spacing(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'item_spacing')

    @property
    def popup_rounding(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'popup_rounding')

    @property
    def window_bg(self) -> items.mvThemeStyle:
        return self._get_theme_element('color', 'window_bg')

    @property
    def window_padding(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'window_padding')

    @property
    def window_rounding(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'window_rounding')

    @property
    def frame_padding(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'frame_padding')

    @property
    def frame_rounding(self) -> items.mvThemeStyle:
        return self._get_theme_element('style', 'frame_rounding')

    # NOTE:'ctx' in this case refers to both the type of menu AND
    # language, as it's managed through the item's `with` statement
    # hooks. Completely independent and in no way related to
    # `_CTX_MENU_STACK`.
    __ctx_menu_stack: collections.deque[items.mvWindowAppItem] = collections.deque()

    @override
    def push_stack(self):
        stack = self.__class__.__ctx_menu_stack
        if not stack or stack[0] != self:
            stack.appendleft(self)
        return super().push_stack()

    @override
    def pop_stack(self):
        super().pop_stack()
        stack = self.__class__.__ctx_menu_stack
        if stack and stack[0] == self:
            stack.popleft()
            if stack and stack[0] != self:
                mitem = self.mitem_factory(label=self.label, parent=stack[0])
                mitem._set_submenu(self)
                self.configure()

    @overload
    def configure(self, *, label: str = ..., width: int = ..., height: int = ..., show: bool = ..., autosize: bool = ..., no_resize: bool = ..., no_title_bar: bool = ..., no_move: bool = ..., user_data: Any = ..., use_internal_label: bool = ..., tag: Item = ..., pos: tuple[int, int]|list[int] = ..., delay_search: bool = ..., min_size: Sequence[int] = ..., max_size: Sequence[int] = ..., menubar: bool = ..., no_scrollbar: bool = ..., horizontal_scrollbar: bool = ..., no_close: bool = ..., indent: int = ..., no_background: bool = ..., no_open_over_existing_popup: bool = ..., no_scroll_with_mouse: bool = ..., on_close: Callable|None = ..., **kwargs) -> None: ...  # type: ignore
    @override
    def configure(self, **kwargs):
        if 'label' in kwargs:
            label = kwargs['label']
            if not '##' in label:
                kwargs['label'] = f'{label}##{self.cascade_arrow}'

        super().configure(**kwargs)

    def to_position(self, x_pos: int, y_pos: int, *, content_aware: bool = True):
        """Close all context menus, then show this menu at the
        the given position. The menu will be brought into the
        foreground as the active window.

        Args:
            * x_pos: The menu's new horizontal position.

            * y_pos: The menu's new vertical position.

            * content_aware: If True (default), try to position the
            menu in a way that would avoid clipping its' content. If
            False, always positions the menu's top-left corner at
            the given coordinates.


        This is a no-op when the cursor is positioned over an open
        context menu.
        """
        if not _CTX_MENU_STACK.hovered_menu():
            _CTX_MENU_STACK.close_menus()
            self.configure(
                pos=(x_pos, y_pos) if not content_aware else _fix_menu_position(
                    *self.state()['rect_size'],
                    x_pos, # type: ignore
                    y_pos, # type: ignore
                ),
                show=True,
                no_bring_to_front_on_focus=False,
            )
            _CTX_MENU_STACK.push_menu(self)

    def to_cursor(self):
        """Close all context menus, then show this menu at the
        cursor's position. The menu will be brought into the
        foreground as the active window.

        This is a no-op when the cursor is positioned over an open
        context menu.
        """
        if not _CTX_MENU_STACK.hovered_menu():
            _CTX_MENU_STACK.close_menus()
            self.configure(
                pos=_fix_menu_position(
                    # BUG: Just like with `MenuItem`s on-hover behavior, this
                    # menu's size will be 0 if it has never been rendered. The
                    # menu's content is at risk of getting clipped for its'
                    # first viewing.
                    *self.state()['rect_size'],
                    *Viewport.mouse_pos_global()
                ),
                show=True,
                no_bring_to_front_on_focus=False,
            )
            _CTX_MENU_STACK.push_menu(self)
